import random
import json
import os

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup


# ============================================================
# LEARN SMART
# PUC PHYSICS + CHEMISTRY
# ============================================================

APP_NAME = "Learn Smart"
SAVE_FILE = "learnsmart_data.json"

Window.clearcolor = (0.055, 0.07, 0.12, 1)


# ============================================================
# DATA
# ============================================================

DEFAULT_DATA = {
    "physics_answered": 0,
    "physics_correct": 0,
    "chemistry_answered": 0,
    "chemistry_correct": 0,
    "total_quizzes": 0,
    "total_questions": 0,
    "total_correct": 0,
}


def load_data():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)

            for key, value in DEFAULT_DATA.items():
                if key not in data:
                    data[key] = value

            return data

        except Exception:
            pass

    return DEFAULT_DATA.copy()


DATA = load_data()


def save_data():
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(DATA, f, indent=4)
    except Exception:
        pass


# ============================================================
# QUESTION BANK
# ============================================================

PHYSICS_QUESTIONS = [

    (
        "The SI unit of force is:",
        ["Newton", "Joule", "Watt", "Pascal"],
        "Newton"
    ),

    (
        "The SI unit of work is:",
        ["Joule", "Newton", "Watt", "Volt"],
        "Joule"
    ),

    (
        "The rate of change of displacement is:",
        ["Velocity", "Acceleration", "Force", "Momentum"],
        "Velocity"
    ),

    (
        "The rate of change of velocity is:",
        ["Acceleration", "Speed", "Momentum", "Work"],
        "Acceleration"
    ),

    (
        "The SI unit of power is:",
        ["Watt", "Joule", "Newton", "Volt"],
        "Watt"
    ),

    (
        "Momentum is equal to:",
        ["mv", "ma", "m/v", "v/m"],
        "mv"
    ),

    (
        "Newton's first law is also called:",
        ["Law of inertia", "Law of acceleration",
         "Law of action", "Law of gravitation"],
        "Law of inertia"
    ),

    (
        "Acceleration due to gravity near Earth is approximately:",
        ["9.8 m/s²", "98 m/s²", "0.98 m/s²", "8.9 m/s²"],
        "9.8 m/s²"
    ),

    (
        "The dimensional formula of velocity is:",
        ["[LT⁻¹]", "[LT]", "[L²T⁻¹]", "[MLT⁻¹]"],
        "[LT⁻¹]"
    ),

    (
        "Kinetic energy depends on:",
        ["Mass and velocity", "Only mass",
         "Only velocity", "Time"],
        "Mass and velocity"
    ),

    (
        "Potential energy near Earth's surface is:",
        ["mgh", "mv", "ma", "½mv²"],
        "mgh"
    ),

    (
        "The SI unit of electric charge is:",
        ["Coulomb", "Ampere", "Volt", "Ohm"],
        "Coulomb"
    ),

    (
        "The SI unit of electric current is:",
        ["Ampere", "Volt", "Ohm", "Coulomb"],
        "Ampere"
    ),

    (
        "Ohm's law is:",
        ["V = IR", "P = VI", "Q = It", "F = ma"],
        "V = IR"
    ),

    (
        "The SI unit of resistance is:",
        ["Ohm", "Volt", "Ampere", "Watt"],
        "Ohm"
    ),

    (
        "The SI unit of frequency is:",
        ["Hertz", "Newton", "Joule", "Watt"],
        "Hertz"
    ),

    (
        "The speed of light in vacuum is approximately:",
        ["3 × 10⁸ m/s", "3 × 10⁶ m/s",
         "3 × 10⁵ m/s", "3 × 10¹⁰ m/s"],
        "3 × 10⁸ m/s"
    ),

    (
        "The unit of wavelength is:",
        ["Metre", "Second", "Hertz", "Newton"],
        "Metre"
    ),

    (
        "A scalar quantity has:",
        ["Magnitude only", "Direction only",
         "Magnitude and direction", "Neither"],
        "Magnitude only"
    ),

    (
        "A vector quantity has:",
        ["Magnitude and direction", "Magnitude only",
         "Direction only", "No magnitude"],
        "Magnitude and direction"
    ),

    (
        "Work done is zero when force and displacement are:",
        ["Perpendicular", "Parallel",
         "Opposite", "At 45°"],
        "Perpendicular"
    ),

    (
        "The unit of pressure is:",
        ["Pascal", "Newton", "Joule", "Watt"],
        "Pascal"
    ),

    (
        "Pressure is defined as:",
        ["Force/Area", "Force × Area",
         "Area/Force", "Mass/Area"],
        "Force/Area"
    ),

    (
        "The centre of mass of a uniform rod is at:",
        ["Its midpoint", "One end",
         "Quarter point", "Outside the rod"],
        "Its midpoint"
    ),

    (
        "Torque is given by:",
        ["r × F", "m × v", "F/m", "v/t"],
        "r × F"
    ),

    (
        "Angular momentum is related to:",
        ["Rotational motion", "Only heat",
         "Only sound", "Chemical reaction"],
        "Rotational motion"
    ),

    (
        "The SI unit of angular velocity is:",
        ["rad/s", "m/s", "N/s", "J/s"],
        "rad/s"
    ),

    (
        "Escape velocity from Earth is approximately:",
        ["11.2 km/s", "5.6 km/s",
         "9.8 km/s", "22.4 km/s"],
        "11.2 km/s"
    ),

    (
        "A satellite remains in orbit mainly because of:",
        ["Gravity", "Friction",
         "Magnetism", "Electric force"],
        "Gravity"
    ),

    (
        "The SI unit of temperature is:",
        ["Kelvin", "Celsius", "Fahrenheit", "Joule"],
        "Kelvin"
    ),

    (
        "Heat is a form of:",
        ["Energy", "Force", "Momentum", "Pressure"],
        "Energy"
    ),

    (
        "The first law of thermodynamics is based on conservation of:",
        ["Energy", "Momentum", "Charge", "Mass only"],
        "Energy"
    ),

    (
        "Sound cannot travel through:",
        ["Vacuum", "Water", "Steel", "Air"],
        "Vacuum"
    ),

    (
        "Sound waves in air are generally:",
        ["Longitudinal", "Transverse",
         "Electromagnetic", "Circular"],
        "Longitudinal"
    ),

    (
        "Light is a:",
        ["Electromagnetic wave", "Mechanical wave",
         "Sound wave", "Matter wave only"],
        "Electromagnetic wave"
    ),

    (
        "The focal length of a plane mirror is:",
        ["Infinity", "Zero", "One metre", "Negative one"],
        "Infinity"
    ),

    (
        "A convex lens is generally:",
        ["Converging", "Diverging",
         "Opaque", "Reflecting only"],
        "Converging"
    ),

    (
        "A concave lens is generally:",
        ["Diverging", "Converging",
         "Plane", "Reflecting"],
        "Diverging"
    ),

    (
        "The unit of lens power is:",
        ["Dioptre", "Newton", "Joule", "Pascal"],
        "Dioptre"
    ),

    (
        "The charge of an electron is:",
        ["Negative", "Positive", "Zero", "Variable"],
        "Negative"
    ),

    (
        "The nucleus contains:",
        ["Protons and neutrons",
         "Only electrons",
         "Only protons",
         "Only neutrons"],
        "Protons and neutrons"
    ),

    (
        "The SI unit of magnetic field is:",
        ["Tesla", "Weber", "Henry", "Ohm"],
        "Tesla"
    ),

    (
        "The SI unit of capacitance is:",
        ["Farad", "Tesla", "Henry", "Ohm"],
        "Farad"
    ),

    (
        "The SI unit of inductance is:",
        ["Henry", "Farad", "Tesla", "Volt"],
        "Henry"
    ),

    (
        "The energy stored in a capacitor is:",
        ["½CV²", "CV", "IR", "mgh"],
        "½CV²"
    ),

    (
        "Photoelectric effect was explained by:",
        ["Einstein", "Newton",
         "Bohr", "Rutherford"],
        "Einstein"
    ),

    (
        "The rest mass of a photon is:",
        ["Zero", "One kg", "Very large", "Variable"],
        "Zero"
    ),

    (
        "The SI unit of Planck's constant is:",
        ["J·s", "J/s", "N/s", "W"],
        "J·s"
    ),

    (
        "Radioactivity is a:",
        ["Nuclear phenomenon", "Chemical phenomenon",
         "Mechanical phenomenon", "Thermal phenomenon"],
        "Nuclear phenomenon"
    ),

    (
        "The half-life is the time required for:",
        ["Half the nuclei to decay",
         "All nuclei to decay",
         "Double the nuclei",
         "Temperature to halve"],
        "Half the nuclei to decay"
    ),

    (
        "The unit of radioactive activity is:",
        ["Becquerel", "Tesla", "Farad", "Ohm"],
        "Becquerel"
    ),
]


