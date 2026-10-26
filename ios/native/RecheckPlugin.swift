import Foundation
import Capacitor
import UserNotifications

/// Local recheck reminders for a patient profile ("Recheck Bella's eye at 8:00"). Scheduled on the
/// device with UNUserNotificationCenter; no server and no push. Tapping one opens that patient
/// through FieldRouter (userInfo["route"] = "patient:<id>").
///
/// JS: Recheck.permission() -> { status }       ("granted" | "denied" | "prompt")
///     Recheck.request() -> { granted }
///     Recheck.schedule({ id, at, title, body, route }) -> { id, at }   (at = ms since 1970)
///     Recheck.cancel({ id })
///     Recheck.pending() -> { reminders: [{ id, at, title, body, route }] }
@objc(RecheckPlugin)
public class RecheckPlugin: CAPPlugin, CAPBridgedPlugin {
    public let identifier = "RecheckPlugin"
    public let jsName = "Recheck"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "permission", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "request", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "schedule", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "cancel", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "pending", returnType: CAPPluginReturnPromise)
    ]
    private let prefix = "smv.recheck."

    @objc func permission(_ call: CAPPluginCall) {
        UNUserNotificationCenter.current().getNotificationSettings { s in
            let status: String
            switch s.authorizationStatus {
            case .authorized, .provisional, .ephemeral: status = "granted"
            case .denied: status = "denied"
            default: status = "prompt"
            }
            call.resolve(["status": status])
        }
    }

    @objc func request(_ call: CAPPluginCall) {
        UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
            call.resolve(["granted": granted])
        }
    }

    @objc func schedule(_ call: CAPPluginCall) {
        guard let id = call.getString("id"), !id.isEmpty,
              let at = call.getDouble("at") else {
            call.reject("id and at are required")
            return
        }
        let date = Date(timeIntervalSince1970: at / 1000)
        guard date.timeIntervalSinceNow > 30 else {
            call.reject("Pick a time in the future")
            return
        }
        let content = UNMutableNotificationContent()
        content.title = String((call.getString("title") ?? "Recheck").prefix(120))
        content.body = String((call.getString("body") ?? "").prefix(400))
        content.sound = .default
        content.userInfo = ["route": call.getString("route") ?? "patients", "at": at]
        content.threadIdentifier = "recheck"
        let comps = Calendar.current.dateComponents([.year, .month, .day, .hour, .minute], from: date)
        let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: false)
        let req = UNNotificationRequest(identifier: prefix + id, content: content, trigger: trigger)
        UNUserNotificationCenter.current().add(req) { error in
            if let error = error {
                call.reject("Could not schedule: \(error.localizedDescription)")
            } else {
                call.resolve(["id": id, "at": at])
            }
        }
    }

    @objc func cancel(_ call: CAPPluginCall) {
        guard let id = call.getString("id"), !id.isEmpty else {
            call.reject("id is required")
            return
        }
        UNUserNotificationCenter.current().removePendingNotificationRequests(withIdentifiers: [prefix + id])
        call.resolve()
    }

    @objc func pending(_ call: CAPPluginCall) {
        let prefix = self.prefix
        UNUserNotificationCenter.current().getPendingNotificationRequests { reqs in
            let list: [[String: Any]] = reqs.filter { $0.identifier.hasPrefix(prefix) }.map { r -> [String: Any] in
                let at = (r.content.userInfo["at"] as? Double)
                    ?? ((r.trigger as? UNCalendarNotificationTrigger)?.nextTriggerDate()?.timeIntervalSince1970 ?? 0) * 1000
                return [
                    "id": String(r.identifier.dropFirst(prefix.count)),
                    "at": at,
                    "title": r.content.title,
                    "body": r.content.body,
                    "route": (r.content.userInfo["route"] as? String) ?? ""
                ]
            }
            call.resolve(["reminders": list])
        }
    }
}
