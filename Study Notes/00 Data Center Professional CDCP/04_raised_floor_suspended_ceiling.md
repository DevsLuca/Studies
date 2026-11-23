# Module 4: Raised Access Flooring and Suspended Ceiling

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section in these notes |
| --- | --- | --- |
| 4.1 | Raised Floor Standards | [Section 1](#41-raised-floor-standards) |
| 4.2 | Raised Floor Types and Components | [Section 2](#42-raised-floor-types-and-components) |
| 4.3 | Types of Loads | [Section 3](#43-types-of-loads) |
| 4.4 | General Guidelines and Weight of the Raised Floor | [Section 4](#44-general-guidelines-and-weight-of-the-raised-floor) |
| 4.5 | Grounding of the Raised Floor and Racks | [Section 5](#45-grounding-of-the-raised-floor-and-racks) |
| 4.6 | Cutting Raised Floor Tiles | [Section 6](#46-cutting-raised-floor-tiles) |
| 4.7 | Ramp and Landing Platform | [Section 7](#47-ramp-and-landing-platform) |
| 4.8 | Suspended Ceiling | [Section 8](#48-suspended-ceiling) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-4-raised-access-flooring-and-suspended-ceiling) |

**Objectives (from your slide).** After this module you should be able to describe and understand: the main standards for raised floors, the main types of raised floors, loading factors, the general rules for raised floors, ramp and landing platform, and the reasons for using suspended ceilings.

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course.

## Why a raised floor?

A raised floor (also called an **access floor** or **computer floor**) is a floor of removable **panels** held above the structural slab on **pedestals**. The space beneath is the **plenum** (or floor void).

| Benefit | Explanation |
| --- | --- |
| **Air distribution** | Cold air is delivered through the plenum and out of perforated tiles in the cold aisle |
| **Cable and pipe routing** | Power, data and pipework can run underneath, out of sight |
| **Flexibility** | Panels lift out, so changes and additions are easy |
| **Grounding** | The metal structure forms a bonded grid (see 4.5) |
| **Leak and fire detection** | Detectors and leak cables sit in the void |

Trade-offs: cost, reduced usable ceiling height, load limits, and less suitability for very high-density racks and liquid cooling. Some modern designs use a **slab floor** with overhead services. TIA-942 covers rack placement relative to the tile grid, tile cuts, and cable trays in access floors.

---

# 4.1 Raised floor standards

## 1. Main standards

| Standard | Origin | Notes |
| --- | --- | --- |
| **EN 12825** | Europe (CEN) | Raised access floors: classification by **ultimate load**, test methods, tolerances, fire and electrostatic characteristics |
| **CISCA** (Recommended Test Procedures for Access Floors) | USA | Test and rate floors by **working (design) load**, including concentrated, rolling and ultimate loads |
| **PSA MOB PF2 PS** | UK | Long-established British specification with three grades (light, medium, heavy), now commonly cross-referenced to EN 12825 |
| **ANSI/TIA-942, EN 50600-2-1, BICSI 002** | Data centre standards | Set floor requirements for the **computer room**: loading, height, bonding, tile cuts, rack placement |
| **IEEE 1100, TIA-607, EN 50310** | Grounding standards | Bonding and grounding of the floor structure |
| **ANSI/ESD S20.20, IEC 61340** | ESD standards | Electrostatic control and floor resistance |
| **NFPA 75, EN 13501** | Fire standards | Fire performance of floor assemblies |

## 2. EN 12825 in detail

EN 12825 classifies a raised floor **element** (panel plus pedestals and stringers, as installed) mainly by its **ultimate load**: the load at which it fails.

| Class | Ultimate load | Working load at safety factor 2.0 | Working load at safety factor 3.0 |
| --- | --- | --- | --- |
| 1 | 4 kN | 2.0 kN | 1.33 kN |
| 2 | 6 kN | 3.0 kN | 2.0 kN |
| 3 | 8 kN | 4.0 kN | 2.67 kN |
| 4 | 9 kN | 4.5 kN | 3.0 kN |
| 5 | 10 kN | 5.0 kN | 3.33 kN |
| 6 | 12 kN | 6.0 kN | 4.0 kN |

Other characteristics from the standard:

| Characteristic | Detail |
| --- | --- |
| **Safety factor** | Two classes: **2.0** and **3.0**. Working load = ultimate load ÷ safety factor |
| **Deflection classes** | **A** = max 2.5 mm, **B** = 3.0 mm, **C** = 4.0 mm, measured at the working load |
| **Permanent deformation** | Residual deflection after loading must not exceed about **0.5 mm** |
| **Test load** | Applied through a small square indenter (25 × 25 mm), at several points including panel centre, edge and corner |
| **Pedestals** | The understructure must support **4 times the working load** without distortion or damage |
| **Other tests** | Impact (hard and soft body), fire reaction and resistance, electrostatic conductivity, tolerances and interchangeability |

**Reading a rating.** A floor described as **"Class 5A, safety factor 2"** has an ultimate load of 10 kN, a working concentrated load of **5 kN**, and deflects no more than **2.5 mm** under that load. Server rooms typically use the upper classes (about Class 5 and 6) **[CHECK]**.

**CISCA vs. EN 12825:** CISCA ratings state the **working (design) load**, while EN 12825 states the **ultimate (breaking) load** and divides by a safety factor. They are not directly interchangeable, so always compare like with like.

**Typical data centre specification [CHECK]:** a concentrated load of at least about **4.45 kN (1,000 lbf)** (CISCA "heavy grade") and a uniform load of about **12 kPa (250 lbf/ft²)** or more are commonly quoted. These are **panel ratings**, which are different from the **building's minimum floor loading**: **ANSI/TIA-942-C** sets **5 kPa (100 lbf/ft²)** for computer rooms under 20 m².

---

# 4.2 Raised floor types and components

## 1. The system parts

| Component | Role |
| --- | --- |
| **Panel (tile)** | The walking surface, typically **600 × 600 mm (24 × 24 in)** |
| **Pedestal** | The adjustable support: **base plate** fixed to the slab, **threaded stem** to set the height, **adjusting nut** and a **head** that receives the panel corners |
| **Stringer** | A horizontal bar linking pedestal heads (stringered systems only) |
| **Cornerlock screws and gaskets** | Fix panels to heads. Conductive gaskets help the electrical path |
| **Perimeter trim and edge pieces** | Finish panels at walls and columns |
| **Ramp and step assemblies** | For level changes (see 4.7) |
| **Finish** | HPL (high-pressure laminate), PVC, carpet or ESD finish on top of the panel |
| **Perforated panels and grates** | Panels that let cold air through (see below) |
| **Cut-out trims and grommets** | Edge protection and air sealing where cables pass |

## 2. By panel construction

| Type | Characteristics | Typical use |
| --- | --- | --- |
| **All-steel (welded)** | Strong and fire-resistant, **conductive**, so it must be earthed and bonded | General data centre use |
| **Steel-encased with cementitious (concrete) fill** | High load rating, rigid, quiet, common in data centres | Heavy loads, higher-rated sites |
| **Steel-encased wood core** | Lighter and cheaper, lower load rating and fire resistance | Offices, low-load areas |
| **Calcium sulphate** | Dense, quiet, dimensionally stable, panels carry a finish | Technical rooms and offices |
| **Aluminium** | Light and strong, often moved frequently | High-density cooling zones |

## 3. By support structure

| Type | Characteristics |
| --- | --- |
| **Stringerless (freestanding / cornerlock)** | Panels sit on pedestal heads only. Cheaper, easy cable and air access, less lateral stability |
| **Stringered (bolted or snap-on grid)** | Horizontal bars link the pedestal heads. More rigid, suited to heavy loads, higher floors and earthquake zones |
| **Seismic systems** | Bolted and braced systems, with pedestals fixed to the slab |

## 4. Floor height

| Item | Typical range |
| --- | --- |
| **Minimum height** | About **300 mm** where the void carries air **[CHECK]** |
| **Mainstream data centre** | About **450 to 600 mm** **[CHECK]** |
| **Large or high-density halls** | About **600 to 800 mm** or more **[CHECK]** |
| **Above about 500 mm** | Stringers and bracing become important for stability (a French standard makes a braced frame compulsory above 500 mm) **[CHECK]** |

The void must be sized by **airflow calculation**, not by rule of thumb. Cable trays in the void can block air.

## 5. Tiles that let air through

| Tile | Characteristics |
| --- | --- |
| **Solid tile** | No airflow |
| **Perforated tile** | Typically about **25% open** area **[CHECK]**, placed in the cold aisle |
| **Grate** | Much more open (about 55% or more) **[CHECK]**, for higher airflow |
| **Adjustable-damper tile** | Airflow can be tuned |

Cold-aisle tiles sit in front of the racks. Only the tiles that are needed should be open: every extra opening or unsealed cut-out wastes cold air.

---

# 4.3 Types of loads

| Load | Meaning | Where it matters |
| --- | --- | --- |
| **Concentrated (point) load** | A load on a small area of one panel (a rack foot, a caster, a person's heel) | **The most important figure for data centres** |
| **Uniformly distributed load (UDL)** | Weight spread evenly over the whole area | Rows of tightly packed cabinets, battery racks, shelving |
| **Rolling load** | A wheeled load crossing the floor, tested over repeated passes | Moving racks, pallet jacks, trolleys |
| **Impact load** | A weight dropped onto the floor | Dropped tools or equipment |
| **Ultimate (failure) load** | The load at which the panel fails | The basis of EN 12825 classes |
| **Working (design) load** | The ultimate load divided by the safety factor | What you actually design to |
| **Safety factor** | Ultimate load ÷ working load, typically 2.0 or 3.0 | Margin against failure |
| **Deflection** | How much the panel bends under load, with a limit (for example 2.5 mm) | Floor stays level, panels don't rock |
| **Static vs. dynamic** | Standing weight vs. weight in motion | Moving loads are harsher than standing ones |

**Key point:** a rack's weight is carried by its **feet or casters**, so the **concentrated and rolling loads** decide the floor specification, not the average floor load. The load must also travel through the **pedestals** and into the **slab**, so the whole chain (panel, pedestal, slab) must be checked.

## Worked example 1: one rack on four feet

A fully loaded rack weighs **1,200 kg**.

```
Weight force = 1,200 kg × 9.81 = 11,772 N = 11.8 kN
Per foot (equal sharing, 4 feet) = 11.8 / 4 = 2.94 kN
Per foot (only 3 feet in contact, on an uneven floor) = 11.8 / 3 = 3.92 kN
```

Compare with the floor's **working concentrated load**:

| Floor | Working load (SF 2.0) | Equal share (2.94 kN) | Three-point contact (3.92 kN) |
| --- | --- | --- | --- |
| Class 3 (8 kN ultimate) | 4.0 kN | Passes, margin 36% | **Marginal** (only 2% margin) |
| Class 5 (10 kN ultimate) | 5.0 kN | Passes, margin 70% | Passes, margin 28% |

This is why designers leave a margin, and why a rack with **levelling feet** and a rack with **casters** are checked differently.

## Worked example 2: the average load

A hall holds **100 racks at 1,200 kg** in **450 m²**:

```
Total weight = 120,000 kg
Average load = 120,000 × 9.81 / 450 = 2,616 N/m² = about 2.6 kPa
```

The **average** is low. But the load is **concentrated on rack feet**, and the **slab** must still carry a local load several times higher. So designers check **concentrated and rolling loads on the panels**, the **pedestals**, and the **slab** separately.

## Convenient conversion

**1 kN ≈ 102 kg** (about 100 kg). So 4.5 kN ≈ 459 kg and 6 kN ≈ 612 kg on one point.

---

# 4.4 General guidelines and weight of the raised floor

## 1. The weight of the floor itself (dead load)

The floor adds its own weight to the slab before any equipment arrives.

**Worked example (illustrative figures).** A steel panel with concrete fill weighs about **22 kg** [CHECK]. One m² holds 1 / (0.6 × 0.6) = **2.78 panels**.

```
Panels:    2.78 × 22 kg = about 61 kg/m²
Pedestals: about 8 kg/m² (assumed)
Total:     about 69 kg/m² = about 0.68 kN/m²
```

So the floor itself is **about 0.7 kN/m²** of **dead load**, plus cabling and trays beneath, plus the **live load** (equipment, people). The building's structural design must include both.

## 2. General guidelines

| Guideline | Detail |
| --- | --- |
| **Floor type and rating** | Specify by class and test report (EN 12825 or CISCA), not by brochure |
| **Height** | Set by an airflow and cabling calculation (see 4.2) |
| **Slab below** | Clean, flat, **sealed** against dust. A dusty slab sheds particles into the air stream |
| **Levelness and flatness [CHECK]** | Typical specification: flatness under a 2 m ruler under about 2 mm, adjacent panels within about 1 mm, levelness over 5 × 5 m under about 3 mm |
| **Pedestals** | Fixed to the slab (glued or bolted), correct height, with panel corners fully seated |
| **Panels removable** | Lifting must always be possible, with **panel lifters (suction)**. Never leave open holes |
| **Ratings** | Use panels with the right load class in each area (heavier near UPS, batteries and high-density racks) |
| **Heavy equipment** | Plan the route and use **load-spreading plates** (such as thick plywood) over the floor when moving heavy items |
| **Racks and the tile grid** | Place racks to line up with the tile grid. A common layout puts a **cold aisle two tiles (about 1.2 m) wide** **[CHECK]** |
| **Cable trays in the void** | Wire-basket or other open trays that don't block airflow, often routed under the **hot aisle** **[CHECK]**. **Separate power from data**, and keep fibre away from copper where practical |
| **Pipes** | Keep water pipes out of the void where possible. If unavoidable, protect and add **leak detection** |
| **Fire** | Non-combustible panels and finishes, **detection in the void**, and **sealed penetrations** to prevent fire and smoke spreading |
| **Seismic zones** | Braced or stringered systems with fixed pedestals |
| **Finishes** | ESD-compliant, no ordinary carpet or insulating coatings |
| **Maintenance** | Periodic inspection of pedestals, panels, bonding and sealing |

## 3. Sealing the plenum

- Seal **cable cut-outs** with brush or grommet kits (see 4.6).
- Seal **perimeter gaps** at walls and columns.
- Keep unused perforated tiles **closed**.
- A leaky floor wastes cold air and **raises PUE**.

---

# 4.5 Grounding of the raised floor and racks

## 1. Why

| Reason | Explanation |
| --- | --- |
| **Static (ESD)** | People and moving equipment build up charge, and a discharge can damage electronics. The floor lets the charge drain away |
| **Safety** | A live conductor touching a panel or rack must trip a breaker, not leave the floor live |
| **Equipotential bonding** | Everything touchable sits at the same voltage |
| **Noise** | A bonded grid gives a stable reference (Module 6, bonding network) |

## 2. How the floor is grounded

The electrical path runs through the whole structure, so **every connection matters**:

```
Footwear → panel surface → panel → pedestal head → pedestal → grid / stringer
       → copper grounding grid → room bonding busbar → building earth
```

| Measure | Detail |
| --- | --- |
| **Conductive path** | Metal panels and pedestals are electrically connected, with **conductive gaskets** at the heads |
| **Bonding the structure** | The floor's metallic support structure is bonded to building steel or the bonding network at **several places**, with the number scaled to the size of the room |
| **Mesh / signal reference grid** | Many sites lay a copper grid under the floor, to which pedestals and racks are bonded. Older practice often bonded about **every sixth pedestal** to the grid **[CHECK]** |
| **Racks** | Each rack is bonded to the grid or a rack busbar by its **own conductor**. The floor connection does **not** bond the racks |
| **Racks and ESD** | Racks, doors and panels are bonded so the whole cabinet is one electrical piece |
| **Finishes** | Coatings, laminates and adhesives must be **ESD-compliant**. An ordinary vinyl, wax or epoxy can insulate the floor and break the path |
| **Maintenance** | Test resistance and continuity after installation and periodically, because corrosion, loose joints and replaced panels create gaps |

## 3. Resistance classes

| Class | Resistance (surface to ground) | Behaviour |
| --- | --- | --- |
| **Conductive** | Below **1 × 10⁶ Ω** | Charge drains very quickly |
| **Static dissipative** | From **1 × 10⁶ Ω** to below **1 × 10⁹ Ω** | Charge drains in a controlled, slower way. **Typical for data centres** |
| **Insulative** | Above **1 × 10⁹ Ω** | Charge doesn't drain. No ESD protection |

(From ANSI/ESD STM7.1 and IEC 61340-4-1.) **[CHECK]**

**Other figures to know [CHECK]:**

- The ESD control standard (ANSI/ESD S20.20, IEC 61340-5-1) assesses the **whole system** (person, footwear and floor): resistance to ground below **1 × 10⁹ Ω**, and **walking body voltage below 100 V**.
- Some equipment makers specify a maximum floor-to-ground resistance of about **2 × 10¹⁰ Ω** and a **minimum of about 150 kΩ** between two points on the floor 1 m apart (a safety limit).
- **Dissipative is preferred over conductive** in data centres: extremely low resistance raises the shock hazard near live equipment.

**Remember the human link:** a perfect floor is wasted if staff wear **insulating soles**. ESD programmes pair the floor with **ESD footwear or heel straps**, wrist straps for handling equipment, and **humidity control** (very dry air makes static far worse).

## 4. Typical commissioning checks

1. Continuity of the grounding path through panels, pedestals, stringers and rack bonds to building steel, at several points.
2. Surface resistance and resistance to ground at representative locations.
3. Walking body voltage where an ESD programme applies.
4. Records kept as a baseline for later re-testing.

---

# 4.6 Cutting raised floor tiles

## 1. Why cutting matters

A panel is engineered as a whole. **Every cut weakens it** and can reduce its load rating, so cutting must be planned.

## 2. Rules for cuts

| Rule | Reason |
| --- | --- |
| **Plan before cutting** | Decide where cables, grommets and air openings go before any panel is cut |
| **Keep cuts away from the edges** | A common recommendation is to keep the cut at least about **75 mm (3 in)** inside the panel edge **[CHECK]** |
| **Never cut a corner** | The corners and edges carry the load into the pedestal heads |
| **Keep the cut within the panel's central quadrant area** | The area away from the **diagonals** is stronger. TIA-942 shows tile cuts that should not touch the lines of the **cross formed by the corners** of the tile **[CHECK]** |
| **Avoid pedestals and stringers** | The hole must not sit on a pedestal or stringer |
| **Use extra support if needed** | A cut panel that carries weight may need **extra pedestal support** under it |
| **Follow the manufacturer's instructions** | They state the tools, procedure, and the **reduced design load of a cut tile** |
| **Keep cut panels out of heavy-load zones** | Use uncut or reinforced panels for racks and heavy equipment |
| **Size the hole precisely** | Too big weakens the tile and wastes cold air. Too small needs enlarging |

## 3. Method

1. **Mark and measure** the cut.
2. **Drill pilot holes** large enough for the saw blade, inside the line.
3. **Cut** with a reciprocating saw and a bi-metal blade (about 14 to 20 teeth per inch) or a jig saw. For round holes use a **hole saw** (a drill press is recommended for holes up to about 150 mm / 6 in). Glass or tile cutters are not suitable.
4. **Deburr** the edges on top and bottom.
5. **Fit edge protection:** plastic **edge trim (L-moulding)** and corners, or a **grommet**.
6. **Seal** the opening around the cables with a **brush grommet** or foam, to stop cold air escaping.

## 4. Edge trim and sealing

| Item | Purpose |
| --- | --- |
| **Edge trim / cut-out trim** | Protects cables from abrasion and hands from sharp edges, and is required by standards for cable passages |
| **Brush grommet / seal kit** | Lets cables pass but blocks airflow |
| **Foam sealing** | Fills gaps after cabling is installed |

Installing racks at the **front edge of a tile** helps, because cables can drop through a cut-out near the rack.

## 5. Related guidance

- Where a **step or ramp** is built from panels, keep widths in whole panel sizes where possible, since **cut panels are inherently weaker**.
- Check air supply: before sealing cut-outs, make sure the rack inlet still gets airflow from **perforated tiles or grates**.

---

# 4.7 Ramp and landing platform

A raised floor sits higher than the corridor or loading area, so equipment needs a **safe, gentle way up**.

## 1. Ramp requirements

| Item | Typical requirement |
| --- | --- |
| **Slope** | **1:12** (about 8%) is the commonly cited slope for accessible ramps. Equipment-only routes may be somewhat steeper, but check local code **[CHECK]** |
| **Width** | At least as wide as the equipment and doors, usually about **1.2 m or more** **[CHECK]** (newer standards also call for racks in some areas at least 800 mm wide) |
| **Surface** | **Non-slip**, with the **same load rating** as the raised floor |
| **Structure** | Built on adjustable supports, strong enough for the heaviest load (a loaded rack, UPS cabinet, battery rack) |
| **Edges** | **Handrails or edge protection** where required by code |
| **Transitions** | Smooth, **no lip or gap** at top and bottom |
| **Alternatives** | A **platform lift or elevator** where space is short |

## 2. Landing platform

| Item | Detail |
| --- | --- |
| **Purpose** | A flat area at the **top** (and sometimes the bottom) of the ramp where equipment can be **stopped, positioned and turned** before moving on |
| **Size** | At least the ramp width in both directions, and commonly about **1.2 to 1.5 m** **[CHECK]**, enough for the longest equipment and the people moving it |
| **Surface and rating** | Same as the ramp and the raised floor |
| **Doors** | Doors should not open onto the ramp itself |
| **Safety** | Edge protection, clear lighting (also emergency lighting), non-slip finish |

**Worked example: ramp length.** The raised floor is **0.6 m** high:

```
Length at 1:12 = 0.6 × 12 = 7.2 m
```

A taller floor needs a **longer ramp**, which takes real floor area. This must be planned with the building layout.

## 3. Steps for people

Where personnel use a step, local codes set the tread and riser sizes (a common guide is a tread of about 300 mm and a riser of about 150 mm) **[CHECK]**, and the raised floor makes a **step assembly** from panels with braced edges.

---

# 4.8 Suspended ceiling

A suspended ceiling is a **false ceiling hung below the structural slab**, creating a void above.

## 1. Reasons for using suspended ceilings

| Reason | Detail |
| --- | --- |
| **Hide and organise services** | Ducts, cable trays, lighting and pipes sit in the void |
| **Return air plenum** | The void carries warm return air back to the cooling units, supporting hot-aisle return |
| **Dust control** | Stops dust falling from the concrete slab above |
| **Mounting** | A place for lights, **smoke detectors**, and sprinkler or gas nozzles |
| **Fire protection** | A smaller room volume needs **less gas** for suppression, and the void can have its own detection |
| **Acoustics** | Helps reduce noise |
| **Appearance** | A clean, uniform finish |
| **Access** | Removable tiles give maintenance access to services above |

## 2. Requirements

| Requirement | Detail |
| --- | --- |
| **Clear height** | At least about **2.6 m** from the finished floor to the underside of the ceiling **[CHECK]** |
| **Ceiling tiles** | **Fire-rated**, **non-dust-shedding** (no loose fibres) and compatible with the fire suppression system |
| **Detection** | Smoke detection in **both the floor void and the ceiling void** |
| **Nozzle clearance** | Keep clear space beneath gas or sprinkler nozzles, commonly about **460 mm (18 in)** to the first obstruction **[CHECK]** |
| **Gas discharge pressure** | A gas release raises room pressure briefly, so tiles are **restrained or the room has pressure relief**, otherwise they can lift or fall **[CHECK]** |
| **Support of services** | Cable trays and heavy services should hang from the **structural slab**, not the ceiling grid |
| **Return air** | If the void is a return plenum, the cable and materials in it must meet the **plenum fire rating** |
| **Services above** | No water or sewer pipes above the computer room, where possible |
| **Clearance above racks** | Leave space between the tallest rack and the ceiling for return airflow and suppression (commonly 600 to 900 mm) **[CHECK]** |

## 3. Trade-offs

Many modern data centres use **no suspended ceiling** at all, relying on **containment**, open plenums and **overhead trays** hung from the slab. The choice depends on the cooling design, fire suppression volume, cleanliness and appearance.

---

## Glossary

| Term | Meaning |
| --- | --- |
| Plenum | The void under the raised floor (or above the ceiling) |
| Pedestal | Adjustable support for a floor panel |
| Stringer | Horizontal bar linking pedestal heads |
| Concentrated load | A load on a small area, such as a rack foot |
| UDL | Uniformly distributed load |
| Rolling load | A moving, wheeled load |
| Ultimate load | The failure load |
| Working load | Ultimate load ÷ safety factor |
| Deflection | How far a panel bends under load |
| ESD | Electrostatic discharge |
| Static dissipative | Floor resistance 10⁶ to 10⁹ Ω |
| PE / bonding | Protective earth / connecting metalwork together |
| Landing platform | Flat area at the top of a ramp |

## Exam takeaways

- The main standards are **EN 12825**, **CISCA** and **PSA MOB PF2 PS**, alongside the data centre standards.
- EN 12825 classifies by **ultimate load** (Class 1 to 6: 4, 6, 8, 9, 10, 12 kN), with **safety factor 2.0 or 3.0**, **deflection classes A, B, C** (2.5, 3.0, 4.0 mm), and pedestals that carry **4 times the working load**.
- **Working load = ultimate load ÷ safety factor**. CISCA states the working load, EN 12825 the ultimate load.
- Panel types: **all-steel, steel with concrete fill, wood core, calcium sulphate, aluminium**. Support: **stringerless** vs. **stringered**.
- Know every load type, especially **concentrated** and **rolling**.
- The floor adds its own **dead load** (about 0.7 kN/m² in the worked example).
- Seal cut-outs and the slab, protect cables with **trim and grommets**, and use panel lifters.
- **Grounding:** the whole path from panel to earth must be continuous. Data centres use **static dissipative** floors (10⁶ to 10⁹ Ω). Racks need their **own bonds**.
- **Tile cuts** weaken panels. Keep cuts away from the edges, corners and pedestals, use trim and grommets.
- **Ramp:** gentle slope (1:12), non-slip, same load rating, handrails if required, **landing platform** at the top.
- **Suspended ceiling:** services, return air plenum, dust control, mounting for detectors and nozzles, **less gas volume**. **Detection in both voids.**

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **EN 12825** | Panel classes, safety factors, deflection classes, pedestal requirement |
| **CISCA** test procedures | Working (design) load ratings |
| **PSA MOB PF2 PS** | British access floor specification |
| **ANSI/TIA-942-C** (2024), **EN 50600-2-1**, **BICSI 002** | Computer room floor requirements, including the 5 kPa minimum floor loading |
| **ANSI/ESD STM7.1**, **IEC 61340-4-1** | Floor resistance classes (conductive, dissipative, insulative) |
| **ANSI/ESD S20.20**, **IEC 61340-5-1** | Electrostatic discharge control |
| **ANSI/TIA-607**, **EN 50310**, **IEEE 1100** | Bonding and grounding of the floor and racks |
| **NFPA 75**, **EN 13501** | Fire performance |
| Accessibility practice | The 1:12 ramp slope |
| Manufacturer and TIA-942 practice | Tile-cutting rules |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
