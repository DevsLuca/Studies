# Module 6, Part A: Incoming Power to Transfer Switches (lessons 6.1 to 6.14)

Detailed notes, following the lesson-level index of the EPI course. Module 6 has 47 lessons, so it is split into four files:

| File | Lessons |
| --- | --- |
| **06-1** (this file) | 6.1 to 6.14: incoming power, renewables, microgrids, power quality, requirements, source to destination, transformers, redundancy options I to III, generators, ATS, STS |
| 06-2 | 6.15 to 6.26: three-phase and single-phase power, phase balancing, cabling, dual and triple supply, availability, distribution, busbar trunking, grounding |
| 06-3 | 6.27 to 6.35: common mode noise, distribution boards, IP grades, power quality guidelines, harmonics, CBEMA curve, power factor, label vs. consumed power, sizing |
| 06-4 | 6.36 to 6.47: UPS technologies and modes, batteries, BESS, thermographic scanning |

| Lesson | Title | Section |
| --- | --- | --- |
| 6.1 | Incoming Power | [Section 1](#61-incoming-power) |
| 6.2 | Renewable Energy | [Section 2](#62-renewable-energy) |
| 6.3 | Microgrid | [Section 3](#63-microgrid) |
| 6.4 | Microgrid: Nuclear Power | [Section 4](#64-microgrid-nuclear-power) |
| 6.5 | Power Supply Quality | [Section 5](#65-power-supply-quality) |
| 6.6 | Power Requirements | [Section 6](#66-power-requirements) |
| 6.7 | Power: From Source to Destination | [Section 7](#67-power-from-source-to-destination-slide) |
| 6.8 | Transformers | [Section 8](#68-transformers) |
| 6.9 | Redundancy Options I | [Section 9](#69-redundancy-options-i-the-source-side) |
| 6.10 | Generator Sets | [Section 10](#610-generator-sets-slide) |
| 6.11 | Automatic Transfer Switch (ATS) Panel | [Section 11](#611-automatic-transfer-switch-ats-panel) |
| 6.12 | Redundancy Options II | [Section 12](#612-redundancy-options-ii-ups-level) |
| 6.13 | Static Transfer Switch (STS) | [Section 13](#613-static-transfer-switch-sts) |
| 6.14 | Redundancy Options III | [Section 14](#614-redundancy-options-iii-dual-path-and-the-sts-slide) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#part-a-lessons-61-to-614) |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. **[SLIDE]** marks content taken from a slide you showed me ("From source to destination", "Generator sets", "In the building: redundancy options (cont.)"). If your course gives a different number, use your course.
>
> The electrical physics (Watt's law, I²R, transformer theory, three-phase, kVA) is in `06a_electrical_physics_foundations.md`. Redundancy terms (N, N+1, 2N, 2(N+1), 2N+1) are in Module 2 and summarised again below.
>
> **A note on Redundancy Options I, II and III.** I couldn't see your three redundancy lessons, so I organised them by **level of the power chain**: I is the **source side** (utility, generators, ATS), II is the **UPS level**, III is the **distribution level** with dual paths and the STS (including your "redundancy options (cont.)" slide). If your slides group them differently, the content still applies.

---

# 6.1 Incoming power

## 1. The supply chain at the boundary

Power reaches the site from the public grid at a voltage chosen by the **size of the load**. Larger loads connect at higher voltage, because current falls as voltage rises (Watt's law, I²R losses).

| Connection level | Typical voltage | Typical load **[CHECK]** | Notes |
| --- | --- | --- | --- |
| **Low voltage (LV)** | 400 / 230 V (415 / 240 V, 208 / 120 V, 480 V in some regions) | up to about 1 MVA | Small server rooms |
| **Medium voltage (MV)** | about 10 to 36 kV | roughly 1 to 50 MVA | Most enterprise and colocation sites |
| **High voltage (HV)** | about 66 to 150 kV | tens to hundreds of MVA | Large and hyperscale campuses |
| **Extra-high voltage (EHV)** | 220 to 400 kV and above | hundreds of MVA | Largest campuses, own substation |

## 2. What the incoming supply includes

| Element | Role |
| --- | --- |
| **Point of common coupling (PCC) / point of supply** | The boundary between the utility network and the customer. Metering and the connection agreement apply here |
| **Utility metering and protection** | Revenue meter, protection relays, circuit breakers |
| **MV switchgear (ring main unit, switchboard)** | Switches, protects and isolates the incoming MV feeders |
| **On-site substation** | The building (or enclosure) housing MV switchgear and transformers |
| **Transformer(s)** | Step MV or HV down to the LV used inside (see 6.8) |
| **Cable routes** | Underground feeders are preferred to overhead lines (less exposed to storms, vehicles and vandalism) |
| **Connection agreement** | Contract setting capacity, voltage, power factor, harmonic and protection requirements |

## 3. Feed diversity options

| Option | Description | Resilience |
| --- | --- | --- |
| **Single feed** | One feeder from one substation | Lowest. One cable fault or substation outage stops the site |
| **Dual feed, same substation** | Two feeders from the same substation | Protects against a cable fault, not a substation or upstream failure |
| **Dual feed, different substations** | Two feeders from **independent substations**, ideally on different routes | Best. Protects against a substation outage and many upstream faults |
| **Ring main** | Feeders form a loop, so supply can come from either direction | Good where the utility network is built as rings |

A higher-rated site (Tier IV, Availability Class 4) normally expects **two independent utility feeds** of full capacity each. The two feeds should not share a route, a bridge or a substation (common-mode risk).

**Main-tie-main arrangement** at the site:

```
 Feed 1 ──[Incomer 1]── Bus A ──┐
                                 [Tie]   (normally open)
 Feed 2 ──[Incomer 2]── Bus B ──┘
```

Each incomer normally feeds its own bus. If a feed fails, the **tie** closes and the other feed supplies both buses (so each feed must be sized for the whole site).

## 4. Utility agreement topics

| Topic | What to agree |
| --- | --- |
| **Connection capacity** | Firm capacity in MVA now, and later phases |
| **Voltage and fault level** | Supply voltage and the available short-circuit current (sizes the switchgear) |
| **Power factor** | Usually a minimum (for example 0.9 to 0.95), with penalties below it |
| **Harmonics and flicker** | Limits at the PCC (for example IEEE 519, EN 50160 related rules) |
| **Protection coordination** | Relay settings, so a fault is cleared in the right place |
| **Reliability** | Outage history (SAIDI, SAIFI, from Module 3), planned works, restoration times |
| **Lead time and cost** | Grid connections can take **years**, and the interconnection queue is often the limit on new capacity |
| **Generator operation** | Rules for running generators in parallel with the grid (closed transition, demand response) |

## 5. Worked example: choosing the connection level

A site has a **10 MW IT load**, **PUE 1.3** and **PF 0.95**, with **25% growth** allowance:

```
Total facility power = 10 × 1.3 = 13 MW
Apparent power       = 13 / 0.95 = 13.68 MVA
With 25% growth      = 13.68 × 1.25 = 17.1 MVA
```

Current for 17.1 MVA at different voltages (three-phase, I = S / (√3 × V)):

| Voltage | Current |
| --- | --- |
| **33 kV** | 17,100,000 / (1.732 × 33,000) = about **299 A** |
| **400 V** | 17,100,000 / (1.732 × 400) = about **24,700 A** |

At 400 V the current is far beyond what ordinary cables or switchgear can carry, so the site **must** connect at medium voltage and use on-site transformers near the load.

---

# 6.2 Renewable energy

## 1. Why data centres use renewable energy

| Driver | Detail |
| --- | --- |
| **Sustainability targets** | Net-zero commitments, carbon reporting (Scope 2), customer demand |
| **Cost stability** | Long-term contracts fix a large part of the energy price |
| **Regulation** | Energy efficiency and reporting rules in the EU, and national rules (for example requirements for a rising share of renewable electricity in Germany) **[CHECK]** |
| **Metrics** | **REF** (Renewable Energy Factor), **CUE** (Carbon Usage Effectiveness): see Module 6 sustainability, and ISO/IEC 30134 |

## 2. Sources

| Source | Typical capacity factor **[CHECK]** | Notes for a data centre |
| --- | --- | --- |
| **Solar PV** | about 10 to 25% | Daytime only. Needs a lot of land |
| **Onshore wind** | about 25 to 45% | Variable, often stronger at night |
| **Offshore wind** | about 40 to 60% | More consistent, near some coastal data centres |
| **Hydropower** | about 30 to 60% | Dispatchable, renewable baseload where available (Nordics, Pacific Northwest) |
| **Geothermal** | about 80 to 95% | Firm 24/7 baseload, location-limited (Iceland, parts of the US) |
| **Biomass / biogas** | varies | Can fuel engines and fuel cells |
| **Fuel cells (hydrogen or biogas)** | high | On-site, quiet, no combustion, emerging for data centres |
| **Battery storage (BESS)** | n/a | Shifts energy in time, supports stability |

**Capacity factor** = actual energy produced ÷ (rated power × hours). It is why a 1 MW solar array produces far less than 1 MW × 8,760 h.

## 3. How a data centre gets renewable electricity

| Route | How it works | Notes |
| --- | --- | --- |
| **On-site generation** | Solar on roofs and land, wind, fuel cells | Rarely enough on its own for a large site |
| **Physical PPA** | A power purchase agreement for power from a specific plant, delivered through the grid or a private wire | Long-term (often 10 to 25 years) |
| **Virtual PPA** | A financial contract: the buyer receives the certificates and the price difference, power still comes from the grid | Flexible, no physical delivery |
| **Utility green tariff** | The utility sources renewable power for its customers | Simple |
| **RECs / Guarantees of Origin** | Certificates for renewable generation elsewhere | Easiest, but weakest evidence of real impact |
| **24/7 carbon-free energy (CFE)** | Match consumption with carbon-free generation **hour by hour** | Most demanding, needs storage and firm clean power |

**Annual vs. hourly matching:** annual matching buys as much renewable energy over a year as the site uses, but a site can run on fossil power at night and "offset" it with midday solar. **Hourly (24/7) matching** requires clean generation in the same hours as the load.

**Additionality:** does the contract finance **new** renewable capacity, or just transfer the claim on existing generation?

## 4. Challenges

- **Intermittency:** sun and wind vary, but the load is constant. Solution: storage, hybrid portfolios, firm clean sources, and a grid connection.
- **Land and scale:** large sites need very large generation (see the example).
- **Grid dependence:** almost all sites keep a grid connection, even with on-site renewables.
- **Reliability:** renewables **do not replace** the UPS and generator, which still protect against failures.

## 5. Worked example: why on-site solar can't power a large site

A **10 MW IT load** (assume constant) uses:

```
Energy per year = 10 MW × 8,760 h = 87,600 MWh
```

Solar at a **20% capacity factor**:

```
Capacity needed = 87,600 / (0.20 × 8,760) = 50 MW of solar panels
```

At roughly **1 to 2 hectares per MW** **[CHECK]**, that needs **50 to 100 hectares** of land, and it still would not supply the site at night.

**Carbon example.** If the grid emits **0.4 kg CO₂ per kWh**:

```
87,600,000 kWh × 0.4 kg = 35,040,000 kg = about 35,000 tonnes of CO₂ per year
```

Renewable Energy Factor example: a site uses **100 GWh** a year, of which **60 GWh** is renewable: **REF = 60 / 100 = 60%**.

## 6. How renewables fit the electrical design

- They connect to the **grid** or to an on-site **microgrid**, never directly to the IT load.
- A **microgrid controller** blends sources, storage and the grid (6.3).
- The **UPS, generator and ATS** stay in place, because renewables are not firm.
- **Battery storage** can add backup time and grid services, but it is a separate system from the UPS batteries unless designed together (see BESS in 06-4).

---

# 6.3 Microgrid

## 1. Definition

A **microgrid** is a **local energy system** of generation, storage and loads with a **control system**, able to operate **connected to** the main grid or **islanded** (independent of it).

```
                    Main grid
                        │
                  [Point of common coupling]
                        │
        ┌───────────────┼──────────────────────┐
        │          Microgrid bus               │
        │    ┌─────┬──────┬────────┬─────┐     │
   Generation  Storage  Controller  Loads (data centre)
   (PV, wind,  (BESS)              
    gensets,
    CHP, fuel
    cells)
```

## 2. Parts

| Part | Role |
| --- | --- |
| **Generation** | Solar PV, wind, gas or diesel engines, gas turbines, fuel cells, **CHP** (combined heat and power), and in future nuclear (6.4) |
| **Storage** | Batteries, flywheels |
| **Loads** | The data centre, plus other site loads |
| **Microgrid controller** | Balances supply and demand, controls voltage and frequency when islanded, decides when to island and reconnect |
| **Point of common coupling (PCC)** | The switchgear that connects to (and can disconnect from) the main grid |
| **Protection and metering** | Protects against faults in both modes |

## 3. Operating modes

| Mode | Description |
| --- | --- |
| **Grid-connected** | In parallel with the utility. Buys or sells power |
| **Islanded** | Disconnected from the grid. Local sources set voltage and frequency |
| **Transition** | Planned or automatic switch between the two. Islanding must be detected and the PCC opened quickly |
| **Black start** | Restart from a total shutdown using local sources |

## 4. Benefits and challenges

| Benefits for a data centre | Challenges |
| --- | --- |
| **Resilience:** keeps running when the grid is down | Cost and complexity |
| **Cost:** peak shaving, energy price arbitrage, grid services | Synchronisation, protection and control design |
| **Renewables:** easier integration | Regulatory approval, grid code compliance |
| **Independence:** less dependence on grid connection delays | Intermittent renewable output |
| **Power quality:** local control of voltage and frequency | Operational skill needed |

## 5. Standards **[CHECK]**

| Standard | Topic |
| --- | --- |
| **IEEE 1547** | Interconnection of distributed energy resources with the grid |
| **IEEE 2030.7 / 2030.8** | Microgrid controllers and their test procedures |
| **IEC TS 62898 series** | Microgrid projects: planning, design and operation |

## 6. Worked example: battery in a microgrid

A site has a **5 MW** load, a **4 MW solar array** and a **5 MW / 10 MWh battery**:

```
Battery duration at full load = 10 MWh / 5 MW = 2 hours
Average solar output at 20% capacity factor = 4 × 0.2 = 0.8 MW
```

So the solar covers only about **16%** of the 5 MW average load, and the battery supports **2 hours** of islanded operation at most. For longer outages the microgrid needs **generators** too. This is why microgrids **combine** sources instead of relying on one.

**Microgrid vs. UPS and generator:** a microgrid is a **bigger system** that can supply the site for long periods, but the **UPS** still rides through the first seconds of any disturbance, and the **generator** still provides long-term backup unless the microgrid sources are themselves firm and redundant.

---

# 6.4 Microgrid: nuclear power

> **Time-sensitive [CHECK].** This area is changing fast. The status below is from sources dated up to **October 2026**.

## 1. Why nuclear for data centres

| Reason | Detail |
| --- | --- |
| **Firm, 24/7 carbon-free power** | Runs day and night, regardless of weather, with capacity factors above about 90% |
| **Small land footprint** | Compared with equivalent solar or wind |
| **Match to the load** | A data centre's load is nearly constant, like a reactor's output |
| **Grid delays** | New grid connections can take many years, so on-site or dedicated power is attractive |

## 2. Types

| Type | Description |
| --- | --- |
| **Existing large reactors** | Power purchase agreements with operating plants (for example 20-year PPAs, plant restarts and uprates) |
| **Small modular reactors (SMRs)** | Factory-built reactors, from tens to a few hundred MW each |
| **Microreactors** | Very small, roughly 1 to 10 MW, for edge or demonstration sites |

**Generation III vs. IV:** many SMRs are scaled-down light-water designs (Generation III, up to about 470 MW). Others use sodium, lead, molten salt or gas cooling (Generation IV), and can be much smaller.

## 3. How a nuclear microgrid would be arranged

```
   Reactor module(s) ──► Generator ──► Site MV switchgear ──► Transformers ──► Data centre
            │                                │
            └──────── (grid tie / PCC) ──────┘      UPS + generators still protect the load
```

| Arrangement | Meaning |
| --- | --- |
| **Behind the meter (co-located)** | The reactor supplies the data centre directly. Reduces grid charges but raises regulatory questions about shared network costs |
| **Front of the meter** | Power goes through the grid, as in any PPA |
| **Grid-tied microgrid** | A local reactor plus the grid for backup, with the ability to island |

## 4. Status as of late 2026 **[CHECK]**

- **No SMR currently supplies a data centre at commercial scale.** The first western SMR power is targeted for around **2030**.
- The most advanced real deals use **existing reactors**: for example a 17-year PPA of about 1.92 GW from the Susquehanna plant, and a 20-year agreement to restart the Three Mile Island Unit 1 (about 835 MW) targeted for 2027 or later.
- Large technology companies have signed agreements with SMR developers (for example Google with Kairos Power, Amazon with X-energy, Meta with TerraPower and Oklo, Equinix with several developers including microreactor makers). Most **new-build** capacity is not yet operating.
- Operating SMRs exist in China and Russia, and demonstration microreactors are under way in the US.

## 5. Challenges

| Challenge | Detail |
| --- | --- |
| **Licensing** | Multi-year regulatory approval (NRC in the US and equivalents elsewhere) |
| **Cost** | First-of-a-kind costs are far above targets |
| **Timeline** | Demand is arriving now, reactors in the 2030s |
| **Fuel supply** | Many designs need **HALEU** (high-assay low-enriched uranium), with limited supply outside Russia and China |
| **Public acceptance and siting** | Local opposition, state siting rules |
| **Waste** | Spent fuel handling |
| **Grid and regulation** | Rules on co-located loads and who pays for the network |

## 6. Worked example: how many reactor modules?

A campus needs **100 MW of IT load** at **PUE 1.3**, using **75 MWe** modules:

```
Total power = 100 × 1.3 = 130 MW
N   = 130 / 75 = 1.73, rounded up to 2 modules
N+1 = 3 modules
```

Nuclear modules are redundant **sources**, but the site still needs the normal protection chain (UPS, generators or storage, ATS), since a reactor module can trip and a grid fault can disturb a microgrid.

---

# 6.5 Power supply quality

## 1. What "power quality" means

Power quality is **how closely the supply matches an ideal sine wave** of the correct voltage and frequency. Poor quality damages or disrupts equipment, causing reboots, errors and shortened life.

## 2. Types of disturbance

| Disturbance | What it is | Typical causes | Typical effect |
| --- | --- | --- | --- |
| **Voltage dip (sag)** | Short drop below 90% of nominal | Faults on the network, large motor starts | IT reboots, contactors drop out |
| **Voltage swell** | Short rise above 110% | Load switching off, faults | Stress on equipment |
| **Short interruption** | Voltage below 5% for up to 3 minutes | Switching, auto-reclosing | Outage without UPS |
| **Long interruption** | Longer than 3 minutes | Faults, storms | Generator needed |
| **Transient / surge** | Very short, very high spike | Lightning, switching | Insulation damage, failures |
| **Harmonics** | Distortion of the wave by multiples of the base frequency | Non-linear loads (UPS rectifiers, power supplies, drives) | Heating, neutral overload, nuisance trips (see 06-3) |
| **Flicker** | Fluctuating voltage | Large varying loads | Lights flicker, equipment disturbed |
| **Unbalance** | Unequal voltages or loads across the three phases | Uneven single-phase loading | Overheating, motor damage |
| **Frequency deviation** | Frequency off nominal | Generator or grid imbalance | Timing and motor problems |
| **Noise (EMI / RFI)** | High-frequency interference | Switching devices, radio sources | Data errors |
| **Under- and over-voltage** | Sustained deviation | Network loading | Wear, trips |

## 3. EN 50160: what the utility is expected to deliver **[CHECK]**

EN 50160 describes the **voltage characteristics of public networks** under normal conditions:

| Parameter | Typical LV requirement |
| --- | --- |
| **Voltage magnitude** | Within **±10%** of nominal for **95% of the week** (10-minute averages). All values within +10% / −15% |
| **Frequency** | **50 Hz ±1%** for 99.5% of the year, and −6% / +4% for 100% of the time |
| **Harmonic voltage** | Total harmonic distortion (THD) **≤ 8%** (up to the 40th harmonic), with limits on individual harmonics (for example 5th about 6%, 7th about 5%, 3rd about 5%) for 95% of the week |
| **Flicker** | Long-term flicker severity **Plt ≤ 1** for 95% of the week |
| **Voltage dip** | Event where voltage falls below **90%**. Indicative numbers per year only, up to about 1,000 |
| **Interruption** | Voltage below **5%**. **Short** up to 3 minutes, **long** over 3 minutes |
| **Transient overvoltage** | Generally below about 6 kV peak |

**Key point:** EN 50160 is a **compromise** between supplier and customer. It sets a **minimum**, not a guarantee of excellent quality, and it does **not** promise a particular number of outages. Most suppliers do better, but a data centre that needs better must **mitigate it itself** (UPS, filters, surge protection) or negotiate a higher-quality supply.

### Worked examples

**1. The voltage band.** For 230 V nominal:

```
±10%  → 207 V to 253 V
Dip threshold (90%)       = 207 V
Interruption threshold (5%) = 11.5 V
```

**2. Total harmonic distortion.** A supply has 5th harmonic = 4% and 7th harmonic = 3% (of the fundamental):

```
THD = √(4² + 3²) = √(16 + 9) = 5%
```

That is within the 8% limit.

## 4. Other standards

| Standard | Topic |
| --- | --- |
| **IEC 61000 series** | EMC, including measurement (IEC 61000-4-30) and immunity |
| **IEEE 519** | Harmonic limits at the point of common coupling |
| **IEEE 1159** | Power quality monitoring definitions |
| **IEC 62040** | UPS |
| **ITIC / CBEMA curve** | Voltage tolerance of IT equipment (see 06-3) |

## 5. How a data centre protects itself

| Measure | Protects against |
| --- | --- |
| **UPS (double conversion)** | Dips, interruptions, noise, frequency and voltage variations |
| **Generator** | Long interruptions |
| **Surge protective devices (Type 1, 2, 3)** | Transients and lightning |
| **Harmonic filters / low-harmonic UPS** | Harmonic distortion |
| **Phase balancing** | Unbalance |
| **Power quality meters (Class A)** | Detecting and recording events |
| **Earthing and bonding** | Noise and safety |

---

# 6.6 Power requirements

## 1. What has to be supplied

| Load | Notes |
| --- | --- |
| **IT (critical) load** | Servers, storage, network. The load the whole design protects |
| **Cooling** | Chillers, CRAH units, pumps, fans. Often the second biggest load |
| **Electrical losses** | UPS, transformers, PDUs, cables, switchgear |
| **Lighting and other** | Lighting, security, monitoring, offices |
| **Future growth** | Planned expansion and spare capacity |

## 2. From IT load to total power

The link is **PUE**:

```
Total facility power = IT load × PUE
```

**Worked example (illustrative figures).** IT load **1,000 kW**, **PUE 1.4**:

| Item | Power | Share |
| --- | --- | --- |
| IT equipment | 1,000 kW | 71.4% |
| Cooling | 280 kW | 20.0% |
| Electrical losses | 90 kW | 6.4% |
| Lighting and other | 30 kW | 2.1% |
| **Total** | **1,400 kW** | **100%** |

Then to the apparent power the supply must carry (at **PF 0.95**) with **25% growth**:

```
S = 1,400 / 0.95 = 1,474 kVA
With growth: 1,474 × 1.25 = 1,842 kVA
```

## 3. Rack density

Total IT load = number of racks × average kW per rack.

| Rack type | Typical power **[CHECK]** |
| --- | --- |
| Legacy / low density | about 3 to 5 kW |
| Typical modern enterprise | about 5 to 15 kW |
| High density / HPC | about 20 to 50 kW |
| AI training racks | about 50 to over 100 kW |

Example: 200 racks at 8 kW = 1,600 kW. At 40 kW the same 200 racks would be 8,000 kW. **Power density drives the electrical, cooling and floor-loading design.**

## 4. Sizing concepts

| Concept | Meaning |
| --- | --- |
| **Connected load** | Sum of all equipment nameplate ratings (usually far above real use) |
| **Demand (actual) load** | What is really drawn |
| **Diversity** | Not everything runs at full power at once, so the design can be less than the sum |
| **Redundancy** | The installed capacity is **more** than the load (N+1, 2N and so on) |
| **Growth and phasing** | Capacity is built in phases (modular) to avoid stranded capacity |
| **Stranded capacity** | Installed power that cannot be used (for example because cooling or distribution is the limit) |
| **Derating** | Reducing equipment capacity for temperature, altitude or load type |

**Redundancy changes installed capacity.** With a **1.8 MVA** load:

| Design | Capacity installed (equipment units sized for the load) |
| --- | --- |
| N | 1.8 MVA |
| N+1 (for example three units of 0.9 MVA) | 2.7 MVA |
| 2N | 3.6 MVA (two full systems) |
| 2(N+1) | 5.4 MVA if built from the same 0.9 MVA modules (6 modules) |

## 5. Supply requirements to specify

- **Voltage and frequency** (400/230 V, 50 Hz in Europe, or 480 V / 208 V, 60 Hz in the US) and tolerances.
- **Number of phases and neutral arrangement.**
- **Available short-circuit level** at each board.
- **Power factor** and harmonic limits.
- **Redundancy level** per stage.
- **Autonomy** (UPS battery runtime and fuel).
- **Growth path** and modularity.

---

# 6.7 Power: from source to destination **[SLIDE]**

Your slide opens with **Watt's law, P = V × I**, and shows the route from a power plant to the data centre.

## 1. The route

| Stage | Example voltage on the slide | Role |
| --- | --- | --- |
| **Power generation plant** (coal, nuclear, hydro and so on) | (generated, then stepped up) | Produces the power |
| **Transmission towers** | 800 kV / 400 kV | Very high voltage for low current over long distances |
| **Regional substation** | 800 kV down to 33 kV | First step-down |
| **Local / building substation** | 33 kV down to 415 V | Final step-down |
| **Data centre** | 415 V three-phase, 240 V single-phase | Three-phase for large loads, single-phase for small |

## 2. The physics in three lines

```
P = V × I           For the same power, higher voltage means lower current
P_loss = I² × R     Lower current means far lower heat losses in the cables
V₂/V₁ = N₂/N₁       Transformers change the voltage, and need AC
```

(Worked through in `06a_electrical_physics_foundations.md`, sections 2 to 4.)

## 3. Inside the data centre, by stage

For a **1 MVA** load (three-phase, I = S / (√3 × V)):

| Stage | Voltage | Current |
| --- | --- | --- |
| Utility MV feed | 20 kV | 1,000,000 / (1.732 × 20,000) = about **29 A** |
| After the transformer (LV) | 400 V | 1,000,000 / (1.732 × 400) = about **1,443 A** |
| One rack on a single-phase circuit | 230 V, 7.4 kW | about **32 A** |

This is why **MV cabling is thin**, **LV busbars and cables are heavy**, and the **transformer room sits next to the LV main board**.

## 4. Efficiency along the chain

Each stage loses some energy as heat:

| Stage | Typical efficiency **[CHECK]** |
| --- | --- |
| Transformer | 98 to 99% |
| UPS (double conversion) | 94 to 97% |
| PDU / isolation transformer | 98 to 99% |
| Cables and busbars | 98 to 99% |

**Worked example (illustrative):** 98.5% × 96% × 98.5% × 99% is:

```
0.985 × 0.96 × 0.985 × 0.99 = 0.922 → 92.2%
```

So about **7.8%** of the power taken from the utility is lost before it reaches the IT equipment. That loss becomes **heat** to remove and a **higher PUE**.

---

# 6.8 Transformers

## 1. Role

A transformer **changes voltage** (and so current) between two AC circuits, linked only by a magnetic field (theory in `06a`, section 4). In a data centre it steps **MV down to LV**, may **isolate** a circuit (delta-wye), and may **match voltages** for equipment.

## 2. Types

| Type | Characteristics | Typical use |
| --- | --- | --- |
| **Oil-immersed** | Windings in mineral or ester oil. Efficient and compact, but a **fire and spill risk** | Outdoor or in fire-rated, bunded rooms |
| **Cast resin (dry-type)** | Windings cast in resin, air-cooled. **Low fire risk**, no oil | **Indoors**, inside buildings, close to the load |
| **Dry-type (VPI)** | Windings impregnated with varnish. Air-cooled | Indoor, lower voltage |
| **Isolation / PDU transformer** | Delta-wye, secondary neutral bonded | Inside the white space (see Module 6, bonding) |
| **Autotransformer** | Single winding, no isolation | Special cases, voltage matching |

## 3. Key ratings and features

| Item | Meaning |
| --- | --- |
| **Rated power (kVA)** | The apparent power it can carry continuously under stated conditions |
| **Voltage ratio** | For example 20 kV / 400 V |
| **Vector group** | Winding connection and phase shift, for example **Dyn11** (delta primary, star secondary with neutral, 30° shift) |
| **Impedance (uk%)** | Voltage drop at full load, which sets the fault current |
| **Cooling class** | **AN** (air natural), **AF** (air forced), **ONAN** (oil natural, air natural), **ONAF** (oil natural, air forced) |
| **Tap changer** | Adjusts the ratio (for example ±2 × 2.5%). **Off-load** (switched with the transformer de-energised) or **on-load** |
| **Losses** | **No-load (core) losses** always present, **load (copper) losses** rise with the square of the load |
| **Efficiency standards** | Regulations on minimum efficiency, for example the EU Ecodesign rules **[CHECK]** |
| **K-factor** | Rating for loads with high harmonic currents |
| **Protection** | Temperature sensors (cast resin), Buchholz relay and pressure devices (oil), overcurrent and earth-fault relays |
| **Noise** | A low-frequency hum (a few tens of dB), relevant for site permits |

## 4. Fault level

The transformer impedance limits the current in a fault:

```
Rated current:  I_n = S / (√3 × V)
Fault current:  I_sc = I_n / uk
```

**Worked example.** A **1,600 kVA, 20 kV / 400 V** transformer with **uk = 6%**:

```
I_n  (LV)  = 1,600,000 / (1.732 × 400) = 2,309 A
I_sc (LV)  = 2,309 / 0.06 = about 38,500 A = 38.5 kA
```

The LV switchgear and busbars must be rated for **at least that fault level**.

## 5. Losses and efficiency

Losses = **no-load loss** (constant) + **load loss × (load fraction)²**.

**Worked example (illustrative).** A 1,600 kVA transformer with no-load loss 1.7 kW and full-load loss 14 kW, at **50% load, PF 0.95**:

```
Output power = 1,600 × 0.5 × 0.95 = 760 kW
Losses       = 1.7 + 14 × (0.5)² = 1.7 + 3.5 = 5.2 kW
Efficiency   = 760 / (760 + 5.2) = 99.3%
```

The **heat** from losses has to be ventilated. At full load this transformer dissipates about 15.7 kW (1.7 + 14).

## 6. Inrush current

When a transformer is energised, it can draw an **inrush current of about 8 to 12 times** its rated current for a fraction of a second **[CHECK]**. The protection must be set so it doesn't trip on inrush. This is also why **primary-side transfer switches between unsynchronised sources** can cause problems (see 6.13).

## 7. Redundancy and loading

- With **two transformers (2N)** each carries about 50% normally, and **each must be able to carry 100%** if the other fails.
- **ONAF/AF cooling fans** can add about 25 to 33% extra capacity for emergencies **[CHECK]**.
- **N+1 transformers** can use several units sharing the load.
- Keep the **transformer close to its LV board** to keep the very high-current LV runs short.

## 8. Placement and safety

| Consideration | Detail |
| --- | --- |
| **Oil-filled** | Outdoors or in a fire-rated room with a **bund** (to contain oil) and suitable fire protection |
| **Cast resin** | Can be indoors, close to the load. Needs ventilation for heat |
| **Access and replacement** | A route for a very heavy item |
| **Noise** | Distance and enclosures |
| **Delta-wye isolation** | Traps third-harmonic currents, isolates upstream disturbances, creates a new neutral for the local bond |
| **Standards** | IEC 60076 (power transformers), IEC 60076-11 (dry-type), IEEE C57 series **[CHECK]** |

---

# 6.9 Redundancy options I: the source side

## 1. Terms (recap)

| Term | Meaning |
| --- | --- |
| **N** | Exactly the capacity needed |
| **N+1** | Needed capacity plus one spare unit |
| **2N** | Two complete, independent systems, each able to carry the full load |
| **2(N+1)** | Two complete systems, each with its own spare |
| **2N+1** | Two full systems plus one shared spare |

Redundancy can be applied at **each level**: utility, generators, ATS, UPS, distribution and cooling. The overall site is only as resilient as its **weakest level**. This lesson covers the **source side**: utility feeds, generators and the ATS.

## 2. Source-side configurations

### A. Single utility, single generator, ATS (N)

```
 Utility ──────────┐
                  [ATS] ──► to the site
 Generator ───────┘
```

Simple and cheap. A generator that fails to start, or an ATS failure, leaves the site on UPS batteries only. Typical of **Tier I and II** (with N+1 added to parts).

### B. N+1 generators (paralleled)

```
 Gen 1 ──[CB]──┐
 Gen 2 ──[CB]──┼── Paralleling bus ──► to ATS / LV main board
 Gen 3 ──[CB]──┤
 Gen 4 (+1) ──[CB]──┘
```

Several generators **synchronise** onto a common bus and **share load**. One can fail or be serviced and the rest carry the load. The **common paralleling bus** and its controls are a **single point of failure**.

### C. Dual utility feeds (main-tie-main) plus generators

```
 Feed 1 ──[Incomer 1]── Bus A ──┐
                                 [Tie]   (normally open)
 Feed 2 ──[Incomer 2]── Bus B ──┘
 Generators connect through ATS or paralleling switchgear
```

Protects against a **utility feed** failure with no generator start, as the tie closes and one feed carries both buses.

### D. Two complete source chains (2N)

```
 Chain A:  Utility 1 + Gen 1 ──► ATS A ──► ...
 Chain B:  Utility 2 + Gen 2 ──► ATS B ──► ...
```

Fully independent. Either chain can carry the whole load. This is what the **A and B chains** on your slide are.

## 3. Comparison

| Configuration | Protects against | Weakness |
| --- | --- | --- |
| **N** | Nothing beyond the basic utility-to-generator step | Any component failure |
| **N+1 generators** | A generator failing or being serviced | Common paralleling bus, shared fuel and controls |
| **Dual utility, main-tie-main** | One utility feed failing | A shared tie or bus, a common upstream fault |
| **2N chains** | A whole chain failing, and concurrent maintenance | Highest cost, more equipment |

## 4. Worked example: how many generators?

The site needs **2,400 kW** from generators.

| Unit size | N | N+1 | Notes |
| --- | --- | --- | --- |
| 800 kW | 3 (2,400 kW) | **4** (3,200 kW) | Normal load per unit 600 kW (75%) |
| 1,200 kW | 2 | **3** | Normal load per unit 800 kW (67%) |
| 2,500 kW | 1 | **2** | Only one spare, but each is a large unit |

Smaller units give a **smaller spare as a share of the total** but more equipment to maintain.

## 5. Common-mode risks on the source side

A redundant arrangement still fails if one cause hits several parts at once:

- A **shared fuel supply, fuel pump or day tank**
- A **shared paralleling bus or control system**
- Both generators in **one room** (fire or flood)
- Both utility feeds on **one cable route** or one substation
- The same **maintenance error** on both systems
- **Shared cooling** or air intake for the generators

## 6. Link to the Tiers

| Tier | Source side |
| --- | --- |
| I | N, a single path |
| II | N+1 generators, single path |
| III | N+1 with multiple paths, concurrently maintainable |
| IV | 2N or 2(N+1), fault tolerant |

---

# 6.10 Generator sets **[SLIDE]**

## 1. Role

Your slide: **generators act as the backup supply for the utility grid.** **Diesel is the most common choice**, and **alternatives are now considered** because of sustainability requirements.

| Fuel / technology | Notes |
| --- | --- |
| **Diesel** | Dense fuel, fast start, proven, high emissions |
| **Gas (natural gas, biogas)** | Cleaner, but the fuel supply depends on a pipeline or on-site storage |
| **Dual-fuel** | Runs on gas and diesel |
| **HVO (hydrotreated vegetable oil)** | A renewable diesel substitute that can often be used in diesel engines **[CHECK]** |
| **Gas turbines** | Larger sites, fast ramp, higher maintenance |
| **Fuel cells, batteries** | Emerging alternatives for part of the backup role |
| **Rotary UPS (DRUPS)** | A flywheel and generator combination |

## 2. What the size depends on **[SLIDE]**

The slide lists three things:

1. **The kVA/kW requirement of the attached installation.**
2. **Harmonics returning from the connected installation.**
3. **Expected inrush currents** on the generator during operation.

| Item | Multiplier on the slide |
| --- | --- |
| **UPS load** | **× 1.0 or × 1.2**, depending on harmonics levels |
| **Cooling and light load** | **× 1.0** |
| **Total gen-set capacity** | Sum, in kW |

**Why the multiplier:** a generator has a much higher internal impedance than the grid, so harmonic currents from the UPS rectifier distort its voltage and overheat the alternator windings. A UPS with high harmonic distortion gets **× 1.2**, a low-harmonic one (active front end or filters) **× 1.0**. (Harmonics are covered in 06-3.)

### Worked example: sizing

UPS load **800 kW** (high harmonics), cooling and lighting **500 kW**:

```
UPS part       = 800 × 1.2 = 960 kW
Cooling/light  = 500 × 1.0 = 500 kW
Total          = 1,460 kW
With a 20 to 25% margin (ambient, ageing, motor starting) = 1,752 to 1,825 kW
```

In kVA at **PF 0.8** (the usual alternator rating): 1,825 / 0.8 = **2,281 kVA**.

If built from **1,000 kW** sets: N = 2, **N+1 = 3 sets**.

## 3. Ratings (ISO 8528-1) **[CHECK]**

A "kW" figure on a generator is meaningless without its **rating**:

| Rating | Meaning | Hours and load |
| --- | --- | --- |
| **ESP** (Emergency Standby Power) | Outages only | About **200 hours per year**, average load up to about **70%**, no overload |
| **LTP** (Limited-Time Power) | Limited running at full load | About **500 hours per year**, 100% load |
| **PRP** (Prime Rated Power) | Primary source with variable load | **Unlimited hours**, average about **70%**, 10% overload for 1 hour in 12 |
| **COP** (Continuous Operating Power) | Constant load | **Unlimited hours** at up to 100%, no overload |
| **DCP** (Data Centre Power, added in ISO 8528-1:2018) | Data centres with a reliable utility | **Unlimited hours** at variable load, **no average-load cap**, no overload |

The same engine has a **different kW** at each rating, with **standby the highest figure** and **continuous the lowest**. Always compare like with like. A prime-rated set has roughly 90% of the standby rating **[CHECK]**.

**Transient performance (ISO 8528-5):** classes **G1 to G4** describe how much voltage and frequency dip a set suffers when load is suddenly applied. Data centres need a good class (commonly G3) because a UPS rectifier is a **large step load** **[CHECK]**.

## 4. Starting time and NFPA 110

**NFPA 110** classifies emergency power systems. Data centres usually use **Level 1, Type 10**: the generator must supply the loads **within 10 seconds** of a utility failure.

| Time | What happens |
| --- | --- |
| **0 s** | Utility fails. The ATS controller detects a voltage drop (commonly below about 85% of nominal) **[CHECK]** |
| **0.5 to 3 s** | A programmed delay confirms the failure is real before starting the engine |
| **About 1 to 5 s** | Engine cranks and starts |
| **By about 10 s** | Generator reaches stable voltage and frequency, and the ATS transfers the load |
| **Throughout** | The **UPS batteries carry the IT load** until the generator takes over |

This **10 to 15 second gap** is why the UPS has batteries, and why UPS battery runtime of **a few minutes** is enough in normal designs.

## 5. Fuel

| Item | Detail |
| --- | --- |
| **Day tank** | Small tank near each set, feeding the engine |
| **Main storage tank** | Larger tank (underground or above ground), with containment and leak detection |
| **Autonomy** | Hours of running at full load. Higher-rated sites commonly need **12 hours or more** (Tier III is often quoted at 12 hours at full load), and some need 48 to 96 hours **[CHECK]** |
| **Resupply contract** | Delivery agreement with priority in a regional emergency |
| **Fuel quality** | Stored diesel degrades and can grow microbes, so it is tested and **polished** (filtered) regularly **[CHECK]** |
| **Alternative fuel** | NFPA 110 requires an alternative fuel for Level 1 systems where off-site fuel supply might be interrupted **[CHECK]** |

**Worked example: fuel.** The 1,120 kW generator load, at about **0.26 L/kWh** **[CHECK]**:

```
Consumption = 1,120 × 0.26 = 291 L/hour
12 hours = 291 × 12 = about 3,490 litres
48 hours = 291 × 48 = about 13,980 litres
```

## 6. Other design points

| Topic | Detail |
| --- | --- |
| **Derating** | Output falls above about **40 °C** ambient or about **1,000 m** altitude, so correct for the site **[CHECK]** |
| **Wet stacking** | Running diesel engines at **light load (below about 30%)** leaves unburned fuel and soot in the exhaust. Testing at load avoids it |
| **Load acceptance** | The set must accept large steps (such as UPS rectifiers) without voltage or frequency collapse. **Walk-in or staged loading** on the UPS and **sequenced starting** of cooling help |
| **Paralleling** | Synchronisation, load sharing, and a paralleling switchgear that can itself be redundant |
| **Starting** | Duplicate starter batteries and starters, with their own chargers |
| **Cooling and air** | Radiator or remote cooler, with the combustion and cooling air supplied and exhausted without re-ingestion |
| **Emissions** | Emergency-only sets may meet lighter limits, but **prime or peak-shaving use triggers stricter rules** (for example US Tier 4 Final, EU Stage V), and non-emergency running is hour-limited **[CHECK]** |
| **Noise** | Acoustic enclosures and silencers |
| **Location** | Outdoors in enclosures, or in a separate fire-rated room, away from the computer room (see Module 3) |
| **Sizing margin** | A margin of roughly 20 to 25% is common **[CHECK]** |

## 7. Testing and maintenance **[CHECK]**

| Test | Frequency |
| --- | --- |
| **Monthly run** | At least about 30 minutes, at 30% or more of rated power (or enough load to reach the manufacturer's minimum exhaust temperature) |
| **Load bank test** | Periodically (commonly annually), to prove full load and reveal hidden faults |
| **ATS operation** | Monthly transfer exercise |
| **Fuel and battery checks** | Regular testing, replacing batteries on schedule |
| **Logs** | Every run is recorded (also for emission-hour limits) |

A generator is the most tested and least used machine in the site. A set that has not been run under load is paper resilience.

---

# 6.11 Automatic transfer switch (ATS) panel

## 1. What an ATS does

An **ATS** monitors the **normal (utility) source** and an **alternate source** (the generator), and **automatically moves the load** between them. It is the link between the **utility and the generator**.

## 2. Sequence of operation

| Step | What happens |
| --- | --- |
| 1 | Controller monitors voltage and frequency on the normal source |
| 2 | Normal source fails (voltage below the set threshold for a set time) |
| 3 | **Engine start signal** goes to the generator (usually a simple two-wire contact) |
| 4 | Generator starts and stabilises (voltage and frequency within limits) |
| 5 | ATS **transfers the load** to the generator |
| 6 | Utility returns. The ATS waits until it is **stable** |
| 7 | ATS **retransfers** the load to the utility |
| 8 | Generator runs on briefly for a **cooldown**, then stops |

**Typical time delays:** **TDNE** (normal to emergency, before transfer), **TDES** (engine start, to ride out short dips), **TDEN** (emergency to normal, to confirm the utility is stable), **TDEC** (engine cooldown) **[CHECK]**.

## 3. Types of transition

| Type | How it transfers | Interruption | Notes |
| --- | --- | --- | --- |
| **Open transition (break-before-make)** | Disconnects one source before connecting the other | **Brief loss of power**, commonly about 40 to 200 ms **[CHECK]** | The standard type. IT loads need a UPS |
| **Delayed (programmed) transition** | Pauses in a **neutral position** for an adjustable time | Short but intentional gap (often 1 to 30 s) | Lets motors and transformers **de-energise** before re-energising, protecting chillers and large motors |
| **Closed transition (make-before-break)** | Both sources are **briefly paralleled** (typically under 100 ms) | **No interruption** | Needs **synchronisation** and usually **utility approval**. Used for retransfer without an outage |

## 4. Poles: 3-pole vs. 4-pole

| Type | Meaning | When |
| --- | --- | --- |
| **3-pole** | Switches the three phases only. The neutral is solid | When both sources share one neutral-earth bond |
| **4-pole (switched neutral)** | Also switches the neutral | When the generator is a **separately derived source** with its **own neutral-earth bond**, so only one bond is in the active path |

Getting this wrong causes **neutral current flowing in earth conductors**, nuisance earth-fault trips and noise (see the single-bond rule in Module 6 earthing).

## 5. Bypass-isolation ATS

A **bypass-isolation** ATS has a second, manual switching path. The main ATS can be **isolated and serviced while the load stays powered**. Without it, the ATS must be de-energised for maintenance, which breaks **concurrent maintainability** (Tier III).

## 6. Ratings and standards **[CHECK]**

| Item | Detail |
| --- | --- |
| **Current rating** | Must carry the full load continuously. Common practice: size the switch for **125% of continuous load** (or use a 100%-rated device) |
| **Short-circuit rating** | **Withstand and closing rating (WCR)** must exceed the available fault current |
| **Standards** | UL 1008 (US), IEC 60947-6-1 (transfer switching equipment), NFPA 110 (emergency power) |
| **Interlocks** | Mechanical **and** electrical, so both sources can never be connected at once (except in closed transition) |
| **Manual operation** | A safe way to operate it by hand |

**Worked example: sizing.** The continuous load is **390 A**:

```
390 × 1.25 = 487.5 A  →  choose a 600 A ATS (not 400 A)
```

## 7. Where ATS units sit

| Arrangement | Description |
| --- | --- |
| **Central ATS at the LV main board** | One ATS (or a pair) switches the whole site between utility and generators |
| **Distributed ATS** | An ATS per UPS, per system, or per load group, so a failure affects less |
| **Main-tie-main with ATS** | Two incomers and a tie, automated |

```
 Utility ──────────┐
                  [ATS] ──► LV main board ──► UPS and cooling
 Generator(s) ────┘
```

## 8. ATS and the UPS

An ATS transfer is **not instantaneous**, so any IT load **must be behind a UPS**. During the transfer the **UPS batteries carry the load**. This is the roles split:

| Device | Speed | Job |
| --- | --- | --- |
| **ATS** | tens to hundreds of milliseconds (open) | Utility to generator |
| **UPS** | zero (online) | Bridges the gap |
| **STS** | a few milliseconds (6.13) | Switches between two sources at the load |

## 9. Maintenance and common faults

- Monthly transfer exercise, with the generator test.
- Check contacts and mechanisms, thermal imaging of connections (see 06-4).
- Common problems: **loose connections**, controller faults, wrong time-delay settings, battery failure in the controller, and untested bypass.

---

# 6.12 Redundancy options II: UPS level

## 1. The UPS stage

The UPS stage is where **continuity** is provided. Several arrangements exist, each trading cost, efficiency and fault tolerance. (UPS technologies are covered in 06-4.)

## 2. Techniques

| Technique | How it works | Strength | Weakness |
| --- | --- | --- | --- |
| **Single UPS (N)** | One module sized for the load | Simple | Any failure drops protection |
| **Parallel redundant (N+1, load sharing)** | Several modules share the load on a **common output bus** | Simple, scalable, any one can fail | **Common output bus** and switchgear are a single point of failure |
| **Isolated redundant ("catcher")** | Main UPS systems each carry their own load. A **reserve UPS** carries little or none, and takes over a failed system through a static switch | Independent systems, faults contained | Reserve is idle, switching adds complexity |
| **Block redundant** | Several UPS blocks each serving part of the load, plus a reserve block that any can switch to | One spare covers many blocks | More switchgear and control |
| **Distributed redundant ("3 to make 2")** | Three UPS systems, each about 2/3 loaded, each load fed from two of them | Less spare capacity than 2N | Complex distribution, dual-fed loads |
| **2N (system plus system)** | Two completely separate UPS systems A and B | Fault tolerant, independent | Highest cost, each side about 50% loaded |
| **2(N+1)** | Two systems, each with its own spare | Redundancy even during maintenance | Largest cost and footprint |

**Which is "the +1 reserve"?** In the **catcher** design the reserve is **idle**. In **parallel redundant**, the "+1" module is **running** and sharing load.

## 3. Loading per module in normal operation

For **N+1 parallel**, the load per module is N / (N+1):

| N | Modules | Load per module |
| --- | --- | --- |
| 1 | 2 | 50% |
| 2 | 3 | 66.7% |
| 3 | 4 | 75% |
| 4 | 5 | 80% |
| 5 | 6 | 83.3% |

For **2(N+1)**, the load per module is N / (2 × (N+1)):

| N | Modules (2 × (N+1)) | Load per module |
| --- | --- | --- |
| 1 | 4 | 25% |
| 2 | 6 | 33.3% |
| 3 | 8 | 37.5% |
| 4 | 10 | 40% |

For **2N** (N modules per side): the load per module is **50%** of its rating. For **distributed (3 to make 2)**: about **66.7%**.

**Lesson:** more redundancy means **lower loading per module**, and **UPS efficiency usually falls at light load**. Redundancy costs twice: to buy, and in efficiency (higher PUE).

## 4. Worked example

Load **600 kVA**, modules **200 kVA**, so N = 3.

| Design | Modules | Load per module (normal) | After one module fails |
| --- | --- | --- | --- |
| N | 3 | 100% | Overload |
| **N+1** | 4 | 600/4 = **150 kVA (75%)** | 200 kVA each (100%) on the other 3 |
| **2N** | 6 (3 + 3) | 600/6 = **100 kVA (50%)** | One module lost leaves 5, each at 120 kVA (60%) |
| **2(N+1)** | 8 (4 + 4) | 600/8 = **75 kVA (37.5%)** | Still a spare in each side |

## 5. Choosing

| Requirement | Typical choice |
| --- | --- |
| Basic protection, low cost | N+1 parallel |
| Fault containment, avoid a common bus | Isolated redundant (catcher) or block redundant |
| Fault tolerance, concurrent maintenance | 2N or 2(N+1) |
| Balance of cost and resilience at scale | Distributed redundant |

---

# 6.13 Static transfer switch (STS)

## 1. What an STS is

An **STS** is a **solid-state switch** (thyristors / SCRs, or IGBTs) that moves a load between **two independent live sources** in a **few milliseconds**, with **no moving parts** in the power path.

```
 Source A (UPS A) ──┐
                  [STS] ──► load (single-corded equipment, PDU)
 Source B (UPS B) ──┘
```

## 2. How it works

1. The controller **watches both sources** continuously (voltage, frequency, phase).
2. If the **preferred source** degrades, the controller **fires the thyristors** of the alternate source and blocks the preferred one.
3. The transfer completes within **about a quarter of a cycle**: typically **under 4 ms**, and commonly **4 to 8 ms** on a 50 Hz system **[CHECK]**.
4. It **retransfers** when the preferred source is healthy again (often after a delay, to avoid cycling).

**Synchronisation:** to transfer cleanly, the two sources must be **in phase (synchronised)**. Out-of-phase sources (for example two unsynchronised UPS outputs) can cause **inrush** in downstream transformers and large transient currents.

## 3. Why speed matters: the ITIC / CBEMA curve

IT power supplies can **ride through a loss of voltage of about 20 ms** **[CHECK]**, and often **10 to 20 ms** at full load. An **STS** (4 to 8 ms) is **inside** that limit, so the load **never notices**. An **ATS** (40 to 200 ms) is **far outside** it. (The curve is covered in 06-3.)

## 4. ATS vs. STS vs. UPS static bypass

| | **ATS** | **STS** | **UPS static bypass** |
| --- | --- | --- | --- |
| **Switches** | Utility ↔ generator | Between **two UPS-fed** sources | One UPS ↔ raw utility |
| **Technology** | Electromechanical | Solid-state | Solid-state, inside the UPS |
| **Transfer time** | tens to hundreds of ms | **a few ms** | a few ms |
| **Position** | Upstream, near the main board | Downstream, at the PDU or distribution level | Inside the UPS |
| **Protects** | The building's source | A load needing two conditioned sources | One UPS in overload or fault |
| **Gives a single-corded load a second conditioned source** | No | **Yes** | **No** |

## 5. Where an STS is used

| Use | Detail |
| --- | --- |
| **Single-corded equipment** | A device with one power cord can be fed from two UPS paths through an STS, giving it A/B resilience |
| **PDU input** | The STS sits ahead of a PDU or distribution board so the whole downstream load gets two sources |
| **Rack level** | A smaller **rack-mounted ATS/STS** serves individual single-corded devices |

**When you don't need one:** **dual-corded servers** plug one supply into the A path and the other into the B path, so they already have two sources **without** an STS.

## 6. Design points

| Point | Detail |
| --- | --- |
| **3-pole or 4-pole** | Depends on the earthing arrangement, as for the ATS. With two separately derived sources each bonded at its own source, a **4-pole (switched neutral)** STS keeps a single neutral-earth bond in the active path |
| **Maintenance bypass** | An STS is a **single point of failure** unless it can be bypassed. Specify a **make-before-break** manual bypass |
| **Fault withstand** | The thyristors must withstand the available fault current until a breaker clears it |
| **Efficiency and heat** | Very efficient (about 99.5 to 99.9%), but the thyristors still dissipate heat that needs ventilation **[CHECK]** |
| **Transformer inrush** | An STS **before a transformer** that switches between unsynchronised sources can trigger inrush. Use inrush control or place the STS on the **secondary side** |
| **Monitoring** | Modbus, SNMP and dry contacts, plus waveform capture |
| **Preferred source and retransfer settings** | Set to avoid cycling |

## 7. Tier relevance

| Tier | STS use |
| --- | --- |
| **III** | Concurrent maintainability with dual UPS paths, bypass-isolation ATS, STS for single-corded equipment |
| **IV** | Fault tolerance, normally 2N distribution, with STS units for any single-corded equipment |

---

# 6.14 Redundancy options III: dual path and the STS **[SLIDE]**

## 1. The design on your slide

Your slide ("In the building: redundancy options (cont.)") shows two identical chains. Each has a **transformer**, a **generator**, an **ATS** and **two UPS units in parallel**. The **UPS outputs are cross-connected** so that **each STS is fed by both chains**, and the two **STS** units feed outputs **A** and **B** to the data hall.

The slide's remark: it is **not preferred due to the higher component count, which leads to increased maintenance, cost and potential failure rate.**

## 2. What can fail

| Failure | Result |
| --- | --- |
| Utility fails on one chain | ATS starts that chain's generator. UPS batteries cover the gap |
| One UPS unit fails | The other in the pair carries the load |
| A whole chain fails | The STS moves to the other chain's UPS output, and A and B stay live |
| One STS fails | That feed is lost, but dual-corded equipment keeps running on the other |
| Planned maintenance on any part | Isolate it while the rest carries the load |

## 3. What the redundancy level is

- **At system level it is 2N** (two independent chains).
- The **UPS stage is 2(N+1)** if one UPS can carry the whole chain's load (a spare in each chain), or just 2N if both UPS units are needed.
- Everywhere else (transformer, generator, ATS, STS) each chain has a **single unit**.

## 4. Counting components

| Design | Main components | Count |
| --- | --- | --- |
| **The slide's design** | 2 transformers, 2 generators, 2 ATS, 4 UPS, 2 STS | **12** |
| **Simple 2N (no cross-connection, no STS)** | 2 × (1 transformer, 1 generator, 1 ATS, 2 UPS) | **10** |

The cross-connection adds **STS units, switchgear, cabling and control complexity**, each one something to buy, maintain and that **can fail or be operated wrongly**.

## 5. Reliability: why more components can reduce availability

**Series** components (all must work) **multiply** their availabilities. **Parallel** (redundant) paths **share** failure risk.

**Worked example.** Each component is **99.9%** available. One chain of **five** components in series:

```
Chain availability = 0.999⁵ = 0.99501 → 99.50%
```

Two **independent** chains in parallel (2N):

```
Unavailability of one chain = 1 − 0.99501 = 0.00499
Both fail together          = 0.00499² = 0.0000249
Availability                = 1 − 0.0000249 = 99.9975%
```

That is a big gain. But now add an **STS** (99.9%) **in series** after the 2N arrangement, for a single-corded load:

```
Total = 99.9975% × 99.9% = 99.8975% → about 99.90%
```

The STS has become a **single point of failure** and **caps the availability near 99.9%**. This is why **dual-corded equipment** (which needs no STS) is preferred, and why an STS needs a **bypass** or duplication.

**Caution:** this calculation assumes **independent** failures. Real systems also suffer **common-mode** failures and **human error**, so the true figure is lower. Treat it as a way to compare designs, not as a prediction.

## 6. Why simpler designs are often preferred

| Factor | Cross-connected design | Simple 2N |
| --- | --- | --- |
| **Component count** | Higher | Lower |
| **Cost** | Higher | Lower |
| **Maintenance** | More to service and test | Less |
| **Operation** | More switching states, more human error risk | Simpler |
| **Single points of failure** | STS units | None with dual-corded loads |
| **Resilience** | Very high | Very high for dual-corded loads |

## 7. Options compared

| Option | Description | Cost | Resilience |
| --- | --- | --- | --- |
| **Single path (N+1)** | One path, redundant components | Lowest | Tier II or III style |
| **Single path with maintenance bypass** | As above, with bypasses | Low | Tier III style |
| **2N dual path (A/B)** | Two independent paths, dual-corded loads | High | Tier IV style |
| **2N with cross-connect and STS (your slide)** | Cross-connected UPS, STS before the load | Highest | Highest, but more complex |
| **2(N+1)** | Dual path with a spare in each path | Very high | Tier IV style, tolerates a failure during maintenance |

## 8. Dual-corded equipment and A/B feeds

- **Dual-corded servers** have **two power supplies**, one on each path. Either can carry the whole server.
- Keep **A and B physically separate** (rooms, cable routes, trays).
- Size **each path for the full load**, even though each normally carries half.
- Use **STS or rack ATS** only for **single-corded** equipment.

---

## Glossary

| Term | Meaning |
| --- | --- |
| PCC | Point of common coupling: boundary with the utility network |
| Main-tie-main | Two incomers with a normally open tie between buses |
| Microgrid | Local generation, storage and loads with a controller, able to island |
| REF / CUE | Renewable Energy Factor / Carbon Usage Effectiveness |
| Capacity factor | Actual energy ÷ (rated power × hours) |
| PPA | Power purchase agreement |
| SMR / HALEU | Small modular reactor / high-assay low-enriched uranium |
| EN 50160 | European standard for voltage characteristics of public networks |
| uk (%) | Transformer impedance (short-circuit voltage) |
| Vector group | Winding connection and phase shift, for example Dyn11 |
| ESP / LTP / PRP / COP | ISO 8528-1 generator ratings |
| NFPA 110 Level 1 Type 10 | Emergency power that must supply loads within 10 seconds |
| Wet stacking | Unburned fuel and soot from light-load diesel running |
| ATS | Automatic transfer switch |
| Open / closed / delayed transition | Break-before-make / make-before-break / with a neutral pause |
| Bypass-isolation | A second path that lets the ATS be serviced while the load is on |
| STS | Static transfer switch (solid-state, a few ms) |
| Catcher | An idle reserve UPS that takes over a failed system |
| Dual-corded | Equipment with two power supplies on separate paths |

## Exam takeaways

**Incoming power (6.1)**

- Large loads connect at **MV or HV** because current falls as voltage rises.
- Diverse feeds: **single, dual from one substation, dual from different substations** (best). **Main-tie-main** at the site.
- Agree **capacity, fault level, power factor, harmonic limits and lead time** with the utility.

**Renewables, microgrids, nuclear (6.2 to 6.4)**

- **Capacity factor** explains why solar and wind need large capacity. **Annual** vs. **hourly (24/7)** matching.
- Renewables **don't replace** the UPS and generator.
- A **microgrid** can **island**. It has generation, storage, loads, a **controller** and a **PCC**.
- **Nuclear**: firm 24/7, but **no SMR supplies a data centre commercially yet** (first about 2030). Challenges: licensing, cost, fuel (HALEU), timeline.

**Power quality, requirements, route, transformers (6.5 to 6.8)**

- EN 50160: **±10%** voltage for 95% of the week, **THD ≤ 8%**, **50 Hz ±1%** for 99.5% of the year. It is a **minimum**.
- **Total power = IT load × PUE.** Then apply PF and growth. **Redundancy increases installed capacity.**
- **Higher voltage means lower current and lower losses.** The transformer room sits next to the LV board.
- **Fault current = In / uk.** Cast resin indoors, oil-filled outdoors or in bunded rooms. **Dyn11** = delta, star with neutral, 30° shift.

**Redundancy and transfer equipment (6.9 to 6.14)**

- **N, N+1, 2N, 2(N+1), 2N+1.** A common bus, shared fuel and controls are **common-mode** risks.
- **Generators (ISO 8528-1:2018):** ESP (about 200 h/yr), LTP (about 500 h/yr), PRP (unlimited, 70% average), COP (unlimited, constant), DCP (unlimited, no average-load cap). **NFPA 110 Level 1 Type 10 = within 10 seconds.** Slide sizing: **UPS × 1.0 or 1.2 + cooling and lighting × 1.0.** Test monthly at 30% load or more.
- **ATS:** utility to generator, **open** (brief gap), **delayed** (neutral pause for motors), **closed** (under 100 ms parallel). **4-pole** when the generator has its own neutral-earth bond. **Bypass-isolation** for concurrent maintenance. Size at 125% of load.
- **STS:** solid-state, **a few ms**, between **two UPS-fed sources**. Needs **synchronised** sources. Itself a **single point of failure** without bypass.
- **UPS level:** parallel (common bus weakness), catcher (idle reserve), distributed (3 to make 2), 2N, 2(N+1). **N+1 load = N/(N+1).**
- **Your slide:** 2N overall, **not preferred** because of **component count** (12 vs. 10), maintenance, cost and failure rate. An STS in series **caps availability**.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **EN 50160** | Voltage characteristics of the public supply |
| **IEC 61000-4-30**, **IEEE 1159**, **IEEE 519** | Power quality measurement, definitions and harmonics |
| **IEC 60076**, **IEC 60076-11** | Power transformers and dry-type transformers |
| EU Ecodesign regulation | Transformer efficiency |
| **ISO 8528-1:2018** | Generator ratings: COP, PRP, LTP, ESP, DCP |
| **ISO 8528-5** | Generator transient performance classes |
| **NFPA 110** | 10-second start (Level 1, Type 10), testing |
| **UL 1008**, **IEC 60947-6-1** | Transfer switches |
| **IEEE 1547**, **IEEE 2030.7 and 2030.8**, **IEC TS 62898** | Microgrids |
| **ISO/IEC 30134** | PUE, REF and CUE |
| **Uptime Institute Tier Standard** | Redundancy classes |
| **NFPA 70** (NEC) | 80% and 125% continuous-load margins |
| Public announcements and agency reporting (to October 2026) | Status of nuclear power for data centres |
| **EPI slides** | Generator sizing, source to destination, dual-path redundancy |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
