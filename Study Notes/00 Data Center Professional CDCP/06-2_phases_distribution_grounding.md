# Module 6, Part B: Phases, Cabling, Distribution and Grounding (lessons 6.15 to 6.26)

Detailed notes, following the lesson-level index of the EPI course. This is the second of four Module 6 files (see `06-1` for lessons 6.1 to 6.14).

| Lesson | Title | Section |
| --- | --- | --- |
| 6.15 | Three Phase Power Cabling | [Section 1](#615-three-phase-power-cabling) |
| 6.16 | Single Phase Power | [Section 2](#616-single-phase-power) |
| 6.17 | Phase Balancing | [Section 3](#617-phase-balancing) |
| 6.18 | Power Cable Routing | [Section 4](#618-power-cable-routing) |
| 6.19 | Dual Power Sources | [Section 5](#619-dual-power-sources) |
| 6.20 | Triple Power Supply | [Section 6](#620-triple-power-supply) |
| 6.21 | Availability Options | [Section 7](#621-availability-options) |
| 6.22 | Techniques for Power Availability | [Section 8](#622-techniques-for-power-availability) |
| 6.23 | Power Distribution | [Section 9](#623-power-distribution) |
| 6.24 | Busbar Trunking | [Section 10](#624-busbar-trunking) |
| 6.25 | Power Cabling Distribution Methods | [Section 11](#625-power-cabling-distribution-methods) |
| 6.26 | Grounding | [Section 12](#626-grounding) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#part-b-lessons-615-to-626) |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. **[SLIDE]** marks content from a slide you showed me (here: "Bonding of neutral & ground"). If your course gives a different number, use your course.
>
> The physics (three-phase, line vs. phase voltage, √3, kVA, harmonics) is in `06a_electrical_physics_foundations.md`. Redundancy terms (N, N+1, 2N, 2(N+1), 2N+1) are in Module 2 and `06-1`.

---

# 6.15 Three-phase power cabling

## 1. The conductors

A three-phase supply has **three phase conductors (L1, L2, L3)**, a **neutral (N)** where single-phase loads are served, and a **protective earth (PE)**. A full supply is **3P + N + PE** (five conductors).

| System | Line voltage | Phase-to-neutral |
| --- | --- | --- |
| Europe and most of the world | **400 V** | 230 V |
| Some regions (including the slide's example) | **415 V** | 240 V |
| US, 120/208 V wye | **208 V** | 120 V |
| US, 277/480 V wye | **480 V** | 277 V |

(Line voltage = √3 × phase voltage. See `06a`, section 6.)

## 2. Conductor identification (colours) **[CHECK]**

| Region / system | L1 | L2 | L3 | Neutral | Earth (PE) |
| --- | --- | --- | --- | --- | --- |
| **Europe, UK (since 2004), IEC 60446 / 60445** | Brown | Black | Grey | Blue | Green/yellow |
| **US 120/208 V (convention)** | Black | Red | Blue | White | Green |
| **US 277/480 V (convention)** | Brown | Orange | Yellow | Grey | Green |
| **Canada (typical)** | Red | Black | Blue | White | Green |

Points to remember:

- In the US the code **requires** colours only for the **grounded conductor (neutral: white or grey)** and the **equipment ground (green, green/yellow or bare)**. Phase colours are by convention.
- **Orange** marks the **high leg** of a four-wire delta system (208 V to neutral on a 240 V system).
- **Never** assume a blue wire is a neutral: in the US it is a phase conductor.
- The IEC change removed yellow from the phase colours to avoid confusion with the green/yellow earth.

## 3. Cable construction

| Choice | Options and notes |
| --- | --- |
| **Conductor** | **Copper** (compact, tolerant at joints) or **aluminium** (about 1.6 times the cross-section for the same resistance, about half the weight, cheaper). Aluminium needs correct terminations |
| **Core arrangement** | **Single-core** cables (one per phase, laid in trefoil, easy to route, good for large currents) or **multi-core** (all conductors in one sheath) |
| **Insulation** | PVC (older, cheaper) or **XLPE** (cross-linked polyethylene, higher temperature rating, common in new work) |
| **Sheath and fire behaviour** | **LSZH / LS0H** (low smoke, zero halogen) is the usual choice in data centres: little toxic smoke or corrosive gas in a fire |
| **Armour** | Steel wire or tape armour (for mechanical protection and as a protective conductor) |
| **Fire-resistant cables** | Keep working for a set time in a fire, used for life-safety circuits |
| **Standards [CHECK]** | IEC 60502 (power cables), IEC 60332 (flame propagation), IEC 60754 and IEC 61034 (halogen and smoke), EN 50575 (EU construction products, fire classes) |

## 4. Sizing a cable

A cable is chosen so that **all** of these hold:

| Check | Meaning |
| --- | --- |
| **Current-carrying capacity** | Must carry the design current without overheating, after **derating** for ambient temperature, grouping with other cables, and installation method |
| **Voltage drop** | Typically limited to a few percent from the source to the load **[CHECK]** (commonly about 3 to 5% in total) |
| **Short-circuit withstand** | Must survive the fault current until the protection clears it |
| **Earth-fault loop impedance** | Low enough that the breaker trips fast on a fault |
| **Neutral** | Sized for neutral current, which can exceed phase current with harmonics (see 6.17) |
| **Mechanical and fire requirements** | Support, bend radius, LSZH, fire stops |

### Worked example 1: power per circuit

Three-phase power: **P = √3 × V × I × PF** (here PF = 1 for simplicity).

| Circuit (400 V) | Calculation | Power |
| --- | --- | --- |
| 16 A | 1.732 × 400 × 16 | about 11.1 kW |
| 32 A | 1.732 × 400 × 32 | about **22.2 kW** |
| 63 A | 1.732 × 400 × 63 | about 43.6 kW |
| 125 A | 1.732 × 400 × 125 | about 86.6 kW |

With a common continuous-load planning figure of **80%**, a 32 A circuit supports about **17.7 kW** **[CHECK]**.

### Worked example 2: why higher voltage helps

The same **20 kW** load:

```
At 400 V: I = 20,000 / (1.732 × 400) = 28.9 A
At 208 V: I = 20,000 / (1.732 × 208) = 55.5 A
```

Almost double the current at 208 V, so thicker cables, bigger breakers and higher losses.

### Worked example 3: voltage drop (simplified)

A **100 A** three-phase feeder, **50 m** long, with a conductor resistance of about **0.6 Ω/km** (illustrative, for a 35 mm² copper conductor at operating temperature) **[CHECK]**:

```
ΔV = √3 × I × R × L = 1.732 × 100 × 0.6 × 0.05 = about 5.2 V
As a share of 400 V = 5.2 / 400 = 1.3%
```

Real calculations also include reactance and power factor, but this shows the idea: **long runs and high current cost voltage**.

## 5. Connectors **[CHECK]**

| Connector | Use |
| --- | --- |
| **IEC 60309 industrial plug and socket** | 16, 32, 63, 125 A. **5-pin (3P+N+E)** for 400 V three-phase. Colour code: **blue** for 230 V single-phase, **red** for 400 V three-phase, **yellow** for 110 V |
| **IEC 60320 C13/C14** | Up to 10 A, small equipment |
| **IEC 60320 C19/C20** | Up to 16 A, servers and larger equipment |
| **Hard-wired connections** | Larger PDUs and distribution |

A **three-phase rack PDU** usually takes a 16 or 32 A three-phase input (IEC 60309 plug) and provides banks of C13 and C19 outlets, spread across the phases.

## 6. Phase rotation (sequence)

The three phases peak in order L1, L2, L3. If two phases are swapped, **three-phase motors run backwards** (cooling fans, pumps, compressors) and some equipment (UPS, STS, paralleled generators) won't operate or synchronise. Always **check phase rotation** with a phase-rotation meter, especially after any change to cabling, and make sure **generator and utility have the same rotation**.

## 7. Neutral sizing and harmonics

Computer power supplies draw **third-harmonic** currents that **add up in the neutral** instead of cancelling (see `06a`, section 9). So data centre feeders that serve single-phase IT loads may need an **oversized neutral** (up to 150 to 200% of the phase conductor) or a K-rated transformer **[CHECK]**.

## 8. Installation and maintenance

- Tighten terminations to the **specified torque**. Loose connections are the most common cause of heating and failures.
- **Thermographic scans** of terminations (see 06-4).
- **Label** every cable at both ends with source, destination and path (A or B).
- **Support** cables properly and respect **minimum bend radius**.
- Keep **phase order consistent** from the transformer to the rack.

---

# 6.16 Single-phase power

## 1. Where single-phase is used

Single-phase supplies one phase and the neutral (or two phases in some US circuits). It serves **rack PDUs**, small loads, lighting, convenience outlets, small UPS units, and control equipment. Nearly all **IT equipment** is single-phase at the plug.

| Item | Voltage |
| --- | --- |
| Europe | **230 V** (phase to neutral) |
| UK, Australia | 230 to 240 V |
| US | **120 V** (phase to neutral) or **208 V / 240 V** (phase to phase) |

## 2. Capacity of a single-phase circuit

**P = V × I × PF**

| Circuit | Calculation | Power |
| --- | --- | --- |
| 230 V, 16 A | 230 × 16 | **3.68 kW** |
| 230 V, 32 A | 230 × 32 | **7.36 kW** |
| 120 V, 20 A | 120 × 20 | 2.4 kW |
| 208 V, 30 A | 208 × 30 | 6.24 kW |

**Continuous-load rule [CHECK]:** in the US, continuous loads are limited to **80%** of the breaker rating. So a 208 V, 30 A circuit supports **208 × 24 = about 5.0 kW** continuously. Many designers apply a similar margin elsewhere.

## 3. Current for the same power at different voltages

A **1 kW** server:

```
At 230 V: I = 1,000 / 230 = 4.3 A
At 120 V: I = 1,000 / 120 = 8.3 A
```

Most server power supplies accept **100 to 240 V**, so running at the higher voltage **halves the current** and improves efficiency slightly.

## 4. Single-phase vs. three-phase

| | Single-phase | Three-phase |
| --- | --- | --- |
| **Power from one 32 A, 230/400 V circuit** | about 7.4 kW | about 22 kW |
| **Cables** | Two live conductors per circuit | One cable carries three phases, more power per cable |
| **Balance** | Needs deliberate spreading across L1, L2, L3 | Naturally balanced if loads are balanced |
| **Neutral current** | Always present | Zero when balanced (without harmonics) |
| **Equipment** | Simple, universal | Needed for large motors, UPS inputs, high-density racks |
| **Typical use** | Low-density racks, small loads | High-density racks, plant, UPS and chillers |

## 5. Points to watch

| Point | Detail |
| --- | --- |
| **Neutral current and harmonics** | Single-phase electronic loads create third-harmonic currents (see 6.17) |
| **Earth leakage current** | Each server power supply leaks a small current (often about 0.5 to 3.5 mA **[CHECK]**) to earth through its filters. On a circuit with an **RCD**, many servers add up and can trip it, which is one reason RCD-protected circuits suit data centres poorly |
| **Single-corded vs. dual-corded** | A single-corded device has one power path and is a weak point (see 6.19) |
| **Plug and socket choice** | C13/C14 for small loads, C19/C20 for larger, with locking cords in high-vibration or high-availability locations |
| **Separate circuits** | Each rack has its own protected circuits, not shared with other racks |

---

# 6.17 Phase balancing

## 1. What it is and why it matters

**Phase balancing** means spreading the single-phase loads **evenly** across the three phases, so each carries about the same current.

| Problem from imbalance | Effect |
| --- | --- |
| **Neutral current** | Current flows in the neutral wire, heating it and any neutral bonds |
| **Voltage imbalance** | The heavily loaded phase drops in voltage, lightly loaded phases rise. Motors (fans, pumps, compressors) overheat |
| **Transformer and UPS heating** | One phase works harder than the others |
| **Wasted capacity** | One phase hits its limit while others have spare room (**stranded capacity**) |
| **Nuisance trips** | A breaker on the busy phase trips first |

## 2. Measuring imbalance

```
Average current  = (I1 + I2 + I3) / 3
Imbalance (%)    = (largest deviation from the average / average) × 100
```

This is the form NEMA MG 1 uses for voltage, and it is applied to currents too **[CHECK]**.

### Worked example 1

Phase currents **18 A, 20 A, 22 A**:

```
Average = 20 A.   Largest deviation = 2 A.   Imbalance = 2 / 20 = 10%
```

### Worked example 2

Phase currents **85 A, 72 A, 68 A**:

```
Average = 75 A.   Largest deviation = 85 − 75 = 10 A.   Imbalance = 10 / 75 = 13.3%
```

## 3. Limits

There is **no single universal limit** for current imbalance **[CHECK]**:

| Guide | Typical figure |
| --- | --- |
| **Working targets for data centre phases** | Often about **±10%** as a target, **±15%** as a warning zone (a rule of thumb, not a standard) |
| **Motors (NEMA MG 1)** | Voltage unbalance **1%** or less at the motor, and derating needed above that, no operation above **5%** |
| **Voltage vs. current** | In motors, current imbalance can be about **6 to 10 times** the voltage imbalance, so 2% voltage imbalance may give 12 to 20% current imbalance |
| **Contracts** | A utility connection agreement or customer specification may set its own number |

Capacitors for power-factor correction **do not** fix current imbalance.

## 4. Neutral current

For a three-phase four-wire system with **linear** single-phase loads at the same power factor:

```
I_N = √( Ia² + Ib² + Ic² − Ia·Ib − Ib·Ic − Ia·Ic )
```

- **Balanced loads:** the neutral current is **zero**.
- **Worked example:** phases **80 A, 40 A, 40 A**: I_N = √(6,400 + 1,600 + 1,600 − 3,200 − 1,600 − 3,200) = √1,600 = **40 A**.
- **Worked example:** phases **30 A, 20 A, 10 A**: I_N = √(900 + 400 + 100 − 600 − 200 − 300) = √300 = **17.3 A**.

**With harmonics:** third-harmonic (and multiples of three) currents are **in phase** in all three conductors, so they **add arithmetically** in the neutral. If each phase carries **20 A** of third harmonic, the neutral carries **60 A** of it, even if the fundamental currents are perfectly balanced. This is why neutrals can carry **more than phase current** in IT-heavy installations.

## 5. How to achieve balance

| Method | Detail |
| --- | --- |
| **Rotate assignments** | Assign racks, outlets or circuits to L1, L2, L3, L1, L2, L3 in turn |
| **Use three-phase rack PDUs** | One PDU spreads its outlets across all three phases |
| **Measure per phase** | Per-phase metering at the PDU, RPP and rack, with alarms |
| **Move loads** | Re-assign circuits after the layout changes |
| **Plan at every level** | Balance at the rack, the row, the PDU and the UPS output |
| **Check after changes** | Re-measure whenever equipment is added |
| **Include the generator** | An unbalanced load also stresses the generator |

### Worked example 3: balanced vs. unbalanced racks

Nine racks of **5 kW** each (single-phase, 230 V):

| Allocation | L1 | L2 | L3 | Imbalance |
| --- | --- | --- | --- | --- |
| **3 racks per phase** | 15 kW | 15 kW | 15 kW | 0% |
| **5 / 3 / 1 racks** | 25 kW | 15 kW | 5 kW | see below |

For 5 / 3 / 1:

```
Currents = 108.7 A, 65.2 A, 21.7 A    Average = 65.2 A
Largest deviation = 108.7 − 65.2 = 43.5 A
Imbalance = 43.5 / 65.2 = 66.7%
```

The busy phase is close to the limit of a 125 A breaker (87%), while the lightly loaded phase has lots of unused capacity. Moving two racks from L1 to L3 gives **3 / 3 / 3** and restores the balance.

---

# 6.18 Power cable routing

## 1. Principles

| Principle | Reason |
| --- | --- |
| **Keep A and B routes physically separate** | One cable damage, fire or maintenance event must not affect both paths. Some designs call for separated feeders (for example about 20 m apart) for the highest-rated sites **[CHECK]** |
| **Separate power from data cables** | Avoids electromagnetic interference. Required safety separation too |
| **Cross at 90°** | Where power and data cross, cross at right angles to minimise coupling |
| **Keep routes short** | Less voltage drop, lower cost, fewer faults |
| **Support properly** | Trays, ladders, supports rated for the cable weight, earthed and bonded |
| **Respect bend radius** | Tight bends damage insulation |
| **Don't block airflow** | Under-floor trays must not obstruct cold air. Overhead trays must not block containment or returns |
| **Keep away from heat and water** | Away from hot pipes, and not under water pipes |
| **Fire stops** | Seal every penetration of a fire wall or floor. Use LSZH cables |
| **Label and document** | Label both ends and record the routes |
| **Plan for growth** | Spare tray capacity, avoid fully packed trays |

## 2. Separation from data cables (EN 50174-2:2018) **[CHECK]**

The standard calculates the **minimum separation A = S × P**:

1. Find the data cable's **segregation class** (most U/UTP cable is class b, and screened Cat 5e, 6 and 6A cables are typically class c).
2. Read the minimum separation **S** for that class and the type of containment (for example **S = 50 mm** for class b on a perforated metal tray, **25 mm** for class c).
3. Multiply by the **power cabling factor P**, which depends on the **number and current of the power circuits** in the route. The unit is a **20 A, 230 V single-phase circuit**: a three-phase circuit counts as three, and a circuit above 20 A counts as multiples of 20 A.

| Example | S | P | Separation A |
| --- | --- | --- | --- |
| Cat 6 U/UTP (class b) on a perforated metal tray, beside eight power circuits | 50 mm | 0.6 | **30 mm** |
| Screened (class c) cable on the same route | 25 mm | 0.6 | **15 mm** |
| **Solid metallic containment** with screening equal to 1.5 mm steel conduit | | | **0 mm** |

Further rules:

- Cable **crossings** should be kept at **90°** for the required distance on both sides.
- The standard allows **no separation for the last 15 m** of a horizontal run in some cases.
- **Electrical safety rules take priority** over the interference calculation. For example, the UK standard BS 6701 asks for at least **50 mm** or a barrier between telecom and power cables in many cases, and some interference sources such as fluorescent lamps need more (about 130 mm).
- **Local regulations** may require a barrier or more separation than the calculation gives.

## 3. Under-floor and overhead routing

| | Under the raised floor | Overhead |
| --- | --- | --- |
| **Pros** | Hidden, short drops to racks | Does not affect airflow, easy access |
| **Cons** | Can block the cold air path, harder to inspect, water risk | Needs ceiling height, can obstruct light and detection |
| **Tips** | Wire-basket trays, power and data in **separate** trays, place trays in the **hot aisle** **[CHECK]**, keep trays clear of tile cut-outs | Ladder or basket trays, power and data on separate levels or sides |

## 4. Worked example: tray fill

20 power cables of **25 mm** overall diameter in a **300 mm × 60 mm** tray (usable area 18,000 mm²):

```
Area of one cable = π × 12.5² = 491 mm²
20 cables         = 9,817 mm²
Tray fill         = 9,817 / 18,000 = 54.5%
```

A common guide limits fill to **about 50%** **[CHECK]**, so use a bigger tray: a **400 × 60 mm** tray (24,000 mm²) gives about **41%**, leaving room for growth.

---

# 6.19 Dual power sources

## 1. The idea

**Dual-corded** IT equipment has **two power supply units (PSUs)**, each connected to a **different, independent power path (A and B)**. Normally both share the load, and if one path fails the other carries all of it, with **no interruption**.

```
 Path A ──► Rack PDU A ──► PSU 1 ──┐
                                    ├──► Server (either PSU can carry the full load)
 Path B ──► Rack PDU B ──► PSU 2 ──┘
```

## 2. How sharing works

| Mode | Behaviour |
| --- | --- |
| **Active-active (load sharing)** | Both PSUs supply about half the load each |
| **Active-standby (cold redundant)** | One PSU supplies the load and the other idles, to keep the working PSU in its efficient range **[CHECK]** |
| **On a failure** | The surviving PSU instantly takes the whole load. Because both PSUs are on, no switching is needed |

**PSU efficiency:** power supplies are most efficient around **50% load**. Efficiency classes (**80 PLUS Platinum / Titanium**) specify efficiency at 20%, 50% and 100% load, for example about **94% to 96% at 50%** for the top classes on 230 V **[CHECK]**. Running two PSUs at 50% each lands in that sweet spot.

## 3. The capacity rule

If both paths carry about half the load normally, **each path must be able to carry all of it**:

- Normal load per path: about **50%** of the load.
- If one path fails: the other must carry **100%** of the load.
- So **each path is sized for the full load**, and in practice kept at **no more than about 40 to 50%** of its capacity in normal operation.

### Worked example: a rack on A and B

A rack draws **6 kW** (dual-corded) from **230 V** circuits:

```
Normal: each path carries 3 kW = 13 A
After a failure: one path carries 6 kW = 6,000 / 230 = 26.1 A
```

A **32 A** circuit works, **but** if the design limits continuous load to 80% of the breaker (25.6 A, or 5.9 kW), the rack's 6 kW is **just over** the limit. The usable rack limit is the capacity of **one** circuit (derated), not the sum of two. So the design must either reduce the rack load, use a bigger circuit, or use three-phase PDUs.

## 4. Failure scenarios

| Failure | Result for a dual-corded server |
| --- | --- |
| Path A UPS or PDU fails | Server runs on path B (path B load doubles) |
| One PSU fails | The other PSU takes the full load. Replace the failed PSU (hot-swap) |
| Both A and B fail | The server stops. Hence A and B must be truly independent |
| Planned maintenance on path A | Path B carries everything. Redundancy is lost during the work |

## 5. Keeping A and B independent

- Separate **utility feed, transformer, generator, UPS, PDU** and **cable route** for each path.
- Separate **rooms and fire compartments**.
- Don't cross-connect A and B except through well-designed switching (STS).
- Label and colour-code (for example one colour for A, another for B).
- Beware of **common-mode** causes: shared fuel, shared control, shared cooling, shared maintenance errors.

## 6. Single-corded equipment

Equipment with only **one** power cord is a weak link. Solutions:

| Option | Detail |
| --- | --- |
| **Rack-mounted ATS/STS** | Switches the single cord between A and B (a few ms for an STS) |
| **Row or PDU-level STS** | A larger STS feeding a group |
| **Accept the risk** | Put it on the more reliable path and treat it as lower resilience |

(See 6.13 and 6.14 in `06-1`.)

## 7. "Dual power sources" at the site level

Dual **utility** feeds (two independent grid connections) are the supply-side version of the same idea. The generator is a **backup** source that takes over after a delay (see 6.9 and 6.10), which is different from the **continuous, simultaneous** sharing of A and B at the equipment.

---

# 6.20 Triple power supply

## 1. What "triple" can mean

There are two related ideas:

1. **Three independent power paths (A, B and C)** feeding the load, where any **two** can carry the full load. This is often called **3N/2**, **distributed redundant** or **"3 to make 2"**.
2. **Three sources at the site level**: for example **two utility feeds plus a generator**, or two feeds and storage.

(Some equipment also has **three PSUs** in an N+1 arrangement, for example two needed and one spare.)

## 2. Three paths: 3N/2 (distributed redundancy)

```
 System A ──┐          ┌── Group 1 (fed by A and B)
 System B ──┼─ pairs ──┼── Group 2 (fed by B and C)
 System C ──┘          └── Group 3 (fed by C and A)
```

Each **load group** is dual-fed from **two** of the three systems, using dual-input PDUs, or dual-corded equipment.

### The loading logic

Let the three systems each have capacity **C**, and the total protected load be **L = 2C**.

| State | Load carried by each system |
| --- | --- |
| **Normal** | L / 3 = 2C / 3 = **66.7%** of its capacity |
| **One system fails** | The other two each carry L / 2 = **100%** of capacity |

**Check with the groups:** each group carries L/3. Normally system A carries half of group 1 and half of group 3: L/6 + L/6 = L/3. If A fails, group 1 runs on B alone and group 3 on C alone. System B then carries all of group 1 (L/3) plus half of group 2 (L/6) = **L/2**. Same for C. Good.

## 3. Comparison with other designs

For a protected load **L** and the total installed capacity:

| Design | Installed capacity | Normal loading per system | After one failure |
| --- | --- | --- | --- |
| **2N** (A and B) | 2 × L = **2.0 L** | 50% | The other at 100% |
| **3N/2** (A, B, C) | 3 × (L/2) = **1.5 L** | **66.7%** | The other two at 100% |
| **4N/3** (four systems) | 4 × (L/3) = about **1.33 L** | 75% | Three at 100% |

**Worked example: load 600 kVA**

| Design | Installed | Per system, normal |
| --- | --- | --- |
| 2N | 1,200 kVA (2 × 600) | 300 kVA each (50%) |
| 3N/2 | 900 kVA (3 × 300 kVA) | 200 kVA each (66.7%) |

3N/2 saves **25% of the installed capacity** compared with 2N, and each system runs **more efficiently** (higher loading).

## 4. Advantages and drawbacks

| Advantages | Drawbacks |
| --- | --- |
| Less installed capacity than 2N | **More complex** distribution (dual-input PDUs, careful load pairing) |
| Higher loading and better UPS efficiency | After one failure or during maintenance, the other two are at **100% with no further redundancy** |
| Fault tolerance against a single failure | Load must be **dual-fed** and carefully balanced between the pairs |
| Scales (4N/3, 5N/4 and so on) | Harder to operate, monitor and test |

**Compared with 2(N+1):** 2(N+1) still has a spare in each side during maintenance, so it tolerates a failure while one side is out for service. 3N/2 does not.

## 5. Three sources at the site level

| Arrangement | Description |
| --- | --- |
| **Two utility feeds plus a generator** | Main-tie-main with a generator behind an ATS. A grid failure doesn't need the generator, as the other feed takes over |
| **Utility, generator and stored energy** | A battery or flywheel bridges the transfer |
| **Microgrid** | Several local sources and storage with a controller (6.3) |

## 6. Triple modular redundancy (TMR) in control logic **[CHECK]**

In **controls**, **TMR** uses **three** logic channels with a **2-out-of-3 vote**, so one faulty channel is outvoted. Some static transfer switches use TMR control for the same reason. This is a different use of "triple" from three power paths.

**2-out-of-3 availability.** If each of three units is available with probability **A** and any two are enough:

```
Availability = 3A² − 2A³
For A = 0.999:  3 × 0.998001 − 2 × 0.997003 = 0.999997 → 99.9997%
```

This is the formula behind N+1 with three modules where two are needed.

---

# 6.21 Availability options

## 1. The calculation tools

| Case | Formula |
| --- | --- |
| **Availability of one item** | A = MTBF / (MTBF + MTTR) |
| **Series** (all must work) | A = A₁ × A₂ × A₃ ... |
| **Parallel** (either can carry the load) | A = 1 − (1 − A₁) × (1 − A₂) |
| **2-out-of-3** (any two of three work) | A = 3A² − 2A³ |
| **Downtime per year** | (1 − A) × 8,760 hours |

These assume **independent** failures. Real sites also have **common-mode failures** and **human error**, so treat results as a way to **compare options**, not to predict outages.

## 2. Comparing options (worked example)

Assume the chain has **three stages** (source, UPS, distribution), each **99.9%** available:

| Option | Calculation | Availability | Downtime per year |
| --- | --- | --- | --- |
| **1. Single path (N)** | 0.999 × 0.999 × 0.999 | **99.70%** | about 26.3 hours |
| **2. Redundant UPS stage only (1+1)** | UPS stage = 1 − 0.001² = 0.999999, so 0.999 × 0.999999 × 0.999 | **99.80%** | about 17.5 hours |
| **3. Redundancy at every stage (1+1 each)** | each stage 0.999999, so 0.999999³ | **99.9997%** | about 1.6 minutes |
| **4. 2N (two complete independent chains)** | chain 99.7003%, so 1 − (0.002997)² | **99.9991%** | about 4.7 minutes |

What it shows:

- Making **only one stage** redundant gives a small gain, because the **other stages still limit** the result (the weakest link).
- **Redundancy at every stage** gives a very high figure in the ideal model, but needs **cross-connections and more switching**, which adds the complexity and common-mode risks the model leaves out.
- **2N** gives most of the benefit with **simple, independent chains**.

## 3. The "nines" and the Tiers

| Availability | Downtime per year |
| --- | --- |
| 99% | 87.6 hours |
| 99.9% | 8.76 hours |
| 99.99% | 52.6 minutes |
| 99.999% | 5.26 minutes |

| Tier | Commonly quoted availability | Downtime per year |
| --- | --- | --- |
| I | 99.671% | about 28.8 h |
| II | 99.741% | about 22 h |
| III | 99.982% | about 1.6 h |
| IV | 99.995% | about 26 min |

(The Tier percentages are indicative figures, see Module 2.)

## 4. Which option when

| Requirement | Typical option |
| --- | --- |
| Low cost, tolerates some outages | Single path, N+1 on key components |
| Maintenance without downtime | N+1 with multiple paths, bypasses (Tier III style) |
| Survives any single failure | 2N or 2(N+1) (Tier IV style) |
| Efficiency with fault tolerance | Distributed redundant 3N/2 |

---

# 6.22 Techniques for power availability

Availability improves by **failing less often** (higher MTBF) and **recovering faster** (lower MTTR). Techniques fall into groups.

| Technique | What it does | Improves |
| --- | --- | --- |
| **Redundancy** (N+1, 2N, 2(N+1)) | Spare capacity so one failure doesn't stop the load | MTBF of the system |
| **Eliminating single points of failure** | Find and remove any one item whose failure stops everything | MTBF |
| **Independent A and B paths** | Two paths with no shared parts | MTBF |
| **Compartmentalisation** | Separate fire and flood compartments for A and B | MTBF (common-mode risk) |
| **Concurrent maintainability** | Bypasses, isolation, redundant paths so maintenance needs no shutdown | Planned downtime |
| **Fault tolerance** | The system survives a failure with no impact | MTBF |
| **Protective device coordination (selectivity)** | A fault trips only the nearest breaker | Limits the impact of a fault |
| **Quality and derating** | Equipment run well within its rating, good components | MTBF |
| **Preventive and predictive maintenance** | Scheduled servicing, thermography, battery tests, generator load tests, oil analysis | MTBF |
| **Monitoring and alarms** | EPMS/BMS/DCIM, power quality meters, early warnings | Both |
| **Spares and modularity** | Spare parts on site, hot-swappable modules | **MTTR** |
| **Trained staff and procedures** | Operating and emergency procedures, practised drills | **MTTR** and fewer errors |
| **Change control** | Reviewed, approved, staged changes | Fewer self-inflicted outages |
| **Commissioning and integrated systems tests** | Prove the design works under failure scenarios before go-live | MTBF |
| **Capacity management** | Keep paths below about 40 to 50% load so one can carry all | MTBF |
| **Fuel and consumables management** | Fuel quality, resupply contracts, battery replacement schedules | MTBF |
| **Power quality management** | UPS, surge protection, filters, grounding | MTBF |
| **Access control and physical protection** | Restrict who can reach power rooms and switches | Fewer human-error events |
| **Simplicity** | Fewer parts and switching states means fewer ways to fail or be operated wrongly | Both |

## Worked example: why MTTR matters

A component has **MTBF = 20,000 hours**:

```
MTTR 8 hours:  A = 20,000 / 20,008 = 99.960%
MTTR 2 hours:  A = 20,000 / 20,002 = 99.990%
```

Cutting the repair time from 8 to 2 hours gives the same gain as making the item far more reliable.

## Emergency power off (EPO)

An **EPO** button cuts all power in an emergency, but an **accidental press** has caused real outages. Use **protective covers**, **two-step operation**, clear labels, restricted placement, and procedures. Some jurisdictions require EPO (check local code).

## Human factors

Most outages involve people. The strongest controls are **clear procedures that are followed**, **labelling**, **two-person verification** for critical switching, **training**, and **change control**.

---

# 6.23 Power distribution

## 1. The chain inside the facility

```
 UPS output board ──► PDU ──► RPP or busway ──► Rack PDU ──► IT equipment
```

(With A and B copies of each, see 6.19.)

| Component | Role |
| --- | --- |
| **LV main switchboard** | Receives the supply from the transformer and generators, distributes to UPS and mechanical loads |
| **UPS output board** | Collects the UPS output and feeds distribution |
| **PDU** | A floor-standing cabinet (often with an isolation transformer) giving many protected output circuits and metering |
| **RPP** | A smaller panel near a row of racks, fed from the PDU |
| **Busway** | Overhead conductors with plug-in tap-offs (6.24) |
| **Rack PDU** | The strip or unit in the rack that feeds the equipment |

## 2. Distribution topologies

| Topology | Description | Resilience |
| --- | --- | --- |
| **Radial** | One source feeds loads through one path | Lowest. A fault takes out everything downstream |
| **Primary selective** | Each load is fed by one of two **primary** (higher-voltage) feeders, with automatic switching at the primary side | Good, with the transformer as a single point |
| **Secondary selective** | Two transformers feed two buses with a normally open tie, with automatic switching at the secondary (LV) side | Better. Loads survive a transformer failure |
| **Ring (loop)** | Feeders form a loop with open points, so supply comes from either direction | Good, but needs good protection |
| **Dual-ended / A and B** | Two complete independent paths feeding dual-corded loads | Best |

```
Radial:                     Secondary selective:
 Source ── Bus ──► Loads     Trafo 1 ── Bus A ──┐
                                                [Tie] (normally open)
                             Trafo 2 ── Bus B ──┘
```

## 3. Protection

| Item | Notes |
| --- | --- |
| **Circuit breakers** | **MCB** (small), **MCCB** (moulded case), **ACB** (air circuit breaker, large) |
| **Fuses** | Fast, current-limiting |
| **RCD / RCBO** | Earth-leakage protection. Used with care in data centres because of server leakage currents |
| **Discrimination (selectivity)** | A fault trips only the breaker nearest to it, so the rest stay on |
| **Short-circuit rating** | Every device must withstand the available fault current |
| **Arc-flash** | Study, label and reduce arc-flash energy, with safe working procedures |
| **Surge protection (SPD)** | At the main board (Type 1), distribution boards (Type 2), near equipment (Type 3) |
| **Metering** | At the UPS output, PDU and rack for load, balance and PUE |
| **Maintenance bypass** | Lets a device be isolated without dropping the load |

**Discrimination example:** a rack breaker of 32 A, an RPP breaker of 100 A and a PDU breaker of 250 A. A fault at the rack should trip **only the 32 A breaker**. The upstream breakers have higher ratings and slower or higher trip settings so they stay closed.

## 4. Sizing a feed

**Worked example.** A row of **10 racks at 6 kW** is **60 kW**. At 400 V (PF 1):

```
Current = 60,000 / (1.732 × 400) = 86.6 A
Continuous load rule: breaker ≥ 125% of load = 86.6 × 1.25 = 108 A, so use a 125 A breaker
```

With **A and B**, **each path** is sized for the **full 60 kW** (87 A), even though each normally carries about half.

## 5. Isolation transformer in the PDU

The PDU transformer is usually **delta-wye**. It creates a **new, separately derived** system with a **local neutral-earth bond**, traps third-harmonic currents and isolates the white space from upstream noise (see 6.26). Some modern designs, especially in 400/230 V regions, feed rack PDUs **directly** without a PDU transformer.

---

# 6.24 Busbar trunking

## 1. What it is

**Busbar trunking** (busway, bus duct) is a **factory-made, modular system of enclosed copper or aluminium bars** in a housing, installed in sections joined together, with **tap-off units** that plug in to supply loads.

| Type | Description |
| --- | --- |
| **Feeder busbar (bus duct)** | Point-to-point transfer, no tap-offs (for example transformer to switchgear) |
| **Plug-in (distribution) busbar** | Has tap-off points along its length for loads such as rack rows |
| **Track busway** | Open slot along the length, with tap-off boxes inserted or moved anywhere, often **hot-swappable** |

```
 LV board ──► Feeder busway ──► Overhead plug-in busway above rack rows
                                     │       │       │
                                tap-off  tap-off  tap-off ──► rack PDUs
```

## 2. Standards and ratings **[CHECK]**

| Item | Detail |
| --- | --- |
| **IEC 61439-6** | The standard for low-voltage busbar trunking systems (replaced IEC 60439-2). Requires the **complete system** to be design-verified (temperature rise, dielectric, short-circuit) |
| **UL 857 / NEC Article 368** | North American busway standard and code |
| **Rated current** | From about 100 A up to about 6,300 A. Tap-off units from about 50 A to over 1,000 A |
| **Short-time withstand (Icw)** | The fault current the busway can carry for a stated time |
| **IP rating** | Protection against solids and water (for example IP40 indoor, IP55 or higher in harsher areas) |
| **Neutral** | 100% neutral, or **200% neutral** where harmonics are high |
| **Materials** | Copper (compact) or aluminium (about 1.6 times the cross-section for the same resistance, about half the weight) |

## 3. Busway vs. cable

| | Busway | Cable |
| --- | --- | --- |
| **Best when** | High current (roughly above 630 to 800 A), long runs, loads that change | Low current (below about 400 A), fixed loads, short runs |
| **Installation** | Fast: pre-made sections | Slower: pulling and terminating many cables |
| **Changes** | Plug in or move a tap-off, no re-cabling, **live** where designed | New cable runs, often an outage |
| **Space** | Compact, no cable congestion | Needs wide trays or many routes |
| **Material cost** | Higher per metre | Lower per metre |
| **Total cost at scale** | Often **lower** in large, changing halls | Lower for small, fixed ones |
| **Thermal and fault data** | Verified as a system | Depends on site installation |
| **Inspection** | Thermographic scans of joints | Many terminations to check |

Most large sites use **both**: overhead **busway** for the trunk run along the rack rows and **cable** for the short drops from the tap-offs to the racks.

## 4. Design points

- **Joints** and connections are the weak spots, so **scan** them and keep torque correct.
- **Thermal expansion** needs expansion units on long runs.
- **Fire barriers** where it passes through walls and floors.
- **Support** at the right spacing, with seismic bracing where needed.
- **Tap-off sizing:** keep the rack's current within about **80%** of the tap-off rating.
- **Monitoring:** many systems have metering in the tap-offs.
- **A and B busway:** run separate busways (A and B) with separate supports.
- **Access:** high-level installation needs safe access for work.

## 5. Worked examples

**Sizing the run.** **10 racks at 8 kW** = 80 kW, at 400 V and PF 0.95:

```
I = 80,000 / (1.732 × 400 × 0.95) = 121.5 A
Add 25% growth: 100 kW → about 152 A  →  choose a 160 A busway
```

**Sizing a tap-off.** A **40 kW rack** at 400 V, PF 0.95:

```
I = 40,000 / (1.732 × 400 × 0.95) = 60.8 A
Keep within 80% of the tap-off rating: 60.8 / 0.8 = 76 A  →  choose a 100 A tap-off
```

**An 8 kW rack:** I = 8,000 / (692.8 × 0.95) = 12.2 A, so 12.2 / 0.8 = 15.2 A, so a **16 A** tap-off is the minimum, and **32 A** gives room to grow.

---

# 6.25 Power cabling distribution methods

## 1. The methods

| Method | Description | Pros | Cons |
| --- | --- | --- | --- |
| **Under-floor cables** | Cables in the raised floor void (trays or conduits) | Hidden, short drops, no overhead clutter | Can block airflow, harder to access, water risk |
| **Overhead cable tray / ladder** | Trays above racks | Clear floor void, easy access | Needs ceiling space, can obstruct light, detection and containment |
| **Overhead busway** | Plug-in busway with tap-offs | Flexible, quick changes, high capacity | Higher first cost |
| **Conduit / trunking** | Cables in conduit or metal trunking | Mechanical protection, good EMC | Slower to change, bulky |
| **In-row or close-coupled PDUs** | Distribution units in the row, short final cables | Shorter runs, less cabling | Uses floor space, needs feeders |
| **Direct feed to racks (hard-wired)** | Cable directly to a rack distribution unit | Simple, fixed | Hard to change |
| **Hybrid** | Busway or tray for the trunk, short cables for the final drop | Balances cost and flexibility | More design coordination |

## 2. Cable types and choice

| Item | Notes |
| --- | --- |
| **LSZH / LS0H** | Low smoke, zero halogen, so little smoke and corrosive gas in a fire. Normal in data centres |
| **Single-core vs. multi-core** | Single-core suits large currents and flexible routing (trefoil). Multi-core suits smaller circuits |
| **Armoured** | Mechanical protection and can serve as the protective conductor |
| **Flexible cords** | For final connections to equipment, rated for flexing |
| **Colour and labelling** | Phase colours, and clear A/B identification (for example different sleeve colours) |

## 3. Derating

The cable must carry the **design current after derating**:

```
Required tabulated rating = design current / (product of derating factors)
```

**Worked example (illustrative factors [CHECK]).** A circuit needs **100 A**. It is **grouped with five other circuits** (grouping factor about **0.57**) in a warm location:

```
Required tabulated current-carrying capacity = 100 / 0.57 = 175 A
```

So choose a cable that can carry about **175 A** in free air or reference conditions, since grouping reduces its real capacity by nearly half. (Ambient temperature adds another factor.)

## 4. Safe working

- Switch off and **prove dead** before working on cables, or follow strict **live-work** procedures.
- Control **arc-flash** risk with labelling and PPE.
- Torque terminations, check with **thermography**, and keep drawings and labels accurate.

---

# 6.26 Grounding

## 1. Definitions

| Term | Meaning | Purpose |
| --- | --- | --- |
| **Grounding (earthing)** | Connecting the electrical system to the **earth** | A path for fault current and lightning, and a stable 0 V reference |
| **Bonding** | Connecting **metal parts to each other** | Keeps everything at the **same voltage** (equipotential) |

**Grounding connects to earth, bonding connects things to each other.** In practice everything is bonded into one network and that network is grounded.

**Why:** safety, lightning and surge protection, equipment protection, noise reduction (EMC) and static (ESD) control.

## 2. The two return wires

| Wire | Everyday job | Emergency job |
| --- | --- | --- |
| **L (line / live)** | Carries power **to** the equipment | |
| **Neutral (N)** | Carries the normal return current | None |
| **Protective earth (PE)** | **Nothing.** No current in normal operation | Carries fault current so the breaker trips |

## 3. Tripping the breaker

| Cause | How it trips |
| --- | --- |
| **Overload** | A heat-sensitive part trips it after a delay |
| **Short circuit or earth fault** | A magnet pulls the switch open almost instantly |

For an earth fault to trip a breaker quickly, the fault current must be large, which needs a **low-resistance earth path**. For a 230 V supply and a 32 A breaker:

| Earth path | Fault current | Result |
| --- | --- | --- |
| 0.5 Ω | 460 A | Trips almost instantly |
| 23 Ω | 10 A | **Does not trip.** The case stays live |

An **RCD** trips on a leakage of a few milliamps.

## 4. Earthing system types (IEC 60364)

| Position | Letter | Meaning |
| --- | --- | --- |
| First (the **source**) | **T** | Earthed directly |
| | **I** | Isolated from earth, or via a high impedance |
| Second (the **equipment case**) | **T** | Own earth rod at the building |
| | **N** | Earthed through the supply's own earthed point, by a wire |
| Third (TN only) | **S** | **Separate** neutral and PE |
| | **C** | **Combined** neutral and PE (PEN) |

| System | How it works | Data centre suitability |
| --- | --- | --- |
| **TN-S** | Source earthed. Separate N and PE all the way | **Preferred.** Neutral current stays in the neutral |
| **TN-C** | Combined PEN all the way | **Avoid.** Neutral current flows in earth and building metalwork |
| **TN-C-S** | Combined upstream, split into N and PE at the building entrance | Acceptable if split **once** and kept separate after |
| **TT** | Source earthed, building has its **own independent** electrode | Needs RCDs. Less common |
| **IT** | Source isolated. First fault doesn't trip | Special cases, with insulation monitoring |

**TN vs. TT:** in TN the fault current returns through a **wire** (large current, trips fast). In TT it returns **through the soil** (small current, so an RCD is needed). With server leakage currents adding up, **TT with RCDs is awkward for data centres**.

**Which is used where:** the **utility** decides the supply system outside (UK often TN-C-S, Germany TN-C-S, France often TT). The **designer** decides the system **inside**. A site with its **own transformer** creates a new source, usually **TN-S**. Local regulations always apply.

## 5. Bonding of neutral and ground **[SLIDE]**

- For reliable ICT equipment performance, the **neutral-ground bond should be as close to the ICT equipment as possible**.
  - This **requires isolation transformers**.
  - It should be **not too close, to avoid possible EMF**.
- **Isolation transformers are based on delta-wye.**

**Single-point rule:** the neutral is bonded to earth at **one point** per supply source. A second bond lets neutral current flow in the ground wires and metalwork (the TN-C noise problem).

**Why delta on the input and wye on the output:**

| Side | Winding | Why |
| --- | --- | --- |
| **Input (primary)** | **Delta**, no neutral needed | Traps **third harmonics** (they circulate in the triangle), isolates the upstream supply, copes with unbalanced loads |
| **Output (secondary)** | **Wye (star)** | The star point is the **new neutral**, which is bonded to ground. Gives phase-to-neutral and line voltages |

Delta-delta has no neutral, wye-wye lets harmonics pass upstream. Delta-wye is the norm (often **Dyn11**), though **transformerless** designs exist where the upstream transformer's bond serves the site.

## 6. The bonding network

```
Earth electrode (ring around building, rods, foundation steel)
        │
        ▼
Primary bonding busbar (PBB, also MET / MGB), the central connection point
        │
        ├──► PE conductors to switchboards, PDUs, rack PDUs
        ├──► Backbone conductor (TBB) ──► Secondary bonding busbar (SBB) in the room
        │                                    ├──► Mesh / signal reference grid under the raised floor
        │                                    │         ├──► Pedestal bonds
        │                                    │         └──► Rack bonding busbar ──► each rack frame
        ├──► Lightning down conductors from the roof
        └──► Incoming pipes, cable shields, building steel (bonded at the entry point)
```

| Part | Role |
| --- | --- |
| **Earth electrode** | Ring, rods or foundation steel in contact with the soil |
| **PBB / MET / MGB** | Central bonding point (older US names: TMGB) |
| **TBB (backbone)** | Heavy, **continuous** conductor, never daisy-chained. It equalises voltage and is not a fault-current return path |
| **SBB** | Room-level busbar (older US name: TGB) |
| **Mesh / signal reference grid** | Many short low-impedance paths under the floor, good for high-frequency noise |
| **Rack bonding busbar** | Bonds each rack and its equipment to the grid |
| **CBN** | The whole bonded network, acting as one |

The approach is a **single common bonded network**. A separate "clean" computer earth is discouraged, because separate earths can sit at different voltages during a surge.

**What is bonded:** racks, doors and panels, raised floor pedestals and stringers (see Module 4.5), cable trays and conduit, cooling equipment and pipes, switchboards, UPS cabinets and battery racks, the generator, building steel, entering metal services and cable shields, lightning conductors. **Joints** are exothermic welded, compression lugs, or clean bolted with anti-oxidant. Bonds must be **metal-to-metal** (paint insulates).

## 7. Ground loops

A **ground loop** forms when two devices are earthed by **more than one path**. Stray magnetic fields or small voltage differences drive circulating current around the loop, causing hum, noise or errors. Avoid it with a **single neutral-earth bond** per source, a **common bonded network**, short low-impedance bonds and careful shield routing.

## 8. Lightning and surge protection (IEC 62305)

| Part | Components |
| --- | --- |
| **External (LPS)** | Air terminals on the roof, down conductors, earth termination |
| **Internal** | Equipotential bonding of all incoming services at **one point**, plus **surge protective devices** |

| SPD type | Where | Job |
| --- | --- | --- |
| **Type 1** | Main incoming board | Direct lightning current |
| **Type 2** | Distribution boards | Remaining surges |
| **Type 3** | At or near the equipment | Final fine protection |

All services (power, telecom, water, gas) **enter at one location** and are bonded there, so lightning current cannot find a path through the equipment.

## 9. Standards **[CHECK]**

| Layer | Standards |
| --- | --- |
| **Electrical safety (mandatory)** | IEC 60364 (parts 4-41, 5-54), BS 7671, NFPA 70 (NEC) Article 250, national regulations. The **local code always wins** |
| **Bonding networks for ICT (usually voluntary)** | **EN 50310** (Europe, with a 2026 amendment), **ANSI/TIA-607** (the 607-E edition was announced in May 2024), **ISO/IEC 30129**, EN 50600-2-2, IEEE 1100 and 142 |
| **Lightning and surge** | IEC 62305, IEC 61643, NFPA 780 |

TIA-607 uses the terms **PBB** and **SBB** (formerly called the TMGB and TGB). Electrical bonding is required by code where needed for safety. A telecom bonding infrastructure is usually only recommended by code, and applies through the specification. TIA-607 does not give a maximum ground resistance for telecoms grounding.

## 10. What a data centre must have in place

| Area | An auditor would ask |
| --- | --- |
| **Design** | Is the earthing system defined (usually TN-S inside), risk-assessed and drawn? |
| **Neutral** | Is the neutral bonded to earth at **one point** per source? |
| **PE and protection** | Do PE wires reach every board, PDU and rack PDU? Do breakers disconnect faults in time? |
| **Electrode** | Is there a ring or foundation electrode and a main terminal? |
| **Backbone and busbars** | Is the backbone continuous and labelled, with a PBB and a busbar in every room? |
| **Mesh and racks** | Is there a grid in the white space and is every rack bonded metal-to-metal? |
| **Metalwork** | Are floors, trays, pipes, steel and cooling plant bonded? |
| **Entry point** | Do all services enter together and bond there, with SPDs fitted? |
| **Evidence** | Are continuity, resistance, electrode and fault-loop tests recorded, with labels and as-built drawings? |
| **Upkeep** | Is there a schedule for inspection and re-testing, and re-testing after changes? |

---

## Glossary

| Term | Meaning |
| --- | --- |
| 3P+N+PE | Three phases, neutral and protective earth |
| LSZH | Low smoke, zero halogen cable |
| IEC 60309 | Industrial plug and socket system (blue 230 V, red 400 V) |
| Phase rotation | The order in which the phases peak (L1, L2, L3) |
| Imbalance (%) | Largest deviation from the average ÷ average |
| Triplen harmonics | Multiples of the third harmonic, which add in the neutral |
| Dual-corded | Equipment with two power supplies on separate paths |
| 3N/2 | Three systems, any two carry the full load |
| Series / parallel availability | Multiply availabilities / combine unavailabilities |
| EPO | Emergency power off |
| Discrimination | A fault trips only the nearest breaker |
| Busbar trunking | Enclosed busbar system with tap-offs (IEC 61439-6) |
| Tap-off | A unit that plugs into the busbar to feed a load |
| Icw | Short-time withstand current |
| PBB / SBB / TBB | Primary / secondary bonding busbar, bonding backbone |
| Ground loop | Circulating current from more than one earth path |
| SPD | Surge protective device |

## Exam takeaways

**6.15 to 6.17: phases**

- A full three-phase supply is **3P+N+PE**. Colours: **IEC brown, black, grey, blue (neutral), green/yellow**. US phase colours are convention.
- **P = √3 × V × I**: 32 A at 400 V is about **22 kW**. Higher voltage halves the current.
- **Check phase rotation**, use **LSZH** cable, label everything, torque terminations.
- Single-phase 230 V: 16 A is about 3.7 kW, 32 A about 7.4 kW. Server leakage current can trip RCDs.
- **Imbalance = largest deviation ÷ average.** Balanced loads give **zero neutral current**. **Third harmonics add up in the neutral.** Typical working target about ±10%.

**6.18 to 6.20: routing and multiple sources**

- Keep **A and B routes separate**, power apart from data (EN 50174-2:2018: separation **A = S × P**), **cross at 90°**.
- **Dual-corded** equipment: two PSUs on two paths. **Each path sized for the full load**, run at no more than about 40 to 50%.
- **Single-corded**: rack ATS or STS.
- **3N/2:** each system **66.7%** loaded, **1.5 × L installed** vs. 2 × L for 2N. No redundancy left after one failure.

**6.21 to 6.22: availability**

- **Series multiplies**, **parallel combines unavailability**. Redundancy of **one stage** only is limited by the others.
- Improve **MTBF** (redundancy, no SPOF, maintenance) and **MTTR** (spares, training, modular). Protect against **human error** and **EPO** misuse.

**6.23 to 6.25: distribution**

- Topologies: **radial, primary selective, secondary selective, ring, A/B**. **Discrimination** limits a fault to the nearest breaker.
- **Busway** wins above about **630 to 800 A**, on long runs and changing loads (IEC 61439-6, UL 857). Tap-off within **80%** of rating. **Hybrid** with cable drops is typical.
- **Derate** cables for grouping and temperature. **LSZH** in data centres.

**6.26: grounding**

- **Grounding** connects to earth, **bonding** connects parts together. **PE** is empty until a fault. **TN-S preferred**, **TN-C avoided**, **TT** needs RCDs.
- **Neutral-ground bond at one point**, close to the equipment (delta-wye isolation transformer), not too close (EMF).
- **Common bonded network**: PBB, continuous backbone, SBBs, mesh, rack bonds. **All services enter at one point.** Standards: **EN 50310, TIA-607, IEC 60364, IEC 62305**.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **IEC 60446**, **NFPA 70** (NEC) | Conductor colours |
| **IEC 60502** | Power cables |
| **IEC 60332**, **IEC 60754**, **IEC 61034**, **EN 50575** | Cable fire, smoke and halogen performance |
| **IEC 60364-5-52** | Cable derating |
| **IEC 60309**, **IEC 60320** | Connectors |
| **NEMA MG 1** | Voltage unbalance limits |
| **EN 50174-2:2018**, **BS 6701** | Power and data separation, and the safety minimum |
| **IEC 61439-6**, **UL 857** | Busbar trunking |
| **IEC 60364**, **BS 7671**, **NFPA 70** Article 250 | Earthing systems and protection |
| **IEC 62305**, **IEC 61643**, **NFPA 780** | Lightning and surge protection |
| **EN 50310** (with its 2026 amendment), **ANSI/TIA-607-E** (2024), **ISO/IEC 30129** | Bonding networks |
| **EN 50600-2-2**, **ETSI EN 300 253**, **IEEE 1100**, **IEEE 142** | Power distribution, telecom centre earthing, grounding practice |
| **Uptime Institute Tier Standard** | Redundancy classes |
| **EPI slide** (bonding of neutral and ground) | Neutral-ground bond and the delta-wye isolation transformer |
| Reliability engineering | Series and parallel availability formulas |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
