# Module 7: Electro Magnetic Fields (EMF)

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section |
| --- | --- | --- |
| 7.1 | Electromagnetic Spectrum, Electric and Magnetic Fields | [Section 1](#71-electromagnetic-spectrum-electric-and-magnetic-fields) |
| 7.2 | What Causes EMF | [Section 2](#72-what-causes-emf) |
| 7.3 | Vendor Disclaimers | [Section 3](#73-vendor-disclaimers) |
| 7.4 | Impact of EMF | [Section 4](#74-impact-of-emf) |
| 7.5 | Standards | [Section 5](#75-standards) |
| 7.6 | EMP | [Section 6](#76-emp-electromagnetic-pulse) |
| 7.7 | Design and Installation | [Section 7](#77-design-and-installation) |
| 7.8 | Shielding | [Section 8](#78-shielding) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-7-electro-magnetic-fields) |

**Objectives (from your slide).** After this module you should be able to describe and understand:

- EMF and the two main different types and units of measurements
- The norms and best practices
- The potential sources for EMF
- How to reduce EMF

| Objective | Where it is covered |
| --- | --- |
| **EMF, its two main types and units** | 7.1 (electric and magnetic fields, V/m, A/m, tesla, gauss) |
| **Norms and best practices** | 7.5 (standards and exposure limits), 7.3 (vendor statements), 7.7 (best practices in design and installation) |
| **Potential sources for EMF** | 7.2 (sources and what makes them strong), 7.6 (pulses) |
| **How to reduce EMF** | 7.7 (design and installation), 7.8 (shielding) |

A one-page summary of each objective follows the introduction below.

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Only the **objectives slide** was available for this module (not the lesson slides), so check the glossary, formulas and thresholds against your course. Related earlier material: earthing and common-mode noise (Module 6, 6.26 and 6.27 in `06-2` and `06-3`), power and data cable separation (6.18 in `06-2`), harmonics (6.31 in `06-3`) and phase balancing (6.17 in `06-2`).

## Why EMF matters in a data centre

| Reason | Detail |
| --- | --- |
| **Equipment immunity** | Strong fields can disturb displays, magnetic media, sensors and data cabling |
| **People** | Staff near switchrooms and busbars are exposed, and exposure guidelines exist |
| **Siting and layout** | Where transformers, busbars and cables are placed decides the fields in the IT space |
| **Cost** | Distance and good cable layout are cheap at design time. Shielding afterwards is expensive |
| **Resilience** | Pulses (lightning, EMP, solar storms) can damage equipment, not just disturb it |

---

## The four objectives at a glance

### 1. EMF and the two main types and units

| Type | Caused by | Unit | Notes |
| --- | --- | --- | --- |
| **Electric field (E)** | **Voltage** | **V/m** (kV/m) | Present whenever equipment is energised. Easy to shield |
| **Magnetic field (H and B)** | **Current** | **H: A/m. B: tesla (T), µT, mG** | Present only when current flows. Passes through walls. Hard to shield at 50/60 Hz |

**Conversions:** **1 µT = 10 mG**, **1 A/m = 1.2566 µT**. Background in a commercial building is about 0.05 to 0.3 µT (0.5 to 3 mG).

### 2. The norms and best practices

| | Key points |
| --- | --- |
| **Exposure norms (people)** | **ICNIRP 2010** at 50 Hz: public **200 µT and 5 kV/m**, occupational **1,000 µT and 10 kV/m**. **EU recommendation 1999/519/EC**: public **100 µT**. **EU Directive 2013/35/EU**: workers (action levels, risk assessment). **IEEE C95.6** (60 Hz) |
| **Equipment norms** | **EMC Directive and CE marking**, **EN 55032 / 55035** (emission and immunity), **IEC 61000-4-8** (50/60 Hz magnetic immunity, 1 to 100 A/m, i.e. 1.3 to 126 µT), IEC 61000-4-3 (RF) |
| **Installation norms** | **EN 50174-2** (power and data separation), bonding standards (EN 50310, TIA-607), **IEC 61786-1** (measurement) |
| **Best practices** | Site away from external sources. Keep transformers, busbars and risers away from the IT space. Keep all phases, neutral and earth together. Balance phases. TN-S with a single bond. Separate power and data and cross at 90°. Use fibre or shielded twisted pair. Measure before and after energising. Design to about **1 µT** at sensitive points |

### 3. The potential sources of EMF

| Group | Examples |
| --- | --- |
| **Power infrastructure (the main ones)** | **Transformers, busbars and bus ducts, large cables, switchboards, UPS and battery cables, PDUs, generators, drives** |
| **Stray currents** | Neutral or earth return currents (TN-C, multiple bonds), unbalanced phases, ground loops |
| **Electronics** | Switching power supplies, lighting drivers, drives |
| **External** | High-voltage lines, substations, railways, transformers in neighbouring buildings, radio transmitters, radar, mobile masts |
| **Natural and pulses** | The Earth's field, lightning, solar storms, EMP |

**What makes a source strong:** high **current**, large **spacing** between go and return conductors, **net current**, **unbalance**, **harmonics**, and **proximity**.

### 4. How to reduce EMF

| Order | Approach | Examples |
| --- | --- | --- |
| **1. Avoid** | Choose the site and layout | Away from HV lines and transmitters. No electrical room adjacent to the white space |
| **2. Reduce at the source** | Electrical design | **Bundle or trefoil conductors**, all phases, neutral and earth in one cable or raceway, **cross-phase arrangement** for parallel cables, low-field busway, **balanced phases**, **TN-S with one neutral-earth bond**, low-THDi equipment |
| **3. Increase distance** | Layout | Fields fall as 1/r, or 1/r² for balanced sources |
| **4. Shield** | Last resort for 50/60 Hz | Mu-metal or steel enclosures, aluminium plates at the source. Grounded metal for electric fields |
| **5. Compensate or relocate** | | Cancellation loops, replace CRT displays with flat panels |
| **6. Operate safely** | People | Zones, signs, risk assessment for staff with implants |
| **Always** | Verify | Measure with a three-axis meter, under load, before and after energising |

---

# 7.1 Electromagnetic spectrum, electric and magnetic fields

## 1. What electromagnetic fields are

An **electromagnetic field (EMF)** has an **electric** part and a **magnetic** part.

| Field | Caused by | Unit | Key idea |
| --- | --- | --- | --- |
| **Electric field (E)** | **Voltage** (electric charge). Present whenever a conductor is **energised**, even with no current | **V/m** (or kV/m) | Easily blocked by conductors, buildings, trees, the human body |
| **Magnetic field (H, B)** | **Current** (moving charge). Present only when current **flows** | **H:** A/m. **B (flux density):** tesla (T), usually **µT** or **mG** | Passes through almost everything, including walls, floors and people |

**Rule to remember:** **voltage makes E, current makes B.** More voltage means more E, more current means more B.

At **power frequency (50/60 Hz)** the electric and magnetic fields behave as **two separate fields** and are treated separately. At **radio frequencies** they travel together as a **wave**.

## 2. Magnetic field units

| Quantity | Unit | Conversion |
| --- | --- | --- |
| **Magnetic field strength H** | A/m | |
| **Magnetic flux density B** | tesla (T), µT, mT | **B = µ₀ × H**, and in air **1 A/m = 1.2566 µT** |
| **Gauss** (older unit) | G, mG | **1 µT = 10 mG**, and 1 G = 100 µT |

| H | B |
| --- | --- |
| 1 A/m | 1.26 µT |
| 3 A/m | 3.8 µT |
| 10 A/m | 12.6 µT |
| 30 A/m | 37.7 µT |
| 100 A/m | 125.7 µT |
| 1,000 A/m | 1,257 µT (1.26 mT) |

**Reference levels for scale:** the Earth's static field is roughly **25 to 65 µT**. Typical **background** power-frequency fields in commercial buildings are about **0.05 to 0.3 µT (0.5 to 3 mG)** **[CHECK]**.

## 3. The electromagnetic spectrum

All electromagnetic radiation travels at the speed of light, with **wavelength × frequency = c**:

```
c = f × λ        c = 3 × 10⁸ m/s        λ = c / f
```

| Band | Frequency (approx.) | Wavelength | Examples |
| --- | --- | --- | --- |
| **Static** | 0 Hz | | Earth's field, magnets, DC cables |
| **ELF** (extremely low frequency) | 0 to 300 Hz | thousands of km | **Mains power 50/60 Hz** and its low harmonics (150 Hz, 250 Hz) |
| **IF** (intermediate frequency) | 300 Hz to 100 kHz | km | Switching power supplies, drives, induction heating |
| **RF** (radio frequency) | 100 kHz to 300 GHz | km to mm | AM/FM radio, TV, mobile, Wi-Fi, radar, microwaves |
| **Infrared** | 300 GHz to about 400 THz | | Heat, remote controls, fibre optics |
| **Visible light** | about 400 to 790 THz | | Light |
| **Ultraviolet** | about 790 THz up | | Sun lamps |
| **X-rays, gamma rays** | far higher | | Medical imaging, nuclear |

**Ionising vs. non-ionising:** the radiation in the first rows (static, ELF, IF, RF, infrared, visible, and the lower end of UV) is **non-ionising**: it doesn't have enough photon energy to break chemical bonds. **X-rays and gamma rays are ionising.** Data centre EMF concerns are almost entirely **non-ionising**.

### Wavelength examples

| Source | Frequency | Wavelength |
| --- | --- | --- |
| Mains power | 50 Hz | 3 × 10⁸ / 50 = **6,000 km** |
| FM radio | 100 MHz | **3 m** |
| 1 GHz (mobile) | 1 GHz | **0.3 m** |
| Wi-Fi / microwave oven | 2.45 GHz | **12.2 cm** |

**Why this matters:** at 50 Hz the wavelength is thousands of km, so near any building you are always in the **near field**, where the electric and magnetic fields are **independent**. At radio frequencies, once you are a few wavelengths from the source (the **far field**), E and H are tied together by the impedance of free space (**377 Ω**): **E / H = 377 Ω**.

### Power density in the far field

```
S = E² / 377      (W/m²)        e.g. E = 3 V/m → S = 9 / 377 = 0.024 W/m² = 2.4 µW/cm²
```

## 4. How fields vary with current and distance

### The magnetic field of a straight conductor

```
B = µ₀ I / (2π r) = 2 × 10⁻⁷ × I / r   (tesla, with I in amps and r in metres)
```

**Worked example: a single 1,000 A conductor**

| Distance | B | In mG |
| --- | --- | --- |
| 1 m | 200 µT | 2,000 mG |
| 2 m | 100 µT | 1,000 mG |
| 5 m | 40 µT | 400 mG |
| 10 m | 20 µT | 200 mG |
| 20 m | 10 µT | 100 mG |

The field falls only as **1/r**. A single conductor with its return current far away is a **long-range** source.

### Why cables that carry current in and out together are quiet

When the **go and return** currents run close together, their fields **cancel**. For two opposite currents separated by **s**, at distance **r** much larger than s:

```
B ≈ µ₀ I s / (2π r²) = 2 × 10⁻⁷ × I × s / r²
```

The field now falls as **1/r²** and is smaller by the ratio s / r.

**Worked example: 1,000 A, field at different distances**

| Distance | Single conductor | Pair, s = 0.1 m (tight bundle) | Pair, s = 0.3 m (busbar spacing) |
| --- | --- | --- | --- |
| 1 m | 200 µT | **20 µT** | **60 µT** |
| 2 m | 100 µT | 5 µT | 15 µT |
| 5 m | 40 µT | **0.8 µT** | **2.4 µT** |
| 10 m | 20 µT | 0.2 µT | 0.6 µT |

Bundling the conductors closer cuts the field by a factor of three here, and at 5 m the result is **50 times smaller** than for a lone conductor.

**Three-phase systems.** Balanced three-phase currents sum to **zero** at every instant (`06a`, section 5), so conductors laid **close together** (a trefoil, or all phases in one raceway) produce very little external field. Cancellation is **imperfect** if the phases are **spread apart** (as in many busbars) or if the currents are **unbalanced**.

### Decay with distance **[CHECK]**

| Source arrangement | Field falls with distance as |
| --- | --- |
| Single conductor, or any group with a **net current** | **1/r** |
| Balanced go-and-return pair, or a bundled three-phase group | **1/r²** or faster |
| Compact devices such as a transformer core (like a magnetic dipole) | **1/r³** |

## 5. Electric and magnetic fields compared

| | **Electric field** | **Magnetic field** |
| --- | --- | --- |
| **Source** | Voltage | Current |
| **Unit** | V/m | A/m, µT, mG |
| **Present when** | Equipment is energised | Current flows |
| **Shielding** | **Easy**: any grounded conductor | **Hard** at 50/60 Hz: needs high-permeability or very thick metal |
| **Penetrates walls** | Mostly blocked | Passes through concrete, floors, people |
| **Falls with distance** | Quickly | Quickly for balanced sources |
| **Main concern** | Perception, induced charges, interference to sensitive sensors | **Interference with equipment**, induced currents, health guidelines |

---

# 7.2 What causes EMF

## 1. Natural and man-made sources

| Type | Examples |
| --- | --- |
| **Natural** | The Earth's field, atmospheric electricity, **lightning**, solar activity (geomagnetic storms) |
| **Power system** | Generation, transmission lines, substations, transformers, wiring, appliances |
| **Electronics** | Switching power supplies, drives, lighting drivers, computers |
| **Radio** | Broadcast, mobile masts, radar, Wi-Fi, two-way radios |
| **Industrial and medical** | Welding, induction heating, MRI |

## 2. Sources in and around a data centre

| Source | Why it creates fields |
| --- | --- |
| **Transformers** | Stray (leakage) flux from the core and windings, and high-current LV connections (**the field is highest close to the unit**) |
| **Busbars and bus ducts** | Very high current, with conductors **spaced apart** for maintenance, so cancellation is incomplete |
| **High-current cables** | Strong fields if the phases are **separated** or the currents **unbalanced** |
| **Switchboards and main LV boards** | Heavy busbars and many feeders |
| **UPS and battery cables** | Large currents, and **DC** battery cables create **static** fields. Rectifiers and inverters add switching harmonics |
| **PDUs and RPPs** | Many circuits with strong local fields |
| **Generators and motors** | Rotating machines, drives |
| **Chillers, pumps, CRAH fans and variable-speed drives** | Currents with switching harmonics (kHz) |
| **Server and network power supplies** | Switch-mode, with fields at their switching frequency (tens to hundreds of kHz), generally small and local |
| **Lighting ballasts and LED drivers** | Switching noise (see 5.1 in `05_light.md`) |
| **Neutral and earth return currents** | **Stray currents** in neutral, PE, cable screens and building steel (6.26 in `06-2`) |
| **External** | High-voltage lines, **substations**, railway traction, neighbouring buildings' transformers, mobile masts, radar and broadcast transmitters |

**A note on scale.** The thousands of servers inside the building generate little EMF outside. The fields that matter are those of the **power infrastructure** that feeds them: **transformers, switchgear, busbars and large cables**.

## 3. What decides how large the field is

| Factor | Effect |
| --- | --- |
| **Current** | Doubling the current doubles the field |
| **Distance** | Fields drop quickly with distance |
| **Conductor spacing (loop area)** | The further the go and return conductors are apart, the weaker the cancellation |
| **Net current** | Any current that does **not** return in the same bundle produces a field that decays slowly |
| **Phase balance** | Unbalanced currents leave a net current in the neutral |
| **Harmonics** | Add fields at 150 Hz, 250 Hz and higher, and drive neutral current (the 3rd harmonic is now a dominant frequency in many environments) |
| **Geometry** | Compact bundles and trefoil layouts cancel best |

### The net-current rule

For a group of conductors (a cable, a raceway, a busbar run), the field **far away** depends on the **net current** (the sum of all the currents, including the neutral and earth conductors). If everything returns inside the bundle, the net current is **zero** and the field falls quickly. If **some current returns elsewhere** (through the structure, a different cable, cable armour or the earth) the field falls only as **1/r** and reaches far.

```
Net current = I_L1 + I_L2 + I_L3 + I_N + I_PE (+ screens and armour)   → should be 0 inside the bundle
```

## 4. Stray currents and earthing

Wrong earthing arrangements create net currents in the building structure:

| Cause | Effect |
| --- | --- |
| **TN-C** (combined neutral and earth, 6.26 in `06-2`) | Neutral current flows in earth conductors, steel, trays and pipes, creating fields along the whole structure |
| **Multiple neutral-ground bonds** | Neutral current splits between the neutral and the earth paths |
| **Ground loops** | Circulating currents driven by voltage differences between earths |
| **Single-core cables with separated phases, or armour bonded at both ends** | Induced circulating currents in armour and screens |
| **Unbalanced phases** | Neutral current (6.17 in `06-2`) |

The cure is in the earthing design: **TN-S, a single neutral-earth bond, a common bonded network, balanced phases**, and phases, neutral and earth kept together.

## 5. Worked example: the LV side of a transformer

A **1,600 kVA, 400 V** transformer carries up to **2,309 A** on its secondary. If that current runs in **separate single-core cables spaced 0.3 m apart**:

```
Field at 1 m  ≈ 2 × 10⁻⁷ × 2,309 × 0.3 / 1² = about 139 µT   (pair-type estimate)
```

If the same current runs in a **tight bundle (s = 0.1 m)**:

```
Field at 1 m  ≈ 2 × 10⁻⁷ × 2,309 × 0.1 / 1² = about 46 µT
```

For a sensitive display at **1 µT**, the distance needed is **r = √(2 × 10⁻⁷ × I × s / B)**:

```
Bundled (s = 0.1 m):   r = √(2 × 10⁻⁷ × 2,309 × 0.1 / 10⁻⁶) = √46 = about 6.8 m
Spread (s = 0.3 m):    r = √(2 × 10⁻⁷ × 2,309 × 0.3 / 10⁻⁶) = √139 = about 11.8 m
```

This is a simplified estimate **[CHECK]** (real three-phase layouts and finite lengths differ), but it shows the principle: **layout and distance matter far more than the current alone.**

## 6. Typical levels **[CHECK]**

| Situation | Typical magnetic field |
| --- | --- |
| Background in commercial buildings | about 0.05 to 0.3 µT (0.5 to 3 mG) |
| Computer monitor, at 35 cm | about 0.2 to 0.4 µT (2 to 4 mG) |
| Household appliances, at 27 cm | about 0.8 to 16 µT (8 to 165 mG) |
| Under a 345 kV transmission line | about 2 to 6 µT (20 to 60 mG), below about 0.2 µT at 90 m (300 ft) |
| Large busbar or transformer room, close to the equipment | tens to hundreds of µT |

---

# 7.3 Vendor disclaimers

## 1. What this means

Equipment vendors state **the electromagnetic conditions their products are designed for** and **disclaim** responsibility for problems outside them. Understanding what the statements really say protects the facility.

| Type of statement | What it usually says | What you must do |
| --- | --- |
| **Emission class (CE/FCC)** | The product meets limits for the radio noise it **emits**. **Class A** is for commercial and industrial use, **Class B** (stricter) for homes. Class A products carry a warning that they may cause radio interference in a domestic setting, and the user may have to take measures | Don't assume Class A is suitable next to sensitive receivers. Check the environment |
| **Immunity (the field it tolerates)** | It was **tested** to withstand stated levels, for example IEC 61000-4-8 at **level 3 (10 A/m, 12.6 µT)** or 3 V/m RF | Compare the levels with the **measured field** at the installation point. It is **not** a guarantee above the tested level |
| **Operating environment limits** | Temperature, humidity, vibration, and sometimes a **maximum ambient magnetic field** | Check the data sheet and install within it |
| **Installation instructions** | Separation from power cables, bonding, cable types (shielded or not) | Follow them. Deviation can void compliance and warranty |
| **Warranty exclusions** | Faults caused by environmental conditions outside the specification are not covered | Make the site conditions part of the contract and acceptance |
| **Health and exposure statements** | The product meets exposure standards (for example EN 62311 or ICNIRP-based limits) at stated distances | Doesn't remove the need to assess the whole installation |
| **Shielding product claims** | "Up to 60 dB" or "blocks 99% of EMF" | See below |

## 2. Limits of vendor statements

| Limit | Explanation |
| --- | --- |
| **Lab vs. site** | Tests use ideal fields, orientations and distances. A site has proximity to busbars, harmonics and loops |
| **"Typical" is not "guaranteed"** | Look for guaranteed (worst-case) values, with the test method and conditions |
| **Frequency range** | Immunity at 50 Hz doesn't mean immunity at 150 Hz, kHz or RF |
| **Component vs. system** | A device may be immune, but the **cabling** connected to it may pick up interference |
| **Self-declaration** | CE marking is a **manufacturer's declaration** of compliance, not an independent guarantee |
| **Shielding claims** | A material's shielding effectiveness (at a stated frequency, flat sheet) is **not** the installed effectiveness: seams, doors and penetrations dominate (7.8) |
| **Unit confusion** | Compare like with like: **A/m, µT and mG**, and **peak vs. RMS** |

### Reading an immunity statement

| Rating | Field tolerated | In µT |
| --- | --- | --- |
| IEC 61000-4-8 level 1 | 1 A/m | 1.26 µT |
| Level 2 | 3 A/m | 3.8 µT |
| Level 3 | 10 A/m | 12.6 µT |
| Level 4 | 30 A/m | 37.7 µT |
| Level 5 | 100 A/m | 125.7 µT |

A product that claims **level 3** is tested to 12.6 µT. A background of **0.05 to 0.3 µT** is far below it. But a rack **1 m from a 1,000 A busbar** could see tens of µT, so level 3 would not be enough there.

## 3. What to do

| Action | Why |
| --- | --- |
| **Ask for the full EMC declaration and test reports** | CE and FCC declarations, EN 55032 / 55035 results, IEC 61000-4-x levels |
| **Ask for the magnetic field limit** | For displays, magnetic storage media, sensors, instruments |
| **Survey the site** | Measure the real field where the equipment will stand (7.7) |
| **Keep a margin** | Don't install at the limit |
| **Put EMC conditions in the contract and acceptance tests** | So responsibility is clear |
| **Follow the installation guide** | Separation and bonding |
| **Treat shielding claims carefully** | Ask for the test method, frequency range and installed performance |

---

# 7.4 Impact of EMF

## 1. On equipment

### How fields couple into equipment and cables

| Mechanism | Explanation |
| --- | --- |
| **Inductive (magnetic) coupling** | A changing magnetic field through a **loop** induces a voltage in it (Faraday's law) |
| **Capacitive (electric) coupling** | A changing electric field couples voltage through stray capacitance |
| **Common-mode currents** | Ground potential differences and induced currents flow on cable shields and conductors (6.27 in `06-3`) |
| **Radiated RF** | Radio waves induce voltage on cables and circuit tracks |
| **Direct effect on components** | Magnetic fields deflect electron beams and affect magnetic sensors and media |

### Induced voltage in a loop

```
V = 2π f B A        (RMS, sinusoidal field; B in tesla, A = loop area in m²)
```

| B | Loop area | f | Induced voltage |
| --- | --- | --- | --- |
| 10 µT | 0.1 m² | 50 Hz | 2π × 50 × 10⁻⁵ × 0.1 = **0.31 mV** |
| 1 µT | 1 m² | 50 Hz | **0.31 mV** |
| 100 µT | 1 m² | 50 Hz | **31 mV** |

**Lesson:** the induced voltage grows with **field strength, frequency and loop area**. Large cable loops pick up much more. Twisting pairs and bundling cables **shrinks the loop area**.

### Typical effects and thresholds **[CHECK]**

| Equipment | Effect | Approximate threshold |
| --- | --- | --- |
| **CRT monitors** | Picture jitter, distortion | About **1 µT (10 mG)**, and some are affected from **0.3 to 0.5 µT (3 to 5 mG)**, large or high-resolution screens from about 0.5 µT |
| **Flat-panel displays** | Not affected at these levels | Replacing a CRT with a flat panel is the simplest fix |
| **Magnetic media (tape, older disks)** | Data errors if exposed to strong fields | Specified by the media vendor, usually far higher than normal building fields |
| **Modern servers, SSDs, network switches** | Generally tolerant of power-frequency fields, tested to levels such as 3 to 30 A/m (3.8 to 38 µT) | Check the vendor limit |
| **Sensitive instruments, magnetic sensors, laboratory equipment** | Interference at very low levels | Can be below 0.5 µT. Usually installed in controlled rooms |
| **Data cabling** | Noise and errors from induced voltage and ground loops | Reduced by separation, twisting, balanced signalling, shielding, fibre |
| **Audio and video equipment** | Hum (50/60 Hz), buzz (harmonics) | Fixed by earthing, shielding, separation |
| **Wireless links** | Degraded by RF noise | Reduced by spacing and filtering |

**Key point:** **modern IT equipment is much more immune than the old CRT**, but **cabling, displays, magnetic media and sensors** near heavy power equipment remain the weak points. Design to **keep fields at the IT space low** and **verify by measurement**.

### Effects on equipment from RF and pulses

- **RF interference** (radio transmitters, radar, mobile): disturbs analogue and digital circuits, mostly through cables. Typical immunity test levels are **1, 3, 10 and 30 V/m** (IEC 61000-4-3 levels 1 to 4) **[CHECK]**. **3 V/m** is the usual commercial level.
- **Pulses** (lightning, switching, ESD, EMP, 7.6) can **upset** (reset, corrupt data) or **damage** equipment.

## 2. On people

### How fields interact with the body

| Frequency | Main interaction | Established effects |
| --- | --- | --- |
| **ELF, IF (up to 100 kHz)** | **Induced electric fields and currents** in tissue | Perception of surface electric charge, stimulation of nerves and muscles, retinal flashes (phosphenes) at high fields |
| **RF (above 100 kHz)** | **Heating** of tissue | Whole-body and local heating at high exposure |

The established effects occur at fields **far above** those normally found in buildings.

### Exposure guidelines at 50 Hz **[CHECK]**

| Guideline | General public | Occupational |
| --- | --- | --- |
| **ICNIRP 2010** (1 Hz to 100 kHz) reference levels | **200 µT**, **5 kV/m** | **1,000 µT**, **10 kV/m** |
| **EU Council Recommendation 1999/519/EC** (public, based on ICNIRP 1998) | **100 µT**, **5 kV/m** | n/a (see the workers' directive) |
| **EU Directive 2013/35/EU** (workers) | n/a | Exposure limit values and **action levels** (low and high) |
| **IEEE C95.6** (60 Hz, 0 to 3 kHz) | about 904 µT | about 2,710 µT |
| **ACGIH threshold limit values** (60 Hz) | | about 1,000 µT and 25 kV/m |

The guidelines are set with **large safety margins** below the levels that cause established effects.

### Long-term exposure and health

- The **International Agency for Research on Cancer** classifies ELF **magnetic fields** as **possibly carcinogenic (Group 2B)**, based on epidemiological studies that associate **childhood leukaemia** with long-term average exposures above about **0.3 to 0.4 µT (3 to 4 mG)**. This remains the EU scientific committee's position **[CHECK]**.
- The association is **not shown to be causal**: laboratory and animal studies are largely negative, and no established mechanism exists. ICNIRP concludes that the evidence for chronic effects is **not strong enough** to set limits on it.
- Some countries apply **precautionary** policies (for example about **0.4 µT** for new lines near homes in the Netherlands).
- **Radio-frequency** fields from Wi-Fi and mobile equipment are far below guideline levels in normal data centre spaces.

### Special cases

| Case | Point |
| --- | --- |
| **Active implanted medical devices (pacemakers, ICDs)** | Can be disturbed by fields near strong sources. The EU workers' directive requires **risk assessment** for staff with implants and for pregnant workers |
| **Static fields** | DC battery cables create static fields. Static field limits are set separately |
| **Contact currents and microshocks** | Induced voltages on conductive objects near strong fields |

### Staff exposure in practice

- Fields inside the IT space are normally **far below** the guideline levels.
- Near **switchrooms, transformer rooms and busbars**, local fields can reach **tens to hundreds of µT** at close range, which can exceed the **public** reference level (but is generally below the **occupational** level).
- **Employers** assess and limit exposure (EU workers' directive), signpost zones, restrict access and consider staff with implants.

## 3. Summary of impacts

| Target | Impact | Control |
| --- | --- | --- |
| **IT servers and switches** | Normally negligible at building field levels | Keep within vendor immunity limits |
| **CRT displays** | Jitter from about 1 µT | Relocate, shield, or replace with flat panels |
| **Magnetic media and sensors** | Errors near strong fields | Keep away from sources, shield |
| **Cabling** | Induced noise, ground loops | Layout, balanced and shielded cable, fibre, bonding |
| **Wireless systems** | Interference | Spacing, filtering |
| **People** | Guidelines limit exposure | Assess, zone, signpost, implant precautions |
| **Equipment against pulses** | Upset or damage | Shielding, filters, SPDs (7.6, 7.8) |

---

# 7.5 Standards

Standards for EMF fall into **five families**. Know **which standard answers which question**.

## 1. Human exposure

| Standard / rule | What it is |
| --- | --- |
| **ICNIRP guidelines (2010, 1 Hz to 100 kHz)** | Reference levels and basic restrictions for time-varying electric and magnetic fields (ELF and IF) |
| **ICNIRP guidelines (2020, 100 kHz to 300 GHz)** | The radio-frequency guidelines (and the 1998 guidelines, on which the EU recommendation is based) |
| **EU Council Recommendation 1999/519/EC** | Limits for the **general public**, 0 Hz to 300 GHz. At 50 Hz: **100 µT** and **5 kV/m**. A **recommendation**, applied differently by each member state |
| **EU Directive 2013/35/EU** | **Workers**: minimum safety requirements, exposure limit values, **action levels**, risk assessment, special groups (implants, pregnancy). Mandatory through national law |
| **IEEE C95.6** (0 to 3 kHz) and **C95.1** (3 kHz to 300 GHz) | US exposure standards, with different values from ICNIRP |
| **IEC 62311** | Assessment of equipment against human exposure restrictions **[CHECK]** |
| **IEC 61786-1** | **How to measure** low-frequency magnetic and electric fields for exposure assessment |
| **National laws** | For example regulations on power lines, and workplace EMF regulations |

## 2. Equipment emissions and immunity (EMC)

| Standard | What it is |
| --- | --- |
| **EU EMC Directive 2014/30/EU, CE marking** | Equipment placed on the EU market must not emit excessive interference and must be adequately immune. **Mandatory**, shown by the manufacturer's declaration of conformity |
| **FCC Part 15 (US)** | Limits on unintentional radio emissions. **Class A** (commercial) and **Class B** (residential, stricter) |
| **CISPR 32 / EN 55032** | **Emissions** from multimedia (IT) equipment |
| **CISPR 35 / EN 55035** | **Immunity** of multimedia equipment |
| **CISPR 11 / EN 55011** | Industrial, scientific and medical equipment |
| **IEC / EN 61000-6-1, -6-2** | Generic **immunity** standards (residential and commercial, and industrial) |
| **IEC / EN 61000-6-3, -6-4** | Generic **emission** standards |
| **IEC 61000-3-2, -3-12** | Limits on **harmonic currents** drawn by equipment (links to 6.31 in `06-3`) |
| **IEC 61000-2-5** | Classification of electromagnetic environments |

### Class A and Class B

| | **Class A** | **Class B** |
| --- | --- | --- |
| **Intended for** | Commercial and industrial areas | Residential areas |
| **Emission limits** | Less strict | Stricter |
| **Warning** | May carry a warning that the product may cause interference in a domestic setting | None |
| **Data centre equipment** | Typically Class A | |

## 3. Immunity test standards (IEC 61000-4-x)

| Test | Phenomenon | Notes |
| --- | --- | --- |
| **4-2** | Electrostatic discharge (ESD) | Contact and air discharge |
| **4-3** | **Radiated RF** field | Levels about **1, 3, 10, 30 V/m** **[CHECK]**. **3 V/m** is the usual commercial level |
| **4-4** | Electrical fast transients | Switching bursts |
| **4-5** | Surge | Lightning and switching surges |
| **4-6** | Conducted RF | Induced on cables |
| **4-8** | **Power-frequency magnetic field** (50/60 Hz) | **Levels 1 to 5: 1, 3, 10, 30, 100 A/m continuous** (1.3 to 126 µT). Short-duration (1 to 3 s) **300 A/m (level 4) and 1,000 A/m (level 5)** for fault conditions |
| **4-9** | **Pulse magnetic field** | 6.4/16 µs pulse, up to 1,000 A/m, simulates a short circuit or nearby lightning |
| **4-10** | **Damped oscillatory magnetic field** | 100 kHz or 1 MHz, up to 100 A/m, simulates switchgear operations |
| **4-11** | Voltage dips and interruptions | (see the ITIC curve, 6.32 in `06-3`) |
| **4-25** | **HEMP** immunity | See 7.6 |
| **4-36** | **IEMI** (intentional EMI) | High-power microwave |

### IEC 61000-4-8 environment classes **[CHECK]**

| Level | Field | Typical environment |
| --- | --- | --- |
| 1 | 1 A/m (1.3 µT) | Well-protected (residential area away from industrial sources) |
| 2 | 3 A/m (3.8 µT) | Typical residential and commercial |
| 3 | 10 A/m (12.6 µT) | Industrial and tertiary buildings, moderate power equipment |
| 4 | 30 A/m (37.7 µT) | **Severe industrial**, close to transformers or high-current conductors |
| 5 | 100 A/m (126 µT) | Conductors, busbars or MV/HV lines carrying **tens of kiloamperes**, lightning-protection ground conductors |

**In practice:** "Class n requires Level n". The IEC standard **does not** cover disturbances coupled into **cables**: that is dealt with by other tests (surge, fast transient, conducted RF).

## 4. Installation, siting and cabling

| Standard | What it covers |
| --- | --- |
| **EN 50174-1, -2, -3** | Cabling installation: specification, planning (including **separation of power and data**, 6.18 in `06-2`) and outdoor |
| **ISO/IEC 14763-2** | Planning and installation of cabling |
| **IEC 61000-5-x** | EMC installation and mitigation guidance (including HEMP protection concepts) |
| **EN 50310, ANSI/TIA-607, ISO/IEC 30129** | Bonding networks (6.26 in `06-2`) |
| **ANSI/TIA-942, EN 50600-2-1** | Data centre site and building requirements: the computer room is to be located **away from sources of electromagnetic interference**. Commonly quoted TIA-942 guidance limits ambient EMI to about **3 V/m (0 to 3 GHz)** **[CHECK]** |
| **IEC 62305, IEC 61643** | Lightning protection and surge protective devices |

## 5. Shielding, pulses and facilities

| Standard | What it covers |
| --- | --- |
| **IEEE 299** | Measuring the **shielding effectiveness** of enclosures with all dimensions of 2 m or more (and **IEEE 299.1** for 0.1 to 2 m) |
| **EN 50147-1** | Shielding effectiveness of shielded enclosures **[CHECK]** |
| **MIL-STD-188-125-1** | **HEMP** protection for ground-based critical facilities, with shielding of **80 dB (10 MHz to 1 GHz)** and **20 dB at 10 kHz**, and pulse current injection tests on every penetration |
| **MIL-STD-461** | Military EMI requirements (RS105 reproduces the E1 pulse at equipment level) |
| **IEC 61000-2-9, 2-10** | HEMP environment descriptions (radiated and conducted) |
| **IEC 61000-5-5** | Specification of protective devices for conducted HEMP disturbance |
| **NERC TPL-007 (US)** | Geomagnetic disturbance vulnerability assessments for bulk power operators |

## 6. Which standard for which question

| Question | Standard |
| --- | --- |
| Is the field safe for **people**? | ICNIRP 2010, EU 1999/519/EC (public), 2013/35/EU (workers), IEEE C95.6 |
| How do I **measure** it? | IEC 61786-1 |
| Will my **equipment** tolerate the field? | IEC 61000-4-8 (50/60 Hz), -4-9, -4-10; EN 55035 |
| Will my equipment **disturb others**? | EN 55032, FCC Part 15, EMC Directive |
| How far apart should **power and data cables** be? | EN 50174-2 |
| How do I **test a shielded room**? | IEEE 299 |
| How do I protect against **EMP**? | MIL-STD-188-125-1, IEC 61000-2-9 and 4-25 |
| How do I protect against **lightning**? | IEC 62305, IEC 61643 |

## 7. Mandatory or voluntary

| Item | Status |
| --- | --- |
| **EU EMC Directive and CE marking, FCC Part 15** | **Mandatory** for products sold in those markets |
| **EU workers' directive** | **Mandatory** through national law |
| **EU public recommendation, ICNIRP, IEEE** | Guidance, widely adopted, binding only where a country makes it law |
| **Installation standards (EN 50174, TIA-942, EN 50600)** | Voluntary unless contract or specification requires them |
| **Shielding and EMP standards** | Voluntary, except for government specifications |

---

# 7.6 EMP (electromagnetic pulse)

## 1. What an EMP is

An **electromagnetic pulse** is a **short, intense burst of electromagnetic energy** that can **upset or damage electronics** over a wide area or inside a facility. Unlike the steady 50/60 Hz fields of 7.1 to 7.4, EMP is **transient**.

## 2. Sources of pulses

| Type | Cause | Notes |
| --- | --- | --- |
| **HEMP** (high-altitude EMP) | A nuclear detonation above about 30 km | **Wide-area** effect, three components (E1, E2, E3) |
| **SREMP** | Source-region EMP from a nuclear burst near the ground | Local to the blast region |
| **IEMI / NNEMP** | **Intentional** electromagnetic interference: non-nuclear weapons, high-power microwave | Local, deliberate attack |
| **LEMP** | **Lightning** electromagnetic pulse | Direct strikes and the surrounding magnetic and electric fields |
| **ESD** | Electrostatic discharge | Small, but frequent |
| **Switching** | Breaker and switchgear operations | Fast transients on power lines |
| **GMD** (geomagnetic disturbance) | **Solar storms** distorting the Earth's field | Slow, affects long conductors and transformers (similar to E3) |

## 3. The three components of HEMP **[CHECK]**

| Component | Time scale | Character | Main effect |
| --- | --- | --- | --- |
| **E1** (early time) | **Nanoseconds**: rises in about **2.5 ns**, with a peak up to about **50 kV/m**, energy mostly from about **1 MHz to a few hundred MHz** | Very fast, strong electric field | Couples into cables and small apertures. **Damages semiconductors** and control electronics. The most severe threat to IT equipment |
| **E2** (intermediate) | Microseconds to a second, about **100 V/m** | Resembles **lightning** | Normally handled by lightning protection. But E1 may already have damaged the protection |
| **E3** (late time) | **Seconds to hundreds of seconds**, about **40 V/km** | Slow, like a severe **solar storm** but stronger | Induces quasi-DC currents (**GIC**, geomagnetically induced currents) in **long conductors**: transmission lines and pipelines. **Saturates large transformers** and can collapse the grid |

**Historical references for solar storms:** the Carrington event of 1859 and the March 1989 geomagnetic storm that brought down the Hydro-Québec grid in about 90 seconds.

## 4. How the pulse reaches equipment

| Path | Explanation |
| --- | --- |
| **Radiated (direct) field** | The field couples into unshielded equipment, wiring and circuit tracks |
| **Conducted via cables** | **Power, data, antenna, telephone, pipe and conduit** penetrations carry induced surges into the building (every conductor that crosses the boundary is a path) |
| **Aperture coupling** | Vents, seams, windows and gaps |
| **Grounding** | Induced currents through earth connections |

## 5. Why ordinary protection is not enough

| Issue | Detail |
| --- | --- |
| **Surge protectors too slow for E1** | Metal-oxide varistors clamp in roughly 1 to 25 ns, comparable to or slower than E1's whole rise time. Specialist hybrid devices are needed |
| **Standard buildings shield little** | A six-sided **metal** building gives roughly **20 to 30 dB**. **Concrete or masonry** gives **under 10 dB** **[CHECK]** |
| **Long cables are antennas** | The longer the cable, the more current is induced |
| **Grid failure follows E3** | The data centre can lose its utility supply for a long time |

## 6. Protection concept

| Layer | Measure |
| --- | --- |
| **Shielded enclosure (Faraday cage)** | The primary defence against radiated E1. A **continuous conductive shield** around the protected area |
| **Treat every penetration** | **Filter** power and signal conductors at the point of entry (POE). Use **waveguide-below-cutoff (WBC)** for ventilation and pipes. Use **fibre optic** (non-metallic) links with a non-conductive entry. RF-tight doors with finger stock |
| **Surge protective devices and fast hybrid protectors** | Fast enough for E1, coordinated with filters |
| **Grounding and bonding** | A single-point or well-planned bonding network, bonded to the shield, so induced current is dissipated |
| **Backup power independence** | On-site generation and fuel, ability to **island** from the grid, a **spare** transformer plan |
| **Operational plan** | Risk assessment, protected spares, recovery procedures |
| **Testing** | Shield and penetration tests (IEEE 299, MIL-STD-188-125-1, pulse current injection) |

**MIL-STD-188-125-1** for HEMP-hardened facilities requires about **80 dB** of shielding from **10 MHz to 1 GHz**, **20 dB at 10 kHz**, and tests with **pulse current injection** (E1: 20/500 ns, 2.5 kA peak; E2: 1.5/4,000 µs, 250 A; E3: 0.2/20 s, 1,000 A) on **every penetration**.

### Worked example: what shielding buys

The incident E1 field is **50 kV/m**:

| Building or shield | Shielding effectiveness | Field inside |
| --- | --- | --- |
| Concrete or masonry | about 10 dB (×3.2) | about **15.8 kV/m** |
| Six-sided metal building | about 25 dB (×17.8) | about **2.8 kV/m** |
| MIL-STD-188-125-1 enclosure | 80 dB (×10,000) | **5 V/m** |

Even 5 V/m is above a typical 3 V/m RF immunity level, which is why **filtering at penetrations** and **protected equipment** are still needed behind the shield.

## 7. Is it a requirement for a data centre?

- **HEMP hardening** is normally required only for **government, military and designated critical infrastructure** facilities.
- **Commercial** data centres more often face **lightning**, **switching surges**, **ESD**, **solar storms (GMD)** and local **IEMI**, handled with **lightning protection, SPDs, bonding, filtering, shielding where needed, and grid resilience**.
- The decision is **risk-based**: the likelihood, the impact of loss, and the cost of protection.

## 8. Solar storms and the grid

E3 and geomagnetic storms drive **GIC** through transformer windings, causing **half-cycle saturation**, **harmonics**, **overheating**, and **reactive power demand**, and can bring down transmission grids. Mitigation is mostly at the **utility** level (blocking devices, operating procedures, **NERC TPL-007** assessments), so a data centre depends on **resilience to a long grid outage**: **on-site generation, adequate fuel, and the ability to island**.

---

# 7.7 Design and installation

## 1. Design process

| Step | What to do |
| --- | --- |
| **1. Identify the sensitive equipment** | Displays, magnetic media, instruments, wireless links, and the cabling serving them. Get the **vendor immunity limits** (7.3) |
| **2. Set design targets** | For example: keep fields below about **1 µT (10 mG)** at displays and sensitive points, below about **0.3 µT** for very sensitive equipment **[CHECK]**, and far below the exposure guidelines for people |
| **3. Survey existing sources** | Utility lines, substations, transformers, radio transmitters, radar, railways (Module 3 site selection) |
| **4. Plan the layout** | Put the high-field equipment away from the IT space |
| **5. Design the electrical system for low field** | Cable and busbar arrangements, balance, earthing |
| **6. Add shielding only where needed** | After distance and layout (7.8) |
| **7. Verify** | Measure before and after energising |
| **8. Maintain** | Re-survey after changes, keep records |

## 2. Siting and layout

| Rule | Reason |
| --- | --- |
| **Choose a site away from high-voltage lines, substations, transmitters and radar** | Fields from them are outside your control |
| **Place transformers, switchgear, UPS, busbars and main cable routes away from the white space** | Fields fall quickly with distance |
| **Avoid electrical rooms directly above, below or next to the computer room** | **Magnetic fields pass through concrete floors and walls**. A stairwell or storage room between helps |
| **Keep risers and main feeders out of IT areas** | A riser carries the whole building's current |
| **Put sensitive equipment (displays, magnetic media, instruments) on the far side of the room from sources** | Even a few metres makes a large difference |
| **Mark field-zone boundaries** | For staff and visitors (people with implants) |
| **Allow for growth** | Currents rise as the load grows |

## 3. Electrical design for low fields

| Measure | Explanation |
| --- | --- |
| **Keep go and return conductors together** | Bundle or lay in **trefoil**: all three phases (and the neutral and PE) in the **same cable or raceway**. The fields cancel |
| **Prefer tightly spaced cables or low-field busway to widely spaced busbars** | Busbars have large spacing, so a conventional busbar run can produce more field than the same current in tight cables. Choose **bundled or low-EMF busway** designs where fields matter |
| **Parallel single-core cables: use a cross-phase arrangement** | Each group contains **one cable of every phase**, avoiding circulating currents and uneven fields |
| **Route feeders by the shortest path, away from sensitive areas** | Less length and less exposure |
| **Balance the phases** | Reduces neutral current (6.17 in `06-2`) |
| **TN-S and a single neutral-earth bond** | Prevents neutral current from flowing in the structure (6.26 in `06-2`). **Never change the bonding to cut fields without an engineer's design**, as it is a safety system |
| **Common bonded network, no ground loops** | Reduces circulating currents and common-mode noise (6.27 in `06-3`) |
| **Keep PE conductors with the phase conductors** | Return paths stay close |
| **Battery (DC) cables: run the positive and negative together** | Cancels the static field |
| **Avoid large cable loops** | Loop area sets the induced voltage |
| **Control harmonics** | Low-THDi UPS and drives reduce harmonic fields and neutral current (6.31 in `06-3`) |
| **Use EMC-compliant equipment** | Lighting drivers, power supplies, drives |
| **Non-magnetic glands and supports for single-core cables** | Avoids eddy-current heating and extra fields from steel parts **[CHECK]** |

## 4. Cabling for immunity

| Measure | Explanation |
| --- | --- |
| **Separate power and data cables** | Per EN 50174-2 (6.18 in `06-2`). **Cross at 90°** |
| **Metal containment** | Closed steel trays and conduits can reduce or remove the required separation under EN 50174-2:2018 |
| **Twisted-pair, balanced cabling** | Noise is induced equally on both conductors and rejected |
| **Shielded cable where the field is high or interference is likely** | Terminate screens correctly (360° at the connector). Bond at **both ends** only where the bonding network is equipotential, otherwise a ground loop can carry current |
| **Fibre optic cable** | Immune to magnetic fields and ground potential differences. Use it in or near high-field areas |
| **Keep cable runs short and tidy** | Reduces antenna length and loop area |
| **Bond racks and trays** | One bonded network |

## 5. Worked example: how far to the displays?

A feeder carries **1,000 A**. The design target at displays is **1 µT**. Using the go-and-return estimate **B ≈ 2 × 10⁻⁷ × I × s / r²** (simplified **[CHECK]**):

| Arrangement | Distance for 1 µT |
| --- | --- |
| Tight bundle, s = 0.1 m | r = √(2 × 10⁻⁷ × 1,000 × 0.1 / 10⁻⁶) = √20 = **4.5 m** |
| Busbar spacing, s = 0.3 m | r = √60 = **7.7 m** |
| Single conductor with the return **far away** (net current) | r = 2 × 10⁻⁷ × 1,000 / 10⁻⁶ = **200 m** |

The third line shows why **net current** (stray return currents) is the worst case, and why the **earthing and cable layout** matter as much as the distance.

**A second example (1,500 A, tight bundle, s = 0.1 m):** r = √(2 × 10⁻⁷ × 1,500 × 0.1 / 10⁻⁶) = √30 = **5.5 m**.

## 6. Mitigation hierarchy

| Order | Approach |
| --- | --- |
| **1** | **Avoid**: choose the site and layout so sources are far from sensitive areas |
| **2** | **Reduce at the source**: cable and busbar arrangement, balance, earthing, low-harmonic equipment |
| **3** | **Increase distance** |
| **4** | **Shield** the source or the victim (7.8) |
| **5** | **Compensate**: passive or active cancellation loops |
| **6** | **Replace or relocate the sensitive equipment** (for example CRT with flat panel) |
| **7** | **Operational controls**: access zones, staff with implants |

## 7. Measurement and verification

| Item | Practice **[CHECK]** |
| --- | --- |
| **Instrument** | A calibrated **three-axis (isotropic) magnetic field meter** with true-RMS reading, and a frequency range covering 50/60 Hz and the harmonics (IEC 61786-1) |
| **Method** | Map the area on a **grid**, commonly at **1 m above the floor**, and also at the position of sensitive equipment |
| **Load conditions** | Record the **load currents** at the time (fields scale with current). Ideally also at **peak load** |
| **Baseline** | Measure **before** installing equipment (background) and **after** energising |
| **Analysis** | Compare with the vendor immunity limits and the design target. Scale to **maximum load** (B is proportional to I) |
| **Electric fields** | Measure where relevant (for example near high-voltage equipment) |
| **Records** | Keep the survey, and **re-survey after changes** (new transformer, new busway, load growth) |
| **Safety** | Surveys near live equipment follow electrical safety rules |

**Scaling to peak load.** A reading of **0.4 µT at 300 A** corresponds to 0.4 × (1,000 / 300) = **1.3 µT at 1,000 A**.

## 8. Installation checks

- Cable and busbar arrangements as designed (bundled, all phases and neutral together).
- **Phase order, cross-phase arrangement** for parallel cables.
- **Neutral-earth bond** at one point only. No neutral current in earth conductors.
- Power and data **separation**, **90° crossings**, bonded trays.
- **Shield terminations**, bonding at connectors, **fibre** where specified.
- **Shielding and penetrations** built and tested (7.8).
- **Post-energisation survey** and records.

---

# 7.8 Shielding

## 1. The principle

Shielding places a **conductive or magnetic barrier** between the source and the equipment so the field inside is weaker.

### Shielding effectiveness (SE)

```
SE (dB) = 20 × log₁₀ (field without shield / field with shield)
```

| SE | Field reduced by a factor of |
| --- | --- |
| 20 dB | 10 |
| 40 dB | 100 |
| 60 dB | 1,000 |
| 80 dB | 10,000 |
| 100 dB | 100,000 |

## 2. Three kinds of shielding, three mechanisms

| Field | Mechanism | Materials | Difficulty |
| --- | --- | --- | --- |
| **Electric field (E)** | A grounded **continuous conductor** redistributes charge and cancels the field inside (reflection) | Any metal: copper, aluminium, steel, mesh, foil | **Easy**: a thin conductor gives more than 70 dB |
| **High-frequency electromagnetic waves (RF)** | **Reflection and absorption** by a conductor: SE = reflection loss + absorption loss | Copper, aluminium, steel, mesh | Easy to moderate. Limited by **apertures and seams** |
| **Low-frequency magnetic field (50/60 Hz)** | (a) **Flux shunting**: a high-permeability material gives the field lines an easier path around the protected space, and (b) **eddy currents** in thick conductors | **Mu-metal, steel** (shunting), **thick aluminium or copper** (eddy currents) | **Hard** |

## 3. Why a Faraday cage does not stop 50/60 Hz magnetic fields

- A **thin** copper or aluminium box stops electric fields and radio waves, but **barely affects** a 50/60 Hz **magnetic** field: the field is too slow to induce enough opposing eddy current in thin metal.
- **Grounding the cage does not change this.** Grounding helps with the **electric** field only. **Magnetic shielding does not depend on earth**.
- Aluminium **foil** is much thinner than the skin depth at 50/60 Hz and gives almost nothing.

## 4. Skin depth

The depth at which an AC field in a conductor falls to 37% of its surface value:

```
δ = 1 / √(π × f × µ × σ)       µ = µ₀ × µr,   σ = conductivity
```

| Material | δ at 50 Hz | δ at 1 MHz |
| --- | --- | --- |
| **Copper** | **9.3 mm** | 66 µm |
| **Aluminium** | **11.6 mm** | about 82 µm |
| **Mild steel** (µr ≈ 200 at low frequency) | **about 1.6 mm** | (steel permeability falls at high frequency, so the figure doesn't apply) |
| **Mu-metal** (µr in the tens of thousands) | well under 1 mm when annealed (a few tenths of a mm) | |

Absorption loss is **8.7 dB per skin depth**:

```
A (dB) = 8.686 × t / δ        (t = thickness)
```

### Worked example: how thick for 40 dB at 50 Hz (absorption only)

```
t = (40 / 8.686) × δ = 4.6 δ
Copper:       4.6 × 9.3 mm  = about 43 mm
Aluminium:    4.6 × 11.6 mm = about 53 mm
Mild steel:   4.6 × 1.6 mm  = about 7.3 mm
```

A **3 mm** plate gives only: copper **2.8 dB**, aluminium **2.2 dB**, mild steel **16 dB**. That is why **ordinary sheet metal and thin enclosures are almost useless against 50/60 Hz magnetic fields** and why steel does much better than copper or aluminium per millimetre.

A measured example: a 2 m aluminium enclosure with 45 mm walls (about four skin depths at 50 Hz) reached about **40 dB** over part of the volume.

### Typical shielding performance at 60 Hz **[CHECK]**

| Material | Approx. SE |
| --- | --- |
| Aluminium or copper, sheet metal thickness | under 5 dB |
| Steel (µr 200 to 500) | about 10 to 30 dB |
| **Mu-metal, about 1 mm** | about **30 to 60 dB** |
| Mu-metal, 0.5 mm | about 30 to 40 dB |

## 5. Practical magnetic shielding

| Approach | Notes |
| --- | --- |
| **Shield the source** | Enclose or screen the **busbar, cable run or transformer**. A **conductive plate (aluminium)** in front of busbars reduces the field by eddy currents. For good results the plate should be **at least twice the size** of the busbar system and placed **symmetrically**, with enough thickness (relative to skin depth) and spacing. Aluminium is as effective as copper for much less cost |
| **Shield the victim** | A mu-metal or steel box around a single device (a display, a sensor, a tape drive). Specific materials such as a **60 Hz shielding sheet** around a monitor |
| **Shield the room** | Possible but expensive: **every penetration** (data, power, lighting, services) must be treated, and the field passes through concrete, so the whole envelope matters |
| **Multi-layer shields** | A high-saturation outer layer for the bulk flux and a high-permeability inner layer for fine attenuation |
| **Mu-metal handling** | Its permeability **drops sharply** after forming, welding or bending, so it must be **heat-treated (annealed) after fabrication**. It is expensive, soft and fragile |
| **Seams and openings** | Overlap or weld seams. Apertures and cable entries leak flux |
| **Compensation loops** | Passive loops or active coils that generate an opposing field |
| **Distance** | Usually **cheaper than shielding**, so use it first (7.7) |

**Cost-effectiveness:** for power-frequency fields it is almost always better to **cut the source** (bundle the conductors, balance the currents, fix the earthing, move the equipment) than to shield.

## 6. RF and EMP shielding (shielded rooms and enclosures)

| Item | Practice **[CHECK]** |
| --- | --- |
| **Construction** | Continuous conductive envelope: steel or copper sheet or mesh on all **six sides** (floor, walls, ceiling) |
| **Performance** | Typically **60 to 120 dB** for well-built RF rooms. HEMP facilities about **80 dB** (10 MHz to 1 GHz) |
| **Seams** | Welded, or bolted with conductive gaskets. Conductive tape is not a permanent seam |
| **Doors** | RF doors with **beryllium-copper finger stock** compressing against the frame. For HEMP a two-door entryway with a waveguide-below-cutoff passage |
| **Power and signal entries** | **Filters** on every conductor |
| **Ventilation and pipes** | **Waveguide-below-cutoff (WBC)** honeycomb panels and pipes |
| **Fibre optic** | Feed through a **non-conductive** waveguide |
| **Grounding** | The shield is bonded to the bonding network. This is essential for E-field and EMP protection, but irrelevant to magnetic shielding |
| **Testing** | **IEEE 299** (large enclosures), with antennas inside and outside, and sweeps of frequency. Re-test periodically, since gaskets and finger stock wear |

### The aperture problem

Shielding is limited by the **largest opening**, not the wall material. A slot of length **L** passes waves with half-wavelength greater than L:

```
SE ≈ 20 × log₁₀ ( λ / (2 L) )       (a simplified estimate)
```

**Worked example.** A **30 mm** slot at **1 GHz** (λ = 0.3 m): SE ≈ 20 log₁₀(0.3 / 0.06) = **14 dB**. At 100 MHz (λ = 3 m): SE ≈ 34 dB. A thick, perfect wall doesn't help: the slot sets the limit. Real rooms therefore use **many small openings**, gaskets and WBC panels.

### Waveguide below cutoff

A tube or honeycomb cell with diameter **d** blocks waves below its **cutoff frequency**:

```
f_c ≈ 175.8 / d     (f_c in GHz, d in mm, for a circular opening)
Attenuation ≈ 27.3 × (length / d)  dB      (well below f_c)
```

A **6 mm** hexagonal cell has f_c ≈ 29 GHz, far above the E1 band. A cell **25 mm long** attenuates by about 27.3 × 25 / 6 = **114 dB**.

## 7. Cable shielding

| Point | Detail |
| --- | --- |
| **What a cable screen does** | Intercepts **electric fields and RF**. It does **little against 50/60 Hz magnetic fields** (hum): that is controlled by **twisted pairs**, balanced signalling and small loops |
| **Screen types** | Foil, braid, or both (braid for low frequencies, foil for high). Shielded twisted pair (STP, F/UTP, S/FTP) |
| **Termination** | 360° bond at the connector. A pigtail leaks at high frequency |
| **Grounding** | Where the bonding network is equipotential, bond **both ends**. Otherwise use one end to avoid a **ground loop** (a screen carrying circulating current becomes a source of noise). A standards rule of thumb treats more than about **1 V** between a screen and the equipment's power ground as a problem **[CHECK]** |
| **Metal containment** | **Closed steel trays and conduits** help against E-fields and let you reduce the separation from power cables (6.18 in `06-2`). Open ladder trays give little |
| **Fibre** | Needs no shield and is immune |

## 8. Shielding in the design sequence

| Step | Action |
| --- | --- |
| 1 | Avoid and reduce at the source (7.7) |
| 2 | Increase distance |
| 3 | Shield only the sources or victims that still need it |
| 4 | Treat **seams, doors, openings and penetrations** first: they decide the result |
| 5 | **Test** the finished shield and keep a maintenance programme |

## 9. Summary by field type

| Field | Best approach | Typical SE |
| --- | --- | --- |
| **Electric field (E)** | Grounded continuous conductor (even thin) | Over 70 dB |
| **RF** | Conductive room or enclosure with filtered and WBC penetrations | 60 to 120 dB |
| **EMP (E1)** | MIL-STD-188-125-1 type shield, filters, fast protectors, bonding | 80 dB |
| **50/60 Hz magnetic** | Cut the source and keep distance. If needed: mu-metal or steel enclosures, thick aluminium plates at the source | 10 to 40 dB, hard to exceed |
| **Static magnetic (DC)** | Mu-metal or steel (flux shunting), distance. Conductors give nothing | |

---

## Glossary

| Term | Meaning |
| --- | --- |
| EMF | Electromagnetic field (electric and magnetic parts) |
| E-field / B-field | Electric field (V/m) / magnetic flux density (T, µT, mG) |
| H | Magnetic field strength (A/m). 1 A/m = 1.2566 µT |
| ELF / IF / RF | 0 to 300 Hz / 300 Hz to 100 kHz / 100 kHz to 300 GHz |
| Non-ionising | Radiation without enough energy to break chemical bonds |
| Near field / far field | Region where E and H are independent / where they form a wave (E/H = 377 Ω) |
| Net current | Sum of all currents in a conductor group. Non-zero means a slowly decaying field |
| Trefoil | Three phase cables laid in a triangle, close together |
| Immunity / emission | Tolerance of interference / interference produced |
| EMC | Electromagnetic compatibility |
| Class A / Class B | Commercial and industrial / residential emission limits |
| ICNIRP | International Commission on Non-Ionizing Radiation Protection |
| IARC 2B | "Possibly carcinogenic" classification of ELF magnetic fields |
| Action level | Measured field level in the EU workers' directive that triggers measures |
| EMP / HEMP | Electromagnetic pulse / high-altitude EMP |
| E1, E2, E3 | Early (fast), intermediate (lightning-like) and late (slow) HEMP components |
| GMD / GIC | Geomagnetic disturbance / geomagnetically induced current |
| IEMI | Intentional electromagnetic interference |
| LEMP | Lightning electromagnetic pulse |
| POE | Point of entry (where a conductor crosses a shield) |
| WBC | Waveguide below cutoff |
| SE | Shielding effectiveness, in dB |
| Skin depth (δ) | Depth at which an AC field falls to 37% in a conductor |
| Mu-metal | High-permeability nickel-iron alloy for magnetic shielding |
| Flux shunting | Magnetic shielding by giving the flux an easy path around the protected space |
| Faraday cage | Conductive enclosure that blocks electric fields and RF |

## Exam takeaways

**7.1 to 7.2: fields and sources**

- **Voltage makes the electric field (V/m). Current makes the magnetic field (A/m, µT, mG).** **1 µT = 10 mG**, **1 A/m = 1.26 µT**.
- Mains power is **ELF (50/60 Hz)**: wavelength thousands of km, so E and B are **independent** and always in the near field.
- **Single conductor: B = 2 × 10⁻⁷ I / r** (falls as 1/r). **Go-and-return pair: B ≈ 2 × 10⁻⁷ I s / r²** (falls as 1/r²). **Bundling cuts the field.**
- **Net current** (return current elsewhere) makes long-range fields. **TN-C, multiple neutral-earth bonds, unbalanced phases and ground loops** cause it.
- The main sources in a data centre are **transformers, busbars, large cables, switchboards, UPS and battery cables, and drives**, not the servers.

**7.3 to 7.5: vendors, impact and standards**

- Read vendor statements carefully: **tested immunity levels** (IEC 61000-4-8 level 3 = 10 A/m = 12.6 µT) are not guarantees above that level. **CE is a self-declaration.** Ask for reports, and put EMC conditions in the contract.
- **CRT monitors** jitter from about **1 µT (10 mG)**. Modern equipment is more tolerant. **Induced voltage in a loop: V = 2π f B A.**
- **Exposure:** ICNIRP 2010 (50 Hz) public **200 µT / 5 kV/m**, occupational **1,000 µT / 10 kV/m**. **EU recommendation 100 µT** (public). **EU Directive 2013/35/EU** for workers. **IARC 2B**, association with childhood leukaemia above about **0.3 to 0.4 µT**, not shown to be causal.
- **Standards:** **IEC 61000-4-8** (50/60 Hz magnetic immunity, levels 1 to 5), **-4-9** (pulse), **-4-10** (damped oscillatory), **-4-3** (radiated RF, 3 V/m), **EN 55032/55035** (emission/immunity), **EN 50174-2** (cable separation), **IEC 61786-1** (measurement), **IEEE 299** (shielding tests), **MIL-STD-188-125-1** (HEMP).

**7.6 to 7.8: EMP, design and shielding**

- **HEMP: E1** (ns, ~50 kV/m, damages electronics), **E2** (like lightning), **E3** (slow, GIC, transformers). **Surge protectors too slow for E1.** Protect with a **shield, filtered penetrations, WBC, fibre, fast protectors, bonding.** MIL-STD-188-125-1: **80 dB**.
- **Design:** avoid and reduce at the source first: **site and layout, bundled conductors, all phases and neutral together, balanced phases, TN-S with one bond, cross-phase arrangement, fibre, separation.** **Measure** with a 3-axis meter under load, before and after energising.
- **Shielding:** **SE (dB) = 20 log₁₀ (field before / field after)**. **E-field: easy** (grounded conductor). **50/60 Hz magnetic: hard**: thin Faraday cages **don't work**, grounding doesn't help, needs **mu-metal/steel or very thick aluminium/copper**. **Skin depth** copper 9.3 mm at 50 Hz. **Apertures and seams limit real shielding.** **Distance beats shielding.**

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **ICNIRP 2010** (1 Hz to 100 kHz), **ICNIRP 2020** (RF) | Human exposure reference levels |
| **EU Council Recommendation 1999/519/EC** | Public exposure limits |
| **EU Directive 2013/35/EU** | Worker exposure: limit values, action levels, risk assessment |
| **IEEE C95.6**, **ACGIH** TLVs, **IARC** classification | Other exposure values and the cancer classification |
| **IEC 61786-1**, **IEC 62311** | Measurement and assessment of exposure |
| **EU EMC Directive 2014/30/EU**, **CISPR 11, 32, 35** (EN 55011, 55032, 55035) | Equipment emission and immunity |
| **IEC 61000** series: -2-5, -2-9, -3-2, -4-3, -4-8, -4-9, -4-10, -4-25, -4-36, -5-5, -6-1, -6-3 | Environments, harmonic emission, immunity tests, HEMP, generic standards |
| **EN 50174-1 and -2**, **ISO/IEC 14763-2**, **EN 50310**, **ANSI/TIA-607** | Cabling installation and bonding |
| **ANSI/TIA-942**, **EN 50600** | Siting away from EMI sources |
| **IEEE 299**, **IEEE 299.1**, **EN 50147-1** | Shielding effectiveness measurement |
| **MIL-STD-188-125-1**, **MIL-STD-461** | HEMP protection and equipment EMI requirements |
| **IEC 62305**, **IEC 61643**, **NERC TPL-007** | Lightning, surge protection and grid vulnerability to geomagnetic disturbance |
| Standard electromagnetics | Ampère's and Faraday's laws, skin depth and shielding formulas |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
