# Module 6: Power Infrastructure (index and review)

Module 6 is the largest module in the course (47 lessons), so its notes are split into four detailed files plus a physics companion. **This file is the map and the quick-review sheet.**

**Objectives (from your slide).** After this module you should be able to describe and understand:

- Sustainability
- Microgrid
- The various components in the power distribution chain
- Various redundancy levels and techniques
- How to achieve proper power distribution within the data centre
- The difference between bonding and grounding and how to apply it in the mission critical site

> **Conventions.** **[SLIDE]** marks content taken from a slide you showed me. **[CHECK]** marks figures from general industry practice or outside research. If your course gives a different number, use your course.

---

## 1. The files

| File | Lessons | Contents |
| --- | --- | --- |
| [06-1_incoming_power_to_transfer_switches.md](06-1_incoming_power_to_transfer_switches.md) | **6.1 to 6.14** | Incoming power, renewables, microgrids (including nuclear), power quality (EN 50160), power requirements, source to destination, transformers, **redundancy options I to III**, generator sets, ATS, STS |
| [06-2_phases_distribution_grounding.md](06-2_phases_distribution_grounding.md) | **6.15 to 6.26** | Three-phase and single-phase cabling, phase balancing, cable routing, dual and triple supply, availability options and techniques, power distribution, busbar trunking, cabling methods, **grounding and bonding** |
| [06-3_power_quality_and_sizing.md](06-3_power_quality_and_sizing.md) | **6.27 to 6.35** | Common mode noise, distribution boards, IP grades, power quality guidelines (IEEE 519), harmonics, CBEMA/ITIC curve, power factor, label vs. consumed power, sizing power |
| [06-4_ups_and_batteries.md](06-4_ups_and_batteries.md) | **6.36 to 6.47** | UPS technologies, static UPS and its modes, comparison, energy-friendly, modular, increased availability, dynamic UPS, batteries, battery testing, BESS, thermographic scanning |
| [06a_electrical_physics_foundations.md](06a_electrical_physics_foundations.md) | companion | Watt's law, I²R, transformers, three-phase, line vs. phase voltage, √3, S/P/Q, harmonics: the physics behind the module |

## 2. Lesson map

