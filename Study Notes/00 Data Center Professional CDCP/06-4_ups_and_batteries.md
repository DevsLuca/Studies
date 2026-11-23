# Module 6, Part D: UPS Systems, Batteries and Inspection (lessons 6.36 to 6.47)

Detailed notes, following the lesson-level index of the EPI course. This is the last of four Module 6 files (see `06-1`, `06-2` and `06-3`).

| Lesson | Title | Section |
| --- | --- | --- |
| 6.36 | UPS Technologies | [Section 1](#636-ups-technologies) |
| 6.37 | Static UPS | [Section 2](#637-static-ups) |
| 6.38 | Static UPS Operating Modes | [Section 3](#638-static-ups-operating-modes) |
| 6.39 | Static UPS Quick Comparison Table | [Section 4](#639-static-ups-quick-comparison-table) |
| 6.40 | Energy-Friendly UPS | [Section 5](#640-energy-friendly-ups) |
| 6.41 | Modular UPS | [Section 6](#641-modular-ups) |
| 6.42 | UPS Increased Availability | [Section 7](#642-ups-increased-availability) |
| 6.43 | Dynamic UPS | [Section 8](#643-dynamic-ups) |
| 6.44 | Batteries for UPS Systems | [Section 9](#644-batteries-for-ups-systems) |
| 6.45 | Battery Testing | [Section 10](#645-battery-testing) |
| 6.46 | Battery Energy Storage System (BESS) | [Section 11](#646-battery-energy-storage-system-bess) |
| 6.47 | Thermographic Scanning | [Section 12](#647-thermographic-scanning) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#part-d-lessons-636-to-647) |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Battery, BESS and fire-code rules change quickly (NFPA 855 has a 2026 edition), so confirm the edition your authority adopts.
>
> Related material: the three UPS types (VFD, VI, VFI) and the rectifier and inverter explanation are summarised in 6.36 to 6.39 below. Harmonics, power factor and sizing are in `06-3`. Redundancy configurations (parallel, catcher, 2N) are in `06-1` (6.12).

---

# 6.36 UPS technologies

## 1. What a UPS does

An **uninterruptible power supply (UPS)** keeps a critical load running **without a break** when the utility fails or drifts outside its limits, and (depending on type) also **conditions** the supply (voltage, frequency, noise). It stores energy for the gap until the generator takes over, or until an orderly shutdown.

## 2. The two families

| Family | Energy store | Converters | Notes |
| --- | --- | --- | --- |
| **Static UPS** | **Batteries** (or sometimes supercapacitors or a flywheel) | **Electronic** (rectifier, inverter): no moving parts in the power path | The standard choice in most data centres |
| **Rotary / dynamic UPS** | **Flywheel** (kinetic energy), often with a diesel engine | **Motor-generator** set: rotating machines | Used on larger sites, covered in 6.43 |
| **Hybrid** | Mix, for example a static UPS with a flywheel ahead of the batteries | | Flywheel absorbs short disturbances, reducing battery cycling |

## 3. Why a battery needs DC and an inverter

Batteries only store and deliver **DC**. The load needs **AC**. So the UPS needs a **rectifier** (AC to DC, to charge the battery and feed the DC link) and an **inverter** (DC to AC, to supply the load).

## 4. IEC 62040-3 classification

IEC 62040-3 describes a UPS by its **output performance**, not by old marketing names ("online", "offline"). The code has **three parts**:

```
   VFI  -  SS  -  11
    │       │      └── dynamic output performance (classes 1 to 3, 1 is the tightest)
    │       └───────── output waveform: normal mode / stored-energy mode (S, X or Y)
    └───────────────── input dependency: VFI, VI or VFD
```

| Part | Meaning |
| --- | --- |
| **Input dependency** | **VFI**: voltage and frequency **independent** (output rebuilt by the inverter). **VI**: voltage independent (voltage regulated, frequency follows the mains). **VFD**: voltage and frequency **dependent** (output follows the mains) |
| **Waveform** | Two letters, for normal mode and battery mode. **S** = sinusoidal, **X** = sinusoidal only with linear load, **Y** = non-sinusoidal (square or stepped). So **SS** is a clean sine wave in both modes |
| **Dynamic performance** | Digits that grade the output voltage during **mode changes** and **load steps**. **1** is the most demanding, **3** the most permissive. Two digits are used (**11** is the tightest class) |

**Common combinations:** **VFI-SS-11** (double-conversion, in its on-line normal mode), **VI-SS-31** (line-interactive), **VFD-SY-33** (offline / standby).

**Important:** a UPS with several normal modes has a **different classification in each mode**. For example, a double-conversion UPS may be **VFI** in its on-line mode but **VFD** in its high-efficiency (eco) mode. Always ask for the full code **for each mode**.

## 5. The three static topologies (normal operation)

**VFD (offline / passive standby):** the load runs from the mains. The inverter is off, and the transfer switch moves the load to the inverter on failure. A few milliseconds of gap.

```
                                    ┌────────────┐
 Mains ──────────┬──────────────────┤  Transfer  ├──────► Load
 (AC)            │                  │   switch   │
                 │                  └─────▲──────┘
                 ▼                        │ switches here
           ┌───────────┐            ┌─────┴──────┐
           │  Charger  │            │  Inverter  │
           └─────┬─────┘            │  (idle)    │
                 ▼                  └─────▲──────┘
           ┌───────────┐                  │
           │  Battery  ├──────────────────┘
           └───────────┘
```

**VI (line-interactive):** the load runs from the mains through a **voltage regulator**. The inverter/charger is connected at the output and takes over on failure.

```
            ┌───────────────────┐
 Mains ─────┤  Voltage          ├──────┬─────► Load
 (AC)       │  regulation (AVR) │      │
            └───────────────────┘      │
                           ┌───────────┴───────────┐
                           │ Inverter / charger    │
                           │ (works both ways)     │
                           └───────────┬───────────┘
                                  ┌────┴────┐
                                  │ Battery │
                                  └─────────┘
```

**VFI (online double conversion):** the load is **always** fed through the rectifier and inverter, with a static bypass for overload and faults.

```
                 ┌───────────┐    ┌────────┐    ┌───────────┐     ┌──────────┐
 Mains ──┬──────►│ Rectifier ├───►│ DC bus ├───►│ Inverter  ├────►│  Static  ├───► Load
 (AC)    │       │ AC → DC   │    │        │    │ DC → AC   │     │  switch  │
         │       └───────────┘    └───┬────┘    └───────────┘     └────┴─────┘
         │                       ┌────┴────┐                           │
         │                       │ Battery │                           │
         │                       └─────────┘                           │
         └────────── static bypass: overload, fault, service ──────────┘
```

## 6. Technology choices inside a static UPS

| Choice | Options and notes |
| --- | --- |
| **Rectifier** | **6-pulse thyristor** (THDi about 30% or more, needs filters), **12-pulse** (about 8 to 12%), **IGBT active front end** (typically under 3 to 5%, input PF 0.99 or better) **[CHECK]**. See `06-3`, 6.31 |
| **Inverter** | **IGBT**-based, using pulse-width modulation. Two-level or **three-level** designs (three-level is more efficient) **[CHECK]** |
| **Transformer** | **Transformer-based** (galvanic isolation, robust, bulky, lower efficiency, roughly 88 to 92%) vs. **transformerless** (smaller, lighter, higher efficiency, roughly 96 to 99%, no isolation) **[CHECK]** |
| **DC link and energy store** | Lead-acid or lithium-ion batteries, supercapacitors or a flywheel |
| **Static bypass** | A solid-state switch to the mains for overload, fault or service |
| **Maintenance bypass** | A manual switch (internal or external) so the UPS can be serviced while the load stays powered |
| **Control and communications** | Monitoring, SNMP, Modbus, dry contacts, remote shutdown |

## 7. Standards **[CHECK]**

| Standard | Topic |
| --- | --- |
| **IEC 62040-1** | Safety |
| **IEC 62040-2** | EMC |
| **IEC 62040-3** | Performance and test requirements (classification, efficiency, dynamic performance) |
| **UL 1778 (US)** | UPS safety |
| **IEC 62040-4** | Environmental aspects |

---

# 6.37 Static UPS

## 1. The double-conversion UPS in detail

```
 Mains ──[Input CB]──► Rectifier ──► DC bus ──► Inverter ──► [Output CB] ──► Load
                           │           │
                        Charger     Battery (via battery breaker)
 Bypass source ──[Bypass CB]──► Static bypass switch ─────────────────────┘
 Maintenance bypass: [MBB] links input directly to output for servicing
```

| Block | Function |
| --- | --- |
| **Input breaker / switch** | Isolates the UPS from the mains |
| **Rectifier** | Converts AC to DC and feeds the DC bus. Also charges the battery |
| **DC bus** | The common point. The battery attaches here |
| **Battery and battery breaker** | Store energy. The breaker protects and isolates the string |
| **Inverter** | Converts DC to a clean, regulated AC output |
| **Static bypass switch** | Moves the load to the bypass source in milliseconds (overload, fault, inverter failure) |
| **Maintenance (manual) bypass** | Allows service without dropping the load. Often a **make-before-break** switch |
| **Output breaker** | Isolates the UPS output |
| **Controls and display** | Monitoring, alarms, event log |
| **Input filter** | May reduce input harmonics |

## 2. Key ratings

| Rating | Meaning |
| --- | --- |
| **Rated power (kVA and kW)** | Size both. **kW = kVA × output PF**. Modern UPS often have PF 1.0 |
| **Input and output voltage, frequency** | For example 400 V, 50 Hz |
| **Overload capability** | The load it can carry briefly (for example 110% for 10 minutes, 125% for 1 minute, 150% for 10 seconds, vendor-specific) **[CHECK]** |
| **Short-circuit capability** | The fault current the inverter can supply to clear a downstream fault |
| **Efficiency** | At 25%, 50%, 75% and 100% load (IEC 62040-3 defines the test) |
| **Input power factor and THDi** | Affect generator and cable sizing |
| **Battery autonomy** | Runtime at rated load, typically 5 to 15 minutes **[CHECK]** |
| **Crest factor, load step response** | Ability to handle server inrush and sudden loads |

## 3. Advantages and limits of the static UPS

| Advantages | Limits |
| --- | --- |
| No moving parts in the power path, fast (zero transfer in on-line mode) | Needs **batteries**, with a limited life and a maintenance cost |
| Modular, scalable, widely available | **Heat losses** (efficiency below 100%) |
| Good efficiency at moderate load, easy to monitor | Battery runtime is limited |
| Fits N+1, 2N and distributed redundancy | Harmonics at the input unless a low-THDi design is used |
| Small footprint | Needs a battery room and cooling |

---

# 6.38 Static UPS operating modes

A double-conversion UPS moves between several **operating modes**. Know the **power path** in each.

| Mode | Load supplied by | What is active | When |
| --- | --- | --- | --- |
| **Normal (on-line)** | **Inverter** | Rectifier powers the inverter and charges the battery. Inverter on | Mains healthy |
| **Stored-energy (battery) mode** | **Inverter**, from the battery | Rectifier off. Battery feeds the DC bus. **No interruption** | Mains fails or goes out of tolerance |
| **Recharge** | Inverter | Mains returns. Rectifier takes over and recharges the battery | After a discharge |
| **Static bypass** | **Bypass source** (mains) | Inverter off or idle. Rectifier only charges the battery | Overload, short-circuit on the output, inverter fault, temperature fault |
| **Maintenance (manual) bypass** | **Mains, directly** | UPS can be switched off and serviced | Planned maintenance |
| **High-efficiency (eco) mode** | **Bypass source**, with the inverter on standby | Static bypass carries the load. Inverter ready to take over | Stable mains and tolerant loads |
| **Frequency converter mode** | Inverter | Output at a different frequency from the input (for example 50 to 60 Hz), no bypass or battery needed | Special applications |
| **Generator mode** | Inverter | Input current limited, rectifier **walk-in** (gradual start) | Running on generator after a mains failure |

```
          mains fails                    mains returns
 Normal ───────────────► Battery ─────────────────────► Recharge ──► Normal
   │                                                        
   │  overload / fault                    overload cleared
   └────────────────► Static bypass ◄─────────────────────┘ (retransfer)
```

## 1. Details of each mode

**Normal mode.** The rectifier takes AC from the mains and supplies the DC bus and the battery charger. The inverter builds a **fresh sine wave** for the load. The output is independent of mains voltage and frequency (VFI).

**Battery mode.** The rectifier stops getting input, so the **battery supplies the DC bus**. The inverter never stops, so the load sees **no interruption**. The UPS monitors the battery voltage and signals when autonomy is running out, so loads can shut down in an orderly way. It shuts the inverter off at the **end-of-discharge voltage** to protect the battery.

**Recharge and generator operation.** When the mains (or the generator) returns, the rectifier **ramps up gradually (walk-in or soft start)** so the generator isn't hit by a sudden step. The **recharge current is limited** so that the battery and the generator are not overloaded. If the UPS is on a generator, input current limiting stops the UPS rectifier from overloading the set.

**Static bypass mode.** If the inverter is overloaded or fails, the load transfers to the bypass source through the **static switch** in a few milliseconds. For a **clean transfer** the inverter should be **synchronised** with the bypass source (same frequency and phase). If it isn't, the UPS may delay or refuse the transfer, or transfer with a break.

| Bypass transfer | Detail |
| --- | --- |
| **Inverter to bypass (automatic)** | Overload beyond the rating, fault, over-temperature, inverter failure |
| **Bypass to inverter (retransfer)** | Automatic when the cause has cleared, if synchronised |
| **Risk** | The load is exposed to **raw mains** while on bypass, with no conditioning and no battery protection (unless the mains is good) |

**Maintenance bypass.** Closing the maintenance bypass connects the load straight to the mains so the UPS can be **isolated and worked on**. While in this mode, the **load has no UPS protection**. It must be a **make-before-break** operation, done by procedure, because a mistake drops the load.

**High-efficiency (eco) mode.** The static bypass carries the load, and the inverter waits. Efficiency can reach about **99%**, but there is a **small transfer gap** (a few milliseconds, sometimes longer) when the mains fails or degrades, and the UPS's **classification falls to VFD** in this mode. It is only suitable where the mains is stable and the loads tolerate the gap (see 6.40).

## 2. Operator checks **[CHECK]**

- Monitor **battery state**, **bypass availability** (the bypass source must be within tolerance), and **load level** (stay below the overload threshold).
- A UPS in static bypass is **not protecting the load**, so investigate promptly.
- Test the transfer and battery modes **under controlled conditions**, with procedures and a rollback plan.

---

# 6.39 Static UPS quick comparison table

## 1. The three types side by side

| | **VFD (offline / passive standby)** | **VI (line-interactive)** | **VFI (online double conversion)** |
| --- | --- | --- | --- |
| **IEC code (typical)** | VFD-SY-33 | VI-SS-31 | VFI-SS-11 |
| **Normal-mode path** | Mains straight to the load | Mains through a voltage regulator | Always through the rectifier and inverter |
| **Inverter in normal mode** | Off | Standby (charges battery) | **Always on** |
| **Transfer on mains failure** | A few ms | A few ms | **Zero** |
| **Voltage regulation** | None | Yes (tap-changing AVR) | **Full** |
| **Frequency independent of mains** | No | No | **Yes** |
| **Waveform on battery** | Often stepped or square | Often sine (or stepped in cheaper units) | **Pure sine** |
| **Isolation from mains problems** | Poor | Moderate | **Complete** |
| **Efficiency (typical) [CHECK]** | About 98% or more | About 96 to 98% | About 94 to 97% (up to 99% in eco mode) |
| **Cost** | Lowest | Medium | Highest |
| **Battery stress** | Used on every outage | Used on outages (and some deep sags) | Used only on real outages |
| **Typical power range [CHECK]** | Small (up to about 2 kVA) | Small to medium (up to about 5 to 10 kVA) | **All sizes, data centres from 10 kVA to MW** |
| **Typical use** | PCs and home equipment | Small servers, network closets | **Data centres, critical loads** |
| **Generator-friendly** | Poor | Moderate | **Best** (with controls) |

## 2. Protection against disturbances **[CHECK]**

| Disturbance | VFD | VI | VFI |
| --- | --- | --- | --- |
| **Power failure** | Yes (after a short gap) | Yes (after a short gap) | **Yes, no gap** |
| **Voltage sag / undervoltage** | Only by going to battery | **Yes** (regulator) | **Yes** |
| **Voltage swell / overvoltage** | Limited | **Yes** (regulator) | **Yes** |
| **Surges and transients** | Surge filter only | Surge filter and regulator | **Yes** (isolated) |
| **Line noise** | Limited | Partly | **Yes** |
| **Frequency variation** | No | No | **Yes** |
| **Voltage harmonics (distortion)** | No | No | **Yes** (output rebuilt) |
| **Switching spikes** | Limited | Partly | **Yes** |

## 3. Choosing

| Need | Choice |
| --- | --- |
| Data centre, critical IT load, generator backup | **VFI** |
| Small server room, network closet, moderate quality supply | VI |
| Non-critical, low-cost, tolerant loads | VFD |
| Energy saving on tolerant loads with a stable supply | A VFI unit in **eco mode**, with the risks understood |

---

# 6.40 Energy-friendly UPS

## 1. Why efficiency matters

All UPS losses become **heat**. That costs energy twice: the electricity lost in the UPS and the cooling to remove it. It also raises **PUE**.

```
Losses = input power − output power = P_out × (1/η − 1)
```

### Worked example 1: the cost of 2% efficiency

A **1,000 kW** load:

| UPS efficiency | Input power | Losses |
| --- | --- | --- |
| 96% | 1,000 / 0.96 = 1,041.7 kW | **41.7 kW** |
| 94% | 1,000 / 0.94 = 1,063.8 kW | **63.8 kW** |

```
Difference = 22.1 kW   ×   8,760 h = about 194,000 kWh per year
At €0.12 per kWh = about €23,300 per year (plus the cooling needed to remove that heat)
```

### Worked example 2: eco mode

At **99%**, the losses for 1,000 kW are 1,000 / 0.99 − 1,000 = **10.1 kW**. Compared with 96% (41.7 kW) that saves **31.6 kW**, or about **277,000 kWh a year**.

A published example: a **5 kW** loss, running all year at 0.15 per kWh, costs 5 × 8,760 × 0.15 = **6,570 per year**, or about 65,700 over 10 years.

## 2. Where efficiency is gained

| Measure | How it helps |
| --- | --- |
| **Transformerless design** | No transformer losses |
| **IGBT rectifier and three-level inverter** | Lower switching losses |
| **Right-sizing** | UPS efficiency is lowest at light load. Best at about **30 to 80%** load **[CHECK]**, with a practical target of about 50 to 70% |
| **Modular UPS with intelligent module management (6.41)** | Idle modules switch off so the active ones run at high load |
| **High-efficiency (eco) mode** | Up to about 99%, at the cost of the transfer gap and a lower IEC class |
| **Lithium-ion batteries** | No need for the cool battery room that lead-acid requires |
| **Low-loss cabling and short runs** | Less I²R loss |
| **Dynamic UPS energy-storage optimisation** | Reduces the energy held in the flywheel to what is needed (6.43) |
| **Efficiency standards** | **ENERGY STAR for UPS** sets efficiency limits across the load range for larger transformerless units (for example around 95% or more at 25 to 100% load) **[CHECK]**. IEC 62040-3 defines how efficiency is measured |

## 3. Efficiency curve (illustrative)

| Load | Typical efficiency of a modern double-conversion UPS **[CHECK]** |
| --- | --- |
| 25% | about 94 to 95% |
| 50% | about 96 to 97% |
| 75% | about 96.5 to 97.5% |
| 100% | about 96 to 97% |

Redundant designs (2N, N+1) keep each UPS at **lower load**, which **lowers efficiency**, which is why modular designs with intelligent module management are attractive.

## 4. Eco mode: the trade-off

| Benefit | Risk |
| --- | --- |
| Efficiency up to about 99% | A **transfer gap** (a few ms, and sometimes up to about 15 ms in some units) when the mains degrades |
| Lower heat and PUE | **Less protection**: raw mains reaches the load (surges, noise, frequency variation). The classification falls to VFD |
| | A fast-failing mains can fall outside the ITIC envelope before the UPS reacts |

**Where it fits:** stable mains, tolerant loads (non-critical IT, lighting), and **quiet** periods. Many sites **decide eco mode in writing**, with the risk acknowledged.

---

# 6.41 Modular UPS

## 1. What it is

A **modular UPS** is built from **hot-swappable power modules** (each a complete rectifier, inverter and charger) in a **frame** with a shared busbar, static bypass, control and communications. Capacity is changed by adding or removing modules.

```
 ┌──────────────────────── UPS frame ────────────────────────┐
 │  Module 1  Module 2  Module 3 ... Module n  (e.g. 20 kW)  │
 │  ───────────────── shared busbar ─────────────────        │
 │  Static bypass     Control / display     Communications   │
 └──────────────────────────┬────────────────────────────────┘
                         Battery cabinets
```

| Item | Typical **[CHECK]** |
| --- | --- |
| **Module size** | About 10 to 50 kW (some larger) |
| **Frame size** | From about 50 kW to over 200 kW, with several frames paralleled up to over 1 MW |
| **Redundancy** | **N+1** (or N+2) inside one frame |
| **Replacement** | Hot-swap, without dropping the load. Often live-swap designs with limited arc-flash energy |

## 2. Advantages

| Advantage | Explanation |
| --- | --- |
| **Scalability (pay as you grow)** | Start with the capacity needed now and add modules as the load grows. No big up-front oversizing |
| **Right-sizing and efficiency** | The system runs at higher loading across its range, and unused modules can sleep |
| **Low MTTR** | A failed module is swapped in minutes (often under 10 to 30 minutes), instead of a long repair. Modest skills needed |
| **N+1 in a single frame** | Redundancy built in |
| **Footprint** | Smaller than an equivalent monolithic UPS |
| **Lower initial capital** | Less to buy on day one |
| **Easier spares** | A few modules cover many failures |

## 3. Limits

| Limit | Explanation |
| --- | --- |
| **Shared frame components** | The busbar, static bypass and controls are common to all modules, so they can be single points of failure. Some designs use a **distributed bypass** (each module has its own) |
| **Proprietary** | Modules fit only the maker's frames |
| **Firmware compatibility** | Mixed firmware can stop modules paralleling |
| **Scale** | Very large sites may still prefer large units, or many frames in parallel |
| **A longer MTTR negates the benefit** | If swapping needs a technician for hours, the redundancy advantage is lost |

## 4. Monolithic vs. modular

| | Monolithic | Modular |
| --- | --- | --- |
| **Capacity change** | Replace or add a whole unit | Add or remove modules |
| **Sizing** | Often oversized for growth, running at low load | Matched to the load |
| **Efficiency at low load** | Lower | Higher (module sleep) |
| **Repair** | Often needs bypass or an outage window | **Hot-swap**, short MTTR |
| **Redundancy** | Add a whole UPS | Add a module |
| **Footprint** | Larger | Smaller |
| **Failure impact** | A major fault sends the whole unit to bypass | One module lost, the rest carry on (if N+1) |

## 5. Worked examples

**Sizing with modules.** A load of **160 kW**, with **20 kW** modules:

```
N   = 160 / 20 = 8 modules
N+1 = 9 modules   →  each normally carries 160 / 9 = 17.8 kW (89%)
N+2 = 10 modules  →  each normally carries 16 kW (80%)
```

**Efficiency through module sleeping.** The load falls to **80 kW** in a frame with 9 modules:

```
All 9 active:   each 80 / 9 = 8.9 kW  →  44% loaded  (lower efficiency)
Intelligent management: N = 80 / 20 = 4, plus 1 = 5 modules active
                each 80 / 5 = 16 kW  →  80% loaded   (higher efficiency)
```

The **idle modules stay in standby** and wake up if the load rises or a module fails.

---

# 6.42 UPS increased availability

## 1. How UPS availability is increased

| Approach | Detail |
| --- | --- |
| **Parallel redundant (N+1)** | Several UPS modules or units share the load on a common bus. One can fail with no impact |
| **Isolated redundant (catcher)** | A reserve UPS takes over a failed main system |
| **Distributed redundant (3 to make 2)** | Three systems, each load fed from two |
| **System plus system (2N)** | Two completely independent UPS systems feeding dual-corded loads |
| **Dual-input UPS** | Separate feeds to the **rectifier** and the **bypass**, so a fault on one supply doesn't stop both |
| **Distributed (per-unit) static bypass** | Each UPS has its own bypass, so a common bypass is not a single point of failure |
| **Redundant battery strings** | Several strings in parallel (for example N+1 strings), or **separate batteries for each UPS**, so one weak string doesn't remove the runtime |
| **Battery monitoring** | Early warning of weak cells (6.45) |
| **Maintenance bypass** | Allows service without a shutdown |
| **Modular design and hot-swap (6.41)** | Cuts MTTR |
| **Good maintenance and testing** | Preventive maintenance, regular tests of transfer and batteries |
| **Remote monitoring and spares** | Faster response |
| **Well-designed generator interface** | Rectifier walk-in, input limiting, compatible alternator |

(Details of the configurations are in `06-1`, 6.12.)

## 2. Availability calculations

**Parallel redundancy.** Each UPS unit is **99.9%** available. Two units in parallel (1+1):

```
Availability = 1 − (0.001)² = 99.9999%
```

**N+1 with 2 of 3 needed:**

```
A = 3A² − 2A³ = 3 × 0.998001 − 2 × 0.997003 = 99.9997%
```

**But the common parts limit it.** If the parallel arrangement also has a **common output bus and switchgear** with **99.99%** availability, in series:

```
Total = 0.9999 × 0.999999 = 0.999899 → about 99.99%
```

The system is limited by the **common bus**, not by the redundant UPS units. That is why designs add **distributed bypass**, **2N**, or independent paths.

## 3. Weak points to watch

- The **common output bus and bypass** of a parallel system.
- A **single battery string** or shared battery breaker.
- **Maintenance bypass** operations (human error during switching).
- A **common control or communications** failure.
- **Dependence on one input feed**.
- **Overloading** one UPS after another fails.

**Operational factors** matter as much as design: procedures, training, change control and testing (6.22 in `06-2`).

---

# 6.43 Dynamic UPS

## 1. What it is

A **dynamic (rotary) UPS** stores energy as **kinetic energy in a spinning flywheel** instead of in batteries. A **diesel rotary UPS (DRUPS)** combines the flywheel, a motor-generator and a diesel engine in one system.

```
 Mains ─► [Choke] ─► Synchronous machine ─► Output ─► Load
                      (motor / generator)
                            │ same shaft
                         Flywheel ──[clutch]── Diesel engine (stopped)
```

| Part | Role |
| --- | --- |
| **Synchronous machine (motor-generator)** | Runs as a **motor** on the mains to keep the flywheel spinning, and as a **generator** on failure |
| **Flywheel (kinetic energy store)** | A heavy rotating mass whose energy bridges the gap |
| **Choke / coupling** | Filters and decouples the load from the mains (a **rotating filter** that smooths harmonics and disturbances) |
| **Clutch** | Connects the **diesel engine** to the shaft to bring it up to speed |
| **Diesel engine** | Takes over for long outages |

## 2. How it works

| State | What happens |
| --- | --- |
| **Normal** | Mains drives the machine as a motor, keeping the flywheel at speed. The load is fed with conditioned power. The diesel is stopped |
| **Mains fails** | The **flywheel's kinetic energy drives the machine as a generator**, so the load sees no break. The diesel is started and clutched in (**ride-through**, commonly about **8 to 15 seconds**, up to 30 seconds or more in some designs) **[CHECK]** |
| **Diesel running** | The diesel carries the load for hours or days |
| **Mains returns** | The load is re-synchronised to the mains, the diesel stops |

Optional modes: **energy-storage optimisation (ESO)** reduces flywheel energy to what is needed, and **diesel start delay (DSD)** avoids starting the diesel for very short mains dips.

## 3. How much energy is in the flywheel?

**Energy = power × time.** For a **1 MW** load and **10 seconds**:

```
E = 1,000 kW × 10 s = 10,000 kJ = 2.78 kWh
```

A **10-minute battery** for the same load holds **1,000 × 10/60 = 167 kWh**, about **60 times** more energy. A flywheel bridges **seconds**, a battery bridges **minutes**, which is why a DRUPS relies on its diesel starting reliably.

## 4. Comparison with a static UPS **[CHECK]**

| | **Static UPS (batteries)** | **Dynamic / diesel rotary UPS** |
| --- | --- | --- |
| **Energy store** | Batteries (minutes) | Flywheel (seconds) |
| **Batteries** | Yes (replacement, room, fire risk) | **None** |
| **Power electronics in path** | Rectifier and inverter | None in the main path (rotating machine) |
| **Efficiency** | About 94 to 97% (double conversion) | Vendors claim up to about 97%. Independent studies show static UPS can be **more efficient at light load** |
| **Footprint** | Larger with batteries | Vendors claim 40 to 60% smaller |
| **Harmonics** | Needs low-THDi front end | The machine and choke act as a rotating filter |
| **Maintenance** | Batteries, fans, capacitors | **Flywheel bearings** (repairs can take a day or more) |
| **Dependence on diesel** | Lower (batteries give minutes) | **Higher**: ride-through is seconds, so the diesel must start |
| **Modularity** | High | Low (large fixed units, typically 250 kVA to 2.5 MVA) |
| **Typical use** | All sizes | **Large sites** where a low-voltage or medium-voltage rotary plant makes sense |

Vendor and independent comparisons **disagree**, so treat efficiency and cost claims with care and check the assumptions (load level, redundancy, battery size, and what is included).

## 5. Static UPS with a flywheel (hybrid)

A **flywheel** can sit **ahead of batteries** in a static UPS, absorbing short disturbances (sags, brief outages) so the **batteries cycle less**, which extends their life.

---

# 6.44 Batteries for UPS systems

## 1. Battery types **[CHECK]**

| Type | Characteristics | Typical real life in a UPS | Notes |
| --- | --- | --- | --- |
| **VRLA (valve-regulated lead-acid)**, AGM or gel | Sealed, maintenance-light, the long-time standard | **About 3 to 8 years**, often sold as "10-year design life" at 25 °C | Hydrogen vents on charge, dry-out failure, temperature-sensitive |
| **Flooded (vented) lead-acid** | Liquid electrolyte, topped up with water | **15 to 20+ years** | Best life, needs a proper battery room, ventilation and maintenance |
| **Nickel-cadmium (NiCd)** | Tolerates heat and abuse | 15 to 20+ years | Costly, toxic cadmium, less common |
| **Lithium-ion (LFP most common)** | Compact, light, long-lived | **About 8 to 15 years** | Needs a BMS, fire-code review (NFPA 855), costs more upfront |

## 2. VRLA vs. lithium-ion **[CHECK]**

| | **VRLA** | **Lithium-ion (LFP)** |
| --- | --- | --- |
| **Upfront cost** | Lower | About 1.5 to 3 times higher |
| **Service life** | About 3 to 6 years real | About 8 to 15 years |
| **Cycle life** | About 200 to 500 | About 1,000 to 4,000+ |
| **Weight and footprint** | Heavy, large | About 60 to 80% lighter, 50 to 70% smaller |
| **Temperature tolerance** | Best at 20 to 25 °C. Life **halves for every 8 to 10 °C above 25 °C** | Tolerates warmer rooms (for example up to about 40 °C, vendor-specific) |
| **Failure mode** | Gradual capacity loss, dry-out | **Thermal runaway** is the serious risk, managed by chemistry (LFP), the BMS and design |
| **Monitoring** | Optional add-on | Integrated BMS with cell-level data |
| **Codes** | Hydrogen ventilation rules | NFPA 855, UL 9540A, UL 1973, IEC 62619 |
| **Total cost over 10 to 15 years** | Several replacements | Often lower, but depends on temperature, quotes and horizon |
| **Service ecosystem** | Everyone can test and replace | More concentrated in OEMs |

**Note:** lithium cabinets are less energy-dense than cell marketing suggests (about 65 to 70 Wh/kg at cabinet level), because of enclosure, controls and cooling.

## 3. Battery arrangement

```
Cell (2 V nominal, lead-acid) → block (e.g. 6 cells = 12 V) → string (blocks in series) → several strings in parallel
```

**Worked example (lead-acid).** A UPS with a **480 V** DC bus:

```
Cells in series = 480 / 2 = 240 cells  (or 40 blocks of 12 V)
End-of-discharge voltage at 1.75 V per cell = 240 × 1.75 = 420 V
Float voltage at about 2.27 V per cell      = 240 × 2.27 = about 545 V
```

The UPS must keep working over the **range from float to end-of-discharge** (about 420 to 545 V here).

## 4. Charging

| Item | Detail |
| --- | --- |
| **Float charge** | A constant voltage (about 2.25 to 2.30 V per cell for lead-acid) that keeps the battery full, with a small current |
| **Temperature compensation** | Float voltage is lowered as the battery gets warmer, to avoid overcharge (commonly a few mV per cell per °C) **[CHECK]** |
| **Recharge current** | Limited, so the generator and battery are not overloaded after a discharge |
| **Ripple** | VRLA needs a charger with low ripple current |
| **Equalising** | Not normally for VRLA unless the maker recommends it |
| **Lithium-ion** | Charged and protected by its BMS, with its own profile |

## 5. Sizing the battery

```
Energy needed = P × t / η_inverter   then multiply by margins (ageing, temperature, design)
```

**Worked example.** A **500 kW** UPS load for **10 minutes**, inverter efficiency **95%**, ageing and design margin **1.25** (illustrative):

```
Energy at the load = 500 × 10/60 = 83.3 kWh
At the battery     = 83.3 / 0.95 = 87.7 kWh
With margin        = 87.7 × 1.25 = about 110 kWh
```

**Current check.** At the end-of-discharge voltage of **420 V**:

```
I = 500,000 / (420 × 0.95) = about 1,253 A
```

Real sizing uses the **manufacturer's discharge tables at the short (10-minute) rate**, because capacity at high rates is **less** than the rated Ah (the Peukert effect), and **end-of-life** (about 80% capacity) must still meet the requirement.

## 6. Autonomy and the generator

| Design choice | Typical **[CHECK]** |
| --- | --- |
| **Standard runtime** | About 5 to 15 minutes at full load. Some AI-oriented designs specify 15 to 30 minutes |
| **Why minutes are enough** | The generator takes about 10 to 15 seconds, and the battery covers the gap plus margin |
| **Longer runtime** | For sites without a generator, or to allow an orderly shutdown |

## 7. Battery room and installation

(See Module 3.5.) Key points: a **dedicated, ventilated room** for lead-acid (hydrogen below 1%), **temperature control** (20 to 25 °C), floor loading, spill containment for flooded cells, **seismic racks**, **DC breakers and protection**, **arc-flash labels**, and for lithium-ion **NFPA 855**, UL 9540A data, off-gas detection and spacing.

## 8. Standards **[CHECK]**

| Standard | Topic |
| --- | --- |
| **IEEE 485** | Sizing lead-acid batteries |
| **IEEE 450** | Vented lead-acid: maintenance, testing, replacement |
| **IEEE 1188** | VRLA: maintenance, testing, replacement |
| **IEEE 1106** | Nickel-cadmium |
| **IEC 60896 series, EN 50272-2** | Stationary lead-acid batteries and their safety |
| **IEC 62485-2** | Safety requirements for stationary batteries |
| **IEC 62619, UL 1973, UL 9540A, NFPA 855** | Lithium-ion batteries and energy storage safety |

---

# 6.45 Battery testing

## 1. Why test

A battery on **float** holds the same voltage whether it is healthy or has **lost 40% of its capacity**. The only way to know what it can deliver is to **measure it**. Most UPS batteries fail **gradually**, so regular testing finds weak cells **before** an outage does.

## 2. Types of tests and checks

| Test | What it tells you |
| --- | --- |
| **Visual inspection** | Leaks, swelling, corrosion, cracks, loose connections, room temperature, ventilation |
| **Float voltage (string and per cell/block)** | Charger setting and cell balance. Cannot prove capacity |
| **Float current and temperature** | Overcharge, thermal problems |
| **Internal ohmic test** (impedance, conductance or resistance of each cell or block) | Quick, online indicator of **weak cells**, trended against a **baseline** |
| **Intercell and terminal connection resistance** | Finds loose or corroded joints |
| **Acceptance test** | Capacity test on a **new** battery to prove it meets the specification, and to set the baseline |
| **Performance test (capacity test)** | A **discharge** at constant current or constant power to the end voltage, to measure actual capacity |
| **Service test** | A discharge that simulates the **real load and duty** for the required time |
| **Modified performance test** | A combination of the above (a discharge to the actual duty, then continued to the rated end voltage) |
| **BMS and monitoring data** | Continuous cell voltage, temperature, impedance, state of health |
| **Thermographic scan** | Hot connections and cells (6.47) |

## 3. Standards **[CHECK]**

| Standard | For |
| --- | --- |
| **IEEE 450** | Vented lead-acid (flooded) batteries |
| **IEEE 1188** | VRLA batteries |
| **IEEE 1106** | Nickel-cadmium batteries |
| **IEC 60896 series** | Stationary lead-acid batteries (test methods) |

## 4. Typical schedule (IEEE 450 and 1188 practice) **[CHECK]**

| Activity | Frequency |
| --- | --- |
| **Visual inspection and string voltage** | Monthly |
| **Per-cell float voltage, temperature, connection checks** | Quarterly |
| **Internal ohmic measurements (VRLA)** | Quarterly (and a baseline about 6 months after installation) |
| **Intercell connection resistance** | Annually |
| **Acceptance test** | At installation (each cell at least about **90%** of rated capacity) |
| **First performance test** | Within about **2 years** (vented) or **1 year** (VRLA not acceptance-tested on site) |
| **Periodic performance tests** | At intervals of **no more than 25% of the expected service life** (often about every 2 years in VRLA practice) |
| **Annual performance tests** | Once the battery shows **degradation** (more than 10% below the previous test, or below 90% of rating), or reaches about **85% of its expected life** |
| **Special inspection** | After any abnormal event (deep discharge, high temperature) |

Utility regulations can add rules. For example, one US reliability standard sets maximum capacity-test intervals of 6 years (vented) and 3 years (VRLA) unless ohmic trending is used, and requires records. The asset owner's specification overrides these where it is stricter.

## 5. Replacement criteria

| Criterion | Value |
| --- | --- |
| **Replace the battery when capacity falls to** | About **80%** of the rated capacity (the "knee" of the ageing curve, after which capacity falls quickly) |
| **Degradation flag** | More than 10% down on the previous test, or below 90% of rating |
| **Ohmic change** | Impedance rise of roughly 30 to 50% (or conductance fall of about 23 to 33%) from baseline is **significant**. Earlier guidance flagged changes over 20%. Investigate and run a capacity test |

**Limits of ohmic testing:** it **flags weak cells** but **does not measure capacity**. There is no direct correlation, especially in the critical 80 to 100% range. It supplements capacity testing and doesn't replace it, unless the owner's programme (and any regulator) accepts it.

## 6. Capacity test: method

1. **Fully charge** the battery (on float for the required time) and record float voltages and temperatures.
2. **Isolate** the battery safely, or use a **redundant** battery or a **load bank** arrangement. Plan so the **load stays protected** during the test.
3. **Discharge** at the specified **constant current or power** (the rated rate) to the **end-of-discharge voltage** (commonly **1.75 V per cell**, sometimes 1.80 V).
4. **Record** cell voltages at intervals and at the end, and note the weakest cells.
5. **Calculate** capacity, **correcting for temperature**:

```
Capacity (%) = (actual discharge time / rated discharge time) × 100
(with the temperature correction factor applied for the average cell temperature)
```

6. **Recharge**, and record results for comparison with the previous test.

### Worked examples

**Capacity.** A battery is rated for **10 minutes** at the test load. It reaches the end voltage after **8 minutes 30 seconds**:

```
Capacity = 8.5 / 10 = 85%
```

It still passes the 80% replacement limit, but it is **below 90%** (a degradation flag), so it moves to **annual** testing and is planned for replacement.

**A failed test.** The same battery lasts **8 minutes**: **80%**, which is at the **replacement threshold**.

**Ohmic trend.** A cell baseline is **4.0 mΩ**. Now it reads **5.4 mΩ**:

```
Change = (5.4 − 4.0) / 4.0 = +35%
```

That is in the **significant** range, so schedule a **capacity test** and watch the string.

## 7. Temperature and life

**Rule of thumb for lead-acid:** battery life **halves for every 8 to 10 °C above 25 °C**.

```
Life(T) = Life(25 °C) × 2^( −(T − 25) / 10 )
10-year design life at 35 °C → 10 × 0.5 = 5 years
10-year design life at 30 °C → 10 × 2^(−0.5) = about 7.1 years
```

## 8. Safety and good practice

- Use **insulated tools**, PPE, and arc-flash controls: a DC battery stays energised.
- **Ventilate** (hydrogen) and keep ignition sources away.
- Run discharge tests only with a **protected load** (redundancy, bypass or a second string).
- **Never open the circuit** on a live string without a procedure.
- **Lithium-ion:** use the **BMS** data (state of health, cell balance), plus periodic capacity checks as the maker specifies.
- Keep **records**: results, temperature, dates, replaced cells. Trend over time.
- Replace **whole strings** where weak cells would drag down new ones, as the maker advises.

---

# 6.46 Battery Energy Storage System (BESS)

## 1. What a BESS is

A **battery energy storage system (BESS)** is a **large installation of batteries with the equipment to charge and discharge them**, connected to the grid or a site, used for energy services as well as backup.

| Part | Function |
| --- | --- |
| **Battery cells and modules** (most often **LFP**) | Store the energy |
| **Racks and containers** | Housing, often a 20-foot container |
| **BMS (battery management system)** | Monitors and protects every cell or module |
| **PCS (power conversion system)** | **Bidirectional inverter**: DC to AC and AC to DC |
| **EMS (energy management system)** | Software that decides **when to charge and discharge**, and enforces the **reserve** |
| **Thermal management** | Air or liquid cooling |
| **Fire detection and suppression** | Gas and smoke detection, suppression, explosion control (NFPA 855) |
| **Switchgear, transformer, protection** | Connection to the site or grid |
| **SCADA and communications** | Monitoring, dispatch, grid operator links |

```
 Grid / site bus ◄──► Transformer ◄──► PCS (bidirectional inverter) ◄──► Battery (LFP) + BMS
                                              ▲
                                             EMS (controls charge and discharge)
```

## 2. Uses in a data centre

| Use | Explanation |
| --- | --- |
| **Backup and ride-through** | Supports load during short outages, may reduce generator starts |
| **Peak shaving** | Discharges at the site's peak to reduce **demand charges** (the highest kW in a billing period) |
| **Time-of-use shifting** | Charges when energy is cheap, discharges when it is expensive |
| **Demand response and grid services** | Paid for reducing load or supporting frequency and voltage |
| **Renewable integration** | Stores surplus solar or wind, smooths variability |
| **Power quality support** | Voltage and frequency support |
| **Faster grid connection** | A BESS can allow a site to connect before a network upgrade |
| **Microgrid role** | Islanding support (6.3 in `06-1`) |

## 3. BESS vs. UPS batteries

| | **UPS battery** | **BESS** |
| --- | --- | --- |
| **Purpose** | Ride through failures for **minutes** | Energy service over **hours**, plus backup |
| **Operation** | **Float** most of its life, rarely cycled | **Regularly cycled** (daily) |
| **Connection** | On the UPS DC bus | On a **medium- or low-voltage AC bus** through a PCS |
| **Size** | Minutes at the UPS rating | **MWh** scale |
| **Protection role** | Zero-break for the IT load | **Not a no-break UPS**: a BESS on the MV bus can't protect every downstream low-voltage fault |

**Do not use ordinary UPS batteries for daily peak shaving:** they are built for float service, and frequent cycling degrades them and can void warranties. A dedicated BESS uses **high-cycle cells**, cooling and controls built for cycling.

**The same stored energy can't be used twice.** If a BESS also provides emergency backup, the EMS must **hold a minimum state of charge** (commonly about 20 to 50%) in **reserve** that routine dispatch may not use.

## 4. Sizing a BESS

| Quantity | Meaning |
| --- | --- |
| **Power (kW or MW)** | The PCS rating: how fast it can charge or discharge |
| **Energy (kWh or MWh)** | The battery capacity |
| **Duration** | **Energy ÷ power** (hours) |
| **C-rate** | Power relative to energy: 1C discharges the full energy in 1 hour, 0.5C in 2 hours |
| **Round-trip efficiency** | Energy out ÷ energy in, typically about 85 to 94% |
| **Depth of discharge and ageing** | Usable energy is less than nameplate and falls over time |

```
Duration = energy / power        e.g. 5 MW / 15 MWh → 3 hours (0.33C)
Nameplate energy needed = usable energy needed / (usable fraction × efficiency × ageing factor)
```

**Worked example.** A site needs **1,000 kWh** delivered. Assume a usable depth of **80%**, efficiency **95%**, and an end-of-life ageing factor of **80%** (illustrative):

```
Nameplate = 1,000 / (0.80 × 0.95 × 0.80) = 1,000 / 0.608 = about 1,645 kWh
```

A **1 MWh** battery can theoretically support a **1 MW** load for about **one hour**, but real projects must allow for efficiency, reserve, usable depth and ageing.

**Example with reserve.** If **100 kWh** must be held back for emergency duty in addition to **100 kWh** for peak shaving, the nameplate is about (100 + 100) / 0.608 = **329 kWh** before other allowances.

## 5. Standards and codes **[CHECK]**

| Standard | Topic |
| --- | --- |
| **UL 9540** | Safety of energy storage systems (product certification) |
| **UL 9540A** | Test method for **thermal runaway fire propagation** (a sixth edition takes effect on 1 January 2027) |
| **UL 1973, IEC 62619** | Batteries for stationary use |
| **NFPA 855** | Installation of stationary energy storage systems. The **2026 edition** requires explosion control (NFPA 69) or a performance-based alternative, and adds a **thermal runaway propagation prevention** category. NFPA 68 venting is no longer accepted as the primary strategy |
| **IEC 62933** | Electrical energy storage systems |
| **IEEE 1547 and 1547.9** | Interconnection of distributed energy resources with the grid, and its application to storage |
| **IEC 61850, Modbus, DNP3** | Communications and SCADA protocols |

A **UL 9540** certificate is for the **system**. **UL 9540A** is a **test method** for fire propagation. They are not the same thing.

## 6. Design and safety points

- **Chemistry** is specified by name (**LFP** vs. NMC): they have very different fire test results.
- **Siting and separation**, detection, suppression, ventilation, drainage and emergency access agreed with the authority and insurer.
- **Emergency response plan** (required by NFPA 855).
- **Interconnection and protection coordination** with the facility's protected power paths: a BESS fault, maintenance or fire must not affect them.
- **Operating policy:** reserve floor, dispatch limits, recovery after an event, loss-of-communications behaviour.
- **Warranty and augmentation** (adding capacity over time as cells age).
- **Cost and lead times** are changing quickly (published installed costs range widely, and certification and equipment lead times can add months) **[CHECK]**.

---

# 6.47 Thermographic scanning

## 1. What it is

**Infrared thermography** uses a **thermal camera** to read the surface temperature of **energised** equipment. A **loose, corroded or overloaded connection** has higher resistance, so it runs **hot** (power lost = I² × R) and shows up on the image **before it fails**.

It is a **predictive maintenance** tool: it finds problems **early, without a shutdown**.

## 2. What to scan in a data centre

| Area | Items |
| --- | --- |
| **Switchgear and switchboards** | Busbar joints, breakers, fuses, cable terminations, ATS and STS |
| **UPS** | Input and output terminals, bypass, DC link, battery breaker |
| **Batteries** | Intercell connections and terminals, hot cells |
| **PDUs and RPPs** | Breakers, terminations, transformers |
| **Busway** | Joints and tap-offs |
| **Transformers and generators** | Windings, bushings, terminations |
| **Rack PDUs and plugs** | Hot plugs and connectors |
| **Cooling plant** | Motor starters, drives, motors and bearings |

## 3. Requirements and good practice

| Requirement | Detail |
| --- | --- |
| **Equipment under load** | Heat only appears with current. Scan at **normal loading**, or at least about **40% of rated load** **[CHECK]**. **Record the load** at the time of the scan |
| **Emissivity and reflections** | Bare, shiny metal has **low emissivity** and reads **too cool** (it reflects its surroundings). Read connections off **high-emissivity** surfaces (painted housings, lugs, insulation) or use matte tape or paint |
| **Focus and distance** | Focus every image before trusting a temperature |
| **Compare** | Compare **phases against each other** first, then against **similar components**, using ambient only when there is no twin |
| **Safety** | Opening covers on live equipment is **energised work**: qualified people, PPE and procedures (NFPA 70E). **IR windows** (permanent crystal or polymer ports) let you scan with the cover closed, outside the arc-flash boundary |
| **People** | Trained (Level I or II) thermographers |
| **Reports** | Thermal and visible image, location, load, temperatures, ΔT, severity, action. Re-scan after repair |
| **Tools** | Cameras, with IR windows. Clamp meters to check the current. Ultrasound can complement it for partial discharge |

## 4. Severity criteria (NETA MTS Table 100.18) **[CHECK]**

Temperature rise (ΔT) compared with a **similar component under similar load** (preferred) or with **ambient**:

| Priority | ΔT vs. similar component | ΔT vs. ambient | Action |
| --- | --- | --- | --- |
| **Possible deficiency** | 1 to 3 °C | 1 to 10 °C | Investigate, trend, re-scan |
| **Probable deficiency** | 4 to 15 °C | 11 to 20 °C | Repair at the next opportunity or outage |
| **Monitor** | | 21 to 40 °C | Monitor until corrected |
| **Major deficiency** | **Over 15 °C** | **Over 40 °C** | **Repair immediately** |

"Repair immediately" sets a **maintenance priority**. It doesn't authorise anyone to work on energised equipment.

## 5. Load correction

Because heat varies with **I²**, a reading at light load **understates** the problem. A common estimate **[CHECK]**:

```
ΔT at full load ≈ ΔT measured × (I_rated / I_measured)²
```

**Worked example.** A hot lug is **68 °C** and a similar lug **40 °C**, so ΔT = 28 °C, at **60%** load:

```
Corrected ΔT = 28 × (1 / 0.6)² = 28 × 2.78 = about 78 °C   → major deficiency, repair immediately
```

A reading of **20 °C at 50%** load would correspond to about **80 °C** at full load (20 × 4).

## 6. How often **[CHECK]**

| Standard | Guidance |
| --- | --- |
| **NFPA 70B (2023 edition)** | A documented electrical maintenance programme with **infrared thermography at intervals tied to equipment condition**: **12 months** (Condition 1 and 2) and **6 months** (Condition 3), and more often for critical equipment. It is now an **enforceable standard**, not just a recommendation |
| **Insurers** | Often require an **annual survey report** |
| **Extra scans** | After installing equipment, changing loads, or making repairs |
| **Critical gear (for example main switchgear)** | Many sites scan quarterly, or install **continuous thermal sensors** |

## 7. Related standards

| Standard | Topic |
| --- | --- |
| **NFPA 70B** | Electrical equipment maintenance |
| **NFPA 70E** | Electrical safety in the workplace (arc flash, PPE) |
| **ANSI/NETA MTS** | Maintenance testing specifications, including ΔT criteria |
| **ISO 18434-1** | Condition monitoring: thermography |
| **ASTM E1934** | Guide for examining electrical and mechanical equipment with infrared thermography |

## 8. What thermography does not do

- It **screens**: a hot spot is a **problem to investigate**, not a proven fault. The cause might be an unbalanced load or a harmonic, not a loose joint.
- It can't see **inside** a closed enclosure unless an **IR window** is fitted.
- It needs **load**, and it shows only the **surface**.
- It complements, but **does not replace**, testing, visual inspection and monitoring.

---

## Glossary

| Term | Meaning |
| --- | --- |
| Static / dynamic UPS | Electronic converters with batteries / rotating machine with flywheel |
| VFI, VI, VFD | Voltage and frequency independent / voltage independent / dependent |
| IEC 62040-3 code | Input dependency, waveform and dynamic performance, for example VFI-SS-11 |
| Static bypass | Solid-state switch from the UPS output to the bypass source |
| Maintenance bypass | Manual path so a UPS can be serviced while the load stays on |
| Eco / high-efficiency mode | Bypass carries the load, inverter on standby |
| Walk-in | Gradual rectifier start to avoid shocking a generator |
| Modular UPS | UPS built from hot-swappable power modules |
| DRUPS | Diesel rotary UPS: flywheel, motor-generator and diesel |
| Flywheel | Rotating mass storing kinetic energy |
| VRLA / LFP | Valve-regulated lead-acid / lithium iron phosphate |
| BMS | Battery management system |
| Float charge | Constant voltage that keeps a battery full |
| End-of-discharge voltage | The lowest voltage per cell during a discharge (about 1.75 V for lead-acid) |
| Capacity test | A discharge that measures real battery capacity |
| Ohmic test | Internal impedance, conductance or resistance measurement |
| BESS / PCS / EMS | Battery energy storage system / power conversion system / energy management system |
| Peak shaving | Using stored energy to cut the site's maximum demand |
| ΔT | Temperature rise above a reference (thermography) |
| IR window | Permanent port for infrared scanning with the cover closed |

## Exam takeaways

**6.36 to 6.39 (static UPS)**

- A UPS needs a **rectifier (AC to DC)** and an **inverter (DC to AC)** because batteries store only DC.
- **IEC 62040-3 code:** input dependency (**VFI, VI, VFD**), waveform (**SS, SY**...), dynamic performance (**11** is best). **VFI-SS-11** = double conversion on-line. A UPS has **a code per mode**.
- **VFI:** inverter always on, **zero transfer**, best protection, lowest efficiency. **VI:** adds a regulator. **VFD:** standby, a few ms gap.
- **Modes:** normal, **battery** (no interruption), recharge, **static bypass** (overload or fault), **maintenance bypass** (manual, no protection), **eco** (bypass carries the load).

**6.40 to 6.43 (efficiency, modular, availability, dynamic)**

- **Losses = P × (1/η − 1)**. Best efficiency at about **30 to 80%** load. **Eco mode ≈ 99%** but a transfer gap and **VFD** class.
- **Modular UPS:** hot-swappable modules, **N+1 in one frame**, **low MTTR**, pay-as-you-grow, module sleep for efficiency. Shared frame parts are a risk.
- **Availability:** parallel, catcher, distributed, **2N**, **dual-input**, **distributed bypass**, redundant battery strings. A **common bus limits** parallel systems.
- **DRUPS:** flywheel + motor-generator + diesel, **no batteries**, ride-through **seconds** (about 8 to 15 s), flywheel energy is about **60 times less** than a 10-minute battery.

**6.44 to 6.47 (batteries, testing, BESS, thermography)**

- **VRLA** about 3 to 8 years real life, **lithium-ion (LFP)** about 8 to 15 years but dearer and a fire-code issue. **Life halves per 8 to 10 °C above 25 °C.** Lead-acid cell: **2 V nominal**, **1.75 V** end-of-discharge, **about 2.25 to 2.30 V** float.
- **Battery sizing:** energy = P × t ÷ η, then margins. Check at the **short discharge rate**.
- **Testing (IEEE 450 vented, IEEE 1188 VRLA):** monthly and quarterly checks, **ohmic tests flag weak cells but don't measure capacity**, **capacity test** is the proof. **Replace at about 80%.** Acceptance at least about 90%.
- **BESS:** cells, BMS, **PCS**, **EMS**, thermal and fire systems. Cycled daily, **not a no-break UPS**, **UPS batteries are not for peak shaving.** **UL 9540** (system), **UL 9540A** (fire test), **NFPA 855** (installation).
- **Thermography:** scan **under load (at least about 40%)**, mind **emissivity**, use **IR windows**, compare phases. **NETA: over 15 °C vs. similar = major.** **NFPA 70B interval about 12 months** (6 months for poor condition).

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **IEC 62040-1, -2, -3, -4**, **UL 1778** | UPS safety, EMC, performance and classification, environmental |
| **IEEE 485**, **IEEE 450**, **IEEE 1188**, **IEEE 1106** | Battery sizing and testing: lead-acid, VRLA, nickel-cadmium |
| **IEC 60896**, **EN 50272-2**, **IEC 62485-2** | Stationary battery requirements and safety |
| **IEC 62619**, **UL 1973**, **UL 9540**, **UL 9540A** (sixth edition effective 1 January 2027) | Lithium-ion and energy storage safety and fire propagation testing |
| **NFPA 855** (2026), **NFPA 69** | Energy storage installation and explosion control |
| **IEEE 1547**, **IEEE 1547.9**, **IEC 62933** | Grid interconnection and electrical energy storage systems |
| **NFPA 70B** (2023), **NFPA 70E** | Electrical maintenance programmes and safe working |
| **ANSI/NETA MTS** Table 100.18 | Thermography temperature-rise criteria |
| **ISO 18434-1**, **ASTM E1934** | Thermography practice |
| ENERGY STAR for UPS | Efficiency levels |

Vendor comparisons of dynamic and static UPS disagree, so treat them with care. Figures marked **[CHECK]** come from general industry practice rather than a named standard.
