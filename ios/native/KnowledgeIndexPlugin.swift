import Foundation
import Capacitor
import CoreSpotlight
import UniformTypeIdentifiers

/// Puts the reference entries and condition cards into the iPhone's own Spotlight index, so typing
/// "carprofen" or "glaucoma" on the Home Screen offers the Silent Medic Vet card directly. Indexing
/// happens on the device; nothing is sent anywhere. Each item's identifier is a FieldRouter route
/// ("kb:12", "cond:eye-glaucoma"), which FieldRouter.accept() hands back to the app when tapped.
///
/// JS: KnowledgeIndex.index({ stamp, items: [{ id, title, detail, keywords }] }) -> { indexed, skipped }
///     KnowledgeIndex.clear()
@objc(KnowledgeIndexPlugin)
public class KnowledgeIndexPlugin: CAPPlugin, CAPBridgedPlugin {
    public let identifier = "KnowledgeIndexPlugin"
    public let jsName = "KnowledgeIndex"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "index", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "clear", returnType: CAPPluginReturnPromise)
    ]
    private let domain = "com.hakoya.silentmedicvet.reference"
    private let stampKey = "smv.spotlight.stamp"

    @objc func index(_ call: CAPPluginCall) {
        guard CSSearchableIndex.isIndexingAvailable() else {
            call.resolve(["indexed": 0, "skipped": true, "reason": "unavailable"])
            return
        }
        let stamp = call.getString("stamp") ?? ""
        if !stamp.isEmpty, UserDefaults.standard.string(forKey: stampKey) == stamp {
            call.resolve(["indexed": 0, "skipped": true, "reason": "current"])
            return
        }
        let raw = call.getArray("items") ?? []
        var items: [CSSearchableItem] = []
        for value in raw.prefix(2000) {
            guard let obj = value as? JSObject,
                  let id = obj["id"] as? String, !id.isEmpty,
                  let title = obj["title"] as? String, !title.isEmpty else { continue }
            let attrs = CSSearchableItemAttributeSet(contentType: UTType.text)
            attrs.title = title
            attrs.displayName = title
            attrs.contentDescription = obj["detail"] as? String
            if let words = obj["keywords"] as? JSArray {
                attrs.keywords = words.compactMap { $0 as? String }.filter { !$0.isEmpty }
            }
            items.append(CSSearchableItem(uniqueIdentifier: id, domainIdentifier: domain, attributeSet: attrs))
        }
        let index = CSSearchableIndex.default()
        let domain = self.domain, stampKey = self.stampKey
        index.deleteSearchableItems(withDomainIdentifiers: [domain]) { _ in
            index.indexSearchableItems(items) { error in
                if let error = error {
                    call.reject("Spotlight indexing failed: \(error.localizedDescription)")
                    return
                }
                UserDefaults.standard.set(stamp, forKey: stampKey)
                call.resolve(["indexed": items.count, "skipped": false])
            }
        }
    }

    @objc func clear(_ call: CAPPluginCall) {
        let stampKey = self.stampKey
        CSSearchableIndex.default().deleteSearchableItems(withDomainIdentifiers: [domain]) { error in
            UserDefaults.standard.removeObject(forKey: stampKey)
            if let error = error { call.reject(error.localizedDescription) } else { call.resolve() }
        }
    }
}
