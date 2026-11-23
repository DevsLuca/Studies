# Module 6, Part C: Power Quality and Sizing (lessons 6.27 to 6.35)

Detailed notes, following the lesson-level index of the EPI course. This is the third of four Module 6 files (see `06-1` for lessons 6.1 to 6.14 and `06-2` for 6.15 to 6.26).

| Lesson | Title | Section |
| --- | --- | --- |
| 6.27 | Common Mode Noise (CMN) | [Section 1](#627-common-mode-noise-cmn) |
| 6.28 | Distribution Board (DB) | [Section 2](#628-distribution-board-db) |
| 6.29 | Ingress Protection (IP) Grades | [Section 3](#629-ingress-protection-ip-grades) |
| 6.30 | Power Quality Guidelines | [Section 4](#630-power-quality-guidelines) |
| 6.31 | Harmonics | [Section 5](#631-harmonics) |
| 6.32 | CBEMA Curve | [Section 6](#632-cbema-curve) |
| 6.33 | Power Factor | [Section 7](#633-power-factor) |
| 6.34 | Label Power versus Consumed Power | [Section 8](#634-label-power-versus-consumed-power) |
| 6.35 | Sizing Power | [Section 9](#635-sizing-power) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#part-c-lessons-627-to-635) |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course.
>
> The physics (kVA, power factor, harmonics basics) is in `06a_electrical_physics_foundations.md`. Generator sizing with the harmonic multiplier is in `06-1` (6.10), and the EN 50160 supply limits are in `06-1` (6.5).

---

# 6.27 Common mode noise (CMN)

## 1. Two modes of signals and noise

| Mode | What it is |
| --- | --- |
| **Differential (normal) mode** | The wanted signal: current flows **out on one conductor and back on the other** (opposite directions). The receiver reads the voltage **between** the two conductors |
| **Common mode** | Noise that appears **in phase and with equal size on both conductors**, measured against ground. Current flows in the **same direction** on both, returning through ground or stray capacitance |

```
 Differential:   signal ──►  wire 1  ──► receiver
                 signal ◄──  wire 2  ◄── receiver        (equal and opposite)

 Common mode:    noise  ──►  wire 1  ──┐
                 noise  ──►  wire 2  ──┴──► receiver ──► ground    (same direction)
```

An **ideal** differential receiver ignores common-mode noise. A **real** one has finite balance, so some common-mode noise is **converted** into differential error that corrupts the signal.

## 2. Sources

| Source | Why |
| --- | --- |
| **Ground potential differences and ground loops** | Two points that should be at the same voltage aren't, so current is driven through cable shields and signal lines |
| **Switch-mode power supplies, UPS inverters, variable-speed drives** | Fast switching edges (high dv/dt) couple noise through stray capacitance to ground |
| **Electromagnetic interference** | Radiated energy from motors, fluorescent lighting, radio sources and power cables couples onto cables, appearing on both conductors |
| **Poor bonding and wrong neutral-ground bonds** | Neutral current in earth conductors creates voltage between "grounds" (see TN-C, multiple bonds) |
| **Switching transients and lightning** | Surges raise the potential of one conductor group relative to another |
| **Long, unshielded cable runs** | Act as antennas |

## 3. Effects

- **Data errors** and retransmissions, reduced link speed.
- **Equipment resets**, nuisance trips, communication failures.
- **Hum** in audio and video equipment.
- **Radiated emissions** (common-mode currents on cables radiate strongly).
- **Stress** on isolation barriers and surge devices.

In the **power** system, common-mode noise shows up as voltage between **neutral and ground** (N–G voltage) and as noise on the supply conductors relative to the protective earth.

## 4. Measuring and limits **[CHECK]**

| Measurement | Notes |
| --- | --- |
| **Neutral-to-ground voltage** | Measure with a true-RMS meter. Practitioners treat roughly **1 to 2 V** as the level to investigate, and a few volts as a clear problem. It should be near zero at the load if neutral and ground are bonded at one point close by |
| **Shield-to-outlet-ground voltage** | Cabling standards treat **more than about 1 V rms** between a cable screen and the ground of the equipment's power outlet as a sign of improper grounding |
| **Common-mode current** | Clamp-on current probe around the whole cable, with a spectrum analyser |
| **CMRR** (common-mode rejection ratio) | How much a receiver rejects common-mode signals: **CMRR (dB) = 20 × log₁₀(differential gain ÷ common-mode gain)** |

### Worked example: CMRR

A receiver with **CMRR = 80 dB** sees a **1 V** common-mode disturbance:

```
Error = 1 V / 10^(80/20) = 1 V / 10,000 = 100 µV
```

A **60 dB** receiver with **2 V** of common-mode noise gives 2 V / 1,000 = **2 mV**. CMRR falls as frequency rises, so a link that is fine at low frequency can fail at high speed.

## 5. Mitigation

| Measure | How it helps |
| --- | --- |
| **Single neutral-ground bond** and a **common bonded network** | Removes the voltage differences that drive common-mode currents (6.26) |
| **Short, low-impedance bonding** and a **signal reference grid** | Keeps equipment at the same potential at high frequency |
| **Isolation transformer (delta-wye, with a Faraday shield)** | Breaks the ground path and reduces common-mode transfer from the upstream supply |
| **Common-mode choke** | A pair of windings on one core: it has **high impedance only to common-mode current**, so the wanted differential signal passes |
| **Y-capacitors (line to chassis)** | Shunt high-frequency common-mode noise to the chassis |
| **Balanced signalling and twisted pairs** | Noise is induced equally on both conductors and cancels at the receiver |
| **Shielded cables with proper termination** | Intercept noise. Terminate shields correctly (360° where required) |
| **Fibre optic cable** | Has **no conductive path**, so it is immune to ground potential differences |
| **Separation from power cables** | Reduces coupling (6.18) |
| **Surge protective devices** | Limit transients |
| **Low-noise equipment** | Equipment that meets EMC limits (CISPR 32 / EN 55032 type) **[CHECK]** |

**Link to earthing:** a TN-C system or multiple neutral-ground bonds make neutral current flow in earth conductors, which raises the common-mode noise. This is one reason TN-S with a single bond is preferred.

---

# 6.28 Distribution board (DB)

## 1. What it is

A **distribution board** is an **assembly of protective devices** (breakers or fuses) that **receives a supply and divides it into protected final circuits**, with busbars, neutral and earth bars, and often metering and surge protection.

| Level | Names | Role |
| --- | --- | --- |
| **Main** | Main distribution board (MDB), main switchboard (MSB), main LV board | Receives the supply from the transformer and generator, feeds the UPS and plant |
| **Intermediate** | Sub-distribution board (SDB), UPS output board | Feeds a zone or system |
| **Final** | Final distribution board, panelboard, RPP, rack distribution | Feeds individual circuits to racks and equipment |

```
 Transformer ──► MDB ──► SDB ──► Final DB / RPP ──► circuits to racks
```

## 2. Components

| Component | Function |
| --- | --- |
| **Incomer** | Main switch or breaker that isolates the whole board |
| **Busbars** | Carry the current to the outgoing devices |
| **Outgoing devices** | **MCB** (small breaker), **MCCB** (moulded case), **ACB** (air circuit breaker), **RCBO** (breaker with earth-leakage protection), fuses |
| **Neutral and earth bars** | Neutral (N) and protective earth (PE) terminations |
| **SPD** | Surge protective device |
| **Metering and monitoring** | Current, power and energy per circuit, with alarms |
| **Indicators and controls** | Status lamps, test points, communications |
| **Enclosure** | Metal or insulated cabinet with an **IP rating** (6.29) |

## 3. Standards and ratings **[CHECK]**

| Item | Detail |
| --- | --- |
| **IEC 61439-1 and -2** | Requirements for **low-voltage switchgear and controlgear assemblies**. Part 2 covers power switchgear assemblies, Part 3 covers distribution boards operated by ordinary persons |
| **Design verification** | The assembly as a whole must be verified (temperature rise, short-circuit withstand, dielectric strength), not just each device |
| **Rated current (In)** | Continuous current of the board or circuit |
| **Short-circuit rating** | **Icw** (short-time withstand) and **Icc** (conditional short-circuit): must exceed the available fault current |
| **Rated diversity factor (RDF)** | The fraction of the sum of outgoing circuit ratings that may be loaded **at the same time** |
| **Degree of protection** | IP and IK rating |
| **UL equivalents** | UL 891 (switchboards), UL 67 (panelboards), NEC **[CHECK]** |

### Rated diversity factor

IEC 61439-2 gives typical values for the **number of main outgoing circuits** **[CHECK]**:

| Number of circuits | RDF |
| --- | --- |
| 2 and 3 | 0.9 |
| 4 and 5 | 0.8 |
| 6 to 9 | 0.7 |
| 10 or more | 0.6 |

**Worked example.** A board has **12 outgoing circuits of 32 A**:

```
Sum of ratings = 12 × 32 = 384 A
Assumed simultaneous loading = 384 × 0.6 = 230 A  →  incomer of 250 A
```

**For a data centre**, circuits to racks are loaded **continuously and together**, so the **RDF should be specified as 1.0**, not the default. Using 0.6 would under-size the board.

## 4. Forms of internal separation

| Form | Separation |
| --- | --- |
| **Form 1** | None between busbars, functional units and terminals |
| **Form 2** | Busbars separated from the functional units |
| **Form 3** | Busbars separated from units **and** units separated from each other |
| **Form 4** | As Form 3 **and** the terminals of each unit separated from those of others |

Higher forms make **maintenance safer** (you can work on one circuit with others live) and **contain faults**, at higher cost. Mission critical boards often use **Form 3 or 4**.

## 5. Design points for data centres

| Point | Detail |
| --- | --- |
| **Spare capacity** | Leave **spare ways** (commonly 20 to 25%) and busbar room for growth **[CHECK]** |
| **A and B** | Separate boards (and rooms) for the A and B paths |
| **Discrimination** | Coordinate settings so a fault trips only the nearest device |
| **Phase distribution** | Spread single-phase circuits across L1, L2, L3 (6.17) |
| **Metering** | Circuit-level metering for balance and PUE |
| **Arc flash** | Calculate, label, and choose designs that reduce energy (for example Form 4, arc-resistant) |
| **Labelling** | Every circuit labelled with source and load |
| **Thermography** | Scan connections regularly (06-4) |
| **Access** | Working space and escape routes per code |
| **Maintenance bypass** | Where a board can't be shut down, provide a bypass |

**Sizing a row board (worked example).** **10 racks at 6 kW** = 60 kW at 400 V: I = 60,000 / (1.732 × 400) = **87 A**. With A and B boards each sized for the full row: continuous rule 87 × 1.25 = 108 A, so a **125 A** board.

---

# 6.29 Ingress protection (IP) grades

## 1. The IP code (IEC 60529)

**IP** = **I**ngress **P**rotection. It is written **IP + two digits**:

```
   IP  5  4
       │  └── second digit: protection against WATER (0 to 9)
       └───── first digit : protection against SOLIDS and dust (0 to 6)
```

A letter **X** replaces a digit that isn't specified (for example IPX4).

## 2. First digit: solids

| Digit | Protects against |
| --- | --- |
| **0** | No protection |
| **1** | Objects larger than **50 mm** (back of the hand) |
| **2** | Objects larger than **12.5 mm** (**fingers**) |
| **3** | Objects larger than **2.5 mm** (tools, thick wires) |
| **4** | Objects larger than **1 mm** (wires, small screws) |
| **5** | **Dust-protected**: dust may enter, but not enough to harm operation |
| **6** | **Dust-tight**: no dust enters |

## 3. Second digit: water

| Digit | Protects against |
| --- | --- |
| **0** | No protection |
| **1** | Vertically **dripping** water |
| **2** | Dripping water with the enclosure tilted up to 15° |
| **3** | **Spraying** water (up to 60° from vertical) |
| **4** | **Splashing** water from any direction |
| **5** | **Water jets** (low pressure) from any direction |
| **6** | **Powerful jets** |
| **7** | **Temporary immersion** (up to about 1 m for 30 minutes) |
| **8** | **Continuous immersion** (beyond 1 m, as specified by the maker) |
| **9** | **High-pressure, high-temperature** jets (steam cleaning) |

**Important points:**

- The digits are **not a cumulative ladder** for water: **IP66 does not mean IP67**. A product tested for jets is not automatically tested for immersion. Some are marked with both (for example IPX6/IPX7).
- **IP2X** (finger-safe) is the usual **touch protection** for live parts inside switchgear and busway.
- IP does **not** cover **condensation, corrosion, explosive atmospheres, or fire**.

### Reading examples

| Code | Meaning |
| --- | --- |
| **IP20** | Finger-safe, no water protection (indoor switchgear in a dry room) |
| **IP31 / IP32** | Objects over 2.5 mm, dripping water |
| **IP42** | Objects over 1 mm, tilted dripping |
| **IP54** | **Dust-protected**, **splash-proof** |
| **IP55** | Dust-protected, **water jets** |
| **IP65** | **Dust-tight**, water jets |
| **IP66** | Dust-tight, powerful jets |
| **IP67** | Dust-tight, temporary immersion |
| **IP68** | Dust-tight, continuous immersion |

## 4. Where each is used in a data centre **[CHECK]**

| Location | Typical IP |
| --- | --- |
| **Computer room (switchgear, rack PDUs, busway)** | IP2X to IP31, busway IP40 to IP54 |
| **Electrical and UPS rooms** | IP21 to IP31 for boards, higher if hose-down or dust |
| **Battery room** | IP21 to IP54 (ventilation, moisture, acid) |
| **Plant rooms, mechanical areas** | IP54 |
| **Outdoor equipment: generators, chillers, dry coolers, outdoor cabinets** | IP54 to IP55, outdoor cabinets often IP55 to IP65 |
| **Wet or washdown areas, flood risk locations** | IP65 to IP67 (or higher) |
| **Light fittings in hot or plant areas** | IP54 or higher |

## 5. Related codes **[CHECK]**

| Code | Topic |
| --- | --- |
| **IK code (IEC 62262)** | Mechanical **impact** resistance, IK00 to IK10 (for example **IK08 = 5 joules**, **IK10 = 20 joules**) |
| **NEMA enclosure types (US)** | NEMA 1 (indoor general), 3R (rain), 4 / 4X (washdown, corrosion), 12 (dust, drips). Roughly comparable to IP ratings, but not identical |

---

# 6.30 Power quality guidelines

## 1. Why guidelines

Equipment is only as reliable as the **power it receives**. Guidelines say **what to expect from the supply**, **what the site must deliver to the IT load**, **how to measure it**, and **what to do about problems**.

## 2. The key documents **[CHECK]**

| Document | What it covers |
| --- | --- |
| **EN 50160** | Voltage characteristics of **public** supply (see `06-1`, 6.5) |
| **IEC 61000 series** | EMC: compatibility levels (61000-2-2), harmonic and flicker emission limits (61000-3-x), immunity (61000-4-x) |
| **IEC 61000-4-30** | **How to measure** power quality (Class A for compliance, Class S for surveys) |
| **IEEE 1159** | Monitoring electric power quality, and definitions of disturbances |
| **IEEE 519-2022** | **Harmonic limits** at the point of common coupling |
| **IEEE 1100 (Emerald Book)** | Powering and grounding electronic equipment |
| **ITIC / CBEMA curve** | Voltage tolerance envelope for IT equipment (6.32) |
| **SEMI F47** | Voltage sag immunity for semiconductor equipment |
| **IEC 62040-3** | UPS performance and output classification |

## 3. IEEE 519-2022 limits at the PCC **[CHECK]**

**Voltage distortion limits (at the PCC):**

| Bus voltage | Individual harmonic | Total voltage distortion (THD) |
| --- | --- | --- |
| Up to 1 kV | **5%** | **8%** |
| 1 kV to 69 kV | 3% | **5%** |

**Current distortion limits** are set as **TDD (total demand distortion)**, which depends on the **short-circuit ratio**: ISC / IL (maximum available fault current ÷ maximum demand load current) for systems from 120 V to 69 kV:

| ISC / IL | TDD limit |
| --- | --- |
| below 20 | **5%** |
| 20 to below 50 | **8%** |
| 50 to below 100 | **12%** |
| 100 to below 1,000 | **15%** |
| 1,000 and above | **20%** |

A **stiff** (high short-circuit) supply tolerates more harmonic current than a **weak** one.

**TDD definition:**

```
TDD = (RMS harmonic current) / IL × 100%       IL = maximum demand load current
```

THD divides by the **present** fundamental current, so it looks bad at light load. TDD divides by the **maximum demand**, so it doesn't mislead.

### Worked example: IEEE 519 compliance

At the PCC: **ISC = 20 kA**, **IL = 800 A**, measured **harmonic current = 55 A RMS**.

```
ISC / IL = 20,000 / 800 = 25  → row "20 to below 50" → limit 8%
TDD = 55 / 800 = 6.9%          → below 8%, so compliant
```

## 4. Typical targets for the IT load **[CHECK]**

| Parameter | Practical guidance |
| --- | --- |
| **Supply voltage** | Within ±10% (public supply), tighter from the UPS |
| **Voltage THD** | About 5% or lower at the load, 8% as the usual limit |
| **Neutral-to-ground voltage** | Near zero at the load. Investigate above about 1 to 2 V |
| **Shield-to-outlet-ground** | Below about 1 V rms |
| **Frequency** | Stable at nominal (UPS output synchronised to the bypass source) |
| **Transients** | Controlled by SPDs (Type 1, 2, 3) |
| **Generator bus** | Voltage THD commonly targeted at 5% or lower |

## 5. Guidelines in practice

| Guideline | Why and how |
| --- | --- |
| **1. Know the supply** | Review the utility's record (SAIDI, SAIFI, EN 50160 reports) and **measure at the PCC** for at least a week (10-minute values) |
| **2. Design for what you find** | If the supply is weak, add conditioning (UPS, filters, voltage regulation) |
| **3. Use a double-conversion UPS** | Gives a clean, regulated output regardless of input |
| **4. Control harmonics at the source** | Low-THDi UPS, filters, multi-pulse rectifiers, active front ends (6.31) |
| **5. Check generator compatibility** | Size for harmonics (the slide multiplier) and test UPS and generator together |
| **6. Ground and bond properly** | Single neutral-ground bond, common bonded network, TN-S (6.26) |
| **7. Protect against surges** | Coordinated SPDs, all services entering at one point |
| **8. Balance the phases** | Prevents unbalance and neutral overload (6.17) |
| **9. Keep power and data apart** | Reduces interference (6.18) |
| **10. Monitor continuously** | Class A power quality meters at the PCC, UPS output, PDUs and key racks, with alarms and event recording |
| **11. Audit regularly** | Periodic power quality surveys, thermography, and testing after changes |
| **12. Use equipment that meets EMC limits** | Compliant drivers, power supplies and UPS |

---

# 6.31 Harmonics

## 1. What harmonics are

Harmonics are **waves at whole-number multiples of the fundamental frequency** that **distort** the voltage or current waveform. They are produced by **non-linear loads**: loads that draw current in **pulses** instead of a smooth sine wave.

| Harmonic order (h) | Frequency (50 Hz) | Frequency (60 Hz) |
| --- | --- | --- |
| 1 (fundamental) | 50 Hz | 60 Hz |
| 2 | 100 Hz | 120 Hz |
| 3 | 150 Hz | 180 Hz |
| 5 | 250 Hz | 300 Hz |
| 7 | 350 Hz | 420 Hz |
| 9 | 450 Hz | 540 Hz |
| 11 | 550 Hz | 660 Hz |
| 13 | 650 Hz | 780 Hz |

Odd harmonics are the main concern. Even harmonics are usually small in a balanced system.

**Sequence:** harmonics rotate in different ways. **Triplen harmonics (3, 9, 15 ...) are zero-sequence**: they are **in phase on all three conductors** and **add up in the neutral**. The 5th is negative-sequence (opposes motor rotation), the 7th positive-sequence.

## 2. Sources in a data centre

| Source | Notes |
| --- | --- |
| **UPS rectifiers** | The biggest single source (6-pulse thyristor, 12-pulse, or IGBT active front end) |
| **Server and network power supplies (switch-mode)** | Single-phase, often rich in **3rd harmonic** unless they have active power factor correction |
| **Variable-speed drives** | On cooling fans, pumps and compressors |
| **LED and electronic lighting drivers** | Small but numerous |
| **Battery chargers and DC supplies** | Rectifiers |
| **Saturated transformers** | Non-linear magnetisation |

## 3. Measuring distortion

```
THD = √(I₂² + I₃² + I₄² + ... ) / I₁ × 100%      (I₁ is the fundamental)
RMS current = I₁ × √(1 + THD²)
```

**Worked example.** A feeder carries a **100 A fundamental** with **30 A of 5th, 15 A of 7th, 8 A of 11th and 5 A of 13th** harmonic (a 6-pulse rectifier pattern):

```
Harmonic RMS = √(30² + 15² + 8² + 5²) = √1,214 = 34.8 A
THD = 34.8 / 100 = 34.8%
RMS current = 100 × √(1 + 0.348²) = 105.9 A
```

The cable heats with the **RMS** value (105.9 A), not the 100 A fundamental. Measure with a **true-RMS** instrument.

**THD vs. TDD:** with a maximum demand current of 160 A, the same 34.8 A gives **TDD = 34.8 / 160 = 21.8%**. And a **40% THD at 50% load** corresponds to a **TDD of 20%**.

## 4. Effects

| Effect | Cause |
| --- | --- |
| **Extra heating of cables and transformers** | Higher RMS current, and losses that rise with the harmonic order (skin and eddy effects) |
| **Neutral overload** | Triplen harmonics add in the neutral |
| **Transformer derating** | Needs K-rated or oversized transformers |
| **Generator voltage distortion** | A generator has a high internal impedance, so the same harmonic current causes **3 to 4 times** more voltage distortion than on the utility **[CHECK]**, and overheats the alternator |
| **UPS, STS and ATS problems** | Distorted waveforms disturb zero-crossing detection and synchronisation |
| **Capacitor failure and resonance** | Power factor capacitors can resonate with a harmonic |
| **Nuisance trips and meter errors** | Breakers and meters reading wrongly |
| **Lower true power factor** | Distortion adds to the apparent power (6.33) |

### Resonance

A capacitor bank and the supply inductance can resonate at the harmonic order:

```
h_resonance = √(S_sc / Q_c)     (S_sc = short-circuit power, Q_c = capacitor power)
```

**Example:** S_sc = 20 MVA and Q_c = 0.5 MVAr: h = √(20 / 0.5) = √40 = **6.3**, right between the 5th and 7th, where rectifiers inject current. That bank is in danger.

## 5. Rectifier harmonics **[CHECK]**

A three-phase rectifier with **p pulses** produces harmonics of order **h = (p × k) ± 1**:

| Rectifier | Harmonics produced | Typical THDi |
| --- | --- | --- |
| **6-pulse** | 5, 7, 11, 13, 17, 19 ... (h = 6k ± 1) | About **30%** ideal (theory: 20%, 14%, 9%, 8% for 5th, 7th, 11th, 13th), **30 to 40%** with a DC choke, **over 80%** with none |
| **12-pulse** | 11, 13, 23, 25 ... (the **5th and 7th cancel**) | About **8 to 12%** |
| **18-pulse** | 17, 19, 35 ... | About **4 to 5%** |
| **24-pulse** | 23, 25 ... | About 3% |
| **Active front end (IGBT)** | Almost none | Typically **below 3 to 5%** |

In a 12-pulse arrangement two rectifier bridges are fed from transformer outputs shifted by **30°**, so the 5th and 7th harmonic currents cancel in the primary.

**Light load:** THDi rises at partial load (the 20 to 40% loading typical of 2N designs), even though harmonic amperes fall.

## 6. Mitigation

| Measure | Notes |
| --- | --- |
| **Low-THDi UPS** (active front end, 12 or 18-pulse) | The best fix at the source |
| **Input filters** | Passive tuned filters, **active harmonic filters** |
| **Line reactors / DC chokes** | Cut a 6-pulse THDi from above 80% to about 30 to 40% |
| **Phase-shifting transformers** | 12 or 18-pulse arrangements |
| **Delta winding (delta-wye transformer)** | Traps **triplen** harmonics |
| **K-rated transformers** | Withstand harmonic heating |
| **Oversized neutral** | 150 to 200% of the phase conductor where needed |
| **Generator oversizing and a good AVR** | Alternator about 1.2 to 1.5 times the UPS kVA for an active front end, **about 2 to 2.5 times** for a 6-pulse UPS **[CHECK]**, and the **× 1.2 factor on your generator slide** |
| **Spread non-linear loads** | Avoid concentrating them on one bus |
| **Detuned capacitor banks** | Avoid resonance |

(See also the generator sizing table in `06-1`, 6.10.)

---

# 6.32 CBEMA curve

## 1. What it is

The **CBEMA curve** (named after the Computer and Business Equipment Manufacturers Association) is a **graph of voltage tolerance** for computer equipment: it shows **how large a voltage disturbance, and for how long, IT equipment can typically withstand**. Today's version is the **ITIC (ITI) curve** (revised 2000), published by the Information Technology Industry Council, and the two names are used interchangeably.

| Item | Detail |
| --- | --- |
| **Axes** | **Horizontal:** duration (microseconds, milliseconds, cycles, seconds, steady state). **Vertical:** voltage as a percentage of nominal |
| **Applies to** | Single-phase **120 V, 60 Hz** equipment (from 120 V, 208Y/120 V and 120/240 V systems). Other voltages and frequencies are not formally covered |
| **Purpose** | An envelope that **most IT equipment can tolerate with no interruption in function**. It is **not** a design specification and **not** a utility supply performance curve |

## 2. The regions

| Region | Meaning |
| --- | --- |
| **No interruption in function region** (inside the envelope) | Equipment should keep working normally |
| **Prohibited region** (above the envelope) | Overvoltages here could **damage** equipment |
| **No damage region** (below the envelope) | Sags and dropouts here are **not expected to damage** equipment, but **normal operation is not expected** (it may reset or shut down) |

## 3. The key points

| Condition | Limit |
| --- | --- |
| **Steady state** | **±10%** of nominal (90% to 110%) for any length of time |
| **Voltage swell** | Up to **120%** for up to **0.5 s** |
| **Voltage sag, short** | Down to **70%** for up to **0.5 s** |
| **Voltage sag, longer** | Down to **80%** for up to **10 s** |
| **Dropout (loss of voltage)** | **0 V** for up to **20 ms** |
| **Low-frequency decaying ringwave** | Peaks of **140% to 200%** (200 Hz to 5 kHz), typically from capacitor switching |
| **High-frequency impulse** | Above 200%, limited by the energy involved |

So the **lower boundary** is **0% up to 20 ms, then 70% up to 0.5 s, then 80% up to 10 s, then 90% in steady state**. The **upper boundary** is **120% up to 0.5 s, then 110%**.

## 4. Applying it to 230 V / 50 Hz **[CHECK]**

The curve is formally for 120 V / 60 Hz, but its **percentages** are commonly applied to 230 V / 50 Hz with the same **times in absolute units**. One 50 Hz cycle is **20 ms**.

| Percentage | On a 230 V supply |
| --- | --- |
| 120% | 276 V |
| 110% | 253 V |
| 90% | 207 V |
| 80% | 184 V |
| 70% | 161 V |

## 5. Using the curve

1. Record disturbances with a **power quality meter** (magnitude and duration).
2. **Plot** each event on the curve.
3. **Inside** the envelope: acceptable. **Below** it: the equipment may malfunction. **Above** it: possible damage.

### Worked examples

| Event (on a 230 V supply) | Where it falls | Result |
| --- | --- | --- |
| **0 V for 15 ms** | Dropout up to 20 ms | **Inside**: tolerated |
| **0 V for 50 ms** | Longer than 20 ms | **Outside** (no-damage region): equipment may reset |
| **60% for 100 ms** | Below the 70% limit for 20 ms to 0.5 s | **Outside**: may malfunction |
| **75% for 100 ms** | Above 70% for up to 0.5 s | **Inside** |
| **85% for 2 s** | Above 80% for 0.5 to 10 s | **Inside** |
| **115% for 0.3 s** | Under 120% for up to 0.5 s | **Inside** |
| **125% for 0.1 s** | Above 120% | **Outside** (prohibited region): damage possible |

## 6. Link to the transfer equipment

| Device | Transfer time | Against the 20 ms dropout limit |
| --- | --- | --- |
| **STS** | Under about 4 to 8 ms | **Inside**: the load doesn't notice |
| **ATS (open transition)** | About 40 to 200 ms | **Far outside**: IT loads would drop |
| **UPS (online)** | Zero | Inside |

That is why an ATS must have a **UPS** behind it for IT loads, and why an STS can switch dual-source loads safely. Server **power supplies** have a **hold-up time** (the time they run on stored energy), often about **10 to 20 ms** at full load **[CHECK]**.

## 7. Limitations

- It covers **voltage magnitude and duration only**, not frequency, harmonics, noise or unbalance.
- It describes **typical** tolerance. Individual equipment may be better or worse.
- Hold-up time is specified **at rated load**. A fully loaded supply may hold up for less.
- **SEMI F47** (for semiconductor tools) is **more demanding**, requiring ride-through of sags to 50% for 200 ms and 80% for up to 1 s **[CHECK]**.
- Being inside the curve doesn't guarantee trouble-free operation. It only describes the **incoming power**.

---

# 6.33 Power factor

## 1. Definitions

| Quantity | Symbol | Unit | Meaning |
| --- | --- | --- | --- |
| **Real (active) power** | P | W | Does useful work |
| **Reactive power** | Q | VAR | Moves back and forth, does no work |
| **Apparent power** | S | VA | Voltage × current, what cables and equipment must carry |
| **Power factor** | PF | 0 to 1 | **PF = P / S = cos φ** (displacement) |

```
S² = P² + Q²        P = S × PF        S = P / PF
```

**Lagging** PF: current lags voltage (inductive loads such as motors and transformers). **Leading** PF: current leads voltage (capacitive loads such as power factor correction capacitors and some power supplies).

## 2. Displacement vs. distortion

With harmonics, the **true power factor** has two parts:

```
True PF = displacement PF × distortion factor
        = DPF / √(1 + THD²)
```

**Worked example.** DPF = 0.95 and current THD = 34.8%:

```
True PF = 0.95 / √(1 + 0.348²) = 0.95 / 1.059 = 0.90
```

## 3. Typical power factors **[CHECK]**

| Load | Power factor |
| --- | --- |
| Server power supply **with active PFC** | About 0.95 to 0.99 |
| Older power supply without PFC | About 0.6 to 0.7 |
| UPS input (IGBT rectifier) | 0.99 or better |
| UPS output | Modern units rate kVA = kW (PF 1.0). Older units 0.8 to 0.9 |
| Chillers, pumps, fans (motors) | About 0.8 to 0.9 |
| Generator alternator rating | 0.8 (kW = 0.8 × kVA) |

## 4. Why it matters

| Effect of a low PF | Result |
| --- | --- |
| **More current for the same kW** | I = P / (√3 × V × PF), so the current rises as PF falls |
| **Higher I²R losses** | Losses vary with the square of the current |
| **Less usable capacity** | Cables, transformers, switchgear and UPS carry kVA, so a low PF **wastes capacity** |
| **Utility charges** | Penalties for PF below a threshold (often about 0.9 to 0.95) |
| **Voltage drop** | Higher current means more voltage drop |

### Worked example: current and losses

A **500 kW** load at **400 V**:

```
At PF 0.80:  S = 500 / 0.8 = 625 kVA     I = 500,000 / (1.732 × 400 × 0.8)  = 902 A
At PF 0.95:  S = 500 / 0.95 = 526 kVA    I = 500,000 / (1.732 × 400 × 0.95) = 760 A
Current reduction = 15.8%
Loss ratio = (0.80 / 0.95)² = 0.71   →  about 29% lower I²R losses
```

**Same IT supply, different PF:** a **1,000 W** server draws **1,010 VA** at PF 0.99 but **1,429 VA** at PF 0.70.

## 5. Correction

Capacitors supply the reactive power locally. The capacitor size needed to raise the PF:

```
Qc = P × (tan φ₁ − tan φ₂)
```

**Worked example.** 500 kW, from PF 0.80 to PF 0.95:

```
tan φ₁ = tan(acos 0.80) = 0.750
tan φ₂ = tan(acos 0.95) = 0.329
Qc = 500 × (0.750 − 0.329) = about 211 kVAR
```

| Method | Notes |
| --- | --- |
| **Capacitor banks** (fixed or automatic) | Central correction at the main board |
| **Detuned (reactor-fitted) banks** | Avoid resonance with harmonics |
| **Active power factor correction in the equipment** | Inside server PSUs and UPS rectifiers |
| **Active filters** | Correct both PF and harmonics |

**Cautions:**

- **Capacitors and harmonics** can resonate (6.31). Use detuned banks where harmonics are present.
- A **leading** power factor from many PFC-equipped power supplies at **light load** can disturb a **generator's voltage regulator** and UPS-generator operation **[CHECK]**.
- Capacitors **don't fix** current imbalance (6.17).

## 6. Where PF matters in sizing

- **UPS:** kW = kVA × output PF. A **500 kVA UPS at 0.9** gives **450 kW**. A unity-PF 500 kVA UPS gives **500 kW**.
- **Generator:** a set sized in kW must also have enough **kVA** (kW ÷ 0.8).
- **Transformers and cables:** size on **kVA** (current), not kW.

---

# 6.34 Label power versus consumed power

## 1. The difference

| Term | Meaning |
| --- | --- |
| **Label / nameplate power** | The maximum rating printed on the equipment: the **input rating** the supply must be able to provide safely (for example "100–240 V, 10–5 A, 1,600 W") |
| **Consumed (actual) power** | What the equipment **really draws**: it varies with workload, configuration, temperature and fan speed |
| **Idle power** | The draw with no load (often 30 to 50% of peak for servers) **[CHECK]** |
| **Peak (maximum measured) power** | The highest draw measured under a heavy test |
| **Average power** | The draw averaged over time |
| **Design (derated) rating** | A planning figure, commonly a **fraction of nameplate** (often 50 to 75%) **[CHECK]** |

## 2. Why the label is conservative

The label is the **sum of the worst-case power of every component in a fully configured machine, divided by the efficiency of the power supply**. It is a number the equipment is **guaranteed not to exceed**, intended to tell the user the **supply infrastructure needed to run it safely**.

**Example (from a published study).** A server's component datasheets add up to **213 W** (DC). With an **85%** efficient power supply the label reads **251 W**:

```
Nameplate = 213 / 0.85 = 251 W
Measured under the heaviest benchmark = 145 W  →  145 / 251 = 58% of the label
```

## 3. What the studies found **[CHECK]**

| Finding | Source type |
| --- | --- |
| Actual draw was typically only about **30%** of nameplate | Berkeley Lab measurements of real data centres (2003) |
| Server draw ranged from **20% to 85%** of nameplate, averaging about **31%** | Intelligent-PDU measurements in a test facility |
| Most servers at peak were **60% or less** of nameplate, but a few were **above 80%** | Measurements of 59 servers |
| Many planners use **70% of nameplate** | Common practice, and still often over-allocated |
| Even the heaviest tests reached only about **60%** of the label for one server | Google power provisioning study |

**But AI and HPC racks differ:** accelerators run **near full power for long periods**, so measured power can approach the label **[CHECK]**.

## 4. The two risks

| Design to... | Risk |
| --- | --- |
| **The label** | **Over-provisioning**: oversized UPS, generators, cooling and distribution, high cost, equipment running at **light load and lower efficiency**, **stranded capacity** |
| **Too far below the label** | **Under-provisioning**: breakers tripping at peak, overloaded circuits, thermal problems, **a shutdown risk** |

**Stranded power** is capacity that is **allocated but never used**, and can't be given to other equipment.

## 5. What to use for what

| Purpose | Use |
| --- | --- |
| **Breaker, cable and PDU protection (safety)** | The **label / input rating**, plus the continuous-load rule |
| **Rack capacity planning** | **Measured or vendor-calculated** power at the expected workload, with margin |
| **Upstream capacity (UPS, generator, transformers, cooling)** | Measured loads, with **diversity**, growth and redundancy |
| **Power-on inrush** | Plan for it: **stagger start-up** of many servers |

## 6. Good practice

- Use the **manufacturer's power calculator** (enter processor, memory, drives and workload).
- **Measure** with **metered or intelligent PDUs** at **outlet level**, over time, to find real peaks and averages.
- Compare **allocated** with **actual** per rack, and recover unused allocation.
- Use **power capping** to protect circuits while allowing safe over-subscription.
- Re-measure after changes, and track **peak** as well as **average**.
- Look at **individual devices**, not only averages: both very low and very high outliers matter.

## 7. Worked example

**40 servers**, each with an **750 W** power supply label, measured **peak 320 W** and **average 220 W**:

| Basis | Per server | 40 servers |
| --- | --- | --- |
| **Label** | 750 W | **30.0 kW** |
| **Derated at 70% of label** | 525 W | 21.0 kW |
| **Measured peak** | 320 W | **12.8 kW** (42.7% of label) |
| **Measured average** | 220 W | 8.8 kW (29.3% of label) |

```
Stranded if allocated by the label:  30.0 − 12.8 = 17.2 kW
Allocation using measured peak + 20% margin = 12.8 × 1.2 = 15.4 kW
Three-phase current at 400 V (PF 1):  label 43.3 A  vs  15.4 kW → 22.2 A
```

Using the label would reserve **nearly twice** the circuit capacity needed.

---

# 6.35 Sizing power

## 1. The sizing flow

```
IT load (measured / vendor data × racks)
   → total facility power (× PUE)
   → apparent power (÷ power factor)
   → growth and phasing
   → redundancy (N+1, 2N ...)
   → equipment sizes: UPS, batteries, generators, transformers, switchgear, cables
   → check the weakest link and the efficiency at the real load
```

## 2. Sizing rules

| Rule | Detail |
| --- | --- |
| **Start from the IT load** | Use realistic rack power from measured or calculated data (6.34), not labels |
| **Add the overhead** | Total power = IT load × PUE (cooling, UPS and distribution losses, lighting) |
| **Use kVA for cables and transformers** | They carry current. kW = kVA × PF |
| **Allow for growth** | Typically 20 to 30%, often built in phases **[CHECK]** |
| **Apply redundancy** | Installed capacity exceeds the load (N+1, 2N, 2(N+1)) |
| **Continuous-load margins** | Devices loaded continuously should not exceed about 80% of rating (or be sized at 125% of load) |
| **Derate for conditions** | Temperature, altitude, grouping, installation method |
| **Harmonics** | Generator: UPS load × 1.0 or 1.2 per your slide. Neutrals and transformers: allow for harmonic heating |
| **Step loads and inrush** | The generator must accept the UPS rectifier step and motor starting |
| **Efficiency at the real load** | Check that equipment isn't so oversized that it runs at very light load |
| **Weakest link** | The system is limited by the smallest or most heavily loaded part |

## 3. Worked example: sizing a 1.6 MW facility

**Given:** 200 racks at **8 kW** each (measured design figure), **PUE 1.4**, **PF 0.95**, UPS efficiency **96%**, 10 minutes of battery.

| Step | Calculation | Result |
| --- | --- | --- |
| **1. IT load** | 200 × 8 kW | **1,600 kW** |
| **2. Total facility power** | 1,600 × 1.4 | **2,240 kW** |
| **3. UPS input** | 1,600 / 0.96 | 1,667 kW (losses 67 kW) |
| **4. Cooling, lighting and other** | 2,240 − 1,667 | 573 kW |
| **5. Heat to remove from the IT load** | 1,600 kW ÷ 3.517 kW per refrigeration ton | **455 tons** |
| **6. UPS modules (500 kW each, unity PF)** | N = 1,600 / 500 = 3.2, so 4. N+1 = 5 | **5 modules**, each 1,600 / 5 = **320 kW (64%)** |
| **6b. Or 2N** | 2 × 4 = 8 modules | Each 1,600 / 8 = **200 kW (40%)** |
| **7. Battery energy (10 min)** | 1,600 × 10/60 = 266.7 kWh. Divide by 0.96 = 277.8 kWh. Multiply by 1.25 for ageing and margin | **about 347 kWh** (illustrative) |
| **8. Generator (your slide)** | UPS part 1,667 × 1.2 = 2,000 kW. Plus 573 × 1.0 = 573 kW. Total 2,573 kW. Add 20% margin | **about 3,090 kW**. With 1,600 kW sets: N = 2, **N+1 = 3 sets** |
| **9. Apparent power** | 2,240 / 0.95 | **2,358 kVA** |
| **10. Transformers (2N, max 80% loaded)** | 2,358 / 0.8 = 2,947 kVA, so a standard **3,150 kVA** | Each normally 37%, **75%** after a failure |
| **11. Utility current** | At 20 kV: 2,358,000 / (1.732 × 20,000). At 400 V: 2,358,000 / (1.732 × 400) | **68 A** at MV vs. **3,404 A** at LV |
| **12. A row of 10 racks** | 10 × 8 = 80 kW at 400 V, PF 0.95 | **121.5 A**, so a **160 A** busway |

**What this shows:**

- The **transformer** sized for 100% duty in a 2N design would run at 75% after a failure, so it is sized for about 80% maximum loading, not 100%.
- The **generator** is far larger than the IT load because of the cooling plant, UPS losses and the harmonic multiplier.
- Redundancy lowers the loading of each module, which lowers efficiency.

## 4. kW, kVA and the UPS

A load of **1,600 kW at PF 0.95** is **1,684 kVA**.

| UPS | Rating | Usable kW | Enough for 1,600 kW? |
| --- | --- | --- | --- |
| Unity-PF (kW = kVA) | 500 kVA | 500 kW | Yes, 4 modules for N |
| 0.9 output PF | 500 kVA | 450 kW | Needs 4 modules (1,800 kW), too little margin for N+1 |
| 0.8 output PF (older) | 500 kVA | 400 kW | Needs 4 modules just for N, 5 for N+1 |

Always compare **kW** with **kW** (and kVA with kVA).

## 5. Common sizing mistakes

- Sizing from **labels** instead of measured or calculated power (6.34).
- Forgetting **redundancy**, so a failure overloads the survivor.
- Ignoring **harmonics** (generator and neutral) and **step loads**.
- Mixing **kW and kVA**.
- Forgetting **cooling and losses** (the PUE overhead).
- **Over-sizing** so far that equipment runs at very light load.
- Sizing the supply **without** the distribution, cabling or transformer limits.
- No **growth path**, or building everything on day one.

---

## Glossary

| Term | Meaning |
| --- | --- |
| Common mode | Noise in phase on both conductors relative to ground |
| Differential mode | The wanted signal: equal and opposite on two conductors |
| CMRR | Common-mode rejection ratio |
| DB / MDB / SDB | Distribution board / main / sub |
| RDF | Rated diversity factor |
| Form 1 to 4 | Levels of internal separation in a board |
| IP code | Ingress protection: solids digit, water digit |
| IK code | Impact protection |
| PCC | Point of common coupling |
| TDD | Total demand distortion (harmonic current ÷ maximum demand current) |
| THD | Total harmonic distortion |
| Triplen harmonics | 3rd, 9th, 15th ... (zero-sequence, add in the neutral) |
| 6, 12, 18-pulse | Rectifier types by the number of pulses per cycle |
| AFE | Active front end (IGBT rectifier) |
| CBEMA / ITIC curve | Voltage tolerance envelope for IT equipment |
| Hold-up time | How long a power supply runs on stored energy after the input fails |
| PF / DPF | Power factor / displacement power factor |
| Nameplate (label) power | Maximum rated input of the equipment |
| Stranded power | Allocated but unused capacity |
| PUE | Total facility energy ÷ IT energy |

## Exam takeaways

**6.27 to 6.29**

- **Common mode** = noise **in phase on both conductors**. **Differential** = wanted signal. Fixes: **single bond, common bonded network, isolation transformer, common-mode choke, twisted/shielded cable, fibre.**
- **CMRR (dB) = 20 log₁₀(Ad / Acm)**: 80 dB turns 1 V into 100 µV.
- A **distribution board** (IEC 61439) splits a supply into protected circuits. Know **MDB, SDB, final DB**, **Forms 1 to 4**, and the **RDF** (use **1.0** for continuously loaded data centre circuits). Leave **spare ways**.
- **IP code: first digit solids (0 to 6), second digit water (0 to 9).** IP54 = dust-protected, splash-proof. IP65 = dust-tight, jets. **IP2X = finger-safe.** IP66 is **not** IP67.

**6.30 to 6.32**

- **IEEE 519-2022:** voltage THD **8%** (below 1 kV), **TDD** limits **5/8/12/15/20%** by **ISC/IL** (<20, 20 to 50, 50 to 100, 100 to 1,000, >1,000). **TDD = harmonic current ÷ maximum demand current.**
- Harmonic order frequencies (50 Hz): **3rd 150, 5th 250, 7th 350 Hz.** **Triplen** harmonics **add in the neutral.**
- **THD = √(sum of harmonic²) / fundamental.** **6-pulse: 5th, 7th, 11th, 13th**, THDi about 30%. **12-pulse** cancels 5th and 7th (about 8 to 12%). **AFE** under 3 to 5%.
- **Generators suffer more** from harmonics (high impedance), hence the **× 1.2** UPS factor.
- **ITIC curve:** **±10% steady, 120% for 0.5 s, 80% for 10 s, 70% for 0.5 s, 0 V for 20 ms.** For IT equipment, not a utility curve. **STS inside it, ATS outside.**

**6.33 to 6.35**

- **PF = P / S.** Low PF means more current, more losses, less capacity. **Qc = P (tan φ₁ − tan φ₂).** **True PF = DPF / √(1 + THD²).** UPS **kW = kVA × PF.**
- **Label power is conservative** (worst case, never reached). Real draw is often **30 to 60%** of the label, so labels **over-provision** and **strand** power. **Measure** with metered PDUs. Use labels for **protection**, measured data for **capacity**.
- **Sizing flow:** IT load, × PUE, ÷ PF, growth, redundancy, equipment, check the weakest link. **Transformers ≤ about 80% loaded** in a 2N design.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **IEEE 519-2022** | Harmonic limits: voltage THD and TDD |
| **EN 50160** | Supply quality limits |
| **IEC 61000-4-30**, **IEEE 1159**, **IEEE 1100** | Measurement, definitions, powering and grounding practice |
| **ITI (CBEMA) curve** (ITIC, 2000), **SEMI F47** | Voltage tolerance envelope and sag immunity |
| **IEC 61439-1 and -2**, **UL 891**, **UL 67** | Distribution assemblies, switchboards and panelboards |
| **IEC 60529**, **IEC 62262**, NEMA enclosure types | IP code, IK code, US enclosure types |
| **IEC 62040-3** | UPS output performance |
| **CISPR 32 / EN 55032** | EMC emission limits |
| Lawrence Berkeley National Laboratory (2003), Google power provisioning study (Fan, Weber and Barroso, 2007), vendor measurements | Label versus consumed power |
| **NFPA 70** (NEC) | 80% and 125% margins |
| Standard electrical engineering | Power factor, THD, resonance and sizing formulas |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
