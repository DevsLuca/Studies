# Module 9: Cooling Infrastructure

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section |
| --- | --- | --- |
| 9.1 | Cooling: Basic Principles | [Section 1](#91-cooling-basic-principles) |
| 9.2 | Comfort Cooling versus Precision Cooling | [Section 2](#92-comfort-cooling-versus-precision-cooling) |
| 9.3 | Refrigerant Circuit and Refrigerants | [Section 3](#93-refrigerant-circuit-and-refrigerants) |
| 9.4 | Types of Cooling Systems I | [Section 4](#94-types-of-cooling-systems-i-direct-expansion) |
| 9.5 | Types of Cooling Systems II | [Section 5](#95-types-of-cooling-systems-ii-chilled-water-and-free-cooling) |
| 9.6 | Cooling: Up Flow or Down Flow | [Section 6](#96-cooling-up-flow-or-down-flow) |
| 9.7 | Cooling: Raised Floor vs. Non-Raised Floor | [Section 7](#97-cooling-raised-floor-vs-non-raised-floor) |
| 9.8 | Raised Floor Cooling I | [Section 8](#98-raised-floor-cooling-i) |
| 9.9 | Raised Floor Cooling II | [Section 9](#99-raised-floor-cooling-ii) |
| 9.10 | Non-Raised Floor Cooling | [Section 10](#910-non-raised-floor-cooling) |
| 9.11 | Supplemental Cooling | [Section 11](#911-supplemental-cooling) |
| 9.12 | Containment Principle | [Section 12](#912-containment-principle) |
| 9.13 | Containment: Possible Impact on Fire Suppression | [Section 13](#913-containment-possible-impact-on-fire-suppression) |
| 9.14 | Cold Aisle versus Hot Aisle Containment | [Section 14](#914-cold-aisle-versus-hot-aisle-containment) |
| 9.15 | Liquid Cooling | [Section 15](#915-liquid-cooling) |
| 9.16 | Seasonal Thermal Energy Storage (STES) | [Section 16](#916-seasonal-thermal-energy-storage-stes) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#lessons-91-to-916) |

**Objectives (from your slide).** After this module you should be able to describe and understand:

- The trends in heat loads and the problems it poses to mission critical sites and its equipment
- The various air-conditioning types with its pros and cons
- Cooling units
- Raised floor and non-raised floor cooling
- The various techniques that can be used for high density cooling requirements
- Cold- and hot aisle containment
- Seasonal Thermal Energy Storage (STER)

| Objective | Where it is covered |
| --- | --- |
| **Trends in heat loads and the problems they pose** | 9.1 (and the introduction below) |
| **Air-conditioning types, pros and cons** | 9.2, 9.3, 9.4, 9.5 |
| **Cooling units** | 9.4, 9.5, 9.6, 9.10, 9.11 |
| **Raised floor and non-raised floor cooling** | 9.6, 9.7, 9.8, 9.9, 9.10 |
| **Techniques for high density cooling** | 9.11, 9.12, 9.15 |
| **Cold and hot aisle containment** | 9.12, 9.13, 9.14 |
| **Seasonal thermal energy storage** | 9.16 (the slide writes the acronym "STER"; the technology is usually abbreviated **STES**) |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Only the **objectives slide** was available for this module (not the lesson slides), so check the glossary and figures against your course. I could not see how your course splits "Types of Cooling Systems I and II", so I took **I as direct expansion (CRAC) systems** and **II as chilled water systems and free cooling**. The thermal physics behind this module (heat, specific heat, the airflow equation, dew point, COP, fan laws) is explained step by step in `09a_thermal_physics_foundations.md`. Related earlier material: raised floors (Module 4), racks and blanking panels (Module 8), PUE and sustainability (Module 6), fire protection (Module 12) and monitoring (Module 14).

## The big picture

Every watt that enters the IT equipment leaves as heat, so the cooling system has to remove **as much heat as the IT load draws, continuously**. The heat travels along a chain:

```
Chip → server air or liquid → rack → room air or rack loop → cooling unit (CRAC, CRAH, in-row, door)
     → refrigerant or chilled water → heat rejection (condenser, cooling tower, dry cooler) → outdoors
```

Cooling is usually the **second largest energy consumer** after the IT equipment itself, so it dominates the facility's **PUE**, its **availability** (a cooling failure stops the site within minutes) and, increasingly, its **water and refrigerant footprint**.

---

# 9.1 Cooling: basic principles

## 1.1 Trends in heat load

| Trend | Evidence **[CHECK]** |
| --- | --- |
| **Rising typical density** | The Uptime Institute's 2026 survey reports the most common (modal) rack density at **11 kW**, up from 9 kW in 2025 |
| **More high-density racks** | **24%** of respondents now have some racks at **30 kW or above** (19% in 2025), and about **one in seven** have racks above **50 kW**, some above 100 kW |
| **AI racks far above the average** | A current rack-scale AI system such as the **NVIDIA GB200 NVL72 is rated at about 120 kW** (observed up to about 132 kW) and the **GB300 NVL72 at up to 142 kW**. Announced next-generation racks go well beyond 200 kW |
| **Chip power** | Processors and accelerators have risen from about 100 W to **over 1,000 W** each, so the heat per square centimetre of silicon exceeds what fans can practically remove |
| **The market is split** | Most existing halls were designed for 5 to 15 kW per rack, while purpose-built AI halls run 100 kW or more. Any "average" depends on which population it measures |
| **Rule-of-thumb limits** | Room-level air cooling works up to about **15 to 20 kW per rack** with good containment. Rear-door and in-row units extend it to about **35 to 50 kW**. Above that, liquid cooling is the practical answer |

**Worked example: what density does to a hall.** One megawatt of IT load:

```
At 11 kW per rack:   1,000 / 11  = about 91 racks
At 130 kW per rack:  1,000 / 130 = about 7.7 racks
```

The same megawatt occupies a tenth of the floor, but all the heat is concentrated in a small area.

## 1.2 Problems that heat causes

| Problem | Effect on the site and the equipment |
| --- | --- |
| **Hot spots** | Locally high inlet temperatures. Servers throttle or shut down |
| **Recirculation and bypass** | Hot exhaust re-enters inlets, and cold air returns to the cooling unit without cooling anything (9.12) |
| **Reduced equipment life and reliability** | Higher temperatures accelerate component ageing and raise failure rates |
| **Thermal throttling** | Processors slow down to protect themselves, so the investment delivers less computing |
| **Short thermal ride-through** | A cooling failure heats the room within seconds to minutes (see the example below) |
| **Capacity limits** | Cooling, not floor space, often limits how many racks a hall can hold |
| **Energy cost and PUE** | Cooling is a large share of energy use |
| **Water and refrigerant use** | Evaporative cooling consumes water. Refrigerants have a climate impact |
| **Cooling-related outages** | Cooling is a recurring cause of data centre outages (reported at about 19% of outages in the Uptime Institute's 2024 data **[CHECK]**) |

**Worked example: how fast does a room heat up?** A hall of **500 m² with a 3 m ceiling** (1,500 m³ of air) carries **500 kW** of IT load and loses all cooling:

```
Air mass        = 1,500 m³ × 1.2 kg/m³ = 1,800 kg
Heat capacity   = 1,800 kg × 1.005 kJ/kg·K = 1,809 kJ/K
Heating rate    = 500 kW / 1,809 kJ/K = 0.276 K per second = about 16.6 K per minute
Time for +25 K  = 25 / 0.276 = about 90 seconds
```

The mass of the building and equipment slows the rise in practice, but the lesson is clear: **thermal ride-through is measured in seconds to minutes**, so cooling needs redundancy and often its own backup power and thermal storage (9.5).

## 1.3 Heat basics

| Principle | Detail |
| --- | --- |
| **Energy conservation** | Electrical power in = heat out. **1 kW of IT load produces 1 kW of heat** |
| **Heat transfer modes** | **Conduction** (through solids), **convection** (moving air or liquid), **radiation**. Data centre cooling is almost entirely convection |
| **Sensible heat** | Heat that changes the **temperature** of air. Servers release almost **only sensible heat** |
| **Latent heat** | Heat that changes the **moisture** content (condensing water out of the air). Servers release none |
| **Sensible heat ratio (SHR)** | Sensible cooling ÷ total cooling. Near 1.0 in a data hall |
| **Units** | **1 kW = 3,412 BTU/h.** **1 ton of refrigeration = 3.517 kW = 12,000 BTU/h** |

### The two heat-transfer equations

```
Q = ṁ × c_p × ΔT        heat (kW) = mass flow (kg/s) × specific heat (kJ/kg·K) × temperature rise (K)
Airflow  (m³/s) = Q / (1.2 × 1.005 × ΔT)        (air: 1.2 kg/m³, 1.005 kJ/kg·K)
Water    (kg/s) = Q / (4.186 × ΔT)              (water: 4.186 kJ/kg·K)
```

| Case | Calculation | Result |
| --- | --- | --- |
| **Air for 1 kW at ΔT 10 K** | 1 / (1.206 × 10) | **0.083 m³/s** = 299 m³/h = about **176 CFM** |
| **Water for 1 MW at ΔT 5 K** | 1,000 / (4.186 × 5) | **47.8 kg/s** = about **172 m³/h** |
| **Water vs. air** | water 4,186 kJ/m³·K ÷ air 1.206 kJ/m³·K | Water carries about **3,500 times** more heat per unit volume |

This ratio is why **liquid cooling** takes over at high densities (9.15).

### The same equation in the three unit systems you will meet

The airflow constant **1.206** is not magic: it is **density × specific heat of standard air** (1.2 kg/m³ × 1.005 kJ/kg·K), the heat that **one cubic metre of air carries per kelvin of warming**. Data sheets use different units, so the constant looks different:

| Unit system | Equation | Constant built from |
| --- | --- | --- |
| **SI** (kW, m³/s, K) | Q = 1.206 × V̇ × ΔT | 1.2 × 1.005 |
| **Europe** (W, m³/h, K) | Q = 0.335 × V̇ × ΔT (often 0.33) | 1.206 × 1,000 ÷ 3,600 |
| **US** (BTU/h, CFM, °F) | **BTU/h = 1.08 × CFM × ΔT** | 60 × 0.075 lb/ft³ × 0.24 BTU/lb·°F |
| **US, in kW** | **CFM = 3,160 × kW ÷ ΔT (°F)** | 3,412 BTU/h per kW ÷ 1.08 |

A temperature **difference** converts at **1 K = 1.8 °F** (10 K = 18 °F). **Never add 32** to a difference. For 1 kW at a 10 K rise all three give the same airflow: **0.083 m³/s = 299 m³/h = 176 CFM**.

**Airflow per kW is not a fixed rule.** It depends on the temperature rise across the servers (ΔT). Rules of thumb such as 120 to 160 CFM per kW assume a ΔT of about 11 to 15 K. The step-by-step derivation is in `09a_thermal_physics_foundations.md`, section 3.

## 1.4 Efficiency measures

| Measure | Definition | Example |
| --- | --- | --- |
| **COP** (coefficient of performance) | Cooling output ÷ electrical input | A chiller with COP 5 uses **200 kW** of electricity for **1 MW** of cooling |
| **EER** | Cooling (BTU/h) ÷ power (W). **EER = 3.412 × COP** | COP 5 is EER 17.1 |
| **kW per ton** | 3.517 ÷ COP | COP 5 gives **0.70 kW/ton** |
| **PUE** | Total facility energy ÷ IT energy | Cooling adds about 0.2 to 0.6 to PUE depending on the system **[CHECK]** |
| **WUE** | Litres of water per kWh of IT energy | High with evaporative cooling, near zero with dry coolers |

## 1.5 Environmental conditions: ASHRAE TC 9.9

The **ASHRAE Thermal Guidelines** (5th edition, 2021) define the conditions at the **IT equipment inlet** (not the room average):

| Class | Typical equipment | Allowable dry-bulb | Max dew point | Notes |
| --- | --- | --- | --- | --- |
| **Recommended** (A1 to A4) | All air-cooled | **18 to 27 °C** | dew point **-9 to 15 °C**, RH up to 70% | RH limit drops to **50%** where corrosive gases are present |
| **A1** | Enterprise servers and storage, tightly controlled rooms | 15 to 32 °C | 17 °C | RH 8 to 80% |
| **A2** | Mainstream servers | 10 to 35 °C | 21 °C | |
| **A3** | Extended-range equipment | 5 to 40 °C | 24 °C | |
| **A4** | Widest tolerance | 5 to 45 °C | 24 °C | |
| **H1** (high-density air-cooled) | Dense HPC and AI accelerators | recommended **18 to 22 °C**, allowable 5 to 25 °C | 17 °C | Tighter, not wider, than A1 |

Other rules: allowable temperature is derated at altitude above 900 m; rate of change is limited (typically 5 °C per hour for tape, 20 °C per hour for other equipment); no condensation.

- **Recommended** is the range to operate in for the best balance of reliability and energy. **Allowable** is the equipment's warranty range. Operating at the upper end raises fan power and can shorten life.
- **Dew point** replaced relative humidity as the humidity metric: a dew point of -9 °C is enough to control ESD risk without active humidification.
- A hall designed to run warm for free cooling **cannot host H1 equipment** without lowering its supply temperature.
- **ASHRAE 90.4** (2025 edition) is the energy standard for data centres, applying where the IT load is above 10 kW and the density above 20 W/ft².

**Temperature rise across servers** is typically **10 to 20 K** (the US DOE guide cites 5.6 to over 22 K), which is why airflow per kW varies.

## 1.6 Redundancy in cooling

Like power, cooling uses **N, N+1, 2N** (Module 2). Typical arrangements: **N+1 cooling units** in the room (so any unit can fail or be serviced), **N+1 chillers, pumps and heat rejection**, **dual chilled-water loops** for 2N, and **thermal storage** to ride through a power loss (9.5). The cooling units' **fans, pumps and controls** must be on **protected power** or the room overheats before the generator and chillers restart.

---

# 9.2 Comfort cooling versus precision cooling

## 2.1 The difference

| | **Comfort cooling** (office air conditioning, split units) | **Precision cooling** (CRAC, CRAH, in-row) |
| --- | --- | --- |
| **Designed for** | People, in offices and homes | IT equipment, in data halls |
| **Heat type** | Mostly **latent** (people and moisture) plus some sensible | Almost entirely **sensible** |
| **Sensible heat ratio** | About **0.6 to 0.7** | About **0.9 to 1.0** **[CHECK]** |
| **Airflow** | Lower airflow per kW of cooling | **Much higher airflow** per kW (large volume at a small temperature difference) **[CHECK]** |
| **Humidity** | Dehumidifies as a by-product | **Controls** humidity, avoids over-dehumidifying |
| **Operating pattern** | Intermittent, office hours, seasonal | **24 hours, 365 days a year**, whole year |
| **Reliability** | Single compressor, no redundancy | Redundant components (dual circuits, multiple fans), N+1 units, alarms, remote monitoring |
| **Control precision** | Wide (a degree or two, wide RH) | **Tight** temperature and humidity control and fast response |
| **Cost** | Lower | Higher |
| **Capacity per floor area** | One ton per about 250 to 300 ft² of office (**12 to 14 W/ft²**) | One ton per about 50 to 100 ft² of data hall (**35 to 70 W/ft²**), and far higher in modern halls (200 to 300 W/ft²) |

## 2.2 Why comfort cooling fails in a data hall

1. **It over-dehumidifies.** The coil runs cold enough to pull moisture out of the air. The humidifier then has to put it back: a wasteful cycle sometimes called the "humidity war".
2. **It delivers too little airflow** for the heat density, creating hot spots.
3. **It isn't built to run continuously** or to fail gracefully.
4. **It has no redundancy**, so a fault means a shutdown.
5. **Its capacity is rated on total (sensible plus latent) cooling**, but only the sensible part helps an IT load.

**Worked example: sensible capacity.** The IT load is **100 kW** (all sensible):

```
Comfort unit, SHR 0.65:    rated capacity needed = 100 / 0.65 = about 154 kW
Precision unit, SHR 0.95:  rated capacity needed = 100 / 0.95 = about 105 kW
```

The comfort unit must be about **50% larger** to deliver the same useful cooling, and it will still fight the humidity.

## 2.3 What makes a unit "precision"

- **High sensible heat ratio** coils and **high airflow** with **EC (electronically commutated) variable-speed fans**.
- **Humidifier and reheat** for tight humidity control (less needed now that ASHRAE uses dew point).
- **Microprocessor control** with alarms, sensors, and network connection (BMS).
- **Redundant circuits and components**, with units sized N+1.
- **Filtration** and **continuous duty** design.

**Where comfort cooling is acceptable:** offices next to the data hall, small non-critical comms closets, and temporary measures. It should **not** be the primary cooling of critical IT.

---

# 9.3 Refrigerant circuit and refrigerants

## 3.1 The vapour-compression cycle

Cooling by refrigerant uses four components in a closed loop:

```
              high-pressure hot vapour
   ┌───────────► CONDENSER ───────────┐   rejects heat to outdoors / condenser water
   │              (heat OUT)           ▼
 COMPRESSOR                     high-pressure liquid
   ▲                                   │
   │                                   ▼
   │                           EXPANSION VALVE
   │              (heat IN)            │
   └─────────── EVAPORATOR ◄───────────┘   absorbs heat from the room air or water
          low-pressure vapour    low-pressure cold liquid/vapour mix
```

| Component | What it does |
| --- | --- |
| **Evaporator** | The refrigerant boils at low pressure and low temperature, **absorbing heat** from the room air (CRAC coil) or from chilled water (chiller) |
| **Compressor** | Raises the vapour's pressure and temperature. This is where the electrical energy goes. Types: **scroll** (small and medium), **screw**, **centrifugal** (large, including **oil-free magnetic-bearing** designs) |
| **Condenser** | The hot, high-pressure vapour condenses to liquid, **rejecting heat** (plus the compressor's work) to outdoor air, condenser water, or a glycol loop |
| **Expansion device** | Drops the pressure (thermostatic or electronic expansion valve), cooling the refrigerant before it re-enters the evaporator |

**Energy balance:**

```
Heat rejected at the condenser = heat absorbed at the evaporator + compressor work
COP = evaporator cooling output / compressor work
```

**Worked example.** A DX unit gives **100 kW** of cooling with a COP of **4**:

```
Compressor work   = 100 / 4 = 25 kW
Condenser rejects = 100 + 25 = 125 kW
```

### Why "lift" matters

The harder the compressor has to push heat "uphill" (the bigger the temperature difference between evaporator and condenser), the lower the COP. The theoretical limit (Carnot) is:

```
COP_max = T_evaporator / (T_condenser − T_evaporator)      (temperatures in kelvin)
```

| Evaporator | Condenser | COP_max | Real unit at about 55% of the limit |
| --- | --- | --- | --- |
| 10 °C (283 K) | 40 °C (313 K) | 283 / 30 = **9.4** | about **5.2** |
| **15 °C (288 K)** | 40 °C (313 K) | 288 / 25 = **11.5** (**22% higher**) | about 6.3 |

So **raising the chilled-water or air temperature** (allowed by ASHRAE) directly improves efficiency.

## 3.2 Refrigerants

| Refrigerant | GWP (100-year) | ASHRAE 34 safety class | Typical use |
| --- | --- | --- | --- |
| **R-410A** | **2,088** | A1 | The refrigerant in most CRAC and DX units of the past two decades |
| **R-407C** | 1,774 | A1 | Older DX units |
| **R-134a** | **1,430** | A1 | Chillers (screw, centrifugal) |
| **R-32** | **675** | A2L | New DX and air-conditioning equipment |
| **R-454B** | **466** | A2L | New R-410A replacement in DX units |
| **R-513A** | about **630** | A1 | R-134a replacement in chillers |
| **R-1234ze(E)** | about **6** | A2L | Low-GWP chillers (oil-free centrifugal) |
| **R-290 (propane)** | about **3** | A3 | Small packaged units (flammable, charge limited) |
| **Ammonia (R-717)** | 0 | B2L | Large industrial plant (toxic) |

GWP values are the 100-year figures used in the US EPA rules. GWP shows how many times more a kilogram of refrigerant warms the climate than a kilogram of CO₂.

### Safety classes (ASHRAE 34)

| Letter | Toxicity |
| --- | --- |
| **A** | Lower toxicity |
| **B** | Higher toxicity |

| Number | Flammability |
| --- | --- |
| **1** | No flame propagation |
| **2L** | Lower flammability ("mildly flammable": burning velocity below 10 cm/s, hard to ignite) |
| **2** | Flammable |
| **3** | Highly flammable |

**ASHRAE 15** (safety standard for refrigeration systems) and **UL 60335-2-40** set requirements for **leak detection, ventilation and charge limits**, especially for A2L refrigerants indoors. Outdoor air-cooled chillers simplify this, because the refrigerant circuit stays outside the building.

### Regulation **[CHECK]**

| Rule | Effect |
| --- | --- |
| **US EPA Technology Transitions rule (AIM Act)** | New **data centre, computer room air conditioning and IT cooling** equipment must use refrigerants with **GWP of 700 or less** from **1 January 2027**. R-410A (2,088) and R-134a (1,430) are out for new equipment. Existing equipment may keep operating and be serviced |
| **EU F-gas Regulation (EU) 2024/573** (in force since 11 March 2024) | Phases HFC supply down to **zero by 2050** and bans high-GWP HFCs in much new equipment |
| **Montreal Protocol and Kigali Amendment** | International basis for phasing out ozone-depleting substances and then HFCs |

**What the transition means:** R-410A to **R-32 or R-454B** in DX units, and R-134a to **R-513A or R-1234ze(E)** in chillers. The A2L fluids are mildly flammable, so replacement may need **new leak detection, ventilation, installation qualifications and service procedures**. Refrigerants are **not interchangeable** without a full system review.

**Worked example: leak emissions.** A site holds **100 kg** of refrigerant and loses **4% a year**:

| Refrigerant | Calculation | CO₂-equivalent per year |
| --- | --- | --- |
| R-410A | 100 × 0.04 × 2,088 | **8,352 kg** |
| R-454B | 100 × 0.04 × 466 | **1,864 kg** (78% less) |

Refrigerant leakage is a **Scope 1** emission, so GWP and charge size are sustainability issues. **Liquid-cooled and chilled-water designs** keep most of the heat in water and need far less refrigerant.

### Choosing a refrigerant

Low GWP is not the only test. Also consider **energy efficiency, safety class, equipment compatibility, pressure, charge size, leak detection, serviceability, regional regulation and supply**.

---

# 9.4 Types of cooling systems I: direct expansion

## 4.1 CRAC: computer room air conditioner

A **CRAC** is a **self-contained, packaged DX unit** with its **own refrigeration circuit and compressor** inside the cabinet. It cools and conditions the room air and discharges it to the raised floor (or a duct), taking return air from the top or front.

Inside a CRAC: scroll compressor(s) (digital or inverter-driven versions can modulate down to about 20% of capacity), evaporator coil with a high sensible heat ratio, **EC fans**, humidifier and reheat, a microprocessor controller, and often **dual independent circuits** so one compressor failure leaves the unit running at reduced capacity.

## 4.2 Three ways a CRAC rejects heat

| Type | How the heat leaves | Features |
| --- | --- | --- |
| **Air-cooled** | A **remote air-cooled condenser** outdoors, joined by refrigerant pipes | Simplest and cheapest. Limited pipe length and height. Output falls in hot ambient conditions. Noise at the condenser |
| **Water-cooled** | Condenser cooled by **condenser water** from a cooling tower or dry cooler | More efficient than air-cooled. Needs a condenser water loop and water treatment |
| **Glycol-cooled** | Condenser cooled by a **glycol-water loop** to an outdoor dry cooler | No refrigerant pipes outdoors, glycol protects against freezing, can add a **free-cooling coil** that uses cold outdoor air in winter |

## 4.3 Pros and cons

| Pros | Cons |
| --- | --- |
| **No central chilled water plant:** low first cost, quick to install, simple | **Lower efficiency** than a chilled water system at scale: many small compressors |
| **Independent units:** a failure affects only one unit | **Many compressors** to maintain |
| **Good for small halls, edge sites and retrofits** | Limited free cooling (except glycol with a free-cooling coil) |
| Easy to add capacity one unit at a time | **Refrigerant leak risk and regulation** (R-410A phase-out, GWP rules) |
| Self-contained controls | Output derates in hot weather (air-cooled) |
| | Cooling cost can be **0.4 to 0.6 of PUE** in typical designs **[CHECK]** |

**Where CRAC fits:** small data halls (a few hundred kW or less), uniform low density (around 3 to 5 kW per rack), edge sites and locations with no chilled water. Larger facilities generally move to chilled water (9.5).

**Worked example: condenser sizing.** A CRAC delivers **30 kW** of cooling at a COP of **3**:

```
Compressor work   = 30 / 3 = 10 kW
Condenser rejects = 30 + 10 = 40 kW   (the remote condenser must be sized for 40 kW, not 30 kW)
```

---

# 9.5 Types of cooling systems II: chilled water and free cooling

## 5.1 CRAH and the chilled water plant

A **CRAH** (computer room air handler) is a **fan and a chilled-water coil**, with **no compressor**. Chilled water comes from a central **chiller plant**.

```
IT heat → room air → CRAH coil → chilled water loop → CHILLER → condenser water or air → cooling tower / dry cooler
```

| Part | Role |
| --- | --- |
| **CRAH** | Cools the air. Quiet, simple, no refrigerant in the room |
| **Chillers** | Make chilled water. **Air-cooled** (fans reject heat to outdoor air) or **water-cooled** (condenser water to a cooling tower). Compressor types: scroll, screw, **oil-free centrifugal** |
| **Pumps and piping** | Primary and secondary loops, N+1 or 2N |
| **Heat rejection** | **Cooling towers** (evaporative, use water), **dry coolers** (air only, no water), adiabatic-assisted |
| **Thermal storage tanks** | Chilled water ride-through (below) |

**Traditional chilled-water temperatures** are about **7 °C supply, 12 °C return**. Raising the supply to **10 to 15 °C** greatly increases the **free-cooling hours** **[CHECK]**.

## 5.2 CRAC vs. CRAH

| | **CRAC (DX)** | **CRAH (chilled water)** |
| --- | --- | --- |
| **Compressor** | In every unit | Central chillers only |
| **Efficiency at scale** | Lower | **Higher** (large chillers, economisers, variable-speed pumping) |
| **Typical size** | Below about 200 kW **[CHECK]** | About **200 kW to many MW** **[CHECK]** |
| **First cost** | Lower | Higher (chiller plant, piping) |
| **Free cooling** | Limited | **Water-side economiser** possible |
| **Single point of failure** | Little | The **chilled water supply**: if it fails, every CRAH loses cooling, so the plant is redundant (N+1 or 2N) |
| **Water in the building** | None | Chilled water pipes enter the hall (leak risk) |
| **Refrigerant** | In the room | Mostly outdoors in the chillers |
| **PUE contribution** | About 0.4 to 0.6 | About 0.2 to 0.4 **[CHECK]** |

## 5.3 Free cooling and economisers

An **economiser** uses cool outdoor conditions to cut or switch off the compressors.

| Type | How it works | Notes |
| --- | --- | --- |
| **Direct air-side (fresh air)** | Outdoor air is filtered and supplied directly to the hall, with mixing and humidity control | Very efficient. Needs filtration, humidity control, and a clean, mild climate. **Contamination risk** |
| **Indirect air-side** | An **air-to-air heat exchanger or heat wheel** transfers heat between the hall air and outdoor air without mixing them | Lowest energy of the economiser modes in a published comparison (about 86% less cooling energy than a baseline perimeter chilled-water system) **[CHECK]**. Large footprint |
| **Water-side** | A **plate heat exchanger** and cooling tower or dry cooler bypass the chiller when the condenser water is cold enough | Works with CRAH systems. Full free cooling when the wet-bulb is low, partial in between |
| **Chiller with integrated free-cooling coil** | The chiller can switch off the compressor in cold weather | Compact. Predictable |
| **Glycol free-cooling coil in a CRAC** | Cold glycol from the dry cooler pre-cools the DX coil | Used with glycol-cooled CRACs |
| **Evaporative and adiabatic** | Water evaporates to lower the air or water temperature toward the wet-bulb | Extends free-cooling hours in hot dry climates. **Uses water** |

**What decides the free-cooling hours:** the **local climate**, the **supply temperature allowed** (ASHRAE class), and the **water temperature of the chilled loop**. Ask for the free-cooling hours as a number from the site's own weather file.

## 5.4 Choosing

| Situation | Typical choice **[CHECK]** |
| --- | --- |
| Small hall or edge site, no chilled water | CRAC |
| Medium to large hall with a central plant | CRAH with chillers and a water-side economiser |
| Cool or mild climate, appropriate filtration | Air-side economiser |
| Hot, dry climate, water available | Adiabatic or evaporative assistance |
| Water-scarce site | Dry coolers (near-zero WUE) |

## 5.5 Ride-through for chilled water

When power fails, the chillers drop out and restarting takes minutes. A **chilled water storage tank** keeps the CRAH units cooled meanwhile.

**Worked example.** A **1 MW** cooling load must ride through **10 minutes** with a **6 K** water temperature rise:

```
Energy = 1,000 kW × 600 s = 600,000 kJ
Volume = 600,000 / (4.186 × 6 × 1,000 kg/m³) = about 24 m³ of chilled water
```

A tank of about 24 m³ carries the load for 10 minutes. The pumps and CRAH fans must stay powered from the UPS or an equivalent protected source for it to work.

---

# 9.6 Cooling: up flow or down flow

## 6.1 The airflow configurations of a cooling unit

| Configuration | Supply air leaves the unit... | Return air enters... | Typical use |
| --- | --- | --- | --- |
| **Downflow** | **Downward**, into the raised floor plenum | At the **top** (or the front) | Raised floor halls with perimeter units |
| **Upflow** | **Upward**, from the top of the unit, into a duct or ceiling plenum (or straight into the room) | At the **bottom, front or rear** | Slab-floor halls, ducted or overhead supply |
| **Horizontal (front-to-back)** | **Sideways** from the front of the unit | From the opposite side | In-row, rack-adjacent and row-based units |

```
DOWNFLOW (raised floor)                         UPFLOW (slab floor, ducted)

  return air ↓ (from ceiling/hot aisle)           ceiling supply duct ↑ → diffuser above cold aisle
  ┌─────────┐                                       ┌─────────┐
  │  unit   │                                       │  unit   │ ◄── return air (low, from the room)
  └────┬────┘                                       └────┬────┘
       ▼ supply into the plenum                          ▲ supply up into the duct
 ═══ raised floor plenum ═══ → perforated tile        ═══ slab floor ═══
```

## 6.2 Downflow units

| Feature | Notes |
| --- | --- |
| **Airflow path** | Unit → raised floor plenum → perforated tiles in the cold aisle → rack inlets → hot aisle → back up to the unit's top return (often through a ceiling plenum) |
| **Needs** | A raised floor tall enough for the unit discharge and the airflow (9.8). If the floor is a slab, a **unit stand (floor stand)** is needed |
| **Pros** | Natural fit for a raised floor, flexible tile placement, hides pipes and cables, units sit at the room perimeter |
| **Cons** | Capacity depends on the plenum staying clear and sealed. Tiles close to the unit receive **less** air (see 9.8). Pipe and cable obstructions upset the pressure. Not suited to the heaviest racks or liquid piping |

## 6.3 Upflow units

| Feature | Notes |
| --- | --- |
| **Airflow path** | Unit → ducts or ceiling plenum → overhead diffusers dropping air into the **cold aisle** → racks → hot aisle → return low at the unit (or through a ceiling return) |
| **Needs** | **Duct space** above the racks (ceiling height, Module 3 and 4), good duct design and sealing |
| **Pros** | No raised floor needed (slab floor, higher floor loads), air delivered **exactly where wanted**, suits new-build halls with a known rack layout and also **retrofits with little height** |
| **Cons** | Ducts take ceiling space and can clash with cable trays, lights, detectors and sprinklers. Fan power is higher with duct losses. Harder to rebalance than moving a tile |

## 6.4 Horizontal and row-based units

Units that blow **front to back** between racks (in-row) or beside racks. They shorten the air path and suit high density (9.10).

## 6.5 Placement and return air

| Rule | Reason |
| --- | --- |
| **Return air should come from the hot aisle** | Warm return improves the unit's efficiency (more cooling per unit of airflow) |
| **Place perimeter units at the ends of the hot aisles** (rack rows perpendicular to the unit's discharge) | Air flows along the cold aisles without short-circuiting back to the unit |
| **Avoid short circuits** | Supply air that returns directly to the unit without passing a server wastes cooling (bypass, 9.12) |
| **Avoid obstructions to the return** | A high return, ceiling plenum or a duct to the hot aisle helps |
| **Leave service access** | Front access for filters, coils and belts, with space to remove components |
| **Keep units away from the first tiles** | Tiles right next to a downflow unit often deliver less air because of the pressure dynamics |

---

# 9.7 Cooling: raised floor vs. non-raised floor

## 7.1 Comparison

| | **Raised floor** | **Non-raised (slab) floor** |
| --- | --- | --- |
| **Air distribution** | Underfloor plenum, **perforated tiles** (flexible, move a tile to move the air) | **Overhead ducts and diffusers, in-row units, rack-level units, containment** |
| **Cables and pipes** | Can run in the void (power under cold aisles, data under hot aisles) | Overhead trays and pipework, or cast in the slab |
| **Flexibility** | High for air. Layout changes are simple | Lower for air. Needs planning and tuning |
| **Cost** | Higher: floor system, grounding, ramps | **Lower**: no floor, simpler build |
| **Floor loading** | Limited by panel and pedestal ratings (Module 4) | **Higher**: the slab carries the load directly |
| **Ceiling or building height** | Uses 450 to 900 mm of height for the void | Needs the height above for ducts and trays |
| **Leakage** | **5 to 15%** of the cooling air can leak through seams and cutouts **[CHECK]** | Ducted air is easier to seal |
| **Fire** | Void needs detection and sealing | No void |
| **Liquid cooling piping** | Awkward (leak risk in the void, condensation, load) | Easy to run **overhead** and to monitor |
| **Retrofit** | Hard to install in an existing building | Usually possible |
| **Typical use** | Enterprise and colocation halls, medium density | New builds, **hyperscale**, high density, heavy racks, liquid cooling |

## 7.2 How to choose

| Factor | Points to raised floor | Points to slab |
| --- | --- | --- |
| **Density** | Low to medium (up to about 10 to 15 kW per rack) | Medium to very high |
| **Rack weight** | Standard | Heavy (storage, AI racks) |
| **Layout changes** | Frequent | Stable |
| **Building height** | Plenty | Limited |
| **Liquid cooling** | Not planned | Planned |
| **Containment** | Cold aisle containment fed from tiles | Hot aisle containment with a ceiling return, or in-row |
| **Budget and speed** | Higher cost | Lower cost, faster |

If a raised floor is used, the US Department of Energy guidance recommends at least **610 mm (24 in)** of clear height under it **[CHECK]**.

**Important:** a raised floor is the **most expensive and least reversible** decision in the hall (changing its height or rating means a shutdown), so decide it before building.

---

# 9.8 Raised floor cooling I

## 8.1 How the system works

```
CRAH / CRAC (downflow) → plenum (slightly pressurised) → perforated tile in the COLD aisle
   → rack inlet → servers → rack exhaust into the HOT aisle → return to the unit
```

The plenum is a **pressurised duct**: the cooling units keep the void at a small positive pressure, and air leaves **only where the designer intends**, through perforated tiles.

## 8.2 Layout

| Rule | Reason |
| --- | --- |
| **Hot aisle / cold aisle**: racks face front to front and back to back | Separates supply and exhaust air |
| **Units at the ends of the hot aisles**, discharge along the cold aisles | Pushes air down the aisles |
| **One perforated tile per rack in the cold aisle** (600 mm tiles, 600 mm rack front) | Basic matching of supply to rack |
| **Solid tiles everywhere else** (hot aisle, walkways, staging, under racks) | Cold air must come out where servers breathe it |
| **Align racks with the tile grid** | Tiles and cold aisles line up (8.5 in `08_equipment_racks.md`) |
| **Blanking panels in every unused rack U** | Stops recirculation |

## 8.3 Plenum height

The clear height between the slab and the raised floor surface (the "plenum height") depends on what the void must hold **[CHECK]**:

| Height | Use |
| --- | --- |
| 200 to 300 mm | Cables only. Not suitable if chilled water runs in it |
| 300 to 450 mm | Cables and small chilled-water pipes |
| **450 to 600 mm** | Cables, large pipes, large air paths, and growth. Sensible for more than 500 kW IT load |
| 600 to 900 mm | Hyperscale or large halls with big ducts |

- Studies find that a plenum of about **760 mm or more** gives the **most uniform airflow** through the tiles and the most uniform rack inlet temperatures. Airflow uniformity improves with plenum depth.
- **Obstructions** (pipes, trays) should take **no more than about one third** of the floor height, and cables **no more than about 20% of the plenum cross-section** **[CHECK]**.
- Keep **power under the cold aisle** and **data under the hot aisle**, away from tile openings.
- Don't run trunk routes under perforated tiles.

## 8.4 Floor tiles

| Tile | Open area | Use |
| --- | --- | --- |
| **Solid tile** | 0% | Hot aisles, walkways, staging, under racks |
| **Standard perforated tile** | about **25%** | Low-density racks (about 1 to 5 kW) |
| **High-airflow tile or grate** | about **56%** | Medium-density racks (about 5 to 12 kW) |
| **Directional grille or damper tile** | about 50 to 65% | Racks above about 12 kW, hot-spot fixes, **adjustable** airflow. Needs more plenum pressure |

Match the **tile type to the rack density**, not to the room average. Uniform airflow is not the goal: **supply must match demand rack by rack**.

## 8.5 Plenum pressure

| Item | Practice **[CHECK]** |
| --- | --- |
| **Static pressure** | About **0.05 to 0.15 inch of water** (roughly 12 to 37 Pa) so that air rises through the tiles without overworking the fans |
| **Too low (below about 0.05 in)** | Remote tiles starve, hot spots at the far end of the row |
| **Directional grilles** | Need more pressure (about 0.10 to 0.30 in) |
| **Pressure control** | EC fans modulate to keep the plenum at target pressure, or to hold rack inlet temperature |

## 8.6 Leakage and cutouts

- Air also escapes through **seams between panels**, **cable cutouts** and **unsealed penetrations**. Measured **leakage is typically 5 to 15%** of the cooling air in a real hall.
- An **unsealed cutout under a rack can leak more cold air than a perforated tile delivers.** Fitting **brush grommets** often raises the plenum pressure so much that every tile in the room improves, with no new tiles.
- **Adding perforated tiles can lower** plenum pressure and make things worse. Sometimes the right move is to **remove** tiles.
- **Tiles near the cooling unit** often deliver less air, because air leaves the unit at high speed and low static pressure. Adding extra tiles there to fix a hot spot can worsen it elsewhere.
- Replace perforated tiles that aren't in front of a server inlet with solid tiles.

### Worked example 1: airflow and tiles for one rack

An **8 kW** rack with a server temperature rise of **12 K**:

```
Airflow = 8 / (1.206 × 12) = 0.553 m³/s = 1,990 m³/h = about 1,170 CFM
```

Assume (illustratively) that a 25% perforated tile delivers about **400 CFM** and a directional grille about **700 CFM**:

```
25% tiles:       1,170 / 400 = 2.9, so 3 tiles
Directional:     1,170 / 700 = 1.7, so 2 grilles
```

A single 25% tile in front of a 600 mm rack **cannot** supply an 8 kW rack: this is why density drives the tile type.

### Worked example 2: how much cooling air leaks

A hall's cooling units supply **50 m³/s** and **10%** leaks:

```
Leakage = 50 × 0.10 = 5 m³/s (about 10,600 CFM) that never reaches a server
```

That is wasted fan energy and lost cooling capacity.

## 8.7 Good practice summary

- Seal **every** cutout and seam. Fit **grommets**.
- **Blanking panels** in the racks.
- Tiles only in front of racks, type matched to density.
- Keep the plenum **clear**, with trays low and orderly.
- **Measure** plenum pressure and tile flow, and **re-balance every 6 to 12 months**, because the load changes.

---

# 9.9 Raised floor cooling II

## 9.1 Typical problems and what to check first

| Symptom | Likely cause | Check, in this order |
| --- | --- | --- |
| **Hot spot at one rack** | Insufficient or misdirected air, recirculation | 1. Blanking panels and gaps. 2. **Cutouts** sealed. 3. Plenum pressure at that location. 4. Tile type and position |
| **Far end of the row too warm** | Pressure falls along the plenum, or the far racks are starved | Plenum pressure at the far end, obstructions (cable bundles, pipes), cooling unit position |
| **Tiles near the cooling unit deliver little** | High-velocity air with low static pressure near the unit | Reduce tiles near the unit, move or add dampers |
| **Room cold but racks hot** | Bypass and recirculation | Containment, blanking panels, supply/demand airflow ratio |
| **Fans at high speed, little cooling** | Leakage, blocked plenum, filters | Seals, plenum, filters |

## 9.2 Airflow management measures

| Measure | Effect |
| --- | --- |
| **Seal and balance the plenum** | Raises pressure and evens airflow |
| **Control cooling units on rack inlet temperature (not return air)** | Delivers the temperature the servers need |
| **EC fans with variable speed** | Fan power falls with the **cube** of speed (see 9.12) |
| **Match airflow supply to IT demand** | Aim for supply slightly above demand (roughly 1.1 to 1.3 times) rather than the 1.5 or more seen without airflow management **[CHECK]** |
| **Raise the supply temperature** | Within the ASHRAE recommended range, saves energy and increases free-cooling hours |
| **Cable routing** | Power under cold aisles, data under hot aisles. Keep trays low and open |
| **Damper tiles** | Fine-tune individual racks |
| **Containment (9.12)** | The strongest single measure |
| **CFD (computational fluid dynamics) modelling** | Predicts pressure, tile flow and hot spots before changes |
| **Measurements** | Plenum pressure, tile flow (flow hood), rack inlet temperatures at the top, middle and bottom |
| **Periodic retuning** | Re-check every 6 to 12 months or after changes |

**Fine-tuning example:** if a rack inlet temperature drops 3 to 5 °C after replacing 1 or 2 perforated tiles with open-damper grilles, the tile airflow was the problem. If it doesn't, look at the load or at bypass.

## 9.3 Metrics for airflow performance

| Metric | Meaning | Target |
| --- | --- | --- |
| **Supply Heat Index (SHI)** | The share of heat gained by the cold air **before** it reaches the racks (recirculation) | Ideal **0** |
| **Return Heat Index (RHI)** | The share of heat that the cooling units remove: **SHI + RHI = 1** | Ideal 1 |
| **Rack Cooling Index (RCI)** | How well rack inlets meet the recommended temperature range: **RCI_HI** (against the upper limit) and **RCI_LO** (against the lower limit) | Ideal **100%** (a result of about 96% or more is commonly called good, 90% or below poor) **[CHECK]** |
| **Airflow ratio** | Cooling-unit airflow ÷ IT airflow | Close to 1 (about 1.1 to 1.3) |
| **ΔT across the cooling unit** | Return minus supply temperature | A **low** ΔT with a high airflow signals bypass |

**Worked example: SHI per rack.** Supply air is **18 °C**. A rack inlet reads **22 °C** and its exhaust **34 °C**:

```
SHI (this rack) = (inlet − supply) / (exhaust − supply) = (22 − 18) / (34 − 18) = 4 / 16 = 0.25
```

A quarter of the heat the air gains at this rack is already picked up **before** the inlet (recirculation). Containment drives this towards zero.

## 9.4 Ceiling plenum and return air

A **ceiling plenum** (or duct) taking hot-aisle air straight back to the cooling units keeps the return air hot, raises the unit's ΔT, and improves efficiency. It works well with **hot aisle containment**. Detection and sprinklers must work with it (9.13).

## 9.5 Other raised floor points

- **Water in the void:** leak detection, and chilled water pipes **insulated and protected**.
- **Fire detection in the void** (Module 12).
- **Floor loading** for heavy racks and cooling units (Module 4).
- **Static and grounding** (4.5 in `04_raised_floor_suspended_ceiling.md`).
- **Don't mix airflow tile types** with large open-area differences in one aisle (more than about 15% difference gives uneven flow) **[CHECK]**.

---

# 9.10 Non-raised floor cooling

Without a raised floor, the cold air must be delivered by **overhead supply, in-row units, rack-level units or direct duct connections**.

## 10.1 Methods

| Method | How it works | Notes |
| --- | --- | --- |
| **Overhead ducted supply** | **Upflow** or ceiling-mounted units feed ducts and **diffusers above the cold aisle**, dropping air down in front of the racks | Suits new builds. Needs ceiling height. Pair with **hot aisle containment** and a ceiling return |
| **Slab perimeter cooling with containment** | Perimeter units blow along the floor or through short ducts into a **contained cold aisle** | Needs good airflow design and containment |
| **Fan wall / cooling wall** | An array of CRAH fans along a wall supplies the whole hall through a plenum or open room | **N+1 at the fan level**, quiet, high efficiency |
| **In-row cooling** | Units **between racks** pull hot-aisle air across a coil and push cold air to the cold aisle | Short air path, matched to the row's load. Needs piping to each row |
| **Rack-level cooling** (rear-door heat exchangers, in-rack coolers) | A cooling coil at or in the rack | See 9.11 |
| **Direct air cooling to rack inlets** | Ducts or "snorkels" connect supply directly to the cold aisle or rack | Specialised |
| **Free air / direct outdoor air to the room** | Outdoor air with filtration | See 9.5 |

## 10.2 In-row cooling in more detail

| Feature | Notes |
| --- | --- |
| **Position** | Between racks in the row, one unit per **2 to 4 racks** or as sized **[CHECK]** |
| **Air path** | Hot aisle → unit → cold aisle (short, little mixing, especially with containment) |
| **Types** | Chilled water or DX, with EC fans |
| **Capacity** | Suits **10 to 30 kW** racks, and high-capacity models serve about **35 to 50 kW** **[CHECK]** |
| **Redundancy** | Add units (N+1 per row) |
| **Pros** | Matches the heat load closely, scalable by row, works on a slab or a raised floor |
| **Cons** | Uses row space, needs piping or refrigerant to every row, fan noise in the aisle |

**Worked example: sizing in-row units.** A row of **10 racks at 15 kW** is **150 kW**. Assume **35 kW** per in-row unit:

```
N   = 150 / 35 = 4.3, so 5 units
N+1 = 6 units
```

## 10.3 Overhead supply design

Air in a duct: **cross-section = airflow ÷ velocity**. For **2 m³/s** at **5 m/s**:

```
Area = 2 / 5 = 0.4 m²   (for example a 0.63 m × 0.63 m duct)
```

Keep velocities moderate (noise, pressure drop), seal the ducts, avoid long runs, and balance with dampers. Check the **clearances** to lights, cable trays, detectors and sprinklers (including the **460 mm** nozzle clearance, Module 4).

## 10.4 Pros and cons of non-raised floor cooling

| Pros | Cons |
| --- | --- |
| No raised floor cost, **higher floor loading** | Needs ceiling height and duct space |
| Suits heavy and dense racks | Less flexible to rearrange |
| Suits liquid cooling pipes overhead | More detailed airflow design and tuning |
| Easy to seal and contain | Cables and pipes overhead (clashes) |
| Faster, cheaper construction | In-row units use row space |

---

# 9.11 Supplemental cooling

**Supplemental cooling** adds cooling **beyond the room-level system**, at the row or rack, to handle **high-density racks and hot spots** without rebuilding the room. It is the main way to **extend an air-cooled hall**.

## 11.1 Options

| Option | Description | Typical capacity **[CHECK]** | Needs |
| --- | --- | --- | --- |
| **In-row cooler** | Unit between racks (9.10) | About 10 to 50 kW per rack equivalent | Chilled water or refrigerant to the row |
| **Rear-door heat exchanger (RDHx), passive or active** | A water-cooled coil in the rack's rear door. In a **passive** door the server fans push the exhaust through it, an **active** door adds **fans in the door** | About **25 to 50 kW** per rack depending on design and water temperature (one vendor rates 44 kW with 24 °C water and 68 kW with 14 °C water) | Chilled water at the rack, quick-disconnects (and fan power for active doors) |
| **Overhead (ceiling-mounted) cooler** | A coil above the cold aisle or rows | Medium | Chilled water overhead |
| **In-rack (closed-loop) cooler** | Cooler inside a sealed rack | Medium to high | Water, sealed rack |
| **Spot cooler (portable)** | A movable DX unit | Low | Power, a hot air duct. For **temporary** use |
| **Direct-to-chip liquid cooling** | Cold plates on the processors (9.15) | **50 to 150 kW+** per rack | CDU, manifolds, facility water |

An RDHx absorbs roughly **60 to 95%** of a rack's exhaust heat and returns near-room-temperature air to the hall.

## 11.2 Pros and cons

| Option | Pros | Cons |
| --- | --- | --- |
| **RDHx** | Fastest retrofit, **no change to servers**, the hall can often stay at higher air temperatures, can be swapped in a maintenance window | Water at the rack (leak risk), condensation if the water is below the dew point, door weight and depth, still heat from the front |
| **In-row** | Scalable, short air path | Uses row space, piping to each row |
| **Overhead** | No floor space used | Needs overhead height and piping |
| **Spot coolers** | Quick, no installation | Inefficient, noisy, temporary only |
| **Direct-to-chip** | Handles the highest densities | Needs liquid infrastructure and still leaves residual air heat |

## 11.3 Worked examples

**How much supplemental cooling?** A row of **10 racks at 20 kW** is **200 kW**. The room cooling can deliver about **8 kW** per rack (80 kW):

```
Supplemental cooling needed = 200 − 80 = 120 kW (12 kW per rack)
```

Rear doors rated at 20 kW or more would cover it.

**Water flow for a rear door.** A **20 kW** door with a **6 K** water temperature rise:

```
Flow = 20 / (4.186 × 6) = 0.796 kg/s = about 2.9 m³/h
```

**Condensation:** the water supply temperature must stay **above the room dew point** (guidance commonly calls for at least about **2 °C above**), otherwise the door and pipes sweat.

## 11.4 Selecting by density **[CHECK]**

| Rack density | Typical approach |
| --- | --- |
| Up to about 10 to 15 kW | Room cooling with containment and blanking panels |
| About 15 to 35 kW | In-row coolers or **rear-door heat exchangers** |
| About 35 to 80 kW | RDHx at the top of the range, **direct-to-chip** increasingly necessary |
| Above about 80 kW | **Direct liquid cooling or immersion** (air cannot remove the heat practically) |

---

# 9.12 Containment principle

## 12.1 The problem containment solves

| Term | Meaning | Effect |
| --- | --- | --- |
| **Bypass airflow** | Cold supply air that returns to the cooling unit **without passing through a server** | Wasted cooling and fan energy. Low ΔT at the unit |
| **Recirculation** | Hot exhaust air that **re-enters a server inlet** (over the top of the rack, around the sides, through empty U spaces) | Hot spots, especially at the top of racks |
| **Mixing** | Hot and cold air blending in the room | Forces the supply temperature **lower** than needed and the airflow **higher** than needed |

Without containment, cooling units typically have to move **much more air than the IT equipment needs**. In a published case (700 kW IT load) the uncontained room's cooling units moved **149%** of the IT airflow and the PUE was 1.84 **[CHECK]**.

## 12.2 The principle

**Physically separate the cold supply air from the hot return air**, so that **all** the cold air passes through the servers and **all** the hot air returns to the cooling units.

```
Without containment:                    With containment:
 cold ↘ ↗ hot mixing                     COLD AISLE (enclosed)  │ servers │  HOT AISLE (or returns to duct)
 supply ~ low, airflow ~ high            supply ~ higher, airflow ~ = IT airflow
```

## 12.3 Benefits

| Benefit | Why |
| --- | --- |
| **Higher supply temperature** | No mixing, so the rack inlet equals the supply. Raising it into the ASHRAE recommended range saves energy |
| **Higher return temperature and unit ΔT** | More cooling per unit of airflow |
| **Lower airflow and fan power** | Fans follow the **cube law** (below) |
| **More free-cooling hours** | Warmer water and air can be used |
| **Lower PUE** | Containment is described as the highest-value air-side measure |
| **Better inlet temperature uniformity** | No hot spots at the top of racks |
| **Higher usable density per rack** | Within air-cooling limits |
| **Less need for tile balancing** | Pressure is more uniform |

Raising server inlets from 20 to 22 °C to the 24 to 27 °C part of the ASHRAE range is commonly reported to cut cooling energy by roughly **15 to 25%** in typical climates **[CHECK]**.

## 12.4 The fan law

Fan power varies with the **cube** of airflow (speed):

```
Power ∝ (airflow)³
```

**Worked example.** Containment lets airflow fall by **30%**:

```
Power ratio = 0.7³ = 0.343, so fan power falls by about 66%
```

In the published case, containment cut cooling-unit airflow by 26 to 31%, which could mean 60 to 67% less fan power. That is an **upper bound**: it needs **variable-speed fans**, and the system's resistance and minimum fan speeds change the result.

### Worked example: reading bypass from the ΔT

The servers need **10 m³/s** with a **12 K** rise. The cooling units see a return-to-supply ΔT of only **8 K**:

```
Cooling-unit airflow = 10 × 12 / 8 = 15 m³/s = 150% of the IT airflow
So 5 m³/s (one third of the unit's output) is bypassing the servers
```

A **low ΔT at the cooling unit** with high airflow is the signature of bypass.

## 12.5 Prerequisites and good practice

Containment only works if the basics are in place:

1. **Blanking panels** in every unused U (Module 8).
2. **Seal** gaps at rack sides, rack tops, floor cutouts and between racks.
3. **Cabinet and aisle fit**: consistent rack heights, tile alignment, doors that close.
4. **Airflow supply matched** to IT demand (not far above it), with **variable-speed fans** controlled by pressure or inlet temperature.
5. **Control and verify**:

| Measure | What a healthy contained aisle shows |
| --- | --- |
| **Differential pressure** between the cold and hot aisles | Held at a small positive value in the cold aisle |
| **Rack inlet temperature** (top, middle, bottom) | Flat vertical gradient |
| **Return ΔT at the cooling units** | High |

6. **Fire protection review** for every containment change (9.13).

A contained aisle that still runs hot usually has a **leak** (missing blanking panels, open cutouts, gaps at the rack tops, a propped door), not a cooling shortfall.

## 12.6 Types of containment (overview)

| Type | Description |
| --- | --- |
| **Cold aisle containment (CAC)** | The **cold aisle** is enclosed (roof and end doors). The rest of the room is the hot area |
| **Hot aisle containment (HAC)** | The **hot aisle** is enclosed, usually ducted to a **ceiling return plenum**. The rest of the room is the cold area |
| **Chimney / ducted cabinets** | Each cabinet exhausts into a duct to the ceiling plenum |
| **In-row with containment** | In-row units and a closed aisle |

Compared in 9.14.

---

# 9.13 Containment: possible impact on fire suppression

## 13.1 The issue

Containment (roofs, doors, panels, collars) can **block the discharge of sprinklers and gas**, **change the airflow smoke detectors rely on**, and **stop a clean agent reaching its design concentration**. A hall that complied at commissioning can fall out of compliance **months later** if containment is added without a fire protection review.

## 13.2 What NFPA 75 requires (2024 edition) **[CHECK]**

| Rule | Detail |
| --- | --- |
| **Scope** | Aisle containment and hot air collars are permitted for **hot aisles or cold aisles**, and they are **not treated as plenums** |
| **Sprinklers** | If containment obstructs sprinklers, the sprinkler system **must be modified** to comply with NFPA 13. **No modification is needed** if **all three** conditions are met (below) |
| **Gaseous suppression** | The system must develop the **required agent concentration for the entire volume** it serves (NFPA 2001). If containment prevents this, modify the system, unless the **same three conditions** are met |
| **The three conditions for no modification** | **(1)** An **automatic means of smoke detection** initiates the **removal of the obstruction before** the suppression system operates. **(2)** Removal doesn't **compromise the means of egress** (NFPA 101). **(3)** The removable elements **don't reduce the level of protection** that existed before the containment |
| **Hot aisle temperature** | Detection and suppression components inside a **hot aisle** must be **rated for the temperature** there |

## 13.3 Approaches

| Approach | Notes |
| --- | --- |
| **Sprinkler heads or gas nozzles inside each contained aisle** | Straightforward for **new builds**. Retrofits are complex and disruptive. Each contained space is protected on its own |
| **Smoke detection inside the aisle, with automatic panel release** | Panels or roof elements **open, angle away or drop** on a **smoke detector signal**, before the suppression discharges. Release must be **electrical** and **resettable**, not a trip hazard or an obstruction to exits |
| **Heat-activated drop-away panels (fusible links, heat-shrink)** | **Fallen out of favour** and **not consistent** with the standard: the fire has to grow large before the link trips, gas is released on **smoke**, falling panels can block escape routes, and they need replacing afterwards. NFPA 75 calls for removal **controlled by smoke detection** |
| **Aspirating smoke detection (ASD, such as VESDA)** | Early warning in a high-airflow environment. Spot detectors on the ceiling may never see much smoke when the aisle is contained |
| **HVAC interlock** | Fans stop and dampers close before **gas** is released so the concentration can build |
| **Pre-action sprinklers** | Common for large halls: the pipes stay dry until both detection and a head operate, which reduces accidental discharge |
| **Sprinkler head temperature rating** | Choose a rating suited to the **hot aisle** (NFPA 13 classifies heads by activation temperature) |

## 13.4 Containment fire-protection checklist

| Question | Why |
| --- | --- |
| Does the containment roof block ceiling sprinklers or gas nozzles? | Discharge must reach the fire |
| Is there detection **inside** the contained aisle? | A fire inside may not reach ceiling detectors |
| Is smoke detection **initiating** the release of any removable element? | The condition for avoiding system modification |
| Can the aisle doors be opened from inside, and do panels leave egress clear? | Life safety (NFPA 101) |
| Does a gas release still reach the design concentration with airflow stopped? | NFPA 2001 |
| Are devices in hot aisles **temperature rated**? | They must not false-trigger or fail |
| Is the **under-floor** void also detected? | Cables are a fire load |
| Was the change put through **change control with fire protection review**? | The most common cause of non-compliance in operating halls |

**Check with the authority having jurisdiction (AHJ)** before installing, because the exact provisions and section numbers move between editions.

---

# 9.14 Cold aisle versus hot aisle containment

## 14.1 Comparison

| | **Cold aisle containment (CAC)** | **Hot aisle containment (HAC)** |
| --- | --- | --- |
| **What is enclosed** | The cold (supply) aisle | The hot (exhaust) aisle |
| **Rest of the room** | **Hot** (the room is the return) | **Cold** (the room is the supply), at inlet temperature |
| **Return air** | Whole room | Ducted or via a **ceiling plenum** straight to the cooling unit |
| **Best fit** | **Retrofit on a raised floor with perimeter units** (tiles feed the contained aisle) | New builds, **slab floors with overhead return**, in-row and ducted return |
| **Cost and ease** | Often **simpler and cheaper** to retrofit | Needs a ceiling return or a ducting path, usually more cost |
| **Staff comfort** | Staff work in a **warm** room (and may enter a cold aisle) | Staff work in a **cool** room, but the enclosed hot aisle can be very **hot** |
| **Return temperature** | Moderate | **Higher** (hot-aisle air returns undiluted), so more cooling per airflow |
| **Economiser hours** | Can be good if the room is allowed to run hot | Good, and the hall stays at a comfortable temperature |
| **Cooling unit airflow** | Units must still draw from the whole room | Units draw straight from the hot aisle |
| **Fire protection** | Cold aisle enclosures need coverage and detection | Hot aisle enclosures need components **rated for the temperature** and often their own coverage |
| **Leakage consequence** | Leaks lose cold air into a hot room | Leaks put hot air into a cold room |
| **Cabling and overhead** | Overhead trays are in the warm room | Trays inside the hot aisle see high temperatures |
| **Failure behaviour** | Room temperature rises gradually | Hot aisle temperature rises, room stays cool |
| **Typical limits** | Room temperature set by the return | Hot aisle often reaches **35 to 50 °C** |

## 14.2 What a published comparison found **[CHECK]**

In one vendor white paper (700 kW IT load, Chicago), both options gave the **same PUE (1.65) and 6,218 economiser hours** when there was **no limit on the room temperature**, but the CAC room then ran at about **41 °C**. With the room **held at 24 °C** for staff:

| | PUE | Economiser hours |
| --- | --- | --- |
| **Hot aisle containment** | **1.69** | 5,319 |
| **Cold aisle containment** | 1.98 | **0** |

With the room held at 24 °C, HAC used about **43% less cooling energy**. The answer therefore depends on **how hot you let the room get**.

## 14.3 Hot aisle temperatures

The hot aisle temperature is the inlet temperature plus the server rise:

```
Inlet 25 °C + ΔT 15 K = 40 °C
Inlet 27 °C + ΔT 20 K = 47 °C
```

At these temperatures **occupational heat-stress rules** (WBGT-based limits on time and work rate) may restrict how long staff can work in the aisle **[CHECK]**. Plan **cool-down** before entry, the ability to **shut down** the aisle, and **drinking water** and **limits on time**.

## 14.4 Choosing

| Situation | Typical choice |
| --- | --- |
| Raised floor retrofit, perimeter units, limited budget | **CAC** |
| New build, slab floor, ceiling return plenum, high density | **HAC** |
| Staff comfort in the hall matters | **HAC** (cool room) |
| Free cooling and warm rooms are acceptable | Either, with staff access planned |
| Mixed densities | Combine: containment plus supplemental cooling for the dense rows |
| Existing sprinklers are hard to modify | Choose the option that is easiest to protect (9.13) |

**Both** types cut mixing, but neither saves energy automatically: the savings come from **raising the supply temperature and lowering airflow**.

---

# 9.15 Liquid cooling

## 15.1 Why liquid

At high density, air runs out of capacity. Water carries about **3,500 times more heat per unit volume** than air (9.1).

**Worked example: a 120 kW rack.**

```
Air (ΔT 12 K):    120 / (1.206 × 12) = 8.29 m³/s = about 29,850 m³/h = about 17,570 CFM
Water (ΔT 10 K):  120 / (4.186 × 10) = 2.87 kg/s = about 172 L/min = about 10.3 m³/h
Ratio             29,850 / 10.3 = about 2,900 times less volume with water
```

A 120 kW rack would need **a gale of air**, but only a garden-hose flow of water.

| Rack density | Cooling approach **[CHECK]** |
| --- | --- |
| Below about 15 to 20 kW | Air with containment |
| About 20 to 50 kW | In-row or rear-door heat exchangers |
| **Above about 50 kW** | **Direct-to-chip liquid cooling** is typical |
| Above about 150 kW | Near-total liquid cooling expected |

The NVIDIA GB200 NVL72 (about 120 kW) and GB300 NVL72 (up to 142 kW) racks require liquid cooling.

## 15.2 Types of liquid cooling

| Type | How it works | Typical use |
| --- | --- | --- |
| **Rear-door heat exchanger** | Water-cooled coil in the rack door (9.11) | Retrofit, 25 to 50 kW |
| **Direct-to-chip (cold plate), single-phase** | A metal **cold plate** on each CPU and GPU, with water or a **water and propylene glycol mix** flowing through it | The **standard approach for AI racks**. Handles about 50 to 150 kW and beyond |
| **Direct-to-chip, two-phase** | A refrigerant **boils** in the cold plate | Higher heat flux, more complex |
| **Single-phase immersion** | Whole servers submerged in **dielectric fluid** that stays liquid and is pumped through a heat exchanger | Captures nearly all heat, no server fans. Changes hardware qualification, maintenance, layout |
| **Two-phase immersion** | The fluid **boils** on hot components and condenses on a coil above the tank | Very high flux. Constrained by fluorinated-fluid (PFAS) rules: a replacement fluid was due to be commercialised from 2026, and the regulatory outcome is still open **[CHECK]** |

A cold plate captures the **processor** heat but **not all** of the server's heat: memory, power supplies and network cards still shed heat into the air. Most halls therefore run **hybrid**: cold plates plus a rear door or room air for the remainder. For example, a 120 kW rack capturing 80% in liquid sends **96 kW** to the water loop and **24 kW** to air.

## 15.3 The two loops and the CDU

```
IT cold plates ◄── TECHNOLOGY COOLING SYSTEM (TCS, secondary loop) ◄── CDU ◄── FACILITY WATER SYSTEM (FWS, primary loop) ◄── chillers / towers / dry coolers
```

| Term | Meaning |
| --- | --- |
| **TCS** (technology cooling system) | The clean, filtered coolant loop that runs through the manifolds and cold plates |
| **FWS** (facility water system) | The loop carrying heat from the CDU to the chillers, towers or dry coolers |
| **CDU** (coolant distribution unit) | A pump and heat exchanger that **separates** the two loops, controls temperature, pressure and flow, and keeps the TCS above the room dew point. **The most important element** of the system |
| **Manifold** | Distributes coolant to each server and collects the return |
| **Approach temperature** | The temperature difference across the CDU heat exchanger: **TCS supply = FWS supply + approach** |

CDU types **[CHECK]**:

| Type | Notes |
| --- | --- |
| **Liquid-to-liquid** | Largest capacity. Needs facility water piping |
| **Liquid-to-air** | Rejects heat into the room through a coil. No facility water at the rack, quick to install, limited capacity, and the room air system must still remove the heat |
| **In-rack and in-row** | Sizes range from a few kW to about 150 kW (in-rack) and 1.5 to 2.5 MW (in-row) in one vendor's range |

## 15.4 ASHRAE liquid cooling classes

**W classes** are named by the **maximum facility water supply temperature** (minimum **2 °C** for all). Equipment complies only if it runs **at full performance across the class's whole range**.

| Class | Max supply temperature | Typical heat rejection |
| --- | --- | --- |
| **W17** | 17 °C | Chiller and cooling tower, optional water-side economiser |
| **W27** | 27 °C | Chiller and cooling tower, economiser |
| **W32** | 32 °C | Cooling tower, chiller as a supplement in some climates |
| **W40** | 40 °C | Cooling tower or dry cooler, **often chiller-free** |
| **W45** | 45 °C | Cooling tower or dry cooler, **chiller-free**, heat reuse |
| **W+** | Above 45 °C | Dry cooler, heat reuse |

**S classes** (about **S30 to S50**) describe the **TCS coolant temperature that enters the IT equipment**, which is what the cold plate sees **[CHECK]**.

**Worked example.** A hall built for **W32** with a CDU approach of **5 K**:

```
TCS supply = 32 + 5 = 37 °C to the cold plates
```

Higher classes allow **chiller-free operation**, **dry coolers**, **less water** and practical **heat reuse**. The trade-off is that warmer coolant carries less heat per unit of flow and the densest equipment may need a lower class. Recent AI racks use about **45 °C** liquid.

## 15.5 Design points

| Topic | Practice **[CHECK]** |
| --- | --- |
| **Redundancy** | CDU **N+1**, **dual manifolds**, redundant pumps. Both the TCS and FWS need redundant design |
| **Water quality** | Treated water or water-glycol, **filtration around 50 microns**, corrosion control |
| **Materials** | Stainless steel (304 or 316L, passivated) is the most common TCS piping |
| **Leak detection** | At rack, manifold and floor level, with controlled shut-off |
| **Condensation** | Keep supply temperature above the room dew point. **Insulate** facility-side and CDU primary-side piping if the water can fall below it |
| **Commissioning** | Pressure test, clean, flush and fill: this largely decides whether the loop stays clean for its life |
| **Floor loading and routing** | Piping, manifolds and heavier racks (Module 4). Plan next-generation density when sizing headers |
| **Hybrid air** | Keep air capacity for the share of heat that liquid doesn't capture |
| **Raised floor** | Avoid high-perforation tiles near liquid pipes. Use solid panels over CDUs and manifolds |

## 15.6 Efficiency

Reported PUE bands (vendor figures, treat with care) **[CHECK]**: well-designed **air** with economisers about **1.1 to 1.3**, **liquid** about **1.05 to 1.1**, **immersion** about **1.01 to 1.05**. Warm-water liquid cooling can reject heat through **dry coolers** for much of the year, which also cuts **water use**, and it makes **heat reuse** (district heating) practical.

---

# 9.16 Seasonal Thermal Energy Storage (STES)

The slide writes "STER". The technology is **seasonal thermal energy storage (STES)**.

## 16.1 What it is

**STES** stores **heat or cold for months** so that it can be used in the **opposite season**: for example storing **winter cold** for **summer cooling**, or storing **summer waste heat** for **winter heating**.

## 16.2 Types of STES **[CHECK]**

| Type | How it works | Notes |
| --- | --- | --- |
| **ATES** (aquifer thermal energy storage) | A **doublet of wells** into a natural groundwater aquifer: a **cold well** and a **warm well**. Water is pumped from one to the other and back, so no net water is taken | Needs a suitable aquifer and permits. Efficiency roughly **55 to 70%**. More than **1,000** systems in the Netherlands. The Reichstag in Berlin has been heated and cooled this way since 1999 |
| **BTES** (borehole thermal energy storage) | A field of **vertical boreholes** (one to hundreds, typically 50 to 300 m deep) with U-tube heat exchangers heats or cools the ground itself | Can be built wherever one can drill. Slow charge and discharge. Efficiency roughly **50 to 65%** |
| **PTES** (pit storage) | A large lined pit filled with water | Large-scale district heating, high charge and discharge power |
| **TTES** (tank storage) | An insulated tank | Smaller scale, high power |
| **CTES** (cavern or mine storage) | Flooded mines or caverns | Needs a suitable site |

ATES is classed by storage temperature: **LT-ATES** charged with waste heat up to about **25 °C** (often with a heat pump), and **HT-ATES** above about **40 °C**.

## 16.3 How it applies to a data centre

| Use | How it works |
| --- | --- |
| **Winter cold for summer cooling (cooling-focused ATES)** | In winter, outside air or a cooling tower chills the groundwater and it is **stored in the cold well**. In summer, cold groundwater (about **10 to 12 °C**) is pumped from the cold well through a **heat exchanger** to cool the hall, and the **warmed** water goes to the warm well |
| **Summer waste heat for winter heating** | The data centre's heat charges the aquifer in summer. In winter the warm well supplies **heat pumps** and district heating |
| **Complement to chillers** | In a German study, an ATES could **replace one chiller** in a data centre cooling system, with the remaining chiller still carrying the load if the ATES failed |
| **Compressor-free cooling** | In direct (passive) cooling mode only **pumps** run, so the cooling COP is very high |

**Real example:** the **Bonner Bogen** district in Bonn, Germany, has used an ATES since **2009** to heat and cool a mixed-use development of offices, a hotel, a medical centre and a **data centre** (six wells 22 to 28 m deep, about 60,000 m² of floor area). In the heating season **60 to 80%** of the heat demand is met from the warm aquifer with heat pumps.

## 16.4 Worked examples

**Flow needed to carry 1 MW at a water temperature difference of 8 K:**

```
Flow = 1,000 kW / (4.186 × 8 K) = 29.9 kg/s = 0.030 m³/s = about 107.5 m³/h
```

**Energy stored per cubic metre of water for an 8 K difference:**

```
E = 1,000 kg × 4.186 kJ/kg·K × 8 K = 33,488 kJ = 9.3 kWh per m³
```

**Water volume for a 120-day season at 1 MW:**

```
Volume = 107.5 m³/h × 24 h × 120 days = about 309,700 m³
```

(1 MW × 24 h × 120 days = 2,880 MWh, and 2,880,000 kWh / 9.3 kWh per m³ = 309,700 m³: the same result.)

**Passive cooling COP:** a 2 MW cooling load served through the exchanger with **50 kW** of pumps:

```
COP = 2,000 / 50 = 40, compared with about 5 for a chiller
```

## 16.5 Requirements, benefits and limits

| Requirement | Detail |
| --- | --- |
| **Geology** | ATES needs an aquifer between impermeable layers. BTES needs ground that can be drilled |
| **Permits** | Groundwater use and thermal discharge are regulated |
| **Thermal balance** | Over the years the **heat stored must match the heat recovered**, so integrate with a heating network or other heat users. Otherwise the ground warms (or cools) progressively |
| **Water quality and well maintenance** | Scaling, clogging and corrosion |
| **Distance** | A heat or cold user close by |
| **Scale** | Efficiency rises and unit cost falls with size |

| Benefits | Limits |
| --- | --- |
| Large cut in chiller electricity and **peak** power | Site-specific, depends on geology |
| **Near-zero water consumption** compared with evaporative towers | Permitting and drilling costs, long lead time |
| Allows **heat reuse** with a heat pump (COP above 4 in heating mode is common) | Needs a seasonal heat or cold user to balance |
| Works with warm-water **liquid cooling** (W40 and W45 return temperatures suit heat reuse) | Performance depends on groundwater flow and thermal losses |
| Long life (boreholes often more than 100 years) | Requires monitoring of the subsurface |

---

## Glossary

| Term | Meaning |
| --- | --- |
| Sensible / latent heat | Heat that changes temperature / heat that changes moisture |
| SHR | Sensible heat ratio: sensible ÷ total cooling |
| Ton of refrigeration | 3.517 kW (12,000 BTU/h) |
| COP / EER | Cooling output ÷ electrical input / the same in BTU/h per W (3.412 × COP) |
| CRAC / CRAH | Computer room air conditioner (DX, compressor in unit) / air handler (chilled water coil) |
| Precision cooling | Cooling designed for IT equipment: high SHR, high airflow, 24/7, redundant |
| DX | Direct expansion: refrigerant cools the air directly |
| GWP | Global warming potential of a refrigerant (relative to CO₂) |
| A2L | Mildly flammable, lower-toxicity refrigerant class |
| Economiser (free cooling) | Using cool outdoor conditions to avoid compressor use |
| Plenum | The underfloor (or ceiling) void used as an air path |
| Downflow / upflow | Unit discharges down into the floor / up into a duct or the room |
| Perforated tile / grate / damper tile | Floor tile with about 25% / 56% / adjustable open area |
| Static pressure | The pressure that pushes air through the tiles |
| Bypass / recirculation | Cold air not passing through servers / hot air re-entering inlets |
| SHI / RHI / RCI | Supply heat index / return heat index / rack cooling index |
| Containment (CAC / HAC) | Enclosing the cold / hot aisle |
| ΔT | Temperature difference (rise across servers, or across the cooling unit) |
| RDHx | Rear-door heat exchanger |
| In-row cooling | Cooling units between the racks |
| DLC / cold plate | Direct liquid cooling / metal plate on the chip carrying coolant |
| CDU | Coolant distribution unit separating the TCS and FWS loops |
| TCS / FWS | Technology cooling system / facility water system |
| W and S classes | ASHRAE facility water / coolant temperature classes (W17 to W+, S30 to S50) |
| Immersion cooling | Servers submerged in dielectric fluid |
| ASD | Aspirating smoke detection |
| STES / ATES / BTES | Seasonal thermal energy storage / aquifer storage / borehole storage |

## Exam takeaways

**9.1 (principles and trends)**

- **1 kW of IT power = 1 kW of heat.** Cooling is the second largest energy use and sets availability.
- **Trends:** the modal rack density is **11 kW** (Uptime 2026), while **AI racks are 120 to 142 kW**. Air works to about **15 to 20 kW**, in-row and rear doors to about **35 to 50 kW**, liquid above about **50 kW**.
- **Q = ṁ c ΔT.** Air: V̇ = Q / (1.2 × 1.005 × ΔT), where **1.206 = density × specific heat** (heat per m³ per K). **US form: BTU/h = 1.08 × CFM × ΔT (°F), so CFM = 3,160 × kW ÷ ΔT (°F).** A temperature difference converts at **1 K = 1.8 °F** (never add 32). **Airflow per kW depends on ΔT**, it is not a fixed ratio. **Water carries about 3,500 times more heat per volume.** **1 ton = 3.517 kW.** **COP = cooling ÷ electricity.**
- **ASHRAE (5th edition):** recommended **18 to 27 °C at the IT inlet**, dew point -9 to 15 °C, RH up to 70% (50% if corrosive). **A1 15 to 32, A2 10 to 35, A3 5 to 40, A4 5 to 45.** **H1 recommended 18 to 22 °C.**
- A cooling failure heats a hall in **seconds to minutes**: protect fans and pumps, add thermal storage.

**9.2 to 9.5 (types of systems)**

- **Precision vs. comfort:** SHR **0.9 to 1.0** vs. **0.6 to 0.7**, much higher airflow, 24/7, redundancy, tight humidity control. Comfort cooling over-dehumidifies ("humidity war").
- **Refrigerant cycle:** **evaporator, compressor, condenser, expansion valve.** Condenser rejects **cooling + compressor work.** **Smaller lift means higher COP.**
- **Refrigerants:** R-410A GWP **2,088**, R-134a **1,430**, R-32 **675**, R-454B **466**. **A2L** = mildly flammable. **US: GWP ≤ 700 for new data centre cooling from 1 January 2027.** EU F-gas (EU) 2024/573 phases HFCs out by 2050.
- **CRAC** (DX, compressor in the unit; air-, water- or glycol-cooled) for **small halls and retrofits.** **CRAH** (chilled water) for **larger sites**, with **economisers**. The chilled-water supply is the single point of failure (N+1 or 2N).
- **Free cooling:** direct air-side, **indirect air-side (lowest energy)**, **water-side**, chiller with free-cooling coil, evaporative or adiabatic (uses water). Higher chilled-water temperature (10 to 15 °C) means more free-cooling hours.
- **Chilled water tank** for ride-through (about 24 m³ for 1 MW and 10 minutes at 6 K).

**9.6 to 9.11 (distribution and high density)**

- **Downflow** = into a raised floor plenum. **Upflow** = into ducts or the room, for slab floors. Put units at the **ends of the hot aisles**, return from the **hot aisle**.
- **Raised floor:** flexible, but cost, load limits, **5 to 15% leakage**, at least **610 mm** (DOE). **Slab:** cheaper, higher loads, suits heavy, dense and liquid-cooled racks, needs ducts or in-row.
- **Plenum:** 450 to 600 mm for more than 500 kW, 760 mm or more gives the most uniform airflow. Pressure about **0.05 to 0.15 in w.c.** Tiles: **25%** (1 to 5 kW), **56%** (5 to 12 kW), **directional** (above 12 kW). **Seal cutouts first.** **Power under the cold aisle, data under the hot aisle.**
- **Metrics:** **SHI + RHI = 1** (ideal SHI 0), **RCI ideal 100%.** Control on **inlet temperature**, not return.
- **Non-raised:** overhead ducts, **in-row** (10 to 30 kW, high-capacity 35 to 50 kW), fan walls, rack-level units. **Duct area = airflow ÷ velocity.**
- **Supplemental:** in-row, **rear-door heat exchangers** (about 25 to 50 kW, capture 60 to 95% of exhaust heat), overhead, in-rack, spot coolers (temporary), direct-to-chip. Keep water above the **dew point**.

**9.12 to 9.14 (containment)**

- **Bypass** (cold air skipping servers) and **recirculation** (hot air re-entering). Containment separates supply and return so inlet equals supply.
- **Fan law: power ∝ airflow³** (30% less airflow = 66% less power). **Low ΔT at the cooling unit = bypass.** Prerequisites: **blanking panels, sealing.**
- **NFPA 75 (2024):** containment may block sprinklers and gas. **No modification needed only if** smoke detection **automatically removes the obstruction first**, egress is not compromised, and protection isn't reduced. **Heat-activated drop-away panels are out of favour.** Hot-aisle devices must be **temperature rated.** **Every containment change needs a fire protection review.**
- **CAC** is simpler for **raised-floor retrofits**. **HAC** gives a cool room and a hot return, best for **new builds and ceiling returns**. With the room held at 24 °C, HAC beat CAC in one published example (PUE 1.69 vs. 1.98).

**9.15 to 9.16 (liquid and STES)**

- **Direct-to-chip**, **rear-door**, **immersion**. **CDU separates TCS and FWS.** **TCS = FWS + approach.** **W17, W27, W32, W40, W45, W+** (min 2 °C). **W32 to W40 often chiller-free**, W45 and above dry coolers and heat reuse. **Hybrid**: cold plates leave 20 to 30% of heat to air.
- **Condensation:** supply above dew point. **PFAS** limits two-phase immersion fluids.
- **STES** stores heat or cold for months: **ATES** (well doublet), **BTES** (boreholes), PTES, TTES. Winter cold stored for summer cooling (about 10 to 12 °C). **Thermal balance** is essential. Very high COP in passive mode. Example: Bonn (data centre, since 2009).

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **ASHRAE TC 9.9** *Thermal Guidelines for Data Processing Environments*, 5th edition (2021) | Recommended and allowable envelopes, classes A1 to A4 and H1, humidity limits, liquid cooling classes W17 to W+ and S classes |
| **ANSI/ASHRAE Standard 90.4** (2025) | Energy standard for data centres |
| **ANSI/ASHRAE Standards 15 and 34** (2022) | Refrigerant system safety and refrigerant safety classification |
| **UL 60335-2-40** | Refrigerant safety requirements for air-conditioning equipment |
| **US EPA Technology Transitions rule (AIM Act, 40 CFR Part 84)** | GWP limit of 700 for new data centre cooling from 1 January 2027 |
| **EU F-gas Regulation (EU) 2024/573** | HFC phase-down |
| **EN 50600-2-3**, **EN 50600-4** series, **ISO/IEC 30134** | Environmental control, efficiency KPIs (PUE, WUE) |
| **NFPA 75** (2024), **NFPA 13** (2022), **NFPA 2001**, **NFPA 101** | Fire protection of IT equipment with aisle containment |
| **Uptime Institute Global Data Center Survey 2026** | Rack density trends |
| **Schneider Electric White Paper 135** (hot vs. cold aisle containment) and **White Paper 132** (economiser modes) | Containment and economiser comparisons |
| **US DOE Best Practices Guide for Energy-Efficient Data Center Design** | Raised floor height, containment, air management |
| Sharma et al. (2002) and Herrlin (RCI) | SHI, RHI and RCI airflow metrics |
| NVIDIA reference architectures | AI rack power ratings (GB200 and GB300 NVL72) |
| Aquifer thermal energy storage studies (Pandey et al., *Groundwater*, 2026; German data centre ATES study, 2015) and the Bonner Bogen case | Seasonal storage with data centres |
| Standard thermodynamics and fluid mechanics | Heat-transfer, airflow, COP, Carnot and fan-law formulas |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
