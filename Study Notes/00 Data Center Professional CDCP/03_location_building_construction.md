# Module 3: The Data Centre Location, Building and Construction

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section in these notes |
| --- | --- | --- |
| 3.1 | Site Selection Criteria | [Section 1](#31-site-selection-criteria) |
| 3.2 | Location Evaluation | [Section 2](#32-location-evaluation) |
| 3.3 | Building Evaluation | [Section 3](#33-building-evaluation) |
| 3.4 | Holding / Staging Area, Computer Room, Media Storage Area, UPS Room | [Section 4](#34-holding--staging-area-computer-room-media-storage-area-ups-room) |
| 3.5 | Battery Room and Service Corridor | [Section 5](#35-battery-room-and-service-corridor) |
| 3.6 | Standby Generator Area, Meet-Me Room, Security and Facilities Room, NOC | [Section 6](#36-standby-generator-area-meet-me-room-security-and-facilities-room-noc) |
| 3.7 | Classic Mistakes | [Section 7](#37-classic-mistakes) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-3-location-building-and-construction) |

**Objectives (from your slide).** After this module you should be able to describe and understand: some of the criteria for selecting the data centre **location**, some of the criteria for selecting a data centre **facility site / location**, and the various parts of a data centre and its supporting facilities and their function.

> **Conventions.** **[CHECK]** marks a figure from general industry practice or outside research, not from your slides (many come from the TIA-942 family and from building and fire codes). If your course gives a different number, use your course. Codes and standards change, and the local code always wins.

## The two levels of selection

Exam questions often test whether you can tell these two levels apart:

| Level | Question it answers | Example criterion |
| --- | --- | --- |
| **Location** (macro) | Which country, region or city? | Data sovereignty law |
| **Site** (micro) | Which exact plot or building? | Distance to a chemical plant |

Site selection is mostly **risk avoidance**. A bad location cannot be fixed later with redundancy, so evaluate it first.

---

# 3.1 Site selection criteria

## 1. The selection process

| Step | What happens |
| --- | --- |
| 1. **Define requirements** | Size, power (MW), availability class or Tier, latency, budget, timeline, growth |
| 2. **Long list** | Many candidate regions or sites |
| 3. **Knock-out screening** | Remove any candidate with a "deal-breaker" (for example a flood plain) |
| 4. **Detailed evaluation** | Score the remaining candidates against weighted criteria |
| 5. **Due diligence** | Surveys, utility letters, legal checks, permits |
| 6. **Decision** | Choose, with a documented rationale |

## 2. The main criteria

### Location criteria (macro level)

| Criterion | What to consider |
| --- | --- |
| **Natural hazards** | Earthquake, flood, hurricane, tornado, volcanic and wildfire risk |
| **Political and economic stability** | Stable government, low risk of unrest or sudden regulation changes |
| **Legal and regulatory** | Data sovereignty and privacy laws, where data is legally allowed to be stored, export and sanctions rules |
| **Power** | Reliable, affordable grid with spare capacity. Energy price, carbon footprint, availability of renewables |
| **Telecommunications** | Multiple carriers, diverse fibre routes, internet exchanges, latency to users |
| **Climate** | Cool climate enables free cooling and better efficiency. Water availability matters for water-cooled designs |
| **Labour** | Skilled staff, salaries, cost of living |
| **Incentives and costs** | Tax breaks, land and construction costs |
| **Proximity** | To customers (latency) and to the primary or DR partner site |
| **Disaster recovery** | Far enough from the other site not to share the same risks |

### Site criteria (micro level)

| Criterion | What to consider |
| --- | --- |
| **Surroundings** | Avoid airports, chemical plants, fuel depots, highways, railways, transmitters |
| **Local flood risk** | Not in a flood plain or low-lying, good drainage |
| **Utilities at the site** | Two independent power feeds (different substations), water, diverse telecom entry points, gas if needed |
| **Access** | Roads for heavy equipment and fuel deliveries, emergency services nearby, staff access |
| **Space** | Room for the building, generators, fuel tanks, chillers, and expansion |
| **Security** | A site that can be fenced, monitored and kept low-profile |
| **Zoning and permits** | Planning permission, noise limits (generators), building codes |
| **Neighbours** | Their fire, water and access risks become yours |

## 3. Recommended distances (examples) **[CHECK]**

The TIA-942 family gives example separation distances for higher-rated sites. Values vary by edition and rating, so use them as examples:

| Hazard | Example recommendation |
| --- | --- |
| Inland waterway | More than about 0.8 km away |
| Coastal waterway | More than about 8 km away |
| Major highway | More than about 273 m away |
| Major airport | Between about 1.6 km and 48 km (not under the flight path, but not too remote) |
| Generator and fuel storage from public areas | At least about 9 m (Tier 3) or 19 m (Tier 4) |

## 4. Weighted scoring

Because no site is perfect, candidates are scored against weighted criteria.

**Worked example.** Seven criteria with weights summing to 100, scored 1 (poor) to 5 (excellent):

| Criterion | Weight | Site A score | Site A weighted | Site B score | Site B weighted |
| --- | --- | --- | --- | --- | --- |
| Natural hazards | 25 | 4 | 100 | 5 | 125 |
| Power | 20 | 5 | 100 | 3 | 60 |
| Network | 15 | 3 | 45 | 5 | 75 |
| Security | 10 | 4 | 40 | 3 | 30 |
| Cost | 10 | 2 | 20 | 4 | 40 |
| Expansion | 10 | 4 | 40 | 2 | 20 |
| Access | 10 | 3 | 30 | 4 | 40 |
| **Total (max 500)** | | | **375 (75%)** | | **390 (78%)** |

Site B scores slightly higher, but two rules apply:

- A **knock-out criterion** (for example "in a flood plain") overrides the score entirely.
- Weights reflect the **customer's priorities**. A latency-sensitive trading firm weights proximity far higher.

---

# 3.2 Location evaluation

Evaluation turns criteria into **evidence**. It combines a desktop study, data requests and site visits.

## 1. Natural hazard evaluation

| Hazard | How to evaluate |
| --- | --- |
| **Flood** | Official flood maps, history, river and coastal data. Check the probability, for example a "100-year flood" |
| **Earthquake** | Seismic hazard maps and zone classifications |
| **Wind and storms** | Wind speed maps, tornado and hurricane history |
| **Lightning** | Lightning flash density maps |
| **Extreme temperatures** | Climate data (affects cooling design) |
| **Wildfire, landslide, volcano** | Regional hazard maps |

**Worked example: understanding "100-year flood".** It means a **1% chance in any given year**, not "once in 100 years". Over a 30-year facility life:

```
Probability of at least one such flood = 1 − (0.99)^30 = 1 − 0.74 = about 26%
```

Over 50 years it is about **39.5%**. A "100-year" flood zone is a real risk for a long-lived facility.

## 2. Utility evaluation

| Item | What to check |
| --- | --- |
| **Power capacity** | Available MW now and in future, with a written confirmation from the utility |
| **Power reliability** | Outage statistics: **SAIFI** (how often customers lose supply) and **SAIDI** (how long, on average) |
| **Feed diversity** | Two feeds from different substations and routes |
| **Water** | Capacity and quality, if cooling needs it |
| **Telecom** | Number of carriers, fibre routes, whether they are truly **diverse** (not sharing a duct or bridge) |
| **Fuel and gas** | Delivery routes for generator fuel |

**Definitions:** **SAIFI** = System Average Interruption Frequency Index (interruptions per customer per year). **SAIDI** = System Average Interruption Duration Index (minutes of interruption per customer per year).

## 3. Surroundings and neighbours

- **Hazardous neighbours:** chemical plants, fuel depots, gas pipelines, airports, railways, highways, military sites.
- **EMI sources:** radio, radar and TV transmitters, power substations and high-voltage lines (links to Module 7).
- **Adjacent land use:** future development, neighbouring tenants, noise sensitivity.
- **Crime and security:** local crime rates, ease of securing the perimeter.
- **Emergency services:** distance and response time of fire and police.

## 4. Practical evaluation methods

| Method | Use |
| --- | --- |
| **Desktop study** | Maps, public data, utility records |
| **Checklist** | Consistent comparison between candidates |
| **Site visit** | Check what maps don't show: access roads, neighbours, drainage |
| **Interviews** | Utility, carriers, local authority, emergency services |
| **Risk matrix** | Rank hazards by likelihood and impact |
| **Specialist surveys** | Soil, flood, seismic, EMI |

## 5. DR site considerations

- The DR site should not share the **same flood zone, power grid, seismic zone, or carrier** as the primary.
- **Synchronous replication** limits distance (latency), while **asynchronous** replication allows longer distances. Many organisations use a nearby site for synchronous replication and a distant site for protection against regional disasters.

---

# 3.3 Building evaluation

Once the site is chosen, the **building** is evaluated: an **existing building** to convert, or a **new build**.

## 1. New build vs. existing building

| | New build | Existing building (conversion) |
| --- | --- | --- |
| Design freedom | Full | Limited by the structure |
| Cost and time | Higher cost, longer | Often cheaper and faster, if suitable |
| Risk | Fewer surprises | Hidden problems (structure, pipes, roof) |
| Typical issue | Cost | Floor loading, ceiling height, risers, neighbours |

## 2. What to evaluate in a building

| Area | Questions |
| --- | --- |
| **Structure** | Floor loading, column spacing, slab-to-slab height, roof strength (for chillers and generators) |
| **Location of the computer room** | Not in the basement or top floor, no windows, no pipes overhead |
| **Tenancy** | Dedicated building, or shared (neighbours' fire, water and access risks) |
| **Utilities** | Power capacity and routes, water, telecom entry points (at least two), risers and shafts |
| **Space for plant** | Room for UPS, batteries, generators, fuel, chillers and expansion |
| **Access** | Loading dock, freight lift, wide doors and corridors, a route for large equipment |
| **Fire** | Compartmentation, fire ratings, suppression possibilities |
| **Security** | Perimeter, setback from the road, controlled entrances |
| **Compliance** | Zoning, building codes, permits, noise limits |

## 3. Key dimensions **[CHECK]**

| Item | Typical requirement |
| --- | --- |
| **Floor loading** | **ANSI/TIA-942-C** sets a minimum floor loading of **5 kPa (100 lbf/ft²)** for computer rooms under 20 m². Heavy racks and larger rooms need a structural assessment |
| **Clear ceiling height** | At least **2.6 m** above the raised floor |
| **Doors** | At least about **1.07 m (3.5 ft)** wide, and often **1.2 m × 2.4 m** in practice, with no centre post |
| **Fire rating of computer room walls** | Commonly **1 hour minimum**, with **2 hours** for higher-rated sites |
| **Windows** | None in the critical area |
| **Roof** | Waterproof, well drained, with lightning protection |

### Worked example: slab-to-slab height

| Layer | Height |
| --- | --- |
| Raised floor | about 0.6 m |
| Clear height above the raised floor | at least 2.6 m |
| Ceiling void (ducts, trays, detectors) | about 0.6 m |
| **Total slab to slab (minimum)** | **about 3.8 m** |

A comfortable design is often **4.5 to 5 m** slab to slab **[CHECK]**. An existing office building with a 3.0 m floor-to-floor height simply cannot host a proper computer room.

### Worked example: floor loading

Rack fleet: **100 racks at 1,200 kg** in a **450 m²** room.

```
Total weight = 100 × 1,200 kg = 120,000 kg
Average load = 120,000 × 9.81 / 450 = about 2,616 N/m² = 2.6 kPa
```

The **average** is well under the 5 kPa minimum, but the load is **not** spread evenly. It sits on rack feet, so the **concentrated and rolling loads** (Module 4) and the slab's local capacity decide. Also add cooling units, cabling and the raised floor itself.

## 4. Why slab-to-slab walls?

A wall that stops at the false ceiling leaves a path for **fire, smoke, dust and intruders** above it. Computer room walls run from the structural slab below to the structural slab above.

---

# 3.4 Holding / staging area, computer room, media storage area, UPS room

## 1. Holding / staging area

| Aspect | Detail |
| --- | --- |
| **Purpose** | Receive, unpack, hold, assemble, configure and test equipment **before** it enters the live computer room, and hold outgoing equipment |
| **Location** | Next to the loading dock, with a controlled route to the computer room |
| **Why separate** | Keeps **dust, cardboard, packaging and pests** out of the white space and limits the fire load. Also controls who enters |
| **Features** | Work benches, rack assembly space, power outlets, a test or **burn-in** area, anti-static flooring, secure storage, disposal area for packaging |
| **Size** | Large enough to stage several racks at once (they arrive in large crates), with a landing platform and ramp where floors differ |
| **Environment** | Allows equipment to **acclimatise** to room temperature and humidity before powering up, avoiding condensation |
| **Condition** | Clean, with access control and CCTV |

## 2. Computer room (white space)

| Aspect | Requirement |
| --- | --- |
| **Purpose** | House the IT equipment in racks, with its power and cooling distribution |
| **Shape** | Rectangular, with **few or no columns**, for flexible rack layout |
| **Location** | Not on the top floor or in the basement, away from external walls and pipes, no windows |
| **Sizing** | Rule of thumb about **4 to 5 m² per rack** including aisles and clearances **[CHECK]**. For example, 100 racks × 4.5 m² = **450 m²** |
| **Aisles** | Hot and cold aisle layout. Allow **front clearance of about 1.2 m** and **rear about 0.9 m** at minimum **[CHECK]** |
| **Floor** | Raised floor or slab, with the loading above (Module 4) |
| **Ceiling** | At least 2.6 m clear, suspended ceiling if used for return air |
| **Walls and doors** | Fire-rated, slab to slab, doors big enough for racks |
| **Environment** | Controlled temperature and humidity, dust-free. **Pre-action sprinklers or gas suppression**, with early smoke detection |
| **Services** | Power, cooling, cabling, lighting, earthing and bonding (Module 6) |
| **What stays out** | Storage of cartons, offices and any non-essential activity |
| **Security** | Access control, CCTV, often a man-trap |

## 3. Media storage area

| Aspect | Detail |
| --- | --- |
| **Purpose** | Store backup tapes, disks and other removable media, and sometimes the tape library |
| **Location** | **Separate from the computer room**, in its own fire compartment, so a fire in the computer room does not destroy the backups |
| **Environment** | Temperature and humidity controlled (media is sensitive), clean, away from magnetic fields (Module 7) |
| **Fire protection** | Fire-rated enclosure, or a **fire-rated media safe**. Gas suppression is common **[CHECK]** |
| **Security** | Controlled access, logging of who removes media, often a vault |
| **Practice** | Keep at least one copy **off-site**, rotating media on a schedule |

## 4. UPS room

| Aspect | Detail |
| --- | --- |
| **Purpose** | House the UPS modules and their switchgear (batteries are normally in a **separate battery room**, see 3.5) |
| **Location** | Next to the electrical room, close to the computer room (short, low-loss runs), and **A and B in separate rooms** (separate fire compartments) in a 2N design |
| **Floor loading** | UPS cabinets are heavy, so the slab must be checked |
| **Cooling** | UPS units **lose energy as heat**, which must be removed |
| **Clearance** | Service access around each cabinet, as the manufacturer and electrical code require |
| **Fire** | Fire-rated enclosure and detection |
| **Other** | Cable entries, noise, access for large equipment |

**Worked example: UPS heat.** A UPS supplies **500 kW** at **96% efficiency**:

```
Input power = 500 / 0.96 = 520.8 kW
Heat released = 520.8 − 500 = about 20.8 kW
```

The UPS room needs cooling for **about 21 kW**, even before counting batteries and switchgear. This is also why UPS efficiency affects **PUE**.

---

# 3.5 Battery room and service corridor

## 1. Battery room

### Battery types

| Type | Characteristics | Main hazards |
| --- | --- | --- |
| **Flooded (vented) lead-acid** | Long life, needs maintenance and ventilation | **Hydrogen** gas, **sulphuric acid** spills |
| **VRLA** (valve-regulated lead-acid) | Sealed, common in UPS, shorter life | Hydrogen vented during charging, acid if damaged |
| **Lithium-ion** | Compact, long life, fast recharge | **Thermal runaway**, flammable and toxic off-gas, fire |

### Hazards in any battery room

- **Hydrogen** (lead-acid): flammable, explosive range starts at **4% by volume**.
- **Acid** (lead-acid): corrosive, burns and spills.
- **Electrical:** DC strings keep their stored energy even with every breaker open, so there are **shock and arc-flash** risks.
- **Heat and fire:** especially for lithium-ion.

### Requirements **[CHECK]**

| Area | Requirement |
| --- | --- |
| **Dedicated room** | Separate from the computer room and UPS room, in its own fire compartment |
| **Fire separation** | Fire-rated walls and doors (commonly 1 to 2 hours, depending on code and battery type) |
| **Ventilation** | Lead-acid: ventilation to keep hydrogen **below 1% by volume** (a quarter of the 4% lower flammable limit). Codes also commonly set about **1 CFM per ft²** (about 5 l/s per m²) of floor area |
| **Lithium-ion** | Governed by **NFPA 855**: off-gas detection (commonly at 25% of the lower flammable limit), explosion control, separation and spacing, and limits such as about **600 kWh per fire area** in non-dedicated buildings (check the edition your authority adopts) |
| **Location** | Not below ground for lithium-ion unless approved. Not under toilets, water pipes or places that leak |
| **Temperature** | About **20 to 25 °C**. Heat shortens lead-acid battery life sharply (a common rule of thumb: life roughly halves for every 8 to 10 °C above 25 °C) |
| **Floor loading** | Battery strings and racks are very heavy |
| **Acid spill control** | Spill containment, neutralising material, **eyewash and emergency shower** |
| **Racking** | Seismic-rated racks where needed, with insulated tools and clear aisles |
| **Safety** | Warning signs, restricted access, **emergency power off (EPO)**, hydrogen or off-gas detection, fire detection and extinguishing suited to the battery type |
| **Backup for safety systems** | Detection and ventilation have to keep working in a power failure |

**Hydrogen check:** the lower flammable limit of hydrogen is **4%**. The design target of **1%** is exactly **25% of that limit**, a 4 : 1 safety margin.

**Life safety note:** statistics show that major data centre fires have been increasing, with lithium-ion UPS batteries a contributing factor. Battery chemistry is now a **room planning decision**, not just a procurement detail.

## 2. Service corridor

| Aspect | Detail |
| --- | --- |
| **Purpose** | A route to move equipment, supplies and people between loading dock, technical rooms and the computer room **without passing through other critical spaces** |
| **Why** | Heavy items (UPS cabinets, battery racks, chillers, racks) need a clear, direct route, and visitors and contractors can be kept away from the white space |
| **Width and height** | Wide and tall enough for the largest item on a pallet jack or trolley, commonly **2 m or more** wide **[CHECK]**. Doors and turns must also fit |
| **Floor** | Strong enough for heavy equipment, level, with ramps and landing platforms at changes of level |
| **Fire** | Fire-rated, with clear escape routes and emergency lighting |
| **Services** | Often carries pipes, cable trays and busway between rooms |
| **Security** | Controlled access with CCTV and card readers |
| **Position** | Between the support areas and the computer room, often acting as a **buffer** or fire break |

---

# 3.6 Standby generator area, meet-me room, security and facilities room, NOC

## 1. Standby generator area

| Aspect | Requirement |
| --- | --- |
| **Purpose** | House the generators and their fuel supply for long outages |
| **Location** | Usually **outdoors** (in weatherproof enclosures) or in a dedicated room, **not adjacent** to the computer room |
| **Setback** | Away from public areas to protect against vehicle impact and tampering, for example about **9 m (Tier 3) or 19 m (Tier 4)** in the TIA-942 family **[CHECK]** |
| **Air intake and exhaust** | Exhaust must not be drawn back into **air intakes** of the generators, the building or the cooling plant |
| **Noise** | Attenuation and permits, since generators are loud, especially near homes |
| **Fuel storage** | A **day tank** near each generator and a **main tank**, with **secondary containment**, leak detection and a safe delivery route for tankers |
| **Fire** | Fire separation from the building, protection and detection, fuel fire controls |
| **Flood** | Placed above flood level |
| **Start time** | About **10 to 15 seconds** to pick up the load **[CHECK]** |
| **Testing** | Regular on-load tests (often monthly), with records |
| **Access** | For maintenance and for replacement of large components |

**Worked example: fuel for a 1,000 kW generator** at full load, using about **0.26 litres per kWh** **[CHECK]**:

```
Consumption = 1,000 kW × 0.26 L/kWh = 260 L/hour
12 hours: 260 × 12 = 3,120 litres
72 hours: 260 × 72 = 18,720 litres
```

Required autonomy depends on the target rating and the **fuel resupply contract**. Many higher-rated sites require 12 hours or more of fuel on site, and some require 72 hours or more **[CHECK]**.

## 2. Meet-me room (MMR)

| Aspect | Detail |
| --- | --- |
| **What it is** | A secure room where **telecom carriers, network providers and customers** connect to each other, usually by **cross-connects** |
| **Why** | Lets customers interconnect directly inside the building instead of buying long circuits. Typical of **carrier-neutral colocation** facilities |
| **Relation to the entrance room** | The entrance room is where carrier cables **enter and terminate**. The meet-me room is where different parties **interconnect**. In many facilities the roles are combined or adjacent |
| **Location** | Separate from the computer room, with controlled access |
| **Resilience** | **Two** meet-me rooms (or two entrance rooms), with diverse routes, are typical in higher-rated sites |
| **Features** | Cross-connect fields, carrier cages, fibre management, power, cooling, security and CCTV |

## 3. Security room

| Aspect | Detail |
| --- | --- |
| **Purpose** | Control point for **access control and CCTV** monitoring, and for the guard function |
| **Location** | Near the **main entrance**, with a view of visitors and the approach. Sometimes with a security **counter** and a **man-trap** |
| **Features** | Access control servers, CCTV monitors and recorders, alarm panels, visitor logs, and in higher-rated sites **bullet-resistant** walls and glass **[CHECK]** |
| **Resilience** | Backup power for systems, separate from the computer room |

## 4. Facilities room

| Aspect | Detail |
| --- | --- |
| **Purpose** | Base for the **facilities and maintenance** staff |
| **Typical contents** | Tools, spare parts, workshop space, **BMS workstations**, drawings and documentation, test equipment |
| **Location** | Close to the **mechanical and electrical** plant, outside the white space |

## 5. Network operations centre (NOC)

| Aspect | Detail |
| --- | --- |
| **Purpose** | Staff **monitor and manage** the IT systems and the facility (and often security) around the clock |
| **Location** | Outside the computer room, with controlled access. Often near the security room |
| **Features** | Video wall and workstations, **BMS and DCIM** screens, communications, ergonomic seating (24/7 staffing), break and rest areas nearby |
| **Resilience** | Dedicated power and connectivity, plus a **backup NOC** at another site in many designs |
| **Why separate** | People and their activity (noise, food, movement) don't belong in the white space |

---

# 3.7 Classic mistakes

| # | Mistake | Why it is a problem | How to avoid |
| --- | --- | --- | --- |
| 1 | **Choosing a site in a flood plain, low-lying area or near a river** | Water is the most common site killer. A "100-year" flood has about a 26% chance over 30 years | Flood maps and knock-out screening |
| 2 | **Putting the computer room in the basement or on the top floor** | Flooding, roof leaks, lightning, heat | Ground or middle floors |
| 3 | **Ignoring neighbours and surroundings** | Hazards from airports, chemical plants, fuel depots, highways, railways, transmitters | Evaluate surroundings, keep distance |
| 4 | **Single utility feed or single carrier** | One cable cut or substation fault stops the site | Two feeds from different substations, two carriers on diverse routes |
| 5 | **Not checking power capacity for growth** | The site cannot expand, or the utility upgrade takes years | Written capacity confirmation, ask about future capacity |
| 6 | **Underestimating floor loading** | Floor cannot take the racks or batteries | Structural check, concentrated and rolling loads |
| 7 | **Low ceiling height** | No room for the raised floor, cooling and cabling | Check slab-to-slab height early |
| 8 | **Windows or external walls on the computer room** | Heat gain, security and weather exposure | Interior placement, no windows |
| 9 | **Water or sewer pipes above the computer room** | Leaks onto live equipment | Keep pipes out of and away from critical areas |
| 10 | **Doors, corridors or lifts too small** | Racks and UPS units cannot be moved in | Check the route and dimensions for the largest items |
| 11 | **No staging area, or one too small** | Unpacking and assembly happens in the white space, bringing dust and fire load | Dedicated staging next to the dock |
| 12 | **Battery room without proper ventilation, fire separation or spill control** | Hydrogen explosion, fire spread, acid injuries | Dedicated room, code-compliant ventilation and protection |
| 13 | **Generator exhaust drawn into air intakes** | Engine fumes reach the cooling plant and the building | Place intakes and exhausts carefully |
| 14 | **Too little fuel storage, no resupply plan** | Generator stops during a long outage | Size fuel for the target autonomy, with a delivery contract |
| 15 | **No service corridor or shared routes** | Equipment moved through critical rooms, visitors near the white space | Separate service routes |
| 16 | **Offices, NOC or storage next to the computer room without separation** | Fire load, noise, traffic and security risk | Separate fire compartments, controlled doors |
| 17 | **Mixing redundancy levels (weakest link)** | Tier III power with Tier II cooling is only Tier II | Design each subsystem to the same level |
| 18 | **Shared building with tenants you don't control** | Their water, fire and access risks affect you | Dedicated building where possible |
| 19 | **Ignoring noise and permits** | Planning refusal or complaints, especially for generators | Check zoning and noise limits early |
| 20 | **No room for expansion** | Phased growth impossible, forced relocation | Land and utility headroom, modular design |
| 21 | **Services entering at several scattered points** | Complicates bonding, security and lightning protection | Few, controlled entry points, bonded together |
| 22 | **Forgetting maintenance access** | Equipment cannot be serviced or replaced safely | Clearances, lifting routes, concurrent maintainability |
| 23 | **Poor commissioning and documentation** | Faults found only in live operation | Integrated systems tests, as-built records |
| 24 | **Treating redundancy as a substitute for good siting** | A bad location cannot be fixed with extra equipment | Evaluate the site first |
| 25 | **Underestimating future power density** | Cooling and power limits reached early | Plan capacity and floor loading for higher densities |

**Pattern to remember:** most classic mistakes come from **deciding too quickly on cost or convenience** and discovering the physical constraints (water, structure, access, utilities, neighbours) too late.

---

## Glossary

| Term | Meaning |
| --- | --- |
| Location / site | Macro (region) / micro (plot) level |
| Knock-out criterion | A deal-breaker that removes a candidate |
| SAIFI / SAIDI | Utility outage frequency / duration indices |
| White space / grey space | IT area / support area |
| Staging area | Where equipment is received and prepared |
| Meet-me room | Where carriers and customers interconnect |
| Entrance room | Where carrier cables enter and terminate |
| NOC | Network operations centre |
| EPO | Emergency power off |
| Day tank | Small fuel tank next to a generator |
| LFL | Lower flammable limit |

## Exam takeaways

- **Location** = macro. **Site** = micro. Give examples of each.
- Site selection is **risk avoidance**, with **knock-out criteria** first and **weighted scoring** after.
- **Water** is the most common site killer. A "100-year flood" is a **1% chance per year**.
- Evaluate utilities (**SAIFI/SAIDI**, feed diversity) and carrier **diversity**.
- Computer room: **no windows, not basement or top floor, no pipes overhead, slab-to-slab walls**, at least about **2.6 m clear height**, floor loading of at least **5 kPa** for small computer rooms (TIA-942-C).
- The **staging area** keeps dust and packaging out of the white space.
- The **media storage area** is separate, fire-rated and climate-controlled.
- **Battery rooms** are dedicated, ventilated (hydrogen below 1%), fire-separated, with spill control and eyewash. **Lithium-ion** follows NFPA 855.
- The **service corridor** moves heavy equipment without crossing critical rooms.
- **Generators:** outdoors or separate, setback from public areas, exhaust away from intakes, fuel storage sized for autonomy.
- **Meet-me room** = interconnection point. **Entrance room** = where carrier cables enter.
- **Classic mistakes** come from rushing and discovering physical constraints too late.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **ANSI/TIA-942-C** (2024) | Minimum floor loading (5 kPa for computer rooms under 20 m²) |
| **TIA-942** family | Example distances from hazards, ceiling height, door width, wall fire ratings |
| **EN 50600-2-1**, **EN 50600-2-5**, **ISO/IEC 22237** | Building construction and security classes |
| **NFPA 855** (2026) | Lithium-ion battery rooms |
| Fire and building code hydrogen limit | Lead-acid battery room ventilation (1% by volume, a quarter of the 4% lower flammable limit) |
| **IEEE 1366** | SAIFI and SAIDI definitions |
| Basic statistics and physics | Flood probability, floor load, UPS heat and generator fuel examples (arithmetic) |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