CHEMISTRY_QUESTIONS = [

    (
        "The atomic number represents the number of:",
        ["Protons", "Neutrons", "Electrons + neutrons", "Nucleons"],
        "Protons"
    ),

    (
        "The charge of a proton is:",
        ["Positive", "Negative", "Zero", "Variable"],
        "Positive"
    ),

    (
        "The charge of a neutron is:",
        ["Zero", "Positive", "Negative", "Variable"],
        "Zero"
    ),

    (
        "The smallest unit of an element is:",
        ["Atom", "Molecule", "Cell", "Compound"],
        "Atom"
    ),

    (
        "H₂O is commonly known as:",
        ["Water", "Hydrogen peroxide",
         "Oxygen", "Hydrogen"],
        "Water"
    ),

    (
        "The chemical symbol of sodium is:",
        ["Na", "So", "S", "Sd"],
        "Na"
    ),

    (
        "The chemical symbol of potassium is:",
        ["K", "P", "Po", "Pt"],
        "K"
    ),

    (
        "The chemical symbol of iron is:",
        ["Fe", "Ir", "I", "In"],
        "Fe"
    ),

    (
        "The chemical symbol of gold is:",
        ["Au", "Ag", "Gd", "Go"],
        "Au"
    ),

    (
        "The pH of a neutral solution at 25°C is:",
        ["7", "0", "14", "1"],
        "7"
    ),

    (
        "A solution with pH less than 7 is:",
        ["Acidic", "Basic", "Neutral", "Salt"],
        "Acidic"
    ),

    (
        "A solution with pH greater than 7 is:",
        ["Basic", "Acidic", "Neutral", "Metallic"],
        "Basic"
    ),

    (
        "The gas essential for respiration is:",
        ["Oxygen", "Nitrogen", "Hydrogen", "Carbon dioxide"],
        "Oxygen"
    ),

    (
        "The most abundant gas in Earth's atmosphere is:",
        ["Nitrogen", "Oxygen", "Carbon dioxide", "Hydrogen"],
        "Nitrogen"
    ),

    (
        "CO₂ is:",
        ["Carbon dioxide", "Carbon monoxide",
         "Calcium oxide", "Cobalt oxide"],
        "Carbon dioxide"
    ),

    (
        "NaCl is:",
        ["Sodium chloride", "Sodium carbonate",
         "Potassium chloride", "Calcium chloride"],
        "Sodium chloride"
    ),

    (
        "The bond formed by transfer of electrons is:",
        ["Ionic bond", "Covalent bond",
         "Metallic bond", "Hydrogen bond"],
        "Ionic bond"
    ),

    (
        "The bond formed by sharing electrons is:",
        ["Covalent bond", "Ionic bond",
         "Metallic bond", "Nuclear bond"],
        "Covalent bond"
    ),

    (
        "The periodic table is arranged mainly according to:",
        ["Atomic number", "Atomic mass only",
         "Density", "Melting point"],
        "Atomic number"
    ),

    (
        "The modern periodic table has:",
        ["18 groups", "8 groups", "10 groups", "20 groups"],
        "18 groups"
    ),

    (
        "The modern periodic table has:",
        ["7 periods", "5 periods", "8 periods", "10 periods"],
        "7 periods"
    ),

    (
        "A catalyst changes the:",
        ["Rate of reaction", "Equilibrium constant",
         "Mass of reactants", "Atomic number"],
        "Rate of reaction"
    ),

    (
        "Oxidation generally involves:",
        ["Loss of electrons", "Gain of electrons",
         "No electrons", "Gain of neutrons"],
        "Loss of electrons"
    ),

    (
        "Reduction generally involves:",
        ["Gain of electrons", "Loss of electrons",
         "Gain of protons", "Loss of neutrons"],
        "Gain of electrons"
    ),

    (
        "The molar mass of H₂O is approximately:",
        ["18 g/mol", "16 g/mol", "20 g/mol", "2 g/mol"],
        "18 g/mol"
    ),

    (
        "Avogadro's number is approximately:",
        ["6.022 × 10²³", "9.8 × 10²³",
         "3 × 10⁸", "1.6 × 10⁻¹⁹"],
        "6.022 × 10²³"
    ),

    (
        "The SI unit of amount of substance is:",
        ["Mole", "Gram", "Kilogram", "Litre"],
        "Mole"
    ),

    (
        "The universal gas constant is approximately:",
        ["8.314 J mol⁻¹ K⁻¹", "9.8 J",
         "6.022 J", "3 × 10⁸ J"],
        "8.314 J mol⁻¹ K⁻¹"
    ),

    (
        "An exothermic reaction:",
        ["Releases heat", "Absorbs heat",
         "Produces no energy", "Stops immediately"],
        "Releases heat"
    ),

    (
        "An endothermic reaction:",
        ["Absorbs heat", "Releases heat",
         "Produces only light", "Produces no energy"],
        "Absorbs heat"
    ),

    (
        "The formula of methane is:",
        ["CH₄", "C₂H₆", "CO₂", "CH₃OH"],
        "CH₄"
    ),

    (
        "The formula of ethane is:",
        ["C₂H₆", "CH₄", "C₂H₄", "C₃H₈"],
        "C₂H₆"
    ),

    (
        "The functional group of alcohols is:",
        ["–OH", "–COOH", "–CHO", "–CO–"],
        "–OH"
    ),

    (
        "The functional group of carboxylic acids is:",
        ["–COOH", "–OH", "–NH₂", "–CHO"],
        "–COOH"
    ),

    (
        "The main component of natural gas is:",
        ["Methane", "Ethane", "Propane", "Butane"],
        "Methane"
    ),

    (
        "Diamond and graphite are allotropes of:",
        ["Carbon", "Silicon", "Sulfur", "Iron"],
        "Carbon"
    ),

    (
        "The strongest type of intermolecular force among these is generally:",
        ["Hydrogen bonding", "London force",
         "Dipole force", "Gravity"],
        "Hydrogen bonding"
    ),

    (
        "Rust is mainly hydrated:",
        ["Iron(III) oxide", "Copper oxide",
         "Aluminium oxide", "Zinc oxide"],
        "Iron(III) oxide"
    ),

    (
        "The gas released when an acid reacts with a carbonate is:",
        ["Carbon dioxide", "Oxygen",
         "Hydrogen", "Nitrogen"],
        "Carbon dioxide"
    ),

    (
        "The main acid present in vinegar is:",
        ["Acetic acid", "Hydrochloric acid",
         "Sulfuric acid", "Nitric acid"],
        "Acetic acid"
    ),

    (
        "The main acid in lemon juice is:",
        ["Citric acid", "Acetic acid",
         "Sulfuric acid", "Carbonic acid"],
        "Citric acid"
    ),

    (
        "The chemical formula of sulfuric acid is:",
        ["H₂SO₄", "HCl", "HNO₃", "H₂CO₃"],
        "H₂SO₄"
    ),

    (
        "The chemical formula of hydrochloric acid is:",
        ["HCl", "H₂SO₄", "HNO₃", "NaCl"],
        "HCl"
    ),

    (
        "The chemical formula of ammonia is:",
        ["NH₃", "NO₂", "N₂H", "NH₄"],
        "NH₃"
    ),

    (
        "The process of conversion of a liquid into vapour is:",
        ["Vaporisation", "Condensation",
         "Freezing", "Sublimation"],
        "Vaporisation"
    ),

    (
        "The direct conversion of solid into gas is:",
        ["Sublimation", "Melting",
         "Condensation", "Freezing"],
        "Sublimation"
    ),

    (
        "The change of gas into liquid is:",
        ["Condensation", "Evaporation",
         "Melting", "Sublimation"],
        "Condensation"
    ),

    (
        "The change of liquid into solid is:",
        ["Freezing", "Melting",
         "Boiling", "Sublimation"],
        "Freezing"
    ),

    (
        "Electrolysis uses:",
        ["Electricity", "Only heat",
         "Only pressure", "Sound"],
        "Electricity"
    ),

    (
        "The electrode connected to the positive terminal in electrolysis is:",
        ["Anode", "Cathode", "Electrolyte", "Salt bridge"],
        "Anode"
    ),

    (
        "The electrode connected to the negative terminal in electrolysis is:",
        ["Cathode", "Anode", "Electrolyte", "Salt bridge"],
        "Cathode"
    ),
]


