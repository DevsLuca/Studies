# Module 10: Water Supply

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section |
| --- | --- | --- |
| 10.1 | Importance of Water | [Section 1](#101-importance-of-water) |
| 10.2 | Water Storage Tank | [Section 2](#102-water-storage-tank) |
| 10.3 | Well Water | [Section 3](#103-well-water) |
| 10.4 | Retention Pond | [Section 4](#104-retention-pond) |
| | Putting it together: building a backup water supply | [Section 5](#105-putting-it-together-building-a-backup-water-supply) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-10-water-supply) |

**Objectives (from your slide).** After this module you should be able to describe and understand:

- The importance of water for the data centre operations
- The usage of back up supply at various installations
- Options for creating a backup water supply system

| Objective | Where it is covered |
| --- | --- |
| **Importance of water for data centre operations** | 10.1 |
| **Usage of backup supply at various installations** | 10.1 (section 1.8), 10.2 and the summary in section 5 |
| **Options for creating a backup water supply system** | 10.2 (tanks), 10.3 (wells), 10.4 (ponds), and section 5 (all options compared) |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Only the **objectives slide** was available for this module (not the lesson slides), so check the glossary and figures against your course. Related earlier material: cooling systems and the evaporation physics (Module 9 and `09a_thermal_physics_foundations.md`), the 12-hour fuel and makeup-water rules in the Uptime Tiers (Module 2), fire protection (Module 12) and site selection (Module 3).

## The big picture

Water is a **utility**, like power. Many data centres cannot reject their heat without it, so a **loss of water supply behaves like a loss of power**: cooling capacity falls, and temperatures climb within minutes to hours. Just as the power chain has a generator and fuel tank behind the utility, the water supply needs **backup**: on-site storage first, then independent sources.

```
Public mains (primary) ──► on-site storage tanks ──► treatment ──► pumps ──► cooling towers / chillers / fire system
                 ▲                    ▲
   second source: well, pond, rainwater, tanker delivery, reclaimed water
```

---

# 10.1 Importance of water

## 1.1 What water is used for in a data centre

| Use | Notes |
| --- | --- |
| **Cooling (heat rejection)** | By far the largest use. **Cooling towers** and **evaporative or adiabatic coolers** evaporate water to reject heat (9.5). **Makeup water** replaces what evaporates and what is drained as blowdown |
| **Closed loops** | Chilled water and liquid-cooling loops need an initial fill and small top-ups (Module 9) |
| **Humidification** | Where humidity control is used, for static control (Module 9) |
| **Fire protection** | Sprinklers, hydrants and hose connections, normally with a **dedicated reserve** (Module 12) |
| **Domestic and sanitary** | Staff, toilets, kitchens, cleaning |
| **Landscape and site** | Irrigation (often the first use to be cut in a shortage) |
| **Generator and plant cooling** | Closed-loop radiators need coolant, some plants use water |
| **Water treatment and blowdown** | Treatment chemicals and the discharge of concentrated water |

**Cooling dominates.** For a data centre that uses evaporative cooling, almost all of the site's water goes to heat rejection. Humidification, domestic use and irrigation are small by comparison.

## 1.2 Why a water loss is a serious event

- A cooling tower cools by **evaporating water**. With no makeup water the basin level falls, the tower can no longer reject heat, the chillers' condenser temperature rises, and they trip on high pressure.
- The result is the same as a cooling failure: **temperatures rise in seconds to minutes** (9.1).
- Water supply can fail through a **main break, a treatment plant outage, drought restrictions, contamination or a power failure at the pumping station**.
- Water-related risks also include **regulatory limits** (permits, bans on potable water for cooling) and **community and reputational pressure**.

The **Uptime Institute** treats the loss of public utility water as a **design condition**, in the same way that the loss of utility power is (see 1.8).

## 1.3 How the physics sets the demand

(Detailed derivation in `09a_thermal_physics_foundations.md`, section 10.) Evaporating water absorbs about **2,450 kJ/kg**. So the **minimum** water needed to reject heat by evaporation is:

```
3,600 kJ per kWh ÷ 2,450 kJ/kg = about 1.47 litres per kWh of heat rejected
```

### Worked example: makeup water for 1 MW of IT load

Assume the chillers have a COP of 5 and **all** the heat is rejected by evaporation (the worst case, no free cooling):

```
Heat rejected = 1,000 + 1,000 / 5 = 1,200 kW
Evaporation   = 1,200 / 2,450 = 0.49 kg/s = about 1.76 m³/h
```

An evaporating tower also **concentrates the minerals** left behind. To keep them in check, some water is drained as **blowdown**. The **cycles of concentration (C)** say how many times the dissolved solids are concentrated compared with the makeup water:

```
Blowdown (B) = Evaporation (E) / (C − 1)
Makeup (M)   = E + B = E × C / (C − 1)
```

| Cycles of concentration | Makeup as a multiple of evaporation | Makeup for 1 MW IT (m³/h) |
| --- | --- | --- |
| 3 | 1.50 | 2.64 |
| **4** | **1.33** | **2.35** |
| 5 | 1.25 | 2.20 |
| 6 | 1.20 | 2.12 |

More cycles means less blowdown and makeup, but needs **better water quality** and treatment. Cycles of 3 to 6 are typical **[CHECK]**.

For the worst case at C = 4: **2.35 m³/h per MW of IT load**, or about **56 m³ per day**, or up to about **20,600 m³ per year** if the towers ran at that rate all year. Real sites use economisers, so their annual figure is lower (see the WUE below).

## 1.4 How much water do data centres use

| Measure | Figure **[CHECK]** |
| --- | --- |
| **US data centres, direct (on-site) water consumption, 2023** | About **66 billion litres (17.4 billion US gallons)**, up from 21.2 billion litres in 2014 (LBNL 2024) |
| **Indirect water** (consumed at power stations to make their electricity), 2023 | Nearly **800 billion litres**, about **12 times** the direct figure |
| **Share of direct use** | About **84%** by hyperscale and colocation facilities |
| **Typical grid water intensity** | About **4.5 litres per kWh** of electricity (US average, 2023) |
| **Operator disclosures** | Fleet WUE of about **0.27 L/kWh** (Microsoft, FY2025), **0.12** (AWS, 2025, withdrawal basis), **0.19** (Meta, withdrawal basis). These bases differ, so don't compare them without checking |
| **Operators that track water** | A 2016 Uptime Institute analysis found **fewer than one third** of operators tracked water use or WUE |
| **Source of the water** | An estimated **57%** of data centres use potable (drinking-quality) water |

## 1.5 Water Usage Effectiveness (WUE)

**WUE** (defined in **ISO/IEC 30134-9**, introduced by The Green Grid in 2011) is the water counterpart of PUE:

```
WUE (site) = annual site water consumption (litres) / annual IT energy (kWh)        [L/kWh]
```

| Term | Meaning |
| --- | --- |
| **Withdrawal** | Water drawn from a source (mains, well, river) |
| **Discharge** | Water returned (to a sewer or river) |
| **Consumption** | Withdrawal minus discharge: water that does **not** come back, mostly **evaporated** |
| **Site WUE** | Counts only the water used at the facility |
| **Source WUE** | Adds the water consumed at the power plants that generate the facility's electricity |

### Worked example: a 5 MW site

```
IT energy = 5,000 kW × 8,760 h = 43.8 GWh per year
At WUE 1.8 L/kWh (evaporative design):  43.8 × 10⁶ × 1.8 = 78.8 million litres = 78,800 m³ per year (216 m³/day)
At WUE 0.36 L/kWh (the US fleet average): 43.8 × 10⁶ × 0.36 = 15.8 million litres = 15,800 m³ per year
```

LBNL puts the US fleet average site WUE at just over **0.36 L/kWh** through 2023, projected to rise to **0.45 to 0.48 L/kWh** by 2028, partly because of more water use by liquid-cooled systems. The **Climate Neutral Data Centre Pact** targets **0.4 L/kWh by 2040**.

## 1.6 Water versus energy: the trade-off

A design that uses less water on site often uses **more electricity**, which moves the water use to the **power station**. Compare two designs for the 5 MW site, using **4.52 L of water per kWh of electricity** at the power plant (the US average):

| | **Air-cooled** (PUE 1.5, WUE 0) | **Evaporative** (PUE 1.3, WUE 1.8) |
| --- | --- | --- |
| Facility energy | 5 × 1.5 × 8,760 = 65.7 GWh | 5 × 1.3 × 8,760 = 56.9 GWh |
| **Site (direct) water** | 0 | **78.8 million litres** |
| **Power-plant (indirect) water** | 65.7 × 10⁶ × 4.52 = **297 million litres** | 56.9 × 10⁶ × 4.52 = **257 million litres** |
| **Total water** | 297 million litres | 336 million litres |
| **Source WUE** (total ÷ 43.8 GWh) | 6.8 L/kWh | 7.7 L/kWh |

Totals are close, but the **local** picture is very different: the evaporative site draws a large volume from the **local** supply, while the air-cooled site's water is consumed elsewhere. **A low site WUE is not automatically better.** Compare **WUE together with PUE**, and consider **where** the water is consumed and how stressed that supply is.

## 1.7 Cooling design and water use

| Cooling design | Typical site water use |
| --- | --- |
| **Air-cooled chillers, DX/CRAC, dry coolers** | Effectively **zero** (more electricity) |
| **Closed-loop liquid cooling with dry coolers** | **Near zero** (sealed loops) |
| **Economiser (free cooling) with a trim of evaporation** | Low to moderate |
| **Adiabatic or evaporative assist** | Moderate: water used on hot days only |
| **Water-cooled chillers with open cooling towers** | **High**, about **1 to 2 L/kWh** and above |
| **Direct evaporative (cooling pads)** | High, used in some hyperscale designs |

Evaporative cooling is chosen because it is **energy efficient**, especially in hot climates. The water use is the price.

## 1.8 Backup supply at various installations

How much backup water a site needs depends on **how much water its cooling depends on**.

| Installation | Water dependence | Typical backup supply |
| --- | --- | --- |
| **Small server room, enterprise room with DX (CRAC) cooling** | Almost none for cooling. Domestic and fire water only | Normal mains. Fire water per the building code. No special backup |
| **Medium site with air-cooled chillers or dry coolers** | Closed-loop fill, small top-ups, fire, domestic | A small tank or the closed loop's own volume. Fire reserve |
| **Site with adiabatic or hybrid coolers** | Water on hot days (peak demand) | On-site storage sized for the **hottest day**, plus a second connection or tanker contract |
| **Large site with open cooling towers (colocation, hyperscale)** | **Critical** | **Uptime: at least 12 hours of on-site makeup water storage**, plus an independent second source for longer events (well, pond, rainwater, tanker, reclaimed water) |
| **Liquid-cooled high-density AI hall with dry coolers** | Low (closed loops), but fire and domestic still needed | Fill water and fire reserve. If hybrid evaporative, store peak-day makeup |
| **Tier III or IV site using evaporative cooling** | Critical and certified | The **makeup water system itself** must be **concurrently maintainable** (III) and **fault tolerant** (IV) **to the point of delivery** |

### The Uptime Institute requirement **[CHECK]**

- Where **evaporative cooling** is used, the Tier Standard calls for **on-site makeup water storage for 12 hours**.
- At **Tier III and IV** the makeup water system must also be **concurrently maintainable and fault tolerant** to the point of delivery (so, for example, any tank, pump or pipe can be taken out of service without dropping below the reserve).
- The **loss of public utility water is a design condition**, like loss of power.
- The 12-hour volume is calculated from the **worst-case hour** (hottest, driest weather, where evaporation is greatest) **multiplied by the hours of storage**. A **thermal storage tank** in the chilled water system can also be a source of stored water.
- Compare **fuel**: the Uptime Standard also requires **12 hours of on-site fuel**. (The 72-hour and 96-hour figures often quoted come from ANSI/TIA-942 at Rated-3 and Rated-4 for fuel, and owners commonly design for 24 to 96 hours.)
- Peak (hot-day) demand can be **several times the annual average**, so size the reserve for the **peak**, not the average.

**Worked example (the 12-hour minimum).** A 1 MW IT load, worst case at C = 4:

```
12 h × 2.35 m³/h = 28.2 m³ per MW of IT load      (a 2 MW site: about 56 m³)
```

Published designs quote figures such as "100 m³ or more" for a 2 MW plant, because real design includes the **worst-case weather profile**, **safety margins**, **non-tower uses** and the **fire reserve kept separately** **[CHECK]**.

## 1.9 Water quality

| Topic | Practice |
| --- | --- |
| **Makeup water quality** | Cooling towers need water whose **hardness, alkalinity, dissolved solids, chlorides and silica** suit the chosen cycles of concentration |
| **Treatment** | Filtration, softening or reverse osmosis, **scale and corrosion inhibitors**, **biocides** (algae and bacteria control) |
| **Potable vs. non-potable** | Cooling doesn't need drinking-quality water. **Reclaimed, harvested and recycled water** can be used if treated, with **backflow and cross-connection control** |
| **Legionella** | Warm, stagnant water grows Legionella bacteria. A **water management plan** per **ASHRAE Standard 188** covers towers, tanks and stored water |
| **Closed loops** | Treated water or water-glycol, filtered (Module 9) |
| **Reserve water** | Must be **treated, monitored and turned over**, because water that sits can foul, scale or breed bacteria |

## 1.10 Regulation and community

- Taking water from a **well or river** (self-supply) usually needs a **permit**, and the rules differ by region.
- Some municipalities **restrict potable water for data centre cooling**. For example, one US town adopted an ordinance in 2024 stating that its water department will not provide potable water to a data centre for cooling or humidity control **[CHECK]**.
- **Discharge** of cooling tower blowdown needs approval (in the US an NPDES permit).
- Operators increasingly **report WUE** and set targets, and communities and regulators ask for the figures.

---

# 10.2 Water storage tank

## 2.1 Purpose

An on-site **water storage tank** is the **first line of backup**: it keeps the cooling plant running while the public supply is interrupted, and gives the operator time to switch to another source. It is the water equivalent of the generator's **fuel tank**.

| Role | Notes |
| --- | --- |
| **Cooling makeup reserve** | The Uptime 12-hour minimum (10.1) is held here |
| **Buffer** | Smooths the difference between the supply rate and the peak demand rate |
| **Fire reserve** | A **separate, dedicated** volume (below) |
| **Receiving point** | For a well, a pond or a **tanker delivery**, so every source feeds one place |
| **Treatment point** | Filtering, dosing and recirculation happen here |
| **Thermal storage** | A chilled-water storage tank can double as a reserve of stored water |

## 2.2 Sizing

```
Net volume needed = peak makeup rate (m³/h) × autonomy (hours)
Gross volume      = net volume / usable fraction     (dead volume and overflow freeboard are unusable)
Autonomy (hours)  = usable volume / makeup rate
```

### Worked example: a 5 MW IT site

Worst case at C = 4: **2.351 m³/h per MW**:

```
Makeup rate = 5 × 2.351 = 11.76 m³/h  (282 m³ per day)
```

| Autonomy | Net volume needed | Gross at 90% usable |
| --- | --- | --- |
| 12 hours (Uptime minimum) | 11.76 × 12 = **141 m³** | 157 m³ |
| 24 hours | **282 m³** | 313 m³ |
| 72 hours | **846 m³** | 940 m³ |

**Autonomy check.** A tank with **300 m³ usable** and a makeup rate of 11.76 m³/h lasts:

```
300 / 11.76 = 25.5 hours
```

**Ways to stretch autonomy:** switch cooling to a **dry mode** (dry coolers, no evaporation) where the plant allows it, **reduce the IT load**, or reduce **non-essential water use** (landscape irrigation first). Halving the water use doubles the autonomy.

## 2.3 How many tanks: concurrent maintainability

For Tier III the storage must be **concurrently maintainable**: any tank can be taken out of service (for cleaning or repair) **without dropping below the required reserve**.

**Worked example.** The required reserve is **28.2 m³** (12 hours for 1 MW):

| Arrangement | Calculation | With one tank out |
| --- | --- | --- |
| **One tank of 28.2 m³** | Not acceptable | 0 m³ (no reserve) |
| **Two tanks of 28.2 m³ each (2N)** | 56.4 m³ total | 28.2 m³ (meets the reserve) |
| **Three tanks of 14.1 m³ each (N+1)** | 42.3 m³ total | 28.2 m³ (meets the reserve) |

The N+1 arrangement uses less total volume. The **pumps, valves and pipes** between the tanks and the towers must also be redundant, so a valve or pump failure doesn't isolate the reserve.

## 2.4 Types of tank **[CHECK]**

| Type | Characteristics |
| --- | --- |
| **Bolted steel** (glass-fused, epoxy-coated, powder-coated or galvanised panels, with a liner) | Large volumes (single tanks up to roughly **2,650 m³ / 700,000 US gallons** in one vendor's range), erected on site, can be relocated. The usual choice for large reserves |
| **Corrugated galvanised steel with a liner** | Large volume at low cost per litre. Liners of PE or PVC rated for potable contact (NSF/ANSI 61) |
| **Fibreglass (FRP)** | Corrosion-free, built to **AWWA** standards, above or below ground, typically up to about 300 m³ |
| **Polyethylene, polypropylene, HDPE** | Small tanks: chemical and day tanks, small reserves |
| **Concrete** (cast in place or precast) | Very large and long-lived, often below ground. Needs a good foundation and waterproofing |

Check the **wind, snow and seismic ratings**, the **liner and coating** (potable contact, chemical resistance), and the **fire rating** where the tank holds fire water (**NFPA 22**).

## 2.5 Above ground or below ground

| | **Above ground** | **Below ground** |
| --- | --- | --- |
| **Cost** | Lower | Higher |
| **Footprint** | Larger surface area | Frees the surface (parking, landscaping) |
| **Temperature** | Exposed to sun and frost (insulation or heating may be needed) | Stable, cooler water, no freezing |
| **Inspection and maintenance** | Easy | Harder, confined space entry |
| **Risks** | Wind, vandalism, seismic sloshing | **Flotation** if the water table is high, groundwater contamination, leaks hard to see |
| **Delivery** | Often needs pumps unless raised | Needs pumps |

## 2.6 Fittings and features

| Feature | Purpose |
| --- | --- |
| **Inlet with backflow prevention (air gap)** | Prevents contamination of the mains |
| **Overflow and drain** | Safe overflow and complete emptying for cleaning |
| **Vent with insect and dust screen** | Allows air movement, keeps contaminants out |
| **Access manway, lockable** | Inspection and security |
| **Level instruments** (redundant) and **alarms** (low, low-low, high) | Early warning and automatic refill. Connect to the BMS |
| **Recirculation loop with treatment connection** | Chlorination, filtration, UV, so the water doesn't stagnate |
| **Sampling points** | Water quality checks |
| **Cover** | Reduces algae, dust and evaporation |
| **Insulation or heating** | Frost protection (and heat protection, since warm water breeds bacteria) |
| **Pumps (N+1) on emergency power** | The reserve is useless if its pumps stop when the grid fails |
| **Automatic changeover** | Switches from mains to the tank when pressure drops |
| **Tanker fill connection** | A quick-connect inlet for emergency delivery (below) |
| **Flow meters** | Track use, support WUE reporting |
| **Isolation valves** | Allow concurrent maintenance |

## 2.7 Keeping stored water healthy

Water that sits for a long time **goes stale, grows bacteria and fouls equipment**.

```
Residence time (days) = tank volume (m³) / daily use (m³/day)
```

**Worked example.** A reserve of **169 m³** (72 hours for 1 MW) at a normal daily use of **56 m³** has a residence time of:

```
169 / 56 = about 3 days
```

If the site is partly free-cooled and uses only 20% of that on average, the water may sit **15 days or more**. So:

- **Recirculate and treat** the stored water continuously.
- **Turn over** the volume regularly, for example by using the tank as the **normal feed** to the towers, not an idle reserve.
- Keep the water **cool** (warm, stagnant water favours **Legionella**), and manage the whole system under an **ASHRAE Standard 188** water management plan.
- **Clean and inspect** the tank on a schedule (commonly annually) **[CHECK]**.

## 2.8 Fire water is separate

The **sprinkler and hydrant reserve** is a **dedicated volume**, sized by the fire design (flow rate × duration, per **NFPA 13/22** and the authority having jurisdiction). It is **not** counted towards the cooling reserve, and the cooling system must **not** be able to drain it.

**Illustration.** A fire design of **1,900 L/min** (about 500 gpm, including hose streams) for **60 minutes**:

```
1,900 × 60 = 114,000 litres = 114 m³ (reserved for fire only)
```

## 2.9 Tanker delivery

As an **emergency measure**, water can be delivered by road tanker into a **tanker fill connection** at the tank.

**Worked example.** The 5 MW site uses **282 m³ per day** at full evaporative load. A tanker carries **30 m³**:

```
282 / 30 = 9.4 truckloads per day (about one every 2.5 hours, around the clock)
```

So tanker delivery is a **bridge** to buy time, not a long-term source, and it needs a **pre-arranged contract**, an **approved water source** and a **delivery route** that works in the same emergency.

## 2.10 Pros and cons of storage as backup

| Pros | Cons |
| --- | --- |
| **Independent of the network** and available instantly | **Finite** autonomy (hours to days) |
| Predictable, easy to size and test | Capital cost and **footprint** (a 72-hour reserve for 5 MW is about 850 m³) |
| Gives time to bring in a second source | Water quality needs active management |
| Required by the Uptime Tier Standard for evaporative sites | Needs redundant pumps, power and controls |

---

# 10.3 Well water

## 3.1 What it is

A **well** draws water from an **aquifer** (underground water-bearing rock or gravel). It can be a **primary source** where there is no adequate municipal supply, or an **independent backup** to the public mains, because it doesn't depend on the municipal network.

## 3.2 Aquifer basics

| Term | Meaning |
| --- | --- |
| **Aquifer** | Rock or sediment that holds and yields usable groundwater |
| **Water table** | The top of the saturated zone |
| **Yield** | The flow a well can deliver, in L/s, m³/h or gpm (1 gpm = 0.227 m³/h) |
| **Drawdown** | How far the water level falls in the well when pumping |
| **Cone of depression** | The funnel-shaped fall in the water table around a pumping well, which can affect **neighbouring wells** |
| **Recharge** | Water entering the aquifer (rainfall, rivers). **Sustainable yield** can't exceed it |

## 3.3 Investigation before relying on a well

A well is a **design that must be proven**, not assumed. Typical steps **[CHECK]**:

1. **Desk study** of geology and nearby drillers' records (these estimates are not reliable on their own).
2. **Test boring**, and a **test well** where the geology looks promising.
3. **Pump tests**: a **step-drawdown test** and a long **constant-rate test** (for example 36 hours) to measure real yield and drawdown.
4. **Water quality baseline**: hardness, iron, manganese, dissolved solids, chlorides, silica, bacteria.
5. **Impact assessment** of neighbouring wells, streams and the aquifer.
6. **Permits and water rights** (usually state or local), which can take **months to years**.
7. **Monitoring wells** to track the effect of pumping (often required).

## 3.4 Yield and sizing

Yields vary enormously with geology: some formations give **100 to 200 gpm (23 to 45 m³/h)** per well, while productive aquifers support **500 to 2,000 gpm or more (114 to 454 m³/h)** from high-capacity production wells **[CHECK]**.

**Conversion check.** 150 gpm = 150 × 3.785 L × 60 = **34.1 m³/h**.

### Worked example: how much IT load can a well support?

Makeup demand is **2.35 m³/h per MW of IT load** (worst case, C = 4):

| Well yield | m³/h | IT load supported |
| --- | --- | --- |
| 100 gpm | 22.7 | 22.7 / 2.35 = **about 9.7 MW** |
| 200 gpm | 45.4 | 45.4 / 2.35 = **about 19.3 MW** |

A **10 MW** site (peak makeup 23.5 m³/h) could be served by **one 200 gpm well**, but a single well is a **single point of failure**, so plan **N+1 wells** (two or more), each able to carry the load.

### Wells plus a tank

A **tank smooths** the difference between peak demand and well yield, so the well can be smaller than the peak.

**Worked example.** Peak demand **25 m³/h**, well yield **15 m³/h**, tank **100 m³**:

```
Deficit = 25 − 15 = 10 m³/h
Time the tank covers the peak = 100 / 10 = 10 hours
```

This works only if the peaks are shorter than the tank can cover, and the well can refill it afterwards.

## 3.5 Pumping and power

The well pump must **keep running on emergency power**, or the backup fails when the grid does.

```
Pump power = ρ × g × Q × H / η
```

**Worked example.** A pump delivers **45 m³/h** (0.0125 m³/s) against a total head of **60 m**, at **60%** efficiency:

```
P = 1,000 × 9.81 × 0.0125 × 60 / 0.6 = about 12.3 kW
```

Use **submersible pumps** (often on variable-frequency drives), **duplicate pumps**, controls and telemetry, and include the pump load in the generator sizing.

## 3.6 Water quality and treatment

| Issue | Effect | Treatment |
| --- | --- | --- |
| **Hardness** (calcium, magnesium) | Scale on heat exchangers and tower fill | Softening, antiscalants, reverse osmosis |
| **Iron and manganese** | Staining, fouling, clogging | Aeration and filtration |
| **High dissolved solids, chlorides** | Limit cycles of concentration, corrosion | Reverse osmosis, blowdown control |
| **Silica** | Hard scale | Reverse osmosis, cycles limit |
| **Bacteria and biofouling** | Fouls the well, creates Legionella risk | Disinfection, ASHRAE 188 plan |

Groundwater temperature is usually **stable and cool** (often about 10 to 15 °C) **[CHECK]**.

## 3.7 Risks and limits

| Risk | Detail |
| --- | --- |
| **Aquifer depletion and drawdown** | Heavy pumping lowers levels, especially in drought or heavily developed regions |
| **Impact on neighbours** | Other wells, farms and streams may be affected, which draws regulatory and community attention |
| **Land subsidence** | In some formations, over-pumping makes the ground settle |
| **Permits and water rights** | Self-supply usually needs a permit, and the rules differ by region and may restrict volumes |
| **Variable yield and quality** | Drought, changing water quality, well fouling |
| **Pump or well failure** | A single well is a single point of failure |
| **Discharge** | Blowdown to the environment needs a permit |
| **A well that is never used fails when needed** | **Exercise** the backup well and its pumps regularly, test water quality, and maintain it |

## 3.8 Wells as a heat sink

Groundwater can also be used as a **heat sink** rather than a consumable supply. In a **pump-and-inject** system, water is pumped from a supply well, passes through a heat exchanger, and is **returned to the aquifer** through an injection well, so **net consumption is zero**. Such systems need as little as **2 gpm per ton** of cooling:

```
1 MW = 1,000 / 3.517 = 284 tons
284 × 2 gpm = 568 gpm = 129 m³/h
Temperature rise = 1,000 kW / (4.186 × 35.8 kg/s) = about 6.7 K
```

(See also seasonal storage, 9.16 in `09_cooling_infrastructure.md`.) The supply and injection wells must be far enough apart that the returned water doesn't **short-circuit**, and both need permits.

## 3.9 Pros and cons of wells

| Pros | Cons |
| --- | --- |
| **Independent** of the municipal network | Needs an **aquifer**, which isn't available everywhere |
| Can supply large volumes and **continuous** flow | **Long investigation and permitting**, and cost of drilling and testing |
| Cool, stable water temperature | Treatment needed, quality can change |
| Can be both primary and backup | Environmental and community concerns |
| Reduces dependence on the public supply | Pumps need emergency power. A single well is a single point of failure |

---

# 10.4 Retention pond

## 4.1 Terms

| Term | Meaning |
| --- | --- |
| **Detention pond (dry pond, detention basin)** | **Normally dry.** Holds stormwater **temporarily** and releases it slowly through an outlet, to control the **peak flow** leaving the site |
| **Retention pond (wet pond)** | Keeps a **permanent pool** of water. Stormwater enters, displaces water, and leaves through a controlled outlet. The pool also **treats** the water (sedimentation, biological uptake) |
| **Rainwater harvesting** | Collecting roof runoff in tanks or cisterns |
| **Stormwater harvesting** | Collecting runoff from paving and the site, usually needing more treatment |

The words differ by region: in some places a "retention" pond is one that holds water until it **soaks away or evaporates**, and a "detention" pond is one that releases it through an outlet. Check the local usage.

A data centre has a very high share of **roofs and paving**, so it sheds a lot of stormwater, and **a pond is often required** by the planning rules. The same pond can also become a **water source**.

## 4.2 Sizing for stormwater control

The regulations set a **design storm** (for example the **25-year, 24-hour** or **100-year, 24-hour** storm). The runoff volume by the rational method:

```
Runoff volume = C × rainfall depth × catchment area       (C = runoff coefficient, 0 to 1)
```

**Worked example.** Catchment **5 ha (50,000 m²)**, design storm **120 mm**, **C = 0.85** (mostly impervious):

```
V = 0.85 × 0.120 × 50,000 = 5,100 m³
```

A **detention** pond is sized by the **gap between the inflow and the permitted release rate**, using a routing calculation with the outlet structure. A **retention** pond is sized by the **storage volume above its permanent pool**.

## 4.3 The pond as a backup water source

Treated stormwater or harvested rainwater can supply **cooling tower makeup** as a non-potable source, reducing the draw on the public supply and providing a **supplementary backup**.

### Rainwater yield

```
Annual yield = roof area × annual rainfall × capture efficiency
```

**Worked example.** Roof **20,000 m²**, rainfall **0.8 m per year**, capture efficiency **0.85**:

```
Yield = 20,000 × 0.8 × 0.85 = 13,600 m³ per year = about 37 m³ per day
```

Rainwater has **very low dissolved solids**, which lets the cooling towers run at **higher cycles of concentration**.

### The trap: annual averages hide dry spells

A system that covers the average demand can still **run dry in a drought** while the towers demand most in the **hottest, driest weeks**. Model **capture, demand and storage through a dry period**.

**Worked example.** Average makeup demand **40 m³/day**, a **60-day dry spell**:

```
Storage needed = 40 × 60 = 2,400 m³
Pond area at 3 m depth = 2,400 / 3 = 800 m² (plus side slopes and freeboard)
```

### Evaporation from the pond

An open pond **loses water to evaporation**, commonly about **1.5 m per year or more in hot, dry climates** **[CHECK]**:

```
Annual loss = 800 m² × 1.5 m = 1,200 m³ per year (about 3.3 m³/day)
Loss over the 60-day dry spell = 800 × 1.5 × 60 / 365 = about 197 m³ (8% of the stored volume)
```

So allow **extra volume**, or reduce losses with **covers** or **underground tanks**.

## 4.4 Quality and treatment

Pond water is **not clean**: it carries sediment, nutrients and organic matter, and it **grows algae** in sunlight.

| Measure | Purpose |
| --- | --- |
| **First-flush diversion** | The first runoff of a storm carries the most dirt, so divert it |
| **Sedimentation forebay** | Settles solids before the main pool |
| **Filtration** | Removes suspended solids |
| **Disinfection** (chlorine, UV) | Controls bacteria |
| **Algae control** | Covers, shading, aeration, biocides. Algae and biofilm foul tower fill and heat exchangers |
| **Cross-connection control and backflow prevention** | Keeps non-potable water out of the potable system |
| **Water management plan (ASHRAE 188)** | Legionella control |
| **Monitoring** | Conductivity, pH, turbidity, bacteria |

Standards for rainwater and stormwater systems include **CSA B805 / ICC 805** and **ARCSA/ASPE/ANSI 63** (rainwater catchment) and **78** (stormwater harvesting for direct end use).

## 4.5 Design points

| Topic | Practice **[CHECK]** |
| --- | --- |
| **Location** | At the low point of the site, with the geotechnical report and groundwater level checked |
| **Liner** | Needed in permeable soils (the pond would drain) or sensitive groundwater areas |
| **Embankment and dam safety** | A berm holding more than a few acre-feet may fall under state dam-safety rules (some states trigger review at about 15 acre-feet or 6 feet of head) |
| **Outlet and overflow** | Sized with the volume. An undersized or oversized outlet defeats the design |
| **Intake** | Screened intake and pumps with redundancy and emergency power |
| **Safety and security** | Fencing, signs, wildlife and mosquito control |
| **Maintenance** | Vegetation and algae control, sediment removal (**dredging every 10 to 20 years**), clearing the outlet |
| **Covers or underground storage** | Cut evaporation and algae (vendor claims of 95 to 98% reduction) |
| **Permits** | Stormwater and water-use approvals |

## 4.6 Other on-site sources

| Source | Notes |
| --- | --- |
| **Cooling and air-handler condensate** | Clean, near-distilled water from CRAH and AHU coils, especially in humid climates. Good tower makeup |
| **Blowdown reuse** | Treat the tower blowdown (reverse osmosis) and reuse it |
| **Greywater** | From offices and sanitary facilities, for flushing and irrigation |
| **Reclaimed (recycled) water** | From a municipal wastewater plant through a separate "purple pipe" network |

## 4.7 Pros and cons

| Pros | Cons |
| --- | --- |
| Reduces use of **potable municipal water** | **Depends on rainfall**: drought leaves it empty |
| Often **already required** for stormwater management, so the volume is built anyway | Quality **varies** and needs treatment |
| Low-TDS water allows more cycles of concentration | **Evaporation** and algae |
| Measurable for water reporting and green building credits | Large **land area**, permits and **dam-safety** rules |
| Can be combined with tanks and covers | **Not reliable enough as the sole backup** unless proven through a drought |

---

# 10.5 Putting it together: building a backup water supply

## 5.1 The options compared

| Option | Independent of the mains? | Typical capacity | Response | Main limits | Typical role |
| --- | --- | --- | --- | --- | --- |
| **Dual municipal connections** (from different mains or pressure zones) | Partly (same utility) | Full flow | Immediate | A utility-wide outage or drought affects both | First layer |
| **On-site storage tanks** | **Yes** | 12 to 72 hours | **Immediate** | Finite, needs treatment and pumps | **The required first backup** |
| **Well** | **Yes** | Continuous | Starts in minutes (pump on emergency power) | Needs aquifer, permits, testing, treatment | Independent second source |
| **Retention pond or rainwater harvesting** | **Yes** | Days, rainfall dependent | Needs treatment | Droughts, quality, evaporation | Supplementary source |
| **Reclaimed (recycled) water** | Partly | Large | Continuous | Dependent on the wastewater utility. Quality | Primary or supplementary non-potable source |
| **Tanker delivery contract** | Yes | About 30 m³ per load | Hours | Logistics, quality, roads in a disaster | **Bridge** for long events |
| **Condensate and blowdown reuse** | Yes | Small to moderate | Continuous | Limited volume | Reduces demand |
| **Demand reduction** (dry mode, closed loop, hybrid cooling, load shedding) | n/a | Cuts the need | Immediate | Capacity and efficiency cost | Stretches every other source |

## 5.2 A layered design ("defence in depth")

```
1. Normal supply:       dual municipal connections (different mains)
2. On-site storage:     at least 12 hours (Uptime), commonly 24 to 72 hours
3. Independent source:  well and/or pond/rainwater and/or reclaimed water
4. Emergency delivery:  contracted tankers with a fill connection
5. Demand reduction:    dry mode, reduced load, non-essential uses cut
```

### Worked example: a 5 MW site

| Item | Calculation | Result |
| --- | --- | --- |
| **Peak makeup demand** | 5 × 2.351 (worst case, C = 4) | **11.76 m³/h** (282 m³/day) |
| **Tanks** | Three tanks of 105 m³ usable (N+1) | **315 m³**: 26.8 hours with all in service, **17.9 hours with one out** (above 12 hours) |
| **Wells** | Two wells of 100 gpm (22.7 m³/h) each | One well covers 22.7 / 11.76 = **193%** of the demand (N+1) |
| **Tanker contract** | 282 / 30 m³ | **9.4 truckloads per day** if everything else fails |
| **Dry-mode reduction** | Water use halved | Tank autonomy doubles to about 35 hours with one tank out |
| **Fire reserve** | Separate, per the fire design | Not counted above |

## 5.3 Design checklist

| Question | Why |
| --- | --- |
| Does the **peak** demand (hottest day) drive the sizing, not the average? | Reserves sized to the average fail when needed |
| Are tanks, pumps, valves and power **concurrently maintainable** (Tier III) or **fault tolerant** (Tier IV)? | Uptime requirement for evaporative sites |
| Do the pumps run on **emergency power**? | Backup water needs backup power |
| Is the water **treated and turned over**? | Stagnation and Legionella |
| Is the backup source **proven in a drought** and **tested regularly**? | Wells and ponds fail quietly |
| Is the fire reserve **separate**? | Cooling must not drain it |
| Are **permits and rights** secured for wells, ponds and discharge? | Often the longest part of the schedule |
| Is the **quality** of every source suitable for the towers? | Hardness, solids, bacteria |
| Is there a **tanker contract** and a **fill point**? | Bridge for long events |
| Can the site **reduce water use** in an emergency? | Extends every other source |

---

## Glossary

| Term | Meaning |
| --- | --- |
| Makeup water | Water that replaces evaporation and blowdown in a cooling tower |
| Blowdown | Concentrated water drained from a tower to limit minerals |
| Cycles of concentration (C) | How many times the dissolved solids are concentrated relative to makeup water |
| WUE | Water usage effectiveness: litres of water per kWh of IT energy (ISO/IEC 30134-9) |
| Site WUE / source WUE | On-site water only / including water used at power stations |
| Withdrawal / discharge / consumption | Water taken / returned / not returned (mostly evaporated) |
| Evaporative cooling | Rejecting heat by evaporating water |
| Autonomy | Hours a site can run on stored water |
| Concurrent maintainability | Any component can be taken out of service without reducing the reserve below the requirement |
| Aquifer | Underground rock or sediment that yields groundwater |
| Yield | Flow a well can deliver (m³/h, gpm) |
| Drawdown | Fall of the water level in a pumped well |
| Cone of depression | Funnel-shaped fall in the water table around a pumping well |
| Pump-and-inject | Groundwater pumped through a heat exchanger and returned to the aquifer |
| Detention pond | Normally dry basin that holds stormwater temporarily |
| Retention pond | Wet pond with a permanent pool |
| First flush | The first, dirtiest runoff of a storm |
| Rational method | Runoff = C × rainfall × area |
| Purple pipe | Separate network carrying reclaimed (recycled) water |
| ASHRAE 188 | Standard for Legionella risk management in building water systems |
| NFPA 22 | Standard for water tanks for private fire protection |

## Exam takeaways

**10.1 (importance of water and backup)**

- **Cooling** is the dominant use of water. **Evaporation** rejects heat: minimum about **1.47 L per kWh of heat** (3,600 / 2,450). **Loss of water behaves like loss of power**: towers can't reject heat and temperatures rise in minutes to hours.
- **Makeup = evaporation × C / (C − 1)**; blowdown = E / (C − 1). About **2.35 m³/h per MW of IT** at C = 4 (worst case).
- **WUE = annual site water (L) / IT energy (kWh)** (ISO/IEC 30134-9). US fleet average about **0.36 L/kWh**. Direct US use 2023 about **66 billion litres**, indirect about **12 times** more. **A low site WUE is not automatically better**: compare WUE with PUE and consider the power plant's water.
- **Uptime:** **12 hours** of on-site makeup water for evaporatively cooled sites, **concurrently maintainable (III) and fault tolerant (IV) to the point of delivery**, sized from the **worst-case hour**. **Loss of public water is a design condition.** (Fuel: 12 hours in Uptime, 72/96 hours in TIA-942 Rated-3/4.)
- Backup needs depend on **how much the cooling depends on water**: small DX rooms need little, large evaporative sites need storage plus an independent source.
- Quality: treatment, **ASHRAE 188** for Legionella, backflow protection.

**10.2 (tanks)**

- **Volume = makeup rate × autonomy.** 5 MW: **282 m³ per 24 h**. **Gross = net / usable fraction.** **Autonomy = usable volume / rate.**
- **Concurrently maintainable:** any tank out of service must still leave the required reserve (2N or N+1 tanks, redundant pumps and valves).
- **Fittings:** backflow-protected inlet, overflow, drain, vent screen, redundant level sensors and alarms, treatment and recirculation, sampling, **pumps on emergency power**, tanker fill connection.
- **Residence time = volume / daily use**: stagnation risk. **Fire water is separate** (NFPA 22). **Tanker** delivery is a bridge: 5 MW needs about **9 to 10 truckloads of 30 m³ per day**.

**10.3 (wells)**

- **Prove it first:** test well, **pump tests** (step-drawdown, 36-hour constant rate), quality baseline, impact assessment, **permits**.
- **Yield:** 100 gpm = 22.7 m³/h supports about **9.7 MW** at C = 4. **N+1 wells.** **Pump power = ρ g Q H / η**; the pump needs **emergency power**. A tank buffers peaks.
- **Risks:** drawdown, cone of depression, subsidence, neighbours, permits, quality, **untested backup well**. Treatment for hardness, iron, solids, silica, bacteria. **Pump-and-inject** returns the water (net zero consumption).

**10.4 (retention pond)**

- **Detention** = normally dry, peak-flow control. **Retention** = permanent pool, water quality treatment. Sized for the **design storm** (rational method: C × depth × area).
- As a source: **roof yield = area × rainfall × capture efficiency**. **Model through a dry spell** (annual averages mislead). **Evaporation** from open water (about 1.5 m per year in hot dry climates).
- **Treat:** first-flush diversion, forebay, filtration, disinfection, algae control, backflow protection; **CSA B805 / ICC 805**, **ARCSA/ASPE/ANSI 63 and 78**. Weakness: rainfall dependent, so supplementary.

**Backup options:** dual mains, **tanks (required)**, wells, ponds and rainwater, reclaimed water, tankers, condensate and blowdown reuse, demand reduction. Use **layers**, size for the **peak**, put pumps on **emergency power**, **test** the backup.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **Uptime Institute Tier Standard: Topology** and **Accredited Tier Designer Technical Paper: Makeup Water** (2026) | 12-hour makeup water storage, concurrently maintainable and fault tolerant to the point of delivery, loss of public water as a design condition, worst-case-hour calculation |
| **ISO/IEC 30134-9**, **The Green Grid** | Definition of WUE |
| **LBNL 2024 United States Data Center Energy Usage Report** | Direct and indirect water use, site WUE, 2023 figures |
| Operator sustainability disclosures (Microsoft, AWS, Meta) | Reported WUE values and their bases |
| **Climate Neutral Data Centre Pact** | WUE target of 0.4 L/kWh by 2040 |
| **ASHRAE Standard 188** | Legionella risk management for building water systems |
| **NFPA 22**, **NFPA 13** | Water tanks for private fire protection, sprinkler systems |
| **NSF/ANSI 61** | Materials in contact with potable water |
| **CSA B805 / ICC 805**, **ARCSA/ASPE/ANSI 63 and 78** | Rainwater and stormwater harvesting |
| US Clean Water Act (NPDES permits, Section 316(b)) | Discharge permits and cooling water intakes |
| **Congressional Research Service, *Data Centers and Water: Frequently Asked Questions*** (2026) | Water sources, permitting and reuse |
| **National Ground Water Association / Water Well Journal** (2026) | Aquifer testing, high-capacity wells, pump-and-inject systems |
| **ANSI/TIA-942** | The 72-hour and 96-hour fuel figures (for comparison) |
| Standard hydrology and thermodynamics | Rational method, evaporation physics, cycles of concentration, pump power |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
