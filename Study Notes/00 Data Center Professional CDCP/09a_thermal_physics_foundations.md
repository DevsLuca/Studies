# CDCP Study Notes: Thermal Physics Foundations

*As of 2026-11-19*

This is the thermal companion to `06a_electrical_physics_foundations.md`. It explains the physics behind Module 9 (cooling) in plain steps: what heat is, why a flow of air or water can carry it away, and where the cooling formulas come from. If a formula in `09_cooling_infrastructure.md` looks like magic, the explanation is here.

**The one idea behind everything:** electricity goes in, **heat** comes out, and a **moving fluid** (air or water) carries that heat to the outdoors. The cooling system is a heat-moving system, and the physics is about **how much fluid has to move**.

---

## 1. Heat, power and temperature are three different things

| Quantity | What it is | Unit | Everyday picture |
| --- | --- | --- | --- |
| **Heat (energy)** | An amount of thermal energy | joule (J), kilojoule (kJ), kWh | The amount of water in a bucket |
| **Heat flow (power)** | Energy **per second** | watt (W), kW (**1 kW = 1 kJ/s**) | How fast the bucket is being filled |
| **Temperature** | How hot something is | °C or kelvin (K) | The water level mark |

- A server drawing **1 kW** produces **1 kJ of heat every second**. That is a **rate**, so it is measured in **kW**, not kWh.
- A **temperature difference (ΔT)** in kelvin is the same number as in °C: a rise from 25 °C to 37 °C is a rise of **12 K**.
- **Conversions:** 1 kW = 3,412 BTU/h. 1 ton of refrigeration = 3.517 kW = 12,000 BTU/h.

---

## 2. Specific heat: how much energy it takes to warm something

The **specific heat capacity (c)** is the energy needed to raise **1 kg** of a substance by **1 K**.

| Substance | c (kJ/kg·K) | Density (kg/m³) | Heat per m³ per K (ρ × c, kJ/m³·K) |
| --- | --- | --- | --- |
| **Air** (about 20 °C, sea level) | **1.005** | **1.2** | **1.206** |
| **Water** | **4.186** | **1,000** | **4,186** |

The energy to warm a mass **m** by **ΔT**:

```
Energy (kJ) = m × c × ΔT
```

**Example.** Warming **1 kg of water by 1 K** takes **4.186 kJ**. Warming **1 kg of air by 1 K** takes only **1.005 kJ**. Water holds about **4 times more heat per kilogram**, and, because it is **830 times denser**, about **3,500 times more per cubic metre**:

```
4,186 / 1.206 = about 3,471
```

---

## 3. From energy to power: the equation Q = ṁ × c × ΔT

This is the equation behind almost all of Module 9. Here it is built step by step.

**The idea:** think of each kilogram of air as a **delivery truck**. When it passes through a server and warms by ΔT, each kilogram carries away

```
c × ΔT kilojoules
```

The server makes heat at a rate **Q** (kJ per second). To carry it all away, enough kilograms must pass through **every second**. That is the **mass flow ṁ** (kg/s):

```
Q (kJ/s) = ṁ (kg/s) × c (kJ/kg·K) × ΔT (K)
```

Since **1 kJ/s = 1 kW**, Q is in kW. Rearranged: **ṁ = Q / (c × ΔT)**.

### Worked example: 1 kW of air at a 10 K rise

| Step | Calculation | Result |
| --- | --- | --- |
| 1. Heat carried by each kg of air | 1.005 kJ/kg·K × 10 K | **10.05 kJ per kg** |
| 2. Kilograms needed each second to carry 1 kJ/s | 1 / 10.05 | **0.0995 kg/s** |
| 3. Convert mass to volume (air is 1.2 kg/m³) | 0.0995 / 1.2 | **0.0829 m³/s** |
| 4. Convert to m³/h | × 3,600 | **299 m³/h** |
| 5. Convert to CFM (1 m³/s = 2,118.88 CFM) | 0.0829 × 2,118.88 | **about 176 CFM** |

Steps 2 and 3 together give the airflow formula used in the notes:

```
Airflow (m³/s) = Q / (1.2 × 1.005 × ΔT) = Q / (1.206 × ΔT)
```

### Where the constant 1.206 comes from, and the same equation in three unit systems

The airflow formula looks as if it has a mysterious number in it. It doesn't. Here is how to read it slowly.

**Step 1: the constant is the heat carried by one cubic metre of air.**

```
density × specific heat = 1.2 kg/m³ × 1.005 kJ/kg·K = 1.206 kJ/m³·K
```

