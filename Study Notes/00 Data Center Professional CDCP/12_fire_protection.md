# Module 12: Fire Protection

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section |
| --- | --- | --- |
| 12.1 | Fire Protection and Safety | [Section 1](#121-fire-protection-and-safety) |
| 12.2 | Standards and Requirements for Data Centres | [Section 2](#122-standards-and-requirements-for-data-centres) |
| 12.3 | Detection Systems | [Section 3](#123-detection-systems) |
| 12.4 | Detection System: Water | [Section 4](#124-water-based-systems) |
| 12.5 | Gas Based Fire Suppression Systems I | [Section 5](#125-gas-based-fire-suppression-systems-i-agents) |
| 12.6 | Gas Based Fire Suppression Systems II | [Section 6](#126-gas-based-fire-suppression-systems-ii-system-design-and-operation) |
| 12.7 | Hypoxic Air Fire Prevention | [Section 7](#127-hypoxic-air-fire-prevention) |
| 12.8 | Fire Suppression Best Practices | [Section 8](#128-fire-suppression-best-practices) |
| 12.9 | Handheld Extinguishers | [Section 9](#129-handheld-extinguishers) |
| 12.10 | Signage and Safety | [Section 10](#1210-signage-and-safety) |
| 12.11 | Regulatory Requirements and Safety Best Practices | [Section 11](#1211-regulatory-requirements-and-safety-best-practices) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-12-fire-protection) |

**Objectives (from your slide).** After this module you should be able to describe and understand:

- The most common causes of fire
- Requirements for fire suppression systems
- Some standards and contents
- Fire detection systems
- The various gas and non-gas based fire suppression systems available
- The various classes of fire and which handheld fire extinguishers to use
- Requirements for signage and safety
- Regulatory requirements

| Objective | Where it is covered |
| --- | --- |
| **Most common causes of fire** | 12.1 |
| **Requirements for fire suppression systems** | 12.2, 12.4 to 12.8 |
| **Some standards and contents** | 12.2 (and the standards table in each lesson) |
| **Fire detection systems** | 12.3 |
| **Gas and non-gas based suppression systems** | 12.4 (water), 12.5 and 12.6 (gas), 12.7 (oxygen reduction), 12.8 |
| **Classes of fire and handheld extinguishers** | 12.9 |
| **Signage and safety** | 12.10 |
| **Regulatory requirements** | 12.11 |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Only the **objectives slide** was available for this module (not the lesson slides), so check the glossary and figures against your course. Your index titles lesson 12.4 "Detection System: Water". I read it as **water-based suppression** (sprinklers and water mist), because that is the lesson that completes the "gas and non-gas based" objective. Related earlier material: aisle containment and fire suppression (9.13 in `09_cooling_infrastructure.md`), battery rooms and NFPA 855 (6.44 in `06-4`), thermography (6.47), site and building construction (Module 3), fire stops and cable pathways (Modules 4 and 11), emergency lighting (Module 5), and the fire reserve of water (10.2 in `10_water_supply.md`).

## The big picture

A data centre is a **small, dense fire risk**: electrical power at very high density, batteries, cables, plastic and packaging, in a building whose business value is far higher than the building itself. Protection therefore has two goals that sometimes pull in different directions:

1. **Life safety**: people must be warned and get out.
2. **Business continuity and property protection**: stop the fire **small and early**, without the **collateral damage** (water, gas discharge, smoke, shutdown) that can cost more than the fire.

The answer is **layered protection**:

```
Prevent (design, maintenance, housekeeping) → Detect early → Alarm and evacuate → Contain (fire-rated rooms) → Suppress → Recover
```

---

# 12.1 Fire protection and safety

## 1.1 How a fire works

A fire needs **fuel, heat and oxygen**, plus an uninterrupted **chemical chain reaction** (the fire tetrahedron). Remove one and the fire stops.

| Element removed | How | Example |
| --- | --- | --- |
| **Heat** | Cool the fuel | Water sprinklers, water mist, halocarbon clean agents (they absorb heat) |
| **Oxygen** | Smother or dilute | Inert gas systems, CO₂, hypoxic air |
| **Fuel** | Remove or isolate it | Cutting power, closing fuel valves, good housekeeping |
| **Chain reaction** | Interrupt the combustion chemistry | Some halocarbon agents, dry chemical |

### Stages of a fire

| Stage | What happens | Detection and response |
| --- | --- | --- |
| **Incipient** | Overheating or **smouldering**: invisible particles, no flame | **Very early warning (aspirating) detection** finds it. A person can act. Minutes to hours |
| **Growth** | Visible smoke, then flame | Standard smoke detectors, alarm, suppression |
| **Fully developed** | Whole room involved, very hot | Suppression and the fire service. Heavy damage |
| **Decay** | Fuel is consumed | Recovery |

**Why early detection is the most important layer:** at the incipient stage almost nothing has burned, and the response (isolate the equipment, call staff) is cheap. By the growth stage the damage, smoke and downtime rise steeply.

## 1.2 Why data centres need special treatment

| Feature | Effect |
| --- | --- |
| **Very high electrical load and many connections** | Heat and arcing faults at connections |
| **Batteries (including lithium-ion)** | Stored energy that can cause thermal runaway |
| **Large quantities of cable and plastic** | Fuel, and smoke with corrosive gases |
| **High airflow** | Dilutes smoke (so detectors react late) and feeds a fire |
| **Raised floors and ceiling voids** | Hidden spaces full of cable where fire can start and spread unseen |
| **Sensitive electronics** | **Smoke particles and acid gases damage equipment** even without flame, and water or powder residue can be as bad as the fire |
| **High value and continuous service** | Downtime costs often exceed the fire damage |
| **Few people present** | A small fire may burn unnoticed unless detected automatically |

## 1.3 The most common causes of fire

| Cause | How it starts | Examples and notes |
| --- | --- | --- |
| **UPS and batteries** | Internal faults, overheating, overcharging, physical damage, or **thermal runaway** in lithium-ion cells. Lead-acid batteries also burn (electrical faults, hydrogen) | The leading named location in public incident records. **Lithium-ion UPS batteries** are a clear contributing factor, according to the Uptime Institute's 2026 analysis |
| **Electrical faults and overload** | Loose or corroded connections (resistance heating), arcing, overloaded circuits and power strips, failed breakers | The commonest ignition source in electrical rooms. Found early by **thermography** (6.47) |
| **Switchgear, transformers and power cabinets** | Insulation failure, arc faults, contamination | Fires often start and end in the electrical room |
| **Cabling** | Damaged or overheated cable, poor terminations, overfilled trays | A large fuel load. PoE and power cables can overheat in bundles |
| **Generators and fuel** | Fuel leaks onto hot surfaces, exhaust, faulty wiring | Fuel-related incidents |
| **Cooling and mechanical plant** | Motor and drive faults, bearings, overheating | Modules 9 and 10 |
| **Hot work and construction** | Welding, cutting, grinding, temporary power near combustibles | **Construction, testing and commissioning** are high-risk phases: systems are energised for the first time with many contractors present |
| **Combustible storage and packaging** | Cardboard, pallets, plastic wrap and spare parts stored in the data hall | Housekeeping failures supply fuel |
| **Dust build-up** | Insulates and can ignite or cause tracking | Inadequate maintenance |
| **Human error and poor procedures** | Incorrect installation, incomplete isolation of power, bypassing safety steps, untrained or unqualified workers | A contributing factor in about nine out of ten outages (Uptime), not counted as a primary cause |
| **Arson, external fire, lightning** | Outside ignition sources | Site security, lightning protection (Modules 3 and 6) |
| **Leaks and cooling failure** | Overheating of equipment when cooling fails | Linked to Module 9 |

### What the records show **[CHECK]**

| Source | Finding |
| --- | --- |
| **Uptime Institute, Annual Outage Analysis 2026** | The frequency of **major data centre fires has increased gradually** in recent years, with **lithium-ion UPS batteries** a clear contributing factor. Part of the rise reflects the build-out of new facilities. Fires remain a **small share of outages** compared with power and network failures |
| **Energy Incident Register (to November 2026)** | 179 data centre incidents in power systems since 2010, of which **59 were fires or thermal events** (33%). Where the part is named, **UPS and battery rooms** appear most often (74 entries), then **backup generators** (57) and **switchgear and electrical rooms** (31) |
| **Allianz Commercial, 2026 claims analysis** | **Fire accounts for well over half** of about €700 million of analysed data centre losses. **Testing and commissioning** are flagged as high-risk |
| **Uptime Institute** | Most fire incidents begin and end in the **electrical room**. Faults in UPS equipment usually create heat and smoke rather than a large fire, but **nearby batteries can catch fire** and burn until the fuel is consumed. Accidental discharge of fire suppression, especially high-pressure clean agent systems, has caused serious disruption on its own |

### Lessons from incidents **[CHECK]**

| Incident | Lesson |
| --- | --- |
| **OVHcloud SBG2, Strasbourg (2021)** | One of the largest data centre fires by damage: a building with limited compartmentation and no automatic extinguishing in the hall, and customers without off-site backups |
| **SK C&C Pangyo (2022)** | A lithium-ion battery fire disrupted a messaging service used by millions |
| **Digital Realty Hillsboro, Oregon (2025)** | A battery room fire |
| **NIRS Daejeon, South Korea (September 2025)** | **Lithium-ion thermal runaway during relocation of UPS battery modules**. The batteries were reportedly at about **80% charge** when moved (guidelines call for below 30%), sat about **60 cm** from major servers, were past their recommended life, and **auxiliary power to the UPS was not isolated**. The fire took about **22 hours** to extinguish and disrupted **709** government systems. A single-site concentration and a lack of tested active-active backup made recovery slow |
| **Tata Communications, New Delhi (June 2026)** | Lithium battery units ignited. Customer services took about three weeks to fully restore |

**Common lessons:** separate and fire-rate battery rooms, control battery handling and charge level, isolate energy before work, keep contractors under permit, detect early, and **keep verified backups off-site**: a fire is also a **data resilience** event.

## 1.4 Consequences

| Consequence | Detail |
| --- | --- |
| **Life safety** | Smoke and toxic gases, evacuation |
| **Downtime** | Service loss while the room is cleaned or rebuilt, often days to weeks |
| **Equipment loss** | Heat damage, and **corrosion from smoke** (acid gases from burning PVC and other halogenated plastics) |
| **Collateral damage** | Water from sprinklers, powder residue, and **accidental discharge** of a suppression system |
| **Data loss** | If backups are not off-site |
| **Cost** | Downtime for large sites runs into hundreds of thousands per hour **[CHECK]** |
| **Regulatory and reputational harm** | Investigations, insurance claims |

## 1.5 Principles of fire safety

| Principle | Practice |
| --- | --- |
| **Prevention** | Design out ignition sources, maintain electrical equipment, control combustibles, permit hot work |
| **Early detection** | Aspirating detection plus standard detection (12.3) |
| **Alarm and evacuation** | Warn people and give a safe route out (12.10) |
| **Compartmentation** | **Fire-rated separation** (at least **1 hour**) of the IT area, battery rooms, electrical rooms and generator areas, with fire-stopped penetrations and fire dampers |
| **Suppression** | Water, gas or both, matched to the room (12.4 to 12.8) |
| **Emergency response** | Procedures, trained staff, fire service pre-planning |
| **Recovery** | Spares, backups, a plan for damaged electronics (NFPA 75 Annex B: the first 24 hours) |

**Two kinds of system:**

- **Life safety systems** (fire alarm, notification, evacuation, emergency lighting) protect **people**.
- **Property protection systems** (sprinklers, gas) protect **equipment and continuity**. A pre-action release panel is not the building's fire alarm panel: it does not provide occupant notification.

## 1.6 Fire risk assessment

NFPA 75 (2024) calls for a **documented fire risk assessment** of the IT equipment area, and that assessment sets the level of protection. Factors weighed include:

- **Business impact** of equipment loss or downtime, and the value of data and equipment
- **Fire load** from construction, furnishings and packaging
- **Surrounding occupancy** and adjacent risks
- **Redundancy** from off-site backup or a failover site
- **Continuity commitments** to customers and regulators

The assessment decides whether to apply the prescriptive path or a performance-based design, whether more than 1-hour separation is needed, whether gas suppression is justified, and how sensitive detection should be. In the UK a **fire risk assessment** is also a legal duty (12.11).

---

# 12.2 Standards and requirements for data centres

## 2.1 Standards and what they contain

Fire standards are **mandatory only when adopted** by a law or building code (enforced by the **authority having jurisdiction, AHJ**), or required by a **contract** or the **insurer**. The edition adopted locally often **lags** the latest.

| Standard | What it covers |
| --- | --- |
| **NFPA 75** (2024) | **Fire protection of IT equipment and IT equipment areas**: risk assessment, construction, storage, detection, suppression, extinguishers, warning signs, training, emergency and recovery procedures, aisle containment, lithium-ion UPS off-gas detection, immersion cooling, modular data centres |
| **NFPA 76** (2024) | **Fire protection of telecommunications facilities** (carrier switch sites): risk based, with **very early warning fire detection (VEWFD)** for larger equipment areas |
| **NFPA 72** (2022) | Fire alarm and signalling code: detectors, panels, notification, releasing service, testing |
| **NFPA 13** (2025) | Installation of **sprinkler systems** |
| **NFPA 25** (2023) | Inspection, testing and maintenance of **water-based** systems |
| **NFPA 750** | **Water mist** systems |
| **NFPA 2001** (2025) | **Clean agent** (gas) extinguishing systems: agents, design concentration, discharge time, hold time, safety, maintenance |
| **NFPA 10** (2026) | **Portable fire extinguishers**: selection, placement, inspection |
| **NFPA 101** | **Life Safety Code**: egress, exit signs, emergency lighting |
| **NFPA 70 (NEC) Article 645** | Electrical requirements for IT equipment rooms, including the optional emergency power-off |
| **NFPA 855** | Stationary **energy storage** (battery) installations, including lithium-ion |
| **NFPA 220, 90A, 80** | Building construction types, air-conditioning and ventilation, fire doors |
| **FM Global Data Sheets** (**5-32** data centres, **4-13** oxygen reduction, **2-0** sprinklers) | Insurer loss-prevention guidance |
| **EN 54** series | **Fire detection and alarm**: Part 2 control panels, Part 4 power supplies, Part 5 heat detectors, Part 7 smoke detectors, Part 10 flame detectors, Part 11 manual call points, Part 12 beam detectors, Part 14 design and maintenance guidance, **Part 20 aspirating detectors** |
| **EN 12845** | Sprinkler systems (Europe) |
| **EN 15004**, **ISO 14520** | **Gaseous extinguishing** systems (Europe and international), with **EN 12094** for components |
| **EN 16750**, **ISO 20338** | **Oxygen reduction** systems |
| **EN 2**, **EN 3** | Classes of fire, and portable extinguishers |
| **ISO 7010** (with ISO 3864, ISO 23601) | Safety signs, colours and evacuation plans |
| **BS 5839-1**, **BS 5306**, **BS 7273** | UK fire detection, extinguishers and electrical actuation of gaseous systems |
| **LPCB LPS 1230, LPS 1048** | Fire testing of gaseous systems, sprinkler contractor approval |
| **ANSI/TIA-942-C, Uptime Tier Standard, EN 50600** | Data centre standards with fire provisions. At **Tier IV**, **1-hour fire-rated partitions** between complementary critical systems |

**NFPA 75 vs. 76:** a data centre follows NFPA 75, a carrier switching site follows NFPA 76. Where a space mixes both, the stricter rule governs. (In the 2024 editions both standards **moved lithium-ion energy storage rules to NFPA 855**, while NFPA 75 keeps its lithium-ion UPS provisions, including off-gas detection.)

## 2.2 Core requirements for a data centre (NFPA 75 and related)

| Area | Requirement |
| --- | --- |
| **Fire risk assessment** | **Documented**, the basis of the protection level |
| **Building** | A **fully sprinklered building** of **Type I or II construction** (NFPA 220), or a single-storey Type II building |
| **Separation** | The IT equipment area separated from other occupancies by construction rated **at least 1 hour** (more if the risk assessment requires) |
| **Location** | Not **above, below or adjacent** to areas with **hazardous processes** |
| **Penetrations and openings** | Cable and pipe penetrations **fire-stopped to the same rating**. Doors and dampers close automatically on smoke or fire |
| **Materials** | Interior **wall and ceiling finishes Class A** (Class B allowed where fully sprinklered), **floor finishes Class I**, **no exposed cellular plastics** |
| **Raised floors** | Constructed to NFPA 75 rules (non-combustible supports). The structural floor must allow **removal of leaks** from cooling water, pipes or sprinkler discharge |
| **Aisle containment and hot air collars** | Permitted, but must not obstruct sprinklers or gas (9.13 in `09_cooling_infrastructure.md`) |
| **Detection** | **Smoke detection in the room, above ceilings and below raised floors that contain cable**. Early warning (aspirating) detection in the risk-based design |
| **Suppression** | Automatic **sprinklers or a gaseous system (or both)** for the IT area. **Under the raised floor** where there is a critical need to protect data or the void holds combustible material. A building without sprinklers must add them or a gaseous system |
| **Power** | Power to protected equipment is disconnected when a **total-flooding gas system discharges**, unless the risk assessment calls for continuous power. The room-level **emergency power-off (EPO)** is mainly an **NEC 645.10** provision that applies only when the Article 645 wiring allowances are used |
| **HVAC** | Dampers and shutdown interlocked with detection and release (12.6) |
| **Portable extinguishers** | **Clean agent or CO₂**, not dry chemical (12.9) |
| **Warning signs** | Required for gaseous systems and special hazards (12.10) |
| **Storage** | Limit combustible storage and packaging in the IT area (record and general storage rules) |
| **Training** | Staff trained in alarms, extinguishers, evacuation and the suppression system |
| **Emergency responders** | In-building emergency responder communications where required |
| **Monitoring** | Alarms transmitted to a **constantly attended location** |
| **Inspection, testing and maintenance (ITM)** | Regular, recorded (12.11) |
| **Expansion and renovation** | **Re-review** the fire protection when the room changes |

### Additional rules for specific hazards

| Hazard | Rule |
| --- | --- |
| **Lithium-ion UPS batteries** | NFPA 75 (2024) adds **off-gas detection** to catch electrolyte vapour **before** thermal runaway (conventional flammable gas sensors do not substitute). Stationary lithium-ion storage is governed by **NFPA 855** |
| **Immersion cooling equipment** | New requirements in NFPA 75 (2024), Chapter 8 |
| **Battery rooms** | Separate, fire-rated, ventilated, with spacing between battery cabinets (6.44 in `06-4`) |
| **Generator and fuel areas** | Fire separation, fuel containment, detection (Module 3) |

## 2.3 What the insurer adds

FM Global Data Sheet 5-32 treats **early warning detection** as a key protection measure and recommends **layered protection** (smart monitoring, early detection, suitable suppression). For **lithium-ion batteries in server racks** it does **not** accept gaseous systems or water mist as the primary protection and recommends a **wet sprinkler system with increased density** **[CHECK]**. Always involve the insurer **early**, because their requirements can exceed the code.

---

# 12.3 Detection systems

## 3.1 Purpose

Detection has three jobs: **find the fire early**, **warn people**, and **trigger the right actions** (alarm, suppression release, HVAC shutdown, door release, power control, call to the fire service). In a data centre the aim is to catch the **incipient stage** (overheating, smouldering cable or battery), before there is flame or visible smoke.

## 3.2 Types of detector

| Type | How it works | Strengths | Limits and data centre use |
| --- | --- | --- | --- |
| **Photoelectric (optical) smoke detector** | Smoke scatters a light beam into a sensor | Good at **smouldering** fires. No radioactive source. EN 54-7 | The standard **spot** detector. A listed spacing of about 9.1 m (30 ft) in each direction, so one detector covers about 83 m² (900 ft²), less with high airflow |
| **Ionisation smoke detector** | Smoke disturbs a small ionised current (a radioactive source) | Fast on flaming fires | Declining use because of the radioactive source and its sensitivity to air movement |
| **Multi-criteria detector** | Combines smoke, heat and sometimes CO sensing (EN 54-15) | Fewer false alarms | Used with cross-zoning |
| **Aspirating smoke detector (ASD)** | A **fan draws air through a pipe network** with sampling holes to a sensitive detector | **Very early warning**, works in high airflow, detectors are away from the equipment, adjustable thresholds. EN 54-20 | The **core of data centre detection**. Needs good pipe design (3.3) |
| **Heat detector** (fixed temperature, rate-of-rise) | Responds to temperature | Immune to smoke and dust, EN 54-5 | Slow. For generator rooms, fuel and dusty areas, not for early warning in the hall |
| **Linear heat detection cable** | A cable that senses temperature along its length (EN 54-22) | Covers cable trays and tunnels | Slower, for specific routes |
| **Flame detector** (UV, IR, or both) | Sees the radiation from a flame | Fast on open flame (EN 54-10) | Fuel stores, generator fuel areas, not for smouldering |
| **Beam (projected beam) smoke detector** | Smoke blocks a light beam across the room (EN 54-12) | Covers large or high spaces | Alignment, building movement |
| **Off-gas and gas sensors** | Detect **electrolyte vapour** (lithium-ion) before thermal runaway, or **hydrogen/CO** in battery rooms | Earliest sign of a battery failure | NFPA 75 (2024) requires **off-gas detection for lithium-ion UPS**, and conventional flammable gas sensors do **not** substitute |
| **Manual call points** | A person breaks the glass or presses | Always provided at exits (EN 54-11) | Raises the alarm, a backup to automatic detection |
| **Video smoke and flame analytics, thermal imaging** | Camera analysis | Complements point detection | Not a replacement for approved detectors |

## 3.3 Aspirating smoke detection in detail

### How it works

```
Sampling holes in the pipe ──► pipe network ──► ASD unit (filter, fan, laser/optical sensing chamber) ──► alarm levels
```

Air is drawn into **every sampling hole at the same time** and the samples are **combined**, so the detector sees a **diluted** mixture. The detector's sensitivity setting is far lower than that of one hole.

### Sensitivity classes (EN 54-20)

| Class | Description | Use |
| --- | --- | --- |
| **A** | **Very high sensitivity** | The earliest warning in business-critical, high-airflow or high-risk areas |
| **B** | **Enhanced sensitivity** | Early detection in challenging environments or inside critical equipment |
| **C** | **Normal sensitivity** | General fire detection comparable to spot detectors |

Most installed systems are Class A or B. **Specify the class** you want. One detector can provide several levels: for example an **initial very early alarm** for investigation (Class A), a **second alarm** for urgent response, and a **third (Class C)** for evacuation or to release suppression.

### US classification (NFPA 76)

| Level | Description |
| --- | --- |
| **VEWFD** (very early warning fire detection) | Aspirating-type detection, for larger telecom equipment areas, and widely applied in data centres |
| **EWFD** (early warning fire detection) | Intermediate |
| **SFD** (standard fire detection) | Ordinary smoke detection per NFPA 72 |

### Alarm levels

Typical multi-level thresholds are **Alert, Action, Fire 1 and Fire 2** (names vary). Each level drives a staged response, from investigation by staff to an automatic release.

### Design rules **[CHECK]**

| Rule | Detail |
| --- | --- |
| **Coverage per sampling hole** | At most about **37 m² (400 ft²)** per hole. With two levels of protection (for example floor and ceiling), the overall coverage between high and low holes is at most about **18.6 m² (200 ft²)** |
| **Hole sensitivity** | For VEWFD the minimum alert sensitivity at a single hole is at most about **0.2%/ft** obscuration and the alarm sensitivity at most about **1.0%/ft** |
| **Where to sample** | The **room volume**, **return air paths and CRAC intakes** (where the smoke goes), **under the raised floor**, **above suspended ceilings**, **inside or on top of critical cabinets**, **battery, electrical and UPS rooms** |
| **Pipe design** | Fixed pipe layout and a **transport time** (smoke reaches the detector within a limited time). Use design software, and commission with smoke tests |
| **Airflow** | High airflow dilutes smoke, so detection is designed with airflow in mind, with all cooling units running during tests |
| **Monitoring** | The ASD, its fan, airflow and power supply are supervised |

### Worked example: the additive effect and hole count

A hall of **4,000 ft² (371.6 m²)** with **400 ft² per hole** and an ASD **Fire level 1 sensitivity of 0.25%/ft**:

```
Holes = 4,000 / 400 = 10 sampling holes
Equivalent single-hole sensitivity = 0.25 × 10 = 2.5%/ft
```

The system as a whole is **sensitive to 0.25%/ft**, even though each hole would need 2.5%/ft on its own. A traditional spot system at 900 ft² (83.6 m²) per detector would need:

```
4,000 / 900 = 4.4, so 5 spot detectors, each reacting at much higher smoke levels
```

## 3.4 The fire alarm system

```
Detectors and call points ──► FACP (fire alarm control panel) ──► notification (sounders, strobes, voice)
                                          │──► releasing panel ──► suppression
                                          │──► interfaces: HVAC and dampers, doors, EPO, lifts, BMS
                                          └──► transmission to a constantly attended location / alarm receiving centre
```

| Element | Notes |
| --- | --- |
| **Fire alarm control panel (FACP)** | The brain: EN 54-2 and NFPA 72. **Addressable** panels identify each device. The FACP gives the building's **life safety notification** |
| **Releasing panel** | Controls the release of a suppression system. Linked to, but separate from, the FACP |
| **Zoning** | The protected area is divided into zones so the fire can be located |
| **Cross-zoning (coincidence)** | **Two detectors in different zones (or two thresholds)** must agree before a suppression system is released. It prevents a false release from a single detector |
| **Interfaces** | HVAC shutdown, fire and smoke dampers, door release, elevator recall, power disconnect, BMS, access control |
| **Supervision** | The panel monitors wiring, devices and power supplies for faults |
| **Power supply** | Battery backup for **24 hours of standby plus 5 minutes of alarm** is the usual NFPA 72 basis **[CHECK]**. EN 54-4 for supplies |
| **Transmission** | Alarms go to a **constantly attended location** or an approved alarm receiving centre |

### Worked example: battery sizing

A panel draws **0.5 A** in standby and **3 A** in alarm. Required: **24 h standby + 5 min alarm**, with a **25% margin** (illustrative):

```
Standby   = 0.5 A × 24 h       = 12.0 Ah
Alarm     = 3 A × (5/60) h     = 0.25 Ah
Total     = 12.25 Ah           × 1.25 = about 15.3 Ah battery
```

## 3.5 Where to detect what

| Space | Typical detection |
| --- | --- |
| **Data hall (room)** | **ASD** (very early warning) plus spot smoke detectors, cross-zoned for gas release |
| **Under the raised floor** | ASD or spot detectors (as a separate zone) |
| **Ceiling void or plenum** | Spot or ASD |
| **Return air path and CRAC intakes** | ASD sampling points |
| **In-rack or in-cabinet** | ASD sampling or in-cabinet detection for dense or critical racks |
| **UPS and battery rooms** | ASD, **off-gas detection** for lithium-ion, hydrogen detection for lead-acid, heat detection |
| **Electrical rooms and switchgear** | ASD or spot detectors, thermography for hot connections (6.47) |
| **Generator hall and fuel areas** | Heat and flame detection, plus gas detection |
| **Cable vaults and trays** | Linear heat cable, ASD |
| **Offices and corridors** | Standard smoke detection and manual call points |
| **Entrance room and meet-me rooms** | As the data hall |

## 3.6 Testing and maintenance **[CHECK]**

| Activity | Frequency |
| --- | --- |
| **Visual and weekly checks** | Panel shows normal, no faults |
| **Detection system service** | **Every 6 months** per BS 5839-1 (a competent person), and **three-monthly** is recommended for data centres. NFPA 72 sets inspection and testing intervals, with an annual functional test of detectors |
| **ASD** | Annual smoke test of transport time and sensitivity, filter change, airflow check |
| **Records** | Keep logs of tests, faults and false alarms |
| **False alarms** | Investigate and fix the cause (dust, contamination, steam, airflow) |

---

# 12.4 Water-based systems

## 4.1 Role of water in a data centre

NFPA 75 requires the IT area to be protected by **automatic sprinklers or a gaseous system (or both)**, and requires it in a **fully sprinklered building**. In practice most data halls use a **pre-action sprinkler system**, a **clean agent system**, or both. Many insurers and authorities require sprinklers even where gas is installed. Gas **supplements** sprinklers, it does not necessarily replace them.

| | **Water (sprinklers)** | **Gas (clean agent)** |
| --- | --- | --- |
| **Action** | Cools and **controls** the fire | **Extinguishes** quickly in a closed room |
| **Residue and damage** | Water damage | No residue (in intended use) |
| **Life safety** | Safe for occupants | Needs pre-discharge alarm, delay and care |
| **Reliance on the room** | Works without an airtight room | Needs an **airtight enclosure** |
| **Repeat protection** | Continues while it flows | One shot (until recharged) |
| **Cost and upkeep** | Lower agent cost | Agent, cylinders and enclosure testing |
| **Required by codes** | Commonly required | Often an addition |

## 4.2 Sprinkler heads

A closed **automatic sprinkler** has a **glass bulb or fusible link** that breaks at a set temperature. **Each head opens individually** over the fire: only the heads near the heat discharge.

| Feature | Detail |
| --- | --- |
| **Temperature rating** | Chosen from NFPA 13 from the **maximum expected ceiling temperature**. Typical glass-bulb colours: **orange 57 °C**, **red 68 °C** (the common choice), **yellow 79 °C**, **green 93 °C**, **blue 141 °C** **[CHECK]** |
| **Response** | **Quick response** (fast bulb, RTI at or below 50 (m·s)½) or **standard response**. Quick response is required in light hazard wet systems, not mandated in dry and pre-action systems. Don't mix types in one compartment |
| **K-factor** | The head's size: **Q = K × √P** (flow in gpm, pressure in psi). A common head has **K = 5.6** (80 in metric units) |
| **Coverage** | A maximum area per head by hazard (for example about 130 ft², 12 m², for ordinary hazard) |
| **Orientation** | Upright or pendent, concealed or exposed |

## 4.3 Types of sprinkler system

| System | Pipe contents | How it operates | Typical use |
| --- | --- | --- | --- |
| **Wet pipe** | **Water** | A head opens, water flows immediately | The commonest, fastest. Heated spaces. Offices, corridors. Risk: leak or damage discharges water at once |
| **Dry pipe** | **Air or nitrogen** under pressure | A head opens, pressure drops, the valve opens, water flows. Water must reach the farthest head in about **60 seconds** (max about 750 gal / 2,840 L without an accelerator). Annual trip test | Unheated or freezing areas |
| **Pre-action** | **Air or nitrogen (or empty)**, supervised | **Detection** must open the valve first, **and** a head must open to discharge (see below) | **Data centres**, archives, telecom rooms: where accidental discharge would be costly |
| **Deluge** | Dry, with **open** heads | A detection signal opens the valve and water flows from **all** heads | High-hazard areas (hangars, flammable liquids, transformers), not data halls |
| **Water mist** | Water at high pressure with fine nozzles | See 4.6 | Specialised, low-water alternative (NFPA 750) |

### Pre-action systems

The pipework is **normally dry**, so a damaged head or a pipe leak **does not** pour water onto servers.

| Variant | Operation |
| --- | --- |
| **Non-interlock** | Water enters the pipe on **either** detection **or** a head opening |
| **Single interlock** | **Detection** opens the valve and fills the pipes with water. **A head must then fuse** before water is discharged. A head opening alone does nothing, and detection alone does not discharge. **The most common in IT rooms** |
| **Double interlock** | **Both** detection **and** a head opening (loss of supervisory air pressure) are required before water enters the pipes. Used where even filling the pipes is unacceptable (freezers). Most protection against accidental discharge, but **slower** |

Key points:

- Detection usually requires **two detectors on separate circuits** to agree (cross-zoning) before the release solenoid operates.
- Pipes are kept at **supervisory pressure** by a compressor or nitrogen generator. Low pressure signals a leak. The minimum supervisory pressure for single interlock systems is low (about 0.5 bar / 7 psi), higher for double interlock and non-interlock. Pipes and detection must be **supervised** where there are more than 20 sprinklers.
- NFPA 13 allows **no more than 1,000 sprinklers** per single-interlock or non-interlock valve. For **double interlock**, water must reach the test connection within **60 seconds**.
- Pre-action is a **property protection** system, **not** a life safety system: occupant notification comes from the building's fire alarm panel.
- Dry and double-interlock pre-action systems need about **30% more design area** (a larger area of heads assumed to open), because water arrives later.

## 4.4 Design basis

NFPA 13 sizes the system from the **hazard classification**, a **design density** (litres per minute per m² or gpm per ft²) applied over a **design area**, plus a **hose allowance**, for a set **duration**.

| Hazard | Design density | Design area | Typical duration **[CHECK]** |
| --- | --- | --- | --- |
| Light | 0.10 gpm/ft² (4.1 L/min per m²) | 1,500 ft² (139 m²) | 30 minutes |
| **Ordinary Group 1** | **0.15 gpm/ft² (6.1 L/min per m²)** | 1,500 ft² | **60 minutes** |
| Ordinary Group 2 | 0.20 gpm/ft² | 1,500 ft² | 60 minutes |
| Extra Group 1 | 0.30 gpm/ft² | 2,500 ft² | 90 to 120 minutes |
| Extra Group 2 | 0.40 gpm/ft² | 2,500 ft² | 90 to 120 minutes |

The designer and the AHJ decide the hazard class. **Under a raised floor** the void needs sprinkler or gas protection unless it is non-combustible and shallow (commonly under about 300 mm) **[CHECK]**, and many data centres combine overhead pre-action sprinklers with an **inert gas** system under the floor.

### Worked example: water demand for a data hall (ordinary group 1)

```
Demand = 0.15 gpm/ft² × 1,500 ft² = 225 gpm = 852 L/min
Pre-action (+30% design area): 0.15 × 1,950 = 292.5 gpm = 1,107 L/min
Volume for 60 minutes: 1,107 × 60 = 66,400 L = about 66 m³ (before any hose allowance)
```

### Worked example: heads and pressure

```
Heads in the design area = 1,500 ft² / 130 ft² = 11.5, so 12 heads
Flow per head = 225 / 12 = 18.75 gpm
Pressure at a K = 5.6 head: P = (Q/K)² = (18.75 / 5.6)² = 11.2 psi (0.77 bar)
```

The fire water comes from the mains or from **storage and a fire pump**. The **fire reserve is separate from the cooling reserve** (10.2 in `10_water_supply.md`), and tanks follow NFPA 22.

## 4.5 Limiting water damage

| Measure | Detail |
| --- | --- |
| **Pre-action rather than wet pipe** | The main safeguard against accidental discharge |
| **Drainage** | The structural floor must allow **removal of water** from sprinklers or fire fighting (NFPA 75) |
| **Zoning and quick isolation** | Isolate the discharging zone and the water supply |
| **Power disconnection** | Power to the affected zone is cut |
| **Protect equipment** | Covers and rack tops where permitted |
| **Prompt recovery** | NFPA 75 Annex B (first 24 hours for damaged electronics): dry, clean and test equipment quickly |

## 4.6 Water mist

**Water mist** uses very fine droplets at high pressure. It cools the fire, displaces oxygen as the droplets turn to steam, and blocks radiant heat, using **far less water** than sprinklers.

| Point | Detail |
| --- | --- |
| **Standard** | **NFPA 750** (water mist is not a sprinkler system under NFPA 13). NFPA 75 (2024) includes a water mist provision |
| **Pros** | Little water, less water damage, no residue chemicals |
| **Cons** | High pressure pumps and fine nozzles, a specialised design, listing tied to the hazard, and **not accepted as primary protection for lithium-ion batteries in server racks** by FM Global Data Sheet 5-32 **[CHECK]** |

## 4.7 Maintenance (NFPA 25 and EN 12845) **[CHECK]**

- **Monthly**: gauges, valves and enclosure visual checks.
- **Quarterly**: supervisory and alarm devices, pilot detection loops.
- **Semi-annual**: low-air alarms.
- **Annual**: **trip-test the pre-action and dry valves**, flow tests.
- Keep **spare sprinklers** on site and use an approved contractor.
- **Any change** (containment, new racks, ceiling changes) needs a fire protection review (9.13).

---

# 12.5 Gas based fire suppression systems I: agents

## 5.1 How gas systems protect

A **total flooding** system discharges enough gas to fill the **whole enclosed room** at the **design concentration**, extinguishing a fire anywhere in it, and holds it for the **hold time** (at least **10 minutes**) while heat dissipates.

Gas agents extinguish in three ways:

| Mechanism | Agents |
| --- | --- |
| **Absorb heat** (cool the flame) | Halocarbons (FK-5-1-12, HFC-227ea) |
| **Reduce oxygen** (dilute below the combustion limit, typically to about 12 to 15% O₂) | Inert gases (IG-541, IG-55, IG-100, IG-01) |
| **Interrupt the chemical chain** | Some halocarbons and the old halons |

**A clean agent** (NFPA 2001) is **non-conducting, volatile or gaseous, and leaves no residue**. After discharge and ventilation, the room can return to service. CO₂ is covered by a separate standard (NFPA 12) and is **not permitted in normally occupied spaces** at suppression concentrations.

## 5.2 The agents

| Family | Agent (generic name) | Composition and notes |
| --- | --- | --- |
| **Halocarbon** | **FK-5-1-12** (a fluoroketone, the generic of the former "Novec 1230") | Lowest global warming potential of the halocarbons |
| | **HFC-227ea** ("FM-200") | The most widely installed halocarbon for decades |
| | HFC-125, HFC-23 | Specialised uses |
| **Inert gas** | **IG-541** ("Inergen") | Nitrogen 52%, argon 40%, carbon dioxide 8% |
| | **IG-55** ("Argonite") | Nitrogen 50%, argon 50% |
| | **IG-100** | Pure nitrogen |
| | **IG-01** | Pure argon |
| **Carbon dioxide** | CO₂ (NFPA 12) | Unoccupied hazards only: lethal at suppression concentrations |
| **Halon 1301** | Bromotrifluoromethane | **Phased out under the Montreal Protocol** because it damages the ozone layer. Existing systems are being replaced |

Agents are named by their **generic designation**, not by brand.

### Comparison **[CHECK]**

| Property | **FK-5-1-12** | **HFC-227ea** | **IG-541** |
| --- | --- | --- | --- |
| **Class A design concentration** (informative, at 21 °C) | **4.5%** | **6.7%** | **34.2%** |
| **Agent per m³ of room** (at 21 °C) | 0.653 kg | 0.523 kg | 0.419 m³ of free gas (0.591 kg) |
| **Occupancy limit** | NOAEL **10.0%** | NOAEL **9.0%** (LOAEL 10.5%) | Oxygen must stay at or above about **12%** (agent up to 43%) |
| **Discharge time** | **10 s** (to 95%) | **10 s** | **60 s** (Class B), **120 s** (Class A and C) in the 2025 edition |
| **Storage** | Liquid, pressurised with nitrogen (a few cylinders) | Liquid, pressurised with nitrogen | **Gas at 200 to 300 bar**, a **bank of many cylinders** |
| **Space needed** | Small | Small | **Large** |
| **GWP** | **Under 1** | **3,350** (NFPA 2001 Annex A) | **0** |
| **Ozone depletion** | 0 | 0 | 0 |
| **Decomposition products** | Hydrogen fluoride on hot surfaces | Hydrogen fluoride on hot surfaces | **None** |
| **Noise** | Lower | Lower | **Loud (about 140 dB)**: needs acoustic nozzles |
| **Regulatory outlook** | Generic supply remains, PFAS debate | **HFC phase-down** (cost, supply) | No restriction |

## 5.3 Calculating the quantity

### Halocarbons

```
W = (V / s) × ( C / (100 − C) )
   W = agent mass (kg)    V = room volume (m³)    C = design concentration (% by volume)
   s = specific vapour volume of the agent (m³/kg) = k1 + k2 × T (T in °C)
```

At 21 °C: **s ≈ 0.1374 m³/kg for HFC-227ea** and **≈ 0.0722 m³/kg for FK-5-1-12** **[CHECK]**.

### Inert gases

```
X = ln( 100 / (100 − C) )         (volume of free gas per m³ of room)
Residual oxygen = 20.9% × (100 − C) / 100
```

### Worked example: a 500 m³ room

| Agent | Calculation | Quantity |
| --- | --- | --- |
| **HFC-227ea at 6.7%** | W/V = 6.7 / (93.3 × 0.1374) = 0.523 kg/m³, so 0.523 × 500 | **261.5 kg** |
| **FK-5-1-12 at 4.5%** | 4.5 / (95.5 × 0.0722) = 0.653 kg/m³, so 0.653 × 500 | **326.5 kg** |
| **IG-541 at 34.2%** | X = ln(100 / 65.8) = 0.419 m³/m³, so 0.419 × 500 | **209.5 m³** of free gas |

**Oxygen after an IG-541 discharge at 34.2%:** 20.9 × (100 − 34.2) / 100 = **13.8%**. At 43%: 20.9 × 0.57 = **11.9%** (the lower limit of the standard occupied band).

**Design temperature:** use the **lowest expected room temperature**, because a colder agent is denser and the same concentration needs more mass. Also **correct for altitude** (for example a factor of 0.82 at about 1,520 m for the quantity) and add for **leakage and non-closable openings**.

## 5.4 Safety limits for people

| Agent type | Limit |
| --- | --- |
| **Halocarbons** | **NOAEL** (no observed adverse effect level) and **LOAEL** (lowest observed adverse effect level) define the limits. Normally occupied spaces may be designed **up to the NOAEL**. Exposure **never longer than 5 minutes**, with pre-discharge alarm and delay |
| **Inert gases** | Limited by **oxygen**: above about 12% O₂ (up to 43% agent) a **5-minute** exposure is allowed. **43 to 52% agent: 3 minutes. 52 to 62%: only normally unoccupied spaces, under 30 seconds.** Above 62%: no exposure |
| **All** | **Unprotected people must not enter** during or after discharge. **Ventilate** before re-entry (halocarbon decomposition gives hydrogen fluoride on contact with hot surfaces, above about 480 °C) |
| **CO₂** | **Not used in normally occupied spaces** |

## 5.5 Environmental and regulatory issues **[CHECK]**

| Issue | Detail |
| --- | --- |
| **Halon** | Phased out under the **Montreal Protocol** (ozone depletion) |
| **HFC agents** | The US **AIM Act** steps HFC production and consumption down towards an **85% reduction by 2036**, and the EU **F-gas Regulation (EU) 2024/573** phases HFCs down. Existing HFC-227ea systems remain legal and recycled agent is expected to stay available, but **cost and supply** push new systems towards FK-5-1-12 or inert gas |
| **PFAS** | FK-5-1-12 is a fluorinated compound within broad PFAS definitions. A major manufacturer left PFAS chemicals in 2025, but generic FK-5-1-12 remains available |
| **Inert gases** | No GWP, no ODP, no phase-down |
| **Discharge tests** | Avoid unnecessary discharges of agents with a GWP |

## 5.6 Choosing an agent

| Factor | Favours halocarbon | Favours inert gas |
| --- | --- | --- |
| **Space for storage** | Limited | Plenty (cylinder bank, distance from room) |
| **Room size** | Small and medium | **Large rooms** (above roughly 280 m³, 10,000 ft³, inert gas becomes cost-preferred) |
| **Environmental objectives** | FK-5-1-12 has a low GWP | **Zero GWP and no PFAS** |
| **Discharge speed** | 10 seconds | 60 to 120 seconds |
| **Noise sensitivity (spinning disks)** | Lower noise | Needs acoustic nozzles |
| **Pressure relief** | Small | **Large vent area** (adds a large gas volume) |
| **Low-temperature storage** | Standard | Gas stays gaseous |
| **Under-floor only protection** | | Often chosen for voids |

**Noise:** inert gas discharge at about **140 dB** can damage **spinning hard disk drives**. Acoustic nozzles keep the level below about 110 dB (FM Global Data Sheet 5-32). **SSDs are not affected** **[CHECK]**.

---

# 12.6 Gas based fire suppression systems II: system design and operation

## 6.1 The components

```
 Detectors (cross-zoned) ──► Releasing control panel ──► pilot / actuator ──► cylinder valves
                                   │                                              │
                       alarms, abort, manual release                  manifold ─► pipework ─► nozzles in the room
                                   └─► HVAC shutdown, dampers, doors, power disconnect, signals to the FACP
```

| Component | Function |
| --- | --- |
| **Storage cylinders** | Hold the agent (halocarbon as liquid under nitrogen pressure, inert gas as high-pressure gas). Fitted with pressure gauges or monitoring |
| **Cylinder valves and actuators** | Electric, pneumatic or manual release |
| **Manifold and discharge pipework** | Distribute the agent. Sized by **flow calculation** so every nozzle delivers the right amount in the right time |
| **Nozzles** | Spread the agent through the room (180° or 360°). Acoustic nozzles for inert gas near spinning disks |
| **Releasing control panel** | Receives detection, runs the **countdown**, controls the release and the interfaces. Supervised and on backup power |
| **Detectors** | **Cross-zoned** (two detectors or two thresholds must agree before release) |
| **Pre-discharge alarms** | Sounders and beacons in the protected room, continuing until acknowledged |
| **Abort switch** | Lets staff **delay** the release during the countdown (below) |
| **Manual release station** | A deliberate manual release, usually at the exits. **It must never be defeated by the abort** |
| **Lockout valve and service switch** | Prevent discharge during maintenance |
| **Discharge indicators and warning signs** | A pressure switch shows that the system has discharged. Lamps and signs at each entrance (12.10) |
| **Pressure relief vents** | Relieve the overpressure of discharge, especially for inert gas |
| **HVAC dampers and shutdown** | Close the room so the agent is held (6.4) |

## 6.2 Operating sequence

| Step | What happens |
| --- | --- |
| **1. Early warning** | An ASD alert or the **first detector** raises an alarm and alerts staff to investigate |
| **2. Confirmed fire** | The **second detector** (or second threshold) activates. The control panel starts the **pre-discharge sequence** |
| **3. Pre-discharge** | Alarms and strobes in the room. **HVAC shuts down, dampers close**, doors may release, **power to the protected equipment is disconnected** (NFPA 75, unless the risk assessment says otherwise). A **countdown (commonly 30 to 60 seconds)** lets people leave |
| **4. Abort (if provided)** | Held pressed by a person, it **delays** the release (for example if a person is trapped or a false alarm). It is located near the egress **inside** the hazard. It **never defeats the manual release** |
| **5. Discharge** | **Halocarbons: 95% of design concentration within 10 seconds. Inert gas: 60 to 120 seconds** (see 5.2) |
| **6. Hold** | The concentration is **held for at least 10 minutes** while the fire is extinguished and hot surfaces cool |
| **7. Alarm and response** | Transmission to the constantly attended location and the fire service. No one enters until the room is ventilated and declared safe |
| **8. Recovery** | **Ventilate**, investigate, recharge or replace the cylinders, restore the system |

## 6.3 Abort, lockout and manual release

| Device | Rule |
| --- | --- |
| **Pre-discharge alarm and delay** | Required in occupied spaces. The delay may be omitted only for hazards that grow too fast to wait |
| **Abort switch** | Needs **constant pressure** to hold off the discharge, is located near the exit **inside** the hazard, and **does not stop the manual release** |
| **Manual release** | At the exit or by the system, protected against accidental operation |
| **Lockout valve** | A **manually operated valve in the discharge pipe**, locked **closed** during maintenance. Its position is monitored and gives a **trouble signal**. **It must be returned to the open position**, a common cause of failed systems |
| **Warning lamps and signs** | At each entrance: "system active", "do not enter" (12.10) |

## 6.4 The enclosure: why the room matters

A gas system only works if the **room holds the agent**. The enclosure is part of the system.

| Requirement | Detail |
| --- | --- |
| **Hold time** | Retain the agent at **at least 85% of the design concentration for at least 10 minutes** (to the top of the protected height) |
| **Door fan (room integrity) test** | A calibrated blower in the doorway pressurises or depressurises the room, and the leakage (**equivalent leakage area**) is measured to **predict the hold time**. Done at **acceptance** and **after any change** to the room, and the room is also inspected visually at least annually |
| **Sealing** | **Slab-to-slab walls**, sealed penetrations and cable entries, dampers that close, doors with seals and closers. A raised floor void and a ceiling void are **part of the volume** and must be protected or sealed |
| **Pressure relief venting** | Discharge adds pressure (especially inert gas, which adds a large gas volume), and cooling afterwards creates a vacuum. Vents prevent damage to walls and doors and close when not needed |
| **Ventilation shut-off** | Fans stop and dampers close at pre-discharge. If critical ventilation must run, the standard allows an **extended discharge** |
| **Enclosure strength** | Walls, ceilings and doors must withstand the pressure |

### Worked example: the concentration that must be held

| Agent | Design concentration | 85% to be held for 10 minutes |
| --- | --- | --- |
| HFC-227ea | 6.7% | **5.7%** |
| FK-5-1-12 | 4.5% | **3.8%** |
| IG-541 | 34.2% | **29.1%** |

**Any new penetration, new duct, door propped open or change of room size** can break the hold time. That is why a **change control** link to the fire protection review is essential.

## 6.5 Interfaces and their trade-offs

| Interface | Why | Trade-off |
| --- | --- | --- |
| **HVAC shutdown and dampers** | So the agent is not blown out and the fire is not fed | **Cooling stops**: temperatures rise quickly (Module 9). Plan for it, and power is usually cut anyway |
| **Power disconnection** | Removes ignition sources and is required by NFPA 75 unless the risk assessment calls for continuous power | Equipment goes down, so the system is designed so a **true fire** triggers it, not a false alarm |
| **Door release** | Allows escape and fire service access | Security design must **fail safe** at the exits |
| **Alarm transmission** | Calls the fire service | Must be monitored |

## 6.6 Maintenance and testing **[CHECK]**

| Activity | Frequency and rule |
| --- | --- |
| **Visual checks** | Regular visual inspection by staff |
| **Semi-annual inspection** | For **halocarbon** containers, **refill or replace if the agent quantity loss exceeds 5% or the pressure loss (adjusted for temperature) exceeds 10%**. Inert gas is checked by pressure |
| **Annual** | Functional test of detection and release (without discharging), nozzle and pipework inspection, **enclosure inspection**, door fan test where needed |
| **Cylinders** | Hydrostatic test at the interval set by the pressure vessel rules (commonly 10 to 12 years) |
| **Records** | Keep all inspection and test records |
| **Reserve and recharge** | A discharged system is **out of service** until recharged, which can take days to weeks. Plan the spare agent and the supplier's lead time, or fit a **reserve bank** for the highest-availability rooms |

## 6.7 Common problems

| Problem | Cause and cure |
| --- | --- |
| **Accidental discharge** | A false detection, a maintenance error (lockout valve left open), or a mechanical knock. Uptime has found accidental discharges, especially of high-pressure clean agent, to have caused more disruption than fires. Cure: **cross-zoning, staged ASD thresholds, lockout procedures, trained staff, acoustic control** |
| **Failure to hold** | New openings, dampers not closing, doors open. Cure: integrity tests and change control |
| **Noise damage** | Inert gas at about 140 dB can damage spinning disks. Cure: acoustic nozzles |
| **Lockout valve left closed** | The system silently cannot discharge. Cure: monitoring and procedures |
| **Insufficient agent** | After the room changes, or the temperature falls below the design value |

---

# 12.7 Hypoxic air fire prevention

## 7.1 The concept

**Hypoxic air fire prevention** (also called an **oxygen reduction system, ORS**) keeps the protected room **permanently** at a reduced oxygen level, so that **fires cannot start or spread easily**. It **prevents** rather than **extinguishes**: sprinklers and gas react after the fire has begun.

| Feature | Detail |
| --- | --- |
| **Oxygen level** | Typically **15% to 17%** (the range used is about 13% to 17%, set by the fuels in the room), compared with **20.9%** in air |
| **How** | A **nitrogen generator** continuously injects nitrogen-enriched air, so the room stays at the set point |
| **Atmosphere** | **Normobaric hypoxia**: normal air pressure, less oxygen (the same oxygen pressure as at altitude) |
| **Effect on fire** | Raises the **ignition energy** and slows combustion. FM Global notes ORS are designed to **limit fire growth and spread**, and **cannot prevent ignition** in every case |
| **Standards** | **EN 16750** (2017, with amendment 2020), **ISO 20338** (2019), **VdS 3527**, **FM Global Data Sheet 4-13**, BSI PAS 95 |

## 7.2 Equipment and design

| Element | Detail |
| --- | --- |
| **Nitrogen generator** | **Membrane**, **pressure swing adsorption (PSA)** or **vacuum swing adsorption (VSA)** (VSA often uses the least energy). Separated oxygen is vented outside |
| **Oxygen sensors** | **Redundant**, in the room, controlling the injection and alarming |
| **Control system** | Holds the set point, logs data, interfaces with the fire alarm and BMS |
| **Airtight enclosure** | The room must be **tight**, otherwise fresh air leaks in and the generator works constantly. Tested like a gas room (NFPA 2001, ISO 14520, EN 15004) |
| **Detection** | **Smoke detection is still required**: hypoxic air does not stop smouldering or pyrolysis |
| **Design oxygen level** | From **ignition tests** or tables for the actual materials. FM uses the **limiting oxygen concentration for fire propagation (LOCFP) minus the measurement error**. FM research found 11.1% to 13% for warehouse commodities, so practical designs use higher levels where people work |
| **Resilience** | The room should keep the oxygen level for about **12 hours** with the generator off, or the generators need **backup power** (FM guidance) |
| **Construction** | Non-combustible or Class 1 construction for the enclosure (FM) |

### Worked example: what 15% oxygen means

**Equivalent altitude.** The oxygen partial pressure at sea level (101.3 kPa) with 15% oxygen:

```
pO₂ = 0.15 × 101.3 = 15.2 kPa
Same pressure of oxygen at altitude (air is 20.9% O₂): total pressure = 15.2 / 0.209 = 72.7 kPa
72.7 kPa corresponds to an altitude of about 2,700 m
```

At **13%** oxygen, the equivalent altitude is about **3,800 m**.

**Nitrogen to reach 15% in a 500 m³ room (ideal mixing, no leakage):**

```
V_N₂ = V × ln( 20.9 / 15 ) = 500 × 0.332 = about 166 m³ of nitrogen
(about 28% of the room's volume is effectively replaced)
```

Leakage then needs **continuous** nitrogen to hold the level, which is why the room must be airtight.

## 7.3 People and health

| Topic | Detail |
| --- | --- |
| **Medical evidence** | Studies conclude that **14.8 to 17%** oxygen is not a hypoxia risk for healthy people, and working at a **minimum of 13%** at normal pressure is not a hazard **if precautions are observed**: medical examinations and limited exposure time |
| **Reduced capacity** | The ability for strenuous work falls as oxygen falls |
| **US rule** | OSHA treats less than **19.5%** oxygen as **oxygen-deficient**, so entry needs a **respiratory protection programme**, not a time-at-altitude permission |
| **Europe** | National rules and EN 16750 require **medical screening, training, exposure limits, signage and controlled entry** |
| **Operating rules** | Entry procedures, oxygen monitoring and alarms, restricted access (people with heart or lung conditions, pregnancy), lone working restrictions, rescue procedures |

## 7.4 Advantages and limits

| Advantages | Limits |
| --- | --- |
| **No discharge event**, no agent, no water, no post-fire cleanup of an agent | **Does not stop smouldering or pyrolysis**, so detection is still needed |
| Continuous protection, even before detection | **Does not stop a lithium cell in thermal runaway**: the reaction continues without ambient oxygen, so battery fire controls remain mandatory |
| Can protect large volumes where sprinklers are hard or the contents are water-sensitive | **Continuous operating energy** (nitrogen generation) raises PUE and costs |
| | Needs an **airtight room** and reliable generators, power and sensors |
| | **Occupational health requirements** for people entering |
| | **Insurer and authority acceptance** varies. One UK insurer's data centre guidance states hypoxic systems are **not normally recommended for data halls** and should be discussed with the insurer and broker **[CHECK]** |
| | Entry doors opening disturb the atmosphere |

## 7.5 Where it is used

Cold storage and warehouses, archives, automated storage, special high-value or water-sensitive rooms. It is **rare in data halls**, where the usual choices remain **detection plus pre-action sprinklers and/or clean agent**.

## 7.6 Prevention versus suppression

| | **Oxygen reduction (prevent)** | **Clean agent (suppress)** | **Pre-action sprinklers (control)** |
| --- | --- | --- | --- |
| **Acts** | Continuously | After detection | After detection and heat |
| **People in the room** | Allowed with health controls | Evacuate before discharge | Allowed |
| **Collateral** | None | Agent, noise, pressure | Water |
| **Needs an airtight room** | Yes | Yes | No |
| **Operating cost** | Continuous energy | Mostly standby | Low |
| **Typical data hall use** | Rare | Common | Common |

---

# 12.8 Fire suppression best practices

## 8.1 A layered strategy

No single system fits every room. Combine **prevention, early detection, compartmentation, suppression and response**, and treat **detection and suppression as one coordinated system**, not separate installations.

| Space | Detection | Suppression | Notes |
| --- | --- | --- | --- |
| **Data hall** | ASD plus spot, cross-zoned | **Pre-action sprinklers and/or clean agent** | Containment must not obstruct (9.13). 800 mm cabinets etc. as in Module 8 |
| **Raised floor void** | ASD or spot detection | Protected where it contains combustibles or a critical need. Often **inert gas** under the floor | Cable fire load |
| **Ceiling void** | Detection | Sprinklers or gas as the risk requires | |
| **UPS and battery rooms** | ASD, **off-gas** (lithium-ion), hydrogen (lead-acid) | Sprinklers for lithium-ion (**FM 5-32**), compliance with **NFPA 855** | Separate, fire-rated, spaced cabinets |
| **Electrical rooms and switchgear** | ASD or spot, thermography | Clean agent or CO₂ (unoccupied), sprinklers where required | Most fires begin here |
| **Generator and fuel areas** | Heat and flame detection | Sprinklers, foam or gas for fuel hazards | Fuel containment |
| **Cable vaults and trays** | Linear heat, ASD | Gas, water mist or sprinklers | |
| **Entrance room and meet-me rooms** | As the data hall | As the data hall | NFPA 76 where telecom |
| **Offices, corridors** | Standard smoke detection | Wet sprinklers | |

## 8.2 Design and construction practices

| Practice | Detail |
| --- | --- |
| **Compartmentation** | **1-hour (or more) fire-rated** separation of the IT area, battery rooms, electrical rooms, generator areas. At Tier IV, 1-hour partitions between complementary critical systems |
| **Fire-stop every penetration** | Cable and pipe holes sealed to the same rating. **One unsealed cable hole undoes the rating** |
| **Doors and dampers** | Self-closing rated doors, fire and smoke dampers on ducts through the barrier |
| **Materials** | Class A finishes, no exposed foam plastics, **low-smoke, low-halogen cables** where appropriate (Module 6) |
| **Cable management** | Tidy, not overfilled trays, remove abandoned cable |
| **Aisle containment** | Detection-controlled release of panels or in-aisle protection (9.13) |
| **Battery rooms** | Separate, ventilated, spaced, with their own detection and suppression, off-gas detection for lithium-ion |
| **Hold-time design** | Enclosure designed for gas hold time and pressure relief |
| **Water and drainage** | Floors that drain, so a discharge or leak is removed |

## 8.3 Operational practices

| Practice | Detail |
| --- | --- |
| **Housekeeping and storage** | **No cardboard, packaging or spare parts stored in the data hall.** Unpack in a staging room. Limit combustible storage (NFPA 75) |
| **Hot work permits** | A **real, controlled permit** for welding, cutting and grinding, with a fire watch, not a generic form. Isolate or protect detection during hot work and **restore it afterwards** |
| **Contractor control** | Qualified, supervised contractors. Fire risk is highest during **construction, testing and commissioning** |
| **Energy isolation** | **Complete isolation** (including auxiliary and battery supplies) before work. The NIRS fire followed incomplete isolation |
| **Battery handling** | **Discharge to a low state of charge before moving** (the guideline cited is below 30%), use qualified staff, follow the manufacturer, replace batteries at end of life |
| **Electrical maintenance** | Thermography of connections (6.47), torque checks, cleaning, planned replacement |
| **Dust control** | Clean regularly |
| **Procedures for suppression** | Lockout valves, abort procedures, notification before testing |
| **Training and drills** | Alarm response, extinguishers, evacuation, suppression behaviour |
| **Fire risk assessment** | Documented and reviewed with every change |
| **Change control** | Any change (new racks, containment, new penetrations) goes through a **fire protection review** |
| **Insurer engagement** | Early and ongoing |

## 8.4 Commissioning and testing

- Do an **integrated systems test** at commissioning: detection, releasing logic, HVAC and damper interlocks, power disconnect, alarms, transmission, and the **door fan test**, working together (NFPA 75 and 76 expect it before occupancy).
- Repeat **annual functional tests**, and **after any change**.
- **Record and trend** faults and false alarms.

## 8.5 Preventing false and accidental discharge

| Measure | Why |
| --- | --- |
| **Early warning (ASD) with staged thresholds** | Staff investigate before any suppression |
| **Cross-zoned detection** | Two detectors must agree |
| **Pre-action, not wet pipe, for sprinklers** | A leak or knock does not discharge |
| **Lockout and service procedures** | Maintenance never leaves a live release |
| **Noise control** | Acoustic nozzles for inert gas |
| **Competent maintenance** | Approved contractors |

## 8.6 Emergency and recovery planning

- **Emergency plan** with roles, evacuation, shutdown, and **pre-planning with the fire service** (site plans, hazards, battery rooms, shut-offs).
- **Recovery:** NFPA 75 Annex B gives guidance for the **first 24 hours** for damaged electronic equipment and media (dry, clean, test).
- **Business continuity:** **verified, tested backups and a failover site**. The NIRS fire showed that a fire can destroy data permanently when backups are not verified.

---

# 12.9 Handheld extinguishers

## 9.1 Classes of fire

Fires are classed by the **fuel**, and extinguishers are rated to match. Europe (EN 2) and North America (NFPA 10) differ slightly.

| Europe (EN 2) | North America (NFPA 10) | Fuel | Examples in a data centre |
| --- | --- | --- | --- |
| **Class A** | **Class A** | **Solids** (ordinary combustibles): wood, paper, cloth, plastics | Cardboard, packaging, cable insulation, furniture |
| **Class B** | **Class B** | **Flammable liquids** (and liquefiable solids). In NFPA, also flammable gases | Diesel, oil, solvents |
| **Class C** | **Class C** | EN: **flammable gases**. NFPA: **energised electrical equipment** (the agent must be non-conductive) | Gas supply (EN), live equipment (NFPA) |
| **Class D** | **Class D** | **Combustible metals** (magnesium, sodium, titanium, lithium **metal**) | Rare (laboratories, workshops) |
| **Class F** | **Class K** | **Cooking oils and fats** | Staff kitchens |

Important points:

- **Electrical fires are not a class in EN 2.** Treat them by **de-energising** first (then the fire is Class A or B), and use **non-conductive** agents in the meantime. In NFPA 10, the **C** suffix means the agent is **non-conductive**.
- **Lithium-ion battery fires are not Class D.** Class D covers lithium **metal**. Lithium-ion thermal runaway is controlled by the **NFPA 855** and manufacturer measures, usually by cooling, and **clean agents and CO₂ do not stop it**. An extinguisher helps only for a small external flame, then evacuate **[CHECK]**.

## 9.2 Extinguisher types and their agents

| Agent | Fire classes (typical) | Residue | Notes for a data centre |
| --- | --- | --- | --- |
| **Water** | A | None, but **wets** | **Never on live electrical equipment** |
| **Foam** | A, B | Foam | Not for live equipment. AFFF foams face PFAS restrictions |
| **Dry chemical (ABC, BC)** | A, B, C | **Powder residue (monoammonium phosphate is corrosive and conductive when damp)** | **Not for electronics**: the residue can destroy servers that survived the fire. Acceptable in a generator room |
| **Carbon dioxide (CO₂)** | **B, C** (no Class A) | **None** | **Good for equipment.** Short range (about 1 to 2.4 m). Very cold horn. Displaces oxygen in small rooms: ventilate after use |
| **Clean agent (halocarbon)** | B, C, and **A in larger sizes** (for example 2-A:10-B:C) | **None** | **Good for equipment**, about twice the range of CO₂. Leaves no residue |
| **Wet chemical** | **K (F)**, also A | Liquid | Kitchens only |
| **Water mist** | A, and non-conductive types for electrical | Little | Specialised |
| **Dry powder (Class D)** | D | Powder | Combustible metals only |

### The data centre rule

NFPA 75 and NFPA 10 (2026) steer you to **clean agent or CO₂** extinguishers in IT equipment rooms, **not dry chemical**, because the **residue is corrosive** and **water or foam** would be dangerous on live equipment.

| Location | Suitable portable extinguisher |
| --- | --- |
| **Data hall, entrance room** | **Clean agent (A:B:C) or CO₂** |
| **UPS and electrical rooms** | Clean agent or CO₂ for equipment fires |
| **Generator and plant rooms** | ABC or BC dry chemical, or CO₂ |
| **Offices and corridors** | Water, foam or ABC |
| **Staff kitchen** | **Class K (F) wet chemical** |
| **Workshops with combustible metal** | **Class D** powder |

## 9.3 Ratings and sizing (NFPA 10)

**2-A:10-B:C** is a typical rating, read as:

| Part | Meaning |
| --- | --- |
| **2-A** | Class A rating: equivalent to a certain volume of water. Ratings run **1-A to 40-A** |
| **10-B** | Class B rating: a measure of the fire area (in ft²) a non-expert operator can extinguish. Ratings run **5-B to 640-B** |
| **C** | Class C: **non-conductive agent**. It has **no number** |

| Rule | Value |
| --- | --- |
| **Maximum travel distance, Class A** | **75 ft (22.9 m)** |
| **Maximum travel distance, Class B** | **30 to 50 ft (9.1 to 15.2 m)**, by hazard |
| **Class D** | Within **75 ft (22.9 m)** of the metal hazard |
| **Class K** | Within **30 ft (9.1 m)** of cooking appliances |
| **Hazard level** | Light, ordinary or extra, which sets the minimum rating and the floor area per extinguisher |

**Worked example.** A **4,000 ft² (372 m²)** hall classed as ordinary hazard, with about **1,500 ft²** allowed per 2-A unit:

```
By area:       4,000 / 1,500 = 2.7, so at least 3 extinguishers
By travel:     no point further than 75 ft (22.9 m) from an extinguisher; this often needs more units
```

In practice the **travel distance** usually forces more units than the area calculation.

## 9.4 Placement and mounting

| Rule | Detail |
| --- | --- |
| **Visible and accessible** | Near exits and along escape routes, not blocked by racks or storage |
| **Identified** | An ISO 7010 **F001** sign above or beside each one (12.10) |
| **Mounting height** | Units up to **18 kg (40 lb)**: top no higher than **1.53 m (5 ft)**. Heavier units: no higher than **1.07 m (3.5 ft)** |
| **Protected** | Away from damage and temperature extremes |
| **Data hall** | Near the **exits**, not in the middle of rows |
| **Gas-protected rooms** | Still equipped with portable extinguishers |

## 9.5 Using an extinguisher

**PASS:** **P**ull the pin, **A**im at the **base** of the fire, **S**queeze the handle, **S**weep side to side.

**Fight a fire only if** it is **small**, you have a **clear escape route behind you**, you have the **right extinguisher**, and you are **trained**. A portable discharges for only about **8 to 30 seconds**. Otherwise **evacuate and call the fire service**. In a gas-protected room, do not delay evacuation.

## 9.6 Inspection and maintenance (NFPA 10) **[CHECK]**

| Activity | Frequency |
| --- | --- |
| **Visual inspection** | **Monthly** (location, pressure, seal, damage). The 2026 edition allows **electronic monitoring** to replace the monthly walk-round with authority approval |
| **Maintenance** | **Annually**, by a certified technician (service tag) |
| **Internal examination** | **Every 6 years** for stored-pressure dry chemical and clean agent units (water and wet chemical about every 5 years, foam about every 3 years) |
| **Hydrostatic test** | **5 years** for CO₂, water and wet chemical. **12 years** for dry chemical, clean agent and dry powder |
| **Disposable units** | Retire **12 years** from manufacture, never refill |
| **After use** | Recharge or replace immediately with an extinguisher of at least equal rating |
| **Condemned units** | Remove and replace |

**European marking (EN 3):** the extinguisher body is red with a **colour band** showing the agent: **cream** foam, **blue** powder, **black** CO₂, **green** clean agent, **yellow** wet chemical, none or red for water **[CHECK]**.

---

# 12.10 Signage and safety

## 10.1 The sign system (ISO 7010)

**ISO 7010** (2019, with later amendments) is the international system of safety signs: symbols that mean the same thing in any language. Colours follow **ISO 3864**. In the US, **ANSI Z535** and **NFPA 170** are widely used, and OSHA does not mandate ISO 7010 itself, so both are often used together.

| Category | Colour and shape | Meaning | Examples |
| --- | --- | --- | --- |
| **Prohibition (P)** | Red circle with a slash | Must **not** do | P002 No smoking, P003 No open flame |
| **Warning (W)** | Yellow triangle | **Danger** ahead | W001 General warning, W012 Electricity |
| **Mandatory (M)** | Blue circle | Must **do** | M004 Wear eye protection |
| **Safe condition / escape (E)** | **Green** rectangle or square | Route or equipment that leads to safety | **E001 and E002 Emergency exit (left and right)**, E003 First aid, **E007 Assembly point** |
| **Fire equipment (F)** | **Red** square | Where fire equipment is | **F001 Fire extinguisher**, F002 Fire hose reel, F003 Fire ladder, **F005 Fire alarm call point** |

## 10.2 Escape route signs

| Rule | Detail |
| --- | --- |
| **A continuous chain** | From the room to the assembly point, signs lead the way: overhead signs show the general direction, **a directional arrow at every change of direction** |
| **Illuminated or self-luminous** | Exit signs are **lit whenever the building is occupied**, and must stay visible for at least **90 minutes** after a power failure (battery, generator or photoluminescent material) **[CHECK]** |
| **Photoluminescent signs** | Meet **UL 1994 or ASTM E2072** and need enough ambient light to charge. Some local codes still require internally lit signs with battery backup |
| **High and low** | Low-level signs stay visible when smoke collects at the ceiling |
| **Doors** | "EXIT" on exit doors and "NOT AN EXIT" on doors that might be mistaken for one |
| **Stairwells** | Floor and stair identification and the direction to exit discharge |
| **Unobstructed** | Never blocked by racks, storage or equipment |
| **Emergency lighting** | Keeps routes and signs visible (Module 5, EN 1838 and NFPA 101) |

## 10.3 Fire equipment signs

- **F001** above or beside every extinguisher so its location stays visible over racks and equipment.
- **F005** at manual call points near exits.
- **Sprinkler control valves, risers and pre-action valves** identified by zone, so a firefighter does not shut the wrong valve.
- The **fire alarm panel**, **fire department connection** and **hose** locations.

## 10.4 Data centre specific signs

| Sign or indicator | Purpose |
| --- | --- |
| **Gas extinguishing system warning at every entrance** | Required by NFPA 75 and the gas standards. States that the room is protected by a gas system, **do not enter when the alarm sounds or the warning lamp is lit**, evacuate on the alarm, and that the room must be ventilated after a discharge **[CHECK]** |
| **Status lamps** | "System active", "Discharged, do not enter" outside each entrance |
| **Abort and manual release identification** | At the abort switch and the release station: what they do and how to use them |
| **Lockout valve labels** | The valve position and the rule that it is **locked closed only during maintenance** and must be returned to **open** |
| **Pre-action valve and zone labelling** | Which zone it controls |
| **Oxygen reduction room signs** | "Reduced oxygen atmosphere", entry only for **authorised, medically cleared** persons, with an **oxygen reading displayed outside** |
| **Emergency power-off (EPO) signs** | Labelled and protected against accidental operation (NEC 645.10) |
| **Battery room signs** | Lithium-ion or lead-acid hazard, electrolyte and **electrical shock** warnings, and an **NFPA 704** hazard diamond for stored chemicals |
| **Arc flash and electrical labels** | On switchgear (NFPA 70E) |
| **Containment doors** | Egress and release instructions (Module 9.13) |
| **Emergency contact and assembly point** | Phone numbers, the meeting place |

## 10.5 Evacuation plans

- **Posted floor plans** at each entrance and on routes, in a standard format (ISO 23601), showing "you are here", escape routes, exits, extinguishers, call points, **assembly points** and any gas-protected rooms.
- Plans in the languages of staff and visitors, kept **up to date** after each change.

## 10.6 Means of egress (NFPA 101)

NFPA 101 treats escape as three parts: **exit access** (the path to an exit), **the exit** (a protected route such as an enclosed stair or an exterior door), and **exit discharge** (to a public way).

| Rule | Detail |
| --- | --- |
| **Number of exits** | Normally **at least two** for any occupied floor, with limited exceptions |
| **Travel distance** | A maximum distance from any point to an exit, set by the occupancy and by **sprinkler protection** (longer in sprinklered buildings, commonly in the 200 to 300 ft range) **[CHECK]** |
| **Doors** | Open in the direction of travel when required, with **panic or exit hardware**. **No locked or chained exits** |
| **Access-controlled doors** | Must **release on alarm** and fail so people can leave (delayed-egress and sensor-release locks only where the code conditions are met) |
| **Mantraps and security doors** | Designed so occupants can still exit |
| **Aisles and corridors** | **Kept clear**. A rack aisle is an escape route: no storage or equipment left in it |
| **Gas-protected rooms** | Everyone must be able to leave within the **pre-discharge delay**. Halocarbon concentrations above the LOAEL are allowed only where people can escape within **30 seconds** |
| **Containment and raised floors** | Doors open easily from inside, open tiles and cables are not a trip hazard |

## 10.7 Safety of people

| Measure | Detail |
| --- | --- |
| **Induction** | For staff, visitors and **contractors**: alarms, exits, assembly point, gas room rules |
| **Fire wardens and roles** | Named people with training who check areas and lead evacuation |
| **Drills** | **Regular evacuation drills** (at least yearly) with records **[CHECK]** |
| **Extinguisher training** | PASS technique and when **not** to fight a fire |
| **Gas and oxygen hazards** | Staff know the signs, the delay and what to do if trapped (use the abort or the manual release rules) |
| **Lone working** | Rules for entering gas-protected, battery, hypoxic and electrical rooms |
| **Disabled persons** | Personal emergency evacuation plans and refuge arrangements |
| **First aid and defibrillators** | Equipment and trained staff, marked with E003 |
| **After a discharge or fire** | **Do not re-enter** until the room is ventilated and declared safe. Hydrogen fluoride from halocarbon decomposition is a hazard |
| **No smoking, hot work and storage rules** | Posted and enforced |

---

# 12.11 Regulatory requirements and safety best practices

## 11.1 How the rules fit together

```
Law (fire safety and building regulations) → codes and standards (adopted by reference) → authority having jurisdiction (approval)
   → insurer requirements → owner and customer requirements (Tier, TIA-942, EN 50600, ISO 27001, SLAs)
```

Standards such as NFPA 75 become **mandatory** only when a **law or building code adopts them**, an **AHJ enforces** them, or a **contract or insurer** requires them. The edition adopted locally often lags the newest edition.

| Region | Key instruments **[CHECK]** |
| --- | --- |
| **United States** | **International Building Code and International Fire Code** (adopt NFPA standards by reference), **OSHA 29 CFR 1910** (portable extinguishers 1910.157, fixed extinguishing systems 1910.160 and gaseous systems 1910.162, emergency egress), local fire marshal as AHJ, **EPA** programmes for agents (SNAP) and the **AIM Act** |
| **United Kingdom** | **Regulatory Reform (Fire Safety) Order 2005** (the **responsible person** must carry out a **fire risk assessment** and maintain protection), Building Regulations, **BS 5839-1, BS 5306, BS 7273**, insurer standards (LPCB) |
| **European Union** | National building and fire laws, the **Construction Products Regulation (EU) 305/2011** (CE marking of components such as EN 54 detectors and EN 12094 gas system parts), **F-gas Regulation (EU) 2024/573**, occupational safety directives, pressure equipment rules for cylinders |
| **International** | **ISO 14520, ISO 20338, ISO 7010**, the **Montreal Protocol** (ozone) and **Kigali Amendment** (HFCs) |

## 11.2 What an authority or insurer checks

| Item | Evidence expected |
| --- | --- |
| **Fire risk assessment** | Documented, current, reviewed after changes (NFPA 75, the UK Order) |
| **Compartmentation** | Fire-rated walls and doors, fire-stopped penetrations, dampers |
| **Detection and alarm** | Commissioning certificate, test and service records, transmission to an attended location |
| **Sprinklers** | Installation and acceptance certificates, NFPA 25 or EN 12845 test records, water supply |
| **Gas system** | Commissioning, **door fan test result**, semi-annual and annual records, cylinder test dates |
| **Extinguishers** | Service tags, correct type for the room |
| **Signs and escape** | Exit and emergency lighting tests, evacuation plans |
| **Hot work and contractor permits** | Permit records |
| **Training and drills** | Attendance records |
| **Battery installations** | NFPA 855 compliance, spacing, monitoring, off-gas detection |
| **Change records** | Fire protection review for each change |
| **Fire service pre-plan** | Site plans and hazard information shared |

## 11.3 Environmental regulation of fire protection **[CHECK]**

| Rule | Effect |
| --- | --- |
| **Montreal Protocol** | **Halon** production phased out |
| **AIM Act (US)** | **HFC** production and consumption stepped down towards an **85% reduction by 2036**, affecting HFC-227ea cost and supply |
| **EU F-gas Regulation 2024/573** | Phases HFCs down, with rules for certified personnel and leak control |
| **PFAS restrictions** | Limits on fluorinated firefighting foams, and a debate over fluorinated clean agents |
| **Hazardous materials** | Battery electrolyte, lead and fuel handled under hazardous materials rules |

## 11.4 Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| **Owner or operator (duty holder)** | Legal responsibility for fire safety, the risk assessment, maintenance, records |
| **Designer and installer** | Compliant design, **approved or certified contractors** (for example LPS 1048 sprinkler contractors, certified gas system installers) |
| **Maintainer** | Inspection, testing and maintenance to the standard |
| **Authority having jurisdiction** | Approval and enforcement |
| **Insurer** | Risk assessment and conditions of cover |
| **Fire service** | Response, pre-planning |
| **Staff and contractors** | Follow procedures, report hazards, take part in drills |

## 11.5 Inspection, testing and maintenance calendar **[CHECK]**

| System | Interval and activity |
| --- | --- |
| **Fire alarm and detection** | Daily or weekly panel check. **Service every 6 months** (BS 5839-1, three-monthly recommended for data centres). **Annual** test of devices (NFPA 72). ASD annual smoke test |
| **Sprinklers (NFPA 25)** | Monthly gauges and valves. Quarterly supervisory and pilot loops. Semi-annual low-air alarms. **Annual trip test of pre-action and dry valves** |
| **Gas systems (NFPA 2001)** | **Semi-annual** container inspection (halocarbon: refill if quantity loss exceeds 5% or temperature-adjusted pressure loss exceeds 10%). **Annual** functional test, enclosure inspection, door fan test after changes. Cylinder hydrostatic tests at the regulated interval |
| **Oxygen reduction systems** | Sensor calibration, generator service, tightness checks, per EN 16750 and VdS 3527 |
| **Extinguishers (NFPA 10)** | **Monthly** visual (or electronic monitoring), **annual** maintenance, **6-year** internal exam, **5 or 12-year** hydrostatic test |
| **Exit signs and emergency lighting** | Regular functional tests, with an annual full-duration test **[CHECK]** |
| **Electrical thermography** | Every 12 months (6 months for equipment in poor condition) per NFPA 70B (6.47) |
| **Battery systems** | Per IEEE and manufacturer schedules (6.45) |
| **Evacuation drills and training** | At least yearly |
| **Fire risk assessment** | Reviewed at least yearly and **after every change** |

## 11.6 Equivalency and performance-based design

Both NFPA 75 and the codes allow an **equivalent** or **performance-based** design if it gives at least the same level of protection, with a **design brief, stakeholder agreement and independent review** (NFPA 75 Chapter 5), and **AHJ approval**. The design features must then be **maintained**. Retroactivity: renovations and expansions trigger a **fresh review** of the protection.

## 11.7 Twelve safety best practices

1. Do a **documented fire risk assessment** and review it at every change.
2. **Separate and fire-rate** the IT area, battery rooms and electrical rooms, and **fire-stop every penetration**.
3. **Detect early**: aspirating detection in the room, under the floor and above the ceiling, with off-gas detection for lithium-ion.
4. Use **pre-action sprinklers and/or clean agent**, matched to each room.
5. Make the **enclosure airtight** for gas, and **test it** after every change.
6. **Cross-zone** detection, add staged alarms, and prevent false discharge.
7. Keep **combustibles out** of the hall and control **hot work and contractors**.
8. **Handle batteries safely**: spacing, state of charge, qualified staff, isolation of energy.
9. Fit **clean agent or CO₂ extinguishers** in IT rooms, and train people to use them.
10. **Sign and light** the escape routes, and keep them clear. Never lock exits.
11. **Inspect, test and record** on the calendar. Use approved contractors.
12. **Plan recovery**: verified off-site backups, spares and a plan for damaged electronics.

---

## Glossary

| Term | Meaning |
| --- | --- |
| Fire tetrahedron | Fuel, heat, oxygen and the chain reaction |
| Incipient stage | Early overheating or smouldering, before flame |
| Thermal runaway | Self-heating reaction in a battery cell |
| Off-gas | Vapours given off by a failing lithium-ion cell |
| AHJ | Authority having jurisdiction: the body that approves and enforces |
| ASD | Aspirating smoke detector: air drawn through a pipe network to a sensitive detector |
| VEWFD / EWFD / SFD | Very early warning / early warning / standard fire detection (NFPA 76) |
| EN 54-20 Class A / B / C | Very high / enhanced / normal sensitivity of ASD |
| FACP | Fire alarm control panel |
| Cross-zoning | Two detectors or thresholds must agree before release |
| Wet / dry / pre-action / deluge | Sprinkler system types |
| Single / double interlock | Pre-action logic: detection, or detection and head opening |
| K-factor | Sprinkler size constant: Q = K√P |
| Design density / area | Flow per area (gpm/ft²) over the area assumed to operate |
| Water mist | Very fine water spray at high pressure (NFPA 750) |
| Clean agent | Non-conducting, volatile or gaseous, residue-free extinguishing agent |
| Halocarbon / inert gas | Heat-absorbing agents (FK-5-1-12, HFC-227ea) / oxygen-diluting gases (IG-541 and others) |
| Total flooding | Filling the whole room with agent |
| Design concentration | Agent concentration required to extinguish, with a safety factor |
| NOAEL / LOAEL | Highest no-effect / lowest observed-effect concentration for people |
| Hold time | Time the agent concentration is retained (at least 10 minutes) |
| Door fan test | Measures enclosure leakage to predict hold time |
| Abort switch / lockout valve | Delays a release / locks the discharge closed during maintenance |
| GWP / ODP | Global warming potential / ozone depletion potential |
| ORS | Oxygen reduction system (hypoxic air fire prevention) |
| LOCFP | Limiting oxygen concentration for fire propagation |
| Class A, B, C, D, K (F) | Fire classes by fuel |
| 2-A:10-B:C | Extinguisher rating |
| PASS | Pull, Aim, Squeeze, Sweep |
| ISO 7010 P, W, M, E, F | Prohibition, warning, mandatory, safe condition, fire equipment signs |
| Means of egress | Exit access, exit, exit discharge |
| ITM | Inspection, testing and maintenance |
| Fire risk assessment | Documented analysis that sets the protection level |

## Exam takeaways

**12.1 and 12.2 (causes, standards, requirements)**

- **Fire needs fuel, heat, oxygen and the chain reaction.** **Early detection at the incipient stage** is the most valuable layer. **Smoke and acid gases damage electronics** even without flame.
- **Common causes:** **UPS and batteries (lithium-ion thermal runaway)**, **electrical faults and overload**, switchgear and cabling, **hot work and construction**, combustible storage, dust, human error. **Uptime 2026:** major fires are **increasing**, lithium-ion UPS batteries a clear contributor. **Incidents:** OVHcloud 2021, SK C&C 2022, **NIRS 2025** (batteries at 80% charge, 60 cm from servers, incomplete isolation).
- **NFPA 75 (2024)** for data centres, **NFPA 76** for telecom. Core requirements: **documented risk assessment**, **sprinklered building**, **1-hour separation**, **fire-stopped penetrations**, **smoke detection below the floor, above the ceiling and in the room**, **sprinklers and/or gas**, **clean agent or CO₂ extinguishers**, **warning signs**, **training**, power disconnect on gas discharge. **Tier IV: 1-hour partitions.** Standards bind only when **adopted, enforced or contracted**.

**12.3 and 12.4 (detection and water)**

- **Detectors:** photoelectric, ionisation, multi-criteria, heat, flame, beam, **aspirating (ASD)**, off-gas. **EN 54-20 Class A very high, B enhanced, C normal.** **NFPA 76: VEWFD, EWFD, SFD.** ASD: about **37 m² (400 ft²) per hole**, sensitivity **adds across holes**. **Cross-zoning**. Panel battery: **24 h standby + 5 min alarm**. Service: **BS 5839-1 six-monthly** (three-monthly recommended).
- **Sprinklers:** wet, dry, **pre-action (single or double interlock)**, deluge, water mist (NFPA 750). **Pre-action is the data centre choice.** **Q = K√P.** Ordinary group 1: **0.15 gpm/ft² over 1,500 ft²** (+30% for pre-action). **Red bulb 68 °C.** **NFPA 25: annual trip test.**

**12.5 to 12.7 (gas and oxygen reduction)**

- **Clean agents:** **halocarbons (FK-5-1-12, HFC-227ea)** absorb heat, discharge in **10 s**, small storage. **Inert gases (IG-541, IG-55, IG-100, IG-01)** reduce oxygen, discharge in **60 to 120 s**, many cylinders at 200 to 300 bar, **zero GWP**, **loud (140 dB)**. **Class A design concentrations: FK 4.5%, HFC-227ea 6.7%, IG-541 34.2%.** NOAEL HFC-227ea 9.0%, FK 10.0%. **Exposure at most 5 minutes.** **CO₂ never in occupied spaces.** **Halon phased out. HFC phase-down (85% by 2036).**
- **Quantities:** W = (V/s) × C/(100−C) (halocarbon), X = ln(100/(100−C)) (inert).
- **Operation:** **cross-zoned detection → pre-discharge alarm and 30 to 60 s delay → HVAC shutdown, dampers, power disconnect → discharge → hold 10 minutes → ventilate.** **Abort needs constant pressure and never defeats manual release.** **Lockout valve** locked closed only for maintenance. **Hold time: 85% of design concentration for 10 minutes**, proved by the **door fan test**. **Semi-annual inspection:** refill if halocarbon loss over 5% or pressure loss over 10%.
- **Hypoxic air (ORS):** **prevents** rather than extinguishes, **15 to 17% O₂** (equivalent to about 2,700 m at 15%), nitrogen generator, airtight room, **detection still needed**, **does not stop lithium-ion runaway**, **OSHA: below 19.5% is oxygen-deficient**, **rare in data halls**. **EN 16750, ISO 20338, VdS 3527, FM 4-13.**

**12.8 to 12.11 (practice, extinguishers, signs, regulation)**

- **Best practice:** layered protection, **compartmentation**, **fire-stop**, **no cardboard in the hall**, **real hot work permits**, **energy isolation**, **battery handling at low charge**, **integrated systems test**, **cross-zoning and lockout to prevent false discharge**, **change control**, **recovery planning (NFPA 75 Annex B)**.
- **Fire classes:** **A solids, B liquids, C gases (EN) or energised electrical (NFPA), D metals, F (EN) or K (NFPA) cooking oils.** **Data centre rule: clean agent (A:B:C) or CO₂, not dry chemical** (corrosive residue), **never water or foam on live equipment.** **Travel distance 75 ft (22.9 m) for Class A**, 30 to 50 ft Class B, Class K within 30 ft. **Top of unit at most 1.53 m (18 kg or less).** **Monthly, annual, 6-year and 12-year checks.** **Lithium-ion is not Class D.**
- **Signs (ISO 7010):** **P** red circle, **W** yellow triangle, **M** blue circle, **E** green (exits), **F** red square (fire equipment). **Exit signs lit with 90 minutes backup.** **Gas warning signs and status lamps at every entrance.** **NFPA 101 egress:** two exits, no locked exits, clear routes, release on alarm.
- **Regulation:** **AHJ** enforces. **UK Order 2005: risk assessment by the responsible person.** **EU: CE marking under Regulation 305/2011, F-gas 2024/573.** **US: IBC/IFC, OSHA 1910.157/.160/.162, AIM Act.** Insurers (**FM Global**, VdS, LPCB) may require more than the code.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **NFPA 75** (2024) | Fire protection of IT equipment: risk assessment, construction, detection, suppression, extinguishers, signs, training, lithium-ion UPS off-gas detection, immersion cooling |
| **NFPA 76** (2024) | Telecommunications facilities, VEWFD, EWFD, SFD |
| **NFPA 72** (2022), **NFPA 25** (2023) | Fire alarm and signalling, inspection and testing of water-based systems |
| **NFPA 13** (2025), **NFPA 750**, **NFPA 22** | Sprinklers, water mist, water tanks for fire protection |
| **NFPA 2001** (2025), **NFPA 12** | Clean agent systems (concentrations, discharge times, hold time, safety, maintenance), CO₂ systems |
| **NFPA 10** (2026) | Portable extinguishers: classes, placement, inspection |
| **NFPA 101** (2024), **NFPA 170**, **NFPA 704** | Life safety and egress, safety symbols, hazard identification |
| **NFPA 70 (NEC) Article 645**, **NFPA 70E**, **NFPA 855** (2026), **NFPA 220, 90A, 80** | IT room electrical rules and EPO, arc flash labels, energy storage, construction, ventilation, fire doors |
| **FM Global Data Sheets 5-32, 4-13, 2-0** | Insurer requirements for data centres, oxygen reduction, sprinklers |
| **EN 54** series (including **54-20**), **EN 12845**, **EN 15004**, **EN 12094**, **ISO 14520** | European and international detection, sprinklers and gas systems |
| **EN 16750** (2017 with A1:2020), **ISO 20338** (2019), **VdS 3527**, **BSI PAS 95** | Oxygen reduction systems |
| **EN 2**, **EN 3**, **UL 711** | Fire classes, extinguisher marking and rating |
| **ISO 7010** (2019), **ISO 3864**, **ISO 23601**, **ASTM E2072 / UL 1994** | Safety signs, colours, evacuation plans, photoluminescent signs |
| **BS 5839-1, BS 5306, BS 7273**, **LPCB LPS 1230 and 1048** | UK detection, extinguishers, gas actuation, approvals |
| **International Building and Fire Codes**, **OSHA 29 CFR 1910**, **UK Regulatory Reform (Fire Safety) Order 2005**, **EU Construction Products Regulation 305/2011** | Legal framework |
| **Montreal Protocol**, **AIM Act**, **EU F-gas Regulation 2024/573** | Environmental regulation of agents |
| **Uptime Institute** Annual Outage Analysis 2026, Tier Standard, and blog on data centre fires | Fire trends and Tier IV partitions |
| **Energy Incident Register** (to November 2026), **Allianz Commercial** 2026 claims analysis, incident reports (OVHcloud 2021, SK C&C 2022, NIRS 2025, Digital Realty 2025, Tata Communications 2026) | Fire statistics and lessons |
| **ANSI/TIA-942-C**, **EN 50600** | Data centre standards with fire provisions |
| Standard fire protection engineering | Sprinkler K-factor and density-area design, agent quantity formulas, oxygen and altitude calculations |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
