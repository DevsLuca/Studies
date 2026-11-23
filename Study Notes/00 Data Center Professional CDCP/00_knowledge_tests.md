# CDCP Knowledge Tests and Practice Questions

All the practice questions from the module notes, grouped by module. Each question has its answer next to it, with the working for calculations.

**How to use this file**

1. Read the module notes first, then come here.
2. **Cover the answer column**, answer each question (write down the working for calculations), then check.
3. Re-do the ones you missed after a day or two.
4. Questions are numbered **within each section**, so a number is only unique inside its own table.
5. Where an answer quotes a figure marked **[CHECK]** in the notes, compare it with your course slides: if your slides give a different number, **use your slides**.

## Contents

| Module | Notes | Questions |
| --- | --- | --- |
| [Module 1: The Mission Critical Site](#module-1-the-mission-critical-site) | `01_mission_critical_site.md` | 20 |
| [Module 2: Data Centre Standards](#module-2-data-centre-standards) | `02_data_centre_standards.md` | 20 |
| [Module 3: Location, Building and Construction](#module-3-location-building-and-construction) | `03_location_building_construction.md` | 25 |
| [Module 4: Raised Access Flooring and Suspended Ceiling](#module-4-raised-access-flooring-and-suspended-ceiling) | `04_raised_floor_suspended_ceiling.md` | 26 |
| [Module 5: Light](#module-5-light) | `05_light.md` | 28 |
| [Module 6: Power Infrastructure](#module-6-power-infrastructure) | `06-1_incoming_power_to_transfer_switches.md`, `06-2_phases_distribution_grounding.md`, `06-3_power_quality_and_sizing.md`, `06-4_ups_and_batteries.md`, `06_power_infrastructure.md`, `06a_electrical_physics_foundations.md` | 283 |
| [Module 7: Electro Magnetic Fields](#module-7-electro-magnetic-fields) | `07_electromagnetic_fields.md` | 76 |
| [Module 8: Equipment Racks](#module-8-equipment-racks) | `08_equipment_racks.md` | 63 |
| [Module 9: Cooling Infrastructure](#module-9-cooling-infrastructure) | `09_cooling_infrastructure.md`, `09a_thermal_physics_foundations.md` | 120 |
| [Module 10: Water Supply](#module-10-water-supply) | `10_water_supply.md` | 60 |
| [Module 11: Designing a Scalable Network Infrastructure](#module-11-designing-a-scalable-network-infrastructure) | `11_network_infrastructure.md` | 92 |
| [Module 12: Fire Protection](#module-12-fire-protection) | `12_fire_protection.md` | 110 |
| [Module 13: Physical Security and Safety](#module-13-physical-security-and-safety) | `13_physical_security_and_safety.md` | 125 |
| [Module 14: Auxiliary Systems](#module-14-auxiliary-systems) | `14_auxiliary_systems.md` | 125 |
| | | **1173 in total** |

All 14 modules are now included.

---

## Module 1: The Mission Critical Site

*Notes: [01_mission_critical_site.md](01_mission_critical_site.md). 20 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Which business layer is at the bottom, and why does its failure affect everything above it? | The site (facility) infrastructure. Every layer above depends on it for power, cooling and protection. |
| 2 | What is the difference between white space and grey space? | White space holds the IT equipment. Grey space holds the support infrastructure (power, cooling, and so on). |
| 3 | What's the difference between colocation and managed hosting? | Colocation: you rent space, power and cooling and bring your own equipment. Managed hosting: the provider owns and runs the hardware for you. |
| 4 | Name three advantages of the cloud model over an enterprise data centre. | Lower up-front cost, faster deployment, easier scaling, less facility responsibility. |
| 5 | Roughly how much downtime per year does 99.99% availability allow? | About 52.6 minutes. |
| 6 | Name four kinds of consequence of an outage. | Any four of: lost revenue, lost productivity, SLA penalties, regulatory fines, reputation damage, data loss, safety risk. |
| 7 | Downtime costs €20,000 per hour. What does a year at 99.9% availability cost in downtime? | 8.76 h × €20,000 = €175,200. |
| 8 | What do RTO and RPO measure? | RTO: the longest acceptable time to restore service. RPO: the longest acceptable period of data loss. |
| 9 | State the risk formula. | Risk = likelihood × impact. |
| 10 | Name the four ways to treat a risk. | Avoid, reduce, transfer, accept. |
| 11 | What is a single point of failure? | A single component whose failure stops the whole system. |
| 12 | What is a common-mode failure, and why does it defeat redundancy? | One cause that takes out several redundant components at once (for example a shared bus), so the backups fail together. |
| 13 | Why does redundancy add complexity risk? | More components and switching states mean more things to maintain, more ways to fail, and more chances for human error. |
| 14 | Which cause is typically the leading cause of impactful outages? | Power problems (UPS, transfer switches, generators). |
| 15 | Name three unplanned causes of unavailability. | Any three of: power, cooling, human error, fire and water, IT failures, network failures, natural disasters, sabotage. |
| 16 | MTBF is 5,000 h and MTTR is 5 h. What is the availability? | 5,000 / 5,005 = 99.9%. |
| 17 | Give two ways to raise availability using the formula. | Raise MTBF (fail less often) or lower MTTR (repair faster). |
| 18 | What are the three phases of the failure-rate "bathtub curve"? | Early life (infant mortality), useful life, wear-out. |
| 19 | What does concurrent maintainability allow? | Planned maintenance without taking the IT load down. |
| 20 | What is the unifying design principle of a mission critical site? | Redundancy, with no single point of failure. |

---

## Module 2: Data Centre Standards

*Notes: [02_data_centre_standards.md](02_data_centre_standards.md). 20 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What is the difference between a standard and a guideline? | A standard uses "shall" (requirements, needed to claim compliance). A guideline uses "should" (recommendations). |
| 2 | Which wins if a building code conflicts with a voluntary standard? | The code. Laws and regulations take precedence. |
| 3 | What is the difference between compliance and certification? | Compliance is the owner's own claim. Certification is an independent body auditing and certifying the facility. |
| 4 | Name the international, European and national standardisation bodies. | International: ISO, IEC, ITU. European: CEN, CENELEC, ETSI. National: for example ANSI, BSI, DIN. |
| 5 | What does Tier III add compared to Tier II? | Concurrent maintainability, through multiple distribution paths (one active). |
| 6 | What does Tier IV add compared to Tier III? | Fault tolerance: any single failure, including a whole path, has no impact. |
| 7 | Match the level terms: Uptime, TIA-942, EN 50600. | Tier I to IV, Rated 1 to 4, Availability Class 1 to 4. |
| 8 | Are the Tier availability percentages a guarantee? | No. Tiers describe topology. The percentages are commonly quoted indicative figures. |
| 9 | What three things does EN 50600 classify? | Availability, physical security (protection) and energy efficiency enablement. |
| 10 | Which standard family covers the KPIs such as PUE? | ISO/IEC 30134, mirrored in Europe by EN 50600-4. |
| 11 | What does Uptime's "Operational Sustainability" add? | It assesses management and operations, building characteristics and site location, since good topology alone doesn't prevent outages. |
| 12 | What is BICSI 002, and how does it relate to TIA and EN? | A design best-practice standard that complements TIA, CENELEC and ISO/IEC documents. |
| 13 | Which standard family would you look to for fire protection, and for cabling? | Fire: NFPA 75 / 72 / 2001, EN 54, ISO 14520. Cabling: ISO/IEC 11801, ANSI/TIA-568, EN 50173 / 50174. |
| 14 | What does ISO/IEC 27001 cover, and how does it differ from ISO/IEC 22237 or EN 50600? | Information security management (organisation and process). EN 50600 / ISO/IEC 22237 cover the physical facility and its infrastructure. |
| 15 | Which body introduced PUE? | The Green Grid. |
| 16 | Name three sub-component areas and a standard for each. | For example: UPS (IEC 62040), grounding (ANSI/TIA-607 or EN 50310), fire suppression (NFPA 2001), lightning (IEC 62305). |
| 17 | If a site needs 3 UPS modules (N = 3), how many units are in N+1, 2N, 2(N+1) and 2N+1? | N+1 = 4, 2N = 6, 2(N+1) = 8, 2N+1 = 7. |
| 18 | When would you choose national over international standards? | When local law and codes require them, or when customers in that country expect them. |
| 19 | Why do real projects use several standards together? | Each covers a different job (availability class, design, cabling, protection, efficiency, security), and none covers everything. |
| 20 | Which standard types are mandatory by law? | Regulations and codes (building, electrical, fire, privacy). Voluntary standards become mandatory only through contract or specification. |

---

## Module 3: Location, Building and Construction

*Notes: [03_location_building_construction.md](03_location_building_construction.md). 25 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Is "data sovereignty law" a location or a site criterion? | Location (macro). |
| 2 | Is "distance from an airport" a location or a site criterion? | Site (micro). |
| 3 | Name three natural and three man-made hazards to check when choosing a site. | Natural: flood, earthquake, hurricane, tornado, landslide, wildfire. Man-made: airport, chemical plant, fuel depot, highway, railway, transmitter. |
| 4 | What is a knock-out criterion? | A deal-breaker (such as a flood plain) that removes a candidate regardless of its score. |
| 5 | What does a "100-year flood" mean, and what is the chance over 30 years? | A 1% chance in any year. Over 30 years: 1 − 0.99³⁰, about 26%. |
| 6 | What do SAIFI and SAIDI measure? | SAIFI: how often customers lose supply. SAIDI: how long, on average, per year. |
| 7 | Why should a DR site be far from the primary site? | So they don't share the same hazards (flood zone, power grid, seismic zone, carrier). |
| 8 | Why avoid both the basement and the top floor for the computer room? | Basement: flooding. Top floor: roof leaks, lightning, heat gain. |
| 9 | Why do walls run slab to slab? | A wall stopping at the false ceiling leaves a path for fire, smoke, dust and intruders above it. |
| 10 | Slab to slab, what is the minimum height with a 0.6 m raised floor, 2.6 m clear and 0.6 m ceiling void? | 0.6 + 2.6 + 0.6 = 3.8 m. |
| 11 | 80 racks at 1,000 kg are in a 320 m² room. What is the average floor load in kPa? | 80,000 × 9.81 / 320 = 2,452 N/m², about 2.5 kPa. |
| 12 | Why is a separate staging area needed? | To keep dust, packaging and fire load out of the white space and to test equipment before it goes live. |
| 13 | Why is the media storage area separate from the computer room? | So a fire in the computer room doesn't destroy the backups, and so media gets its own controlled environment. |
| 14 | A UPS supplies 400 kW at 95% efficiency. How much heat does it release? | 400 / 0.95 = 421.1 kW input, so about 21.1 kW of heat. |
| 15 | Why must lead-acid battery rooms be ventilated, and to what hydrogen level? | Charging releases hydrogen, which is explosive from 4% by volume. The design keeps it below 1% (25% of the lower flammable limit). |
| 16 | Which standard governs lithium-ion battery rooms, and what is the main hazard? | NFPA 855. The main hazard is thermal runaway with flammable and toxic off-gas. |
| 17 | What is the purpose of the service corridor? | To move equipment, supplies and people between the dock, technical rooms and computer room without crossing critical rooms. |
| 18 | Why must generator exhaust and air intakes be kept apart? | Exhaust fumes drawn into intakes can harm the cooling plant, generators and building air quality. |
| 19 | A 1,500 kW generator burns 0.26 L/kWh at full load. How much fuel for 24 hours? | 1,500 × 0.26 = 390 L/h, × 24 = 9,360 litres. |
| 20 | What is the difference between the entrance room and the meet-me room? | The entrance room is where carrier cables enter and terminate. The meet-me room is where carriers and customers interconnect. |
| 21 | Why have two entrance rooms or meet-me rooms? | So a single incident or cable cut can't isolate the site (network equivalent of A/B power). |
| 22 | What goes in the security room? | Access control, CCTV monitoring, alarm panels, visitor logs, usually near the entrance. |
| 23 | Why keep the NOC outside the computer room? | People, noise, food and movement don't belong in the white space, and it needs its own secure, staffed environment. |
| 24 | Name three classic site and building mistakes. | Any three of: flood plain, basement or top floor, single utility feed, low ceiling, pipes overhead, doors too small, no staging area, poor battery room, no expansion room. |
| 25 | A data centre has Tier III power but Tier II cooling. What Tier is it overall? | Tier II. The weakest subsystem sets the level. |

---

## Module 4: Raised Access Flooring and Suspended Ceiling

*Notes: [04_raised_floor_suspended_ceiling.md](04_raised_floor_suspended_ceiling.md). 26 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Name three standards used for raised floors. | EN 12825, CISCA, PSA MOB PF2 PS (and the data centre standards such as TIA-942 and EN 50600-2-1). |
| 2 | In EN 12825, what is the main classification criterion? | The ultimate (failure) load. |
| 3 | An EN 12825 floor has an ultimate load of 10 kN and a safety factor of 2. What is its working load? | 10 ÷ 2 = 5 kN. |
| 4 | The same floor has a safety factor of 3. What is the working load? | 10 ÷ 3 = 3.33 kN. |
| 5 | What do deflection classes A, B and C allow? | Maximum deflection of 2.5 mm, 3.0 mm and 4.0 mm. |
| 6 | What must EN 12825 pedestals withstand? | Four times the working load without distortion or damage. |
| 7 | What is the difference between CISCA and EN 12825 ratings? | CISCA states the working (design) load. EN 12825 states the ultimate load, then applies a safety factor. |
| 8 | Name three panel types. | Any three of: all-steel, steel with concrete fill, wood core, calcium sulphate, aluminium. |
| 9 | Name two differences between a stringered and a stringerless floor. | Stringered: bars link the pedestal heads, so it is more rigid and suits heavy loads, tall floors and seismic zones, but costs more. Stringerless: panels sit on heads only, so it is cheaper with easier access but less stable laterally. |
| 10 | Why is concentrated load more important than average load for racks? | A rack's weight sits on a few small feet or casters, so local panel stress is far higher than the average load suggests. |
| 11 | A rack weighs 900 kg and stands on four feet. What is the load per foot? | 900 × 9.81 / 4 = 2,207 N, about 2.2 kN. |
| 12 | Convert 6 kN into kilograms. | About 612 kg (1 kN is about 102 kg). |
| 13 | A panel weighs 20 kg. What is the weight of panels per m² (600 × 600 mm panels)? | 2.78 panels per m² × 20 kg = about 56 kg/m². |
| 14 | What is the purpose of sealing the slab under a raised floor? | To stop dust from the concrete entering the air stream. |
| 15 | Why use grommets or brush seals at cable cut-outs? | To stop conditioned air escaping through the opening. |
| 16 | What are the three resistance classes for flooring and their boundaries? | Conductive below 10⁶ Ω, static dissipative 10⁶ to below 10⁹ Ω, insulative above 10⁹ Ω. |
| 17 | Why do data centres prefer dissipative over conductive floors? | Very low resistance raises the shock hazard near live equipment, and dissipative still drains charge safely. |
| 18 | Why can an ordinary vinyl coating on a floor be a problem? | It acts as an insulator and breaks the electrical path that drains static. |
| 19 | Does bonding the raised floor bond the racks? | No. Each rack needs its own bonding conductor to the grid or rack busbar. |
| 20 | Give three rules for cutting a raised floor tile. | Plan first, keep the cut away from edges (about 75 mm) and pedestals, never cut a corner, trim the edge and seal it. |
| 21 | Why does cutting weaken a tile, and what can be done? | The panel is designed as a whole, so a hole reduces its load rating. Use manufacturer limits, extra pedestal support, or keep cut panels out of heavy areas. |
| 22 | What ramp slope is commonly used, and how long is the ramp for a 0.6 m floor? | 1:12, so 0.6 × 12 = 7.2 m long. |
| 23 | Why is a landing platform needed? | A flat space to stop, position and turn equipment safely before entering the raised floor. |
| 24 | Give three reasons to use a suspended ceiling. | Any three of: hide services, return air plenum, dust control, mounting for detectors and nozzles, smaller gas volume, acoustics, access. |
| 25 | Why must detection be in both the floor void and the ceiling void? | Fire and smoke can start in either void, and both contain cabling and equipment. |
| 26 | Why do ceiling tiles need restraint when gas suppression is used? | A gas release briefly raises room pressure, which can lift or dislodge tiles. |

---

## Module 5: Light

*Notes: [05_light.md](05_light.md). 28 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What's the difference between lumen and lux? | Lumen measures light emitted by a source. Lux measures light arriving on a surface (lumens per m²). |
| 2 | What does candela measure? | Luminous intensity: light emitted in one particular direction. |
| 3 | What does luminance describe, and why does it matter? | The brightness of a surface as seen by the eye (cd/m²). It determines glare. |
| 4 | Convert 500 lux to foot-candles. | 500 / 10.76, about 46.5 fc. |
| 5 | A luminaire gives 1,000 cd directly at a surface 2 m away. What is the illuminance, and at 4 m? | 1,000 / 4 = 250 lux at 2 m. 1,000 / 16 = 62.5 lux at 4 m. |
| 6 | An aisle area of 40 m² needs 500 lux, UF = 0.5, MF = 0.8. What total lumens are needed? | 500 × 40 / (0.5 × 0.8) = 20,000 / 0.4 = 50,000 lm. |
| 7 | How many 5,000 lm luminaires does that need? | 50,000 / 5,000 = 10 luminaires. |
| 8 | Why is vertical illuminance important in a data centre? | Technicians read labels, ports and LEDs on the vertical faces of racks, which can stay dark even if the floor is bright. |
| 9 | What two lux levels does TIA-942 set for computer room aisles, and where measured? | 500 lux horizontal and 200 lux vertical, at 1 m above the finished floor in the middle of the aisle. |
| 10 | Name three lighting standards. | Any three of: EN 12464-1, EN 1838, EN 50172, EN 60598-2-22, TIA-942, NFPA 101. |
| 11 | Why position fixtures above the aisles rather than the racks? | Light reaches the rack faces from the side, and nothing is wasted on rack tops. |
| 12 | Why use LED over fluorescent in a data centre? | Higher efficacy, less heat and cooling load, long life, instant on, dimmable, and no magnetic-ballast interference. |
| 13 | A 62,500 lm installation uses LED at 130 lm/W. What power does it draw? | 62,500 / 130, about 481 W. |
| 14 | What problem affects LED drivers in hot aisles? | Heat shortens driver life (especially electrolytic capacitors), so use high-temperature drivers or remote mounting. |
| 15 | Why keep lighting circuits separate from IT power? | A lighting fault or maintenance can't then affect the servers, and the UPS capacity stays reserved for critical IT load. |
| 16 | Why alternate fixtures across two circuits? | One circuit failure then leaves the room only partly dark. |
| 17 | What is the three-level lighting idea? | A very low level when unoccupied (enough for CCTV), a walking level when motion is detected, and full task lighting when people work. |
| 18 | What are the three categories of emergency escape lighting? | Escape route lighting, open area (anti-panic) lighting, high-risk task area lighting. |
| 19 | What is the minimum illuminance on an escape route centre line, and in an open area? | 1 lux on the route centre line, 0.5 lux in the open area core. |
| 20 | What is the requirement for high-risk task areas? | 10% of the normal task illuminance, with a minimum of 15 lux, reached within 0.5 s. |
| 21 | What is the response-time requirement for escape lighting? | 50% of the required level within 5 s and 100% within 60 s. |
| 22 | A route has 24 lux under each luminaire and 0.5 lux between. Does it meet 40 : 1 uniformity? | 24 / 0.5 = 48 : 1, so it fails. |
| 23 | Why can't a generator alone provide emergency lighting? | It takes about 10 to 15 s to start, longer than the 5 s needed, so luminaires need their own batteries. |
| 24 | Name six places that need an emergency luminaire. | Any six of: exit doors, outside final exits, stairs, direction changes, junctions, level changes, exit signs, call points, fire equipment, first aid points. |
| 25 | How many luminaires should each escape route compartment have at minimum, and why? | At least two, so one failure doesn't leave it dark. |
| 26 | What's the difference between maintained and non-maintained emergency luminaires? | Maintained: lit all the time. Non-maintained: off until the mains fails. |
| 27 | What testing is normally required for emergency lighting? | Monthly function tests, an annual full-duration test, and a log book of results. |
| 28 | 50 luminaires at 5 W emergency load must run 3 hours. What energy is needed before the design margin? | 50 × 5 × 3 = 750 Wh. |

---

## Module 6: Power Infrastructure

### Part A: lessons 6.1 to 6.14

*Notes: [06-1_incoming_power_to_transfer_switches.md](06-1_incoming_power_to_transfer_switches.md). 57 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Why do large data centres connect at MV or HV? | Current falls as voltage rises, so cables, switchgear and losses stay manageable. At LV the current would be impractically large. |
| 2 | What is the difference between a dual feed from one substation and from two substations? | One substation protects against a cable fault only. Two independent substations also protect against a substation or upstream failure. |
| 3 | What is the point of common coupling? | The boundary between the utility network and the customer's installation, where metering and the connection agreement apply. |
| 4 | An 8 MVA load connects at 20 kV. What is the line current? | 8,000,000 / (1.732 × 20,000) = about 231 A. |
| 5 | What does capacity factor mean, and what energy does a 10 MW solar plant at 20% give in a year? | Actual energy ÷ (rated power × hours). 10 × 0.2 × 8,760 = 17,520 MWh. |
| 6 | What is the difference between annual and hourly (24/7) matching? | Annual matching buys as much renewable energy over a year as consumed. Hourly matching requires clean generation in the same hours as the consumption. |
| 7 | Why don't renewables replace the UPS and generator? | They are intermittent, not firm, and don't protect against faults or short interruptions. |
| 8 | A site uses 90 GWh a year, 45 GWh renewable. What is the REF? | 45 / 90 = 50%. |
| 9 | Define a microgrid and its two operating modes. | A local system of generation, storage and loads with a controller. It operates grid-connected or islanded. |
| 10 | What do the PCC and the controller do in a microgrid? | The PCC connects or disconnects the microgrid from the grid. The controller balances supply and demand and manages islanding. |
| 11 | A 6 MWh battery supplies a 3 MW load. How long does it last? | 6 / 3 = 2 hours. |
| 12 | Is any SMR commercially supplying a data centre today? | No. The first western SMR power is targeted for around 2030. Deals so far mainly use existing reactors. |
| 13 | Name two challenges for nuclear in data centres. | Any two of: licensing, cost, timeline, HALEU fuel supply, public acceptance, regulation of co-located loads. |
| 14 | 90 MW of IT at PUE 1.4, using 50 MWe modules. What is N and N+1? | Total 126 MW. N = 126 / 50 = 2.52, so 3 modules. N+1 = 4. |
| 15 | What voltage band does EN 50160 allow, and for how long? | ±10% of nominal for 95% of the week (10-minute averages). |
| 16 | What is the allowed voltage range for a 120 V nominal supply at ±10%? | 108 V to 132 V. |
| 17 | Fifth harmonic 3% and seventh harmonic 4%. What is the THD? | √(3² + 4²) = √25 = 5%. |
| 18 | Why is EN 50160 called a minimum? | It is a compromise that suppliers must meet, not a promise of high quality, and it allows many dips and interruptions. A data centre must mitigate itself. |
| 19 | Name four power quality disturbances and a mitigation for each. | For example: dip (UPS), interruption (UPS and generator), transient (surge protection), harmonics (filters or low-harmonic UPS), unbalance (phase balancing). |
| 20 | An IT load of 800 kW at PUE 1.5. What is the total facility power? | 800 × 1.5 = 1,200 kW. |
| 21 | What apparent power is that at PF 0.9? | 1,200 / 0.9 = 1,333 kVA. |
| 22 | A load of 1.2 MVA uses 2N. How much capacity is installed? | 2.4 MVA (two full systems). |
| 23 | What is stranded capacity? | Installed capacity that cannot be used, for example because cooling or distribution is the limit. |
| 24 | Why transmit at hundreds of kV instead of 415 V? | Higher voltage means lower current for the same power, so far lower I²R heat losses over long distances. |
| 25 | Power passes through stages with efficiencies of 99%, 95%, 98% and 99%. What is the overall efficiency? | 0.99 × 0.95 × 0.98 × 0.99 = about 91.2%. |
| 26 | What is the current of 2 MVA at 400 V (three-phase)? | 2,000,000 / (1.732 × 400) = about 2,887 A. |
| 27 | Name two transformer types and where each is typically used. | Cast resin: indoors close to the load. Oil-immersed: outdoors or in fire-rated, bunded rooms. |
| 28 | A 2,000 kVA, 400 V transformer has uk = 6%. What is the fault current? | In = 2,887 A. Isc = 2,887 / 0.06 = about 48.1 kA. |
| 29 | A transformer has no-load loss 2 kW and full-load loss 12 kW. What are its losses at 50% load? | 2 + 12 × 0.5² = 5 kW. |
| 30 | What does Dyn11 mean? | Delta primary, star secondary with the neutral brought out, 30° phase shift. |
| 31 | How many generators for a 2,400 kW load with 800 kW sets, N and N+1? | N = 3, N+1 = 4. |
| 32 | What is a main-tie-main arrangement? | Two incomers feeding two buses, with a normally open tie that closes if one feed fails. |
| 33 | What common-mode failure can defeat N+1 generators? | A shared paralleling bus, control system, fuel supply or room. |
| 34 | State the five ISO 8528-1 ratings and their hours. | ESP about 200 h/yr, LTP about 500 h/yr, PRP unlimited at about 70% average, COP unlimited at constant load, DCP unlimited at variable load with no average-load cap. |
| 35 | What does NFPA 110 Level 1 Type 10 require? | Acceptable power to the loads within 10 seconds of a utility failure. |
| 36 | Per your slide, size a generator for a 600 kW UPS (high harmonics) and 400 kW cooling and lighting. | 600 × 1.2 + 400 × 1.0 = 720 + 400 = 1,120 kW. |
| 37 | Add a 25% margin to that. | 1,120 × 1.25 = 1,400 kW. |
| 38 | Fuel for 12 hours at 1,120 kW and 0.26 L/kWh? | 1,120 × 0.26 = 291 L/h, × 12 = about 3,490 litres. |
| 39 | What is wet stacking, and how is it avoided? | Unburned fuel and soot in the exhaust from light-load running. Avoid by running and testing at 30% load or more. |
| 40 | Why do UPS batteries only need a few minutes of runtime? | They only cover the gap of 10 to 15 seconds (plus margin) until the generator takes over. |
| 41 | Describe the ATS sequence of operation. | Detect source failure, send engine start, generator stabilises, transfer, wait for stable utility, retransfer, generator cooldown. |
| 42 | Compare open, delayed and closed transition. | Open: brief break. Delayed: neutral pause so motors de-energise. Closed: sources briefly paralleled, no interruption. |
| 43 | When is a 4-pole ATS needed? | When the generator is a separately derived source with its own neutral-earth bond, so only one bond is in the active path. |
| 44 | The continuous load is 320 A. Which ATS rating, applying 125%? | 320 × 1.25 = 400 A. |
| 45 | What does a bypass-isolation ATS allow? | Servicing the ATS while the load stays powered, supporting concurrent maintainability. |
| 46 | How fast is an STS compared with an ATS? | An STS takes a few ms (under about 8 ms). An ATS takes tens to hundreds of ms. |
| 47 | Why might dual-corded servers not need an STS? | Each power supply is fed from a different path, so they already have two sources. |
| 48 | How does an STS differ from a UPS static bypass? | An STS switches between two separate UPS-fed sources. A static bypass switches one UPS to raw utility and gives no second conditioned source. |
| 49 | Why is a primary-side STS between unsynchronised sources risky? | It can trigger large transformer inrush that trips upstream breakers. |
| 50 | A load needs 4 UPS modules (N = 4), so an N+1 design has 5 modules. What is the normal load per module? | 4 / 5 = 80%. |
| 51 | A 2(N+1) UPS design with N = 3. What is the normal load per module? | 3 / (2 × 4) = 37.5%. |
| 52 | What is the weakness of parallel redundant UPS systems? | The common output bus and switchgear are a single point of failure. |
| 53 | What does a catcher UPS do in normal operation? | Nothing or very little. It is an idle reserve that takes over a failed main system. |
| 54 | Count the components of the dual-path design on your slide. | 2 transformers, 2 generators, 2 ATS, 4 UPS and 2 STS: 12 main components. |
| 55 | Five series components of 99.9% each. What is the chain availability, and with two chains in parallel? | 0.999⁵ = 99.50%. Two in parallel: 1 − 0.00499² = 99.9975%. |
| 56 | Why does an STS in series reduce the benefit of 2N? | It becomes a single point of failure. 99.9975% × 99.9% is about 99.90%. |
| 57 | Why does your slide say the design is not preferred? | The higher component count increases maintenance, cost and failure rate. |

### Part B: lessons 6.15 to 6.26

*Notes: [06-2_phases_distribution_grounding.md](06-2_phases_distribution_grounding.md). 60 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Which conductors make up a full three-phase supply? | L1, L2, L3, neutral and protective earth (3P+N+PE). |
| 2 | What are the IEC colours for L1, L2, L3, neutral and PE? | Brown, black, grey, blue, green/yellow. |
| 3 | What colours are commonly used for US 277/480 V phases and neutral? | Brown, orange, yellow, with a grey neutral. |
| 4 | What power can a 32 A, 400 V three-phase circuit supply (PF 1)? | 1.732 × 400 × 32 = about 22.2 kW. |
| 5 | What current does a 20 kW three-phase load draw at 208 V? | 20,000 / (1.732 × 208) = about 55.5 A. |
| 6 | Why are LSZH cables used in data centres? | They give off little smoke and no corrosive halogen gases in a fire. |
| 7 | Why must phase rotation be checked? | Wrong rotation runs three-phase motors backwards and can stop UPS, STS or generator paralleling from working. |
| 8 | A feeder carries 80 A over 40 m with R = 0.6 Ω/km. What is the voltage drop? | 1.732 × 80 × 0.6 × 0.04 = about 3.3 V (0.8% of 400 V). |
| 9 | What power does a 230 V, 32 A single-phase circuit supply? | 230 × 32 = 7.36 kW. |
| 10 | What continuous power can a 208 V, 30 A circuit supply at an 80% limit? | 208 × 24 A = about 5.0 kW. |
| 11 | What current does a 1 kW server draw at 230 V? | 1,000 / 230 = about 4.3 A. |
| 12 | Why can many servers on one RCD cause nuisance trips? | Each server power supply leaks a small current to earth, and the leakage adds up. |
| 13 | What is the imbalance for phase currents 45 A, 50 A and 55 A? | Average 50 A, largest deviation 5 A, so 10%. |
| 14 | What is the neutral current for phases 60 A, 30 A and 30 A? | √(3,600 + 900 + 900 − 1,800 − 900 − 1,800) = √900 = 30 A. |
| 15 | Why can neutral current exceed phase current with computer loads? | Third-harmonic currents are in phase on all three phases and add up arithmetically in the neutral. |
| 16 | Give three effects of phase imbalance. | Any three of: neutral current, voltage imbalance, motor heating, transformer or UPS heating, stranded capacity, nuisance trips. |
| 17 | Six racks of 4 kW are spread over L1, L2 and L3. What is the balanced allocation? | Two racks per phase, so 8 kW on each phase. |
| 18 | Do power-factor correction capacitors fix current imbalance? | No. They correct reactive power, not unequal load distribution. |
| 19 | How does EN 50174-2:2018 calculate the minimum separation between power and data cables? | A = S × P: S comes from the data cable's segregation class and the containment, and P (the power cabling factor) from the number and current of the power circuits. |
| 20 | Why cross power and data cables at 90°? | It minimises coupling of interference between them. |
| 21 | With S = 50 mm and P = 0.6, what is the minimum separation? | S × P = 30 mm. |
| 22 | 30 cables of 20 mm diameter go in a 300 × 50 mm tray. What is the fill, and is it acceptable at a 50% limit? | 30 × 314 = 9,425 mm² of 15,000, so 62.8%. It exceeds 50%, so use a larger tray. |
| 23 | Why keep A and B cable routes physically separate? | So one cable fault, fire or maintenance event can't affect both paths. |
| 24 | A dual-corded 4 kW server runs on 230 V. What current does one path carry if the other fails? | 4,000 / 230 = about 17.4 A. |
| 25 | What size must each path of a dual-corded design have? | The full load, because one path must carry everything if the other fails. |
| 26 | How can a single-corded device get A/B resilience? | Through a rack-mounted ATS or STS fed from both paths. |
| 27 | At what load are power supplies most efficient, and why is this relevant to dual PSUs? | Around 50% load. Two PSUs sharing a load each run near 50%. |
| 28 | In a 3N/2 design, what is each system's normal load and its load after one failure? | 66.7% normally, 100% after one failure. |
| 29 | A load of 900 kVA. What is the installed capacity for 2N and for 3N/2? | 2N: 1,800 kVA. 3N/2: 3 × 450 = 1,350 kVA. |
| 30 | What is the main drawback of 3N/2 compared with 2(N+1)? | After one failure or during maintenance, the remaining systems are at 100% with no redundancy left. |
| 31 | What is the availability of a 2-out-of-3 arrangement with units of 99%? | 3 × 0.9801 − 2 × 0.970299 = 0.9997, so 99.97%. |
| 32 | Three stages in series, each 99.9%. What are the availability and yearly downtime? | 0.999³ = 99.70%, about 26.3 hours. |
| 33 | Two 99.9% units in parallel. What is the availability? | 1 − 0.001² = 99.9999%. |
| 34 | Why does making only one stage redundant give a limited gain? | The remaining single stages still limit the result (weakest link). |
| 35 | MTBF is 20,000 h. What is the availability with MTTR of 8 h and 2 h? | 99.960% and 99.990%. |
| 36 | Give five techniques that improve power availability. | For example: redundancy, removing SPOFs, independent A/B paths, concurrent maintainability, maintenance and testing, monitoring, spares, procedures and training. |
| 37 | Which techniques mainly reduce MTTR? | Spares, modular and hot-swap equipment, trained staff and clear procedures, monitoring. |
| 38 | Why must EPO buttons be protected? | An accidental press cuts all power and has caused real outages. |
| 39 | Compare radial, primary selective and secondary selective distribution. | Radial: one path, lowest resilience. Primary selective: two primary feeders with switching, transformer is a single point. Secondary selective: two transformers and buses with a tie, survives a transformer failure. |
| 40 | What is discrimination (selectivity)? | A fault trips only the breaker nearest to it, so upstream breakers stay on. |
| 41 | A 60 kW row at 400 V (PF 1). What current, and what breaker for a continuous load at 125%? | 86.6 A, × 1.25 = 108 A, so a 125 A breaker. |
| 42 | At what current does busway generally become preferable to cable? | Roughly above 630 to 800 A, especially on long runs with changing loads. |
| 43 | Which standards govern busbar trunking? | IEC 61439-6 (international) and UL 857 with NEC Article 368 (US). |
| 44 | Size the busway for 80 kW at 400 V, PF 0.95. | 80,000 / (1.732 × 400 × 0.95) = 121.5 A, so a 160 A busway. |
| 45 | What tap-off for a 40 kW rack at 400 V, PF 0.95, kept within 80%? | 60.8 A / 0.8 = 76 A, so a 100 A tap-off. |
| 46 | How does aluminium compare with copper in busbars? | About 1.6 times the cross-section for the same resistance, but about half the weight and lower cost. |
| 47 | What is a typical hybrid distribution arrangement? | Overhead busway for the trunk run, with cables for the short drops from tap-offs to racks. |
| 48 | A circuit needs 100 A and the grouping factor is 0.57. What tabulated rating is needed? | 100 / 0.57 = about 175 A. |
| 49 | What is the difference between grounding and bonding? | Grounding connects the system to earth. Bonding connects metal parts to each other so they stay at the same voltage. |
| 50 | What does the PE wire do in normal operation and in a fault? | Nothing in normal operation. In a fault it carries the fault current so the breaker trips. |
| 51 | Which earthing system is preferred in a data centre, and which should be avoided? | TN-S preferred. TN-C avoided. |
| 52 | Why does a TT system need an RCD? | The fault current through soil may be too small to trip an ordinary breaker. |
| 53 | Why is the neutral-ground bond made at only one point? | A second bond gives neutral current another path through ground wires and metalwork, causing noise. |
| 54 | Why must the bond be close to the ICT equipment, but not too close? | Close, so a long neutral doesn't build up voltage at the racks. Not too close, to avoid EMF from the transformer. |
| 55 | Why is the isolation transformer delta-wye? | Delta input traps third harmonics and isolates upstream. Wye output gives a neutral to bond to ground. |
| 56 | What are the PBB and SBB, and what were they formerly called in US practice? | The primary and secondary bonding busbars (formerly the TMGB and TGB). |
| 57 | What is a ground loop and how is it avoided? | Circulating current from more than one earth path. Avoid with a single neutral bond, a common bonded network and short bonds. |
| 58 | Name the three SPD types and where each is fitted. | Type 1 at the main board, Type 2 at distribution boards, Type 3 near the equipment. |
| 59 | Why must all services enter at one location and be bonded there? | So lightning or surge current can't find a path through the equipment to another entry. |
| 60 | Which standards cover ICT bonding networks and electrical safety grounding? | Bonding networks: EN 50310 and ANSI/TIA-607 (ISO/IEC 30129). Electrical safety: IEC 60364, BS 7671, NEC Article 250. |

### Part C: lessons 6.27 to 6.35

*Notes: [06-3_power_quality_and_sizing.md](06-3_power_quality_and_sizing.md). 60 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What is the difference between common-mode and differential-mode signals? | Differential: equal and opposite currents on two conductors (the wanted signal). Common mode: noise in phase on both conductors, relative to ground. |
| 2 | Give three sources of common-mode noise. | Any three of: ground loops or ground potential differences, switch-mode supplies and drives, radiated EMI, wrong neutral-ground bonds, transients. |
| 3 | Name four ways to reduce common-mode noise. | Any four of: single neutral-ground bond, bonded network, isolation transformer, common-mode choke, twisted or shielded cables, fibre, Y-capacitors. |
| 4 | A receiver has a CMRR of 60 dB and sees 2 V of common-mode noise. What is the error? | 2 V / 1,000 = 2 mV. |
| 5 | Why is fibre optic cable immune to ground potential differences? | It has no conductive path between the two ends. |
| 6 | What is the order of boards from supply to final circuits? | Main distribution board, sub-distribution board, final distribution board (RPP/panelboard). |
| 7 | Which standard covers low-voltage switchgear and controlgear assemblies? | IEC 61439 (Part 2 for power switchgear). |
| 8 | What is the difference between Form 1 and Form 4? | Form 1 has no separation. Form 4 separates busbars, units from each other, and the terminals of each unit. |
| 9 | A board has 12 outgoing 32 A circuits. What is the incomer at an RDF of 0.6? | 384 A × 0.6 = 230 A, so 250 A. |
| 10 | Why specify an RDF of 1.0 for a data centre board? | Rack circuits are loaded continuously and at the same time, so the default factors under-size the board. |
| 11 | What does IP54 mean? | Dust-protected and protected against splashing water. |
| 12 | What does IP2X mean? | Protection against fingers (objects over 12.5 mm): touch protection for live parts. |
| 13 | What do the two digits of the IP code represent? | First: protection against solids and dust (0 to 6). Second: protection against water (0 to 9). |
| 14 | Does IP66 imply IP67? | No. Jet protection does not guarantee immersion protection. |
| 15 | Which IP ratings are typical for outdoor chillers or generator enclosures? | About IP54 to IP55 (outdoor cabinets often IP55 to IP65). |
| 16 | What is the IEEE 519-2022 voltage THD limit below 1 kV? | 8% total, with 5% for an individual harmonic. |
| 17 | What TDD limit applies if ISC / IL = 30? | 8% (the 20 to 50 row). |
| 18 | ISC = 20 kA, IL = 800 A, harmonic current 55 A. Is the site compliant? | ISC/IL = 25, limit 8%. TDD = 55/800 = 6.9%, so yes. |
| 19 | What is the difference between THD and TDD? | THD divides by the present fundamental current. TDD divides by the maximum demand current, so it doesn't exaggerate at light load. |
| 20 | Which standard describes how to measure power quality? | IEC 61000-4-30 (Class A for compliance). |
| 21 | Name five power quality guidelines for a data centre. | For example: measure the supply, use a double-conversion UPS, control harmonics, check generator compatibility, ground and bond properly, protect against surges, balance phases, monitor. |
| 22 | What are the frequencies of the 3rd, 5th and 7th harmonics at 50 Hz? | 150, 250 and 350 Hz. |
| 23 | Which harmonics does a 6-pulse rectifier produce? | 5th, 7th, 11th, 13th, 17th, 19th (6k ± 1). |
| 24 | What is the THD for a 100 A fundamental with 20 A of 5th and 10 A of 7th harmonic? | √(20² + 10²) = 22.4 A, so 22.4%. |
| 25 | Harmonic current is 40 A and the maximum demand current is 200 A. What is the TDD? | 40 / 200 = 20%. |
| 26 | Each phase carries 20 A of third harmonic. What is the neutral current from it? | 60 A (the three add arithmetically). |
| 27 | Which harmonics does a 12-pulse rectifier cancel? | The 5th and 7th (leaving the 11th and 13th). |
| 28 | What THDi is typical for an active front end UPS? | Below about 3 to 5%. |
| 29 | S_sc = 50 MVA and the capacitor bank is 2 MVAr. At which harmonic does it resonate? | √(50 / 2) = 5, the 5th harmonic, which is dangerous. |
| 30 | Why do harmonics affect generators more than the utility? | A generator has a much higher internal impedance, so the same current distorts the voltage more and overheats the alternator. Hence the × 1.2 UPS factor. |
| 31 | What does the ITIC (CBEMA) curve show, and what is it not? | The voltage tolerance envelope of IT equipment (magnitude vs. duration). It is not a utility performance curve or a design specification. |
| 32 | State the main points of the lower and upper boundaries. | Steady state ±10%. 120% up to 0.5 s. 80% up to 10 s. 70% up to 0.5 s. 0 V up to 20 ms. |
| 33 | What are 70%, 80% and 120% on a 230 V supply? | 161 V, 184 V and 276 V. |
| 34 | Where does a 60% sag lasting 100 ms fall? | Below the lower boundary (70% for up to 0.5 s): outside, so malfunction is possible. |
| 35 | Where does an 85% sag lasting 2 s fall? | Inside (above the 80% limit for 0.5 to 10 s). |
| 36 | Where does a 125% swell lasting 0.1 s fall? | In the prohibited region (above 120%): damage is possible. |
| 37 | Why is an STS inside the curve but an ATS outside it? | An STS transfers in a few ms (within the 20 ms dropout limit). An ATS takes tens to hundreds of ms. |
| 38 | Why is SEMI F47 more demanding? | It requires ride-through of deeper sags (down to 50% for 200 ms) for semiconductor equipment. |
| 39 | Define power factor. | PF = P / S = cos φ, the ratio of real power to apparent power. |
| 40 | What is the apparent power of an 800 kW load at PF 0.8? At 0.95? | 1,000 kVA and 842 kVA. |
| 41 | What capacitor size raises 800 kW from PF 0.8 to 0.95? | 800 × (0.750 − 0.329) = about 337 kVAR. |
| 42 | What is the current for 500 kW at 400 V at PF 0.8, and at 0.95? | 902 A and 760 A (15.8% less). |
| 43 | By how much do I²R losses fall when PF improves from 0.8 to 0.95? | (0.8/0.95)² = 0.71, so about 29% lower. |
| 44 | DPF is 0.95 and THD is 34.8%. What is the true PF? | 0.95 / √(1 + 0.348²) = 0.90. |
| 45 | What real power does a 400 kVA UPS with an output PF of 0.9 supply? | 360 kW. |
| 46 | Why can capacitors and harmonics be a problem together? | The capacitors can resonate with a harmonic and fail, or amplify it. Use detuned banks. |
| 47 | Why is label power conservative? | It is the sum of worst-case component draws divided by PSU efficiency, a number the equipment is guaranteed not to exceed. |
| 48 | A server's label is 251 W and the heaviest test measures 145 W. What fraction is that? | 145 / 251 = 58%. |
| 49 | 25 servers have 800 W labels and a measured peak of 350 W each. Compare the totals. | Label 20 kW, measured peak 8.75 kW (43.75%), so 11.25 kW would be stranded. |
| 50 | What is stranded power? | Capacity that is allocated but never used and can't be given to other equipment. |
| 51 | How do you find real power use? | Metered or intelligent PDUs with outlet-level measurement, over time, plus manufacturer power calculators. |
| 52 | What is the risk of sizing too far below the label? | Peaks can trip breakers or overload circuits and cause shutdowns, especially for AI and HPC racks that run near full power. |
| 53 | An IT load of 1,600 kW at PUE 1.4. What is the total facility power? | 2,240 kW. |
| 54 | Modules of 500 kW (unity PF) for 1,600 kW with N+1. How many, and what normal load per module? | 5 modules, each 320 kW (64%). |
| 55 | Battery energy for 1,000 kW for 5 minutes (before losses and margin)? | 1,000 × 5/60 = 83.3 kWh. |
| 56 | A load of 1,800 kVA, transformer at most 80% loaded. What minimum rating? | 1,800 / 0.8 = 2,250 kVA, so the next standard size (2,500 kVA). |
| 57 | Size a generator per your slide: UPS input 1,667 kW (high harmonics) and 573 kW cooling, lighting and other. | 1,667 × 1.2 + 573 = 2,573 kW, and about 3,090 kW with 20% margin. |
| 58 | How many refrigeration tons for 700 kW of heat? | 700 / 3.517 = about 199 tons. |
| 59 | Put the sizing steps in order. | IT load, × PUE, ÷ PF, growth, redundancy, equipment sizes, check the weakest link. |
| 60 | Why are labels used for breaker sizing but measured data for capacity planning? | Protection must cover the worst case the equipment could draw. Capacity planning should reflect real use to avoid oversizing and stranded capacity. |

### Part D: lessons 6.36 to 6.47

*Notes: [06-4_ups_and_batteries.md](06-4_ups_and_batteries.md). 62 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Why does a UPS need both a rectifier and an inverter? | Batteries store only DC. The rectifier charges them and feeds the DC link, and the inverter turns DC back into AC for the load. |
| 2 | What do VFI, VI and VFD stand for? | Voltage and frequency independent, voltage independent, voltage and frequency dependent. |
| 3 | Decode VFI-SS-11. | Voltage and frequency independent output, sinusoidal waveform in both normal and battery mode, and the best dynamic performance class. |
| 4 | Why does a UPS have a classification for each mode? | Its output performance changes: for example VFI in on-line mode but VFD in high-efficiency (eco) mode. |
| 5 | What are the two UPS families? | Static (electronic converters, batteries) and rotary or dynamic (motor-generator, flywheel). |
| 6 | Which rectifier type gives the lowest input THDi? | The IGBT active front end (typically under 3 to 5%). |
| 7 | What is the difference between transformer-based and transformerless UPS? | Transformer-based has galvanic isolation but is bulkier and less efficient (about 88 to 92%). Transformerless is smaller and more efficient (about 96 to 99%). |
| 8 | In a VFI UPS, which path does the load take in normal mode? | Mains, rectifier, DC bus, inverter, load. |
| 9 | What happens in battery mode, and why is there no interruption? | The battery takes over the DC bus, and the inverter never stops. |
| 10 | When does a UPS transfer to static bypass? | On overload, a short circuit on the output, inverter failure or over-temperature. |
| 11 | What is the risk while a UPS is on static bypass or maintenance bypass? | The load is on raw mains with no conditioning, and on maintenance bypass there is no UPS protection at all. |
| 12 | Why do UPS rectifiers walk in gradually on a generator? | To avoid a sudden load step that would disturb the generator's voltage and frequency. |
| 13 | What is eco mode, and what is its main risk? | The static bypass carries the load with the inverter on standby (up to about 99% efficiency). The risk is a transfer gap and less protection. |
| 14 | Which UPS type is typical for data centres, and why? | VFI (online double conversion): zero transfer time and full conditioning. |
| 15 | Compare VFD, VI and VFI on transfer time. | VFD and VI: a few ms. VFI: zero. |
| 16 | A UPS supplies 800 kW at 96% efficiency. What are its losses? | 800 / 0.96 − 800 = 33.3 kW. |
| 17 | The same load at 99% efficiency (eco mode)? | 800 / 0.99 − 800 = 8.1 kW. |
| 18 | At what load range is a UPS typically most efficient? | About 30 to 80% of its rating. |
| 19 | Why do redundant designs lower UPS efficiency? | Each UPS runs at a lower share of its rating (for example 40 to 50% in 2N). |
| 20 | What is a modular UPS? | A UPS built from hot-swappable power modules in a frame with shared busbar, bypass and controls. |
| 21 | A load is 160 kW and the modules are 20 kW. How many for N+1, and what load does each carry? | N = 8, N+1 = 9 modules, each 160 / 9 = 17.8 kW (89%). |
| 22 | The load falls to 80 kW. Compare all 9 modules active with intelligent management. | All 9: 8.9 kW each (44%). Managed: 5 active modules at 16 kW each (80%). |
| 23 | Name two limits of modular UPS. | Shared frame components (busbar, bypass, controls) and proprietary modules or firmware compatibility. |
| 24 | Why is MTTR lower in a modular UPS? | Hot-swappable modules can be replaced in minutes by operations staff. |
| 25 | What does a dual-input UPS improve? | Separate feeds to the rectifier and bypass, so one supply fault doesn't affect both. |
| 26 | Two 99.9% UPS in parallel (1+1). What is the availability? | 1 − 0.001² = 99.9999%. |
| 27 | A parallel UPS system of 99.9999% has a common bus of 99.99%. What is the total? | About 99.99%: the common bus limits it. |
| 28 | What does a distributed (per-unit) static bypass avoid? | A common bypass being a single point of failure. |
| 29 | What is a DRUPS, and what stores its energy? | A diesel rotary UPS: a motor-generator, flywheel and diesel engine. The flywheel stores kinetic energy. |
| 30 | What is the ride-through of a flywheel, and what takes over after? | About 8 to 15 seconds (up to 30 s or more in some designs), and the diesel engine takes over. |
| 31 | How much energy does a flywheel hold for 2 MW for 12 seconds? | 2,000 kW × 12 s = 24,000 kJ = 6.7 kWh. |
| 32 | How does that compare with a 10-minute battery at 1 MW? | The battery holds about 167 kWh, around 60 times more than the 10-second flywheel. |
| 33 | Name an advantage and a drawback of a DRUPS. | Advantage: no batteries, a rotating filter. Drawback: seconds of ride-through, so it depends on the diesel starting, and bearing maintenance. |
| 34 | Name four battery types for UPS. | VRLA, flooded lead-acid, nickel-cadmium, lithium-ion. |
| 35 | How does temperature affect lead-acid battery life? | Life roughly halves for every 8 to 10 °C above 25 °C. |
| 36 | A 10-year design-life VRLA runs at 35 °C. What life can you expect? | About 5 years. |
| 37 | Name three advantages and one drawback of lithium-ion over VRLA. | Longer life, less weight and space, built-in monitoring. Drawback: higher upfront cost and thermal runaway and fire-code requirements. |
| 38 | How many 2 V cells make a 480 V string, and what is the end-of-discharge voltage at 1.75 V per cell? | 240 cells. 240 × 1.75 = 420 V. |
| 39 | A 500 kW load for 10 minutes at 95% inverter efficiency. What battery energy before margins? | 500 × 10/60 / 0.95 = 87.7 kWh. |
| 40 | Why use the manufacturer's tables at the 10-minute rate for sizing? | Capacity at a high discharge rate is less than the rated Ah (Peukert effect). |
| 41 | Why can't float voltage tell you a battery's capacity? | The charger holds the same terminal voltage on a weak battery, so only a discharge test reveals capacity. |
| 42 | What standards cover vented and VRLA battery testing? | IEEE 450 (vented) and IEEE 1188 (VRLA). |
| 43 | At what capacity should a battery be replaced? | About 80% of rated capacity. |
| 44 | A battery rated for 10 minutes lasts 8 minutes 30 seconds in a test. What is the capacity? | 85%. It is below 90%, so test annually and plan replacement. |
| 45 | An ohmic reading rises from 4.0 mΩ to 5.4 mΩ. What is the change and what action? | +35%, which is significant. Schedule a capacity test. |
| 46 | Can ohmic testing replace a capacity test? | Generally no. It flags weak cells but doesn't measure capacity (unless the owner's programme and any regulator accept it). |
| 47 | What are the typical VRLA inspection frequencies? | Monthly visual and voltage checks, quarterly ohmic checks, annual connection resistance, periodic capacity tests. |
| 48 | What is a BESS made of? | Cells and modules, BMS, PCS (bidirectional inverter), EMS, thermal management, fire protection, switchgear and communications. |
| 49 | Why shouldn't ordinary UPS batteries be used for daily peak shaving? | They are designed for float service, and frequent cycling degrades them and can void warranties. |
| 50 | Is a BESS a UPS? | No. A BESS on the medium-voltage bus can't give no-break protection against downstream low-voltage faults. |
| 51 | What is the duration of a 5 MW / 15 MWh BESS? | 3 hours. |
| 52 | A site needs 1,000 kWh. Usable depth 80%, efficiency 95%, ageing 80%. What nameplate energy? | 1,000 / 0.608 = about 1,645 kWh. |
| 53 | Why must a BESS keep a minimum state of charge when also used for backup? | The same stored energy can't be used twice, so a reserve must be protected from routine dispatch. |
| 54 | What is the difference between UL 9540 and UL 9540A? | UL 9540 certifies the energy storage system as a product. UL 9540A is a test method for thermal runaway fire propagation. |
| 55 | Which fire code governs stationary energy storage installations? | NFPA 855 (2026 edition current). |
| 56 | Why does thermography need the equipment under load? | Heat from a bad connection is I²R, so it only appears with current. Typically at least about 40% load. |
| 57 | Why does bare shiny metal give a wrong temperature reading? | Low emissivity: it reflects its surroundings instead of radiating its own heat. |
| 58 | A connection is 18 °C above a similar component. What is the NETA priority? | Major deficiency (over 15 °C), repair immediately. |
| 59 | A hot lug is 28 °C above a similar lug at 60% load. What is the corrected ΔT? | 28 × (1/0.6)² = about 78 °C. |
| 60 | What is an IR window, and why is it useful? | A permanent infrared-transparent port that allows scanning with the cover closed, keeping the thermographer outside the arc-flash boundary. |
| 61 | What does NFPA 70B require for thermography intervals? | Intervals tied to equipment condition: 12 months for Conditions 1 and 2, 6 months for Condition 3. |
| 62 | Does "repair immediately" mean you can work on live equipment? | No. It sets a maintenance priority only. Energised work needs a qualified person, a permit and PPE. |

### Mixed review across Module 6

*Notes: [06_power_infrastructure.md](06_power_infrastructure.md). 20 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Put in order: UPS, LV main board, transformer, rack PDU, PDU. | Transformer, LV main board (with the ATS and generator), UPS, PDU, rack PDU. |
| 2 | Why does higher voltage reduce losses? | For the same power, higher voltage means lower current, and loss is I² × R. |
| 3 | Size a generator per your slide: UPS 400 kW (high harmonics) and 300 kW cooling and lighting. | 400 × 1.2 + 300 × 1.0 = 780 kW. |
| 4 | What load does each module carry in an N+1 UPS with N = 3? | 3/4 = 75%. |
| 5 | What is faster, an ATS or an STS, and why does it matter? | An STS (a few ms). It stays inside the 20 ms ITIC dropout limit, whereas an ATS needs a UPS behind it. |
| 6 | Which earthing system is preferred inside a data centre? | TN-S, with the neutral bonded to earth at one point. |
| 7 | Why is the isolation transformer delta-wye? | Delta traps third harmonics and isolates upstream. Wye gives a neutral to bond to ground. |
| 8 | What does PUE of 1.5 mean? | Total facility energy is 1.5 times the IT energy. |
| 9 | What does IP54 mean? | Dust-protected and splash-proof. |
| 10 | What is the NETA severity for a connection 18 °C above a similar component? | Major deficiency (over 15 °C): repair immediately. |
| 11 | When should a battery be replaced? | At about 80% of rated capacity. |
| 12 | Each phase carries 20 A of third harmonic. What is the neutral current? | 60 A. |
| 13 | Why must each A/B path be sized for the full load? | If one path fails, the other must carry everything. |
| 14 | What is the loading of each system in a 3N/2 design? | 66.7% normally, 100% after one failure. |
| 15 | Why use measured power, not label power, for capacity planning? | The label is a conservative worst case, often far above real use, causing oversizing and stranded capacity. |
| 16 | What does VFI-SS-11 mean? | Voltage and frequency independent, sinusoidal in both modes, best dynamic class: a double-conversion UPS in on-line mode. |
| 17 | How long is the ride-through of a rotary UPS flywheel? | About 8 to 15 seconds, so the diesel must start. |
| 18 | A site has IEEE 519 ISC/IL of 25. What TDD limit applies? | 8%. |
| 19 | 500 kW at PF 0.8. What capacitor size raises it to 0.95? | About 211 kVAR. |
| 20 | Why is a BESS not a UPS? | A BESS on the MV bus can't give no-break protection against downstream low-voltage faults. It is cycled for energy services, whereas UPS batteries float. |

### Electrical physics foundations (companion file 06a)

*Notes: [06a_electrical_physics_foundations.md](06a_electrical_physics_foundations.md). 24 questions.*

Try each question before reading the answer column.

| # | Question | Answer |
| --- | --- | --- |
| 1 | You double the transmission voltage and deliver the same power. What happens to the current? | It halves (P = V × I). |
| 2 | The current halves. What happens to cable losses? | They drop to a quarter (loss = I² × R). |
| 3 | Why does a transformer induce no voltage with steady DC? | Induction needs a changing magnetic field. DC gives a steady one. |
| 4 | A transformer has 5,000 primary turns and 250 secondary turns. What is the voltage ratio? | 20 : 1 step-down (5,000 / 250). |
| 5 | Which side of a transformer carries the higher current, and why? | The low-voltage side, because power is conserved (V × I stays about equal). |
| 6 | Why not have the utility deliver 415 V all the way from the power station? | The current would be huge, so I² × R losses and cable costs would be enormous. |
| 7 | Phase voltage is 230 V. What is the line voltage? | 230 × 1.732 ≈ 398 V, nominally 400 V. |
| 8 | Phase voltage is 120 V (as in the US). What is the line voltage? | 120 × 1.732 ≈ 208 V. |
| 9 | Which two wires give 230 V, and which two give 400 V? | 230 V: a phase wire and neutral. 400 V: two phase wires. |
| 10 | A load draws 20 A at 230 V with PF 0.8. What are S and P? | S = 230 × 20 = 4,600 VA. P = 4,600 × 0.8 = 3,680 W. |
| 11 | A 200 kVA UPS has PF 0.9. How many kW can it supply? | 200 × 0.9 = 180 kW. |
| 12 | A three-phase 400 V load is rated 50 kVA. What current does each phase carry? | 50,000 / (1.732 × 400) ≈ 72 A. |
| 13 | A three-phase load draws 50 A at 400 V, PF 1. What is its power? | 1.732 × 400 × 50 ≈ 34.6 kW. |
| 14 | Why is a transformer rated in kVA rather than kW? | Heating depends on current, and current depends on S whatever the power factor. |
| 15 | Why does a balanced three-phase system need no neutral current? | The three waves, 120° apart, sum to zero at every instant. |
| 16 | Why are three-phase supplies good for chiller compressors? | They give constant power and a smooth rotating magnetic field for induction motors. |
| 17 | Why spread rack loads evenly across L1, L2 and L3? | Unbalanced loads cause neutral current, overheating, voltage imbalance and trips. |

**Harmonics and generator questions.**

| # | Question | Answer |
| --- | --- | --- |
| 18 | What is the 3rd harmonic on a 50 Hz system? | 150 Hz (3 × 50 Hz). |
| 19 | Name two kinds of data centre equipment that create harmonics. | Any two of: server power supplies, UPS rectifiers, variable-speed drives, LED drivers. |
| 20 | Why do harmonics hurt a generator more than the utility grid? | A generator has a higher internal impedance, so harmonic currents distort its voltage more and overheat its windings. |
| 21 | Which UPS gets the × 1.2 sizing factor, and why? | A UPS with high harmonic levels, because the generator needs extra capacity to cope with the distortion. |
| 22 | UPS load 250 kW (high harmonics), cooling and lighting 180 kW. What gen-set capacity? | 250 × 1.2 + 180 × 1.0 = 480 kW. |
| 23 | Why do harmonics overload the neutral? | Third-harmonic currents from the three phases add up in the neutral instead of cancelling. |
| 24 | What is inrush current, and why does it matter for generator sizing? | The brief surge when large motors start, several times running current. The generator must handle it without its voltage collapsing. |

---

## Module 7: Electro Magnetic Fields

*Notes: [07_electromagnetic_fields.md](07_electromagnetic_fields.md). 76 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What creates an electric field, and what creates a magnetic field? | Electric field: voltage. Magnetic field: current. |
| 2 | Convert 10 mG to µT. | 10 mG = 1 µT. |
| 3 | Convert 30 A/m to µT. | 30 × 1.2566 = about 37.7 µT. |
| 4 | Which frequency band includes 50/60 Hz mains power? | ELF (0 to 300 Hz). |
| 5 | What is the wavelength at 50 Hz, and at 2.45 GHz? | 3 × 10⁸ / 50 = 6,000 km, and 3 × 10⁸ / 2.45 × 10⁹ = about 12.2 cm. |
| 6 | Why are E and B treated separately at 50 Hz? | The wavelength is thousands of km, so you are always in the near field where they are independent. |
| 7 | What is the field 5 m from a single 500 A conductor? | 2 × 10⁻⁷ × 500 / 5 = 20 µT. |
| 8 | What is the field 4 m from a go-and-return pair of 500 A, 0.2 m apart? | 2 × 10⁻⁷ × 500 × 0.2 / 16 = 1.25 µT. |
| 9 | Why do tightly bundled cables give less field? | The go and return (or three-phase) fields cancel. The field falls as 1/r² and scales with the spacing. |
| 10 | What is the power density of a far-field wave of 10 V/m? | S = E² / 377 = 100 / 377 = 0.27 W/m². |
| 11 | Which field is easy to shield, and which is hard at 50 Hz? | Electric field is easy (any grounded conductor). Magnetic field is hard. |
| 12 | Name five EMF sources in and around a data centre. | For example: transformers, busbars, large cables, switchboards, UPS and battery cables, drives, external HV lines and substations, radio transmitters. |
| 13 | State the net-current rule. | The far field depends on the sum of all currents in the group. If everything returns in the same bundle, the net current is zero and the field falls quickly. |
| 14 | How does TN-C create magnetic fields? | Neutral current flows in earth conductors and building metalwork, creating a net current along the structure. |
| 15 | Find the distance for 1 µT from 800 A in a pair spaced 0.2 m. | r = √(2 × 10⁻⁷ × 800 × 0.2 / 10⁻⁶) = √32 = 5.7 m. |
| 16 | Why can a busbar give a larger field than the same current in a tight cable bundle? | Busbar conductors are spaced further apart, so the cancellation is weaker. |
| 17 | What is a typical background field in a commercial building? | About 0.05 to 0.3 µT (0.5 to 3 mG). |
| 18 | What is the difference between Class A and Class B emission limits? | Class A (commercial and industrial) is less strict. Class B (residential) is stricter. |
| 19 | What field does a product tested to IEC 61000-4-8 level 3 tolerate, in µT? | 10 A/m = 12.6 µT. |
| 20 | Is the CE mark an independent guarantee? | No. It is a manufacturer's declaration of conformity. |
| 21 | What should you ask a vendor about EMF? | The EMC declaration and test reports, immunity levels (including magnetic field), operating environment limits, and installation instructions. |
| 22 | Why isn't a shielding product's "up to 60 dB" the installed performance? | The figure is a material or lab value at specific frequencies. Seams, doors and penetrations in the real installation decide the result. |
| 23 | What voltage is induced in a 0.5 m² loop by a 20 µT, 50 Hz field? | V = 2π × 50 × 20 × 10⁻⁶ × 0.5 = about 3.1 mV. |
| 24 | At what field do CRT monitors typically start to jitter? | About 1 µT (10 mG), and some from 0.3 to 0.5 µT. |
| 25 | What is the simplest fix for CRT interference? | Replace the CRT with a flat-panel display (or relocate or shield it). |
| 26 | State the ICNIRP 2010 reference levels at 50 Hz. | Public: 200 µT and 5 kV/m. Occupational: 1,000 µT and 10 kV/m. |
| 27 | What is the EU public reference level at 50 Hz? | 100 µT and 5 kV/m (Recommendation 1999/519/EC). |
| 28 | How are ELF magnetic fields classified by IARC, and why? | Group 2B, possibly carcinogenic, based on epidemiology linking childhood leukaemia to long-term averages above about 0.3 to 0.4 µT. A causal link has not been shown. |
| 29 | What is the main interaction of ELF fields with the body, and of RF fields? | ELF: induced electric fields and currents. RF: heating. |
| 30 | Which staff need special risk assessment near strong fields? | Workers with active implanted devices and pregnant workers. |
| 31 | Which directive covers worker exposure in the EU? | Directive 2013/35/EU. |
| 32 | Which standard tests power-frequency magnetic field immunity? | IEC 61000-4-8 (levels 1 to 5, 1 to 100 A/m). |
| 33 | What do IEC 61000-4-9 and 4-10 test? | Pulse magnetic field and damped oscillatory magnetic field. |
| 34 | What is the difference between EN 55032 and EN 55035? | EN 55032 covers emissions, EN 55035 covers immunity (multimedia equipment). |
| 35 | Which standard covers separation of power and data cables? | EN 50174-2. |
| 36 | Which standard measures shielding effectiveness of enclosures? | IEEE 299 (and 299.1 for small enclosures). |
| 37 | Which standard covers HEMP protection of facilities? | MIL-STD-188-125-1. |
| 38 | What is the usual commercial RF immunity level, and what does IEC 61000-4-3 test? | 3 V/m. IEC 61000-4-3 tests radiated RF immunity. |
| 39 | Name three types of electromagnetic pulse. | HEMP, lightning (LEMP), IEMI or non-nuclear weapons, ESD, switching, solar storm (GMD). |
| 40 | Describe E1, E2 and E3. | E1: nanosecond rise, up to about 50 kV/m, damages electronics. E2: lightning-like. E3: slow, induces GIC and saturates transformers. |
| 41 | Why do ordinary surge protectors fail against E1? | Metal-oxide varistors clamp in about 1 to 25 ns, as slow as or slower than E1's rise. |
| 42 | An E1 field of 50 kV/m meets an 80 dB shield. What is the field inside? | 50,000 / 10,000 = 5 V/m. |
| 43 | What is the field inside a 25 dB metal building? | 50,000 / 17.8 = about 2.8 kV/m. |
| 44 | What does MIL-STD-188-125-1 require for shielding? | About 80 dB from 10 MHz to 1 GHz and 20 dB at 10 kHz, plus pulse current injection tests on every penetration. |
| 45 | How does E3 or a solar storm harm the grid? | It induces quasi-DC currents (GIC) that saturate large transformers, causing heating, harmonics and possible grid collapse. |
| 46 | What are waveguide-below-cutoff panels used for? | Passing air or pipes through a shield without letting radio waves through. |
| 47 | What does "point of entry (POE) protection" mean? | Filtering or protecting every conductor where it crosses the shield boundary. |
| 48 | Name five design measures for low magnetic fields. | Bundle conductors, keep all phases and neutral together, balance phases, TN-S with one bond, cross-phase arrangement, route away from sensitive areas, low-field busway. |
| 49 | Why avoid placing an electrical room next to the computer room? | Magnetic fields pass through concrete walls and floors. |
| 50 | How should a magnetic field survey be done? | Three-axis true-RMS meter, grid at about 1 m above the floor, under known load, before and after energising, then scaled to maximum load. |
| 51 | A reading is 0.4 µT at 300 A. What is the estimate at 1,000 A? | 0.4 × 1,000 / 300 = 1.3 µT. |
| 52 | Why is a cross-phase arrangement used for parallel single-core cables? | Each group contains all phases, so fields cancel and circulating currents are avoided. |
| 53 | Find the distance for 1 µT from 1,500 A in a tight bundle (s = 0.1 m). | √(2 × 10⁻⁷ × 1,500 × 0.1 / 10⁻⁶) = √30 = 5.5 m. |
| 54 | Why is fibre optic cable good near strong fields? | It has no conductor, so it is immune to induced voltage and ground potential differences. |
| 55 | Put the mitigation hierarchy in order. | Avoid, reduce at the source, increase distance, shield, compensate, relocate or replace equipment, operational controls. |
| 56 | What does 40 dB of shielding effectiveness mean? | The field is reduced by a factor of 100. |
| 57 | Why doesn't a copper Faraday cage stop 50 Hz magnetic fields? | Thin metal is much thinner than the skin depth (9.3 mm at 50 Hz), so little opposing eddy current forms. Grounding doesn't change it. |
| 58 | What is the skin depth of copper and of mild steel at 50 Hz? | Copper about 9.3 mm. Mild steel (µr ≈ 200) about 1.6 mm. |
| 59 | How thick must copper be for 40 dB at 50 Hz by absorption alone? | 4.6 skin depths, about 43 mm. |
| 60 | What shielding does 3 mm of copper give at 50 Hz? | About 8.686 × 3 / 9.3 = 2.8 dB. |
| 61 | Why must mu-metal be annealed after fabrication? | Bending, forming and welding sharply reduce its permeability, which the heat treatment restores. |
| 62 | A 30 mm slot at 1 GHz: what is the approximate SE? | 20 log₁₀(0.3 / 0.06) = about 14 dB. |
| 63 | What is the cutoff frequency of a 6 mm circular waveguide opening? | About 175.8 / 6 = 29 GHz. |
| 64 | What size should an aluminium screening plate in front of a busbar system be? | At least twice the size of the busbar system, placed symmetrically in front of it. |
| 65 | Does a cable screen stop 50 Hz magnetic coupling? | Little. Use twisted pairs, balanced signalling, small loops and distance. |
| 66 | How should a cable screen be terminated? | 360° at the connector, bonded at both ends only where the bonding network is equipotential, otherwise at one end. |
| 67 | What does a RF shielded room need at doors and entries? | RF doors with finger stock, filtered power and signal entries, WBC for air and pipes, non-conductive fibre feedthroughs. |
| 68 | Why is distance usually better than shielding for power-frequency fields? | Fields fall quickly with distance, while magnetic shielding is expensive, thick and easily defeated by seams and penetrations. |
| 69 | Name the two main types of EMF, what causes each, and their units. | Electric field (caused by voltage, in V/m) and magnetic field (caused by current, in A/m for H and tesla, µT or mG for B). |
| 70 | Convert 5 mG to µT, and 2 A/m to µT. | 5 mG = 0.5 µT. 2 A/m = 2 × 1.2566 = 2.5 µT. |
| 71 | Name the main exposure norms for the public and for workers. | Public: ICNIRP 2010 (200 µT at 50 Hz) and the EU recommendation 1999/519/EC (100 µT). Workers: EU Directive 2013/35/EU, with action levels and risk assessment. |
| 72 | Which standard tests equipment immunity to 50/60 Hz magnetic fields, and over what range? | IEC 61000-4-8, with levels 1 to 5 from 1 to 100 A/m (about 1.3 to 126 µT). |
| 73 | List five best practices for a low-EMF data centre. | For example: site away from external sources, keep electrical rooms away from the white space, bundle phases, neutral and earth together, balance phases, TN-S with one bond, separate power and data, use fibre or shielded twisted pair, measure after energising. |
| 74 | Name the main potential sources of EMF in and around a data centre. | Transformers, busbars and bus ducts, large cables, switchboards, UPS and battery cables, drives, stray neutral or earth currents, external HV lines, substations and transmitters. |
| 75 | What makes an EMF source strong? | High current, wide spacing of go and return conductors, net current, unbalance, harmonics, and closeness. |
| 76 | List the ways to reduce EMF in order of preference. | Avoid, reduce at the source, increase distance, shield, compensate or relocate, operational controls, and verify by measurement. |

---

## Module 8: Equipment Racks

*Notes: [08_equipment_racks.md](08_equipment_racks.md). 63 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Which standard defines the 19-inch rack, and what are its international equivalents? | EIA-310 (now EIA/ECA-310), with IEC 60297 and DIN 41494 as equivalents. |
| 2 | How many millimetres is 1U, and how many holes does a U have? | 44.45 mm and 3 holes, spaced 15.875, 15.875 and 12.7 mm. |
| 3 | Give the three width figures of a 19-inch rack. | 482.6 mm panel width, 465.1 mm hole spacing and about 450.85 mm clear opening. |
| 4 | What is the mounting height of a 42U rack? | 42 × 44.45 = 1,866.9 mm. |
| 5 | What is the actual panel height of a 2U device? | 44.45 × 2 − 0.794 = about 88.1 mm. |
| 6 | Is 19 inches the width of the cabinet? | No. It is the equipment front panel width. Cabinets are commonly 600 or 800 mm wide. |
| 7 | What does EIA-310 not specify? | Rack depth, outside width, doors, and load rating. |
| 8 | What are the ETSI rack mounting width and unit height? | 535 mm (21 inch) and 25 mm. |
| 9 | What are the OCP Open Rack bay width and unit height? | 21 inch and 48 mm (OpenU). |
| 10 | What does TIA-942-C require for cabinet width in the MDA, IDA and HDA? | At least 800 mm. |
| 11 | How much total side space does a 600 mm cabinet have for a 482.6 mm panel? | 600 − 482.6 = about 117 mm. |
| 12 | Why use an 800 mm cabinet? | Room for vertical cable managers and 0U PDUs at the sides without blocking airflow. |
| 13 | How many 600 mm floor tiles do three 800 mm cabinets span? | 3 × 800 = 2,400 mm = 4 tiles. |
| 14 | A server is 750 mm deep, with 40 mm of front handles and 150 mm of rear cable space. What usable depth is needed? | 750 + 40 + 150 = 940 mm. |
| 15 | Why can external depth mislead? | The usable depth between the rails is less, because of doors, frame and cable space. |
| 16 | Will a 48U cabinet of 2,200 mm external height fit under a 2.6 m clear ceiling with a 460 mm nozzle clearance? | No: 2,200 + 460 = 2,660 mm, which is more than 2,600 mm. |
| 17 | What is the difference between static and dynamic load rating? | Static applies when the rack is installed and not moving. Dynamic applies while it is moved on casters, and is lower (often about a third). |
| 18 | A rack has a static rating of 1,200 kg and a dynamic rating 33% lower. What is the dynamic rating? | About 800 kg. |
| 19 | What floor pressure does a 1,200 kg rack on 0.72 m² give? | 1,200 × 9.81 / 0.72 = about 16.4 kPa. |
| 20 | A 42U rack has 36U of equipment at 300 W per U. What power does it draw? | 36 × 300 = 10.8 kW. |
| 21 | What is the main difference between a 2-post and a 4-post rack? | A 2-post holds equipment by its front ears only (cantilever) and suits light, shallow gear. A 4-post supports equipment front and rear, for deep, heavy equipment. |
| 22 | Give two limitations of a 2-post rack. | Any two of: limited depth, lower load rating, needs floor anchoring, no sliding rails for servers, no security or dust protection. |
| 23 | What is the difference between flush mount and centre mount in a 2-post rack? | Flush mount puts the equipment forward of the posts. Centre mount holds it at its centre of gravity to reduce the lever effect. |
| 24 | Name four types of 4-post racks and one limitation of each. | For example: open-frame (no security, no air separation), enclosed cabinet (restricted airflow, less usable depth), network cabinet (larger footprint, tile grid), wall-mount (shallow, light load), OCP (not 19-inch compatible). |
| 25 | Why can't an open-frame rack be converted to a cabinet later? | It isn't designed to take panels and doors, so the usual path is to replace it. |
| 26 | Why is a mis-set rail depth a problem on an adjustable 4-post rack? | If too far apart the equipment won't engage the rear rail, and if too close it binds. |
| 27 | When would you choose a wide (800 mm) network cabinet? | Where cable counts and patching are high, as in the MDA, IDA and HDA. |
| 28 | Which rack types give no physical security? | 2-post racks and 4-post open-frame racks. |
| 29 | Why is rack-level security needed when the room is already secure? | Anyone who gets into the room or cage can reach an unlocked rack, and colocation tenants share the hall. |
| 30 | List five rack security measures. | For example: keyed lock, PIN or RFID electronic lock, biometric, multi-factor, door sensors, audit trail, lockable panels, cameras, cages, locking PDUs. |
| 31 | What are the weaknesses of mechanical keys? | They can be copied, lost or shared, and there is no audit trail. |
| 32 | Give an example of multi-factor rack access. | RFID card plus PIN, or card plus fingerprint. |
| 33 | What does a rack audit trail record? | Who opened which rack, when, and for how long. |
| 34 | Why are 125 kHz proximity cards a weak choice? | They are easily cloned, so modern encrypted smart cards are better. |
| 35 | What is the difference between fail-secure and fail-safe locks? | Fail-secure stays locked when power fails. Fail-safe unlocks. |
| 36 | Which standards require documented audit trails for rack access? | PCI DSS, HIPAA, ISO/IEC 27001 and SOC 2. |
| 37 | Why fit side and rear panel sensors as well as a door contact? | To detect access through any panel, not only the front door. |
| 38 | How do you decide the security level for a rack? | By tiering: the sensitivity of the data and the criticality of the equipment. |
| 39 | Name the main levels of rack PDU. | Basic, metered, monitored, switched, outlet-metered (managed), and rack ATS. |
| 40 | What is the difference between metered and monitored? | Metered shows load locally on a display. Monitored adds network connectivity for remote reading, alarms and DCIM. |
| 41 | What does a switched PDU add? | Remote on/off of each outlet and power-on sequencing, useful at unstaffed sites. |
| 42 | What is a 0U PDU? | A vertical PDU mounted in the rack's side channel that uses no rack units. |
| 43 | What are the ratings of C13 and C19 outlets? | C13 is 10 A, C19 is 16 A. |
| 44 | What is the nameplate power of a 230 V, 32 A single-phase PDU, and at 80%? | 7.4 kW, and about 5.9 kW at 80%. |
| 45 | What is the nameplate power of a 400 V, 32 A three-phase PDU? | √3 × 400 × 32 = about 22.2 kW. |
| 46 | What continuous power does a 208 V, 30 A three-phase PDU supply at 80%? | √3 × 208 × 30 × 0.8 = about 8.6 kW. |
| 47 | A dual-corded rack draws 10 kW on 400 V three-phase. Which PDU rating is needed per feed? | 32 A three-phase (17.7 kW at 80%). A 16 A unit (8.9 kW) is too small. |
| 48 | A and B PDUs are each rated 7.4 kW. What total rack load can they support? | About 7.4 kW, not 14.8, because either must carry the whole rack. |
| 49 | Why should A and B PDUs each be sized for the whole rack? | If one feed fails, the other must carry everything. |
| 50 | What is the per-phase current of a balanced 12 kW load at 400 V? | 12,000 / (√3 × 400) = 17.3 A. |
| 51 | 30 dual-corded servers, one cord on each PDU, with 25% spare. How many outlets per PDU? | 30 × 1.25 = 37.5, so 38 outlets. |
| 52 | How do you give a single-corded device two sources? | Use a rack-mounted ATS or STS. |
| 53 | Why use locking outlets? | A bumped cord could otherwise cause an outage. |
| 54 | Why shouldn't one PDU be plugged into another? | The ampere limits compound, and the second PDU's input metering is bypassed. |
| 55 | What is the difference between block and alternating-phase outlet layouts? | Block puts each phase on a contiguous group of outlets. Alternating interleaves the phases, which helps cable routing but doesn't balance an uneven load by itself. |
| 56 | What colours do IEC 60309 plugs use for 230 V and 400 V? | Blue for 230 V and red for 400 V. |
| 57 | Why do blanking panels matter? | They stop exhaust air recirculating to the front through empty U spaces. |
| 58 | What airflow does a 6 kW rack need with a 10 K temperature rise? | 6 / (1.206 × 10) = about 0.50 m³/s (1,790 m³/h). |
| 59 | Why put heavy equipment at the bottom of a rack? | It lowers the centre of gravity and reduces the risk of tipping. |
| 60 | How should racks be bonded? | Each rack directly to the common bonded network with its own conductor, never daisy-chained (TIA-607), with doors and panels strapped. |
| 61 | Where should power and data cables run under a raised floor? | Power under the cold aisle and telecom trays under the hot aisle, kept apart (EN 50174-2). |
| 62 | What often limits a rack before space does? | Power, cooling or weight. |
| 63 | Which standard covers rack and cable labelling? | TIA-606. |

---

## Module 9: Cooling Infrastructure

### Lessons 9.1 to 9.16

*Notes: [09_cooling_infrastructure.md](09_cooling_infrastructure.md). 89 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What is the modal (most common) rack density in the Uptime Institute's 2026 survey? | About 11 kW (up from 9 kW in 2025). |
| 2 | Name four problems that rising heat loads cause. | Any four of: hot spots, recirculation and bypass, reduced equipment life, thermal throttling, short thermal ride-through, capacity limits, higher energy cost and PUE, water and refrigerant use. |
| 3 | How much heat does 1 kW of IT load produce? | 1 kW (all electrical power ends up as heat). |
| 4 | How many kW is one ton of refrigeration? | 3.517 kW (12,000 BTU/h). |
| 5 | How much air does 1 kW need at a 10 K temperature rise? | 1 / (1.206 × 10) = 0.083 m³/s (about 176 CFM). |
| 6 | How much water flow carries 1 MW at a 5 K rise? | 1,000 / (4.186 × 5) = 47.8 kg/s (about 172 m³/h). |
| 7 | Why does liquid cooling take over at high density? | Water carries about 3,500 times more heat per unit volume than air. |
| 8 | A chiller has a COP of 5. How much electricity does it use for 1 MW of cooling? | 1,000 / 5 = 200 kW. |
| 9 | What are ASHRAE's recommended server inlet temperature and dew point range? | 18 to 27 °C and a dew point of -9 to 15 °C (RH up to 70%, 50% where corrosive gases are present). |
| 10 | What is the recommended range for H1 (high-density air-cooled) equipment? | 18 to 22 °C. |
| 11 | A 500 m² hall (1,500 m³) with 250 kW of IT load loses cooling. How long for the air to rise 25 K, ignoring other thermal mass? | Heat capacity 1,809 kJ/K, rate 250 / 1,809 = 0.138 K/s, so 25 / 0.138 = about 181 s (3 minutes). |
| 12 | What are the two types of heat in air conditioning, and which do servers release? | Sensible (temperature) and latent (moisture). Servers release only sensible heat. |
| 13 | Compare the sensible heat ratio of comfort and precision cooling. | Comfort about 0.6 to 0.7, precision about 0.9 to 1.0. |
| 14 | What is the "humidity war"? | Over-dehumidifying coils pull moisture out and the humidifier puts it back, wasting energy. |
| 15 | An 80 kW IT load is cooled by a comfort unit with SHR 0.7. What rated capacity is needed? | 80 / 0.7 = about 114 kW. |
| 16 | Why is comfort cooling unsuitable as the primary cooling of a data hall? | It over-dehumidifies, gives too little airflow, isn't designed for continuous duty, and has no redundancy. |
| 17 | Name the four components of the refrigerant cycle. | Evaporator, compressor, condenser, expansion valve. |
| 18 | What does the condenser reject? | The heat absorbed at the evaporator plus the compressor's work. |
| 19 | A DX unit delivers 60 kW of cooling at a COP of 4. Compressor work and condenser heat? | 15 kW and 75 kW. |
| 20 | What is the Carnot COP for an evaporator at 10 °C and condenser at 35 °C? | 283 / (308 − 283) = 283 / 25 = 11.3 (a real unit reaches about half to 60% of that). |
| 21 | How does raising the evaporating temperature affect COP? | It reduces the lift, so COP rises (for example from 9.4 to 11.5 when the evaporator goes from 10 to 15 °C at a 40 °C condenser). |
| 22 | Give the GWP of R-410A, R-134a and R-32. | 2,088, 1,430 and 675. |
| 23 | What does safety class A2L mean? | Lower toxicity and lower (mild) flammability. |
| 24 | What GWP limit applies to new data centre cooling in the US, and from when? | 700 or less, from 1 January 2027. |
| 25 | 50 kg of R-134a leaks at 5% per year. What is the CO₂-equivalent? | 50 × 0.05 × 1,430 = 3,575 kg per year. |
| 26 | Which refrigerants replace R-410A in new DX units? | R-32 or R-454B (both A2L). |
| 27 | What is the difference between a CRAC and a CRAH? | A CRAC has its own compressor (DX). A CRAH is a fan and chilled-water coil fed by a central plant. |
| 28 | Name the three ways a CRAC rejects heat. | Air-cooled (remote condenser), water-cooled, glycol-cooled. |
| 29 | A CRAC gives 45 kW of cooling at a COP of 3. What must the condenser reject? | Compressor 15 kW, condenser 45 + 15 = 60 kW. |
| 30 | What is an advantage of a glycol-cooled CRAC? | No refrigerant pipes outdoors, freeze protection, and a free-cooling coil option. |
| 31 | Name two pros and two cons of CRAC systems. | Pros: no central plant, quick and simple, independent units. Cons: lower efficiency, many compressors, refrigerant regulation, limited free cooling. |
| 32 | What is the single point of failure of a CRAH system, and how is it managed? | The chilled water supply (chillers, pumps, piping). Use N+1 or 2N plant. |
| 33 | Why raise the chilled-water supply temperature? | It increases free-cooling hours and chiller efficiency. |
| 34 | Size a chilled water tank for 2 MW cooling, 5 minutes, 5 K rise. | 2,000 × 300 = 600,000 kJ, so 600,000 / (4.186 × 5 × 1,000) = about 28.7 m³. |
| 35 | Name four free-cooling (economiser) approaches. | Direct air-side, indirect air-side, water-side, chiller with free-cooling coil, evaporative or adiabatic. |
| 36 | Which economiser mode used the least energy in a published comparison? | Indirect air-side with an air-to-air heat exchanger (about 86% less than a baseline). |
| 37 | What is the water-use difference between cooling towers and dry coolers? | Towers evaporate water (WUE above zero). Dry coolers use air only (WUE near zero). |
| 38 | What is the difference between downflow and upflow units? | Downflow discharges into a raised floor plenum. Upflow discharges up into a duct or ceiling plenum (slab floors). |
| 39 | Where should perimeter cooling units be placed relative to the racks? | At the ends of the hot aisles, discharging along the cold aisles. |
| 40 | Why do tiles next to a downflow unit often deliver less air? | Air leaves the unit at high speed and low static pressure. |
| 41 | Give two advantages of upflow with overhead supply. | No raised floor needed (higher floor loads), air delivered where wanted, suits retrofits with little height. |
| 42 | Compare raised floor and slab cooling on cost, floor loading and liquid piping. | Raised floor: higher cost, limited loading, awkward for liquid piping. Slab: lower cost, higher loading, easy overhead piping. |
| 43 | What leakage is typical in a raised floor hall? | About 5 to 15% of the cooling air. |
| 44 | What clear height under a raised floor does the US DOE guidance recommend? | At least 610 mm (24 in). |
| 45 | Give the open area of a standard perforated tile and of a high-airflow grate. | About 25% and about 56%. |
| 46 | What underfloor static pressure is typical? | About 0.05 to 0.15 inch of water (roughly 12 to 37 Pa). |
| 47 | How much air does a 12 kW rack need at a 12 K rise? | 12 / (1.206 × 12) = 0.83 m³/s = about 2,985 m³/h (1,757 CFM). |
| 48 | How many 700 CFM directional grilles does it need? | 1,757 / 700 = 2.5, so 3. |
| 49 | Cooling units supply 40 m³/s and 12% leaks. How much air is lost? | 40 × 0.12 = 4.8 m³/s. |
| 50 | A rack is hot. What should you check first? | Blanking panels, gaps, and sealed cable cutouts, then plenum pressure, then the tile type and position. |
| 51 | Why can adding more perforated tiles make things worse? | It lowers the plenum pressure and so the air from every tile. |
| 52 | Where should power and data cables run under a raised floor? | Power under the cold aisle, data under the hot aisle, kept low and tidy. |
| 53 | Supply air is 17 °C. A rack inlet is 20 °C and the exhaust 33 °C. What is the SHI for that rack? | (20 − 17) / (33 − 17) = 3 / 16 = 0.19. |
| 54 | What do SHI and RHI add up to, and what is the ideal SHI? | They add up to 1. The ideal SHI is 0. |
| 55 | Should cooling units be controlled on return air or rack inlet temperature? | Rack inlet temperature, because that is what the servers need. |
| 56 | Name three ways to cool a slab-floor hall. | Overhead ducted supply, in-row units, rack-level units (such as rear doors), fan walls. |
| 57 | Size the duct for 3 m³/s at 6 m/s. | 3 / 6 = 0.5 m². |
| 58 | How many 30 kW in-row units are needed for 120 kW, and with N+1? | 4 units, and 5 with N+1. |
| 59 | What share of exhaust heat does a rear-door heat exchanger absorb, and what capacity? | About 60 to 95%, and about 25 to 50 kW per rack. |
| 60 | What water flow does a 25 kW rear door need at a 5 K rise? | 25 / (4.186 × 5) = 1.19 kg/s = about 4.3 m³/h. |
| 61 | What condensation rule applies to rear doors and cold plates? | Keep the water supply above the room dew point (commonly at least about 2 °C above). |
| 62 | Which approach suits a 25 kW rack? | In-row coolers or rear-door heat exchangers. |
| 63 | Define bypass airflow and recirculation. | Bypass: cold air returns to the unit without passing a server. Recirculation: hot exhaust air re-enters a server inlet. |
| 64 | Airflow is cut by 20%. By how much does fan power fall? | 0.8³ = 0.512, so about 49% less. |
| 65 | The servers need 8 m³/s at a 14 K rise, but the cooling units see a ΔT of 10 K. What airflow do they move? | 8 × 14 / 10 = 11.2 m³/s, 140% of the IT airflow. |
| 66 | What must be in place before installing containment? | Blanking panels, sealed gaps and cutouts, matched airflow, and a fire protection review. |
| 67 | Under NFPA 75, when can sprinkler or gas modification be avoided? | When automatic smoke detection removes the obstruction before suppression operates, egress isn't compromised, and protection isn't reduced. |
| 68 | Why are fusible-link drop-away panels out of favour? | The fire must grow large before they trip, gas is released on smoke, they can block escape, and they need replacing. |
| 69 | What must devices inside a hot aisle be? | Rated for the hot aisle temperature. |
| 70 | Which containment is simpler for a raised-floor retrofit, and which suits ceiling returns? | Cold aisle containment, and hot aisle containment. |
| 71 | In the published comparison with the room held at 24 °C, which gave the better PUE? | Hot aisle containment (1.69) against cold aisle containment (1.98). |
| 72 | What is the hot aisle temperature for a 27 °C inlet and an 18 K rise? | 27 + 18 = 45 °C. |
| 73 | Name the main types of liquid cooling. | Rear-door heat exchanger, direct-to-chip (single-phase, two-phase), single-phase and two-phase immersion. |
| 74 | What does the ASHRAE class W32 mean? | Facility water supplied at up to 32 °C (minimum 2 °C), with equipment that runs at full performance across that range. |
| 75 | What do the TCS, FWS and CDU do? | The TCS is the coolant loop to the cold plates, the FWS carries heat to the plant, and the CDU separates and controls them. |
| 76 | What water flow does a 60 kW rack need at a 10 K rise? | 60 / (4.186 × 10) = 1.43 kg/s = about 86 L/min (5.2 m³/h). |
| 77 | A hall is built for W40 with a 4 K CDU approach. What coolant temperature reaches the cold plates? | 40 + 4 = 44 °C. |
| 78 | A 100 kW rack sends 75% of its heat to liquid. How much goes to air? | 25 kW. |
| 79 | Why does immersion cooling face PFAS issues? | Many two-phase fluids are fluorinated chemicals under regulatory restriction. |
| 80 | What does STES stand for and what does it do? | Seasonal thermal energy storage: it stores heat or cold for months for use in the opposite season. |
| 81 | What are ATES and BTES? | Aquifer thermal energy storage (a doublet of wells) and borehole thermal energy storage (vertical boreholes in the ground). |
| 82 | What flow carries 2 MW at an 8 K difference? | 2,000 / (4.186 × 8) = 59.7 kg/s = about 215 m³/h. |
| 83 | How much energy does 1 m³ of water store for an 8 K difference? | About 9.3 kWh. |
| 84 | Why must an ATES be thermally balanced? | The heat stored must match the heat recovered over the years, otherwise the aquifer warms or cools progressively. |
| 85 | What cold-well temperature is typical for cooling a data centre with ATES? | About 10 to 12 °C. |
| 86 | A 2 MW cooling load needs 50 kW of pumps in passive ATES mode. What is the COP? | 2,000 / 50 = 40. |
| 87 | Where does the airflow constant 1.206 come from? | Density times specific heat of standard air: 1.2 kg/m³ × 1.005 kJ/kg·K. Each cubic metre of air carries 1.206 kJ per kelvin. |
| 88 | Use the US formula CFM = 3,160 × kW ÷ ΔT (°F) for 1 kW at a 20 °F rise. | 3,160 / 20 = 158 CFM per kW. |
| 89 | Convert a server temperature rise of 12 K to °F, and say whether airflow per kW is a fixed ratio. | 12 × 1.8 = 21.6 °F (no 32 added). No: airflow per kW depends on ΔT. |

### Thermal physics foundations (companion file 09a)

*Notes: [09a_thermal_physics_foundations.md](09a_thermal_physics_foundations.md). 31 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What is the difference between heat, heat flow and temperature? | Heat is an amount of energy (J, kWh), heat flow is energy per second (W, kW), temperature is how hot something is (°C, K). |
| 2 | How much heat does a 5 kW server rack produce each second? | 5 kJ every second (5 kW = 5 kJ/s). |
| 3 | What is the specific heat of air and of water? | Air 1.005 kJ/kg·K, water 4.186 kJ/kg·K. |
| 4 | Write the equation that links heat flow, mass flow and temperature rise. | Q = ṁ × c × ΔT. |
| 5 | What does ΔT mean in the airflow equation? | The temperature rise of the air across the servers (exhaust minus inlet), not the room temperature. |
| 6 | How much air does 1 kW need at a 10 K rise? | 1 / (1.206 × 10) = 0.083 m³/s (299 m³/h, about 176 CFM). |
| 7 | How much air does a 10 kW rack need at a 12 K rise? | 10 / (1.206 × 12) = 0.69 m³/s (about 2,490 m³/h, 1,460 CFM). |
| 8 | If the temperature rise across the servers doubles, what happens to the airflow needed? | It halves. |
| 9 | Why is air density important to the calculation? | Fans move volume, but heat is carried by mass. Thinner air (warm or at altitude) carries less heat per m³. |
| 10 | How much more airflow is needed at 1,500 m than at sea level? | About 20% more (density 1.0 instead of 1.2 kg/m³). |
| 11 | How much more heat does a cubic metre of water carry than air? | About 3,500 times (4,186 / 1.206). |
| 12 | A 60 kW rack uses water with a 10 K rise. What flow is needed? | 60 / (4.186 × 10) = 1.43 kg/s = about 86 L/min. |
| 13 | Why does a pump use less power than a fan for the same heat load? | Water needs a far smaller volume flow, so even at higher pressure the power is much lower. |
| 14 | A 500 W chip has a heat sink with a thermal resistance of 0.1 K/W. How far above the local air temperature is the chip? | 500 × 0.1 = 50 K. |
| 15 | Why do 1,000 W accelerators need cold plates? | Air heat sinks have too high a thermal resistance, so the chip would run far too hot. Water on a cold plate gives a much lower resistance. |
| 16 | What is latent heat and how large is it for water? | Heat absorbed or released when water changes state, with no temperature change. About 2,450 kJ/kg of water at room temperature. |
| 17 | A coil condenses 2 g/s of moisture. What latent load is that? | 0.002 × 2,450 = 4.9 kW. |
| 18 | A comfort unit has a sensible heat ratio of 0.65. How much of its capacity is wasted on moisture? | 35%. |
| 19 | What is the dew point, and why must cold pipes stay above it? | The temperature at which air saturates. Surfaces below it collect condensation. |
| 20 | Why does a refrigerant need a compressor? | Heat flows naturally hot to cold. The compressor supplies the work to move heat from the cool hall to the warmer outdoors. |
| 21 | What is the Carnot COP for an evaporator at 12 °C and a condenser at 37 °C? | 285 / (310 − 285) = 285 / 25 = 11.4. |
| 22 | A fan slows from 100% to 70% speed. What is the new airflow and power? | Airflow 70%, power 0.7³ = 34.3%. |
| 23 | How much water per kWh of heat is evaporated, at minimum? | About 1.5 litres (3,600 / 2,450 kg). |
| 24 | How much energy is stored in 500 m³ of water cooled by 6 K? | 500 × 1,000 × 4.186 × 6 = 12,558,000 kJ = about 3,488 kWh. |
| 25 | A 1 MW hall has an IT load heat rise of 12 K. How much air flows? | 1,000 / (1.206 × 12) = 69 m³/s (about 146,000 CFM). |
| 26 | Where does the constant 1.206 come from, and what does it mean? | Density × specific heat: 1.2 kg/m³ × 1.005 kJ/kg·K = 1.206 kJ/m³·K. Each cubic metre of air carries 1.206 kJ per kelvin of warming. |
| 27 | Where does the US factor 1.08 come from? | 60 min/h × 0.075 lb/ft³ × 0.24 BTU/lb·°F = 1.08, so BTU/h = 1.08 × CFM × ΔT (°F). |
| 28 | Convert a temperature rise of 12 K to °F. | 12 × 1.8 = 21.6 °F. For a difference you multiply by 1.8 and do not add 32. |
| 29 | Use CFM = 3,160 × kW / ΔT (°F) for a 5 kW rack with a 20 °F rise. | 3,160 × 5 / 20 = 790 CFM. |
| 30 | A rule of thumb says 160 CFM per kW. What temperature rise does it assume? | 3,160 / 160 = 19.75 °F, about 11 K. |
| 31 | Use W = 0.335 × m³/h × ΔT for a 6 kW rack with a 10 K rise. What airflow? | 6,000 / (0.335 × 10) = about 1,791 m³/h (0.50 m³/s). |

---

## Module 10: Water Supply

*Notes: [10_water_supply.md](10_water_supply.md). 60 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What is the largest use of water in a data centre with evaporative cooling? | Heat rejection (cooling towers and evaporative coolers). |
| 2 | Why does a loss of water supply behave like a loss of power? | Cooling towers can't evaporate water to reject heat, so the chillers trip and temperatures rise within minutes to hours. |
| 3 | What is the minimum water needed per kWh of heat rejected by evaporation? | About 1.47 litres (3,600 kJ / 2,450 kJ/kg). |
| 4 | 1 MW of IT load, chiller COP 5, all heat rejected by evaporation. What is the evaporation rate? | Heat rejected 1,200 kW, so 1,200 / 2,450 = 0.49 kg/s, about 1.76 m³/h. |
| 5 | Define cycles of concentration and give the blowdown formula. | The factor by which dissolved solids are concentrated compared with makeup water. Blowdown = Evaporation / (C − 1). |
| 6 | At C = 5, what is the makeup for an evaporation of 1.76 m³/h? | Makeup = 1.76 × 5 / 4 = 2.20 m³/h. |
| 7 | Define WUE and its unit. | Annual site water consumption divided by annual IT energy, in litres per kWh. |
| 8 | A 10 MW IT site has a WUE of 1.8 L/kWh. What is the annual water use? | 10,000 kW × 8,760 h = 87.6 GWh, × 1.8 = about 157.7 million litres. |
| 9 | The same site at the US fleet average WUE of 0.36? | 87.6 × 10⁶ × 0.36 = about 31.5 million litres. |
| 10 | Distinguish withdrawal, discharge and consumption. | Withdrawal is water taken, discharge is water returned, consumption is the difference: water that doesn't come back (mostly evaporated). |
| 11 | Why is a low site WUE not automatically better? | Air-cooled designs use more electricity, shifting water use to the power station. Compare WUE with PUE and the power plant's water. |
| 12 | How much water did US data centres directly consume in 2023, and how does indirect use compare? | About 66 billion litres (17.4 billion gallons) directly. Indirect (at power plants) was nearly 800 billion litres, about 12 times more. |
| 13 | Which cooling designs have near-zero site water use? | Air-cooled chillers, DX/CRAC systems, and closed-loop liquid cooling with dry coolers. |
| 14 | What does the Uptime Tier Standard require for makeup water? | At least 12 hours of on-site storage where evaporative cooling is used. At Tier III the system must be concurrently maintainable, at Tier IV fault tolerant, to the point of delivery. |
| 15 | How is the 12-hour volume calculated? | From the worst-case hour (hottest, driest weather) multiplied by the 12 hours of storage. |
| 16 | What does it mean that loss of public water is a "design condition"? | The design must handle it as a normal event, like loss of utility power, not as a failure to be tolerated by luck. |
| 17 | Makeup storage for 3 MW of IT at C = 4 and 12 hours? | 3 × 2.351 × 12 = about 84.6 m³. |
| 18 | Why size the reserve for peak demand, not the average? | Evaporation peaks on the hottest days (several times the average), which is when the supply is most stressed. |
| 19 | Which standard covers Legionella risk in building water systems, and what conditions favour the bacteria? | ASHRAE Standard 188. Warm, stagnant water. |
| 20 | Name five options for a backup water source. | Any five of: dual mains, on-site tanks, well, retention pond or rainwater, reclaimed water, tanker delivery, condensate or blowdown reuse, demand reduction. |
| 21 | Which installations need little or no backup water for cooling? | Small server rooms with DX cooling, and sites with dry coolers or air-cooled chillers (they still need fire and domestic water). |
| 22 | Why is the 72-hour or 96-hour figure not an Uptime requirement? | Those figures come from TIA-942 (Rated-3 and Rated-4) for fuel. Uptime requires 12 hours of fuel and 12 hours of makeup water. |
| 23 | A 5 MW site, C = 4, 24-hour autonomy. What net tank volume? | 5 × 2.351 × 24 = about 282 m³. |
| 24 | What gross volume if only 90% is usable? | 282 / 0.9 = about 313 m³. |
| 25 | A tank holds 300 m³ usable and the makeup rate is 11.76 m³/h. How long does it last? | 300 / 11.76 = 25.5 hours. |
| 26 | How can autonomy be stretched? | Dry-mode cooling, reducing the load, cutting non-essential uses such as irrigation. |
| 27 | A concurrently maintainable design needs 28.2 m³. Give an N+1 tank arrangement. | Three tanks of 14.1 m³ (42.3 m³ total): with one out, 28.2 m³ remains. |
| 28 | Why not use one large tank for Tier III? | If it is taken out of service there is no reserve, which fails concurrent maintainability. |
| 29 | Residence time of a 169 m³ reserve at a daily use of 56 m³? | 169 / 56 = about 3 days. |
| 30 | How do you keep stored water healthy? | Recirculate and treat it, turn it over, keep it cool, clean and inspect, and manage it under an ASHRAE 188 plan. |
| 31 | Why must the fire water reserve be separate from the cooling reserve? | So cooling use can never drain the water needed to fight a fire (NFPA 13 and 22). |
| 32 | How much fire reserve for 1,900 L/min over 60 minutes? | 114,000 litres = 114 m³. |
| 33 | How many 30 m³ tankers a day does a 5 MW site need at full evaporative load? | 282 / 30 = about 9.4 truckloads per day. |
| 34 | Name five features of a good water tank installation. | Backflow-protected inlet, overflow and drain, vent screen, redundant level sensors and alarms, recirculation and treatment, pumps on emergency power, tanker fill connection. |
| 35 | Compare above-ground and below-ground tanks. | Above ground: cheaper, easy inspection, exposed to sun and frost. Below ground: frees land, stable temperature, but costly, harder to inspect, flotation risk. |
| 36 | What is the role of NFPA 22? | Water tanks for private fire protection. |
| 37 | What must be done before relying on a well? | Test well, pump tests (step-drawdown and constant-rate), water quality baseline, impact assessment, and permits. |
| 38 | Convert a yield of 150 gpm to m³/h. | 150 × 3.785 × 60 / 1,000 = about 34.1 m³/h. |
| 39 | How many MW of IT load can a 100 gpm well supply at C = 4? | 22.7 / 2.351 = about 9.7 MW. |
| 40 | Why plan N+1 wells? | A single well is a single point of failure: pump failure, fouling or a yield drop would remove the source. |
| 41 | A 45 m³/h pump lifts 60 m at 60% efficiency. What power? | 1,000 × 9.81 × 0.0125 × 60 / 0.6 = about 12.3 kW. |
| 42 | Peak demand 25 m³/h, well 15 m³/h, tank 100 m³. How long can the tank cover the peak? | Deficit 10 m³/h, so 100 / 10 = 10 hours. |
| 43 | Give four risks of using a well. | Any four of: aquifer depletion, drawdown, impact on neighbours, subsidence, permits, quality changes, well fouling, pump failure, untested backup. |
| 44 | Why should a backup well be exercised regularly? | A well and pumps that are never used can fail silently, and water quality changes. |
| 45 | What is a pump-and-inject system, and what is its net consumption? | Groundwater is pumped through a heat exchanger and returned to the aquifer through an injection well, so net consumption is zero. |
| 46 | At 2 gpm per ton, what flow does 1 MW of cooling need? | 284 tons × 2 = 568 gpm, about 129 m³/h. |
| 47 | Distinguish detention and retention ponds. | A detention pond is normally dry and controls peak flow. A retention pond keeps a permanent pool and also treats the water. |
| 48 | Runoff from 5 ha with a 120 mm design storm and C = 0.85? | 0.85 × 0.120 × 50,000 = 5,100 m³. |
| 49 | Annual yield from a 20,000 m² roof, 0.8 m rainfall, 85% capture? | 20,000 × 0.8 × 0.85 = 13,600 m³, about 37 m³ per day. |
| 50 | Why do annual averages mislead for rainwater supply? | Demand peaks in dry, hot spells, so the tank or pond can empty. Model storage through a dry period. |
| 51 | Demand is 40 m³/day and a dry spell lasts 60 days. What storage is needed, and what pond area at 3 m depth? | 2,400 m³, so 800 m². |
| 52 | How much does an 800 m² pond lose to evaporation at 1.5 m per year? | 800 × 1.5 = 1,200 m³ per year (about 3.3 m³/day). |
| 53 | Name four treatments for pond or harvested water. | First-flush diversion, sedimentation forebay, filtration, disinfection, algae control, backflow protection. |
| 54 | Which standards cover rainwater and stormwater harvesting? | CSA B805 / ICC 805, ARCSA/ASPE/ANSI 63 (rainwater catchment) and 78 (stormwater harvesting). |
| 55 | Why is a pond unsuitable as the only backup source? | It depends on rainfall, quality varies, it loses water to evaporation, and a drought can leave it empty. |
| 56 | Name other on-site water sources. | CRAH and air handler condensate, blowdown reuse, greywater, reclaimed water. |
| 57 | In the 5 MW example, air-cooled (PUE 1.5, WUE 0) vs. evaporative (PUE 1.3, WUE 1.8): which has more total water, and which more site water? | Total: 297 vs. 336 million litres (evaporative more). Site water: 0 vs. 78.8 million litres (evaporative far more locally). |
| 58 | What is source WUE? | Site WUE plus the water consumed at the power plants that make the facility's electricity. |
| 59 | List the layers of a defence-in-depth water supply. | Dual mains, on-site storage, independent source (well, pond, reclaimed), tanker delivery, demand reduction. |
| 60 | What permits might a data centre need for water? | Water-use or water-rights permits for wells and surface water, discharge permits for blowdown (NPDES in the US), and stormwater permits for ponds. |

---

## Module 11: Designing a Scalable Network Infrastructure

*Notes: [11_network_infrastructure.md](11_network_infrastructure.md). 92 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What is structured cabling? | A standards-based, hierarchical, modular cabling infrastructure with patch panels and defined pathways, independent of the applications it carries. |
| 2 | Why is structured cabling better than point-to-point cabling? | Changes are patch cord changes, growth is planned, links are tested and documented, and it follows standards. |
| 3 | How long is the cable plant expected to last? | About 10 to 25 years, across several generations of equipment. |
| 4 | Which TIA standards cover copper, fibre, pathways, administration and data centres? | TIA-568.2-E (copper), 568.3-E (fibre), TIA-569 (pathways and spaces), TIA-606 (administration), TIA-942-C (data centres). |
| 5 | What is the difference between the TIA and ISO naming? | TIA names the cable category (Category 6A). ISO/IEC names the channel class (Class EA). |
| 6 | Give five planning considerations. | Any five of: capacity and growth, speed roadmap, media choice, topology, pathways and spaces, density, labelling, fire performance, redundancy, testing and documentation, PoE, cost. |
| 7 | 20 racks, 20 servers each, 2 links per server. How many horizontal cables for end-of-row, and how many fibre uplinks for top-of-rack with 2 switches per rack and 2 uplinks each? | End-of-row: 20 × 20 × 2 = 800. Top-of-rack: 20 × 2 × 2 = 80 uplinks. |
| 8 | Why twist the pairs in copper cable? | Both wires pick up noise equally so the receiver, reading the difference, rejects it. Different twist rates reduce crosstalk. |
| 9 | What does S/FTP mean? | Overall braid shield and a foil shield on each pair. |
| 10 | Give the bandwidth of Cat 5e, 6, 6A and 8. | 100 MHz, 250 MHz, 500 MHz and 2,000 MHz. |
| 11 | What does Cat 6A support at 100 m? | 10GBASE-T (10 Gb/s). |
| 12 | How far can Cat 6 carry 10GBASE-T? | About 37 to 55 m, depending on the crosstalk environment. |
| 13 | What are the speed and distance limits of Cat 8? | 25GBASE-T and 40GBASE-T over 30 m (two connectors). |
| 14 | Which categories does TIA recognise, and what is Cat 7? | Cat 5e, 6, 6A and 8. Cat 7 and 7A are ISO classes (F and FA) only. |
| 15 | Define the 100 m copper channel. | 90 m permanent link plus up to 10 m of patch and equipment cords. |
| 16 | A 90 m permanent link has 15 m of patch cords. Is it compliant? | No: 105 m exceeds the 100 m channel and the cords alone exceed the 10 m allowance. |
| 17 | Give the power of 802.3af, 802.3at and 802.3bt. | 15.4 W, 30 W, and up to 60 W (Type 3) or 90 W (Type 4). |
| 18 | Which wiring scheme is recommended for new installations, and what must you avoid? | T568A is recommended. Never mix T568A and T568B on one cable or installation. |
| 19 | How far does passive direct-attach copper reach? | About 3 to 5 m. |
| 20 | How much untwisting is acceptable at a copper termination? | About 13 mm or less. |
| 21 | Name three pros and three cons of copper. | Pros: low cost, PoE, easy termination. Cons: distance limit, bulk, speed ceiling, EMI, heating in PoE bundles. |
| 22 | What are the core sizes of single-mode and multimode fibre? | About 9 µm and 50 µm. |
| 23 | How much latency does fibre add per km? | About 5 µs one way (10 µs round trip). |
| 24 | Compare OM3 and OM4 bandwidth. | 2,000 MHz·km and 4,700 MHz·km at 850 nm. |
| 25 | What are the jacket colours of OM3, OM4, OM5 and OS2? | OM3 aqua, OM4 aqua or erika violet, OM5 lime green, OS2 yellow. Colour is a convention: read the print. |
| 26 | What is the reach of 10GBASE-SR on OM3 and OM4? | 300 m and 400 m. |
| 27 | What is the reach of 40GBASE-SR4 and 100GBASE-SR4 on OM4? | 150 m and 100 m. |
| 28 | When does OM5 give more reach than OM4? | Only with multi-wavelength (SWDM) optics, for example 100G SWDM4 reaches 150 m on OM5 against 100 m on OM4. |
| 29 | Give the reach of LR, ER, ZR, DR4 and FR4. | 10 km, 40 km, 80 km, 500 m and 2 km. |
| 30 | When should you choose single-mode over multimode? | For trunks, runs over about 550 m, campus links, and any pathway meant to outlive the current speed. |
| 31 | What is the difference between UPC and APC? | UPC is a flat polish (blue). APC is angled 8° (green) to reduce back-reflection. Never mate them. |
| 32 | Name the three MPO polarity methods. | A (straight-through), B (reversed), C (pair-flipped). Use one method end to end. |
| 33 | 250 links at 100G: how many fibres with SR4, and with SWDM4 on OM5? | SR4: 250 × 8 = 2,000 fibres. SWDM4: 250 × 2 = 500 fibres. |
| 34 | A 120 m run needs 100GBASE-SR4. Does OM4 work? | No. OM4 supports 100 m. Use OM5 with SWDM4, single-mode, or shorten the run. |
| 35 | A 100G channel over OM4 allows 1.5 dB. With 4 mated pairs at 0.5 dB and 0.35 dB of fibre, what happens? | 0.35 + 2.0 = 2.35 dB, which exceeds 1.5 dB, so the link fails its budget. |
| 36 | What is the rule for connectors before mating? | Inspect, clean, inspect, then mate. |
| 37 | Which form factors carry 100G, 400G and 800G? | QSFP28 (100G), QSFP-DD (400G), QSFP-DD or OSFP (800G). |
| 38 | Define ER, MDA and HDA. | ER: where carrier cables enter and meet the internal cabling. MDA: the central area with the main cross-connect and core switches. HDA: the distribution area with the horizontal cross-connect and access switches. |
| 39 | Which TIA-942 spaces are optional? | The IDA and the ZDA. |
| 40 | What is the maximum horizontal channel length? | 100 m (90 m permanent link plus cords). |
| 41 | What topology does the backbone use? | A star. |
| 42 | Compare a cross-connect and an interconnect. | A cross-connect joins two sets of patch panels with patch cords (flexible, more connections). An interconnect connects equipment directly to the permanent cabling (fewer connections, less flexible). |
| 43 | Name three changes in TIA-942-C. | 800 mm cabinets in the MDA, IDA and HDA, at least two fibres on each run, single-pair cabling, edge and immersion cooling content. |
| 44 | Where should telecom cabling and power be routed relative to the aisles? | Telecom in or above the hot aisle, power under the cold aisle, and fibre kept separate from copper. |
| 45 | What labelling does TIA-606 call for? | Unique identifiers on racks (for example tile coordinates), labels at both ends of every cable, and records. |
| 46 | What does TIA-942 require of cabling at Rated-3 and Rated-4? | Redundant, physically separated pathways. Rated-4 also redundant entrance room, main distribution area and backbone. |
| 47 | How far apart should a secondary entrance room be? | About 20 m, in a separate fire zone. |
| 48 | The MDA serves 10 HDAs, each with 24 fibres on two paths. How many fibres and MPO-24 trunks? | 10 × 2 × 24 = 480 fibres, 20 trunks. |
| 49 | Why does routing A and B through one tray not give redundancy? | They share a failure mode: one tray fire or crush takes out both. |
| 50 | Why measure the routed length? | Cable follows trays, rises and slack, which often adds 20 to 30% to a straight-line estimate. |
| 51 | Distinguish verification, qualification and certification. | Verification: is it connected correctly. Qualification: can it support an application. Certification: does it meet the full standard, with a recorded result. |
| 52 | What is the difference between a permanent link and a channel test? | The permanent link is the installed cabling (up to 90 m) without patch cords. The channel is end to end including cords (up to 100 m). |
| 53 | Name five copper test parameters. | Wire map, length, insertion loss, NEXT (and PS NEXT), ACR-F, return loss, delay and skew, alien crosstalk, DC resistance. |
| 54 | What is the classic cause of a NEXT failure? | Untwisted pairs at the connector. |
| 55 | Which tester levels suit Cat 6A and Cat 8? | Level 2G for Cat 6A and Level VI for Cat 8. |
| 56 | A Cat 6A cable is terminated on Cat 6 connectors. What does it certify as? | Cat 6. |
| 57 | Distinguish Tier 1 and Tier 2 fibre testing. | Tier 1 uses an OLTS to measure loss, length and polarity. Tier 2 adds an OTDR trace and event table. |
| 58 | Budget for a 300 m OM4 link at 850 nm with 3 mated pairs. | 0.3 × 3.5 + 3 × 0.75 = 1.05 + 2.25 = 3.3 dB. |
| 59 | Budget for a 5 km OS2 link with 2 connector pairs and 2 splices. | 5 × 0.4 + 2 × 0.75 + 2 × 0.3 = 2.0 + 1.5 + 0.6 = 4.1 dB. |
| 60 | Why test at two wavelengths? | 850 and 1300 nm for multimode, 1310 and 1550 nm for single-mode, because loss differs with wavelength and bends affect longer wavelengths more. |
| 61 | Why record the OLTS reference method? | One-jumper and three-jumper methods differ by about 0.75 dB. |
| 62 | Why use launch cables with an OTDR? | To move the first connector out of the instrument's dead zone (typically 100 to 500 m of fibre). |
| 63 | Why can the application's loss budget be tighter than the standard's? | The standard allows 0.75 dB per connector pair, while a transceiver such as 100GBASE-SR4 allows only about 1.5 dB in total. The tighter limit governs. |
| 64 | Can an OTDR event loss be compared directly with a calculated OLTS budget? | No. They are different measurements. |
| 65 | Define redundancy and diversity. | Redundancy is spare capacity or a second path. Diversity is physical independence so one event cannot take out both. |
| 66 | What is a common-mode failure in cabling? | One cause, such as a shared duct, that takes out several "redundant" paths at once. |
| 67 | With 4 spines, how much bandwidth remains after one fails? | 75% (3 of 4). |
| 68 | A leaf has 32 × 25G ports and 4 × 100G uplinks. What is the oversubscription, and after losing one uplink? | 800 / 400 = 2:1, then 800 / 300 = 2.67:1. |
| 69 | How are servers dual-homed to two switches? | With MLAG (vPC) or EVPN multihoming (ESI-LAG), using LACP. |
| 70 | What does ECMP do? | Spreads flows across all equal-cost paths, hashing each flow to one path to keep packets in order. |
| 71 | Two independent 99.9% links in parallel. What availability, and with a shared duct of 99.95%? | 99.9999%, and about 99.95% with the shared duct. |
| 72 | Why deploy border leaves in pairs and use BGP multihoming? | So one border device or one carrier failing doesn't cut the connection to the outside. |
| 73 | Give the recovery times of BFD, optical 1+1 and fast reroute. | BFD detects in milliseconds, optical 1+1 under 5 ms, IP/MPLS fast reroute and SONET/SDH rings under 50 ms. |
| 74 | Why have an out-of-band management network? | To reach and manage equipment when the production network is down. |
| 75 | List five options for connecting sites. | Any five of: dark fibre, managed wavelength, own DWDM/CWDM, Carrier Ethernet (EPL/EVPL), MPLS or IP VPN, internet with IPsec or SD-WAN, cloud on-ramp, wireless. |
| 76 | Give the three DCI distance classes. | Campus under 10 km, metro 10 to 120 km, long haul over 120 km. |
| 77 | What are the one-way and round-trip latency of 100 km of fibre? | 0.5 ms one way and 1.0 ms round trip. |
| 78 | What is the one-way latency of 120 km? | About 600 µs. |
| 79 | Estimate the unamplified reach of 400ZR with an 11 dB budget, 0.25 dB/km, 4 connectors at 0.5 dB and 2 dB margin. | (11 − 2 − 2) / 0.25 = 28 km. |
| 80 | How much capacity does 8-channel CWDM give on a fibre pair that carried 10G? | 8 × 10G = 80G. |
| 81 | Contrast dark fibre and a managed wavelength. | Dark fibre is an unlit fibre you light and operate yourself. A managed wavelength is a provider-operated optical channel. |
| 82 | What is IP over DWDM? | A coherent ZR module in the router or switch port produces a DWDM wavelength directly, removing the separate transponder. |
| 83 | What cabling practices apply between buildings? | OS2 outdoor fibre in underground ducts, at least two diverse routes with separate entry points, no copper, spare fibres and ducts, bonding of armour. |
| 84 | How are inter-site links secured? | Encryption with MACsec or IPsec, physical protection of maintenance holes and entrances, monitoring. |
| 85 | Name five things to monitor in the network. | Any five of: optical power, link errors and utilisation, device health, routing neighbours, traffic flows, latency and loss, security events, topology, configuration. |
| 86 | What is the difference between SNMP polling and streaming telemetry? | SNMP polls periodically and averages. Streaming telemetry pushes data continuously at high frequency. |
| 87 | A link runs at 100% for 30 s in a 300 s polling window. What does the poller show? | 30 / 300 = 10% utilisation. |
| 88 | Receive power falls from −2.0 dBm to −6.5 dBm. What does that mean? | A 4.5 dB loss increase, pointing to a dirty or damaged connector, a bend or a disturbed cable. |
| 89 | MTBF is 5,000 h. Compare availability with MTTR of 4 h and 1 h. | 99.920% and 99.980%. |
| 90 | What are NetFlow, IPFIX and sFlow used for? | Flow records or sampled packets that show who talks to whom, for capacity, top talkers and attack detection. |
| 91 | What does LLDP do? | Discovers neighbours so the topology map builds automatically. |
| 92 | Why must monitoring not depend on the network it watches? | Otherwise a network failure also blinds the monitoring. Use an out-of-band path. |

---

## Module 12: Fire Protection

*Notes: [12_fire_protection.md](12_fire_protection.md). 110 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Name the four elements of the fire tetrahedron. | Fuel, heat, oxygen and the chemical chain reaction. |
| 2 | Why is the incipient stage the most important to detect? | Almost nothing has burned yet, so a cheap response (isolating equipment, calling staff) works, and damage and downtime are minimal. |
| 3 | Give five common causes of data centre fires. | Any five of: UPS and battery failure (including lithium-ion thermal runaway), electrical faults and overload, switchgear and transformers, cabling, generators and fuel, hot work, combustible storage, dust, human error, arson or lightning. |
| 4 | What does the Uptime Institute's 2026 analysis say about fires? | Major data centre fires have increased gradually, with lithium-ion UPS batteries a clear contributing factor, though fires remain a small share of outages. |
| 5 | The Energy Incident Register lists 59 fires among 179 incidents. What share is that? | 59 / 179 = about 33%. |
| 6 | Name three lessons from the NIRS fire (2025). | Batteries were moved at about 80% charge (guideline below 30%), sat about 60 cm from servers, power was not fully isolated, and a single-site concentration without tested failover slowed recovery. |
| 7 | Why is smoke damaging to electronics even without flame? | Smoke particles and acid gases (for example from burning halogenated plastics) corrode and contaminate equipment. |
| 8 | Distinguish life safety systems from property protection systems. | Life safety (alarm, notification, evacuation, emergency lighting) protects people. Property protection (sprinklers, gas) protects equipment and continuity. A pre-action panel is not the building alarm panel. |
| 9 | What factors does the NFPA 75 fire risk assessment weigh? | Business impact, value of equipment and data, fire load, surrounding occupancy, redundancy from off-site backup, and continuity commitments. |
| 10 | Which standard applies to a data centre and which to a carrier switch site? | NFPA 75 for data centres, NFPA 76 for telecommunications facilities. |
| 11 | What fire separation does NFPA 75 require for the IT area? | At least 1 hour, with penetrations fire-stopped to the same rating. |
| 12 | What building does NFPA 75 require? | A fully sprinklered building of NFPA 220 Type I or II construction (or a single-storey Type II building). |
| 13 | Where is smoke detection required in an IT room? | In the room, above suspended ceilings, and below a raised floor that contains cables. |
| 14 | What finishes does NFPA 75 specify? | Class A interior wall and ceiling finishes (Class B if fully sprinklered), Class I floor finishes, and no exposed cellular plastics. |
| 15 | What portable extinguishers go in an IT room? | Clean agent or CO₂ extinguishers, not dry chemical. |
| 16 | What does NFPA 75 say about power when a total-flooding gas system discharges? | Power to protected equipment is disconnected, unless the risk assessment calls for continuous power. The room-level EPO is mainly an NEC 645.10 provision. |
| 17 | What does FM Global Data Sheet 5-32 say about lithium-ion batteries in racks? | It does not accept gaseous or water mist as primary protection and recommends a wet sprinkler system with increased density. |
| 18 | What fire provision does Tier IV add? | 1-hour fire-rated partitions between complementary critical systems. |
| 19 | When does a fire standard become mandatory? | When a law or building code adopts it, the AHJ enforces it, or a contract or insurer requires it. |
| 20 | Name six types of fire detector. | Photoelectric smoke, ionisation smoke, multi-criteria, heat, flame, beam, aspirating (ASD), off-gas, linear heat cable. |
| 21 | What are the EN 54-20 aspirating detector classes? | Class A very high sensitivity, B enhanced sensitivity, C normal sensitivity. |
| 22 | What are the NFPA 76 detection levels? | Very early warning (VEWFD), early warning (EWFD) and standard fire detection (SFD). |
| 23 | A 2,000 ft² room needs one ASD sampling hole per 400 ft². How many holes? | 2,000 / 400 = 5 holes. |
| 24 | An ASD with Fire level 1 at 0.2%/ft has 8 sampling holes. What is the single-hole equivalent sensitivity? | 0.2 × 8 = 1.6%/ft. |
| 25 | How many spot detectors at 900 ft² each for 3,000 ft²? | 3,000 / 900 = 3.3, so 4 detectors. |
| 26 | What is cross-zoning? | Two detectors in different zones (or two thresholds) must agree before a suppression system is released. |
| 27 | A panel draws 0.4 A standby and 2 A in alarm. Size the battery for 24 h standby plus 5 min alarm with a 25% margin. | 0.4 × 24 = 9.6 Ah, plus 2 × 5/60 = 0.17 Ah, total 9.77 Ah, × 1.25 = about 12.2 Ah. |
| 28 | What new detection does NFPA 75 (2024) require for lithium-ion UPS? | Off-gas detection to catch electrolyte vapour before thermal runaway. Conventional flammable gas sensors do not substitute. |
| 29 | How often should detection be serviced under BS 5839-1? | Every 6 months, with three-monthly recommended for data centres. |
| 30 | Where should detection be placed in a data centre? | Room volume, return air paths and CRAC intakes, under the floor, above the ceiling, in or on critical racks, in battery, electrical and UPS rooms. |
| 31 | Name the four main sprinkler system types and what fills the pipes. | Wet (water), dry (air or nitrogen), pre-action (air, nitrogen or empty) and deluge (dry with open heads). |
| 32 | Distinguish single and double interlock pre-action. | Single: detection opens the valve and fills the pipes, and a head must then fuse. Double: both detection and a head opening are required before water enters the pipes. |
| 33 | Why do data centres prefer pre-action sprinklers? | The pipes are normally dry, so a leak or damaged head does not discharge water, and water needs detection plus a head opening. |
| 34 | What flow does a K = 5.6 head give at 10 psi? | Q = 5.6 × √10 = 17.7 gpm. |
| 35 | Ordinary group 2 hazard (0.20 gpm/ft² over 1,500 ft²). What is the demand, and with the +30% area for pre-action? | 300 gpm, and 0.20 × 1,950 = 390 gpm. |
| 36 | Light hazard: 0.10 gpm/ft² over 1,500 ft² for 30 minutes. What volume? | 150 gpm × 30 min = 4,500 gal = about 17 m³. |
| 37 | What bulb colour and temperature is the common sprinkler head? | Red, 68 °C. |
| 38 | Which standard covers water mist? | NFPA 750. |
| 39 | What does a deluge system do? | All heads are open, and a detection signal opens the valve so water flows from all heads. Used for high-hazard areas. |
| 40 | Is a pre-action system a life safety system? | No. It protects property. Occupant notification comes from the building fire alarm panel. |
| 41 | What is the NFPA 25 test for pre-action valves? | A trip test every year. |
| 42 | How many sprinklers can one single-interlock pre-action valve control? | No more than 1,000 under NFPA 13. |
| 43 | How quickly must water reach the farthest head of a dry system? | About 60 seconds. |
| 44 | How do gas agents extinguish fires? | Halocarbons absorb heat (and interrupt the chemistry), inert gases dilute oxygen below the combustion limit. |
| 45 | What is a clean agent? | Non-conducting, volatile or gaseous, and leaves no residue. |
| 46 | Give four differences between halocarbon and inert gas systems. | Halocarbons: liquid storage, few cylinders, 10 s discharge, GWP of concern. Inert gases: high-pressure cylinders (200 to 300 bar), many cylinders, 60 to 120 s discharge, zero GWP, loud. |
| 47 | Give the Class A design concentrations of FK-5-1-12, HFC-227ea and IG-541. | 4.5%, 6.7% and 34.2%. |
| 48 | How much HFC-227ea for a 300 m³ room at 6.7% (0.523 kg/m³)? | 0.523 × 300 = about 157 kg. |
| 49 | How much IG-541 free gas for a 300 m³ room at 34.2% (0.419 m³/m³)? | 0.419 × 300 = about 126 m³. |
| 50 | What is the residual oxygen after IG-541 at 40%? | 20.9 × 0.60 = 12.5%. |
| 51 | State the NOAEL of HFC-227ea and FK-5-1-12. | 9.0% and 10.0%. |
| 52 | What is the maximum occupant exposure to clean agents? | 5 minutes, with a pre-discharge alarm and delay. |
| 53 | What are the discharge times of halocarbons and inert gases? | Halocarbons 10 seconds (95% of design concentration). Inert gases 60 s (Class B) and 120 s (Class A and C) in the 2025 edition. |
| 54 | Why are inert gases cost-preferred for large rooms? | Halocarbon agent cost grows with volume, and above about 280 m³ (10,000 ft³) a cylinder bank of inert gas becomes cheaper. |
| 55 | How loud is an inert gas discharge, and what fixes it? | About 140 dB, which can damage spinning hard disks. Acoustic nozzles keep it below about 110 dB. |
| 56 | What is the AIM Act target for HFCs? | A step-down towards an 85% reduction in production and consumption by 2036. |
| 57 | Give the GWP of HFC-227ea, FK-5-1-12 and inert gases. | 3,350, under 1, and 0. |
| 58 | Why is CO₂ not used in occupied spaces? | Suppression concentrations are lethal. |
| 59 | What happened to Halon 1301? | It was phased out under the Montreal Protocol because it depletes the ozone layer. |
| 60 | Describe the operating sequence of a gas system. | Detector 1 alert, detector 2 confirms (cross-zoned), pre-discharge alarm and delay with HVAC shutdown and dampers closing and power disconnected, discharge, hold at least 10 minutes, ventilate and recover. |
| 61 | What is a typical pre-discharge delay? | About 30 to 60 seconds. |
| 62 | What rules apply to the abort switch? | It needs constant pressure, sits near the egress inside the hazard, and never defeats the manual release. |
| 63 | What is a lockout valve, and what is its main risk? | A manual valve in the discharge pipe locked closed during maintenance. Leaving it closed disables the system. |
| 64 | What concentration must be held, and for how long? | At least 85% of the design concentration for at least 10 minutes. |
| 65 | What is the held concentration for a 6.7% design? | 0.85 × 6.7 = 5.7%. |
| 66 | What is the held concentration for IG-541 at 34.2%? | 0.85 × 34.2 = 29.1%. |
| 67 | What does the door fan test measure? | The enclosure's equivalent leakage area, to predict the hold time. |
| 68 | When must a halocarbon container be refilled or replaced? | If the agent quantity loss exceeds 5% or the temperature-adjusted pressure loss exceeds 10%. |
| 69 | Why shut down HVAC at discharge, and what is the trade-off? | So the agent is held and the fire is not fed, but cooling stops and temperatures rise quickly. |
| 70 | Name causes of accidental gas discharge and cures. | False detection, a lockout valve left open, mechanical knocks. Cures: cross-zoning, staged ASD, lockout procedures, trained staff, acoustic nozzles. |
| 71 | Why are pressure relief vents needed? | The discharge, especially inert gas, adds pressure, and cooling afterwards creates a vacuum, which can damage walls and doors. |
| 72 | What is a hypoxic air (oxygen reduction) system? | A system that keeps a room permanently at about 15 to 17% oxygen with a nitrogen generator to prevent fires rather than extinguish them. |
| 73 | What altitude equals 15% oxygen at sea-level pressure? | About 2,700 m. |
| 74 | How much nitrogen takes a 300 m³ room to 15% oxygen (ideal mixing)? | 300 × ln(20.9/15) = 300 × 0.332 = about 100 m³. |
| 75 | Name three limits of hypoxic air systems. | Smouldering and pyrolysis are not prevented, lithium-ion thermal runaway is not stopped, it needs an airtight room, continuous energy, health controls and insurer acceptance. |
| 76 | What does OSHA say about oxygen below 19.5%? | It is oxygen-deficient, so entry needs a respiratory protection programme. |
| 77 | Which standards cover oxygen reduction systems? | EN 16750, ISO 20338, VdS 3527 and FM Global Data Sheet 4-13. |
| 78 | Name the three types of hypoxic air generator. | Membrane, pressure swing adsorption (PSA) and vacuum swing adsorption (VSA). |
| 79 | Why is detection still needed with hypoxic air? | Hypoxic air does not stop smouldering and pyrolysis. |
| 80 | Describe a layered protection strategy for a data hall. | Early warning (ASD) plus spot detection, cross-zoned, with pre-action sprinklers and/or clean agent, compartmentation, fire-stopping and housekeeping. |
| 81 | Why keep cardboard and packaging out of the data hall? | It adds fuel. Unpack in a staging room. |
| 82 | What makes a hot work permit effective? | It is a real controlled permit with a fire watch, detection protected and restored afterwards, not a generic form. |
| 83 | What state of charge applies when moving lithium-ion batteries? | A low charge: the guideline cited is below 30%. |
| 84 | What is an integrated systems test? | Testing detection, releasing logic, HVAC and damper interlocks, power disconnect, alarms and enclosure integrity working together. |
| 85 | What does NFPA 75 Annex B cover? | What to do in the first 24 hours for damaged electronic equipment and media. |
| 86 | Name the EN 2 and NFPA 10 fire classes. | EN: A solids, B liquids, C gases, D metals, F cooking oils. NFPA: A, B, C (energised electrical), D, K (cooking oils). |
| 87 | Which extinguisher suits a server room, and why not dry chemical? | Clean agent (A:B:C) or CO₂, because dry chemical's monoammonium phosphate residue is corrosive and conductive when damp. |
| 88 | What does 2-A:10-B:C mean? | Class A rating 2, Class B rating 10, and Class C means the agent is non-conductive (no number). |
| 89 | How close must a Class K extinguisher be to cooking appliances? | Within 30 ft (9.1 m). |
| 90 | What are the maximum travel distances for Class A and Class D? | 75 ft (22.9 m) for both. |
| 91 | What is the maximum mounting height of a unit up to 18 kg? | Top no higher than 1.53 m (5 ft). |
| 92 | What does PASS stand for? | Pull, Aim at the base, Squeeze, Sweep. |
| 93 | Give the NFPA 10 inspection intervals. | Monthly visual, annual maintenance, 6-year internal examination, hydrostatic test at 5 or 12 years by agent. |
| 94 | Is a lithium-ion battery fire a Class D fire? | No. Class D is for lithium metal. Lithium-ion is handled under NFPA 855 and manufacturer guidance, and clean agents do not stop thermal runaway. |
| 95 | A 6,000 ft² ordinary-hazard hall allows 1,500 ft² per 2-A unit. How many by area? | 6,000 / 1,500 = 4 extinguishers (travel distance may require more). |
| 96 | Name the ISO 7010 sign categories and colours. | Prohibition (red circle), warning (yellow triangle), mandatory (blue circle), safe condition (green), fire equipment (red square). |
| 97 | What do E001, E007, F001 and F005 show? | Emergency exit (left), assembly point, fire extinguisher, fire alarm call point. |
| 98 | What must a gas system warning sign say? | That the room has a gas system, do not enter when the alarm sounds or the lamp is lit, evacuate on the alarm, and ventilate after discharge. |
| 99 | How long must exit signs stay visible after power fails? | At least 90 minutes. |
| 100 | What signage does a hypoxic room need? | A reduced-oxygen warning, authorised and medically cleared entry only, and an oxygen reading shown outside. |
| 101 | State key NFPA 101 egress rules. | At least two exits, no locked or chained exits, panic hardware where required, clear routes, and access control that releases on alarm. |
| 102 | Which standard governs evacuation plan symbols? | ISO 23601 (with ISO 7010). |
| 103 | Who enforces fire codes? | The authority having jurisdiction (the fire marshal or building authority). |
| 104 | What does the UK Regulatory Reform (Fire Safety) Order 2005 require? | The responsible person must carry out a fire risk assessment and maintain protection. |
| 105 | How are EN 54 detectors and EN 12094 components legally marketed in the EU? | CE marking under the Construction Products Regulation (EU) 305/2011. |
| 106 | Which OSHA rules apply to extinguishers and fixed systems? | 29 CFR 1910.157 (portable extinguishers), 1910.160 (fixed extinguishing systems) and 1910.162 (gaseous agent systems). |
| 107 | Name three regulatory pressures on fire suppression agents. | The Montreal Protocol (halon), the AIM Act and EU F-gas rules (HFCs), and PFAS restrictions. |
| 108 | List five records an inspector expects. | Fire risk assessment, detection and alarm certificates, sprinkler tests, gas system door fan test, extinguisher service tags, drill and training records, hot work permits, change records. |
| 109 | What are the annual tests of a pre-action system and a gas system? | A trip test of the pre-action valve, and a functional test with an enclosure inspection (and door fan test after changes) for the gas system. |
| 110 | Why may an insurer's requirements exceed the code? | The insurer assesses the loss risk independently and can set conditions of cover (for example FM Global Data Sheets), so engage them early. |

---

## Module 13: Physical Security and Safety

*Notes: [13_physical_security_and_safety.md](13_physical_security_and_safety.md). 125 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | What is the difference between physical security and physical safety? | Security stops people who should not be there (or who intend harm) from reaching the equipment. Safety protects people who are there legitimately, and the facility, from accidents and hazards. |
| 2 | Why does physical access defeat cyber defences? | An attacker with the hardware can read data, management-controller credentials and keys in memory, or remove and analyse the equipment offline. |
| 3 | Name five physical security threats to a data centre. | Any five of: theft, intrusion, insider threat, tailgating and social engineering, vandalism or sabotage, hostile vehicle, terrorism or espionage, drones, supply chain tampering. |
| 4 | What does EN 50600-2-5 require before the protection level is chosen? | A documented risk analysis. |
| 5 | Write the basic risk formula. | Risk = likelihood × impact (or severity), assessed for each asset and threat. |
| 6 | What is defence in depth, and what must each layer be? | Several independent controls in sequence so defeating one leaves the others. Each layer must be independently auditable and testable. |
| 7 | What are the four functions of a security layer? | Deter, detect, delay and respond. |
| 8 | What must be true of the delay compared with detection and response? | The delay must last longer than the time to detect, assess and respond. |
| 9 | Detection takes 15 s, assessment 45 s and response 240 s. Delays are fence 120 s, door 90 s, cage 45 s. Do the layers hold? | Time needed = 300 s. Delay = 255 s. They fail by 45 s. |
| 10 | With the same delays, the response is cut to 150 s. What is the margin? | Needed = 15 + 45 + 150 = 210 s. Delay 255 s, so a margin of 45 s. |
| 11 | What is the six walls rule? | A secure room is a barrier on all six surfaces (four walls, floor and ceiling), slab to slab. A partition that stops at a dropped ceiling is not secure. |
| 12 | Why have a low profile and no windows in the data hall? | A low profile does not advertise the target. No windows removes visibility and an attack route. |
| 13 | How many Protection Classes does EN 50600-2-5 define, and what are they assigned to? | Four (1 to 4), assigned to individual spaces, not the whole site. |
| 14 | What is a protection class island? | A space (such as a lobby, staging area or data hall) with its own Protection Class within the site. |
| 15 | For which aspects are Protection Classes set separately? | Unauthorised access, intrusion, fire, internal environmental events and external environmental events. |
| 16 | What are the typical features of a high-security perimeter fence? | About 2.4 m (8 ft) high, anti-climb design (such as 358 mesh or palisade), anti-climb topping, rated for delay. |
| 17 | What does LPS 1175 rate, and what is the caveat? | The time a fence or gate resists forced entry with tools. The certificate applies only to the tested configuration. |
| 18 | Why must a gate match the fence rating? | Otherwise the gate is the weak point of the perimeter. |
| 19 | Name four perimeter intrusion detection technologies. | Fence-mounted vibration sensors, fibre-optic sensors, taut wire, buried cable, radar, thermal cameras. |
| 20 | What does an ASTM F2656 M30 rating mean? | The barrier stops a 15,000 lb (6,800 kg) vehicle at 30 mph (M40 at 40 mph, M50 at 50 mph). |
| 21 | Which classification did ASTM F2656 replace in the US? | The old US State Department K ratings (K4, K8, K12). |
| 22 | How do IWA 14-1 and PAS 68 relate? | IWA 14-1 is the international standard combining elements of ASTM F2656 and PAS 68. PAS 68 (UK) is largely superseded by IWA 14-1 and ISO 22343. |
| 23 | What is a vehicle dynamics assessment for, and how does it guide M30 or M50? | It analyses approach routes, speed and angle to set the barrier rating. M30 suits constrained speed, M50 suits long straight approaches. |
| 24 | What replaced CPNI in the UK, and in what year? | NPSA (the National Protective Security Authority), in 2023. |
| 25 | What are EN 50131 grades, and which are typical for data centres? | Intruder alarm grades 1 to 4 by risk. Data centres typically use Grade 3 or 4. |
| 26 | What is video verification of an alarm for? | An operator confirms what triggered it before a response is sent, cutting false alarms. |
| 27 | What is the most common gap in an otherwise well-built security system? | Visitor, vendor and contractor access. |
| 28 | Give three visitor controls. | Pre-registration and ID check, distinct expiring badges, escort at all times in secure areas. |
| 29 | Where do deliveries go, and why? | To the loading dock and staging room outside the data hall, so unpacking and inspection happen away from the white space. |
| 30 | How often should asset inventory be reconciled with the racks? | At least annually, with drive serial numbers recorded. |
| 31 | When should a leaver's access be revoked? | The same day. |
| 32 | What does NIST SP 800-88 cover? | Media sanitisation: wiping or destroying drives before reuse or disposal. |
| 33 | How many controls are in ISO/IEC 27001:2022 Annex A.7, and which is new? | 14 physical controls. A.7.4 Physical security monitoring is new in 2022. |
| 34 | What are the NIS2 key dates? | In force 16 January 2023, with a national transposition deadline of 17 October 2024. |
| 35 | Why do security systems need backup power? | So security keeps working in a power failure, and a power cut does not open or disable everything. |
| 36 | What is CPTED? | Crime prevention through environmental design: natural surveillance, clear sight lines, controlled access routes, lighting and landscaping that does not hide intruders. |
| 37 | What is the two-person rule? | Critical actions or access to the most sensitive areas need two people. |
| 38 | Name four purposes of a video surveillance system. | Deter, detect and verify, record evidence, direct the response, audit access, monitor safety. |
| 39 | Match camera types to uses: thermal, PTZ, dome. | Thermal for perimeter at night, fog and glare. PTZ for tracking and large areas. Vandal-resistant dome (IK10) for indoor rooms and corridors. |
| 40 | What does an IK10 rating mean? | The highest impact resistance rating (vandal resistance), tested to IEC 62262. |
| 41 | List the seven pixel density levels of IEC 62676-4:2025. | Overview 20, Outline 40, Discern 80, Perceive 125, Characterise 250, Validate 500, Scrutinise 1,500 px/m. |
| 42 | What are the older DORI levels? | Detect 25, Observe 62.5, Recognise 125 and Identify 250 px/m. |
| 43 | How many pixels across a 16 cm face at 250 px/m? | 0.16 × 250 = 40 pixels. |
| 44 | At what scene width does a 4 MP camera (2,688 pixels) reach 250 px/m? | 2,688 / 250 = 10.75 m. |
| 45 | At what scene width does it reach 125 px/m? | 2,688 / 125 = 21.5 m. |
| 46 | At what scene width does a 1080p camera (1,920 pixels) reach 250 px/m? | 1,920 / 250 = 7.7 m. |
| 47 | A 4K camera has 3,840 pixels. What is its identification scene width, and how does it compare with 1080p? | 3,840 / 250 = 15.4 m, twice the width of 1080p, although 4K has four times the pixels. |
| 48 | How far must a 4 MP camera with a 90° horizontal field of view be to identify (10.75 m scene width)? | d = W / (2 × tan 45°) = 10.75 / 2 = about 5.4 m. |
| 49 | What is the distance for the same camera with a 60° lens? | d = 10.75 / (2 × tan 30°) = 10.75 / 1.155 = about 9.3 m. |
| 50 | Why is 250 px/m a floor and not a target? | Backlight, motion blur, focus, angle to the face, compression and poor light all cost detail, so plan above it. |
| 51 | What is wide dynamic range (WDR) for? | Backlit scenes such as doors with bright light behind the person. |
| 52 | What is the storage per camera per day at 6 Mbps? | 6 × 10.8 = 64.8 GB. |
| 53 | How much storage for 50 cameras at 4 Mbps for 60 days? | 43.2 GB × 50 × 60 = 129,600 GB = 129.6 TB. |
| 54 | What is the network load of 80 cameras at 5 Mbps? | 80 × 5 = 400 Mbps. |
| 55 | How does H.265 compare with H.264? | About half the bitrate for the same quality. |
| 56 | What retention is typical for CCTV? | 30 to 90 days. Some regimes such as PCI DSS commonly call for 90 days or more. |
| 57 | List four GDPR measures for CCTV. | Lawful basis, a DPIA, signs, proportionate documented retention, restricted viewing and export, no audio, subject access handling. |
| 58 | Why is audio recording usually avoided? | It is often unlawful and raises further privacy issues. |
| 59 | Name four cybersecurity measures for the video system. | Unique strong passwords, patched and signed firmware, network segmentation and 802.1X, HTTPS, disable unused services, no open vendor remote access. |
| 60 | What does NDAA Section 889 do? | In the US it bars certain manufacturers' video equipment from federal procurement. |
| 61 | Why synchronise time with NTP? | So footage and access control logs agree to the second as evidence. |
| 62 | Give two ways video is used in alarm-driven monitoring. | An alarm brings up the nearest camera for verification, and a door event is tied to a clip. |
| 63 | Where must cameras cover in a data hall? | Both ends of each row, cage fronts, mantraps and doors, with overlapping fields of view. |
| 64 | Name three common CCTV mistakes. | Cameras bought without an operational requirement, storage too small for the retention promised, backlit entrances, time not synchronised, default passwords, blind spots, nobody watching. |
| 65 | What gives a video system resilience? | Failover recorders, edge (SD) storage in cameras, redundant switches, UPS and generator power. |
| 66 | What are the five functions of entry control? | Identify and authenticate, authorise, enforce, record, alarm. |
| 67 | Give the component chain of an access control system. | Credential, reader, controller, lock, with door contact, request-to-exit, power and management software. |
| 68 | Why should the controller decide locally? | Doors keep working if the network or server fails. |
| 69 | Name the three authentication factors with examples. | Have (card, phone), know (PIN), are (fingerprint, iris, face). |
| 70 | Why are 125 kHz proximity cards weak? | The fixed number is unencrypted and can be cloned in seconds with a copier costing about $30. |
| 71 | Why is MIFARE Classic unsuitable for new systems? | Its Crypto-1 cipher is broken and the card can be cloned with free tools. |
| 72 | Name strong card credentials and their protection. | MIFARE DESFire EV2/EV3, HID Seos and iCLASS SE, using AES-128 mutual authentication. |
| 73 | Why is a card's UID not a credential? | It can be read without authentication and replayed. The credential must be in an AES-protected application. |
| 74 | What is the main attack on mobile credentials and the defence? | Relay attacks. Platforms limit BLE range (about 1 to 5 m) and require the phone to be unlocked. |
| 75 | Define FAR, FRR and CER. | False accept rate (wrong person admitted), false reject rate (right person refused), and the crossover error rate where they are equal. |
| 76 | A reader has a 0.5% FRR and 1,200 entries a day. How many false rejects? | 1,200 × 0.005 = 6 per day. |
| 77 | Why are biometrics sensitive under GDPR? | They are special category data, needing explicit consent or another valid basis, secure templates and a non-biometric alternative. |
| 78 | Compare Wiegand and OSDP. | Wiegand is a one-way, unencrypted link. OSDP is bidirectional, supervised and supports AES-128 Secure Channel. |
| 79 | What makes OSDP secure? | Secure Channel enabled, a unique key per reader, the reader out of install mode, and the default key not used. |
| 80 | Which standard publishes OSDP internationally? | IEC 60839-11-5:2020. |
| 81 | What is a mantrap? | Two interlocked doors where the second cannot open until the first has closed, admitting one person at a time. |
| 82 | Each mantrap cycle takes 10 s and 90 people enter at shift change. How long is the queue? | 90 × 10 = 900 s = 15 minutes. |
| 83 | What is anti-passback? | A credential cannot enter twice without exiting, which needs in and out readers. |
| 84 | Distinguish tailgating and piggybacking. | Tailgating is following an authorised person through a door without consent. Piggybacking is doing it with their consent. |
| 85 | How do anti-tailgating detectors work? | Sensors (overhead 3D, thermal, optical) count the people through the door and compare with the credential reads. |
| 86 | What is the difference between fail-safe and fail-secure locks, and which goes on escape routes? | Fail-safe releases on power loss or fire alarm (a magnetic lock). Fail-secure stays locked (an electric strike). Escape routes use fail-safe release. |
| 87 | What does the life-safety release of an electric lock on an exit include? | A request-to-exit device, a timed auxiliary push button and a fire alarm interface, approved by the AHJ. |
| 88 | What authentication suits the data hall entry? | Card plus PIN or biometric, through a mantrap. |
| 89 | What makes a visitor badge effective? | It looks different from staff badges, expires automatically and requires an escort. |
| 90 | How should lost credentials and mechanical keys be handled? | Deactivate a credential at once. Control keys with an audited key cabinet, restricted keyways, sealed emergency keys and a lost-key procedure. |
| 91 | How often should access be reviewed, and what is removed? | Regularly, for example quarterly. Orphaned and shared badges are removed. |
| 92 | How long are access logs usually kept, and what are they? | Commonly 30 to 90 days. They are personal data. |
| 93 | What do EN/IEC 60839-11-1 grades cover? | Security grades 1 to 4 for electronic access control systems. |
| 94 | Name three access control system security mistakes. | Controllers on the corporate LAN with factory passwords, shared operator accounts, integrator remote access left open, manual badge administration, cloneable cards. |
| 95 | What rules apply to a mantrap on egress? | A person inside can always leave, it releases on a fire alarm, and there is a separate equipment entrance for large items. |
| 96 | List the hierarchy of controls. | Eliminate, substitute, engineering controls, administrative controls, PPE. |
| 97 | A hazard has severity 5 and likelihood 2. What is the risk score? | 5 × 2 = 10. |
| 98 | Name four steps of establishing an electrically safe work condition. | Identify all sources, interrupt and open the disconnect, visually verify, apply lockout/tagout, test for absence of voltage, ground if required. |
| 99 | Why is lockout/tagout complex in data centres? | Dual feeds, bypass switches and static transfer switches keep circuits live, and batteries and capacitors store energy. |
| 100 | How hot can an arc flash be? | Above 19,000 °C. |
| 101 | Give the NFPA 70E PPE category energies. | Category 1: 4 cal/cm². Category 2: 8. Category 3: 25. Category 4: 40. |
| 102 | What PPE category applies to 6, 30 and 50 cal/cm²? | Category 2, Category 4, and no category (do not work live). |
| 103 | Is cost or lost service a valid reason for energised work? | No. Energised work needs infeasibility or a greater hazard. The remedy is design, such as concurrently maintainable distribution. |
| 104 | Why are battery strings special in electrical safety? | They cannot be switched off: the terminals are always live, so use insulated tools, covered terminals and the manufacturer's procedure. |
| 105 | What hydrogen level is the usual ventilation target in a lead-acid battery room? | Below about 1% by volume, a quarter of the 4% lower flammable limit. |
| 106 | A server weighs 46 kg. What is the lifting index against 23 kg? | 46 / 23 = 2.0, so use a lift or a two-person lift. |
| 107 | Name three controls against rack tipping. | Stabilisers or floor anchoring, load heavy items at the bottom, pull out one device at a time. |
| 108 | State the OSHA, NIOSH and EU noise limits. | OSHA: PEL 90 dBA and action level 85 dBA with a 5 dB exchange. NIOSH: 85 dBA with a 3 dB exchange. EU: action values 80 and 85 dB(A), limit 87 dB(A). |
| 109 | How long is the OSHA allowed exposure at 85, 95 and 100 dBA? | 16 hours, 4 hours and 2 hours. |
| 110 | A worker has 3 h at 95 dBA, 2 h at 85 dBA and 3 h at 70 dBA. What is the noise dose? | 3/4 + 2/16 = 0.875, so 87.5%. |
| 111 | What is the level of four equal 80 dB sources? | 80 + 10 × log₁₀ 4 = 86 dB. |
| 112 | What is the ambient level of 1,000 servers at 62 dBA each? | 62 + 10 × log₁₀ 1,000 = 92 dBA. |
| 113 | Name the elements of a hearing conservation programme. | Noise monitoring, audiometric testing, hearing protection, training and records. |
| 114 | How much does liquid cooling cut hot aisle noise? | About 8 to 15 dB for direct-to-chip and 15 to 25 dB for immersion, but CDUs and pumps are still 70 to 85 dBA. |
| 115 | What protected noise level should hearing protectors target? | About 75 to 85 dB(A), to avoid isolating people from alarms and colleagues. |
| 116 | What is the hot aisle temperature for a 26 °C inlet and a 16 K rise? | 26 + 16 = 42 °C. |
| 117 | Name three heat stress controls. | Limit time in the hot aisle, work-rest cycles, drinking water, acclimatisation, a rest area outside, a buddy system, intact containment. |
| 118 | Name three permit-required confined spaces in a data centre, and the oxygen range for entry. | Under-floor voids, sumps and tower basins (also water vaults and cable chambers). Oxygen between about 19.5% and 23.5%. |
| 119 | What is the rule for looking at fibre optic connectors? | Never look into a fibre or connector that might be live. Use a power meter and filtered inspection scopes. |
| 120 | What resistor does an ESD wrist strap contain, and why? | 1 MΩ, to protect equipment and limit shock current to the wearer. |
| 121 | Name three hazards of liquid cooling. | Hot coolant, pressurised lines, leaks and wet floors, electrical equipment near water. |
| 122 | How should an EPO button be protected? | A cover or guard, an alarm, labelling, and a location away from exits and light switches, because accidental operation is a recognised cause of outages. |
| 123 | How is the conflict between locked doors and escape resolved? | Egress always wins: escape-route locks fail safe, release on the fire alarm and have a mechanical or push-button release. |
| 124 | Which OSHA rules cover hearing conservation, lockout/tagout and confined spaces? | 29 CFR 1910.95, 1910.147 and 1910.146. |
| 125 | Which standard covers occupational health and safety management systems? | ISO 45001. |

---

## Module 14: Auxiliary Systems

*Notes: [14_auxiliary_systems.md](14_auxiliary_systems.md). 125 questions.*

| # | Question | Answer |
| --- | --- | --- |
| 1 | Name five reasons to monitor a data centre. | Any five of: detect faults early, reduce repair time (MTTR), plan capacity, run efficiently (PUE), prove compliance and SLAs, support maintenance, detect security and safety events. |
| 2 | Which cause of impactful outages leads in the Uptime Institute analysis? | Power (54% of operators in the 2025 analysis, with cooling at 13%). |
| 3 | Name six monitoring challenges. | Any six of: many protocols and vendors, silos, data volume, alarm floods, sensor placement and drift, data quality, OT cybersecurity, the monitoring system as a single point of failure, records that drift from reality, unclear ownership, over-design. |
| 4 | Give an example of the silo problem. | The same UPS alarm arrives from the BMS, the EPMS and the DCIM at three priorities to three different lists. |
| 5 | Why do three systems polling one Modbus device cause trouble, and what is the fix? | They time out on each other over the same RS-485 line. One master polls the device and the others read from it over IP. |
| 6 | Why are BMS and EPMS networks a cybersecurity concern? | They are operational technology. A DCIM integration can become a route from the corporate network to plant controllers, so use segmentation (IEC 62443 zones and conduits) and controlled remote access. |
| 7 | How is the monitoring system itself protected from being a single point of failure? | Redundant collectors and servers, protected power, redundant networks, an out-of-band (cellular) alert path and edge buffering. |
| 8 | Why is wrong DCIM data worse than no data? | It creates false confidence, so decisions about capacity and changes are made on incorrect information. |
| 9 | List the seven monitoring domains. | Power, cooling, environment, water and liquids, fire safety and security, network and IT, energy and efficiency. |
| 10 | Where should temperature sensors be placed? | At the IT equipment air inlet (the geometric centre of the intake), not at the cooling unit or the room centre. |
| 11 | How many sensors per rack, and on which racks, according to LBNL guidance on ASHRAE practice? | Three per monitored rack (top, middle, bottom of the inlet), on every rack in dense rows and on every other or every third rack in uniform rows. |
| 12 | A hall has 6 rows of 10 racks. How many inlet sensors if every third rack is monitored (racks 1, 4, 7, 10) with 3 sensors each? | 4 × 6 = 24 racks × 3 = 72 sensors. |
| 13 | How many inlet sensors if every one of the 60 racks is monitored, and how many with rear sensors as well? | 60 × 3 = 180 inlet sensors, and 360 including 3 rear sensors per rack. |
| 14 | Why use dew point rather than relative humidity? | Dew point measures absolute moisture and stays constant as air warms, whereas relative humidity changes with temperature. ASHRAE states the envelope as a dew point range. |
| 15 | What sensor accuracy is recommended? | Temperature ±0.5 °C or better (±0.3 °C near the 18 and 27 °C limits), humidity about ±2 to 3% RH. |
| 16 | How often should humidity sensors be checked? | At least once a year against a reference, because they drift. |
| 17 | State the ASHRAE rate-of-change limits. | 20 °C per hour for most IT equipment (and about 5 °C in any 15 minutes), and 5 °C per hour for tape. |
| 18 | Temperature rises from 24 °C to 29 °C in 4 minutes. What is the rate, and when is the 5 °C in 15 minutes limit reached? | 5 / 4 = 1.25 K per minute, so after 4 minutes. |
| 19 | Give typical sampling intervals by purpose. | Seconds for control and critical alarms, 1 to 5 minutes for trending, about 15 minutes for energy and PUE, hourly or daily for capacity. |
| 20 | Why keep at least 13 months of readings? | So a season can be compared with the same season the year before. |
| 21 | 5,000 points are polled every 10 s at 16 bytes per sample. What is the daily sample count and storage? | 500 samples per second = 43.2 million per day, about 691 MB per day. |
| 22 | Which signals must stay hardwired? | Fire suppression release and emergency power off must not depend on a network or monitoring server. |
| 23 | Why synchronise all systems with NTP? | So events from different systems line up in time for diagnosis and evidence. |
| 24 | What is the common mistake of monitoring only at room level? | One ceiling sensor says little about the server inlet, and hot spots form at individual cabinets. |
| 25 | What does EMS mean in your course, and what else can it mean? | Environmental Monitoring System. In much of the literature it means Energy Management System (energy aggregation, ISO 50001). |
| 26 | What does an environmental monitoring system measure? | Temperature, humidity and dew point, airflow, differential pressure, water leaks and door contacts, and similar room conditions. |
| 27 | Does an EMS control equipment? | No. It measures and alarms, and does not control the plant. |
| 28 | What is a BMS and what does it control? | A building management system that controls and monitors the building plant: chillers, pumps, air handlers, CRAH units, lighting, with interfaces to fire and security. |
| 29 | What are the BMS refresh rate and main protocol? | About 1 to 10 seconds, and BACnet. |
| 30 | Which standards define BACnet? | ANSI/ASHRAE 135 and ISO 16484-5. |
| 31 | Give a BMS interlock example. | Gas suppression pre-discharge stops the air handlers and closes the dampers. Also: loss of mains keeps cooling on protected power, or a CRAH fault starts the standby unit. |
| 32 | What is DCIM, and name five of its functions? | Data centre infrastructure management. Functions include asset management, connectivity tracing, capacity planning, monitoring, change management, visualisation, energy and PUE, analytics and integration. |
| 33 | Is DCIM real-time control, and at what level does it work? | No. It refreshes about every 1 to 5 minutes and works at the rack and port level. |
| 34 | What does an EPMS do? | Monitors the electrical path from incomer to PDU (voltage, current, kW, power factor, harmonics, breaker status) with event analysis and branch-circuit monitoring. |
| 35 | What is SCADA in this context? | The supervisory layer that reads controllers and sends commands such as setpoints and sequencing, often performed by the BMS. |
| 36 | Compare the unit of measure of EMS, BMS and DCIM. | EMS: sensors in the space. BMS: building plant. DCIM: assets, racks and capacity. |
| 37 | Name the capacity dimensions DCIM plans. | Power, cooling, space and network (and weight). |
| 38 | 20 racks are allocated 8 kW each but measure 4.5 kW each. What is the stranded capacity? | 160 − 90 = 70 kW. |
| 39 | Headroom is 120 kW power, 90 kW cooling and space for 200 kW. What can be deployed? | The smallest headroom, 90 kW: cooling is the binding constraint. |
| 40 | Name three DCIM pitfalls. | No physical asset survey, records drifting from reality, vendor lock-in or closed data model, weak integration, duplicate metering. |
| 41 | What does DCIM integrate with? | BMS (cooling data), EPMS and EMS (meters), IT systems (CMDB, SNMP, IPMI, Redfish) and ITSM (tickets). |
| 42 | Name six protocols used in data centre monitoring. | BACnet, Modbus, SNMP, LonWorks, OPC UA, MQTT, Redfish and IPMI. |
| 43 | Which protocol is typical for building plant, meters and UPS, and IT devices? | BACnet for building plant, Modbus for meters, UPS and generator controllers, SNMP for IT devices and rack PDUs. |
| 44 | Which system owns which alarm? | The BMS owns mechanical and environmental alarms, the EPMS electrical events and power quality, the DCIM capacity data. |
| 45 | Define PUE and name the standard. | Total facility energy divided by IT equipment energy over the same period (ISO/IEC 30134-2, EN 50600-4-2). |
| 46 | What are the three PUE measurement levels? | Level 1: IT energy at the UPS output. Level 2: at the PDU output. Level 3: at the IT equipment input (rack PDU). |
| 47 | Facility draw is 1,350 kW and UPS output is 900 kW with 3% distribution loss to the servers. What are the Level 1 and Level 3 PUEs? | Level 1: 1,350 / 900 = 1.50. Level 3: IT = 873 kW, PUE = 1.55. |
| 48 | What does a rising PUE with stable IT load indicate? | Degrading cooling or distribution, such as a fouled chiller, a failing pump or poor air distribution. |
| 49 | What does IEC 62443 contribute? | Industrial control system security, with the zones and conduits model that keeps IT and OT networks separated. |
| 50 | Name secure variants of common protocols. | SNMPv3, BACnet/SC and OPC UA security. Modbus has no security of its own, so protect it by network design. |
| 51 | What platforms suit a small site versus a Tier III or IV site? | Small: an EMS, possibly with a simple BMS and basic DCIM. Tier III or IV: BMS + EPMS + DCIM with defined boundaries, plus an EMS or rack sensor network. |
| 52 | Why avoid three overlapping platforms on a small site? | It adds cost and conflicting alarms without benefit. |
| 53 | What do EN 50600-2-6 and ISO/IEC TS 22237-7 cover? | Management and operational information for data centres. |
| 54 | Name five sources of liquid in a data centre. | Chilled water pipes, CRAH condensate pans and pumps, humidifiers, overhead pipework, roof leaks, plant rooms, battery acid, generator fuel, liquid cooling. |
| 55 | Why monitor condensate pans and drains? | A blocked drain quietly overflows the pan, and every CRAH produces condensate. |
| 56 | Why is an overhead leak worse than one below the IT load? | Gravity carries water onto the equipment before it reaches the floor. |
| 57 | When do you use a spot sensor and when sensing cable? | Spot sensors where a leak starts at a known point (drip trays, pans). Cable where water can travel or pool along a route (under floors, along pipes). |
| 58 | What accuracy do location cables offer? | About ±4% of the cable length, or about ±0.4 m per 10 m. |
| 59 | A leak is found 60 m along a location cable. What is the uncertainty? | 0.04 × 60 = ±2.4 m. |
| 60 | Which cable detects diesel, and why not standard cable? | Hydrocarbon cable. Diesel is not conductive, so standard conductive cable will not trigger. |
| 61 | Which cable suits a battery room? | Acid or chemical-resistant cable in a perimeter loop and acid-resistant spot sensors. |
| 62 | What sensors suit dielectric immersion coolants? | Optical or other compatible sensors, because the fluid does not conduct. |
| 63 | Does a water-glycol mixture trigger conductive sensing cable? | Yes, it is conductive. |
| 64 | Where should sensing cable go under a raised floor? | Along the chilled water pipe routes, around the perimeter, beneath cable cutouts, around valves and pumps and across low points, with cross-aisle runs every 4 to 6 m as a starting point. |
| 65 | A 20 m × 30 m hall has a perimeter loop, 6 cross-aisle runs of 20 m, and 40 m along the pipes. What cable length and how many zones? | 100 + 120 + 40 = 260 m, about 3 zones of under 100 m each. |
| 66 | Why use short, labelled zones? | So an alarm points to a place operators can identify quickly, instead of one long zone across several areas. |
| 67 | Where do leak sensors go in a liquid cooled hall? | At every quick-disconnect, manifold junction and supply and return valve, cable loops around CDU bases, rack base sensors, and sensors inside the chassis near cold plate connections. |
| 68 | Describe the leak alarm chain. | Sensor, controller (zone and location), BMS, DCIM and notification, operator verifies and locates, isolates, contains, repairs and records. |
| 69 | Compare automatic and manual isolation. | Automatic closes a valve in seconds but may cut cooling and a false alarm closes a valve. Manual is slower but avoids cutting cooling by mistake. |
| 70 | What should isolation logic consider? | Cooling redundancy, alarm verification, valve feedback, flow and pressure status and the risk of interrupting cooling to active equipment. |
| 71 | How often should leak detection be tested end to end? | At least quarterly, from a wetted sensor to the alarm, location, notification and response. |
| 72 | What does NFPA 75 require that relates to leaks? | The structural floor must allow removal of leaks from cooling water, pipes and sprinkler discharge. |
| 73 | Name three common leak detection mistakes. | Cable in a grid that does not follow the pipes, no condensate monitoring, no overhead protection, one zone for the whole hall, wrong cable for the liquid, untested sensors, no backup power. |
| 74 | How is leak detection connected to the BMS and DCIM? | By relay (dry contact), SNMP or Modbus, so the alarm shows the zone and location. |
| 75 | How do flow and pressure sensors detect leaks? | Indirectly: abnormal flow or a pressure drop in the water loop. |
| 76 | How long do wireless leak sensor batteries last? | Typically 2 to 10 years, depending on the reporting rate. |
| 77 | What is the purpose of a notification system? | To get the right alarm to the right person through a channel that reaches them in time, and close the loop from detection to resolution. |
| 78 | Name the four alarm levels with an example of each. | Information (generator test started), warning (rack inlet 28 °C), major (CRAH fan fault with N+1 intact), critical (UPS on battery, loss of cooling, fire, leak near live equipment). |
| 79 | Where do awareness-only messages belong? | In events and logs, not in the alarm stack. |
| 80 | Name six notification channels and one weakness of e-mail. | On-site sounders, dashboards, e-mail, SMS, voice call, mobile push, SNMP traps, relay outputs, tickets. E-mail can be delayed and missed at 2 a.m. |
| 81 | Why send critical alarms through several channels at once? | No single channel is reliable, so simultaneous SNMP, e-mail, SMS and voice improve the chance it reaches someone. |
| 82 | What is an out-of-band alert path? | A separate path such as a cellular modem that works when the main network or internet is down. |
| 83 | What is a heartbeat test? | A regular test message that proves the notification chain works, with an alarm if it stops. |
| 84 | What should an alarm message contain? | What, where, how severe, when, what to do, and a link to the procedure, without sensitive data in SMS. |
| 85 | Describe an escalation matrix. | Level 1 (NOC) acknowledges within a time, then level 2 (on-call engineer), then level 3 (manager, specialist, vendor), with customers and authorities informed. |
| 86 | Who sets escalation timers? | The site alarm philosophy, after a consequence review. Do not copy another site's times. |
| 87 | State the NIS2 notification timeline for significant incidents. | Early warning within 24 hours, incident notification within 72 hours, final report within one month. |
| 88 | Polling every 60 s, notification 30 s and an on-call answer after 5 minutes. What is the time to human response? | 60 + 30 + 300 = 390 s = 6.5 minutes, before travel. |
| 89 | How does ISA-18.2 define an alarm? | A signal that needs a timely response to avoid or reduce a consequence. With no defined action and no time to act, it is information. |
| 90 | Give the three tests of alarm rationalisation. | A real consequence if ignored, a defined operator action, and enough time to act. |
| 91 | What does the master alarm database record? | For each alarm: cause, consequence, operator response, setpoint, priority and time available. |
| 92 | What is the steady-state alarm benchmark per operator? | About 1 per 10 minutes (6 per hour, 144 to 150 per day). ISA-18.2 treats 2 per 10 minutes (12 per hour) as the most manageable. |
| 93 | Define an alarm flood and when it ends under EEMUA 191. | More than 10 new alarms in 10 minutes on one console. It ends when a 10-minute period has fewer than 5 new alarms. |
| 94 | What share of time should a system spend in flood? | Under 1%. |
| 95 | What priority distribution is the benchmark, and what does it give for 200 alarms? | About 80% low, 15% medium, 5% high: 160, 30 and 10. |
| 96 | Alarm counts per 10-minute block are 2, 3, 12, 25, 7. What is the time in flood? | Two blocks over 10, so 20 of 50 minutes, 40%. |
| 97 | A UPS-on-battery event produces 120 alarms in 3 minutes. How do you handle it? | Group the alarms and use first-out so the operator sees about 3 root-cause alarms (utility failure, UPS state, generator start) and the rest stay in the log. |
| 98 | An alarm at 27.0 °C chatters with a sensor oscillating between 26.9 and 27.1 °C every 20 s. How many alarms per hour, and the fix? | 3 per minute = 180 per hour. A deadband (for example clearing at 26.0 °C) and an on-delay remove the repeats. |
| 99 | Define deadband and on-delay. | Deadband: the value must move back by a margin before the alarm clears. On-delay: the condition must persist for a set time before the alarm activates. |
| 100 | Distinguish shelved, suppressed-by-design and out-of-service alarms. | Shelved: time-limited, operator-controlled suppression. Suppressed by design: automatic, state-based hiding. Out of service: formally disabled with management approval. |
| 101 | What is a first-out alarm? | The first alarm in a cascade, which points to the root cause. |
| 102 | Which standard governs alarm presentation on the operator display? | ISA-101. |
| 103 | What happened at Milford Haven in 1994? | Two operators faced 275 alarms in the last 11 minutes before an explosion, almost all irrelevant to the fault. |
| 104 | What is IEC 62682? | The international version of ANSI/ISA-18.2 alarm management. |
| 105 | Name three notification mistakes. | Alarm floods without grouping, awareness messages in the alarm list, one channel only, an unattended mailbox, no escalation, untested paths, no owner. |
| 106 | What should be monitored on a generator? | Fuel level and quality, oil level and pressure, coolant level and temperature, start battery voltage and charger, run status, load, output voltage, current and frequency, vibration, exhaust temperature, run hours and test results. |
| 107 | What should be monitored on a UPS? | Load, input and output voltage, battery status, charge, remaining runtime and time on battery, temperature, bypass state, alarms. |
| 108 | What battery data is monitored, and why trend it? | Cell voltage, temperature and internal resistance or impedance. Trending against a baseline reveals weakening cells before they fail. |
| 109 | Why monitor PDUs per phase and rack PDUs per outlet? | Per phase catches imbalance and overloaded phases that a total hides. Per outlet supports colocation billing and detailed capacity. |
| 110 | Chilled water flow is 30 L/s, supply 7 °C and return 13 °C. What cooling is delivered, and the capacity factor against 800 kW? | 30 × 4.186 × 6 = about 754 kW, 94%. |
| 111 | A chiller's approach temperature rises from 3 K to 5 K. What does it mean? | A 67% increase, indicating fouled evaporator tubes: schedule cleaning. |
| 112 | Name chiller monitoring points. | Status and alarms, compressor current, evaporator and condenser pressures, supply and return water temperature, approach temperature, kW per ton, refrigerant leak detection. |
| 113 | Name pump monitoring points. | Status, flow, differential pressure, vibration, bearing temperature and drive speed. |
| 114 | Name CRAH monitoring points. | Supply and return temperature, fan speed, valve position, filter differential pressure, condensate pump, humidifier and alarms. |
| 115 | Name liquid cooling monitoring points. | CDU supply and return temperature, flow, differential pressure, coolant quality and conductivity, filter differential pressure, pressure and leak sensors. |
| 116 | Give four examples of monitoring the health of protection systems. | Gas lockout valve position, disabled detector zones, camera offline, controller offline, sprinkler valve tamper, ASD airflow fault. |
| 117 | Compare time-based, condition-based and predictive maintenance. | Time-based: fixed interval. Condition-based: service when a measured parameter crosses a threshold. Predictive: trends forecast failure so work is planned before it. |
| 118 | What UPS battery indicator triggers action? | Cell impedance up about 20% from baseline: run a capacity test. |
| 119 | A 1,500 kW generator burns 0.26 L/kWh with a 20,000 L tank. What are the consumption and autonomy? | 390 L/h and 20,000 / 390 = about 51 hours. |
| 120 | When should the low-fuel alarm fire if set at 50%, and what is the remaining time? | At 10,000 L, which is about 26 hours (10,000 / 390), above the 12-hour Uptime minimum. |
| 121 | A 32 A PDU shows 28 A, 15 A and 12 A. What is the imbalance and the 80% limit? | Average 18.3 A, imbalance 53%. The 80% limit is 25.6 A, so L1 at 28 A is over the limit. |
| 122 | Why alarm on stale or missing data? | A sensor that stops reporting looks like normal, so silence must itself be an alarm. |
| 123 | Name five monitoring KPIs. | PUE, availability, MTTR, capacity margin, mean time to acknowledge and resolve, alarm KPIs, rack inlet compliance, planned versus unplanned maintenance. |
| 124 | Why run generator test runs under load? | They check start reliability and performance, and avoid problems such as wet stacking from light running. |
| 125 | Which standards support maintenance and testing of power equipment? | NFPA 70B (maintenance and thermography), IEEE 450 and 1188 (batteries), ISO 8528 and NFPA 110 (generators). |

---