| Lesson | Title | Where |
| --- | --- | --- |
| 6.1 | Incoming Power | [06-1](06-1_incoming_power_to_transfer_switches.md#61-incoming-power) |
| 6.2 | Renewable Energy | [06-1](06-1_incoming_power_to_transfer_switches.md#62-renewable-energy) |
| 6.3 | Microgrid | [06-1](06-1_incoming_power_to_transfer_switches.md#63-microgrid) |
| 6.4 | Microgrid: Nuclear Power | [06-1](06-1_incoming_power_to_transfer_switches.md#64-microgrid-nuclear-power) |
| 6.5 | Power Supply Quality | [06-1](06-1_incoming_power_to_transfer_switches.md#65-power-supply-quality) |
| 6.6 | Power Requirements | [06-1](06-1_incoming_power_to_transfer_switches.md#66-power-requirements) |
| 6.7 | Power: From Source to Destination | [06-1](06-1_incoming_power_to_transfer_switches.md#67-power-from-source-to-destination-slide) |
| 6.8 | Transformers | [06-1](06-1_incoming_power_to_transfer_switches.md#68-transformers) |
| 6.9 | Redundancy Options I | [06-1](06-1_incoming_power_to_transfer_switches.md#69-redundancy-options-i-the-source-side) |
| 6.10 | Generator Sets | [06-1](06-1_incoming_power_to_transfer_switches.md#610-generator-sets-slide) |
| 6.11 | Automatic Transfer Switch (ATS) Panel | [06-1](06-1_incoming_power_to_transfer_switches.md#611-automatic-transfer-switch-ats-panel) |
| 6.12 | Redundancy Options II | [06-1](06-1_incoming_power_to_transfer_switches.md#612-redundancy-options-ii-ups-level) |
| 6.13 | Static Transfer Switch (STS) | [06-1](06-1_incoming_power_to_transfer_switches.md#613-static-transfer-switch-sts) |
| 6.14 | Redundancy Options III | [06-1](06-1_incoming_power_to_transfer_switches.md#614-redundancy-options-iii-dual-path-and-the-sts-slide) |
| 6.15 | Three Phase Power Cabling | [06-2](06-2_phases_distribution_grounding.md#615-three-phase-power-cabling) |
| 6.16 | Single Phase Power | [06-2](06-2_phases_distribution_grounding.md#616-single-phase-power) |
| 6.17 | Phase Balancing | [06-2](06-2_phases_distribution_grounding.md#617-phase-balancing) |
| 6.18 | Power Cable Routing | [06-2](06-2_phases_distribution_grounding.md#618-power-cable-routing) |
| 6.19 | Dual Power Sources | [06-2](06-2_phases_distribution_grounding.md#619-dual-power-sources) |
| 6.20 | Triple Power Supply | [06-2](06-2_phases_distribution_grounding.md#620-triple-power-supply) |
| 6.21 | Availability Options | [06-2](06-2_phases_distribution_grounding.md#621-availability-options) |
| 6.22 | Techniques for Power Availability | [06-2](06-2_phases_distribution_grounding.md#622-techniques-for-power-availability) |
| 6.23 | Power Distribution | [06-2](06-2_phases_distribution_grounding.md#623-power-distribution) |
| 6.24 | Busbar Trunking | [06-2](06-2_phases_distribution_grounding.md#624-busbar-trunking) |
| 6.25 | Power Cabling Distribution Methods | [06-2](06-2_phases_distribution_grounding.md#625-power-cabling-distribution-methods) |
| 6.26 | Grounding | [06-2](06-2_phases_distribution_grounding.md#626-grounding) |
| 6.27 | Common Mode Noise (CMN) | [06-3](06-3_power_quality_and_sizing.md#627-common-mode-noise-cmn) |
| 6.28 | Distribution Board (DB) | [06-3](06-3_power_quality_and_sizing.md#628-distribution-board-db) |
| 6.29 | Ingress Protection (IP) Grades | [06-3](06-3_power_quality_and_sizing.md#629-ingress-protection-ip-grades) |
| 6.30 | Power Quality Guidelines | [06-3](06-3_power_quality_and_sizing.md#630-power-quality-guidelines) |
| 6.31 | Harmonics | [06-3](06-3_power_quality_and_sizing.md#631-harmonics) |
| 6.32 | CBEMA Curve | [06-3](06-3_power_quality_and_sizing.md#632-cbema-curve) |
| 6.33 | Power Factor | [06-3](06-3_power_quality_and_sizing.md#633-power-factor) |
| 6.34 | Label Power versus Consumed Power | [06-3](06-3_power_quality_and_sizing.md#634-label-power-versus-consumed-power) |
| 6.35 | Sizing Power | [06-3](06-3_power_quality_and_sizing.md#635-sizing-power) |
| 6.36 | UPS Technologies | [06-4](06-4_ups_and_batteries.md#636-ups-technologies) |
| 6.37 | Static UPS | [06-4](06-4_ups_and_batteries.md#637-static-ups) |
| 6.38 | Static UPS Operating Modes | [06-4](06-4_ups_and_batteries.md#638-static-ups-operating-modes) |
| 6.39 | Static UPS Quick Comparison Table | [06-4](06-4_ups_and_batteries.md#639-static-ups-quick-comparison-table) |
| 6.40 | Energy-Friendly UPS | [06-4](06-4_ups_and_batteries.md#640-energy-friendly-ups) |
| 6.41 | Modular UPS | [06-4](06-4_ups_and_batteries.md#641-modular-ups) |
| 6.42 | UPS Increased Availability | [06-4](06-4_ups_and_batteries.md#642-ups-increased-availability) |
| 6.43 | Dynamic UPS | [06-4](06-4_ups_and_batteries.md#643-dynamic-ups) |
| 6.44 | Batteries for UPS Systems | [06-4](06-4_ups_and_batteries.md#644-batteries-for-ups-systems) |
| 6.45 | Battery Testing | [06-4](06-4_ups_and_batteries.md#645-battery-testing) |
| 6.46 | Battery Energy Storage System (BESS) | [06-4](06-4_ups_and_batteries.md#646-battery-energy-storage-system-bess) |
| 6.47 | Thermographic Scanning | [06-4](06-4_ups_and_batteries.md#647-thermographic-scanning) |

## 3. Objectives checklist

| Objective | Main lessons |
| --- | --- |
| **Sustainability** | 6.2 (renewables), 6.40 (energy-friendly UPS), and the metrics in section 5 below |
| **Microgrid** | 6.3, 6.4 |
| **Components of the power distribution chain** | 6.1, 6.7, 6.8, 6.10, 6.11, 6.13, 6.36 to 6.39, 6.23 |
| **Redundancy levels and techniques** | 6.9, 6.12, 6.14, 6.19 to 6.22, 6.41, 6.42 |
| **Power distribution within the data centre** | 6.15 to 6.19, 6.23 to 6.25, 6.28 |
| **Bonding vs. grounding** | 6.26, 6.27 |

---

## 4. The power chain on one page

```
 Grid ─► MV switchgear ─► Transformer ─► LV main board (ATS ◄── Generator)
                                              │
                                     UPS (rectifier ─ DC bus/battery ─ inverter)
                                              │
                          UPS output board ─► PDU ─► RPP / busway ─► Rack PDU ─► Server
        (A path and B path, each complete; dual-corded servers use both)
```

| Stage | Key points |
| --- | --- |
| **Incoming power** | MV or HV connection, two diverse feeds, firm capacity |
| **Transformer** | Dyn11 common, uk sets fault current, losses 1 to 2% |
| **Generator** | NFPA 110 Level 1 Type 10 (10 s), size = UPS × 1.0 or 1.2 + cooling and lighting × 1.0 **[SLIDE]** |
| **ATS** | Utility to generator, open/delayed/closed transition, 4-pole if separately derived, bypass-isolation |
| **UPS** | VFI in data centres, battery minutes, static bypass, eco mode risk |
| **STS** | A few ms, between two UPS-fed sources, itself a single point of failure |
| **Distribution** | A/B paths, PDU, RPP or busway, rack PDU, each path sized for the full load |
| **Earthing** | TN-S inside, one neutral-ground bond, common bonded network, delta-wye isolation transformer **[SLIDE]** |

## 5. Sustainability metrics (ISO/IEC 30134, EN 50600-4)

| Metric | Formula / meaning | Notes |
| --- | --- | --- |
| **PUE** (Power Usage Effectiveness) | **Total facility energy ÷ IT equipment energy** | Ideal **1.0**, lower is better. Efficient modern sites about 1.2 to 1.5 **[CHECK]** |
| **DCiE** | **IT energy ÷ total energy × 100%** (the inverse of PUE) | Higher is better |
| **WUE** (Water Usage Effectiveness) | Litres of water per kWh of IT energy | Matters where cooling uses water |
| **CUE** (Carbon Usage Effectiveness) | kg CO₂ per kWh of IT energy | Depends on the energy source |
| **REF** (Renewable Energy Factor) | Share of energy from renewable sources | |
| **ERF** (Energy Reuse Factor) | Share of energy reused, for example waste heat | |

**PUE measurement levels** (The Green Grid): **Level 1** at the UPS output, **Level 2** at the PDU output, **Level 3** at the IT equipment input. A higher level is more accurate.

**Worked example.** A site draws **1,500 kW** in total and **1,000 kW** reaches the IT equipment: PUE = 1,500 / 1,000 = **1.5**, DCiE = 1,000 / 1,500 = **67%**.

**Ways to improve:** efficient UPS (and eco mode where suitable), low-loss transformers, free cooling and containment, higher supply air temperature (within ASHRAE limits), renewable energy and waste heat reuse, right-sizing, LED lighting, monitoring and management systems (**ISO 50001**). The **EU Code of Conduct for Data Centres** is the main voluntary best-practice programme in Europe.

## 6. Key formulas

| Topic | Formula |
| --- | --- |
| Power (single-phase) | P = V × I × PF |
| Power (three-phase) | P = √3 × V_line × I × PF |
| Line and phase voltage | V_line = √3 × V_phase |
| Cable loss | P_loss = I² × R |
| Transformer | V₂/V₁ = N₂/N₁, and V₁I₁ ≈ V₂I₂ |
| Transformer fault current | I_sc = I_n / uk |
| Apparent power | S = P / PF, S² = P² + Q² |
| Availability | MTBF / (MTBF + MTTR) |
| Series / parallel availability | A₁A₂... / 1 − (1 − A₁)(1 − A₂) |
| Phase imbalance | max deviation from average ÷ average × 100 |
| Neutral current (linear) | √(Ia² + Ib² + Ic² − IaIb − IbIc − IaIc) |
| THD | √(sum of harmonic²) ÷ fundamental |
| PF correction | Qc = P (tan φ₁ − tan φ₂) |
| UPS losses | P_out × (1/η − 1) |
| Battery energy | P × t ÷ η, then margins |
| Total facility power | IT load × PUE |

## 7. Numbers worth remembering

| Item | Value |
| --- | --- |
| Generator transfer | NFPA 110 Type 10: within **10 s** |
| ATS open transition | about **40 to 200 ms** |
| STS | **a few ms** (under about 8 ms) |
| ITIC curve | ±10% steady, **120% for 0.5 s**, 70% for 0.5 s, 80% for 10 s, **0 V for 20 ms** |
| EN 50160 | ±10% voltage (95% of week), THD ≤ 8%, 50 Hz ±1% (99.5% of year) |
| IEEE 519 | Voltage THD 8% below 1 kV, TDD limits 5/8/12/15/20% by ISC/IL |
| Battery replacement | At about **80%** capacity, acceptance at least about 90% |
| Battery life | Halves per 8 to 10 °C above 25 °C |
| Lead-acid cell | 2 V nominal, 1.75 V end-of-discharge, about 2.25 to 2.30 V float |
| Busway vs. cable | Busway preferred above about 630 to 800 A |
| Thermography | Under load (≥ about 40%), over 15 °C vs. similar = major |
| NFPA 70B thermography | 12 months (6 months for poor condition) |
| IP54 | Dust-protected, splash-proof |
| 2N each side | about 50% loaded, sized for 100% |
| 3N/2 | each system 66.7% loaded |

## 8. Mixed review questions

The practice questions for this file are in [00_knowledge_tests.md](00_knowledge_tests.md#mixed-review-across-module-6).

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **ISO/IEC 30134** series, **EN 50600-4** | PUE, DCiE, WUE, CUE, REF and ERF |
| **The Green Grid** | PUE measurement levels 1 to 3 |
| **ISO 50001**, **EU Code of Conduct for Data Centres** | Improvement practices |
| Part files **06-1** to **06-4** | Every other figure here summarises them. Their references are listed at the end of each |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