# ============================================================
# COMMON UI
# ============================================================

def title_label(text, size=26):
    return Label(
        text=text,
        font_size=dp(size),
        bold=True,
        color=(1, 1, 1, 1),
        size_hint_y=None,
        height=dp(55)
    )


def normal_label(text, size=17):
    return Label(
        text=text,
        font_size=dp(size),
        color=(0.9, 0.92, 0.96, 1),
        halign="center",
        valign="middle"
    )


def make_button(text, height=58):
    btn = Button(
        text=text,
        font_size=dp(17),
        bold=True,
        size_hint_y=None,
        height=dp(height),
        background_normal="",
        background_color=(0.12, 0.18, 0.28, 1),
        color=(1, 1, 1, 1)
    )
    return btn


def back_button(screen):
    btn = make_button("← Back", 50)
    btn.bind(on_release=lambda x: App.get_running_app().go_back())
    return btn


# ============================================================
# HOME SCREEN
# ============================================================

class HomeScreen(Screen):

    def on_pre_enter(self):
        self.build()

    def build(self):

        self.clear_widgets()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(12)
        )

        root.add_widget(title_label("📚 LEARN SMART", 29))

        subtitle = normal_label(
            "PUC Learning • Physics + Chemistry",
            16
        )
        subtitle.size_hint_y = None
        subtitle.height = dp(40)
        root.add_widget(subtitle)

        grid = GridLayout(
            cols=2,
            spacing=dp(12),
            size_hint_y=None
        )
        grid.bind(minimum_height=grid.setter("height"))

        buttons = [
            ("⚡ Physics", "physics"),
            ("🧪 Chemistry", "chemistry"),
            ("📖 Formulas", "formulas"),
            ("🧠 Smart AI", "ai"),
            ("📊 My Progress", "progress"),
            ("ℹ️ About", "about"),
        ]

        for text, target in buttons:
            btn = make_button(text, 100)
            btn.bind(
                on_release=lambda x, t=target:
                App.get_running_app().open_screen(t)
            )
            grid.add_widget(btn)

        root.add_widget(grid)

        reset = make_button("Reset Progress", 50)
        reset.bind(on_release=self.reset_progress)
        root.add_widget(reset)

        self.add_widget(root)

    def reset_progress(self, instance):

        popup_content = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=dp(15)
        )

        popup_content.add_widget(
            normal_label(
                "Reset all your Learn Smart progress?",
                17
            )
        )

        yes = make_button("Yes, Reset", 50)
        no = make_button("Cancel", 50)

        popup_content.add_widget(yes)
        popup_content.add_widget(no)

        popup = Popup(
            title="Reset Progress",
            content=popup_content,
            size_hint=(0.85, 0.4)
        )

        def reset(_):
            global DATA
            DATA = DEFAULT_DATA.copy()
            save_data()
            popup.dismiss()
            self.build()

        yes.bind(on_release=reset)
        no.bind(on_release=lambda x: popup.dismiss())

        popup.open()