Read the units: **1.206 kJ per cubic metre per kelvin** means that **each cubic metre of air carries 1.206 kJ of heat for every degree it warms**. If the air warms by 10 K, each cubic metre carries 12.06 kJ. The airflow formula simply asks how many cubic metres per second are needed to carry the heat:

```
Airflow (m³/s) = heat (kJ/s) / (1.206 kJ/m³·K × ΔT)
```

**Step 2: where 1.2 and 1.005 come from.** They are **properties of standard air** (about 20 °C at sea level), taken from property tables such as the ASHRAE Fundamentals Handbook. They are not design choices. Different conditions give different values (see the altitude example in section 4).

**Step 3: the same equation in three "costumes".** Engineers in different regions use different units, so the constant looks different. It is the same physics.

| Unit system | Equation | Where the constant comes from |
| --- | --- | --- |
| **SI** (kW, m³/s, K) | **Q = 1.206 × V̇ × ΔT** | 1.2 kg/m³ × 1.005 kJ/kg·K |
| **Common in Europe** (W, m³/h, K) | **Q = 0.335 × V̇ × ΔT** (often rounded to 0.33) | 1.206 × 1,000 W per kW ÷ 3,600 s per hour = 0.335 |
| **US** (BTU/h, CFM, °F) | **Q = 1.08 × CFM × ΔT** | 60 min per hour × 0.075 lb/ft³ × 0.24 BTU/lb·°F = 1.08 |

Check the US constant: air density 0.075 lb/ft³ is the same as 1.2 kg/m³, and 0.24 BTU/lb·°F is the same as 1.005 kJ/kg·K. The 60 converts "per minute" (CFM) into "per hour" (BTU/h).

**Step 4: the US formula in kilowatts.** Since **1 kW = 3,412 BTU/h**:

```
CFM = 3,412 × kW / (1.08 × ΔT in °F) = 3,160 × kW / ΔT (°F)
```

**Step 5: converting the temperature rise.** A temperature **difference** converts at **1 K = 1.8 °F**, so **10 K = 18 °F**, and 12 K = 21.6 °F. **Do not add 32**: that is only for converting an actual temperature (25 °C = 77 °F), never a difference.

**The same server three ways (1 kW, 10 K rise):**

| Version | Calculation | Result |
| --- | --- | --- |
| SI | 1 / (1.206 × 10) | 0.083 m³/s |
| m³/h | 1,000 W / (0.335 × 10) | 298.5 m³/h |
| US | 3,160 × 1 / 18 | 175.6 CFM |

They are the same airflow: 0.083 m³/s = 299 m³/h = 176 CFM.

**Is 176 CFM per kW a rule?** No. It is a **worked example**. The formula is fixed (for standard air), but the airflow per kW **depends on ΔT**, which is set by the equipment (table below). A "rule of thumb" such as **120 to 160 CFM per kW** is just this formula with an assumed ΔT:

```
160 CFM per kW → ΔT = 3,160 / 160 = 19.75 °F = about 11 K
120 CFM per kW → ΔT = 3,160 / 120 = 26.3 °F  = about 14.6 K
```

When you see a rule of thumb, ask **which ΔT it assumes**. In practice use the manufacturer's data sheet, and in an exam use the ΔT the question gives.

### What ΔT is, and why it matters so much

**ΔT is the temperature rise of the air as it passes through the servers** (exhaust minus inlet). It is **not** the room temperature. A server that heats the air more needs **less air** for the same power, because each kilogram carries more heat:

| ΔT across the servers | Airflow per kW (m³/s) | Airflow per kW (CFM) |
| --- | --- | --- |
| 5 K | 0.166 | 351 |
| 10 K | 0.083 | 176 |
| 12 K | 0.069 | 146 |
| 15 K | 0.055 | 117 |
| 20 K | 0.041 | 88 |

Doubling ΔT **halves** the airflow. Servers vary their fan speed to hold a target temperature, so a lightly loaded server moves less air and a hot one moves more.

### The 10 kW rack at a 12 K rise (the check question)

```
Airflow = 10 / (1.206 × 12) = 0.69 m³/s = about 2,490 m³/h = about 1,460 CFM
```

---

## 4. Mass flow, volume flow and why density matters

The equation needs **mass** flow (kg/s), but fans move **volume** (m³/s). Density links the two:

```
mass flow = density × volume flow
```

