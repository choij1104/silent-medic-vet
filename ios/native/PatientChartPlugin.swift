import Foundation
import Capacitor

/// Keeps the owner's or clinician's own animal profiles (name or tag, species, a weight they noted,
/// free notes and a dated observation log) in one JSON file inside the app's Application Support
/// folder, protected by iOS Data Protection. Nothing is computed from the weight; it is a note.
/// No network, no sharing between apps.
///
/// JS: PatientChart.list() -> { patients: [...] }
///     PatientChart.save({ patient }) -> { patients }
///     PatientChart.remove({ id }) -> { patients }
@objc(PatientChartPlugin)
public class PatientChartPlugin: CAPPlugin, CAPBridgedPlugin {
    public let identifier = "PatientChartPlugin"
    public let jsName = "PatientChart"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "list", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "save", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "remove", returnType: CAPPluginReturnPromise)
    ]
    private let maxPatients = 300
    private let queue = DispatchQueue(label: "com.hakoya.silentmedicvet.patients")

    private var fileURL: URL? {
        guard let base = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first else { return nil }
        let dir = base.appendingPathComponent("PatientChart", isDirectory: true)
        if !FileManager.default.fileExists(atPath: dir.path) {
            try? FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
        }
        return dir.appendingPathComponent("patients.json")
    }

    private func readAll() -> [[String: Any]] {
        guard let url = fileURL, let data = try? Data(contentsOf: url),
              let arr = (try? JSONSerialization.jsonObject(with: data)) as? [[String: Any]] else { return [] }
        return arr
    }

    private func write(_ patients: [[String: Any]]) throws {
        guard let url = fileURL else { throw NSError(domain: "PatientChart", code: 1) }
        let data = try JSONSerialization.data(withJSONObject: patients, options: [])
        try data.write(to: url, options: [.atomic, .completeFileProtectionUntilFirstUserAuthentication])
    }

    @objc func list(_ call: CAPPluginCall) {
        queue.async {
            call.resolve(["patients": self.readAll()])
        }
    }

    @objc func save(_ call: CAPPluginCall) {
        guard let patient = call.getObject("patient"),
              let id = patient["id"] as? String, !id.isEmpty, id.count <= 64,
              JSONSerialization.isValidJSONObject(patient) else {
            call.reject("A patient with an id is required")
            return
        }
        let record: [String: Any] = patient
        queue.async {
            var all = self.readAll()
            if let i = all.firstIndex(where: { ($0["id"] as? String) == id }) {
                all[i] = record
            } else {
                if all.count >= self.maxPatients {
                    call.reject("Patient list is full (\(self.maxPatients)). Delete one first.")
                    return
                }
                all.append(record)
            }
            do {
                try self.write(all)
                call.resolve(["patients": all])
            } catch {
                call.reject("Could not save: \(error.localizedDescription)")
            }
        }
    }

    @objc func remove(_ call: CAPPluginCall) {
        guard let id = call.getString("id"), !id.isEmpty else {
            call.reject("id is required")
            return
        }
        queue.async {
            let all = self.readAll().filter { ($0["id"] as? String) != id }
            do {
                try self.write(all)
                call.resolve(["patients": all])
            } catch {
                call.reject("Could not delete: \(error.localizedDescription)")
            }
        }
    }
}