# ============================================================
# SUBJECT SCREEN
# ============================================================

class SubjectScreen(Screen):

    subject = "Physics"

    def on_pre_enter(self):
        self.build()

    def build(self):

        self.clear_widgets()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        root.add_widget(
            title_label(f"{self.subject}", 28)
        )

        info = normal_label(
            "Choose what you want to study.",
            16
        )
        info.size_hint_y = None
        info.height = dp(45)
        root.add_widget(info)

        quiz = make_button("🎯 Start 15 Question MCQ", 70)
        quiz.bind(
            on_release=lambda x:
            App.get_running_app().start_quiz(self.subject)
        )
        root.add_widget(quiz)

        formula = make_button("📐 Formulas", 65)
        formula.bind(
            on_release=lambda x:
            App.get_running_app().open_formula(self.subject)
        )
        root.add_widget(formula)

        topics = make_button("📚 Important Topics", 65)
        topics.bind(
            on_release=lambda x:
            App.get_running_app().open_topics(self.subject)
        )
        root.add_widget(topics)

        root.add_widget(back_button(self))

        self.add_widget(root)


# ============================================================
# FORMULA SCREEN
# ============================================================

class FormulaScreen(Screen):

    subject = "Physics"

    def on_pre_enter(self):
        self.build()

    def build(self):

        self.clear_widgets()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(8)
        )

        root.add_widget(
            title_label(f"{self.subject} Formulas", 25)
        )

        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            size_hint_y=None,
            padding=dp(8)
        )
        content.bind(minimum_height=content.setter("height"))

        if self.subject == "Physics":

            formulas = [
                ("Velocity", "v = s / t"),
                ("Acceleration", "a = (v - u) / t"),
                ("Force", "F = ma"),
                ("Momentum", "p = mv"),
                ("Work", "W = Fs cosθ"),
                ("Kinetic Energy", "K.E. = ½mv²"),
                ("Potential Energy", "P.E. = mgh"),
                ("Power", "P = W / t"),
                ("Pressure", "P = F / A"),
                ("Density", "ρ = m / V"),
                ("Ohm's Law", "V = IR"),
                ("Electric Power", "P = VI"),
                ("Electric Charge", "Q = It"),
                ("Frequency", "f = 1 / T"),
                ("Wave speed", "v = fλ"),
                ("Lens power", "P = 1/f"),
                ("Torque", "τ = rF sinθ"),
                ("Angular momentum", "L = Iω"),
                ("Coulomb's Law", "F = kq₁q₂/r²"),
                ("Gravitational force", "F = Gm₁m₂/r²"),
            ]

        else:

            formulas = [
                ("Moles", "n = m / M"),
                ("Molarity", "M = moles / volume"),
                ("Density", "ρ = m / V"),
                ("Ideal gas equation", "PV = nRT"),
                ("pH", "pH = −log[H⁺]"),
                ("pOH", "pOH = −log[OH⁻]"),
                ("pH + pOH", "pH + pOH = 14"),
                ("Percentage yield",
                 "% yield = actual/theoretical × 100"),
                ("Mole fraction", "χ = moles of component / total moles"),
                ("Avogadro number", "Nₐ = 6.022 × 10²³ mol⁻¹"),
                ("First law", "ΔU = Q − W"),
                ("Gibbs energy", "ΔG = ΔH − TΔS"),
            ]

        for name, formula in formulas:

            box = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=dp(75),
                padding=dp(8)
            )

            box.add_widget(
                Label(
                    text=name,
                    font_size=dp(17),
                    bold=True,
                    color=(0.5, 0.85, 1, 1)
                )
            )

            box.add_widget(
                Label(
                    text=formula,
                    font_size=dp(19),
                    color=(1, 1, 1, 1)
                )
            )

            content.add_widget(box)

        scroll.add_widget(content)
        root.add_widget(scroll)

        root.add_widget(back_button(self))

        self.add_widget(root)