Air density changes with **temperature** (warm air is lighter) and with **altitude** (thinner air is lighter). A fan moves the same volume at altitude, but each cubic metre carries **less mass**, and so **less heat**.

**Worked example: altitude.** Standard atmospheric pressure at **1,500 m** is about **84.6 kPa**, against 101.3 kPa at sea level. For air at 20 °C (density = pressure / (287 × temperature in K)):

```
Sea level: 101,325 / (287 × 293.15) = 1.20 kg/m³
1,500 m:   84,560  / (287 × 293.15) = 1.00 kg/m³
Extra volume needed = 1.20 / 1.00 = about 20% more airflow for the same cooling
```

This is one reason ASHRAE **derates the allowable temperature** above 900 m, and why cooling equipment is **derated at altitude** **[CHECK]**.

---

## 5. Air versus water: why liquid takes over

For the same heat, compare the **volume** that must flow:

```
Volume flow = Q / (ρ × c × ΔT)
```

**Worked example: a 120 kW rack.**

| Fluid | Calculation | Flow |
| --- | --- | --- |
| **Air**, ΔT 12 K | 120 / (1.206 × 12) | **8.29 m³/s** (29,850 m³/h, about 17,570 CFM) |
| **Water**, ΔT 10 K | 120 / (4.186 × 10) = 2.87 kg/s | **0.00287 m³/s** (172 L/min, 10.3 m³/h) |

The air volume is **about 2,900 times larger**. Moving that much air through a rack means a hurricane of airflow, large ducts and large fans.

### Fan power versus pump power

The power needed to move a fluid is:

```
Power = volume flow × pressure rise / efficiency
```

Take illustrative values: the air fan works against **500 Pa** and the pump against **200 kPa**, both at 60% efficiency:

```
Air fan:   8.29 m³/s × 500 Pa / 0.6     = 6,908 W (about 6.9 kW)
Water pump: 0.00287 m³/s × 200,000 Pa / 0.6 = 956 W (about 1.0 kW)
```

Even though the pump works against a **400 times higher pressure**, it moves so much less volume that it needs about **7 times less power**. This is part of why liquid cooling saves energy.

---

## 6. Heat transfer from the chip to the fluid

Heat reaches the air or liquid by three routes:

| Mode | How | Where it matters |
| --- | --- | --- |
| **Conduction** | Through solids (chip, heat sink, cold plate), q = k × A × ΔT / L | Inside the server |
| **Convection** | Moving fluid carries heat from a surface, q = h × A × ΔT | Almost all data centre cooling |
| **Radiation** | Electromagnetic emission, grows with T⁴ | Negligible at data centre temperatures |

### Thermal resistance: the key concept for chips

The temperature step between the chip and the fluid is:

```
ΔT = P × R_th        (P = chip power in W, R_th = thermal resistance in K/W)
```

| Chip | Power | R_th | Chip temperature above the local coolant |
| --- | --- | --- | --- |
| CPU with an air heat sink | 300 W | 0.15 K/W | 300 × 0.15 = **45 K** |
| Accelerator | 1,000 W | 0.15 K/W | 1,000 × 0.15 = **150 K** (far too hot) |
| Accelerator with a cold plate | 1,000 W | 0.05 K/W | 1,000 × 0.05 = **50 K** |

A **1,000 W** chip needs a thermal resistance **three times lower** than an air heat sink can give. A **cold plate with flowing water** achieves it, because water transfers heat from a surface far better than air. This is the physics reason liquid cooling is needed as chip power rises.

The chain of temperatures from the room to the silicon:

```
Chip junction = inlet air + air heating inside the server + heat sink step (P × R_th) + ...
```

So a **higher inlet temperature** leaves **less margin** at the chip, which is why dense, hot chips can **require cooler inlet or coolant temperatures** (ASHRAE class H1, and the liquid S classes).

---

## 7. Sensible heat, latent heat, moisture and dew point

| Term | Meaning | Example |
| --- | --- | --- |
| **Sensible heat** | Heat that changes **temperature** | Warming air from 20 to 32 °C |
| **Latent heat** | Heat absorbed or released when **water changes state** (evaporates or condenses), with **no temperature change** | A cold coil condensing water out of the air |

**Latent heat of vaporisation of water:** about **2,450 kJ/kg** at room temperature. Evaporating (or condensing) **1 kg** of water moves as much heat as warming about **585 kg of water by 1 K**, or **2,440 kg of air by 1 K**. It is a big energy transfer.

**Worked example.** A cooling coil condenses **1 g/s** of moisture:

```
Latent load = 0.001 kg/s × 2,450 kJ/kg = 2.45 kW
```

That 2.45 kW does **nothing** to cool the servers: it is wasted capacity. This is the physics behind the **sensible heat ratio**:

```
SHR = sensible cooling / total cooling
```

A comfort unit with SHR 0.65 spends **35%** of its capacity on moisture, which a data hall doesn't need. A precision unit has an SHR of about 0.9 to 1.0.

### Dew point

The **dew point** is the temperature at which air becomes **saturated** (100% relative humidity). Any surface **colder than the dew point** gets covered in condensation.

- **Relative humidity** changes with temperature even when the amount of moisture is constant. The **dew point measures the moisture itself**, which is why ASHRAE uses it.
- **Cold surfaces sweat:** chilled-water pipes, rear doors, cold plates and CDU piping must be kept **above the room dew point** (guidance commonly asks for about 2 °C margin), or be **insulated**.
- Warming air **without adding moisture** lowers its relative humidity but doesn't change the dew point.

---

## 8. The refrigeration cycle: moving heat uphill

Heat flows **naturally from hot to cold**. A cooling system must move heat from the **cool hall** to the **warmer outdoors**, which means working **against** the natural direction. That takes **work**, supplied by the compressor.

**Why the cycle works:** a refrigerant's **boiling point depends on its pressure**. At low pressure it boils at a low temperature (below the room temperature), so it can **absorb heat while it boils** in the evaporator. After the compressor raises its pressure, it condenses at a high temperature (above the outdoor temperature), so it can **give the heat away** in the condenser.

```
Heat rejected = heat absorbed + compressor work
COP = heat absorbed / compressor work
```

### The limit: Carnot

No machine can beat:

```
COP_max = T_cold / (T_hot − T_cold)       (temperatures in kelvin)
```

| Evaporator | Condenser | COP_max |
| --- | --- | --- |
| 10 °C (283 K) | 40 °C (313 K) | 283 / 30 = **9.4** |
| 15 °C (288 K) | 40 °C (313 K) | 288 / 25 = **11.5** |
| 15 °C (288 K) | 25 °C (298 K) | 288 / 10 = **28.8** |

The smaller the **temperature lift**, the better the COP. This is why **warmer chilled water, warmer air and cooler outdoor air** all improve efficiency, and why **free cooling** (no compressor at all) is so attractive. Real machines reach about **50 to 60%** of the Carnot limit.

---

## 9. Fans and pumps: the affinity laws

For a fan or pump running at different speeds (and a fixed system):

| Quantity | Varies with speed as |
| --- | --- |
| **Flow** | speed |
| **Pressure** | speed² |
| **Power** | **speed³** |

**Worked example.** A fan slows to **80%** speed:

```
Flow     = 80% of the original
Pressure = 0.8² = 64%
Power    = 0.8³ = 51.2%   (a 20% cut in airflow saves about 49% of fan power)
```

This is why **containment** (which lets airflow fall), **EC variable-speed fans** and **variable-speed pumps** save so much energy, and why **bypass air** (moving air that does no cooling) is so wasteful.

---

## 10. Evaporative cooling: where water use comes from

When water **evaporates**, it absorbs its latent heat from the surroundings. This cools the air or the water, down towards the **wet-bulb temperature**.

**Worked example: the ideal water use of evaporative heat rejection.**

```
Latent heat       = 2,450 kJ/kg
Water per kWh of heat = 3,600 kJ / 2,450 kJ/kg = about 1.47 kg = about 1.5 litres per kWh of heat rejected
```

So rejecting **1 MW** of heat purely by evaporation boils off:

```
1,000 kW / 2,450 kJ/kg = 0.41 kg/s = about 1,470 litres per hour
```

This is the **minimum**: real towers also lose water to blow-down and drift. It explains why **evaporative and adiabatic** cooling raise **WUE**, and why **dry coolers** (which reject heat with air only) use almost no water but need cooler outdoor conditions.

---

## 11. Storing thermal energy

Energy stored in a body of water, warmed or cooled by ΔT:

```
E (kJ) = m × c × ΔT       and       1 kWh = 3,600 kJ
```

| Case | Calculation | Result |
| --- | --- | --- |
| **1 m³ of water, 8 K difference** | 1,000 × 4.186 × 8 = 33,488 kJ | **9.3 kWh per m³** |
| **Chilled-water tank for 1 MW, 10 minutes, 6 K** | 1,000 kW × 600 s = 600,000 kJ. Volume = 600,000 / (4.186 × 6 × 1,000) | **about 24 m³** |
| **Ice (melting)** | 1 kg of ice absorbs **334 kJ** as latent heat | About **10 times more per kg** than warming water by 8 K (33.5 kJ/kg) |

