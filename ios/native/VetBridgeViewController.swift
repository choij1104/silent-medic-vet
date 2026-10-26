import UIKit
import Capacitor

/// The app's root view controller: Capacitor's web view plus Silent Medic Vet's own native plugins.
class VetBridgeViewController: CAPBridgeViewController {
    override open func capacitorDidLoad() {
        bridge?.registerPluginInstance(FieldRoutePlugin())
        bridge?.registerPluginInstance(KnowledgeIndexPlugin())
        bridge?.registerPluginInstance(PatientChartPlugin())
        bridge?.registerPluginInstance(RecheckPlugin())
        bridge?.registerPluginInstance(FieldHapticsPlugin())
    }
}