# ============================================================
# TOPICS SCREEN
# ============================================================

class TopicsScreen(Screen):

    subject = "Physics"

    def on_pre_enter(self):
        self.build()

    def build(self):

        self.clear_widgets()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        root.add_widget(
            title_label(f"{self.subject} Topics", 25)
        )

        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter("height"))

        if self.subject == "Physics":

            topics = [
                "Units and Measurements",
                "Motion in a Straight Line",
                "Motion in a Plane",
                "Laws of Motion",
                "Work, Energy and Power",
                "System of Particles",
                "Rotational Motion",
                "Gravitation",
                "Mechanical Properties",
                "Thermodynamics",
                "Oscillations",
                "Waves",
                "Electrostatics",
                "Current Electricity",
                "Magnetism",
                "Electromagnetic Induction",
                "Optics",
                "Dual Nature of Matter",
                "Atoms and Nuclei",
                "Semiconductor Electronics",
            ]

        else:

            topics = [
                "Some Basic Concepts of Chemistry",
                "Structure of Atom",
                "Classification of Elements",
                "Chemical Bonding",
                "Thermodynamics",
                "Equilibrium",
                "Redox Reactions",
                "Organic Chemistry",
                "Hydrocarbons",
                "Solutions",
                "Electrochemistry",
                "Chemical Kinetics",
                "Surface Chemistry",
                "Coordination Compounds",
                "Biomolecules",
                "Polymers",
            ]

        for i, topic in enumerate(topics, 1):

            btn = make_button(
                f"{i}. {topic}",
                55
            )

            content.add_widget(btn)

        scroll.add_widget(content)
        root.add_widget(scroll)
        root.add_widget(back_button(self))

        self.add_widget(root)