Seasonal storage (Module 9, lesson 9.16) uses the same equation, scaled up: water in an aquifer or the ground, warmed or cooled by a few kelvin, over hundreds of thousands of cubic metres.

---

## 12. Putting it together: one chain for a 1 MW hall

| Step | Calculation | Result |
| --- | --- | --- |
| IT load = heat | | **1,000 kW** |
| Air through the servers (ΔT 12 K) | 1,000 / (1.206 × 12) | **69.1 m³/s** (248,700 m³/h, about 146,400 CFM) |
| Chilled water to the CRAHs (ΔT 6 K) | 1,000 / (4.186 × 6) | **39.8 kg/s** (about 143 m³/h) |
| Chiller electricity (COP 5) | 1,000 / 5 | **200 kW** |
| Heat rejected outdoors | 1,000 + 200 | **1,200 kW** |
| If rejected by evaporation alone | 1,200 / 2,450 | **0.49 kg/s** (about 1,760 litres per hour) |

---

## 13. Exam cheat sheet

| Topic | Key point or formula |
| --- | --- |
| **Heat vs. power** | 1 kW = 1 kJ/s. Heat is energy, kW is a rate |
| **Heat equation** | **Q = ṁ × c × ΔT** (kW = kg/s × kJ/kg·K × K) |
| **Airflow** | **V̇ (m³/s) = Q / (1.206 × ΔT)** |
| **Air per kW at 10 K** | 0.083 m³/s (299 m³/h, about 176 CFM) |
| **Same equation, other units** | W = 0.335 × m³/h × ΔT(K). **BTU/h = 1.08 × CFM × ΔT(°F)**. **CFM = 3,160 × kW / ΔT(°F)** |
| **Where 1.206 comes from** | 1.2 kg/m³ × 1.005 kJ/kg·K: one m³ of air carries 1.206 kJ per kelvin |
| **Where 1.08 comes from** | 60 × 0.075 lb/ft³ × 0.24 BTU/lb·°F |
| **ΔT conversion** | 1 K = 1.8 °F for a **difference** (10 K = 18 °F). Never add 32 |
| **Airflow per kW** | Not a fixed ratio: it depends on ΔT. 120 to 160 CFM/kW assumes about 11 to 15 K |
| **Water flow** | ṁ (kg/s) = Q / (4.186 × ΔT) |
| **Air vs. water** | Water carries about **3,500 times** more heat per volume |
| **ΔT** | Temperature rise **across the servers**. Larger ΔT, less airflow |
| **Altitude** | Thinner air carries less heat per m³: about 20% more airflow at 1,500 m |
| **Thermal resistance** | ΔT = P × R_th. High-power chips need low R_th (cold plates) |
| **Latent heat** | About 2,450 kJ/kg of water. Moisture removal wastes cooling capacity |
| **SHR** | Sensible ÷ total. About 0.9 to 1.0 for precision cooling |
| **Dew point** | Surfaces below it sweat. Keep cold surfaces about 2 °C above it |
| **COP** | Cooling ÷ work. Carnot: T_cold / (T_hot − T_cold) |
| **Condenser heat** | Cooling + compressor work |
| **Affinity laws** | Flow ∝ speed, pressure ∝ speed², **power ∝ speed³** |
| **Evaporative water** | About 1.5 L per kWh of heat rejected (minimum) |
| **Stored energy** | E = m c ΔT. 1 m³ of water, 8 K = 9.3 kWh |

---

## 14. Practice questions with answers

The practice questions for this file are in [00_knowledge_tests.md](00_knowledge_tests.md#thermal-physics-foundations-companion-file-09a).

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| Standard thermodynamics and fluid mechanics | Specific heat, Q = ṁ c ΔT, thermal resistance, Carnot COP, latent heat, affinity laws |
| **ASHRAE Handbook: Fundamentals** | Properties of air and water (density, specific heat), psychrometrics, dew point |
| **ISO 2533 / standard atmosphere** | Air pressure and density at altitude |
| **ASHRAE TC 9.9 Thermal Guidelines (5th edition, 2021)** | Dew point as the humidity metric, altitude derating, ASHRAE classes |

The data centre applications of these formulas are developed, with their references, in `09_cooling_infrastructure.md`.
