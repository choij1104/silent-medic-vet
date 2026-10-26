import UIKit
import Capacitor

/// Taptic feedback for the moments that matter in the field: choosing an animal, building a triage
/// plan that lists red flags, saving a patient, setting a reminder.
///
/// JS: FieldHaptics.selection() · FieldHaptics.impact({ style }) · FieldHaptics.notify({ type })
@objc(FieldHapticsPlugin)
public class FieldHapticsPlugin: CAPPlugin, CAPBridgedPlugin {
    public let identifier = "FieldHapticsPlugin"
    public let jsName = "FieldHaptics"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "selection", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "impact", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "notify", returnType: CAPPluginReturnPromise)
    ]

    @objc func selection(_ call: CAPPluginCall) {
        DispatchQueue.main.async {
            let g = UISelectionFeedbackGenerator()
            g.selectionChanged()
            call.resolve()
        }
    }

    @objc func impact(_ call: CAPPluginCall) {
        let style: UIImpactFeedbackGenerator.FeedbackStyle
        switch call.getString("style") ?? "medium" {
        case "light": style = .light
        case "heavy": style = .heavy
        case "rigid": style = .rigid
        case "soft": style = .soft
        default: style = .medium
        }
        DispatchQueue.main.async {
            UIImpactFeedbackGenerator(style: style).impactOccurred()
            call.resolve()
        }
    }

    @objc func notify(_ call: CAPPluginCall) {
        let type: UINotificationFeedbackGenerator.FeedbackType
        switch call.getString("type") ?? "success" {
        case "warning": type = .warning
        case "error": type = .error
        default: type = .success
        }
        DispatchQueue.main.async {
            UINotificationFeedbackGenerator().notificationOccurred(type)
            call.resolve()
        }
    }
}