# ============================================================
# QUIZ SCREEN
# ============================================================

class QuizScreen(Screen):

    subject = "Physics"

    def on_pre_enter(self):
        self.build()

    def build(self):

        self.clear_widgets()

        if self.subject == "Physics":
            bank = PHYSICS_QUESTIONS
        else:
            bank = CHEMISTRY_QUESTIONS

        # Pick any 15 questions randomly
        self.questions = random.sample(
            bank,
            min(15, len(bank))
        )

        self.index = 0
        self.score = 0
        self.answered = False

        self.root_box = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        self.progress_label = normal_label("", 15)
        self.progress_label.size_hint_y = None
        self.progress_label.height = dp(35)

        self.root_box.add_widget(self.progress_label)

        self.question_label = Label(
            text="",
            font_size=dp(20),
            bold=True,
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle"
        )
        self.root_box.add_widget(self.question_label)

        self.options_box = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            size_hint_y=None
        )
        self.options_box.bind(
            minimum_height=self.options_box.setter("height")
        )

        self.root_box.add_widget(self.options_box)

        self.feedback = normal_label("", 17)
        self.feedback.size_hint_y = None
        self.feedback.height = dp(50)
        self.root_box.add_widget(self.feedback)

        self.next_button = make_button(
            "Next Question",
            58
        )
        self.next_button.disabled = True
        self.next_button.bind(
            on_release=self.next_question
        )
        self.root_box.add_widget(self.next_button)

        self.add_widget(self.root_box)

        self.show_question()

    def show_question(self):

        self.answered = False
        self.next_button.disabled = True
        self.feedback.text = ""

        question, choices, answer = self.questions[self.index]

        self.current_answer = answer

        self.progress_label.text = (
            f"{self.subject} MCQ   "
            f"{self.index + 1} / {len(self.questions)}"
        )

        self.question_label.text = question

        self.options_box.clear_widgets()

        shuffled_choices = choices[:]
        random.shuffle(shuffled_choices)

        for choice in shuffled_choices:

            btn = make_button(choice, 60)

            btn.bind(
                on_release=lambda x, c=choice:
                self.check_answer(c)
            )

            self.options_box.add_widget(btn)

    def check_answer(self, choice):

        if self.answered:
            return

        self.answered = True
        self.next_button.disabled = False

        correct = choice == self.current_answer

        if correct:

            self.score += 1
            self.feedback.text = "✓ Correct!"

        else:

            self.feedback.text = (
                f"✗ Correct answer: {self.current_answer}"
            )

        self.options_box.children

        for child in self.options_box.children:
            child.disabled = True

    def next_question(self, instance):

        self.index += 1

        if self.index >= len(self.questions):
            self.finish_quiz()
        else:
            self.show_question()

    def finish_quiz(self):

        total = len(self.questions)

        DATA["total_quizzes"] += 1
        DATA["total_questions"] += total
        DATA["total_correct"] += self.score

        if self.subject == "Physics":
            DATA["physics_answered"] += total
            DATA["physics_correct"] += self.score
        else:
            DATA["chemistry_answered"] += total
            DATA["chemistry_correct"] += self.score

        save_data()

        percentage = round(
            (self.score / total) * 100
        )

        App.get_running_app().show_result(
            self.subject,
            self.score,
            total,
            percentage
        )


