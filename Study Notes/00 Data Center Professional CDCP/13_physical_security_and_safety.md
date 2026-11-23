# Module 13: Physical Security and Safety

Detailed notes, following the lesson-level index of the EPI course. The practice questions for this module are in [00_knowledge_tests.md](00_knowledge_tests.md#module-13-physical-security-and-safety).

| Lesson | Title | Section |
| --- | --- | --- |
| 13.1 | Physical Security Considerations | [Section 1](#131-physical-security-considerations) |
| 13.2 | CCTV Cameras / Video Surveillance System (VSS) | [Section 2](#132-cctv-cameras--video-surveillance-system-vss) |
| 13.3 | Entry Control | [Section 3](#133-entry-control) |
| 13.4 | Physical Safety Considerations | [Section 4](#134-physical-safety-considerations) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-13-physical-security-and-safety) |

**Objectives (from your slide).** After this module you should be able to describe and understand:

- The components for physical security
- The components for physical safety

| Objective | Where it is covered |
| --- | --- |
| **Components for physical security** | 13.1 (layers, perimeter, building, people, rack), 13.2 (video surveillance), 13.3 (entry control) |
| **Components for physical safety** | 13.4 (hazards, electrical, batteries, handling, noise, heat, chemicals, emergency arrangements) |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Only the **objectives slide** was available for this module (not the lesson slides), so check the glossary and figures against your course. Related earlier material: site selection and building (Module 3), rack locks (8.3 in `08_equipment_racks.md`), fire protection and gas rooms (Module 12), emergency lighting (Module 5), batteries (6.44 and 6.45 in `06-4`), earthing and bonding (6.26), electromagnetic fields (Module 7), cooling and hot aisles (Module 9).

## Security and safety: two different questions

| | **Physical security** | **Physical safety** |
| --- | --- | --- |
| **Question** | How do we stop **people who should not be here, or who intend harm**, reaching the equipment? | How do we stop **people who are here legitimately** (and the facility) coming to **harm** through accidents and hazards? |
| **Threats** | Theft, intrusion, sabotage, insider misuse, vehicle attack, espionage | Electric shock, arc flash, falls, lifting injuries, noise, heat, chemicals, fire, gas |
| **Main tools** | Zones, perimeter, entry control, video, alarms, guards, procedures | Risk assessment, safe systems of work, protective equipment, training, emergency arrangements |
| **Conflict** | Locked doors keep people out | **People must always be able to get out**: egress and life safety come first |

Both start from a **documented risk assessment** and both rely on **layers**, **procedures** and **trained people**, not on equipment alone.

---

# 13.1 Physical security considerations

## 1.1 Why physical security matters

Cyber defences assume the hardware is untouched. **Physical access defeats them.** A server in a rack holds the data, the credentials in its management controller, the encryption keys in memory and the hardware itself, which can be removed and analysed offline. A few minutes of unmonitored access to a rack can achieve more than months of network attack.

| Reason | Detail |
| --- | --- |
| **Theft** | Equipment, drives, cabling (copper), media |
| **Tampering and implants** | Rogue devices, altered hardware, extra network taps |
| **Sabotage and vandalism** | Deliberate outages, damage to power and cooling |
| **Insider misuse** | Staff, contractors and visitors with legitimate access |
| **Availability** | A security incident is also an outage |
| **Compliance and trust** | ISO/IEC 27001, SOC 2, PCI DSS, HIPAA, NIS2 and customer audits all test physical security |
| **Insurance** | Insurers expect documented protection |

## 1.2 Threats and the risk assessment

| Threat | Examples |
| --- | --- |
| **Theft and intrusion** | Opportunistic or planned break-in, copper theft |
| **Insider threat** | Malicious or careless employees, contractors, cleaners |
| **Social engineering and tailgating** | Following an authorised person through a door, posing as a technician or delivery driver |
| **Vandalism and sabotage** | Cutting cables, tripping the emergency power-off, damaging plant |
| **Hostile vehicle** | Ramming a gate, wall or loading dock |
| **Terrorism and espionage** | Targeted attack, reconnaissance, surveillance of procedures |
| **Drones** | Surveillance of the site, or a delivery of a harmful payload |
| **Supply chain** | Tampered equipment in delivery, compromised contractors |
| **Environmental events** | Fire, flood, power failure (they also defeat security systems) |

**Risk assessment.** **EN 50600-2-5** requires a **documented risk analysis** to set the protection level, in the same way as NFPA 75 does for fire:

```
Risk = likelihood × impact      for each asset and threat, then choose controls to reduce it to an accepted level
```

Steps: list the **assets** (data, equipment, people, reputation), the **threats**, the **vulnerabilities**, rate the **likelihood and impact**, select **controls** (avoid, reduce, transfer, accept, as in Module 1), record the **residual risk**, and review it after every change.

## 1.3 Principles of physical security

| Principle | Meaning |
| --- | --- |
| **Defence in depth (layers)** | Several **independent** controls in sequence, so defeating one leaves the others. **Each layer must be independently auditable and testable**: a control that silently depends on another is not a real extra layer |
| **Deter, detect, delay, respond** | **Deter** (visible controls), **detect** (alarms, cameras), **delay** (barriers, locks), **respond** (guards, police). Delay must last longer than detection plus response |
| **Concentric zones** | Each step from the boundary to the rack **adds a control** and **reduces the number of people authorised** |
| **Least privilege / need to know** | People get access only to the areas and times they need |
| **Separation of duties and two-person rule** | Critical actions need two people (for example access to the most sensitive cage) |
| **Fail-safe and fail-secure by design** | Escape routes **fail safe** (open) so people can leave. Other doors **fail secure** (stay locked) where code permits |
| **No single point of failure** | Security systems need **backup power**, redundant paths and fallback procedures (a power cut must not open or disable everything) |
| **Auditability** | Every access, alarm and change is logged and reviewed |
| **Low profile** | No signs advertising the building's use, anonymous appearance |
| **CPTED** (crime prevention through environmental design) | Natural surveillance, clear lines of sight, controlled access routes, lighting, landscaping that does not hide intruders |
| **Integration** | Access control, video, intrusion alarms and fire systems work together, but each must still work if another fails |

## 1.4 Site and building design

(Site selection is in Module 3.)

| Feature | Why |
| --- | --- |
| **Low profile, no signage** | Does not advertise the target |
| **Setbacks and standoff distance** | Keeps vehicles and threats away from the building. Parking away from the walls |
| **Single controlled main entrance** | Everyone passes one staffed point |
| **No windows in the data hall; no critical rooms on exterior walls** | Removes visibility and attack routes |
| **"Six walls" rule** | A secure room is a barrier on **all six surfaces**: four walls, floor and ceiling, **slab to slab**. A partition that stops at a dropped ceiling is not secure |
| **Hardened doors and frames** | Doors, frames and locks matched to the attack resistance needed (burglar resistance classes such as EN 1627 RC 1 to 6 **[CHECK]**) |
| **Separated loading dock and staging** | Deliveries and unpacking happen **outside** the data hall |
| **Protected utility entries and roof** | Cable and pipe entries, roof hatches, fuel and generator yards are fenced and monitored |
| **Safe siting of critical rooms** | Not under water pipes, kitchens or plant (ISO 27001 A.7.8, NIST PE-18) |

## 1.5 Layers and zones

A common model has **five to seven zones**:

```
Public road → [perimeter] → site grounds → [building shell / reception] → support areas
            → [data hall entry, mantrap] → data hall → [cage or suite] → [rack / cabinet] → asset
```

| Layer | Typical controls |
| --- | --- |
| **Perimeter** | Fence or wall, gates, vehicle barriers, lighting, clear zone, intrusion detection, guardhouse |
| **Site and grounds** | Controlled parking, CCTV, patrols, access to plant yards restricted |
| **Building shell** | Hardened walls and doors, one entrance, staffed reception, visitor management |
| **Support and office areas** | Badge access, visitor escort |
| **Data hall entry** | Mantrap or interlocked doors, **two-factor** authentication (card plus PIN or biometric), anti-tailgating |
| **Data hall (white space)** | Access-controlled, CCTV on aisles, escorted visitors only |
| **Cage or suite** (colocation) | Six-sided mesh or solid cage, separate access control per tenant |
| **Rack / cabinet** | Locking cabinets, **electronic locks with logging** (8.3 in `08_equipment_racks.md`), door sensors, tamper-evident seals |
| **Asset** | Asset tags, media control, secure disposal |

### EN 50600-2-5 Protection Classes

**EN 50600-2-5:2021** (the security part of the European data centre series, with the international equivalent in **ISO/IEC TS 22237-6**) defines **four Protection Classes (1 to 4)**. Key points:

- A Protection Class is assigned **to a space**, not to the whole site. A site is made of **"protection class islands"** (for example a lobby, a staging area, a data hall) with different classes.
- Classes are set **separately for each aspect**: **unauthorised access**, **intrusion**, **fire**, **internal environmental events** and **external environmental events**.
- The class is **chosen from the risk analysis**, independently of the availability class (Module 2).
- A higher class means **more demanding controls**. As a guide, from Protection Class 3 upward **two-factor authentication** is expected at the data hall, and Protection Class 4 adds **cabinet-level two-factor access with event logging, tamper-evident sealing and anti-tailgating controls** **[CHECK]**.

## 1.6 The perimeter

| Element | Detail |
| --- | --- |
| **Fence or wall** | A typical minimum of about **2.4 m (8 ft)** with an **anti-climb** design. Welded **358 mesh** (small apertures that prevent climbing and cutting) or palisade for high security. Anti-climb toppings add height |
| **Delay rating** | **LPS 1175** (UK, recognised widely) grades fences and gates by the time they resist forced entry with tools. The certificate applies to the **tested configuration only**: change the height or posts and it no longer applies |
| **Gates** | Must match the **fence's rating**, otherwise the gate is the weak point |
| **Perimeter intrusion detection (PIDS)** | Fence-mounted vibration or fibre-optic sensors, taut wire, buried cable, radar, thermal cameras. Feeds the same platform as CCTV and access control |
| **Lighting** | Illuminates the fence line, gates and building so cameras and guards can see |
| **Clear zone** | An open strip inside and outside the fence with no cover for intruders |
| **Guardhouse and gate control** | A staffed gatehouse for checking and recording vehicles and visitors |
| **Drone detection** | Radio-frequency, radar and video sensors, considered for high-risk sites |

### Vehicle barriers

A normal fence **does not stop a vehicle**. Where there is a vehicle threat, use **crash-rated barriers**, chosen from a **vehicle dynamics assessment** (approach routes, speed, angle, standoff).

| Standard | Notes |
| --- | --- |
| **ASTM F2656** (US) | Crash-tests barriers. **M30** stops a **15,000 lb (6,800 kg) vehicle at 30 mph**, **M40** at 40 mph, **M50** at 50 mph. Ratings also report the penetration distance |
| **IWA 14-1** (international) | Combines elements of F2656 and PAS 68 |
| **PAS 68** (UK) | The UK impact test specification, largely superseded by IWA 14-1 and **ISO 22343** |
| **K4, K8, K12** | The **old** US State Department ratings, replaced by ASTM F2656 |

- **M30** suits sites where speed is naturally limited (tight turns, short runs). **M50** suits **long straight approaches** where speed can build.
- Typical pattern at a gate: a **crash-rated gate** plus an **active barrier** (such as a wedge) behind it. **Bollards** protect pedestrian edges and the dock face.
- **Ask for the original crash-test report** (product model, test body and date). Marketing names are not certification.
- UK guidance comes from **NPSA** (the National Protective Security Authority, which replaced CPNI in 2023).

### Worked example: detect, delay, respond

An intruder reaches the data hall only if the total **delay** exceeds the time to **detect, assess and respond**:

```
Detection        10 s
Assessment       30 s  (an operator verifies the alarm on video)
Response        180 s  (security reaches the location)
Time needed     = 220 s

Delay: fence 90 s + building door 120 s + cage 60 s = 270 s
Margin = 270 − 220 = 50 s   (the layers hold long enough)
```

The figures are illustrative. The point: **barriers only buy time, and the response must fit inside it**. If response takes 5 minutes (300 s), the same layers fail: add delay or shorten the response.

## 1.7 Intrusion detection, alarms and security operations

| Element | Detail |
| --- | --- |
| **Intruder alarm system** | Door contacts, motion detectors (PIR, dual-technology), glass-break, vibration sensors on walls, sensors in ceiling and floor voids. **EN 50131** grades systems **1 to 4** by risk, and data centres typically use **Grade 3 or 4** |
| **Panic and duress buttons** | At reception, guard posts and sensitive rooms |
| **Alarm verification** | **Video verification** by an operator before a response is sent, to cut false alarms |
| **Alarm transmission** | Resilient, supervised links to a **monitoring or alarm receiving centre** (EN 50136, EN 50518) |
| **Security control room or SOC** | Staffed 24/7 for monitoring alarms, video and access events, with procedures for each alarm |
| **Guards** | On-site patrols and gate or reception duty. Licensed where the law requires (for example by the Private Security Authority in Ireland) **[CHECK]**. **Post orders** and **patrol tours** recorded |
| **Integration** | Access control, video and alarm events in one platform so an alarm pops up the nearest camera |
| **Incident response** | Written procedures: who responds, who is called, how evidence is kept |
| **Power for security systems** | UPS and generator backup, so security keeps working in a power failure |

## 1.8 Visitors, vendors and deliveries

**Visitor, vendor and contractor access is the most common gap** in an otherwise well-built system.

| Control | Detail |
| --- | --- |
| **Pre-registration and ID check** | Named visitors, host approval, identity verified at reception |
| **Distinct, expiring badges** | Visibly different from staff badges, valid only for the visit, **escort required** |
| **Escort** | Visitors are never alone in the white space. The host is responsible |
| **Contractor vetting and induction** | Qualifications, method statement, safety and security briefing (13.4) |
| **Tools, devices and photography rules** | Inspect and log equipment brought in and out. Control cameras and removable media |
| **Delivery and removal control** | Deliveries arrive at the **dock and staging room**, outside the hall. Components entering and leaving are **authorised and recorded** (NIST PE-16), with **asset tags reconciled** at both ends |
| **Chain of custody** | Sealed, tracked equipment during moves, migrations and decommissioning |
| **Records** | Sign-in and sign-out, badge issue, delivery logs, retained and reviewed |

## 1.9 People: insiders and personnel security

| Control | Detail |
| --- | --- |
| **Background checks** | Where the law allows, for staff and contractors with access to sensitive areas |
| **Joiner, mover, leaver process** | Access granted, changed and **revoked on the same day**, linked to HR and contractor records |
| **Least privilege and periodic access reviews** | Remove orphaned and shared badges |
| **Separation of duties** | One person cannot both approve and use sensitive access |
| **Monitoring and audit** | Review logs and unusual access (after-hours, repeated denials) |
| **Awareness and training** | Tailgating, social engineering, reporting suspicious behaviour, challenge culture |
| **Reporting** | A no-blame route to report incidents and near misses |

## 1.10 Asset and rack security

| Control | Detail |
| --- | --- |
| **Locking cabinets** | Per-rack locks, electronic with audit trail (8.3 in `08_equipment_racks.md`) |
| **Cages** | Six-sided mesh or solid cages in colocation |
| **Tamper-evident seals and sensors** | On cabinets and equipment |
| **Port and media control** | Disable or block unused ports, control removable media and management interfaces |
| **Asset inventory** | Hardware location and custody tracked, **reconciled with racks at least yearly**, serial numbers of drives recorded |
| **Media sanitisation and secure disposal** | Drives wiped or destroyed to a standard (**NIST SP 800-88**) before reuse or disposal. Certificate of destruction |

## 1.11 Standards and frameworks

| Standard | What it contributes |
| --- | --- |
| **EN 50600-2-5:2021** and **ISO/IEC TS 22237-6** | Data centre security: Protection Classes 1 to 4, protection class islands, risk analysis, controls against unauthorised access, intrusion, fire and environmental events |
| **ANSI/TIA-942-C**, **Uptime Tier Standard** | Security provisions by rating |
| **ISO/IEC 27001:2022 Annex A.7** | **14 physical controls** (below). 93 controls in total across four themes |
| **NIST SP 800-53 (PE family)**, **NIST SP 800-116** | US physical and environmental controls, and PIV credentials in facility access |
| **EN 50131**, **EN 50136**, **EN 50518** | Intruder alarms (Grades 1 to 4), alarm transmission, alarm receiving centres |
| **EN/IEC 60839-11-1, -11-2, -11-5** | Electronic access control systems and OSDP (13.3) |
| **IEC 62676 series** | Video surveillance systems (13.2) |
| **ASTM F2656, IWA 14-1, PAS 68, ISO 22343, LPS 1175** | Vehicle barriers and fence delay ratings |
| **PCI DSS, SOC 2, HIPAA** | Customer and sector audit requirements |
| **NIS2 (EU Directive 2022/2555)** | Digital infrastructure providers must manage security risks, including physical. In force since 16 January 2023, transposition deadline 17 October 2024 |
| **ISO 31000** | Risk management |

### ISO/IEC 27001:2022 Annex A.7: the 14 physical controls

| Control | Title |
| --- | --- |
| A.7.1 | Physical security perimeters |
| A.7.2 | Physical entry |
| A.7.3 | Securing offices, rooms and facilities |
| A.7.4 | Physical security monitoring (**new in 2022**) |
| A.7.5 | Protecting against physical and environmental threats |
| A.7.6 | Working in secure areas |
| A.7.7 | Clear desk and clear screen |
| A.7.8 | Equipment siting and protection |
| A.7.9 | Security of assets off-premises |
| A.7.10 | Storage media |
| A.7.11 | Supporting utilities |
| A.7.12 | Cabling security |
| A.7.13 | Equipment maintenance |
| A.7.14 | Secure disposal or re-use of equipment |

---

# 13.2 CCTV cameras / video surveillance system (VSS)

## 2.1 What a video surveillance system does

| Purpose | Detail |
| --- | --- |
| **Deter** | Visible cameras discourage intrusion and misuse |
| **Detect and verify** | An operator sees what triggered an alarm, so the response is proportionate and false alarms fall |
| **Record evidence** | Footage for investigations, insurers and the police |
| **Direct the response** | Guards see where the incident is and who is involved |
| **Audit access** | Video backs up the access control log (who really went through the door) |
| **Monitor safety** | Spot a person down, a leak, smoke or an unsafe act |

### Components

```
Cameras (PoE) ─► PoE switches (security VLAN) ─► recording servers (VMS / NVR) ─► storage (RAID, retention)
                                                        │
                                  operator workstations, video wall, alarms, integration with access control
```

| Component | Role |
| --- | --- |
| **Cameras and lenses** | Capture the image. Chosen for the scene and the task |
| **Lighting** | White light, infrared or thermal for night |
| **Network** | PoE switches, on a **separate, segmented network** |
| **Video management software (VMS) and recorders (NVR)** | Record, search, export, manage cameras and users |
| **Storage** | Disk arrays sized for bitrate and retention |
| **Viewing** | Workstations and video walls in the security control room |
| **Analytics** | Motion, line crossing, loitering, counting, plate reading |
| **Integration** | With access control, intruder alarms, fire system and the monitoring platform |
| **Power** | UPS (and generator) so video keeps recording during a power failure |
| **Time source** | **NTP** so footage and access logs agree to the second |

## 2.2 Camera types

| Type | Description | Typical use |
| --- | --- | --- |
| **Fixed (bullet or box)** | One field of view, usually with a visible camera body | Entrances, corridors, fence lines. Good deterrent |
| **Dome (vandal-resistant)** | Camera in a dome, harder to see where it points | Indoor rooms and corridors. **IK10** rating for impact resistance |
| **PTZ** (pan, tilt, zoom) | Remote-controlled movement and zoom, can auto-track | Perimeter pursuit, large areas, **one per fence segment with overlapping coverage** at higher security levels |
| **Panoramic (multi-sensor, 180° or 360°)** | Several sensors in one housing | Corners, wide areas, gate approaches |
| **Thermal** | Images heat, not light | **Perimeter at night, fog and glare**, detection of people and vehicles at range |
| **Fisheye** | A single 360° view | Rooms, lobbies (needs dewarping) |
| **Low-light and licence plate (LPR)** | Optimised sensor and shutter | Gate vehicle entrances, plate reading |
| **Covert or miniature** | Small, hidden | Special situations, subject to law |

Selection points: **resolution**, **lens (focal length and field of view)**, **low-light performance**, **wide dynamic range (WDR)** for backlit doors, **IP rating** (dust and water) and **IK rating** (impact), **PoE class**, built-in **edge storage**, analytics, and **cybersecurity features** (secure boot, signed firmware, 802.1X, HTTPS).

## 2.3 Where to put cameras

Start from the **operational requirement** for each camera: what task must it support (see 2.4), not "cover the area".

| Location | Task | Notes |
| --- | --- | --- |
| **Perimeter, gates** | Detect people and vehicles, read plates | Thermal and PTZ, lighting, overlap so no gap |
| **Building entrance and reception** | **Identify** every person | Face height, front-lit, no backlight |
| **Mantraps and data hall doors** | **Identify** (inside both doors) | The strongest identification point |
| **Corridors** | Recognise a known person, follow movement | At corners and junctions |
| **Data hall aisles** | Observe people at the aisle ends and cage fronts | Cover **both ends of each row** |
| **Cages and suites** | Observe entry and activity | Per-tenant privacy rules |
| **Electrical, UPS, battery and generator rooms** | Observe entry and equipment condition | Also safety monitoring |
| **Loading dock and staging** | Identify people and record deliveries | Cover the door and the yard |
| **Fuel and plant yards, roof** | Detect intrusion | Thermal or low-light |
| **Parking** | Overview, plate capture | Away from the building |
| **Security control room, key cabinets** | Record access to security assets | |

General rules: no blind spots and **overlapping fields of view**, mount to avoid glare and backlight, protect cameras from tampering (high mounting, vandal housings, tamper alarms), **no cameras in toilets or private areas**, and **avoid audio recording** (often unlawful).

## 2.4 Image quality: pixel density (IEC 62676-4)

The standard that links **what you need to see** to **how many pixels fall on the subject**. It is based on a **human face about 16 cm wide**. **IEC 62676-4:2025** (second edition, October 2025, replacing the 2014 edition) defines seven levels, in **pixels per metre (px/m)** on the target:

| Level (2025) | Pixel density | Meaning (approximate) | Pixels across a 16 cm face |
| --- | --- | --- | --- |
| **Overview** | 20 px/m | General scene awareness | 3 |
| **Outline** | 40 px/m | A person or object is present | 6 |
| **Discern** | 80 px/m | What it is doing, whether it moves | 13 |
| **Perceive** | **125 px/m** | **Recognise** a known person or object | **20** |
| **Characterise** | **250 px/m** | **Identify** an individual by their features | **40** |
| **Validate** | 500 px/m | Verify a face against a known photograph | 80 |
| **Scrutinise** | 1,500 px/m | Detailed scrutiny, passport-grade capture | 240 |

Datasheets and design tools still use the **earlier four-level wording (DORI)**: **Detect 25, Observe 62.5, Recognise 125 and Identify 250 px/m**. The 125 and 250 values are the same in both. Values above are for **a human watching the image**: analytics and thermal cameras use different criteria **[CHECK]**.

### The formulas

```
Scene width (m) at distance d:   W = 2 × d × tan(HFOV / 2)
Pixel density (px/m)             = horizontal pixels / W
Scene width for a level          = horizontal pixels / required px/m
```

### Worked example: how wide a scene each camera can cover

Scene width at which each level is reached (horizontal pixels divided by px/m):

| Camera | Horizontal pixels | Characterise (250) | Perceive (125) | Discern (80) | Outline (40) | Overview (20) |
| --- | --- | --- | --- | --- | --- | --- |
| **1080p (2 MP)** | 1,920 | 7.7 m | 15.4 m | 24 m | 48 m | 96 m |
| **4 MP** | 2,688 | **10.75 m** | **21.5 m** | 33.6 m | 67.2 m | 134.4 m |
| **4K (8 MP)** | 3,840 | **15.4 m** | 30.7 m | 48 m | 96 m | 192 m |

**Megapixels mislead:** 4K has **four times** the pixels of 1080p but only **twice the width**, so with the same lens it identifies **twice as far**, not four times.

**Distance for the 4 MP camera (identification):**

```
Scene width = 2,688 / 250 = 10.75 m
Lens with 90° horizontal field of view:  d = W / (2 × tan 45°)  = 10.75 / 2    = about 5.4 m
Lens with 80° horizontal field of view:  d = 10.75 / (2 × tan 40°) = 10.75 / 1.68 = about 6.4 m
```

So for **identification at a door**, the camera must be within about **5 to 6 m** and look at the face. At **recognition** (125 px/m) the width doubles to 21.5 m (distance about 10.8 m for a 90° lens).

### Real-world factors

The density is a **best case**. Light direction, **backlight**, motion blur, focus, the **angle to the face**, compression and noise all cost detail. Treat 250 px/m as a **floor**, not a target, and add margin. Use the camera's **pixel counter** to check the real image at commissioning.

## 2.5 Light, motion and frame rate

| Factor | Practice |
| --- | --- |
| **Low light** | Larger sensors and wide apertures. **IR illuminators** for monochrome night images. **Thermal** where light is absent. A bigger sensor on 4 MP can beat a small-sensor 4K in the dark |
| **Backlight** | **WDR** at doors with bright outside light behind the person |
| **Shutter speed** | Fast enough to freeze motion, which needs light |
| **Frame rate** | Roughly 12 to 15 fps for general viewing, **25 to 30 fps at entrances** and fast action **[CHECK]** |
| **White light** | Gives colour images where light is permitted |

## 2.6 Network and storage

**Bitrate** depends on resolution, frame rate, scene activity and compression. **H.265** needs roughly **half the bitrate of H.264** for the same quality, and smart codecs cut it further for static scenes.

```
Storage per camera per day (GB) = bitrate (Mbps) × 10.8        (1 Mbps = 0.125 MB/s = 10.8 GB per day)
Total storage                   = per-day storage × cameras × retention days
```

### Worked example: storage and bandwidth

Cameras at **4 Mbps**, **100 cameras**:

```
Per camera per day = 4 × 10.8 = 43.2 GB
30 days: 43.2 × 100 × 30 = 129,600 GB = 129.6 TB
90 days: 43.2 × 100 × 90 = 388.8 TB
Motion-based recording (40% duty): 129.6 × 0.4 = about 51.8 TB for 30 days
RAID 6 on 8 disks (6 of 8 usable = 75%): raw capacity for 129.6 TB = 129.6 / 0.75 = 172.8 TB
Network load = 100 × 4 Mbps = 400 Mbps into the recorders
```

| Design point | Practice |
| --- | --- |
| **Segmentation** | Cameras and recorders on a **dedicated network or VLAN**, not the corporate LAN |
| **PoE** | 802.3af (15.4 W) for most fixed cameras, 802.3at (30 W) for PTZ and heaters |
| **Redundancy** | **Failover recorders**, **edge (SD card) storage** in cameras for network loss, redundant switches |
| **Power** | UPS and generator on the video system |
| **Time** | NTP on every device, so footage matches the access log |
| **Capacity headroom** | Allow for added cameras and higher bitrates |

## 2.7 Retention and the law

| Topic | Practice **[CHECK]** |
| --- | --- |
| **Retention period** | Commonly **30 to 90 days**. Some regimes (for example PCI DSS for cardholder areas) commonly call for **90 days or more**. Higher-security classes may specify 90 days for the data hall |
| **Data protection (GDPR and similar)** | CCTV records **personal data**: have a **lawful basis**, keep retention **proportionate** and documented, complete a **data protection impact assessment (DPIA)**, post **signs**, **limit who can view and export**, avoid **audio**, handle **subject access requests**, notify staff |
| **Biometrics and facial recognition** | **Special category data**: explicit consent or another legal basis, and strict controls |
| **Evidence handling** | Documented **export procedure**, hashing or watermarking, **chain of custody**, an audit log of who viewed or exported footage |
| **Local law** | Camera placement, signage and retention differ by country and by workplace rules |

## 2.8 Cybersecurity of the video system

Cameras are **networked computers** and a common way into a network.

| Risk | Control |
| --- | --- |
| **Default or shared passwords** | Unique strong credentials, no shared accounts |
| **Outdated firmware** | Patch management, signed firmware |
| **Exposed services and ports** | Disable unused services, no direct internet exposure |
| **Flat network** | Segmentation, 802.1X port security, firewall rules |
| **Unencrypted streams and management** | HTTPS and TLS, encrypted storage |
| **VMS server weaknesses** | Hardening, role-based operators, audit logs |
| **Vendor remote access left open** | Time-limited, logged access only |
| **Supply chain** | Buy from trustworthy vendors. In the **US**, **NDAA Section 889** bars certain manufacturers from federal procurement **[CHECK]** |
| **Interoperability** | **ONVIF** profiles help mix vendors, but check security support |

## 2.9 Monitoring and analytics

| Approach | Detail |
| --- | --- |
| **Recording only** | Footage is reviewed after an event (cheapest, slow) |
| **Live monitoring** | Operators watch the most critical views continuously |
| **Alarm-driven monitoring** | Alarms (door forced, intrusion, analytic) bring up the relevant camera for **verification** |
| **Analytics** | Motion, **line crossing**, loitering, object left behind, **people counting** (tailgating), **licence plate recognition**, thermal analytics, auto-tracking by PTZ |
| **Integration** | A door alarm opens the door camera, and each access event is tied to a video clip |
| **Limits** | Analytics produce false alarms and need tuning. Facial recognition has legal limits |

## 2.10 Maintenance and testing

| Activity | Detail |
| --- | --- |
| **Acceptance test** | Check each camera against its operational requirement: pixel density at the target, day and night, with the real lighting (IEC 62676-4) |
| **Health monitoring** | The VMS reports camera offline, stream loss, storage faults, tampering |
| **Routine** | Clean lenses and domes, check focus and field of view, test night mode and IR, check storage and retention |
| **Time check** | Verify NTP sync |
| **Review** | Review coverage after layout changes and after incidents |
| **Records** | Maintain a camera schedule: location, task, settings, serial number, firmware |

## 2.11 Common mistakes

- Cameras bought **without an operational requirement** (cannot say what each one must achieve).
- **Too high or too wide**: nobody is identifiable.
- **Backlit entrances** with no wide dynamic range.
- **Storage too small** for the retention promised.
- **Time not synchronised**.
- **Default passwords** and a flat network.
- **Nobody watching or reviewing**.
- Privacy law ignored (no DPIA, no signs, audio recorded).
- **Blind spots** at row ends, corners and doors.

## 2.12 Standards

| Standard | Contribution |
| --- | --- |
| **IEC / EN 62676** series | Video surveillance systems: system requirements, video transmission, interfaces, and **Part 4 application guidelines** (pixel density, design, commissioning) |
| **ONVIF** | Interoperability profiles |
| **IEC 60529 (IP) and IEC 62262 (IK)** | Dust and water, impact resistance |
| **GDPR and local law** | Privacy |
| **EN 50600-2-5, ISO/IEC 27001 A.7.4** | Physical security monitoring requirements |

---

# 13.3 Entry control

## 3.1 Purpose

**Entry control (access control)** decides **who may enter which area and when**, enforces it at the door, and **records** every attempt.

| Function | Meaning |
| --- | --- |
| **Identify and authenticate** | Establish who the person is (something they have, know or are) |
| **Authorise** | Check the person is allowed in **this area at this time** |
| **Enforce** | Unlock the door (and keep it locked otherwise) |
| **Record** | Log every access and alarm |
| **Alarm** | Report forced or held-open doors and repeated denials |

## 3.2 The components

```
Credential ─► Reader ─► Controller (panel) ─► Lock / door hardware
                             │
              door position switch, request-to-exit, alarm outputs
                             │
        management software and database ◄─► video, intruder alarm, fire alarm, HR/identity systems
```

| Component | Role |
| --- | --- |
| **Credential** | Card, fob, phone, PIN or biometric |
| **Reader** | Reads the credential. Mounted on the **unsecured side**, so it must not give access to the wiring |
| **Controller (panel)** | **Makes the decision** and stores credentials and rules **locally**, so doors keep working if the network or server fails |
| **Lock** | **Electric strike**, **magnetic lock**, electrified mortise or exit device |
| **Door position switch** | Tells the system if the door is open or closed |
| **Request-to-exit (REX)** | Releases the door for a person leaving |
| **Door hardware** | Door, frame and hinges that resist attack as well as the lock |
| **Power supply and battery backup** | Keeps locks and controllers working in a power cut |
| **Management software and server** | Enrol people, set rules, view reports and alarms |
| **Network and reader link** | RS-485 (OSDP) between reader and controller, IP to the server |
| **Interfaces** | **Fire alarm release**, CCTV, intruder alarm, visitor management, HR or identity system |

## 3.3 Authentication factors and credentials

| Factor | Examples |
| --- | --- |
| **Something you have** | Card, fob, phone |
| **Something you know** | PIN |
| **Something you are** | Fingerprint, iris, palm vein, face |

**Multi-factor** (two or more factors) is expected for the data hall and higher zones.

### Credential technologies

| Technology | Security | Notes |
| --- | --- | --- |
| **PIN code** | Low alone | Can be shared or observed. Good as a **second factor** |
| **125 kHz proximity card** (EM4100, HID Prox) | **Weak** | Fixed, **unencrypted** number. **Cloned in seconds** with a copier costing about $30. Legacy: avoid for anything sensitive |
| **MIFARE Classic (13.56 MHz)** | **Weak** | Its cipher (Crypto-1) is **broken**: cloneable with free tools |
| **MIFARE DESFire EV2 / EV3, HID Seos, iCLASS SE** | **Strong** | **AES-128 mutual authentication** between card and reader. Practically cannot be cloned when set up correctly |
| **Mobile credentials (BLE or NFC)** | **Strong** | Cloning resistant, fast revocation, bound to a device. **Relay attacks** are possible, so platforms limit BLE range (about 1 to 5 m) and require the phone to be unlocked |
| **Biometrics** | Strong, non-transferable | See below |

**Important:** a card's **UID** (its chip serial number) is **not a credential**. It can be read without authentication and replayed by a phone. A system that authorises on the UID of even a strong card is as weak as 125 kHz. The credential must be stored in an **AES-protected application** and authenticated before it is read.

### Biometrics

| Modality | Notes |
| --- | --- |
| **Fingerprint** | Cheap, common. Affected by dirty or worn fingers |
| **Iris** | Very accurate, contactless |
| **Palm vein** | Accurate, hygienic, hard to copy |
| **Face** | Contactless, convenient, but legally sensitive |

| Measure | Meaning |
| --- | --- |
| **FAR** (false accept rate) | How often a wrong person is let in (a **security** risk) |
| **FRR** (false reject rate) | How often a right person is refused (an **usability** problem) |
| **CER** (crossover error rate) | The setting where FAR equals FRR: a measure of overall accuracy |

**Worked example.** At **400 entries a day** and a **1% FRR**:

```
False rejects = 400 × 0.01 = 4 per day
```

A very strict (low FAR) setting raises FRR, so tune it with a **fallback** for people who cannot enrol. Biometric data is **special category personal data** under GDPR: explicit consent or another valid basis, secure storage of templates, and a non-biometric alternative.

### The wire between reader and controller

| Protocol | Properties |
| --- | --- |
| **Wiegand** | A 1970s one-way link, usually **26-bit**, **unencrypted**. The card number can be sniffed and replayed. Acceptable only on old panels |
| **OSDP** (Open Supervised Device Protocol, **IEC 60839-11-5:2020**, current SIA version v2.2.2 from October 2024) | **Bidirectional, supervised** (a cut or disconnected reader raises an alarm), supports **AES-128 Secure Channel** encryption. **Recommended for all new work** |

**OSDP is only secure with Secure Channel switched on**, with a **unique key per reader** and the reader **out of install mode**. The published default key must not be left in use. A strong card over a plaintext wire still leaves a weakness.

## 3.4 Zones and access policy

Define **zones**, **roles** and the **authentication needed**, and keep the number of people authorised falling towards the rack.

| Zone | Typical authentication **[CHECK]** | Who |
| --- | --- | --- |
| **Perimeter gate** | Card or guard check, vehicle plate | Authorised vehicles, escorted visitors |
| **Reception and lobby** | Staffed desk, visitor registration | Everyone, under control |
| **Building and office areas** | Card | Staff and approved visitors |
| **Data hall entry** | **Card plus PIN or biometric**, through a **mantrap** | Named operations staff and escorted visitors |
| **Cage or suite** | Card plus PIN | The tenant's named staff |
| **Rack or cabinet** | Electronic lock with log (and PIN or card) | Named individuals, time-limited |
| **Critical rooms (electrical, UPS, generator)** | Card plus PIN, tighter list | Authorised facilities staff |

Policy points: **role-based access**, **time schedules** (for example contractor hours only), **dual authorisation** for the most sensitive areas (two people must both be present or approve), **escort rules**, and **access reviews**.

## 3.5 Stopping tailgating and piggybacking

**Tailgating** is following an authorised person through a door. **Piggybacking** is doing it with their consent. Both defeat the credential.

| Measure | How it works | Security level |
| --- | --- | --- |
| **Mantrap (security vestibule, air lock)** | Two interlocked doors: the second cannot open until the first has closed. Admits **one person at a time**, with an authentication inside | **High**. Often with weight sensors or optical sensors |
| **Turnstile (full-height) / speed gate** | Physical barrier that passes one person per authentication | High (full-height) to medium (optical) |
| **Revolving door** | Limits passage to one at a time | Medium |
| **Anti-tailgating detector (ATG)** | Sensors (overhead 3D, thermal, optical) **count the people** through a door and compare with the credential reads | Medium to high |
| **Anti-passback** | A credential **cannot enter twice without exiting** (hard: blocks, soft: alarms) | Supporting. Needs in and out readers |
| **Guard or reception** | A person checks | Variable |
| **Door held-open and forced-open alarms** | Alarm if a door stays open or is forced | Detection |
| **CCTV analytics** | Count and alert | Detection |
| **Culture and training** | Challenge strangers, report | Essential |

### Mantrap design points

- **Egress must always work:** a person inside can always leave, and it **releases on a fire alarm**.
- Allow for **wheelchairs and equipment**: a **separate equipment entrance** (a freight door or airlock under guard) for large items.
- **Intercom and CCTV** inside, and a way to **release a person who is stuck**.
- **Throughput:** plan the queue.

**Worked example.** One mantrap cycle takes **8 s per person**. At shift change **120 people** enter:

```
Queue time = 120 × 8 s = 960 s = 16 minutes
```

If 16 minutes is too long, add a second mantrap, shorten the cycle, or stagger shift changes.

## 3.6 Door hardware and life safety

| Topic | Rule |
| --- | --- |
| **Fail-safe** | The lock **releases when power fails or the fire alarm operates** (a **magnetic lock** is fail-safe). Used on **escape routes** |
| **Fail-secure** | The lock **stays locked** without power (an **electric strike** can be fail-secure). Egress is by a **mechanical lever or push bar** from inside. Used where security must hold and the code permits |
| **Escape routes** | **Must never trap people.** Building and fire codes (NFPA 101, local rules) require **free egress**. Electric locking on an exit needs a **life-safety release**: request-to-exit device, a timed auxiliary push button, and a **fire alarm interface**. **Delayed-egress and sensor-release locks** are allowed only where the code conditions are met |
| **Approval** | The **AHJ or fire marshal** reviews the locking and emergency release arrangements |
| **Door and frame strength** | The lock is only as strong as the door, frame, hinges and wall. Use tested products (for example burglar resistance class RC 3 or 4 under EN 1627) **[CHECK]** |
| **Door position switch and alarms** | **Held-open** (timer) and **forced-open** alarms to the control room |
| **Controller protection** | Controllers and power supplies **inside the secure area**, with tamper switches and battery backup |
| **Reader placement** | The reader's wiring must not be reachable from outside |

## 3.7 Visitors, contractors and keys

| Topic | Practice |
| --- | --- |
| **Visitors** | Pre-registration, ID check, **temporary badges that expire automatically** and are **visibly different**, escorted at all times in secure areas |
| **Contractors** | Vetted, inducted, **time-limited credentials** tied to the work order |
| **Lost credentials** | Deactivate **at once** (a software action that works at every reader within seconds, which a mechanical key cannot offer) |
| **Mechanical keys** | A **key cabinet with audit** (checkout and return), **restricted keyways**, **no uncontrolled master keys**, sealed emergency keys, key inventory, and a procedure for lost keys |
| **Combination and code changes** | On a schedule and when anyone leaves |
| **Equipment moves** | Authorised and logged (13.1), with asset tags reconciled |

## 3.8 Management, audit and maintenance

| Activity | Detail |
| --- | --- |
| **Joiner, mover, leaver** | Add, change and **remove access the same day**, driven from HR and contractor records. **Leavers and contractors keeping working badges for weeks** is a classic failure |
| **Access reviews** | Review the access list **regularly** (for example quarterly) with area owners. Remove orphaned and **shared badges** |
| **Audit logs** | Record every event. Keep for a defined period (commonly **30 to 90 days**, longer where a standard requires) and treat them as **personal data** **[CHECK]**. **Review** after-hours entries and repeated denials. Alert on exceptions |
| **Alarm response** | Procedures for door forced, door held open, tamper and offline alarms |
| **Testing** | Periodic door and release tests, battery and power-failure tests, fire-alarm release tests |
| **System security** | Controllers **not on the corporate LAN with factory passwords**, **no shared operator accounts**, **integrator remote access closed**, patched firmware, segmented network, backups of the database |
| **Resilience** | Controllers decide **locally**, dual power, a fallback procedure (for example guards with a key cabinet) |
| **Migration** | Move from 125 kHz and Wiegand to **DESFire/Seos or mobile credentials over OSDP**. Migrating the wire while keeping weak cards leaves the card as the weakest link |
| **Metrics** | Tailgating alarms, denied-access events, orphan badges found, time to revoke |

## 3.9 Standards

| Standard | Contribution |
| --- | --- |
| **EN / IEC 60839-11-1 and -11-2** | Electronic access control systems: requirements, **security grades 1 to 4**, application guidelines |
| **IEC 60839-11-5** | **OSDP** |
| **EN 50600-2-5, ISO/IEC 27001 A.7.2** | Access control to data centre spaces, physical entry |
| **NIST SP 800-116, FIPS 201** | PIV credentials in facility access (US) |
| **NFPA 101 and local building codes** | Egress and electric locking on escape routes |
| **EN 1627** | Burglar resistance of doors **[CHECK]** |
| **GDPR / UK GDPR** | Access logs and biometrics are personal data |

---

# 13.4 Physical safety considerations

## 4.1 How safety is managed

Data centres combine **high voltage, stored energy, heavy equipment, noise, heat, chemicals and gases** in a space where people work shifts and contractors come and go. Safety is managed by **finding hazards, assessing the risk and applying controls in order of effectiveness**.

```
Risk = severity × likelihood         e.g. severity 4 (serious injury) × likelihood 3 (possible) = 12 (high)
```

### Hierarchy of controls (most effective first)

| Level | Meaning | Example |
| --- | --- | --- |
| **1. Eliminate** | Remove the hazard | Design so equipment can be **de-energised** for maintenance (concurrent maintainability, Tier III) |
| **2. Substitute** | Replace with something less hazardous | Liquid cooling instead of loud, hot-aisle air cooling |
| **3. Engineering controls** | Isolate people from the hazard | Arc-resistant switchgear, guards, interlocks, acoustic panels, ventilation |
| **4. Administrative controls** | Change the way people work | Procedures, permits to work, training, warning signs, time limits |
| **5. PPE** | Protect the person (last line) | Arc-rated clothing, hearing protection, gloves, safety shoes |

### The management system

| Element | Detail |
| --- | --- |
| **Risk assessment** | Written, for each task and area, reviewed after changes |
| **Safe systems of work** | **Method statements and risk assessments (RAMS)**, **permits to work** for high-risk jobs (electrical, hot work, confined space, work at height) |
| **Competence** | Only **qualified and authorised** people do hazardous work |
| **Contractor control** | Induction, supervision, coordination |
| **Training** | Hazards, emergency procedures, first aid, equipment, drills |
| **Incident and near-miss reporting** | Investigate to the root cause. Share the lessons |
| **Audit and review** | Inspections, KPIs, management review |
| **Standards** | **ISO 45001** (occupational health and safety management), and the legal duty of the employer |

## 4.2 Hazards in a data centre at a glance

| Hazard | Where | Main controls |
| --- | --- | --- |
| **Electric shock and arc flash** | Switchgear, UPS, PDUs, busway, batteries | De-energise and lock out, qualified persons, arc-rated PPE, insulated tools (4.3) |
| **Battery hazards** | Battery rooms | Ventilation, acid containment, DC arc protection, separation (4.4) |
| **Fire and smoke** | Everywhere | Module 12: detection, suppression, evacuation |
| **Manual handling and tipping** | Equipment, racks, deliveries | Lifting aids, two-person lifts, rack stabilisation (4.5) |
| **Falls, slips and trips** | Raised floors, ladders, cables, wet floors | Tidy cables, barriers on open tiles, safe access (4.9) |
| **Noise** | Hot aisles, plant rooms | Noise mapping, hearing protection, engineering controls (4.6) |
| **Heat and cold** | Hot aisle, cold aisle, outdoor plant | Heat stress controls, limits on time (4.7) |
| **Chemicals** | Batteries, refrigerants, coolant, fuel, water treatment | Safety data sheets, spill kits, ventilation, PPE (4.8) |
| **Confined spaces** | Under-floor voids, sumps, tower basins | Permit to enter, atmosphere test, standby person (4.9) |
| **Asphyxiation** | Inert gas, nitrogen, refrigerant, oxygen-reduced rooms | Gas detection, procedures, training (4.10) |
| **Lasers** | Fibre optic connectors | Never look into a fibre, use the right test equipment (4.10) |
| **Electromagnetic fields** | Switchgear, transformer rooms | Module 7 exposure rules |
| **Electrostatic discharge** | Equipment handling | Wrist straps with a 1 MΩ resistor (4.10) |
| **Liquid cooling** | CDUs, manifolds, racks | Hot coolant, pressure, leaks, wet floors (4.10) |
| **Vehicles and loading dock** | Dock, yard | Traffic management, edge protection |
| **Lone working** | Remote rooms, night shifts | Check-in procedures, man-down alarms |
| **Violence and security incidents** | Reception, guards | Training, panic alarms, procedures |

## 4.3 Electrical safety

### The principle

**Treat equipment as live until proven dead.** Work **de-energised** wherever possible. **Energised work is the exception**, and needs a written justification and permit.

### Establishing an electrically safe work condition (the usual sequence) **[CHECK]**

1. **Identify all sources** of supply (including dual feeds, bypass paths, generators, batteries and capacitors).
2. **Interrupt** the load and open the disconnect.
3. **Visually verify** the disconnect is open.
4. **Apply lockout/tagout** to every source (personal lock for every worker).
5. **Test for absence of voltage** with a tested, rated meter (test the meter before and after).
6. **Ground** where required.

**LOTO in data centres is complex**: dual power feeds, bypass switches and static transfer switches keep circuits live even when one switchgear is isolated, and **batteries and capacitors store energy**. Authorised people must know the complete energy picture for each task.

### Arc flash

An **arc flash** is an explosive release of energy from a fault. It can exceed **19,000 °C** and produce a pressure blast, intense light and molten metal.

| Item | Detail **[CHECK]** |
| --- | --- |
| **Incident energy** | The energy at a working distance, in **cal/cm²**, from the **arc flash study** |
| **Arc flash boundary** | The distance at which a person would receive a second-degree burn without PPE |
| **Labels** | Each switchboard carries a label with the boundary, incident energy and PPE |
| **PPE categories (NFPA 70E)** | Category 1: 4 cal/cm². Category 2: 8. Category 3: 25. Category 4: 40. Above 40 cal/cm² there is no PPE category: do not work live |
| **Arc-rated clothing** | Rated to IEC 61482 (Europe) or ASTM F1506 (US) |
| **Reduce the energy** | Arc-resistant switchgear, **remote racking** of breakers, **infrared windows**, maintenance modes that speed up protection, current-limiting fuses, good protection coordination |

**Worked example (choosing PPE).** The study gives an incident energy of **6 cal/cm²** at the working distance:

```
4 < 6 ≤ 8 → PPE Category 2 (8 cal/cm² rated clothing)
30 cal/cm² → Category 4 (40 cal/cm²).   50 cal/cm² → no category: de-energise
```

### Energised work and uptime

Standards (NFPA 70E, EN 50110) allow energised work only where **de-energising creates a greater hazard or is infeasible** because of equipment design or operational limits. **Cost, schedule or loss of service alone is not a justification.** Data centres are under uptime pressure, so the real remedy is **design**: **concurrently maintainable** distribution (Tier III and above) lets electrical equipment be **de-energised** while the load runs on the other path **[CHECK]**.

### Data centre specifics

| Point | Detail |
| --- | --- |
| **Rack PDUs and busway taps** | Live-work temptation is highest here: use the A/B design to de-energise one side |
| **Battery strings** | **Cannot be switched off**: the terminals are always live. Use insulated tools, cover terminals, remove jewellery, follow the manufacturer's procedure |
| **Qualified person** | A person trained and authorised for the specific equipment and voltage |
| **Standards** | **NFPA 70E** (US), **EN 50110** (Europe), **IEC 60364 / BS 7671 / NFPA 70** for installations, and local regulations |
| **Tools and test equipment** | Rated, tested and calibrated |

## 4.4 Battery safety

(Batteries are also covered in 6.44, 6.45 and Module 12.)

| Hazard | Lead-acid | Lithium-ion |
| --- | --- | --- |
| **Hydrogen gas** | Released when charging: ventilate to keep it **well below the flammable limit** (commonly below 1% by volume, a quarter of the 4% lower flammable limit) | Not hydrogen, but **off-gas** (flammable, toxic) during failure |
| **Electrolyte** | **Sulphuric acid**: eye and skin burns | Flammable electrolyte |
| **DC arc** | A battery string can deliver very high fault current | The same, at high voltage |
| **Thermal runaway** | Possible (dry-out) | **The main hazard**: self-heating, fire, explosion |
| **Weight** | Very heavy modules | Lighter, but still heavy racks |

Controls: a **separate, fire-rated, ventilated battery room**, **eyewash and emergency shower** with a spill kit for acid, **PPE** (face shield, gloves, apron), **insulated tools**, spacing between cabinets, **temperature and off-gas detection**, **qualified staff**, and a **state-of-charge rule** for moving lithium batteries (the guideline cited in the NIRS fire was below 30%). Signs identify the hazard (NFPA 704 diamond).

## 4.5 Manual handling and rack safety

| Hazard | Detail |
| --- | --- |
| **Heavy equipment** | Servers commonly 20 to 60 kg, **GPU servers heavier**, populated racks **over 1,000 kg** (8.1 in `08_equipment_racks.md`) |
| **Lifting guidance** | NIOSH recommends about **23 kg (51 lb)** as the weight limit under ideal conditions, lower in awkward positions **[CHECK]** |
| **Rack tipping** | A tall rack loaded high, or with several drawers out, can tip. Use **stabilisers and floor anchoring**, load **heavy items at the bottom**, pull out **one device at a time** |
| **Moving racks** | Respect the **dynamic load rating** (8.1), ramps no steeper than about 1:12 (4.7 in `04`), floor ratings, door widths, and clear routes |
| **Raised floor tiles** | Use **suction tile lifters**, never leave open tiles unprotected (barriers, guards, signs), watch point loads |
| **Cables** | Tidy routing, no loose cables across aisles (trip hazard) |

**Controls:** **server lifts** and **rack-mounted lift tables**, **two-person lifts**, trolleys, ramps, training in manual handling, clear and well-lit aisles.

**Worked example (simple lifting check).** A server weighs **40 kg**:

```
Lifting index = load / recommended weight limit = 40 / 23 = 1.74 (above 1: the task is not acceptable for one person)
→ use a server lift or a two-person lift
```

## 4.6 Noise

### Levels and limits

| Place | Typical level |
| --- | --- |
| **Hot aisle** | About **85 to 95 dBA** |
| **Cold aisle** | About **70 to 80 dBA** |
| **Plant and generator rooms** | About **80 to 90 dBA** |
| **CRAC units (sound power)** | About **70 to 85 dB(A)** |
| **NOC and offices** | Target NC 35 to 40 |

| Rule | Value |
| --- | --- |
| **US (OSHA, 29 CFR 1910.95)** | **Permissible exposure limit 90 dBA** over 8 hours. **Action level 85 dBA** (8-hour average): a **hearing conservation programme** is required. **5 dB exchange rate**: allowed time halves for every 5 dB |
| **NIOSH recommendation** | **85 dBA** over 8 hours with a **3 dB exchange rate** (more protective) |
| **EU Directive 2003/10/EC** | **Lower action value 80 dB(A)**, **upper action value 85 dB(A)**, **exposure limit 87 dB(A)** (at the ear, allowing for hearing protection). Health surveillance and protection from the action values |

### Allowed time (OSHA)

```
T (hours) = 8 / 2^((L − 90) / 5)
 85 dBA: 16 h    90 dBA: 8 h    95 dBA: 4 h    100 dBA: 2 h    105 dBA: 1 h
```

### Worked example 1: noise dose

A technician spends 2 hours at 90 dBA (hot aisle), 1 hour at 85 dBA, 5 hours in a quiet NOC at 70 dBA:

```
Dose = (2/8 + 1/16 + 0) × 100% = 31%      (under 100%: within the OSHA limit)
```

### Worked example 2: adding noise sources

Sound levels add on a **logarithmic** scale: SPL_total = SPL_single + 10 × log₁₀(N).

```
Two equal sources:       +10 × log₁₀ 2     = +3 dB          (85 + 85 = 88 dB)
3,000 servers at 65 dBA: 65 + 10 × log₁₀ 3,000 = 65 + 34.8 = about 100 dBA ambient sound power
```

Measured levels in the aisle are lower (about 78 to 88 dBA) because of distance and absorption, but it shows why a full hall is loud.

### The hearing conservation programme

**Noise monitoring** (area surveys and personal dosimetry), **audiometric testing** (baseline and annual), **hearing protectors** (several types, fit-tested), **training**, and **records**. A new **GPU pod** is a change that needs re-measurement.

### Controls

| Level | Measure |
| --- | --- |
| **Engineering** | **Liquid cooling** reduces hot aisle noise (direct-to-chip about 8 to 15 dB, immersion about 15 to 25 dB), but the **CDUs and pumps** are still 70 to 85 dBA. **Acoustic absorption** (perforated metal panels with mineral fibre, baffles). **Avoid open-cell foam** (fire hazard and dust). Enclosures and partitions for plant rooms |
| **Administrative** | Limit time, quiet refuge areas, **noise zone signs** |
| **PPE** | Earplugs or muffs sized to bring the **protected level to about 75 to 85 dB(A)** (**over-protection** isolates people from alarms and colleagues: use communication-capable protectors) |

## 4.7 Heat and cold

| Topic | Detail |
| --- | --- |
| **Hot aisle** | Inlet plus the server temperature rise, for example **27 + 18 = 45 °C** (Module 9), commonly **35 to 50 °C** |
| **Heat stress** | Measured by the **WBGT** (wet-bulb globe temperature). The safe exposure depends on the **work rate, clothing and acclimatisation**. Limits come from occupational standards (for example ACGIH threshold limit values) **[CHECK]** |
| **Regulation** | Heat rules are emerging: in the US the OSHA proposed heat injury and illness prevention standard (2024) is still in rulemaking in 2026, and some states (for example Minnesota for indoor heat, California) have their own rules |
| **Controls** | Limit time in the hot aisle, **work-rest cycles**, drinking water, **acclimatisation** of new staff, rest area outside the aisle, **buddy system**, heat-stress training, **keep containment intact**, pre-cool before entry, protective clothing that breathes |
| **Cold aisle** | Air movement and cool air: a cold-air chill at the work position. Warm clothing available |
| **Hot surfaces** | Heat exchangers, pipes, liquid-cooling coolant (often 40 to 50 °C), containment panels near a fire |
| **Outdoor plant** | Summer heat illness for generator and cooling tower work |

## 4.8 Chemical and environmental hazards

| Substance | Hazard | Controls |
| --- | --- | --- |
| **Battery electrolyte** | Acid burns, flammable electrolyte | Spill kit, eyewash, PPE, containment |
| **Refrigerants** | Asphyxiation, frostbite, **A2L refrigerants are mildly flammable** (9.3) | Leak detection, ventilation, trained handling |
| **Coolant (glycol, treated water)** | Skin and eye irritation, slippery floors | Spill procedure, PPE |
| **Diesel and fuel** | Fire, spills, fumes | Bunding, fire separation, spill kits, no ignition sources |
| **Water treatment chemicals (biocides, acids)** | Corrosive, toxic | Storage, labelling, PPE (10.1) |
| **Fire suppression agents** | Asphyxiation, decomposition gas | Module 12 |
| **Dusts and fibres** | Irritation | Clean, ventilate |

Controls in general: **safety data sheets**, **hazard communication** (labels, 29 CFR 1910.1200), **segregated and labelled storage**, **spill kits**, **eyewash and showers**, ventilation, PPE and training.

## 4.9 Confined spaces and work at height

### Confined spaces

**Under-floor voids** (crawl spaces), **sumps**, **cooling tower basins**, **water vaults**, some **battery rooms** and **underground cable chambers** may be **permit-required confined spaces** (OSHA 29 CFR 1910.146).

| Control | Detail |
| --- | --- |
| **Permit to enter** | Written, with hazards, isolation and rescue plan |
| **Atmosphere testing** | Oxygen (between about 19.5% and 23.5%), flammable gas, toxic gas, **before and during** entry |
| **Isolation** | Lock out power, water and gas supplies |
| **Standby person and communication** | Someone outside, never alone |
| **Rescue arrangements** | A rescue plan and equipment. **Never enter to rescue without them** |

### Work at height

Falls from **ladders, mobile platforms, ceiling voids, cable trays and roofs**. Use **mobile access platforms** in preference to ladders, **guardrails and edge protection** on roofs, **fall protection** where required (typically from about 2 m in Europe and about 1.8 m in US general industry), tools tethered, and **no work over live equipment** without protection **[CHECK]**.

## 4.10 Gas, laser, static and liquid cooling hazards

| Hazard | Detail and control |
| --- | --- |
| **Inert gas and nitrogen** | A discharge or leak reduces oxygen. **Never enter** during an alarm. Follow pre-discharge procedures (Module 12). Oxygen monitors in reduced-oxygen rooms |
| **Hypoxic (oxygen-reduced) rooms** | Medical screening, training, controlled entry (12.7) |
| **Compressed gas cylinders** | Secure upright, caps on, handle with the right trolley |
| **Fibre optic lasers** | The light is **invisible infrared** and can damage the eye. **Never look into a fibre or connector** while it might be live, use a **power meter** to check, use filtered inspection scopes. Fibre systems are normally **Class 1** (IEC 60825-1 and -2) |
| **Electromagnetic fields** | Module 7: exposure limits and zones near switchgear and busbars |
| **Electrostatic discharge** | A **wrist strap with a 1 MΩ resistor** protects equipment and limits shock current to the wearer. **Never wear a strap near exposed live conductors** unless it has the resistor |
| **Liquid cooling** | **Hot coolant** (burns), **pressurised lines**, quick-disconnects, **slippery floors**, electrical equipment near water. Procedures to **depressurise and isolate** before work, leak detection, spill kits |
| **Loading dock** | Vehicle movements, dock edges, heavy lifting: separate pedestrian routes, edge protection |

## 4.11 Emergency arrangements

| Component | Detail |
| --- | --- |
| **Emergency plan** | Roles and actions for **fire, medical emergency, gas release, power failure, flood, bomb threat and violent incidents**. Posted, trained, rehearsed |
| **Evacuation** | Routes, assembly points, headcount, help for people with disabilities (Module 12) |
| **Emergency lighting and signs** | Keep routes visible (Module 5, Module 12) |
| **First aid and defibrillators (AED)** | Trained first aiders and equipment, marked with the ISO 7010 first aid sign |
| **Eyewash and emergency showers** | In battery and chemical areas, tested regularly |
| **Spill kits** | For acid, coolant and fuel |
| **Emergency power off (EPO)** | A deliberate button that **disconnects power** to the room (an NEC 645.10 feature that applies only if the Article 645 wiring allowances are used **[CHECK]**). **Label it, protect it with a cover or guard, alarm it, and keep it away from exit and light-switch positions**: **accidental EPO operation is a recognised cause of outages** |
| **Emergency stops** | On pumps, CDUs and mechanical plant |
| **Lone worker protection** | Check-in, man-down devices, no hazardous work alone |
| **Drills** | Evacuation drills at least yearly, with records |
| **Incident investigation** | Root cause, corrective action, sharing lessons |
| **Fire service liaison** | Pre-planning and site plans (Module 12) |

## 4.12 Where security and safety collide

| Conflict | Resolution |
| --- | --- |
| **Locked doors vs escape** | **Egress always wins.** Escape-route locks **fail safe**, release on **fire alarm**, and have a mechanical or push-button release. Delayed egress only where the code allows |
| **Mantrap vs emergency exit** | Egress path is always open in both directions for people leaving, and releases on alarm |
| **Cage doors vs emergency access** | Cages open from the inside without credentials |
| **Gas room (security and safety)** | The door opens from inside always, and the pre-discharge time allows exit |
| **CCTV vs privacy** | A DPIA, signs, and restricted viewing |
| **Lone worker vs secure area** | A check-in with the control room, and a duress button |
| **EPO vs accidental operation** | A cover, an alarm, a location away from doors, and a procedure |
| **Hot aisle containment doors** | Open easily from inside, for evacuation and heat relief |

## 4.13 Roles and common failures

| Role | Responsibility |
| --- | --- |
| **Employer / operator** | Legal duty for a safe workplace, risk assessments, resources |
| **Safety officer** | Advice, audits, incident investigation |
| **Qualified persons** | Perform hazardous work to procedure |
| **All staff and contractors** | Follow procedures, stop unsafe work, report |

**Common failures:** live work "to avoid downtime", **bypassing lockout**, **incomplete isolation** (auxiliary or battery supplies), **untrained contractors**, **no noise or heat assessment** (never measured), **open floor tiles unguarded**, **cables across aisles**, **blocked exits**, **eyewash dry or blocked**, **an exposed EPO button**, and an **emergency plan that nobody has rehearsed**.

## 4.14 Regulations and standards

| Standard or rule | Contribution |
| --- | --- |
| **ISO 45001** | Occupational health and safety management systems |
| **OSHA 29 CFR 1910** (US general industry) | Electrical (1910.301 to .399), lockout/tagout (1910.147), confined spaces (1910.146), hazard communication (1910.1200), PPE (1910.132 to .138), **hearing conservation (1910.95)**, emergency action plans (1910.38) |
| **NFPA 70E** | Electrical safety in the workplace: safe work, arc flash, PPE |
| **EN 50110, IEC 61482, IEC 60364 / BS 7671** | Operation of electrical installations (Europe), arc protective clothing, installation rules |
| **EU Directive 2003/10/EC** | Noise |
| **EU Directive 2013/35/EU** | Electromagnetic fields (Module 7) |
| **EU Framework Directive 89/391/EEC, UK Management of Health and Safety at Work Regulations, Manual Handling and Work at Height regulations** | Employer duties, risk assessment, handling and height **[CHECK]** |
| **IEC 60825** | Laser safety, including fibre optic systems |
| **ISO 7010, ISO 3864** | Safety signs (Module 12) |
| **NFPA 101** | Life safety and egress |
| **ACGIH TLVs, NIOSH criteria** | Heat stress and noise guidance |

---

## Glossary

| Term | Meaning |
| --- | --- |
| Defence in depth | Several independent layers of protection |
| Deter, detect, delay, respond | The four functions of a security layer |
| CPTED | Crime prevention through environmental design |
| Protection Class (EN 50600-2-5) | Security class 1 to 4 for a data centre space |
| Protection class island | A space with its own class within the site |
| Six walls | A secure room is a barrier on all six surfaces, slab to slab |
| PIDS | Perimeter intrusion detection system |
| LPS 1175 | Fence and gate forced-entry delay rating |
| ASTM F2656 M30 / M40 / M50 | Vehicle barrier crash ratings (30, 40, 50 mph) |
| IWA 14-1 / PAS 68 / ISO 22343 | International, UK and ISO vehicle barrier standards |
| VDA | Vehicle dynamics assessment |
| EN 50131 Grade 1 to 4 | Intruder alarm grades |
| SOC | Security operations centre |
| VSS / VMS / NVR | Video surveillance system / management software / network video recorder |
| PTZ | Pan, tilt, zoom camera |
| WDR | Wide dynamic range (for backlit scenes) |
| IK / IP rating | Impact resistance / dust and water protection |
| Pixel density (px/m) | Pixels on the target per metre. Levels: Overview 20, Outline 40, Discern 80, Perceive 125, Characterise 250, Validate 500, Scrutinise 1,500 |
| DORI | Detect 25, Observe 62.5, Recognise 125, Identify 250 px/m (the 2014 wording) |
| DPIA | Data protection impact assessment |
| ONVIF | Interoperability standard for video devices |
| Credential / reader / controller | What the person presents / the device that reads it / the unit that decides |
| Prox card (125 kHz) | Legacy unencrypted card, cloneable |
| DESFire EV3 / Seos | Strong smart card credentials (AES) |
| UID | The chip serial number: not a credential |
| Wiegand / OSDP | Legacy plaintext reader link / supervised, encrypted reader link |
| Secure Channel | OSDP's AES-128 encryption |
| FAR / FRR / CER | False accept / false reject / crossover error rate |
| Mantrap | Two interlocked doors admitting one person at a time |
| Tailgating / piggybacking | Following a person through a door without or with consent |
| Anti-passback | A credential cannot enter twice without exiting |
| REX | Request to exit |
| Fail-safe / fail-secure | Lock opens / stays locked on power loss |
| LOTO | Lockout/tagout |
| Arc flash | An explosive electrical fault discharge |
| Incident energy (cal/cm²) | Arc flash energy at the working distance |
| Hierarchy of controls | Eliminate, substitute, engineer, administer, PPE |
| TWA / action level / PEL | Time-weighted average / exposure level that triggers a programme / permissible exposure limit |
| WBGT | Wet-bulb globe temperature (heat stress index) |
| RAMS | Risk assessments and method statements |
| EPO | Emergency power off |

## Exam takeaways

**13.1 (physical security considerations)**

- **Security** stops people who should not be there. **Safety** protects people who are. **Safety (egress) wins** when they conflict.
- **Defence in depth** with **independent, auditable layers**: perimeter, site, building shell, data hall entry (mantrap, two-factor), cage, rack, asset. **Deter, detect, delay, respond**: delay must exceed detection plus response (220 s needed vs 270 s delay = 50 s margin in the example).
- **EN 50600-2-5:2021**: **Protection Classes 1 to 4**, assigned **per space** ("islands"), per aspect, from a **documented risk analysis**. ISO/IEC TS 22237-6 is the international counterpart. **ISO 27001:2022 Annex A.7 has 14 physical controls (A.7.4 monitoring is new).**
- **Perimeter:** about 2.4 m anti-climb fence, **LPS 1175** delay rating, **PIDS**, lighting, clear zone, **gates matching the fence**, **crash-rated barriers (ASTM F2656 M30 = 15,000 lb at 30 mph, IWA 14-1, PAS 68; K-ratings obsolete)** from a **vehicle dynamics assessment**. **Six walls**, slab to slab.
- **EN 50131 Grade 3 or 4** intruder alarms, **video verification**, **24/7 control room**, **visitor, vendor and contractor access is the usual gap**, **deliveries stay outside the hall**, same-day access revocation, **NIST SP 800-88** media sanitisation.

**13.2 (CCTV / VSS)**

- **IEC 62676-4:2025 pixel density:** Overview 20, Outline 40, Discern 80, **Perceive 125 (recognise)**, **Characterise 250 (identify)**, Validate 500, Scrutinise 1,500 px/m (face = 16 cm). Old **DORI: 25 / 62.5 / 125 / 250**. **Scene width = horizontal pixels / px/m** (4 MP = 2,688 px → 10.75 m at 250). **W = 2 d tan(HFOV/2).** **4K = 2× the width of 1080p**, not 4×. 250 is a **floor**.
- **Storage (GB/day) = Mbps × 10.8.** 100 cameras at 4 Mbps for 30 days = **129.6 TB**. H.265 about half the bitrate of H.264. **Separate network, failover recording, UPS, NTP.**
- **Retention 30 to 90 days.** **GDPR: DPIA, signs, proportionate retention, no audio.** Cameras are **networked computers**: unique passwords, patching, segmentation, 802.1X.
- Types: **fixed, dome (IK10), PTZ, panoramic, thermal (perimeter night), LPR.**

**13.3 (entry control)**

- Chain: **credential → reader → controller (decides locally) → lock**, plus door contact, REX, power, software. **Three factors:** have, know, are. **Multi-factor for the data hall and above.**
- **125 kHz prox: cloneable (about $30). MIFARE Classic: broken. DESFire EV2/EV3, Seos, mobile: AES-128, strong.** **UID is not a credential.** **Wiegand 26-bit plaintext vs OSDP (IEC 60839-11-5) with Secure Channel.** **FAR/FRR/CER.** Biometrics are **special category data**.
- **Mantrap (interlocked doors, one at a time)**, turnstiles, ATG sensors, **anti-passback**, door alarms. **Egress always works.** **Fail-safe maglock vs fail-secure strike.** Escape routes need a **life-safety release (REX, push button, fire alarm interface)**, approved by the AHJ.
- **Joiner-mover-leaver same day**, **access reviews**, **logs 30 to 90 days**, no shared accounts, controllers off the corporate LAN. **EN/IEC 60839-11-1 grades 1 to 4.**

**13.4 (physical safety)**

- **Hierarchy of controls:** eliminate, substitute, engineering, administrative, PPE. **Risk = severity × likelihood.** **Permit to work, RAMS, competence, ISO 45001.**
- **Electrical:** **de-energise, lock out, test for absence of voltage**, **energised work only if infeasible (cost or downtime is not enough)**. **Arc flash PPE categories 4, 8, 25, 40 cal/cm²**, above 40 do not work live. **Batteries can't be switched off.** **NFPA 70E, EN 50110.**
- **Noise:** **OSHA PEL 90 dBA, action level 85 dBA, 5 dB exchange**, **NIOSH 85 dBA with 3 dB**, **EU 80/85/87 dB(A)**. Hot aisle 85 to 95 dBA. **Dose = Σ C/T.** **Add sources: +3 dB per doubling.** Liquid cooling cuts fan noise.
- **Heat:** hot aisle 35 to 50 °C, **WBGT**, work-rest, acclimatisation. **Lifting: about 23 kg (NIOSH), use lifts, rack stabilisers.** **Confined spaces: permit, atmosphere test, standby.** **Fibre lasers: never look into a fibre.** **ESD strap with 1 MΩ.** **EPO: cover and alarm, accidental operation causes outages.**
- **Conflicts:** egress beats security.

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **EN 50600-2-5:2021**, **ISO/IEC TS 22237-6**, **ANSI/TIA-942-C**, **Uptime Tier Standard** | Data centre security: Protection Classes 1 to 4, protection class islands, risk analysis, zoning |
| **ISO/IEC 27001:2022** (Annex A.7), **NIST SP 800-53 (PE family)**, **NIST SP 800-116**, **NIST SP 800-88** | Physical controls, facility access with PIV credentials, media sanitisation |
| **EN 50131**, **EN 50136**, **EN 50518** | Intruder alarm grades, alarm transmission, alarm receiving centres |
| **IEC / EN 62676** series (Part 4: 2025 edition), **ONVIF** | Video surveillance, pixel density, interoperability |
| **EN / IEC 60839-11-1, -11-2, -11-5**, **FIPS 201** | Electronic access control, security grades, OSDP, PIV |
| **ASTM F2656**, **IWA 14-1**, **PAS 68**, **ISO 22343**, **LPS 1175**, **NPSA guidance** | Vehicle barriers and fence delay ratings |
| **NFPA 101**, **NFPA 70**, **NFPA 70E** (US), **EN 50110**, **IEC 61482**, **IEC 60364 / BS 7671** | Egress and electric locking, electrical safety and arc flash |
| **ISO 45001**, **OSHA 29 CFR 1910** (including 1910.95, .146, .147, .38, .1200), **EU Directive 2003/10/EC**, **EU Directive 2013/35/EU**, **IEC 60825** | Safety management, workplace rules, noise, EMF, lasers |
| **EU NIS2 Directive (2022/2555)**, **GDPR / UK GDPR**, **PCI DSS** | Obligations on security, privacy and cardholder environments |
| **NIOSH** (lifting, noise), **ACGIH TLVs** (heat) | Recommended limits |
| Industry guidance and vendor papers (2026): security and access control, perimeter and barrier guidance, noise and safety audit reports | Credential security, OSDP, perimeter practice, hazard levels |
| Standard security engineering and acoustics | Delay-detection-response timing, pixel density and storage formulas, noise dose and decibel addition |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
