# Module 14: Auxiliary Systems

Detailed notes, following the lesson-level index of the EPI course. The practice questions for this module are in [00_knowledge_tests.md](00_knowledge_tests.md#module-14-auxiliary-systems).

| Lesson | Title | Section |
| --- | --- | --- |
| 14.1 | Monitoring Challenges and Requirements | [Section 1](#141-monitoring-challenges-and-requirements) |
| 14.2 | EMS, BMS and DCIM | [Section 2](#142-ems-bms-and-dcim) |
| 14.3 | Water Leak Detection | [Section 3](#143-water-leak-detection) |
| 14.4 | Notification System | [Section 4](#144-notification-system) |
| 14.5 | Equipment and Components Monitoring | [Section 5](#145-equipment-and-components-monitoring) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-14-auxiliary-systems) |

**Objectives (from your slide).** After this module you should be able to describe and understand:

- Monitoring challenge
- Monitoring requirements
- Environmental Monitoring System (EMS)
- Building Management System (BMS)
- Data Centre Infrastructure Management (DCIM)
- Water leak detection
- Notification

| Objective | Where it is covered |
| --- | --- |
| **Monitoring challenge** | 14.1 (section 1.2) |
| **Monitoring requirements** | 14.1 (section 1.3), 14.5 |
| **Environmental Monitoring System (EMS)** | 14.2 (section 2.2) |
| **Building Management System (BMS)** | 14.2 (section 2.3) |
| **Data Centre Infrastructure Management (DCIM)** | 14.2 (section 2.5) |
| **Water leak detection** | 14.3 |
| **Notification** | 14.4 |

Lesson 14.5 (equipment and components monitoring) is in your index but not in the objectives, so it is covered as the practical detail behind "monitoring requirements".

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Only the **objectives slide** was available for this module (not the lesson slides), so check the glossary and figures against your course. **Watch the abbreviation "EMS":** on your slide it means **Environmental Monitoring System**, but in much of the industry literature it stands for **Energy Management System**. Section 2 explains both. Related earlier material: ASHRAE classes and sensor locations (9.1, 9.9), PUE (6 index), alarm and detection systems for fire (Module 12), security systems (Module 13), network monitoring (11.8), batteries and thermography (6.44 to 6.47), leak removal and water (Modules 9 and 10).

## The big picture

The **primary systems** of a data centre are power, cooling, network, fire protection and security. The **auxiliary systems** in this module are what let people **see, control, manage and be warned about** them:

```
Sensors and field devices ─► monitoring / control layer (EMS, BMS, EPMS) ─► management layer (DCIM)
        │                                         │                                │
   leak detection                         alarms and events                 capacity, assets, reports
        └────────────────────────► NOTIFICATION ─► the right person ─► response
```

You cannot manage, protect or plan what you cannot measure. But **more data is not the same as more insight**: the aim is the **right data, in the right place, with the right alarm reaching the right person in time**.

---

# 14.1 Monitoring challenges and requirements

## 1.1 Why monitor

| Reason | Benefit |
| --- | --- |
| **Detect faults early** | Fix a failing fan, valve or battery before it becomes an outage |
| **Reduce repair time (MTTR)** | Faster detection and diagnosis lifts availability (availability = MTBF / (MTBF + MTTR)) |
| **Plan capacity** | See remaining power, cooling, space and ports |
| **Run efficiently** | Measure and improve PUE and other KPIs |
| **Prove compliance** | SLA reports, ISO/IEC 27001 (A.7.4 monitoring, A.7.5 environmental threats), customer audits, regulators |
| **Support maintenance** | Condition data drives planned work (14.5) |
| **Detect security and safety events** | Doors, leaks, smoke, temperature |

**Power remains the leading cause of impactful outages** (reported at 54% of operators in the Uptime Institute's 2025 analysis, with cooling at 13%, and still the leading cause in 2026) **[CHECK]**, which is why the monitoring of the **power chain** matters as much as the cooling.

## 1.2 The monitoring challenges

| Challenge | What goes wrong | Response |
| --- | --- | --- |
| **Many different devices and protocols** | BACnet, Modbus, SNMP, LonWorks and proprietary protocols, on equipment of different ages. A 20-year-old chiller and a new GPU rack do not speak the same language | A **vendor-neutral integration layer** (gateways, open protocols), and a **points list** |
| **Silos** | The BMS watches cooling, the electrical system has its own monitoring, IT has network tools, and nobody sees the whole. The **same UPS alarm** arrives from three systems at three priorities to three lists | **One master per device**, defined **boundaries**, **one accountable owner** per alarm |
| **Data volume and scale** | Thousands of points, faster polling, AI racks producing far more telemetry | Collect what **supports a decision**, tier the storage, summarise old data |
| **Alarm floods and fatigue** | A single event (power dip, cooling trip) cascades into hundreds of alarms. Staff learn to ignore the board | **Alarm management** (14.4) |
| **Sensor placement and accuracy** | A sensor in the wrong place gives false confidence. Humidity sensors drift | Measure at the **equipment inlet**, calibrate, check sensor health |
| **Data quality** | Inconsistent point names, wrong units or scaling, clocks out of step, duplicate readings | Naming standard, unit checks, **NTP**, plausibility limits |
| **Speed versus load** | Control needs seconds, trending needs minutes, energy needs 15 minutes. Several systems polling one Modbus device time out on each other | Match the **polling interval** to the decision. One master polls, others read from it |
| **Cybersecurity** | The BMS and EPMS are **operational technology (OT)** networks. A DCIM integration can become a route from the corporate network to plant controllers | **Segmentation (IEC 62443 zones and conduits)**, controlled remote access, no default passwords |
| **The monitoring system itself can fail** | A single collector, a single network path or no backup power turns monitoring into a single point of failure | Redundant collectors, **UPS and generator power**, an **out-of-band alert path** (cellular), **edge buffering** |
| **Records drift from reality** | The asset register shows what was installed, not what is there | Initial **asset survey**, change workflow, periodic audits. **Wrong data is worse than no data** |
| **Skills and ownership** | An alarm on three platforms with no owner creates the illusion of control | Roles, procedures, training |
| **Over-design and cost** | All three platforms installed in parallel on a small site | Scope to the site's size and Tier (14.2) |
| **Density and speed of failure** | A cooling failure heats a dense hall in seconds to minutes (9.1) | Rate-of-change alarms, short polling for critical points |

## 1.3 Monitoring requirements

### What to monitor

Guidance (ASHRAE TC 9.9, ANSI/TIA-942-C, Uptime Institute) converges on these **domains**:

| Domain | Examples |
| --- | --- |
| **Power** | Utility, switchgear, transformers, generators, ATS, UPS, batteries, PDUs, branch circuits, rack PDUs, energy meters |
| **Cooling** | Chillers, pumps, towers, CRAH/CRAC, chilled water, liquid cooling (CDUs) |
| **Environment** | Temperature, humidity and dew point, airflow, differential pressure |
| **Water and liquids** | Leak detection (14.3), tank levels, fuel |
| **Fire, safety and security** | Fire panel, aspirating detection, gas systems, doors, access control, cameras, intruder alarms |
| **Network and IT** | Switches, servers (management controllers), storage, optical links |
| **Energy and efficiency** | PUE, kWh, capacity margins |

### Sensor requirements

| Requirement | Practice |
| --- | --- |
| **Where** | At the **IT equipment air inlet** (the geometric centre of the intake, about 5 cm in front of the equipment), **not at the cooling unit or the room centre** |
| **How many** | **Three sensors per monitored rack** (top, middle, bottom of the inlet), on **every rack in dense rows** and on **every other or every third rack** in uniform low-density rows. ASHRAE is not specific about the number of racks. Some vendors quote **six per rack** (front and rear) for the inlet-to-exhaust ΔT: treat that as a design choice, not a rule **[CHECK]** |
| **Also** | Supply and return at each cooling unit, rack exhaust for ΔT, **hot aisle and containment** areas, under-floor and ceiling plenums, **differential pressure** across floor and containment |
| **Humidity** | **Dew point** (not only relative humidity), co-located with temperature, because dew point is the moisture itself and ASHRAE uses it |
| **Accuracy** | Temperature **±0.5 °C or better** (±0.3 °C near the 18 and 27 °C limits), humidity about **±2 to 3% RH**, a fast response (T90 under about 60 s) **[CHECK]** |
| **Drift** | Temperature probes are stable for years, humidity sensors **drift**: check at least once a year against a reference |
| **Rate of change** | ASHRAE limits: **20 °C per hour** for most IT equipment (and about 5 °C in any 15-minute period), **5 °C per hour for tape**. Alarm on the **rate of rise**, not only the absolute value **[CHECK]** |

**Worked example: sensor count.** A hall has **6 rows of 10 racks** (60 racks):

```
Uniform rows, every third rack (racks 1, 4, 7, 10 per row): 4 × 6 = 24 racks × 3 sensors = 72 inlet sensors
Dense rows (every rack): 60 × 3 = 180 inlet sensors
Plus rear (exhaust) sensors for ΔT:           60 × 3 = 180 more, so 360 in total
```

**Worked example: rate-of-change alarm.** The inlet temperature rises from 24 °C to 29 °C in 4 minutes:

```
Rate = 5 K / 4 min = 1.25 K per minute  →  the 5 °C in 15 minutes limit is reached after 4 minutes
```

A cooling failure heats air far faster than that (16.6 K per minute for the whole hall air in 9.1), so a rate alarm fires **long before** a high-temperature threshold.

### Other requirements

| Requirement | Detail |
| --- | --- |
| **Sampling interval** | Match the decision: **seconds** for control and critical alarms, **1 to 5 minutes** for trending, **about 15 minutes** for energy and PUE, hourly or daily for capacity **[CHECK]** |
| **Alarm management** | Multi-level thresholds, deadband, delays, priorities, grouping (14.4) |
| **Data retention** | Keep **readings, not just alarms**, to compare seasons: raw data for months, summaries for years (at least 13 months so a season can be compared with last year) **[CHECK]** |
| **Reliability of the monitoring** | Redundant collectors and servers, **protected power**, redundant network, **out-of-band** notification, **edge buffering** so events survive a network break |
| **Integration** | Open protocols (BACnet, Modbus, SNMP, OPC UA, MQTT), links to **DCIM, BMS, ITSM** and the fire and security systems |
| **Hardwired safety loops stay hardwired** | Fire suppression release and EPO must not depend on a network or monitoring server |
| **Scalability** | Room to add points, rooms and sites without replacing the platform |
| **Security** | Segmented network, strong authentication, role-based access, audit logs, patching |
| **Time synchronisation** | **NTP** everywhere, so events from different systems line up |
| **Calibration and maintenance** | Scheduled calibration and sensor health checks |
| **Documentation** | Points list, naming standard, thresholds with their basis, single-line and flow diagrams |
| **Standards and reporting** | PUE per **ISO/IEC 30134-2 / EN 50600-4-2**, management and operational information per **EN 50600-2-6 / ISO/IEC TS 22237-7**, ASHRAE envelopes |
| **Cost** | Total cost over the life (licences, support, expansion, engineering time), not the first price |

### Worked example: data volume

**5,000 points polled every 10 seconds**, 16 bytes per sample:

```
Samples = 5,000 / 10 = 500 per second = 43.2 million per day
Storage = 43.2 × 10⁶ × 16 B = about 691 MB per day = about 252 GB per year
```

Fine for storage, but the **alarm and display load** is the real problem: tier the data (fast for a few days, summarised after).

## 1.4 Common mistakes

- Monitoring only at **room level** (one sensor tells you almost nothing about the server inlet).
- **Collecting data with no decision attached.**
- **No owner** for each alarm.
- **Thresholds copied** from another site.
- The **monitoring server on a single power feed** and a single network path.
- **Sensors never calibrated or tested.**
- Three systems **polling the same device**.
- Ignoring the **IT side** (no inlet temperature from the servers themselves).
- **No out-of-band alert path.**

---

# 14.2 EMS, BMS and DCIM

## 2.1 Three layers, three different jobs

| Layer | Unit of measure | Core question |
| --- | --- | --- |
| **EMS** (environmental monitoring) | **Sensors** in the space (temperature, humidity, airflow, leak, door) | "What are the **conditions**, and are they in range?" |
| **BMS** (building management) | The **building's mechanical and electrical systems** (chillers, air handlers, pumps, lighting, fire and security interfaces) | "How do I **control** and coordinate the plant to hold conditions?" |
| **DCIM** (data centre infrastructure management) | The **assets and capacity** (racks, PDUs, UPS, switches, cables, space) | "What is **installed**, how much capacity is **left**, and what happens if I **change** something?" |

A fourth acronym appears in the literature:

| Term | Meaning |
| --- | --- |
| **EPMS** | **Electrical power monitoring system**: the power chain from the utility to the PDU, with **sequence-of-events** analysis and power quality |
| **Energy Management System (also "EMS")** | Reads **submeters**, aggregates energy, supports **ISO 50001** and regulatory reporting. It does **not control** equipment |
| **SCADA** | The **supervisory** layer that reads controllers and sends commands (setpoints, sequencing). Often the BMS performs this role |

## 2.2 Environmental Monitoring System (EMS)

| Feature | Detail |
| --- | --- |
| **Purpose** | **Continuously measure the room's environment and alarm** when it leaves the allowed range |
| **Sensors** | Temperature, humidity and **dew point**, airflow, differential pressure, **water leak**, door contacts, smoke or fire status inputs, sometimes particulates, vibration, power |
| **Hardware** | Sensor probes (wired RS-485 or 1-Wire, or wireless mesh), a base unit or gateway, a server or cloud application |
| **Outputs** | **Alarms**, trend graphs, **thermal maps**, reports, relay outputs |
| **Protocols** | **SNMP, Modbus**, BACnet, MQTT, e-mail, SMS |
| **Strengths** | Fast to deploy, inexpensive, good for small rooms and sites with no BMS, adds **rack-level** detail a BMS lacks |
| **Limits** | Monitors and alarms but **does not control** the plant, and gives little asset or capacity context |
| **Where used** | Server rooms, comms rooms, edge and remote sites, as a **sensor layer** feeding a BMS or DCIM |

The point of an EMS is to measure **at the server inlet**, where thermal failure starts, and to warn **before** the cooling alarm does.

## 2.3 Building Management System (BMS)

| Feature | Detail |
| --- | --- |
| **Purpose** | **Control and monitor** the building services so the data centre holds the required conditions |
| **Scope** | Chillers, pumps, cooling towers and dry coolers, CRAH/CRAC control, air handling, humidifiers, **free-cooling changeover**, lighting, and **interfaces** to fire, security, leak detection and (often) basic electrical states |
| **Architecture** | Field devices (sensors, valves, drives) → **DDC controllers or PLCs** → network → **head-end server** with graphics, trends, schedules and alarms |
| **Control** | Closed loops (PID), **sequences of operation** (stage chillers, rotate units, change over to free cooling), setpoints, interlocks (for example gas release shuts down air handling) |
| **Data rate** | Fast: typically **1 to 10 seconds** (motor and damper control needs it) |
| **Protocols** | **BACnet** (ANSI/ASHRAE 135 = ISO 16484-5) as the main language, **Modbus**, LonWorks, OPC UA at supervisory boundaries |
| **Users** | Facilities engineers and mechanical technicians |
| **Strengths** | **Real-time control**, the system of record for **mechanical and environmental alarms**, ties plant behaviour to conditions |
| **Limits** | Not designed for **asset tracking, rack-level capacity planning or IT workflows**. Often lower resolution on electrical data |

### Typical BMS interlocks and sequences

| Event | BMS response |
| --- | --- |
| Gas suppression pre-discharge | Air handlers stop, dampers close (12.6) |
| Power failure, UPS on battery | Keep cooling fans and pumps on protected power, hold a safe state (9.1) |
| Outside air cold enough | Switch to free cooling (9.5) |
| CRAH unit fault | Start the standby unit (N+1) |
| Leak detected | Alarm and close an isolation valve where designed (14.3) |
| High differential pressure across a filter | Maintenance alarm |

## 2.4 The electrical side: EPMS

An EPMS covers the **power path from incomer to PDU**, with **voltage, current, kW, kVA, power factor, frequency, harmonics, breaker status, energy and event records**. Its strength is **high-resolution event analysis** (what exactly happened in a power disturbance) and **branch-circuit monitoring** (finding a circuit before it trips). Where the site is small, the BMS may do this at lower resolution. Where it is large, the **seam between the BMS and the EPMS** is where problems live: the cooling team must know **UPS on battery, generator running, ATS position and mains healthy**.

## 2.5 Data Centre Infrastructure Management (DCIM)

### What DCIM does

| Function | Detail |
| --- | --- |
| **Asset management** | An **asset register** at rack and U position: servers, switches, PDUs, UPS, cooling units, with attributes (power, weight, depth, ports, owner, warranty) |
| **Connectivity management** | Which port connects to which, power and network path tracing ("what is plugged into PDU 3A?") |
| **Capacity planning** | **Four dimensions: power, cooling, space and network (and weight).** Shows installed, available, redundant and committed capacity, and **what-if** simulation |
| **Monitoring** | Collects power, temperature and environmental data (via SNMP, Modbus, BACnet) and shows it in context |
| **Change management** | **Workflow** for moves, adds and changes with approvals, work orders and an audit trail |
| **Visualisation** | Floor plans, rack elevations, **thermal maps** (with interpolation between sensors), 3D views, digital twins with CFD |
| **Energy and PUE** | Collects meters, calculates **PUE** and other KPIs, trends over rolling windows |
| **Analytics and reporting** | Reports for management, audits and customers, anomaly detection |
| **Integration** | **BMS** (cooling data), **EPMS and EMS** (meters), **IT** (CMDB, SNMP, IPMI, Redfish), **ITSM** (ServiceNow, Jira Service Management) for tickets |

DCIM is **not** designed for **real-time control** of physical processes. Its data rate is slower (typically **1 to 5 minutes**) and it works at the **rack and port** level.

### What a good DCIM answers

1. What is installed and where?
2. What power, cooling and space is **used** and **available**?
3. What is about to run out or fail?
4. What happens if I **move or add** this equipment?

A product that leads with AI but cannot answer "what is plugged into PDU 3A?" is **a dashboard, not a DCIM.**

### Worked example 1: stranded capacity

**20 racks** are allocated **8 kW** each, but their measured peak is **4.5 kW** each:

```
Allocated = 20 × 8   = 160 kW
Measured  = 20 × 4.5 =  90 kW
Stranded  = 160 − 90 =  70 kW   (reserved on paper, never used)
```

DCIM makes this visible, so the stranded capacity can be reallocated (6.34 in `06-3`).

### Worked example 2: the limiting resource

The hall has **headroom** of **120 kW of power**, **90 kW of cooling**, space for **40 racks averaging 5 kW (200 kW)**, and enough ports:

```
Deployable load = the smallest headroom = min(120, 90, 200) = 90 kW   → cooling is the binding constraint
```

Adding racks beyond 90 kW needs more cooling, not more power.

### Pitfalls

| Pitfall | Why it matters |
| --- | --- |
| **No asset survey** | A DCIM rolled out without a physical survey (often weeks of work) shows wrong data for a long time. **Wrong data is worse than no data** |
| **Records drift** | The IT inventory and DCIM inventory diverge constantly, so the change workflow must keep the drift small |
| **Vendor lock-in** | Choose an **open data model** (export in CSV, JSON, BACnet objects, OPC UA) |
| **Deployment model** | On-premises, SaaS or hybrid, with **data residency** and security in mind |
| **Integration depth** | Check the list of supported BMS, EPMS, ITSM and CMDB integrations before buying |
| **Duplicate instrumentation** | Read meters from the EMS or EPMS instead of metering twice |

## 2.6 Comparison

| | **EMS (environmental)** | **BMS** | **EPMS** | **DCIM** |
| --- | --- | --- | --- | --- |
| **Unit of measure** | Sensors in the space | Building plant | Electrical path and circuits | Assets, racks and capacity |
| **Controls equipment?** | No | **Yes** | No | **No** (not real time) |
| **Main protocols** | SNMP, Modbus | **BACnet**, Modbus, LonWorks | Modbus, SNMP | **SNMP, Modbus, BACnet**, APIs |
| **Granularity** | Sensor and rack | Air handler, circuit, plant item | Breaker, circuit, outlet | **Rack and port** |
| **Refresh** | Seconds to minutes | **1 to 10 s** | Seconds (events), minutes (trends) | **1 to 5 min** |
| **Main users** | Operations, IT | Facilities engineers | Electrical engineers | IT operations, capacity planners |
| **Strength** | Rack-level, quick, cheap | Real-time control, mechanical alarms | Power event analysis | Capacity, assets, change |
| **System of record for** | Environmental readings | Mechanical and environmental alarms | Electrical events and power quality | Asset and capacity data |

## 2.7 How they fit together

```
 Field level:     sensors · valves · drives · meters · UPS · generators · PDUs · servers
                    │          │            │         │
 Control layer:     EMS      BMS (BACnet)  EPMS (Modbus)  IT (SNMP, Redfish)
                    └──────────┴─────┬──────┴─────────────┘
 Management layer:             DCIM (assets, capacity, workflow, PUE)  ─► ITSM / CMDB / dashboards
                                      │
 Notification:             alarms ─► email · SMS · voice · tickets ─► on-call team
```

### Rules for clean integration

| Rule | Why |
| --- | --- |
| **One master per device** | Several systems polling one Modbus device over the same RS-485 line time out on each other. One polls, the others read from it over IP |
| **Define the source of truth** for every critical data point | Avoids contradictory values |
| **One accountable owner per alarm** | An alarm visible on three platforms still needs one owner who investigates, escalates and closes it |
| **BMS owns mechanical alarms, EPMS owns electrical events, DCIM owns capacity** | One device, three consumers, one gateway if the head-end cannot read SNMP |
| **Open protocols at every seam** | **BACnet/IP** between building systems, **Modbus** at meters, **OPC UA** at supervisory boundaries, **SNMP** to IT. Proprietary protocols lock the layer above to one vendor |
| **Hardwired safety loops** | Fire suppression release and EPO must run with **no network dependency** |
| **Common clock and naming** | NTP and a single asset ID scheme |

## 2.8 Protocols and interfaces

| Protocol or interface | Typical use |
| --- | --- |
| **BACnet** (ANSI/ASHRAE 135, ISO 16484-5; BACnet/IP, MS/TP, and **BACnet/SC** for secure links) | Building automation: chillers, air handlers, valves |
| **Modbus** (RTU serial, TCP/IP) | Meters, UPS, generator controllers, sensors |
| **SNMP** (v1, v2c, **v3**) | IT devices, rack PDUs, UPS cards, environmental monitors. Polling and **traps** |
| **LonWorks** | Older building controls |
| **OPC UA** | Supervisory data exchange, secure and vendor-neutral |
| **MQTT** | Light-weight messages from IoT sensors |
| **Redfish, IPMI** | Server management controllers (inlet temperature, power) |
| **DNP3, IEC 61850** | Utility and substation equipment |
| **REST APIs, webhooks** | Cloud platforms, ITSM and ticketing |
| **Dry contacts (relays), 4 to 20 mA, 0 to 10 V** | Simple status and analog signals, and hardwired safety signals |
| **Wireless (mesh, LoRaWAN, BLE)** | Battery sensors in hard-to-wire places |

## 2.9 PUE and metering

**PUE = total facility energy ÷ IT equipment energy** over the same period (ISO/IEC 30134-2 / EN 50600-4-2). The meter location sets the **measurement level** (The Green Grid):

| Level | IT energy measured at | Accuracy |
| --- | --- | --- |
| **1 (basic)** | **UPS output** | Lowest: includes losses in the PDUs and distribution |
| **2 (intermediate)** | **PDU output** | Better |
| **3 (advanced)** | **IT equipment input** (rack PDU or smart plug) | Most accurate |

Two PUE figures are comparable **only if measured at the same level, boundary and period**. Use **continuous metering** (readings of about 15 minutes or better), not a spot reading.

**Worked example.** The facility draws **1,350 kW** on average and the UPS output is **900 kW**. Distribution losses between UPS and servers are about 3%:

```
Level 1:  PUE = 1,350 / 900 = 1.50
Level 3:  IT at the rack input = 900 × 0.97 = 873 kW  →  PUE = 1,350 / 873 = 1.55
```

The same site reports 1.50 or 1.55 depending on where it meters. **Trend PUE** over a rolling 30-day window: a **rising PUE with stable IT load** points to degrading cooling (fouled chiller, failing pump, poor air distribution).

## 2.10 Cybersecurity of the monitoring systems

| Risk | Control |
| --- | --- |
| **OT networks** | BMS and EPMS networks are operational technology. Keep them **separate** from corporate IT |
| **DCIM as a bridge** | Integration must not become a route from the corporate network to plant controllers. **IEC 62443 zones and conduits** |
| **Weak protocols** | Modbus has no security: protect it by network design. Use **SNMPv3**, **BACnet/SC**, **OPC UA** security |
| **Default and shared passwords** | Unique accounts, role-based access, audit logs |
| **Remote access** | Controlled, logged, time-limited, with multi-factor authentication. No open vendor VPN |
| **Patching** | Controllers, gateways and servers on a patch schedule |
| **Regulation** | **NIS2** and similar rules extend to digital infrastructure operators |

## 2.11 Choosing what a site needs

| Site | Typical choice **[CHECK]** |
| --- | --- |
| **Small server room or edge site** | An **EMS** with alerts, possibly with a simple BMS. A spreadsheet or small DCIM for capacity |
| **Tier I to II site with a few air handlers** | A BMS (which also reads basic electrical states) and a basic DCIM |
| **Colocation under about 200 kW** | A modern **DCIM** with an energy module often covers the roles |
| **Tier III or IV or large site** | **BMS + EPMS + DCIM** (each with defined boundaries), plus an EMS or rack sensor network |
| **Colocation with billing** | **EPMS and DCIM sharing one data model** (outlet metering, tenant portals) |
| **AI and GPU halls** | The above plus **IT telemetry** (Redfish, IPMI) and liquid cooling monitoring in the same view |

Avoid **three platforms installed in parallel with overlapping scope** on a site that does not need them: it adds cost and conflicting alarms.

## 2.12 Standards

| Standard | Contribution |
| --- | --- |
| **ANSI/ASHRAE 135 = ISO 16484-5** | BACnet |
| **ISO/IEC 30134-2 = EN 50600-4-2** | PUE |
| **EN 50600-2-6 and ISO/IEC TS 22237-7** | Management and operational information (monitoring, operations) |
| **ISO 50001** | Energy management systems |
| **IEC 62443** | Industrial control system security |
| **ISA-18.2 / IEC 62682, EEMUA 191, ISA-101** | Alarm management and HMI (14.4) |
| **ASHRAE TC 9.9** | Thermal envelopes for the thresholds |
| **ANSI/TIA-942-C** | Monitoring provisions by rating |

---

# 14.3 Water leak detection

## 3.1 Why it matters

A data centre combines **a high density of water-bearing services** with **equipment that is extremely sensitive to water**. A hall can have tens of chilled water pipe runs and thousands of litres of water, all under pressure, a few metres from live equipment.

| Source of liquid | Notes |
| --- | --- |
| **Chilled water and glycol pipes** | Valves, joints, flanges and expansion loops age. A pinhole in a pressurised line sprays |
| **CRAH and CRAC units** | Coils, valves, and the **condensate pan, drain and pump**. A blocked drain quietly overflows the pan |
| **Humidifiers** | Water supply and drain |
| **Overhead pipework** | A leak above the IT load is worse than one below it |
| **Roof and ceiling** | Rain ingress, roof drains, plant on the roof |
| **Sprinkler pipework** | Pre-action reduces the risk (12.4) |
| **Plant rooms and cooling towers** | Pumps, valves, basins |
| **Battery rooms** | Acid electrolyte |
| **Generator and fuel areas** | Diesel, oil, coolant |
| **Liquid cooling** | Manifolds, quick-disconnects, CDUs, rack connections, immersion tanks |
| **Plumbing nearby** | Toilets, kitchens, risers through the slab |

| Consequence | Detail |
| --- | --- |
| **Short circuits and fire** | Water on power equipment |
| **Equipment damage** | Servers, switchgear, UPS |
| **Loss of cooling** | A cooling unit failure heats the room |
| **Safety** | Slips, electric shock, acid |
| **Downtime and cost** | Often large |

**Leaks travel**: water follows gravity and the pipe, then spreads along trays and floors, so an **early, located** alarm is worth far more than a late general one.

## 3.2 Sensor technologies

| Technology | How it works | Use |
| --- | --- | --- |
| **Spot (point) sensor** | Two contacts at a point: a conductive liquid bridges them | **Known low points and sources**: drip trays, under CRAH units, condensate pumps, pump and valve bases, floor cutouts |
| **Tray sensor** | Collects a small volume before alarming | Drip trays and small collection points |
| **Sensing cable** | A conductive cable that **triggers anywhere along its length** | **Where water can travel or pool**: under raised floors, along pipe runs, around perimeters |
| **Location (distance-to-leak) cable** | The panel measures resistance or capacitance and **reports the distance along the cable** (accuracy about **±4%**, so about ±0.4 m per 10 m) **[CHECK]** | Large under-floor areas: lift **the right tile first** |
| **Hydrocarbon (fuel) cable** | Responds to oil and fuel but **not to water** | **Generator rooms, day tanks, fuel lines** |
| **Acid or chemical-resistant cable** | Survives electrolyte | **Battery rooms** |
| **Optical sensors** | Detect a liquid by its optical properties | **Low-conductivity or dielectric fluids** (immersion cooling), specific surfaces |
| **Flow and pressure sensors** | Detect a leak indirectly: abnormal flow or a pressure drop | Chilled water and liquid cooling loops |
| **Water meters (pulse output)** | Unexplained consumption | Hidden or slow leaks |
| **Double-wall pipe with containment sensors** | A sensor in the containment space | Critical pipe runs |
| **Wireless leak sensors** | Battery powered (typically **2 to 10 years** depending on reporting rate) | Hard-to-wire locations |

**Which liquid is detected matters:**

| Liquid | Standard conductive cable? |
| --- | --- |
| Water | Yes |
| **Water and glycol mixtures** (most cooling loops) | **Yes** (they conduct) |
| **Diesel fuel and oil** | **No**: use hydrocarbon cable |
| Acids and other chemicals | Use chemical-resistant cable |
| **Dielectric coolants** (immersion) | **No**: use optical or other compatible sensors |

Always **test the actual fluid** with the sensor.

## 3.3 System architecture

```
Sensors / cable / spot sensors ─► leak detection controller (zones, adjustable sensitivity, relays)
                                         │
              BMS · DCIM · EMS (relay, SNMP, Modbus) ─► notification (14.4) ─► response
                                         │
                       optional automatic intervention: isolation valve, pump, power isolation
```

| Element | Detail |
| --- | --- |
| **Controller or zone module** | Manages the cable inputs, calculates leak position (location cables), gives alarm outputs and often several channels (zones) |
| **Zones** | **Short, clearly labelled zones** that correspond to a place operators can identify quickly (a CDU, a row, a branch, a room). One long zone across several areas wastes the time to find the leak |
| **Communication** | **Relay or dry contact** to the BMS, **SNMP or Modbus** to DCIM and monitoring, local sounder and beacon |
| **Power** | UPS-backed (an alarm is useless if it cannot sound in a power cut) |
| **Automatic intervention** | An **isolation valve** that closes on a verified leak, with **drainage**. See 3.5 |
| **Integration** | The alarm names the **zone and location**, not just "leak" |

## 3.4 Where to put sensors

**Principle: follow the water.** The cable must follow the **pipe routes and likely migration paths**, not a generic grid, because a leak tracks along the pipe by gravity before it spreads. A third of surveyed installations reportedly route cable away from the pipes.

| Location | Sensor type and layout |
| --- | --- |
| **Under the raised floor** | Cable along **chilled water pipe routes**, around the **perimeter**, beneath **cable cutouts**, around valves and pumps, across **low points**. As a starting point, **cross-aisle runs every 4 to 6 m** **[CHECK]** |
| **CRAH and CRAC units** | A **spot sensor in each unit's pan** plus a **cable loop** around the base, and a sensor at the **condensate drain overflow and pump** |
| **Humidifiers** | Spot sensor at the base |
| **Overhead pipes** | **Drip trays with embedded spot sensors** under joints, valves and crossings above rows, and cable along the mains |
| **Risers and shafts** | Cable running vertically beside the risers, to catch joint or flange failures |
| **Plant, pump and valve rooms** | Drip trays and cable around equipment, floor drains |
| **Cooling tower and dry cooler areas** | Basin level and overflow, nearby floor sensors |
| **UPS and electrical rooms** | Spot sensors at low points and under any pipes passing over |
| **Battery rooms** | **Acid-resistant cable** in a perimeter loop around banks, spot sensors at the base of cabinets |
| **Generator rooms and fuel areas** | **Hydrocarbon cable** along fuel lines and at day tanks, sensors in bunds |
| **Roof penetrations and ceiling voids** | Spot sensors under penetrations and drains |
| **Liquid cooling** | Spot sensors at **every quick-disconnect, manifold junction and supply and return valve**, cable loops around **CDU bases**, **rack base** sensors, sensors **inside the chassis** near cold plate connections |
| **Immersion tanks** | Overflow sensors at the rim and a **secondary containment** sensor |
| **Floor drains and sumps** | Level or spot sensors |

Place sensors **both at the likely source and along the migration path**: slope, airflow, insulation, penetrations and cable trays can carry liquid away from the source.

### Worked example: cable length and location accuracy

A hall **20 m × 30 m**:

```
Perimeter:                 2 × (20 + 30) = 100 m
Cross-aisle runs every 5 m along the 30 m length: 30 / 5 = 6 runs × 20 m = 120 m
Along the chilled water pipes: 40 m
Total cable = 100 + 120 + 40 = 260 m   → split into about 3 zones (under about 100 m each)
```

With a location cable accurate to **±4%**, a leak found **60 m** along the cable is within:

```
0.04 × 60 = ±2.4 m
```

Shorter zones (for example 5 or 6) narrow the search further.

## 3.5 Alarm and response

### The alarm chain

1. **Sensor** detects liquid.
2. **Controller** raises an alarm for that **zone** (and location).
3. **BMS, DCIM and the notification system** send it to the on-call team (14.4).
4. **Operator verifies** and **locates** the leak.
5. **Isolate** the source (valve), **contain**, **protect** equipment, **repair**, **record**.

### Response procedure

| Step | Action |
| --- | --- |
| **Verify** | Check the sensor, camera or a person, and the source |
| **Locate** | Use the zone and the cable distance |
| **Isolate** | Close the isolation valve or stop the pump |
| **Protect equipment** | Cover or move equipment, and de-energise affected circuits **only by procedure** |
| **Contain and remove water** | Absorbents, wet vacuum, pumps, drain |
| **Assess cooling** | Check the effect on cooling and the redundancy left |
| **Repair and restore** | Plumber or vendor, then test |
| **Record and review** | Incident report, root cause, lessons |

### Automatic or manual isolation

| | **Automatic isolation valve** | **Manual response** |
| --- | --- | --- |
| **Speed** | **Seconds** | Minutes (a person must arrive) |
| **Risk** | May **cut cooling to active equipment**, and a false alarm closes a valve | Water continues to flow until someone acts |
| **Needs** | Valve feedback, **redundant cooling**, alarm verification (two sensors, flow and pressure check), a design that fails **safe** | Staffing, procedures, access |
| **Typical use** | High-risk areas, liquid cooling loops, plant rooms | Lower-risk areas, or where isolation would reduce cooling |

Isolation logic **should consider cooling redundancy, alarm verification, valve feedback, flow and pressure status, and the risk of interrupting cooling to active compute equipment.**

## 3.6 Testing and maintenance

| Activity | Frequency **[CHECK]** |
| --- | --- |
| **End-to-end test** | At least **quarterly**: wet a sensor and confirm the alarm, the **location**, the **notification** (SMS, voice), the response and escalation. **A sensor never triggered is a sensor never proven** |
| **Humidity sensors** | Check at least **annually** against a reference |
| **Cable and sensors** | Inspect for damage, dust and corrosion. Replace aged sensors and **wireless batteries** |
| **After work** | Re-test after floor work, new pipework or layout changes |
| **Zone map** | Keep a current zone drawing and update it |
| **Records** | Test logs, calibration and false alarm records |
| **False alarms** | Investigate: condensation, cleaning water, a sensor in a wet place |

## 3.7 Liquid cooling

(9.15 in `09_cooling_infrastructure.md`.) Liquid cooling brings coolant **to every rack**, so leak detection must reach the rack.

| Measure | Detail |
| --- | --- |
| **Rack level** | Sensors at the rack base and inside the chassis near cold plate connections, **drip trays under CDU manifolds and quick-disconnects** |
| **CDU level** | Built-in leak sensing in many CDUs, cable around the CDU base, flow and pressure monitoring on both loops |
| **Zoning** | By CDU, row and branch, so the alarm says **which** to investigate |
| **Intervention** | Automatic isolation of a leaking branch, balanced against cooling redundancy |
| **Fluids** | Water-glycol is conductive. **Dielectric fluids need optical or compatible sensors** |
| **Design** | Dripless quick-disconnects, double-wall pipe, secondary containment, low-point sensors |

Facility-level detection (cable under the floor, sensors at CRAH units) remains the **baseline**: liquid cooling adds a layer, it does not replace one.

## 3.8 Common mistakes

- **Grid pattern cable** that does not follow the **pipe routes**.
- **No condensate monitoring** (drip pan, drain overflow and pump).
- **No overhead protection**: only the floor is covered.
- **One zone** for the whole hall.
- **Wrong cable** for the liquid (fuel, acid, dielectric).
- **Sensors never tested.**
- **Alarm to an unmanned inbox**, with no response procedure.
- **No backup power** for the controller.
- **Automatic shut-off** that cuts cooling with no redundancy check.

## 3.9 Standards and guidance

There is **no single dedicated standard** for data centre leak detection. It sits within:

| Source | Contribution |
| --- | --- |
| **NFPA 75** | Structural floor must allow **removal of leaks** (cooling water, pipes, sprinklers) |
| **EN 50600-2-5 / ISO/IEC 22237-6** | Protection against internal environmental events (including water) |
| **ISO/IEC 27001 A.7.5** | Protecting against physical and environmental threats |
| **ANSI/TIA-942-C** | Facility provisions by rating |
| **ASHRAE guidance, OCP and vendor papers** | Liquid cooling leak detection and intervention (manual versus automatic) |
| **Manufacturer data (for example cable specifications)** | Sensitivity, location accuracy, fluids detected |

---

# 14.4 Notification system

## 4.1 Purpose

The notification system gets **the right alarm to the right person, through a channel that reaches them, in time**, and **closes the loop**:

```
Detect ─► Notify ─► Acknowledge ─► Respond ─► Resolve ─► Review
```

Detection without notification is a silent alarm. Notification without **filtering** is noise. And an alarm that **nobody owns** is not managed.

## 4.2 Alarm levels

Alarms are classed by the **consequence of ignoring them** and the **time available to respond**. Names and times are set in the **site alarm philosophy**, not by a standard.

| Level | Meaning | Example | Typical response expectation **[CHECK]** |
| --- | --- | --- | --- |
| **Information / event** | Awareness only, **no action required** | Generator weekly test started, scheduled maintenance | Logged, not annunciated as an alarm |
| **Warning (minor)** | Developing condition | Rack inlet 28 °C, filter differential pressure rising, one battery cell high impedance | Review within hours |
| **Major** | Degradation with redundancy still intact | CRAH fan fault with N+1 available, UPS module fault, a leak in a zone | Prompt response, minutes |
| **Critical** | Immediate threat to service or safety | Loss of cooling in a zone, **UPS on battery**, **fire**, **leak near live equipment**, rapid temperature rise | **Immediate**, 24/7 on-call |

**Awareness-only items belong in events and logs, not in the alarm stack**, or operators learn to ignore the board.

## 4.3 Channels

| Channel | Strength | Weakness |
| --- | --- | --- |
| **On-site sounder, beacon and wall display** | Immediate for whoever is present | Nobody on an empty site |
| **Dashboards and NOC screens** | Overview, context | Needs someone looking |
| **E-mail** | Detail, record | **Delays**, easily missed at 2 a.m. |
| **SMS** | Reaches a phone anywhere | Short, can be delayed, no guaranteed acknowledgement |
| **Voice call (text-to-speech)** | Hard to ignore, supports acknowledgement | Needs an answered phone |
| **Mobile app push** | Rich, acknowledgement button | Needs data and the app |
| **Pager** | Reliable coverage in some regions | Declining |
| **SNMP trap, syslog, webhook** | Feeds other systems automatically | Machine only |
| **Relay (dry contact) outputs** | Simple signal to another system, hardwired | One bit of information |
| **Chat tools (Teams, Slack)** | Team awareness | Not a primary channel |
| **ITSM ticket (ServiceNow and similar)** | Tracking, accountability, audit | Not immediate |

**Use several channels at the same time for critical alarms**: for example SNMP trap, e-mail, SMS and a voice call. Do not rely on one.

### Notification path reliability

| Measure | Detail |
| --- | --- |
| **Out-of-band path** | A **cellular** modem or gateway so alarms get out when the primary network or internet is down |
| **Edge buffering** | Remote units store events during a network break and forward them when it returns |
| **Power** | Protected power for gateways and servers |
| **Redundant servers and gateways** | No single notification server |
| **Heartbeat ("dead-man") tests** | A regular test message proves the chain works. **Alarm if the heartbeat stops** |
| **Test regularly** | A scheduled real-world test (monthly) of each channel and the on-call numbers |
| **Content** | **What, where, how severe, when, what to do**, and a link to the procedure. Avoid sensitive data in SMS |
| **Audit log** | Every alarm, notification, acknowledgement and closure recorded |

## 4.4 Escalation and on-call

```
Alarm ─► L1 (NOC / operator) acknowledges within T1
            │ no acknowledgement
            ▼
        L2 (on-call engineer) within T2
            │ no acknowledgement or not resolved
            ▼
        L3 (manager, specialist, vendor under SLA) within T3 ─► customers, management, authorities informed
```

| Element | Practice |
| --- | --- |
| **Acknowledgement required** | The alarm stays escalating until a person accepts it |
| **Timers** | Set in the philosophy (for example 5, 15 and 30 minutes), **after a consequence review**: do not copy another site's times |
| **24/7 rota** | Named on-call staff for critical and major alarms, with a published schedule and handover |
| **Backups for people** | If the person does not answer, the next one is called |
| **Vendor call-out** | Contracted response times, a direct route for generator, UPS and chiller faults |
| **Customer notification** | In colocation, tenants are told according to the contract, often with a **status page** |
| **Regulatory notification** | **NIS2** requires staged notification of significant incidents: an **early warning within 24 hours**, an **incident notification within 72 hours** and a **final report within one month** **[CHECK]** |
| **Escalation is not a substitute for rationalisation** | Paging a flood still loses the root cause |

**Worked example: response time budget.** The monitoring system polls every **60 s**, notification takes **30 s**, and the on-call engineer answers after **5 minutes**:

```
Time to a human response = 60 + 30 + 300 = 390 s = 6.5 minutes (before any travel time)
```

A rate-of-rise alarm and a shorter poll can save minutes when the room heats at several kelvin per minute.

## 4.5 Alarm management (ISA-18.2, IEC 62682, EEMUA 191)

Alarm management is a **discipline**, not just a configuration. **ANSI/ISA-18.2** (2009, revised 2016), its international version **IEC 62682**, and the British guide **EEMUA 191** (4th edition) set out the **lifecycle** and the **targets**.

### What an alarm is

An alarm is a signal that needs a **timely response** to avoid or reduce a consequence. **If there is no defined action and no time in which action would help, it is information, not an alarm.**

### The three tests of rationalisation

For every alarm, document:

1. There is a **real consequence** if it is ignored.
2. The operator has a **defined action** to take.
3. There is **enough time** to take it.

Alarms that fail are **removed, downgraded or re-engineered**. The result is a **master alarm database** (cause, consequence, response, setpoint, priority, time available).

### Benchmarks (per operator position) **[CHECK]**

| Measure | Target |
| --- | --- |
| **Average alarm rate (steady state)** | About **1 per 10 minutes** (6 per hour, about 150 per day). ISA-18.2 treats **2 per 10 minutes** (12 per hour) as the most an operator can manage |
| **Alarm flood** | **More than 10 new alarms in 10 minutes**. EEMUA 191 ends the flood when a 10-minute period has fewer than 5 new alarms. The system should spend **under 1% of the time in flood** |
| **Peak after an upset** | No more than about **10 alarms in the first 10 minutes** |
| **Standing alarms** | Fewer than about **10** |
| **Chattering alarms** | Essentially none |
| **Stale alarms** | Active for **more than 24 hours**: investigate |
| **Priority distribution** | About **80% low, 15% medium, 5% high** |

Systems measured for the first time are often **5 to 20 times above** these figures. A handful of "bad actor" alarms typically produce **40 to 80%** of the load.

The standard example of failure: at the **Texaco refinery in Milford Haven (1994)** two operators faced **275 alarms in the last 11 minutes** before an explosion, almost all irrelevant to the developing fault.

### Techniques

| Technique | What it does |
| --- | --- |
| **Deadband (hysteresis)** | The value must move back by a margin before the alarm clears, so it does not chatter |
| **On-delay and off-delay** | The condition must persist for a set time before the alarm activates |
| **Rate-of-change alarms** | Catch a fast rise before the absolute threshold |
| **Multi-level thresholds** | Advisory, warning, critical, so staff are warned earlier without a flood |
| **Grouping and first-out** | In a cascade (power dip, cooling trip) show the **root cause first** and suppress the consequences |
| **State-based suppression (suppressed by design)** | Automatically hide alarms that are meaningless in a given mode (for example during planned maintenance) |
| **Shelving** | A **time-limited, operator-controlled** suppression that un-shelves automatically |
| **Out of service** | Formally disabled **with management approval** |
| **Rationalisation workshop** | Operators, facilities and controls engineers review each alarm |
| **Alarm philosophy and management of change** | Documents the rules, and every new alarm goes through them |
| **KPIs and review** | Monthly review of rate, floods, chattering, stale and top contributors |
| **HMI design (ISA-101)** | Colour, layout and consistency so alarms stand out |

Shelved, suppressed-by-design and out-of-service alarms **behave differently in an audit**: do not collapse them into one "silenced" state.

### Worked example 1: counting floods

Alarm counts per 10-minute block over 50 minutes: **2, 3, 12, 25, 7**:

```
Blocks over 10 alarms: 12 and 25 → 2 blocks = 20 minutes in flood
Time in flood = 20 / 50 = 40%   (target: under 1%)
```

### Worked example 2: a cascade

A **UPS-on-battery event** triggers **120 alarms in 3 minutes** (UPS, ATS, PDU, rack PDU, every server UPS-input alarm). With grouping and first-out the operator sees **3 alarms**: the root cause (utility failure), the UPS state and the generator start. The rest stay in the log.

### Worked example 3: chatter and deadband

A temperature alarm at **27.0 °C** with a sensor oscillating between **26.9 and 27.1 °C** every 20 s:

```
Without deadband: 3 alarms per minute = 180 per hour
With a 1 °C deadband (clears at 26.0 °C) and a 30 s on-delay: 0 repeat alarms
```

### Worked example 4: priority distribution

200 configured alarms at **80/15/5**:

```
Low 160, medium 30, high 10
```

If **40% are high priority**, the priorities have lost their meaning: when everything is urgent, nothing is.

## 4.6 Notifying people on site

| System | Detail |
| --- | --- |
| **Fire alarm** | Sounders, beacons, voice evacuation (Module 12, **EN 54-3, NFPA 72**) |
| **Gas release** | Pre-discharge alarms and warning lamps (12.6) |
| **Security and panic alarms** | Control room and guards (Module 13) |
| **Public address and mass notification** | For evacuation and emergency instructions |
| **Local sounders and beacons for environmental alarms** | A visible and audible cue in the hall or NOC |

## 4.7 Common mistakes

- **Alarm floods** with no first-out or grouping.
- **Awareness messages** mixed into the alarm list.
- **One channel only.**
- **Alarms to an unattended mailbox.**
- **No escalation** if nobody answers.
- **Copied escalation times.**
- **No test** of the notification path (the number changed, the SMS credit ran out).
- **No owner** for an alarm that three systems report.
- **Silencing instead of fixing** the root cause.

## 4.8 Standards

| Standard | Contribution |
| --- | --- |
| **ANSI/ISA-18.2, IEC 62682** | Alarm management lifecycle and metrics |
| **EEMUA 191** | Alarm system design, management and procurement targets |
| **ISA-101** | Human-machine interface for alarms |
| **NFPA 72, EN 54-3** | Fire alarm notification |
| **NIS2** | Incident notification timelines |

---

# 14.5 Equipment and components monitoring

## 5.1 Principle

**Monitor what you can act on.** Every point should support a decision: an alarm, a capacity figure, an efficiency measure, a maintenance action. Points are organised in a hierarchy: **site → system → equipment → component**.

| Level | Example |
| --- | --- |
| **Site** | Utility feed, total power, PUE |
| **System** | The UPS system, the chilled water loop |
| **Equipment** | UPS module 2, chiller 3 |
| **Component** | One battery cell, one pump bearing, one fan |

## 5.2 The power chain

| Equipment | What to monitor |
| --- | --- |
| **Utility feed** | Voltage, frequency, power quality events, outages, import energy |
| **MV and LV switchgear** | Breaker position and trips, temperature, load, (partial discharge on MV), **thermography** of connections (6.47) |
| **Transformers** | Winding and oil temperature, load |
| **Generators** | **Fuel level and quality, oil level, oil pressure, coolant level and temperature (standby and running), start battery voltage and charger**, run status, engine speed, load, output voltage, current and frequency, **vibration**, exhaust temperature, emissions, number of starts and **run hours** |
| **ATS and STS** | Position, source availability, transfer events and times |
| **UPS** | Load (kW and %), input and output voltage and current, **battery status, charge, remaining runtime, time on battery**, temperature, **bypass state**, alarms, module status, efficiency and operating mode (6.38) |
| **Batteries** | **Cell or block voltage, temperature, internal resistance, impedance or conductance (trended against a baseline)**, string current, float voltage and charger state, **off-gas** for lithium-ion (Module 12) |
| **PDUs, RPPs and busway** | **Current per phase**, voltage, kW, kVA, power factor, harmonic distortion, breaker status, **branch circuit** loading |
| **Rack PDUs** | Per-phase current, **outlet-level** power and energy (essential for colocation billing), temperature |
| **Energy meters** | kWh at main points (for PUE and billing) |

### What to alarm on in the power chain

| Condition | Why |
| --- | --- |
| **UPS on battery, battery low, bypass active** | Protection reduced |
| **Generator not in auto, fuel low, start battery weak, failed test** | Backup not ready |
| **Breaker trip, circuit near its limit** | Capacity and outage risk |
| **Phase imbalance** | Hidden overload of one phase |
| **Loss of redundancy** (A/B path state) | Single point of failure exposed |
| **Battery impedance rising** | End of life approaching |

## 5.3 The cooling plant

| Equipment | What to monitor |
| --- | --- |
| **Chillers** | Run status and alarms, **compressor current**, evaporator and condenser pressures, supply and return water temperature, **approach temperature**, efficiency (kW per ton), refrigerant leak detection |
| **Pumps** | Status, **flow, differential pressure, vibration, bearing temperature**, drive speed and fault |
| **Cooling towers and dry coolers** | Fan status, **basin level**, water temperatures, **conductivity and blowdown**, vibration, water consumption (Module 10) |
| **CRAH and CRAC units** | **Supply and return temperature, fan speed, valve position**, **filter differential pressure**, condensate pump, humidifier, unit alarms |
| **Chilled water loop** | Flow, supply and return temperature, differential pressure, **tank level and temperature** (thermal storage), valve positions |
| **Free cooling and economisers** | Mode, damper and valve positions, outside temperature, dew point |
| **Liquid cooling** | **CDU supply and return temperature, flow, differential pressure, coolant quality and conductivity, filter differential pressure, pressure**, leak sensors, TCS and FWS temperatures (9.15) |
| **Humidity and dew point** | Room and supply air |
| **Differential pressure** | Under-floor and across containment |

### Worked example 1: cooling delivered

Chilled water flow is **30 L/s** (30 kg/s), supply **7 °C**, return **13 °C**:

```
Q = ṁ × c × ΔT = 30 × 4.186 × 6 = about 754 kW
Rated capacity 800 kW → capacity factor = 754 / 800 = 94%
```

A capacity factor that falls over time, with the same flow and ΔT method, reveals **fouling or degradation** (chiller, pump or heat exchanger).

### Worked example 2: approach temperature

A chiller's leaving water is **7 °C** and the evaporating refrigerant is at **4 °C** (approach **3 K**). Later the evaporating refrigerant is at **2 °C** (approach **5 K**):

```
Increase = (5 − 3) / 3 = 67%   → the evaporator tubes are fouling: schedule cleaning
```

## 5.4 Environment and air (cross-reference 14.1)

| Point | Detail |
| --- | --- |
| **Rack inlet temperature** | Top, middle, bottom (the key reading) |
| **Dew point and humidity** | Co-located |
| **Supply and return air** at cooling units | Cooling unit performance |
| **Differential pressure** | Floor to room, cold to hot aisle |
| **Hot aisle temperature** | Containment integrity |
| **Rate of change** | Early warning |

Threshold examples (set from the equipment class and manufacturer): inlet **warning at 27 °C** (the upper recommended limit) and **critical at about 32 °C** (the Class A1 allowable limit), **dew point** within **-9 to 15 °C** recommended **[CHECK]**.

## 5.5 Fire, security, safety and water systems

Monitor the **health** of the protection systems themselves, not only their alarms:

| System | What to monitor |
| --- | --- |
| **Fire alarm panel** | Normal, alarm, fault, **isolated or disabled zones**, power supply and battery |
| **Aspirating smoke detection** | Alert levels, **airflow fault, filter status**, sensitivity |
| **Gas suppression** | Cylinder pressure, **lockout valve position**, abort and manual release status, discharge indication, ready or trouble state |
| **Sprinklers** | Supervisory pressure, **valve tamper**, flow switches, pre-action panel trouble |
| **Oxygen reduction rooms** | Oxygen level, generator and sensor health |
| **Access control** | Door status, **forced and held-open** alarms, **controller offline**, battery, tamper |
| **CCTV** | **Camera offline, recorder and storage health**, tamper, time sync |
| **Intruder alarm** | Zone status, tamper, communication link |
| **Leak detection** | Zone status, cable and controller faults (14.3) |
| **EPO and emergency systems** | EPO status, emergency lighting test results, generator-backed lighting |

## 5.6 IT, network and optical monitoring

| Point | Detail |
| --- | --- |
| **Servers** | Management controller (Redfish, IPMI): **inlet temperature** (a built-in sensor network), fan speed, power, component health |
| **Network devices** | SNMP, flow, streaming telemetry, port errors, optical power (11.8) |
| **Storage and SAN** | Health, capacity |
| **Application and service level** | Latency, availability (synthetic checks) |
| **Correlation** | Link IT telemetry with the facility data: a server inlet alarm and a CRAH fault tell one story |

## 5.7 Condition-based and predictive maintenance

| Strategy | Basis | Strength | Weakness |
| --- | --- | --- | --- |
| **Run to failure** | Fix after it breaks | No effort | Unacceptable for the critical path |
| **Time-based (preventive)** | Fixed calendar or run-hour interval | Regulatory and warranty baseline | Blind to actual condition: replaces healthy parts and still misses fast degradation. Every task on a non-redundant path is a planned risk |
| **Condition-based (CBM)** | **A measured parameter crosses a threshold** | Service when needed | Needs sensors and baselines |
| **Predictive** | **Trends and models forecast failure** (P-F curve) | Plan work before failure | Needs history and expertise |

| Indicator | What it warns of **[CHECK]** |
| --- | --- |
| **UPS cell impedance up about 20% from baseline** | A weakening cell: run a capacity test |
| **Vibration RMS and bearing temperature rising (pumps, fans, chillers)** | Bearing wear, weeks before seizure |
| **Motor current signature** | Mechanical or electrical faults |
| **Approach temperature widening** | Fouled heat exchanger tubes |
| **Filter or strainer differential pressure rising** | Clogging |
| **Refrigerant charge trending down** | A leak |
| **Generator oil analysis, fuel and coolant quality, start reliability** | Wear, microbial fuel contamination (a classic no-start cause) |
| **Breaker and connection temperature (thermography)** | Loose or degrading connections (6.47) |
| **Harmonic and power quality trends** | Stress on distribution |
| **Cooling margin falling with no single alarm** | Gradual multi-unit degradation |
| **PUE rising with stable IT load** | Cooling or distribution degradation |

**Data needed:** baselines (including seasons), at least a year of history, maintenance records (CMMS), failure history and the operating context. Vendors claim AI models can flag some faults **14 to 30 days** early; treat that as a vendor claim **[CHECK]**.

Generators are a **readiness** problem: they spend most of their life not running and must start once. **Test runs (weekly or monthly)** under load, with the engine, voltage, frequency and start time logged, are both maintenance and a health check (light loads cause "wet stacking").

## 5.8 Data handling

| Topic | Practice **[CHECK]** |
| --- | --- |
| **Sampling and retention** | Seconds for control and critical alarms, 1 to 5 minutes for trends, about 15 minutes for energy, with raw data kept for months and summaries for years |
| **Time and naming** | NTP, one asset ID, location and point naming standard |
| **Points list** | Source, unit, scaling, interval, plausibility limits, alarm settings for each point |
| **Thresholds** | Documented basis (ASHRAE class, manufacturer, standard) and owner |
| **Sensor health** | Alarm on **stale or missing data** (a sensor that stops reporting is a fault), watchdogs, calibration schedule |
| **Baselines** | By season and redundancy state |
| **Change control** | New equipment adds points, owners and alarm rationalisation before go-live |
| **Reporting** | Dashboards and reports for operations, management and customers |

### Key performance indicators

| KPI | Meaning |
| --- | --- |
| **PUE** (and component metrics) | Efficiency, with its boundary and period stated |
| **Availability, MTBF, MTTR** | Service reliability |
| **Cooling and power capacity margin** | Installed, available, redundant and committed capacity |
| **Mean time to acknowledge and to resolve** | Operations performance |
| **Alarm KPIs** | Rate, floods, chattering, stale and standing alarms (14.4) |
| **Rack inlet compliance** | Share of racks in the recommended range |
| **Maintenance KPIs** | Planned versus unplanned work, test completion |

### Worked example: generator fuel monitoring

A **1,500 kW** generator at about 0.26 L/kWh with a **20,000 L** tank:

```
Consumption = 1,500 × 0.26 = 390 L/h
Autonomy    = 20,000 / 390 = about 51 hours
Low-fuel alarm at 50% (10,000 L) → 10,000 / 390 = about 26 hours left (well above the 12-hour Uptime minimum)
```

### Worked example: PDU phase loading

A **32 A** three-phase PDU shows **28 A, 15 A and 12 A**:

```
Average = (28 + 15 + 12) / 3 = 18.3 A
Imbalance = (28 − 18.3) / 18.3 = 53%
80% limit = 0.8 × 32 = 25.6 A → phase L1 at 28 A is over the limit although the total looks acceptable
```

Per-phase monitoring catches what a total hides (6.17 in `06-2`).

## 5.9 Common mistakes

- Monitoring **alarms but not readings** (no trends, no baseline).
- **No health monitoring of the protection systems** (a closed lockout valve, a disabled detector zone).
- Monitoring **only the UPS** and not the **batteries** (cell-level).
- **Generators watched only when running.**
- **Total power** without **per-phase** or **per-circuit** data.
- **No stale-data alarm**: a dead sensor looks like "normal".
- **Points with no owner or response.**
- **Maintenance records separate from monitoring data.**

## 5.10 Standards

| Standard | Contribution |
| --- | --- |
| **ISO/IEC 30134-2, EN 50600-4-2, The Green Grid metering levels** | PUE and the meter locations |
| **EN 50600-2-6, ISO/IEC TS 22237-7** | Management and operational information |
| **ASHRAE TC 9.9** | Thresholds and sensor placement |
| **NFPA 70B** | Electrical maintenance programmes and thermography (6.47) |
| **IEEE 450 and 1188, IEC 60896** | Battery inspection and testing (6.45) |
| **ISO 8528, NFPA 110** | Generator performance and testing |
| **ISO 55001** | Asset management **[CHECK]** |
| **IEC 62443** | Security of monitoring and control systems |

---

## Glossary

| Term | Meaning |
| --- | --- |
| EMS (this module) | Environmental Monitoring System: sensors and alarms for room conditions |
| Energy Management System | Another meaning of "EMS": aggregates energy data (ISO 50001) |
| BMS / BAS | Building management (automation) system: controls and monitors plant |
| EPMS | Electrical power monitoring system |
| SCADA | Supervisory control and data acquisition |
| DCIM | Data centre infrastructure management: assets, capacity, change, energy |
| DDC / PLC | Direct digital controller / programmable logic controller |
| BACnet | Building automation protocol (ANSI/ASHRAE 135, ISO 16484-5) |
| Modbus | Serial or IP protocol for meters, UPS and controllers |
| SNMP | Simple Network Management Protocol: polling and traps |
| OPC UA / MQTT / Redfish | Supervisory data exchange / light IoT messaging / server management API |
| OT | Operational technology (control networks) |
| IEC 62443 | Industrial control system security (zones and conduits) |
| Dew point | Temperature at which air saturates: the humidity measure |
| Rate-of-change alarm | Alarms on how fast a value moves |
| Differential pressure | Pressure difference across floor, containment or filter |
| Asset register | Record of equipment, location and attributes |
| Stranded capacity | Capacity allocated but unused |
| PUE metering levels 1, 2, 3 | IT energy at UPS output, PDU output, IT input |
| Spot sensor / sensing cable | Point leak sensor / continuous leak cable |
| Location cable | Leak cable that reports distance (about ±4%) |
| Hydrocarbon cable | Cable that detects fuel and oil, not water |
| Zone | A section of leak cable or monitored area reported separately |
| Automatic isolation valve | Valve closed by the leak controller |
| Alarm philosophy / master alarm database | Rules for alarms / record of every alarm and its response |
| Rationalisation | Reviewing each alarm against consequence, action and time |
| Alarm flood | More than 10 new alarms in 10 minutes |
| Chattering / stale / standing alarm | Repeating / active over 24 h / acknowledged but still active |
| Deadband / on-delay | Margin before clearing / time condition must last before alarming |
| Shelving / suppressed by design / out of service | Time-limited suppression / automatic state-based hiding / formally disabled |
| First-out | The first alarm in a cascade (root cause) |
| Escalation | Passing an unacknowledged alarm to the next level |
| Out-of-band | A separate path (such as cellular) independent of the main network |
| Heartbeat | Regular test message proving a path works |
| CBM / predictive maintenance | Condition-based / trend-based maintenance |
| P-F curve | Interval between a detectable potential failure and functional failure |
| CMMS | Computerised maintenance management system |
| ITSM / CMDB | IT service management / configuration management database |
| NTP | Network time protocol |

## Exam takeaways

**14.1 (challenges and requirements)**

- **Challenges:** many **protocols and vendors**, **silos** (same alarm on three systems), **data volume**, **alarm floods**, **sensor placement and drift**, **data quality**, **OT cybersecurity**, **monitoring as a single point of failure**, **asset records that drift**, no clear **ownership**.
- **Requirements:** measure at the **server inlet** (top, middle, bottom, **every rack in dense rows, every other or every third in uniform rows**), **dew point**, **±0.5 °C accuracy**, **rate-of-change alarms (20 °C per hour; tape 5 °C per hour)**, **multi-level thresholds**, **matched sampling intervals (seconds, minutes, 15 minutes)**, **retention of readings**, **redundant, UPS-powered monitoring with an out-of-band path and edge buffering**, **NTP**, **open protocols**, **hardwired safety loops**.
- **Power is the leading cause of impactful outages** (Uptime).

**14.2 (EMS, BMS, DCIM)**

- **EMS (environmental)** = sensors and alarms for room conditions. **BMS** = **controls** building plant (**BACnet**, 1 to 10 s, facilities). **DCIM** = **assets, capacity, change, energy** (SNMP/Modbus/BACnet, 1 to 5 min, rack level, **not real-time control**). **EPMS** = power chain and event analysis. "EMS" can also mean **Energy Management System** (ISO 50001).
- **One master per device**, **one owner per alarm**, **a source of truth** per data point, **open protocols**, **hardwired safety loops**. **BACnet = ASHRAE 135 = ISO 16484-5.**
- **DCIM capacity: power, cooling, space, network, weight.** The **smallest headroom limits deployment.** **Stranded capacity = allocated − measured.** **Asset survey first; wrong data is worse than none.**
- **PUE = total facility ÷ IT energy.** **Meter levels 1 (UPS output), 2 (PDU output), 3 (IT input).** **Compare only at the same level, boundary and period.** **Rising PUE with stable load = degrading cooling.**
- **IEC 62443 zones and conduits; BMS and EPMS are OT.**

**14.3 (water leak detection)**

- **Sources:** chilled water, CRAH **condensate**, humidifiers, overhead pipes, roof, plant, battery acid, fuel, **liquid cooling**.
- **Sensors:** **spot** (known points), **sensing cable** (continuous), **location cable (±4%)**, **hydrocarbon cable (fuel)**, **acid-resistant cable (batteries)**, **optical (dielectric fluids)**, flow and pressure sensors. **Glycol–water conducts; diesel does not.**
- **Follow the pipes**, short labelled zones, spot sensors in every CRAH pan, drip trays overhead, quick-disconnects and CDU bases in liquid cooling, **cross-aisle cable every 4 to 6 m** as a start.
- **Controller → BMS/DCIM → notification → response.** **Automatic isolation valve** is fast but must consider **cooling redundancy** and false alarms. **Test end to end at least quarterly.** NFPA 75 requires **leak removal**.

**14.4 (notification)**

- **Detect → notify → acknowledge → respond → resolve → review.** **Levels:** information (log only), warning, major, critical. **Several channels at once** (SNMP, email, SMS, voice), **out-of-band cellular**, **heartbeat tests**, **audit log**.
- **Escalation matrix with timers**, **24/7 on-call**, vendor call-out, customer and **NIS2 (24 h, 72 h, one month)** notifications.
- **ISA-18.2 / IEC 62682 / EEMUA 191:** an alarm needs an **action and time**. **Targets: about 1 alarm per 10 minutes per operator, flood = more than 10 in 10 minutes, under about 10 standing, priority 80/15/5.** **Deadband, on-delay, rate alarms, grouping and first-out, shelving vs suppressed by design vs out of service.** **Rationalisation tests: consequence, action, time.**

**14.5 (equipment and components)**

- **Power:** utility, switchgear, transformers, **generators (fuel, oil, coolant, start battery, test runs)**, ATS, **UPS (battery status, runtime, bypass)**, **cell-level battery data (impedance trending)**, **per-phase and per-circuit PDU data**, outlet-level for billing.
- **Cooling:** chillers (approach, kW/ton), pumps (flow, DP, vibration), towers (basin, conductivity), CRAH (supply/return, valve, filter DP), liquid cooling (CDU flow, DP, coolant quality). **Cooling delivered = flow × ΔT.**
- **Monitor the protection systems' health** (lockout valve, disabled zones, camera offline).
- **Maintenance strategies:** time-based, **condition-based**, **predictive**. **UPS cell impedance +20%**, **vibration**, **approach temperature**, **filter DP**, **refrigerant charge**, **oil analysis**. **Stale-data alarms.**

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **ASHRAE TC 9.9** *Thermal Guidelines* (5th edition) and the **LBNL** *Thermal Guidelines and Temperature Measurements in Data Centers* (2020) | Sensor placement at the inlet (top, middle, bottom), every other or every third rack, rate-of-change limits |
| **ANSI/ASHRAE 135 = ISO 16484-5** (BACnet) | Building automation protocol |
| **ISO/IEC 30134-2 = EN 50600-4-2**, **The Green Grid White Paper 49** and the **US DOE Data Center Metering and Resource Guide** | PUE definition, metering levels 1 to 3, continuous metering |
| **EN 50600-2-6**, **ISO/IEC TS 22237-7** | Management and operational information |
| **ISO 50001** | Energy management systems |
| **IEC 62443** | Security of industrial control systems, zones and conduits |
| **ANSI/ISA-18.2** (2016), **IEC 62682**, **EEMUA 191** (4th edition), **ISA-101** | Alarm management lifecycle, benchmarks and HMI |
| **NFPA 75**, **EN 50600-2-5 / ISO/IEC TS 22237-6**, **ISO/IEC 27001 Annex A.7** | Leak removal, environmental events, physical and environmental controls |
| **NIS2 Directive (EU 2022/2555)** | Staged incident notification (24 hours, 72 hours, one month) |
| **NFPA 72, EN 54-3** | Fire alarm notification |
| **NFPA 70B**, **IEEE 450 and 1188**, **ISO 8528**, **NFPA 110** | Maintenance, battery testing, generator tests |
| **Uptime Institute** *Annual Outage Analysis* (2025 and 2026) | Leading causes of impactful outages |
| **OCP / Vertiv** *Leak Detection and Intervention* white paper and manufacturer leak detection guidance (2026) | Liquid cooling leak detection, manual and automatic intervention, sensor types and placement |
| Industry guidance on EMS, BMS, EPMS and DCIM, predictive maintenance and alarm rationalisation (2026) | Roles, protocols, refresh rates, integration rules, failure indicators |
| Standard thermodynamics and statistics | Cooling delivered (Q = ṁ c ΔT), PUE, imbalance, data volume and alarm-rate calculations |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
