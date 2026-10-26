import UIKit
import Capacitor
import CoreSpotlight
import UserNotifications

/// Every way into Silent Medic Vet from outside the app ends here: a Spotlight result, a Siri or
/// Shortcuts action, or a tapped recheck reminder. Each is reduced to one short route string that the
/// app's web layer understands:
///
///   kb:<entry number>            open a reference entry
///   cond:<condition id>          open a condition card
///   lookup:<animal>:<term>       reference tab for that animal, search filled in
///   plan:<animal>                triage plan builder for that animal
///   patients                     patient list
///   patient:<profile id>         one patient profile
///
/// The route is kept in UserDefaults until the web layer takes it, so it survives a cold launch.
final class FieldRouter: NSObject, UNUserNotificationCenterDelegate {
    static let shared = FieldRouter()
    static let routeQueued = Notification.Name("SilentMedicVetRouteQueued")
    private let storeKey = "smv.route.pending"

    /// Called from AppDelegate before launch finishes, so a reminder tapped while the app was
    /// closed is still delivered here.
    func install() {
        UNUserNotificationCenter.current().delegate = self
    }

    func queue(_ route: String) {
        UserDefaults.standard.set(route, forKey: storeKey)
        NotificationCenter.default.post(name: FieldRouter.routeQueued, object: nil)
    }

    func take() -> String {
        let route = UserDefaults.standard.string(forKey: storeKey) ?? ""
        UserDefaults.standard.removeObject(forKey: storeKey)
        return route
    }

    /// Spotlight results carry the route as their unique identifier.
    func accept(_ activity: NSUserActivity) -> Bool {
        guard activity.activityType == CSSearchableItemActionType,
              let id = activity.userInfo?[CSSearchableItemActivityIdentifier] as? String,
              !id.isEmpty else { return false }
        queue(id)
        return true
    }

    // Show a recheck reminder even when the app is open.
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification,
                                withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.banner, .list, .sound])
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                didReceive response: UNNotificationResponse,
                                withCompletionHandler completionHandler: @escaping () -> Void) {
        if let route = response.notification.request.content.userInfo["route"] as? String, !route.isEmpty {
            queue(route)
        }
        completionHandler()
    }
}

/// JS: Capacitor.registerPlugin('FieldRoute').take() -> { route }. Emits "route" when a new one arrives
/// while the app is running.
@objc(FieldRoutePlugin)
public class FieldRoutePlugin: CAPPlugin, CAPBridgedPlugin {
    public let identifier = "FieldRoutePlugin"
    public let jsName = "FieldRoute"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "take", returnType: CAPPluginReturnPromise)
    ]
    private var observer: NSObjectProtocol?

    override public func load() {
        observer = NotificationCenter.default.addObserver(forName: FieldRouter.routeQueued, object: nil, queue: .main) { [weak self] _ in
            self?.notifyListeners("route", data: ["pending": true], retainUntilConsumed: true)
        }
    }

    deinit {
        if let observer = observer { NotificationCenter.default.removeObserver(observer) }
    }

    @objc func take(_ call: CAPPluginCall) {
        call.resolve(["route": FieldRouter.shared.take()])
    }
}