# ============================================================
# PROGRESS SCREEN
# ============================================================

class ProgressScreen(Screen):

    def on_pre_enter(self):
        self.build()

    def build(self):

        self.clear_widgets()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        root.add_widget(
            title_label("📊 My Progress", 27)
        )

        total_q = DATA["total_questions"]
        total_c = DATA["total_correct"]

        if total_q:
            percentage = round(
                (total_c / total_q) * 100
            )
        else:
            percentage = 0

        root.add_widget(
            normal_label(
                f"Overall Accuracy: {percentage}%",
                20
            )
        )

        progress = ProgressBar(
            max=100,
            value=percentage,
            size_hint_y=None,
            height=dp(25)
        )

        root.add_widget(progress)

        stats = GridLayout(
            cols=2,
            spacing=dp(10),
            size_hint_y=None
        )
        stats.bind(minimum_height=stats.setter("height"))

        values = [
            ("Total Quizzes", DATA["total_quizzes"]),
            ("Questions", DATA["total_questions"]),
            ("Correct", DATA["total_correct"]),
            ("Physics Correct",
             DATA["physics_correct"]),
            ("Chemistry Correct",
             DATA["chemistry_correct"]),
        ]

        for name, value in values:

            box = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=dp(75)
            )

            box.add_widget(
                Label(
                    text=name,
                    font_size=dp(15),
                    color=(0.55, 0.85, 1, 1)
                )
            )

            box.add_widget(
                Label(
                    text=str(value),
                    font_size=dp(21),
                    bold=True,
                    color=(1, 1, 1, 1)
                )
            )

            stats.add_widget(box)

        root.add_widget(stats)

        root.add_widget(
            back_button(self)
        )

        self.add_widget(root)


# ============================================================
# SIMPLE AI SCREEN
# ============================================================

class AIScreen(Screen):

    def on_pre_enter(self):
        self.build()

    def build(self):

        self.clear_widgets()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        root.add_widget(
            title_label("🧠 Smart AI", 27)
        )

        root.add_widget(
            normal_label(
                "Ask a simple study question.\n"
                "This offline AI gives quick learning help.",
                16
            )
        )

        self.input_box = Button(
            text="Tap here for study suggestions",
            font_size=dp(17),
            size_hint_y=None,
            height=dp(70),
            background_normal="",
            background_color=(0.12, 0.18, 0.28, 1)
        )

        root.add_widget(self.input_box)

        suggestions = [
            "What is Newton's second law?",
            "What is kinetic energy?",
            "What is Ohm's law?",
            "What is a mole?",
            "What is pH?",
            "What is an ionic bond?",
        ]

        for text in suggestions:

            btn = make_button(text, 55)
            btn.bind(
                on_release=lambda x, q=text:
                self.answer(q)
            )
            root.add_widget(btn)

        self.answer_label = normal_label(
            "",
            17
        )

        root.add_widget(self.answer_label)

        root.add_widget(back_button(self))

        self.add_widget(root)

    def answer(self, question):

        answers = {

            "What is Newton's second law?":
                "Newton's second law: F = ma. "
                "Force equals mass multiplied by acceleration.",

            "What is kinetic energy?":
                "Kinetic energy is the energy of motion. "
                "Formula: K.E. = ½mv².",

            "What is Ohm's law?":
                "Ohm's law states V = IR, where V is voltage, "
                "I is current and R is resistance.",

            "What is a mole?":
                "A mole is the SI unit of amount of substance. "
                "One mole contains about 6.022 × 10²³ particles.",

            "What is pH?":
                "pH measures how acidic or basic a solution is. "
                "At 25°C, pH 7 is neutral.",

            "What is an ionic bond?":
                "An ionic bond forms when electrons are transferred "
                "between atoms, producing oppositely charged ions.",
        }

        self.answer_label.text = answers.get(
            question,
            "Try another question."
        )


# ============================================================
# ABOUT SCREEN
# ============================================================

