# Module 5: Light

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section in these notes |
| --- | --- | --- |
| 5.1 | Standards, Definition and Units of Measure | [Section 1](#51-standards-definition-and-units-of-measure) |
| 5.2 | Light Fixtures and Placement | [Section 2](#52-light-fixtures-and-placement) |
| 5.3 | Emergency Light | [Section 3](#53-emergency-light) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-5-light) |

**Objectives (from your slide).** After this module you should be able to describe and understand: the various measurements of light, some standards on lighting, the best way to connect and position lights, and emergency light standards and placement requirements.

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Standards are revised, so confirm the edition your course uses.

## Why lighting matters in a data centre

| Reason | Detail |
| --- | --- |
| **Safe, accurate work** | Technicians read labels, port numbers and status LEDs, and make connections |
| **Safety** | Poor light causes accidents, and people must be able to leave safely in an emergency |
| **Heat and energy** | Every watt of lighting becomes heat that the cooling system must remove, and it counts toward PUE |
| **Reliability** | Lighting must not cause outages or interference (electrical noise, flicker) |
| **Security** | CCTV needs enough light to see |

---

# 5.1 Standards, definition and units of measure

## 1. What light is

**Light** is the part of the electromagnetic spectrum the human eye can see, roughly **380 to 780 nm** in wavelength. Lighting design measures **how much** light a source produces, **where it goes**, **how much arrives** on a surface, and **how it looks**.

## 2. The measurements

| Quantity | Unit | Symbol | Meaning |
| --- | --- | --- | --- |
| **Luminous flux** | **lumen** | lm (Φ) | Total visible light emitted by a source |
| **Luminous intensity** | **candela** | cd (I) | Light emitted in **one direction** (lumens per steradian) |
| **Illuminance** | **lux** | lx (E) | Light **arriving at a surface**: 1 lux = 1 lumen per m² |
| **Illuminance (US)** | **foot-candle** | fc | 1 lumen per ft². **1 fc ≈ 10.76 lux** |
| **Luminance** | **candela per m²** | cd/m² (L) | Brightness of a surface **as seen by the eye**, linked to glare |
| **Luminous efficacy** | **lumens per watt** | lm/W | How efficiently electricity is turned into light |
| **Colour temperature** | **kelvin** | K | How warm or cool the light looks (about 2700 K warm, 4000 K neutral, 6500 K cool) |
| **Colour rendering index** | none (0 to 100) | CRI / Ra | How faithfully colours appear under the light |
| **Uniformity** | ratio | Uo | Minimum illuminance ÷ average illuminance |
| **Glare rating** | index | UGR | Unified glare rating: discomfort glare (lower is better) |
| **Maintenance factor** | ratio | MF | Allowance for dirt and ageing (for example 0.8) |
| **Utilisation factor** | ratio | UF | Share of the lamp's light that actually reaches the working plane |

**Key distinction:** **lumens** describe what the lamp *emits*, **lux** describes what *reaches the surface*, **candela** describes the *direction*, and **luminance** describes how bright a surface *looks*.

## 3. Horizontal and vertical illuminance

| Type | Measured on | Why it matters |
| --- | --- | --- |
| **Horizontal** | The floor or a work surface | Navigation, work at benches |
| **Vertical** | A vertical surface, such as the **face of a rack** | Technicians read labels and LEDs on the vertical face |

A hall can have plenty of horizontal light and still leave rack faces in shadow. **Vertical illuminance on the rack face is the important figure** in a data centre.

## 4. The formulas

```
Illuminance:             E = Φ / A            (lux = lumens ÷ area in m²)
Inverse-square law:      E = I / d²           (point source, surface facing the source)
With an angle:           E = I × cos θ / d²
Lumen method:            N = (E × A) / (Φ_luminaire × UF × MF)
Uniformity:              Uo = E_min / E_average
Efficacy:                lm/W = lumens ÷ electrical watts
```

### Worked example 1: inverse-square law

A luminaire shines **1,000 cd** straight down on a surface **2 m** away:

```
E = 1,000 / 2² = 250 lux
```

At **4 m** (twice the distance):

```
E = 1,000 / 4² = 62.5 lux     (a quarter of the light, not half)
```

### Worked example 2: lumen method

A hall's aisles total **60 m²** and must be lit to **500 lux**. Assume **UF = 0.6** and **MF = 0.8**, and luminaires of **5,000 lm** each:

```
Total lumens needed = (500 × 60) / (0.6 × 0.8) = 30,000 / 0.48 = 62,500 lm
Number of luminaires = 62,500 / 5,000 = 12.5, so 13 luminaires
```

### Worked example 3: energy and heat

The same 62,500 lm delivered by two technologies:

| Source | Efficacy | Electrical power | Heat to remove |
| --- | --- | --- | --- |
| **LED** at 130 lm/W | 130 | 62,500 / 130 = about **481 W** | about 0.48 kW |
| **Fluorescent** at 80 lm/W | 80 | 62,500 / 80 = about **781 W** | about 0.78 kW |

Almost all the power ends up as **heat**, so the cooling system must remove it. LED lighting therefore saves energy twice: less electricity for lighting, and less cooling.

### Worked example 4: uniformity

Measured on a grid: **E_min = 350 lux, E_average = 500 lux**:

```
Uo = 350 / 500 = 0.7
```

A common target is **Uo of 0.6 or better** for a work area **[CHECK]**.

### Conversions

```
1 fc  = 10.76 lux          500 lux = about 46.5 fc
10 fc = about 107.6 lux    1 lux   = about 0.093 fc
```

## 5. Light source technologies **[CHECK]**

| Source | Typical efficacy | Notes for data centres |
| --- | --- | --- |
| **Incandescent / halogen** | about 10 to 25 lm/W | Very inefficient, lots of heat. Not used |
| **Fluorescent (T8, T5)** | about 70 to 100 lm/W | Older sites. Magnetic ballasts can cause **electromagnetic interference** and flicker, lamps need replacing |
| **Metal halide / HID** | about 70 to 110 lm/W | High-bay areas, slow start. Largely replaced |
| **LED** | about 100 to 200+ lm/W | **The normal choice**: efficient, long life, instant on, dimmable, little radiant heat |

**LED points in a data centre:**

- The **driver (power supply)** is the weak point. Heat shortens its life, so in **hot aisles** use drivers rated for high temperatures, or mount drivers remotely.
- Choose **flicker-free** drivers: flicker disturbs cameras and people.
- Drivers must meet **electromagnetic compatibility (EMC)** limits, so they don't interfere with data cabling (see Module 7). Keep lighting cables apart from data cables, commonly **at least 300 mm** **[CHECK]**.
- Choose **CRI 80 or higher**, and about **4000 K** neutral white so labels and cable colours are easy to read **[CHECK]**.

## 6. Standards on lighting

| Standard | Topic |
| --- | --- |
| **EN 12464-1** | Lighting of indoor workplaces (European): illuminance, uniformity, glare (UGR) and colour rendering by task |
| **EN 12665** | Basic terms and criteria for lighting requirements |
| **EN 15193** | Energy performance of lighting (LENI indicator) |
| **EN 60598 series** | Luminaire safety. EN 60598-2-22 covers **emergency luminaires** |
| **ANSI/TIA-942** | Data centre standard with lighting recommendations for the computer room |
| **EN 50600-2-1 / ISO/IEC 22237-2** | Data centre building construction, including lighting provisions |
| **EN 1838** | Emergency lighting: the lighting requirements |
| **EN 50172 / ISO 30061** | Emergency escape lighting **systems**: installation, testing, maintenance and documentation |
| **NFPA 101, IBC** | US life safety and building codes (egress lighting) |
| **NFPA 70 (NEC) Article 700** | US emergency systems wiring |
| **CIE publications** | International definitions: colorimetry, glare, photometry |

**Typical data centre lighting targets (TIA-942 family) [CHECK]:**

| Where | Requirement |
| --- | --- |
| **Computer room aisles, horizontal** | **500 lux**, measured **1 m above the finished floor** in the middle of the aisle |
| **Computer room, vertical** | **200 lux**, measured **1 m above the floor**, on the rack face |

Other guidance commonly used **[CHECK]**:

| Space | Typical level |
| --- | --- |
| Equipment aisles | 300 to 500 lux |
| Plant, electrical and UPS rooms | about 200 lux |
| Staging and maintenance benches | 300 to 500 lux |
| Corridors | about 100 to 200 lux |
| NOC, control room and offices (screen work) | 500 lux or more, **UGR ≤ 19** |

There is no single mandatory lux value for every server room. Targets come from the **standard in force, the task, and local law**.

---

# 5.2 Light fixtures and placement

## 1. Fixture types

| Fixture | Typical use |
| --- | --- |
| **Linear LED (surface or suspended)** | Rack aisles, running parallel to the rows |
| **Recessed troffer (ceiling grid panel)** | Where a suspended ceiling exists, offices, NOC |
| **High-bay** | Tall spaces such as generator halls or loading areas |
| **Sealed / IP-rated fittings (for example IP54 or higher)** | Plant rooms, battery rooms, generator areas (dust and moisture) |
| **Task and inspection lights** | Maintenance work, portable lamps |
| **Emergency luminaires and exit signs** | Escape routes (see 5.3) |

## 2. Placement rules

| Rule | Reason |
| --- | --- |
| **Centre the fixtures over the aisles, not over the racks** | Light reaches the rack faces from the side. Fixtures over a rack light the rack top and waste output |
| **Run fixtures parallel to the rack rows** | Continuous light along the aisle |
| **Use narrow-aisle optics** | Directs light onto both rack faces |
| **Aim for even light and no dark spots** | Avoids shadows between fittings, and keeps uniformity high |
| **Allow for light loss** | Full cable trays and tall racks block light, so design with that in mind |
| **Coordinate with other services** | Sprinkler or gas nozzles, smoke detectors, cable trays, containment and return air paths |
| **Keep clear of airflow** | Fittings in containment must be compact and out of the air path |
| **Heat-tolerant fittings in hot aisles** | Driver life falls quickly with temperature |
| **Control glare** | Especially in the NOC and any area with screens |
| **Allow safe maintenance** | Drivers and fittings that can be replaced **without opening the ceiling above live racks** |
| **Mount in the ceiling grid or on rails** | With enough clearance and without loading the grid |

### Worked example: fixtures along an aisle

An aisle is **20 m long and 1.2 m wide** (24 m²). Target **500 lux**, with **UF = 0.5** (racks absorb light) and **MF = 0.8**, using linear fixtures of **4,500 lm**:

```
Total lumens = (500 × 24) / (0.5 × 0.8) = 12,000 / 0.4 = 30,000 lm
Fixtures = 30,000 / 4,500 = 6.7, so 7 fixtures
Spacing = 20 m / 7 = about 2.9 m
```

This is only a first estimate. Real designs use **photometric software** with the cabinets in the model, and they check **vertical illuminance on the rack face**.

## 3. Controls

| Control | Detail |
| --- | --- |
| **Three-level lighting [CHECK]** | A TIA-942 recommendation based on occupancy: a **very low level** when nobody is present (enough for CCTV, about 5 to 10 lux), a **walking level** that **motion detection** switches on when someone enters, and **full task lighting** when people are working |
| **Occupancy sensors** | Save energy. Test coverage with racks in place so nobody is left in the dark |
| **Maintenance mode** | A manual override with a delay, so technicians keep full light |
| **Switching** | Switches at each entrance and exit |
| **DALI / BMS integration** | Dimming, status and fault reporting to the building management system |
| **Zoning** | Separate zones so one fault does not darken the whole hall |

## 4. Connecting the lights (electrical)

| Rule | Reason |
| --- | --- |
| **Separate circuits and panels from the IT equipment** | Lighting faults and maintenance work can't affect the servers |
| **Alternate fixtures across two or more circuits** | One circuit failing doesn't leave the room dark |
| **Normally not from the UPS** | The UPS capacity is reserved for critical IT load. General lighting usually sits on the **essential (generator-backed) supply** |
| **Emergency lighting separate from normal lighting** | It has its own supply and battery (see 5.3) |
| **Follow EMC practice** | Keep lighting cables apart from data cables and use compliant drivers |
| **Protection and earthing** | Proper protection, bonding and labelling, per the electrical code |

**Why the lighting is not on the UPS:** lighting adds load to the protected supply and takes capacity from the servers. A UPS fault or overload would also then plunge the room into darkness. Emergency lighting uses its **own batteries** instead.

---

# 5.3 Emergency light

## 1. Purpose

If the normal supply fails, **emergency lighting** lets people **see, find the way out and leave safely**, operate safety equipment, and shut down hazardous processes. It is a **life-safety system**, so it must not be designed by simply running the normal lights at a lower output.

## 2. Types (EN 1838)

| Type | Purpose |
| --- | --- |
| **Emergency escape lighting** | Lets people leave safely. It has three categories (below) |
| **Standby lighting** | Lets **normal activities continue** after a failure (not an evacuation measure) |

Escape lighting categories:

| Category | Purpose |
| --- | --- |
| **Escape route lighting** | Lights corridors, stairs and exits |
| **Open area (anti-panic) lighting** | Reduces panic in large spaces and helps people reach an escape route |
| **High-risk task area lighting** | Protects people working at hazardous equipment, so they can make it safe |

## 3. EN 1838 requirements **[CHECK]**

| Parameter | Escape route | Open area (anti-panic) | High-risk task area |
| --- | --- | --- | --- |
| **Minimum illuminance** | **1 lux** on the centre line of the route (routes up to 2 m wide) | **0.5 lux** across the empty core area (excluding a 0.5 m border) | **10% of the normal task illuminance, minimum 15 lux** |
| **Applies to** | Corridors, stairs, exits | Open areas larger than about **60 m²**, or with an escape route through them or identified hazards | Hazardous equipment, such as plant and machinery |
| **Uniformity** (max : min) | No worse than **40 : 1** | No worse than **40 : 1** | No worse than **10 : 1** |
| **Response** | **50% within 5 s, 100% within 60 s** | **50% within 5 s, 100% within 60 s** | Full level within **0.5 s** |
| **Duration** | At least **1 hour** | At least **1 hour** | As long as the hazard lasts |
| **Colour rendering** | **Ra 40 or higher** (so safety colours can be recognised) | Same | Same |

**Duration in practice:** national rules often require **3 hours**, especially where people sleep or may re-enter quickly (for example the UK's BS 5266-1 recommends 3 hours for most premises). In the US, egress lighting is typically required for **90 minutes**, with an average of about **1 foot-candle (about 10.8 lux)** along the path **[CHECK]**. Always follow the local code.

### Worked example: uniformity

A route has **20 lux** directly under each luminaire and **0.4 lux** between them:

```
Ratio = 20 / 0.4 = 50 : 1
```

That **fails** the 40 : 1 limit, even though the average looks generous. The fix is **more luminaires, closer together**, not brighter ones.

## 4. Where to place emergency luminaires (points of emphasis)

A luminaire is required **near** each of these (commonly **within 2 m**) **[CHECK]**:

| Location | Reason |
| --- | --- |
| **Each exit door** and **outside each final exit** | People must see the exit and get clear of the building |
| **Stairs**, so that each flight is lit | Trip and fall risk |
| **Changes of direction** | People must see where the route turns |
| **Intersections of corridors** | Choosing the right way |
| **Changes of floor level** | Steps, ramps, thresholds (including the **ramp to a raised floor**) |
| **Exit signs** | Signs must be seen |
| **Fire alarm call points** | They must be found and used. About **5 lux vertical** is recommended at call points and fire equipment |
| **Fire-fighting equipment** | Extinguishers, hose reels |
| **First-aid points** | Quick access |
| **High-risk areas** | Battery room, generator room, switch rooms, plant rooms |

Additional rules:

- Every escape route compartment should have **at least two luminaires**, so that one failure does not leave it dark.
- Between the points of emphasis, **extra luminaires** are added until the lux and uniformity targets are met, using the manufacturer's **spacing tables** or a photometric calculation.
- **Luminaires that are not in mains-powered maintained mode** must still meet the response times.

## 5. Exit signs

| Item | Detail |
| --- | --- |
| **Colour** | White symbol on a **green** background for exits |
| **Pictograms** | Standard "running man" symbol and arrows, understood internationally |
| **Luminance** | Minimum luminance on the sign, with white-to-green ratio about **5 : 1 to 15 : 1** **[CHECK]** |
| **Viewing distance** | Related to the sign height: commonly about **200 times the height** for internally illuminated signs and **100 times** for externally illuminated ones **[CHECK]** |
| **Position** | Over exits, and along the route where the exit is not directly visible |
| **Illumination** | Internally illuminated, or lit by an emergency luminaire within about 2 m |

## 6. Types of emergency lighting system

| System | How it works | Notes |
| --- | --- | --- |
| **Self-contained luminaire** | Each luminaire has its **own battery** | Simple, no central equipment. Each battery must be tested and replaced |
| **Central battery system (CBS)** | One central battery and charger supplies many luminaires | Fewer batteries to maintain, but a central point of failure, and fire-resistant cabling is needed |
| **Generator-backed supply** | A generator after a short delay | The generator takes **about 10 to 15 seconds**, which is **too slow** for the 5 s requirement, so luminaires also need a battery or UPS to cover the gap |

| Mode | Meaning |
| --- | --- |
| **Maintained** | The luminaire is **lit all the time**: normal lighting from the mains, emergency lighting from the battery |
| **Non-maintained** | The luminaire is **off** in normal use and switches **on** when the mains fails |
| **Combined** | One luminaire provides normal and emergency light |

### Worked example: response time

```
t = 0 s    Utility fails. Lights go out
t = 5 s    Emergency lighting must already be at 50% (battery-powered)
t = 10–15 s  Generator starts and takes the load
t = 60 s   Emergency lighting must be at 100%
```

The generator alone cannot meet the 5 s requirement, which is why emergency luminaires have **their own batteries**.

### Worked example: battery sizing

60 luminaires at **4 W each** in emergency mode for **3 hours**:

```
Energy = 60 × 4 W × 3 h = 720 Wh
With a design margin of 1.25 for battery ageing and temperature = 900 Wh
```

## 7. Testing and maintenance **[CHECK]**

| Test | Frequency |
| --- | --- |
| **Function test** (briefly switch to battery, check every luminaire lights) | Monthly |
| **Full-duration test** (run on battery for the full rated period, for example 3 hours) | Annually |
| **Charge indicator checks** | Regularly |
| **Records** | A **log book** of every test and repair (or an **automatic test system** that records results) |

Why it matters: batteries age silently. A luminaire can pass a short monthly test but fail well before the full duration.

## 8. Emergency lighting in a data centre

- **Escape routes** from the white space and plant rooms must meet EN 1838 (or the local code).
- **Exits from the computer room**, especially because a **gas suppression discharge** means everyone must leave quickly.
- **High-risk task lighting** in battery rooms, generator rooms and switch rooms.
- **Ramps and raised floor edges** need light, as trips there are dangerous.
- **Wiring and fixtures** should be separate from IT circuits, with **their own batteries**, and tested on a schedule.
- **The emergency lighting does not replace** normal task lighting, so staff still need handlamps or standby lighting to keep working after a power failure.

---

## Glossary

| Term | Meaning |
| --- | --- |
| Lumen / candela / lux | Light emitted / light in one direction / light arriving on a surface |
| Foot-candle | 1 lm per ft² (about 10.76 lux) |
| Luminance | Brightness of a surface as seen by the eye (cd/m²) |
| Efficacy | Lumens per watt |
| CRI (Ra) | Colour rendering index |
| UGR | Unified glare rating |
| Uniformity | Minimum ÷ average illuminance (or max : min for emergency lighting) |
| UF / MF | Utilisation factor / maintenance factor |
| Escape route lighting | Emergency lighting along the route out |
| Anti-panic lighting | Open area emergency lighting |
| High-risk task lighting | Emergency lighting at hazardous equipment |
| Standby lighting | Lighting that lets work continue |
| Maintained / non-maintained | Lit all the time / lit only on failure |
| CBS | Central battery system |
| Points of emphasis | Locations that need a luminaire (exits, stairs, call points, and so on) |

## Exam takeaways

- **Lumen** = emitted, **lux** = arriving (lm/m²), **candela** = direction, **luminance** = how bright a surface looks, **1 fc ≈ 10.76 lux**.
- **Inverse-square law:** double the distance, a quarter of the light.
- **Lumen method:** N = (E × A) / (Φ × UF × MF).
- **Vertical illuminance** on rack faces matters most. TIA-942 style targets: **500 lux horizontal and 200 lux vertical**, at 1 m above the floor in the aisle.
- Standards: **EN 12464-1** (workplace lighting), **EN 1838** (emergency lighting), **EN 50172 / ISO 30061** (emergency systems), **EN 60598-2-22** (emergency luminaires), **TIA-942**.
- **LED** is the normal choice. Watch **driver heat** (hot aisles), **flicker** and **EMC**, and remember that **lighting load becomes heat**.
- Place fixtures **over the aisles**, **parallel to the rows**, on **circuits separate from IT**, alternated across circuits, normally **not on the UPS**.
- Use **three-level control** (low, walking, full) and **occupancy sensors**, with a **maintenance override**.
- **Emergency lighting (EN 1838):** **1 lux** on escape routes (centre line), **0.5 lux** in open areas, **10% or 15 lux minimum** for high-risk tasks. **40 : 1** uniformity. **50% in 5 s, 100% in 60 s**. At least **1 hour** (often 3).
- Place emergency luminaires at **exits, stairs, direction changes, junctions, level changes, exit signs, call points, fire equipment and first aid**, with at least **two per compartment**.
- **Generator start (10 to 15 s) is too slow** for emergency lighting, so luminaires use **batteries**.
- Test **monthly (function)** and **annually (full duration)**, and keep a log.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **EN 12464-1**, **EN 12665**, **EN 15193** | Workplace lighting levels, definitions, lighting energy performance |
| **EN 60598** (including **-2-22**) | Luminaire safety and emergency luminaires |
| **ANSI/TIA-942** | Computer room targets: 500 lux horizontal, 200 lux vertical at 1 m above the floor |
| **EN 50600-2-1**, **ISO/IEC 22237-2** | Building provisions |
| **EN 1838** | Emergency lighting values: 1 lux, 0.5 lux, 15 lux or 10%, 40:1 uniformity, 50% in 5 s and 100% in 60 s, one hour minimum |
| **EN 50172 / ISO 30061** | Emergency escape lighting systems, testing and records |
| **BS 5266-1** | The 3-hour duration |
| **NFPA 101**, International Building Code | The US 90-minute egress lighting figure |
| **NFPA 70** (NEC) Article 700 | Emergency systems wiring |
| **CIE** photometry | Illuminance, inverse-square and lumen method formulas |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
