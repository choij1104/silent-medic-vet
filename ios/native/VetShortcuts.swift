import Foundation
#if canImport(AppIntents)
import AppIntents

/// Siri, Spotlight and Shortcuts actions (App Intents, iOS 16+; App Shortcuts with Siri phrases, iOS 17+).
/// Each one opens Silent Medic Vet and queues a route through FieldRouter, which the app picks up
/// as it comes to the foreground.

@available(iOS 16.0, *)
enum VetAnimal: String, AppEnum {
    case dog, cat, rabbit, horse, cattle, sheep, goat, deer, pig, chicken, duck, turkey, peafowl

    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Animal"
    static var caseDisplayRepresentations: [VetAnimal: DisplayRepresentation] = [
        .dog: "Dog", .cat: "Cat", .rabbit: "Rabbit", .horse: "Horse",
        .cattle: "Cattle", .sheep: "Sheep", .goat: "Goat", .deer: "Deer", .pig: "Pig",
        .chicken: "Chicken", .duck: "Duck", .turkey: "Turkey", .peafowl: "Peafowl"
    ]
}

@available(iOS 16.0, *)
struct LookUpVetDrugIntent: AppIntent {
    static var title: LocalizedStringResource = "Look Up a Drug for an Animal"
    static var description = IntentDescription("Opens the Silent Medic Vet reference for the animal you choose, with your drug or problem already searched.")
    static var openAppWhenRun: Bool = true

    @Parameter(title: "Animal", default: .dog)
    var animal: VetAnimal

    @Parameter(title: "Drug or problem")
    var term: String?

    @MainActor
    func perform() async throws -> some IntentResult {
        let clean = (term ?? "").trimmingCharacters(in: .whitespacesAndNewlines)
        FieldRouter.shared.queue("lookup:\(animal.rawValue):\(String(clean.prefix(80)))")
        return .result()
    }
}

@available(iOS 16.0, *)
struct BuildTriagePlanIntent: AppIntent {
    static var title: LocalizedStringResource = "Build a Triage Plan"
    static var description = IntentDescription("Opens the Silent Medic Vet plan builder for the animal you choose: red flags, what to do now and what not to do.")
    static var openAppWhenRun: Bool = true

    @Parameter(title: "Animal", default: .dog)
    var animal: VetAnimal

    @MainActor
    func perform() async throws -> some IntentResult {
        FieldRouter.shared.queue("plan:\(animal.rawValue)")
        return .result()
    }
}

@available(iOS 16.0, *)
struct OpenPatientsIntent: AppIntent {
    static var title: LocalizedStringResource = "Open My Patients"
    static var description = IntentDescription("Opens the animal profiles and recheck reminders you keep in Silent Medic Vet.")
    static var openAppWhenRun: Bool = true

    @MainActor
    func perform() async throws -> some IntentResult {
        FieldRouter.shared.queue("patients")
        return .result()
    }
}

@available(iOS 17.0, *)
struct VetShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(intent: LookUpVetDrugIntent(),
                    phrases: ["Look up a drug for \(\.$animal) in \(.applicationName)",
                              "Look up a drug in \(.applicationName)",
                              "Check a medicine for my \(\.$animal) in \(.applicationName)"],
                    shortTitle: "Look Up a Drug",
                    systemImageName: "pills")
        AppShortcut(intent: BuildTriagePlanIntent(),
                    phrases: ["Build a triage plan for my \(\.$animal) in \(.applicationName)",
                              "Start a triage plan in \(.applicationName)"],
                    shortTitle: "Triage Plan",
                    systemImageName: "cross.case")
        AppShortcut(intent: OpenPatientsIntent(),
                    phrases: ["Open my patients in \(.applicationName)",
                              "Show my animals in \(.applicationName)"],
                    shortTitle: "My Patients",
                    systemImageName: "pawprint")
    }
}
#endif