class AboutScreen(Screen):

    def on_pre_enter(self):
        self.build()

    def build(self):

        self.clear_widgets()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15)
        )

        root.add_widget(
            title_label("About Learn Smart", 26)
        )

        root.add_widget(
            normal_label(
                "Learn Smart is an offline study app "
                "for PUC students.\n\n"
                "Subjects:\n"
                "• Physics\n"
                "• Chemistry\n\n"
                "Features:\n"
                "• Random MCQs\n"
                "• 15-question quizzes\n"
                "• Formula reference\n"
                "• Progress tracking\n"
                "• Offline Smart AI",
                17
            )
        )

        root.add_widget(back_button(self))

        self.add_widget(root)


# ============================================================
# MAIN APP
# ============================================================

class LearnSmartApp(App):

    def build(self):

        self.title = APP_NAME

        self.history = []

        self.sm = ScreenManager()

        self.sm.add_widget(
            HomeScreen(name="home")
        )

        self.sm.add_widget(
            SubjectScreen(name="physics")
        )

        self.sm.add_widget(
            SubjectScreen(name="chemistry")
        )

        self.sm.add_widget(
            FormulaScreen(name="physics_formulas")
        )

        self.sm.add_widget(
            FormulaScreen(name="chemistry_formulas")
        )

        self.sm.add_widget(
            TopicsScreen(name="physics_topics")
        )

        self.sm.add_widget(
            TopicsScreen(name="chemistry_topics")
        )

        self.sm.add_widget(
            QuizScreen(name="quiz")
        )

        self.sm.add_widget(
            ProgressScreen(name="progress")
        )

        self.sm.add_widget(
            AIScreen(name="ai")
        )

        self.sm.add_widget(
            AboutScreen(name="about")
        )

        self.sm.current = "home"

        return self.sm

    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

    def open_screen(self, name):

        if name == "physics":
            screen = self.sm.get_screen("physics")
            screen.subject = "Physics"
            target = "physics"

        elif name == "chemistry":
            screen = self.sm.get_screen("chemistry")
            screen.subject = "Chemistry"
            target = "chemistry"

        else:
            target = name

        if target != self.sm.current:
            self.history.append(self.sm.current)

        self.sm.current = target

    def open_formula(self, subject):

        if subject == "Physics":
            target = "physics_formulas"
        else:
            target = "chemistry_formulas"

        self.history.append(self.sm.current)

        screen = self.sm.get_screen(target)
        screen.subject = subject

        self.sm.current = target

    def open_topics(self, subject):

        if subject == "Physics":
            target = "physics_topics"
        else:
            target = "chemistry_topics"

        self.history.append(self.sm.current)

        screen = self.sm.get_screen(target)
        screen.subject = subject

        self.sm.current = target

    def start_quiz(self, subject):

        self.history.append(self.sm.current)

        quiz = self.sm.get_screen("quiz")
        quiz.subject = subject

        self.sm.current = "quiz"

    def go_back(self):

        if self.history:

            previous = self.history.pop()
            self.sm.current = previous

        else:

            if self.sm.current != "home":
                self.sm.current = "home"

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    def show_result(
        self,
        subject,
        score,
        total,
        percentage
    ):

        content = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        content.add_widget(
            Label(
                text=f"{subject} Quiz Complete!",
                font_size=dp(22),
                bold=True,
                color=(1, 1, 1, 1)
            )
        )

        content.add_widget(
            Label(
                text=(
                    f"Score: {score}/{total}\n"
                    f"Accuracy: {percentage}%"
                ),
                font_size=dp(19),
                color=(1, 1, 1, 1)
            )
        )

        if percentage >= 80:
            message = "Excellent! Keep going! 🌟"
        elif percentage >= 60:
            message = "Good job! Practice a little more."
        elif percentage >= 40:
            message = "Keep studying. You can improve!"
        else:
            message = "Don't give up. Try the quiz again!"

        content.add_widget(
            Label(
                text=message,
                font_size=dp(17),
                color=(0.6, 0.9, 1, 1)
            )
        )

        button = make_button("Continue", 55)
        content.add_widget(button)

        popup = Popup(
            title="Quiz Result",
            content=content,
            size_hint=(0.85, 0.5),
            auto_dismiss=False
        )

        def close(_):

            popup.dismiss()

            if self.history:
                self.sm.current = self.history.pop()
            else:
                self.sm.current = "home"

        button.bind(on_release=close)

        popup.open()


# ============================================================
# ANDROID BACK BUTTON
# ============================================================

def android_back(window, key, scancode, codepoint, modifier):

    if key == 27:

        app = App.get_running_app()

        if app:

            if app.sm.current != "home":
                app.go_back()
                return True

            return False

    return False


Window.bind(on_keyboard=android_back)


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    LearnSmartApp().run()