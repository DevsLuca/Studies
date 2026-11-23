# Module 8: Equipment Racks

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section |
| --- | --- | --- |
| 8.1 | Standards, Width, Depth and Height of Racks | [Section 1](#81-standards-width-depth-and-height-of-racks) |
| 8.2 | Types of Racks | [Section 2](#82-types-of-racks) |
| 8.3 | Rack Security | [Section 3](#83-rack-security) |
| 8.4 | Rack Power Rails | [Section 4](#84-rack-power-rails-rack-pdus) |
| 8.5 | Additional Considerations | [Section 5](#85-additional-considerations) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-8-equipment-racks) |

**Objectives (from your slide).** After this module you should be able to describe and understand:

- The difference between 2-post and 4-post racks
- Name the different 4-post rack types with their limitations
- The various width, depth and height and their usage and impact
- The various security measures available on racks
- The various power rail/strip options

| Objective | Where it is covered |
| --- | --- |
| **2-post vs. 4-post** | 8.2 (section 2.2 and 2.3) |
| **4-post rack types and their limitations** | 8.2 (section 2.4) |
| **Width, depth and height: usage and impact** | 8.1 (sections 1.3 to 1.6) |
| **Security measures** | 8.3 |
| **Power rail/strip options** | 8.4 |

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Only the **objectives slide** was available for this module (not the lesson slides), so check the glossary and figures against your course. Related earlier material: raised floor loads and tile grid (Module 4), power distribution to the rack and A/B paths (6.19 and 6.23 in `06-2`), earthing of racks (6.26 in `06-2`, 4.5 in `04`), cooling (Module 9) and the hot/cold aisle layout.

## Why racks matter

The rack is the **unit of deployment** in a data centre: it carries the IT equipment and ties together **space, power, cooling, cabling, weight and security**. A rack runs out of **power, cooling or weight capacity before it runs out of space** more often than not, so the rack choice affects the whole design.

| Term | Meaning |
| --- | --- |
| **Rack** | Strictly, the vertical mounting rails or frame that carry the equipment |
| **Cabinet / enclosure** | A rack **with** side panels, doors, roof and base (the words are often used interchangeably, so check which is meant) |
| **Open-frame rack** | A rack with no panels or doors |
| **Bay / suite** | Racks bolted side by side into a row |

---

# 8.1 Standards, width, depth and height of racks

## 1.1 The standards

| Standard | What it covers |
| --- | --- |
| **EIA-310** (current revision: EIA/ECA-310-E) | The **19-inch rack**: mounting width, rail spacing, **rack unit (U)** and hole pattern. It does **not** set cabinet depth, outside width, doors or load rating |
| **IEC 60297** (including 60297-3-100) and **DIN 41494** | The international and German equivalents for the **482.6 mm (19 in)** series. Equipment from one region fits racks from another |
| **ETSI (ETS 300 119)** | The European **telecom** rack: a **21-inch (535 mm)** mounting width and a **25 mm** unit. Enclosure widths of 150, 300, 600 and 900 mm and depths of 300 and 600 mm |
| **23-inch rack (Western Electric)** | Legacy North American telecom, 584.2 mm, holes on 1-inch centres |
| **10-inch rack** | Small network racks for homes and small offices |
| **OCP Open Rack (V3)** | Hyperscale format: a **21-inch** equipment bay, a **48 mm** OpenU, busbar power. Not interchangeable with a standard 19-inch rack |
| **ANSI/TIA-942-C** | Data centre standard. Cabinets in the **MDA, IDA and HDA** must be **at least 800 mm wide** (matching BICSI 002, CENELEC and ISO/IEC). Covers hot and cold aisles and equipment placement **[CHECK]** |
| **TIA-606, TIA-607** | Labelling and bonding of racks |
| **EN 50174-2** | Separation of power and data cables |

## 1.2 The five numbers of the 19-inch rack

| Item | Value |
| --- | --- |
| **Front panel width** (across the mounting ears) | **482.6 mm (19.00 in)** |
| **Hole centre-to-centre** across the rails | **465.1 mm (18.312 in)** |
| **Clear opening** between the rails (the equipment body passes through) | about **450.85 mm (17.75 in)** |
| **Rack unit (1U)** | **44.45 mm (1.75 in)** |
| **Hole pattern** | **3 holes per U**, spaced **15.875, 15.875 and 12.7 mm** (5/8, 5/8, 1/2 in). The U boundary falls in the middle of the 12.7 mm gap |

**Almost nothing on a "19-inch" rack measures 19 inches.** 19 inches is the equipment **front panel**, not the cabinet.

### Panel height

Equipment is made slightly **shorter than its U** so neighbours don't bind:

```
Panel height (mm) = 44.45 × n − 0.794        (n = number of U)
```

| Equipment | Nominal | Actual panel height |
| --- | --- | --- |
| 1U | 44.45 mm | 43.66 mm |
| 2U | 88.9 mm | 88.11 mm |
| 4U | 177.8 mm | 177.01 mm |

### Mounting height

```
42U × 44.45 mm = 1,866.9 mm   (about 1.87 m of mounting space)
```

The **external** height of a 42U cabinet is higher (about 2,000 mm) because of the frame, roof and base or castors.

## 1.3 Rail holes and fasteners

| Type | Notes |
| --- | --- |
| **Square holes (about 9.5 mm)** | The modern data centre default. **Cage nuts** clip in and carry the thread (10-32 or M6). Easy to reposition |
| **Round, tapped holes** | Screws go directly in (10-32, 12-24 or M6). Common in telecom and audio. Threads can strip |
| **Round, untapped holes** | Need a nut and bolt |

**Thread forms are not interchangeable** (10-32 is US fine thread, M6 is metric, 12-24 is coarser and used for heavy equipment). Cage-nut rails let the thread be chosen at installation.

## 1.4 Width: equipment vs. cabinet

| Width | Meaning |
| --- | --- |
| **482.6 mm** | The equipment front panel (fixed by the standard) |
| **450.85 mm** | The usable opening between the rails |
| **600 mm** | The common **cabinet** width for servers |
| **750, 800 mm and wider** | Cabinets with room at the sides |

**What the extra width is for:**

| Cabinet | Side space (total, then per side) | Consequence |
| --- | --- | --- |
| **600 mm** | 600 − 482.6 = about **117 mm** (about 59 mm each side) | The rail extrusions and side panels use most of it, so cables run in front of or behind the equipment, and a **0U PDU** and cables compete for space |
| **800 mm** | 800 − 482.6 = about **317 mm** (about 159 mm each side) | Room for **vertical cable managers and 0U PDUs** at the sides, so rear airflow is not obstructed |

**TIA-942-C** requires **800 mm minimum** cabinets in the **distribution areas** (MDA, IDA, HDA), where patching and cable density is highest. Cabling in 600 mm cabinets in these areas ends up on the floor and the doors won't close.

**Raised floor grid:** floor tiles are **600 mm**, so 600 mm cabinets fit the grid exactly, and **800 mm cabinets** don't align with a single tile. **Three 800 mm cabinets = 2,400 mm = four tiles**, so planning needs care (Module 4).

## 1.5 Depth

Depth is the dimension **nobody standardised**.

| Depth | Typical use |
| --- | --- |
| **600 mm** | Wall cabinets, patch panels, shallow network equipment |
| **800 mm** | Network switches, lighter equipment, small cabinets |
| **1,000 mm** | Standard servers and general data centre use |
| **1,070 mm (42 in)** | Common server cabinet depth (US sizes) |
| **1,200 mm (48 in)** | Deep servers, storage, high-density racks with heavy rear cabling |

**The trap:** the number in a cabinet's name is the **external** depth. The **usable (mounting) depth** between the front and rear rails is **less**, by roughly 45 mm up to 190 mm depending on the model **[CHECK]**, because of doors, frame and cable space.

### Choosing depth

```
Required internal depth ≥ deepest equipment depth
                         + anything protruding in front of the ears (bezels, handles, UPS fronts)
                         + rear allowance for cables, connectors, cable arms and PDU plugs (about 100 to 200 mm)
```

**Worked example.** The deepest server is **800 mm**, with **50 mm** of front handles and bezel and **150 mm** of rear space for cables and cable arm:

```
Required = 800 + 50 + 150 = 1,000 mm of usable depth
```

A cabinet sold as "1,000 mm" may only offer about 900 mm of rail-to-rail depth, so choose **1,070 mm or 1,200 mm** and check the rail adjustment range against the equipment depth.

**Impact of depth:** too shallow and equipment won't seat on the rear rail, cable arms won't swing, or the rear door won't close. Deeper cabinets use more floor space (and need deeper rows or aisles), but give **cable space and airflow**.

## 1.6 Height

| Height | Notes |
| --- | --- |
| **42U** | The most common full-height cabinet (about 2,000 mm external) |
| **45U, 47U, 48U** | More capacity in the same floor area |
| **12U to 25U** | Half-height racks |
| **4U to 18U** | Wall-mounted cabinets (small offices, closets, edge) |

**What height affects:**

| Impact | Detail |
| --- | --- |
| **Capacity** | More U per footprint, but only if **power, cooling and weight** allow |
| **Access routes** | Door, lift and corridor heights (Module 3: doors about 2.4 m high), and the room's **clear ceiling height** |
| **Clearance to fire suppression and the ceiling** | Cabinet top must stay below the **suppression nozzle clearance** (about 460 mm, Module 4) and the ceiling or containment |
| **Stability** | Taller racks are more top-heavy: **stabilisers, anchoring, seismic bracing** |
| **Reach** | Equipment at the top needs a ladder or lift |
| **Air stratification** | Hot air collects at the top without containment |
| **Cable length** | Tall racks need more cable between top and bottom |

**Worked example: ceiling check.** The room has the **2.6 m minimum clear height** and a **460 mm** sprinkler or nozzle clearance requirement:

| Cabinet | External height | Plus 460 mm clearance | Fits under 2.6 m? |
| --- | --- | --- | --- |
| 42U (about 1,991 mm) | 1,991 mm | 2,451 mm | **Yes** |
| 48U (about 2,200 mm) | 2,200 mm | 2,660 mm | **No**, needs a higher ceiling |

## 1.7 Usable space vs. power

Not every U holds a server: **PDUs, cable managers, patch panels, switches and blanking panels** use space.

| Item | Typical U used **[CHECK]** |
| --- | --- |
| Horizontal PDUs, cable managers, patch panels, switches | about 7 to 12U in a 42U rack |
| Left for servers | about 30 to 35U |

**Space vs. power example.** A 42U rack with **36U of equipment** at **250 W per U** draws **9 kW**. The same rack at 600 W per U would draw 21.6 kW: it may **fit** physically but exceed the **power, cooling or floor loading** it can have. Plan **kW per rack**, not only U.

## 1.8 Load ratings and floor loading

| Rating | Meaning |
| --- | --- |
| **Static load rating** | The weight the rack can carry **installed and not moving** (for example about 800 kg for a 42U network cabinet, many server cabinets 1,000 to 1,500 kg and more, some OCP racks about 1,400 kg) **[CHECK]** |
| **Dynamic load rating** | The weight it can carry **while being moved** on casters. **Lower** than static, often by about 30 to 36% **[CHECK]** |
| **Concentration** | A high static rating doesn't mean the full load can sit on one shelf, rail or the top |

**Worked example: dynamic rating.** A cabinet with a **1,500 kg** static rating and a dynamic rating about 33% lower:

```
Dynamic ≈ 1,500 × 0.67 = about 1,000 kg
```

A populated rack heavier than that **must not be rolled** fully loaded.

**Floor loading (Module 4).** A **1,000 kg** cabinet on a **0.6 × 1.0 m (0.6 m²)** footprint:

```
Pressure = 1,000 × 9.81 / 0.6 = 16,350 Pa = about 16.4 kPa
```

That is far above the **average** floor load in the room. What matters is the **concentrated and rolling loads** on the raised floor panels, pedestals and slab. TIA-942-C gives a minimum floor loading for computer rooms under 20 m² of **5 kPa (100 lbf/ft²)** **[CHECK]**, and heavier racks need **load-spreading** or a rated floor.

## 1.9 Usage guide

| Use | Typical cabinet |
| --- | --- |
| **Network / distribution (MDA, IDA, HDA)** | **800 mm wide**, 1,000 to 1,200 mm deep, 42 to 48U |
| **Servers** | 600 or 800 mm wide, 1,000 to 1,200 mm deep, 42 to 48U |
| **Storage, blade, heavy equipment** | 1,200 mm deep, high static rating |
| **High-density / AI** | 800 mm wide, deep, high rating, three-phase power, liquid-cooling provisions |
| **Telecom** | 2-post, 21-inch (ETSI) or 23-inch racks |
| **Edge / small sites** | Wall-mount or small sealed cabinets (4 to 18U) |

---

# 8.2 Types of racks

## 2.1 Overview

| Type | Posts | Doors and panels |
| --- | --- | --- |
| **2-post rack** (relay or telco rack) | 2 | No |
| **4-post open-frame rack** | 4 | No |
| **4-post enclosed cabinet** (server or network cabinet) | 4 (inside) | Yes: doors, side panels, roof |
| **Wall-mount cabinet** | 2 or 4 | Often a hinged door |

All use the **same 19-inch EIA-310 mounting width and U**, so they look interchangeable. **They are not**: each supports a different **depth, weight, security and airflow** profile.

## 2.2 The 2-post rack

| Feature | Detail |
| --- | --- |
| **Structure** | **Two vertical posts** on a foot plate. Equipment bolts to the posts by its **front ears** only: it is supported as a **cantilever** |
| **Mounting position** | **Flush (front) mount** (equipment forward of the posts) or **centre mount** (equipment mounted at its centre of gravity, to reduce the lever effect) |
| **Typical equipment** | Patch panels, switches, routers, light shallow network gear, telecom equipment |
| **Load** | Low: roughly **300 to 800 lb (140 to 360 kg)** static in many designs **[CHECK]** |
| **Depth** | Limited: only short equipment (the manufacturer states a **maximum mounting depth**) |
| **Stability** | Often must be **anchored to the floor**: equipment forward of the posts makes a loaded rack top-heavy |
| **Airflow and access** | Excellent: fully open, easy access to both sides |
| **Cost and footprint** | Low (can be about half the cost of a 4-post rack) and small |
| **Material** | Often extruded aluminium with tapped holes |
| **Security and dust** | **None** |
| **Typical use** | Wiring closets, telecom rooms, comms rooms (telco/relay racks) |

**Limitations:** limited depth and weight, no rails for sliding servers, no security or dust protection, and the cantilever load can bend posts and amplify vibration.

## 2.3 The 4-post rack

| Feature | Detail |
| --- | --- |
| **Structure** | **Two front posts and two rear posts** joined by a frame. Equipment is supported **front and rear**, usually on **sliding rails** or shelves |
| **Rear posts** | Usually **adjustable in depth** to match the equipment rails |
| **Typical equipment** | Full-depth servers, storage arrays, heavy chassis, UPS units, large routers |
| **Load** | Much higher: roughly **1,000 to 3,500 lb (450 to 1,600 kg)** static **[CHECK]** |
| **Stability** | Weight spread across four posts: better stability and less vibration |
| **Hole types** | Square holes (cage nuts) or tapped holes |
| **Cost and footprint** | Higher cost, larger footprint |

### 2-post vs. 4-post

| | **2-post** | **4-post** |
| --- | --- | --- |
| **Support** | Front ears only (cantilever) | Front and rear (rails) |
| **Equipment** | Light, shallow network gear | Deep, heavy servers, storage, UPS |
| **Depth capacity** | Limited | Adjustable, deep |
| **Load capacity** | Lower | Higher |
| **Sliding rails for servers** | No | Yes |
| **Stability** | Needs floor anchoring | Self-supporting |
| **Airflow and access** | Open, easy | Open (frame) or restricted (cabinet) |
| **Security** | None | None (open frame), good (enclosed) |
| **Cost, footprint** | Lower, smaller | Higher, larger |
| **Typical place** | Telecom and network closets | Data centres, server rooms |

**Selection rule:** use **2-post** for **light, shallow gear mounted by its front ears** (patch panels, switches, 1U appliances) in a controlled space. Use **4-post** for **servers, storage, multi-U UPS**, equipment deeper than about 500 mm, heavy equipment, or anything that needs **rails**.

## 2.4 The 4-post rack types and their limitations

| Type | Description | Strengths | Limitations |
| --- | --- | --- | --- |
| **4-post open-frame rack** (fixed or adjustable depth) | Front and rear rails with no panels or doors | Best passive airflow, full access on all sides, lowest cost, easy cabling | **No physical security**, exposed to dust, **no separation of hot and cold air** (recirculation without blanking and containment), exposed cables, **cannot be converted to a cabinet later** (the usual path is to replace it) |
| **4-post enclosed server cabinet** | Same 4-post frame with **side panels, roof, lockable front and rear doors** | **Security and dust protection**, supports airflow containment, cable entry control, individual lock | **Reduced passive airflow** (solid or poorly perforated doors trap heat), harder access for cabling, door swing clearance, **usable depth less than external depth**, heavier, costlier |
| **Network cabinet** (wide, typically **800 mm**) | Enclosed cabinet with extra side width for vertical cable managers | Room for **high cable counts**, patching, 0U PDUs | Larger footprint, **doesn't match a 600 mm tile grid**, often shallower than server cabinets, costs more |
| **Fixed-depth 4-post rails** | Front and rear rails at a set depth | Rigid, simple | Only fits equipment designed for that depth. Not flexible |
| **Adjustable-depth 4-post rails** | Rear rails can be moved | Fits a range of equipment | **Mis-set depth is a common installation error**: too far apart and equipment won't engage the rear rail, too close and it binds. The rail kit has a **limited adjustment range** |
| **Wall-mount cabinet** (4 to 18U) | Cabinet hung on the wall, with a hinged front or swing-out frame | Saves floor space, suits small sites and edge | **Shallow depth**, low load rating (for example about 80 kg), needs a solid wall (studs or backing board), limited cooling |
| **High-density / heavy-duty cabinet** | Reinforced frame, wider, deeper, higher load rating, three-phase power provisions | Supports AI and dense racks | Costly, heavy, floor loading and cooling become the limits |
| **Containment cabinet** (chimney or ducted) | Hot-air chimney to the ceiling plenum | Captures exhaust, separates hot and cold | Needs a ceiling return plenum, fixed airflow design, little flexibility |
| **Rear-door heat exchanger cabinet** | Water-cooled door at the rear | Removes heat at the rack | Needs chilled water to the rack, leak risk, door weight and depth |
| **OCP Open Rack** | 21-inch equipment bay, 48 mm OpenU, power busbar | Efficient, scale, shared power | **Not interchangeable with standard 19-inch equipment**, special power shelves, not widely available outside hyperscale |

**General limitations for any 4-post rack:** the **rail adjustment range**, the **static and dynamic load rating**, the **usable depth** (including rear cables and PDUs), the **floor loading**, and whether the **doors close** with the equipment installed.

## 2.5 Equipment mounting

| Item | Notes |
| --- | --- |
| **Sliding rail kits** | Span front and rear rails. Allow the server to be pulled out for service. Need the correct rail depth and hole type |
| **Fixed shelves** | For equipment without rails (UPS, tape libraries, appliances) |
| **Cage nuts and screws** | Match the thread (10-32 or M6) to the equipment |
| **Universal rails** | Fit many holes and depths but with less stability |
| **Blanking panels** | Fill every unused U (see 8.5) |
| **Cable management arms** | Hold cables behind a sliding server. Use rear depth |

## 2.6 Quick selection flow

| Question | If yes | If no |
| --- | --- | --- |
| Is the equipment light, shallow (under about 500 mm), front-ear mounted? | 2-post may do | 4-post |
| Does it need sliding rails or weigh more than about 130 kg per rack? | 4-post | 2-post may do |
| Does the room provide security and cleanliness? | Open-frame may do | Enclosed cabinet |
| Is there a lot of patching or cabling (distribution)? | Wide (800 mm) network cabinet | 600 mm cabinet may do |
| Is the density high (above about 10 kW)? | Wide, deep, high-rated, with containment or rear-door cooling | Standard cabinet |
| Is floor space tiny (closet, edge)? | Wall-mount or small cabinet | Floor-standing |

Choose for the environment you expect in **three to five years**, not just today: an open-frame rack can't later become an enclosed cabinet.

---

# 8.3 Rack security

## 3.1 Why security at the rack

Perimeter fences, building access and room doors are not enough: anyone who gets **into the room or cage** can reach an unlocked rack. Rack-level security protects against **theft, tampering, unauthorised cable changes, malicious devices and accidental interference**, and gives an **audit trail**. It matters most in **colocation** (many tenants in one hall) and for **sensitive or regulated data**.

```
Site perimeter → building → floor / data hall → cage or row → RACK → device
                                                              ↑ this lesson
```

(The wider security layers are in Module 13.)

## 3.2 Security measures at the rack

| Measure | Description | Strength | Weakness |
| --- | --- | --- | --- |
| **Mechanical key lock** | Keyed cylinder or **swing handle**, often 3-point latching | Simple, cheap, robust, no power | Keys can be copied, lost or shared, **no audit trail**. A **common key** across many racks is a risk. A **unique key** per rack means many keys to manage |
| **Combination lock** | Mechanical code | No keys | Codes shared, no audit |
| **Electronic lock with PIN keypad** | Code entered at the handle | Easy to change codes, can set **time-limited PINs** | PINs get shared or observed |
| **RFID / proximity / smart card** | Badge held to a reader on the handle | Can reuse the **building badge**, quick | Cards can be **lost or loaned**. Old **125 kHz proximity cards are easily cloned**: use modern encrypted smart cards |
| **Biometric** (fingerprint, palm vein, iris, face) | A physical trait | **Cannot be lost, loaned or stolen** | Cost, enrolment, privacy rules |
| **Multi-factor** | For example **card + PIN**, or **card + fingerprint**, or biometric + mobile credential | Much stronger | Slower, more equipment |
| **Mobile or Bluetooth credentials** | Phone as the key | No wiring needed, easy issue and revoke | Depends on the phone and the app |
| **Networked electronic locks** | Locks connect to a central system (often over **PoE** or by Wiegand to the building access control system) | **Central control**, **audit trail**, remote unlock and alarms, one credential for every zone | Needs power and network, and good design |
| **Audit trail** | Records **who** opened **which** rack, **when**, and **for how long** (and whether it was left unlocked) | Evidence for incidents and audits | Useless if credentials are shared or logs unreviewed |
| **Door, side-panel and rear-panel sensors** | Contacts that report open, ajar or removed panels | Detects access through any side, not only the front door | Needs monitoring |
| **Lockable panels and doors** | Locking front door, **split rear doors**, **locking side panels** and roof | Closes every route into the cabinet | Doors with locks only where fitted. Open-frame racks have none |
| **Locking PDUs and cord retention** | Locked strips, **locking outlets**, cable locks | Stops unplugging and tampering | Adds hardware |
| **Cameras** | CCTV on the aisle and, in sensitive areas, **in-cabinet or row cameras** | Records activity, deters | Storage, privacy, review effort |
| **Cages and partitions** | Wire-mesh or solid cages around rack groups (floor to ceiling) | Separate tenants, simple | Space and cost, **cabinet-level locks** can replace cages in colocation |
| **Tamper-evident seals and procedures** | Seals on panels and equipment, asset tags, removal controls | Cheap, shows interference | Needs a process |

### Power-failure behaviour

| Mode | Behaviour |
| --- | --- |
| **Fail-secure** | The lock stays **locked** when power fails (safer against intruders, but staff can't open it without a mechanical override) |
| **Fail-safe** | The lock **opens** on power failure (safer for access, weaker for security) |
| **Mechanical override** | A key or manual release for emergencies, itself controlled and logged |

Specify what the lock does in a power failure, and make sure **fire and emergency egress** rules are respected.

## 3.3 Choosing the level (tiering)

Not every rack needs the same protection. Choose by **data sensitivity** and **how critical the equipment is**.

| Tier | Typical racks | Suggested measures |
| --- | --- | --- |
| **Low** | Internal, non-sensitive, in a controlled private room | Keyed lock or PIN lock, room access control |
| **Medium** | Business systems, shared rooms | **RFID + PIN**, networked locks with an audit trail, door sensors |
| **High** | Payment, health, financial or regulated data, colocation tenants | **Biometric or multi-factor**, audit trail linked to central access control, door and panel sensors, camera, alarms |

Applying the highest level everywhere wastes money, and applying the lowest everywhere leaves critical racks exposed.

## 3.4 Compliance and standards **[CHECK]**

| Rule | Requirement |
| --- | --- |
| **PCI DSS** | Restricted, monitored physical access to cardholder data environments |
| **HIPAA** | Controlled physical access to systems with protected health information |
| **ISO/IEC 27001, SOC 2** | Protect equipment from unauthorised access, with records |
| **EN 50600-2-5, ISO/IEC 22237** | Physical security systems and **protection classes 1 to 4** |
| **ANSI/TIA-942, BICSI 002** | Rack-level locking and security at the higher ratings |

All of them depend on **documented audit trails**.

## 3.5 Good practice

- **Key and credential control:** issue, record, review and revoke. Don't share cards or PINs.
- **Time-limited access** for contractors (expiring PINs or credentials), with escort for visitors.
- **Review the logs** and alarms: an audit trail that nobody reads is not security.
- **Integrate** rack locks with the building access control and the DCIM or BMS.
- **Separate duties:** keep access management separate from the auditing of it.
- **Seal cable entries** and fit blanking panels so nothing can be reached without opening a locked door.
- **Asset tags and removal controls** for equipment leaving a rack.
- **Two-person rule** for the most critical racks.

---

# 8.4 Rack power rails (rack PDUs)

## 4.1 What they are

A **rack power rail, power strip or rack PDU** (power distribution unit) takes power from the branch circuit (from the floor PDU, RPP or busway tap, see 6.23 in `06-2`) and **distributes it to the equipment in the rack** through outlets. It is **not** the same as the floor-standing PDU.

```
Floor PDU / RPP / busway tap ──► Rack PDU (power rail) ──► Server power supplies
```

## 4.2 Intelligence levels

Names differ between vendors (one vendor's "smart" may be another's "monitored").

| Level | What it does | Typical use |
| --- | --- | --- |
| **Basic** | Distributes power only. No measurement | Low-criticality loads, closets |
| **Metered** | **Measures** current, voltage or power at the **input** and shows it on a **local display** | Racks where technicians need to see the load and avoid overloads |
| **Monitored** | Metered, plus **network connectivity** (SNMP, Modbus, web or API): remote reading, alarms, DCIM integration | Most data centre racks |
| **Switched** | Adds **remote on/off of each outlet**, **power-on sequencing** and outlet locking | Unstaffed and edge sites, labs, remote reboot (lower MTTR) |
| **Outlet-metered (managed, intelligent)** | **Per-outlet** measurement, and often switching | **Chargeback** (billing per customer) in colocation, detailed capacity planning |
| **Rack ATS / STS** | A transfer switch feeding **single-corded** equipment from two sources | Single-corded devices in an A/B rack (see 6.13 and 6.19) |
| **Hot-swap PDU with manual bypass** | Allows the PDU to be changed without powering down the equipment | Maintenance without an outage |

Also: **environmental sensor ports** (temperature, humidity, door contact, leak) on most monitored models, secure management (SNMPv3, signed firmware), and a **lifetime** in which the network card may need replacing after about 7 to 10 years while the chassis can last 15 years or more **[CHECK]**.

## 4.3 Form factor

| Form | Description | Notes |
| --- | --- | --- |
| **0U (zero-U), vertical** | Mounts in the rack's **side channel** or rear rail. **Uses no rack units** | The default for high-density racks, carries the most outlets (often 24 to 54). Needs a rack **wide and deep enough** (a 600 mm cabinet is tight, 800 mm is comfortable) |
| **1U or 2U, horizontal** | Mounts in the rails like a server | Uses rack space. Used in 2-post racks, shallow racks and low-outlet needs |
| **Wall or under-counter** | Small sites | |

Mount **A and B** PDUs on opposite sides of the rack, with outlets facing the equipment's power supplies.

## 4.4 Input: voltage, phase, current

| Choice | Notes |
| --- | --- |
| **Single-phase** | Simple. Typical for racks below about **5 kW**. 230 V (16 or 32 A) in Europe, 120 V or 208 V in the US |
| **Three-phase** | More power per cable and per PDU. Needed above about 5 kW. 400 V (16, 32 or 63 A) in Europe, 208 V (and 415 V) in the US. **Needs balanced phases** (6.17 in `06-2`) |
| **Plug** | **IEC 60309** (blue for 230 V, red for 400 V) in Europe. NEMA locking types (L6-30, L21-30) in North America |
| **Cord length and entry** | Match the rack height and the whip or busway tap position |
| **Internal protection** | PDUs above a certain size contain **branch circuit breakers** per bank, so one bank can trip while the PDU has capacity left |

### Capacity of common rack PDUs

Nameplate power = V × I (single-phase) or √3 × V × I (three-phase). The **continuous** rating is often **80% of the nameplate** (the NEC and UL convention) **[CHECK]**.

| Input | Nameplate | At 80% continuous |
| --- | --- | --- |
| 230 V, single-phase, 16 A | 3.7 kW | 2.9 kW |
| **230 V, single-phase, 32 A** | **7.4 kW** | **5.9 kW** |
| 400 V, three-phase, 16 A | 11.1 kW | 8.9 kW |
| **400 V, three-phase, 32 A** | **22.2 kW** | **17.7 kW** |
| 400 V, three-phase, 63 A | 43.6 kW | 34.9 kW |
| US 120 V, single-phase, 30 A | 3.6 kW | 2.9 kW |
| US 208 V, single-phase, 30 A | 6.2 kW | 5.0 kW |
| **US 208 V, three-phase, 30 A** | 10.8 kW | **8.6 kW** |
| US 415 V (240 V phase), three-phase, 30 A | 21.6 kW | 17.3 kW |

## 4.5 Outlets

| Outlet | Rating | Used for |
| --- | --- | --- |
| **IEC C13** (mates with C14 plug) | **10 A** (15 A in some North American listings) | Most servers, switches and 1U appliances |
| **IEC C19** (mates with C20) | **16 A** (20 A in North America) | Blade chassis, large storage, GPU servers, big switches, UPS units |
| **Combination C13/C19 outlets** | Accept either plug | Useful when the equipment mix is unknown |
| **NEMA 5-15 / 5-20, Schuko** | Local sockets | Small loads, avoid for dense racks |

| Feature | Notes |
| --- | --- |
| **Typical mix** | For example 30 to 36 C13 plus 6 C19 on a vertical PDU |
| **Locking outlets or cord retention** | Cords vibrate loose, so a bumped cable becomes an outage. Recommended for any rack that is serviced |
| **Phase layout (three-phase)** | **Block layout** (each phase on a contiguous group, so balancing means routing cords up and down) or **alternating-phase layout** (A, B, C on adjacent outlets, which helps routing but doesn't balance an uneven load by itself) |
| **Banks and breakers** | Outlets grouped by phase and branch breaker. Spread **dual power supplies** across banks and across feeds |
| **Colour coding** | Different colours for A and B PDUs and cords |
| **Spare outlets** | Count every cord and add about 20 to 30% |

**Match plugs, not just outlet counts.** A rack of high-draw GPU servers can run out of C19 outlets well before it runs out of power.

## 4.6 A and B power rails and redundancy

| Rule | Explanation |
| --- | --- |
| **Spec an A and a B PDU** for any dual-corded rack | Each server power supply is plugged into a different PDU, fed from a different path (6.19 in `06-2`) |
| **Each PDU sized for the whole rack** | If one feed fails, the other carries everything |
| **Normal load per PDU at most about 40 to 50% of its rating** | Leaves headroom for failover |
| **Check the failover scenario** | The surviving PDU, its breakers and its upstream circuit must carry the full load |
| **A and B must be truly independent** | Separate floor PDU, UPS and upstream path |
| **Single-corded devices** | Break the model. Use a **rack ATS or STS**, or accept the weakness |
| **Don't cascade PDUs** | Plugging one PDU into another compounds ampere limits and bypasses the second unit's metering. (You can daisy-chain the *network management* connection so one IP address manages several PDUs) |
| **Feed from a UPS-protected source** | A PDU gives no backup power itself |

## 4.7 Worked examples

### Example 1: choosing the PDU rating

A **10 kW**, dual-corded rack on **400 V three-phase** with A and B PDUs. In failover each PDU carries all **10 kW**.

| PDU | Nameplate | At 80% | Carries 10 kW alone? |
| --- | --- | --- | --- |
| 16 A three-phase | 11.1 kW | 8.9 kW | **No** (8.9 < 10) |
| **32 A three-phase** | 22.2 kW | 17.7 kW | **Yes** |

In normal operation each 32 A PDU carries about **5 kW**, which is **28% of its 80% rating**, leaving plenty of headroom.

### Example 2: the A/B trap

A rack with **7.4 kW** PDUs on each feed can support about **7.4 kW of total load**, not 14.8 kW, because either PDU must carry the whole rack. At the 80% continuous limit, about **5.9 kW**.

### Example 3: single-phase or three-phase?

A rack of **20 servers at 450 W** is **9 kW**:

| Option | Capacity | Verdict |
| --- | --- | --- |
| 230 V single-phase 32 A | 7.4 kW (5.9 kW at 80%) | Too small |
| 400 V three-phase 16 A | 11.1 kW (8.9 kW at 80%) | Marginally below 9 kW |
| **400 V three-phase 32 A** | 22.2 kW (17.7 kW at 80%) | Suitable |

### Example 4: phase current

A balanced **12 kW** load on a **400 V** three-phase PDU:

```
I per phase = 12,000 / (√3 × 400) = 17.3 A
```

If the phases are unbalanced (for example 25 A, 15 A and 10 A), one phase and its breaker bank can trip while the total looks acceptable. Use per-phase metering (6.17 in `06-2`).

### Example 5: outlet count

**30 dual-corded servers**, one cord on each PDU:

```
Outlets per PDU = 30 × 1.25 (spare) = 37.5, so 38 outlets
```

A 36 C13 + 6 C19 unit has enough outlets, but check that **C19-cord devices** get C19 outlets.

## 4.8 DC and Open Rack power

| Item | Notes |
| --- | --- |
| **OCP Open Rack** | Servers plug into a **busbar** at the back of the rack, fed by **power shelves** that convert AC to DC (**48 V** in recent versions). Replaces the PDU and per-server power supplies **[CHECK]** |
| **Telecom racks** | **-48 V DC** distribution with fuse panels and battery plants |
| **High-density AC racks** | Three-phase 32 A and 63 A PDUs, with busway tap-offs (6.24 in `06-2`) |

## 4.9 Common mistakes

- Sizing from the **breaker label** or nameplate, not the real load (6.34 in `06-3`).
- Sizing the A/B pair at **half** the load each.
- Buying by **outlet count** instead of matching **plug types** and C19 needs.
- No **locking outlets** on racks that get serviced.
- Ignoring **phase balance** and bank breakers.
- Plugging a **single-corded** device into one PDU without a transfer switch.
- Specifying the PDU before confirming the **input receptacle and phase** with facilities.
- **Basic** PDUs on production racks, with no way to see load or headroom.

---

# 8.5 Additional considerations

## 5.1 Airflow and cooling at the rack

| Topic | Practice |
| --- | --- |
| **Airflow direction** | Servers breathe **front to back**. Racks face each other across **cold aisles** (supply) and back to back across **hot aisles** (exhaust) |
| **Blanking panels** | Fill **every unused U** so exhaust air can't recirculate to the front. An open U is a leak in the cold aisle |
| **Seal the gaps** | Around rails, side gaps and the **cable entry** (brush panels, grommets) and the cabinet base |
| **Doors** | Front and rear doors need a **high open (perforated) area** (commonly about 63 to 80% **[CHECK]**). Solid doors trap heat |
| **Containment** | Hot-aisle or cold-aisle containment, and **chimney cabinets** where used, must fit the cabinets |
| **Don't rely on rack-top fans** | Fans added to compensate for poor sealing can pull hot air back toward the server inlets |
| **Density** | Above about 10 to 15 kW per rack, air cooling needs containment. Higher densities need **rear-door heat exchangers or liquid cooling** (Module 9) |
| **Liquid-cooling readiness** | Space for manifolds, hoses, quick-disconnects and leak management |
| **Temperature sensors** | At the inlet of the rack (top, middle and bottom) |

### Worked example: airflow for a rack

Airflow needed for a heat load **P** with temperature rise **ΔT**:

```
Airflow (m³/s) = P (kW) / (1.2 × 1.005 × ΔT (K))       (air density 1.2 kg/m³, specific heat 1.005 kJ/kg·K)
```

| Rack | ΔT | Airflow |
| --- | --- | --- |
| **10 kW** | 12 K | 10 / (1.206 × 12) = **0.69 m³/s** = 2,487 m³/h = about **1,460 CFM** |
| **6 kW** | 10 K | 6 / (1.206 × 10) = **0.50 m³/s** = about 1,790 m³/h |

The rack and the **perforated tile or supply opening** must be able to deliver that volume (Module 9 covers this in detail).

## 5.2 Weight, stability and installation

| Topic | Practice |
| --- | --- |
| **Heavy at the bottom** | Load from the bottom up (UPS, storage, heavy servers low) to keep the **centre of gravity** low and avoid tipping |
| **Static and dynamic ratings** | Check both, and **don't roll** a rack that exceeds the dynamic rating |
| **Floor loading** | Check the raised floor panels, pedestals and slab for concentrated and rolling loads (Module 4), especially for several heavy racks side by side |
| **Levelling feet, stabilisers and anchoring** | Level the rack, fit **stabilisers** on tall or top-heavy racks, anchor to the floor or slab where needed |
| **Seismic** | In earthquake zones use seismic-rated racks, bracing and anchors designed with the structural engineer and authority |
| **Baying** | Join racks into rows with **baying kits** and joint side panels, keeping a consistent row |
| **Delivery routes** | Doors, lifts, ramps and the staging area must handle the rack's size and weight (Modules 3 and 4). Decide whether racks are moved **empty or populated** |
| **Service clearance** | Front and rear clearance to pull servers and reach rear connections, about **1 m at the rear preferred**, with some equipment needing more **[CHECK]** |

## 5.3 Cable management

| Topic | Practice |
| --- | --- |
| **Vertical and horizontal managers** | Space for them inside the cabinet (the reason for wider racks) |
| **Separate power and data** | Per EN 50174-2 and TIA practice, on opposite sides of the rack where possible. **Power under the cold aisle, telecom trays under the hot aisle** with an access floor |
| **Bend radius** | Respect minimum bend radius (commonly about four times the diameter for copper and ten times for fibre **[CHECK]**) |
| **Cable entry** | Brush or grommet seals at the top and bottom |
| **Label everything** | Per TIA-606: rack, U position, port and both ends of every cable |
| **Leave room** | Don't fill the vertical managers to the brim, cables will block airflow and doors |
| **Fibre** | Protect from sharp bends and crushing |

## 5.4 Bonding and earthing of racks

| Rule | Detail |
| --- | --- |
| **Bond every rack** to the facility's **common bonded network** with its **own conductor** | **Do not daisy-chain** racks together. TIA-607 requires each rack to bond directly (6.26 in `06-2`) |
| **Use a rack bonding busbar** | Inside the cabinet, with a link to the room's bonding busbar or grid |
| **Bond doors, side panels and roof** | With flexible straps, so the whole cabinet is one piece electrically |
| **Metal to metal contact** | Remove paint at bonding points, or use star washers and bonding hardware |
| **ESD** | Wrist-strap points in the rack, connected to the bonding network |
| **Equipment** | Servers earth through the PE pin of their power cord, **not** instead of the rack bond |

## 5.5 Rack layout and documentation

- **Rack elevation** drawings show every device and its U position.
- **Row layout:** hot and cold aisles, access aisle widths, tile alignment (600 mm tiles), room for door swing.
- **Plan power, cooling and weight with the space**: a rack is **full** when it reaches the **first** of its limits (U, kW, airflow or kg).
- **Standardise** rack sizes, PDUs and layouts to cut cost, spares and errors.
- **Keep records** in DCIM: asset, location, power draw, connections, owner.
- **Leave spare U** (about one third in a typical plan) for growth, and for cable managers and blanking panels.

### Rack elevation example (42U) **[CHECK]**

| Position | Item | U |
| --- | --- | --- |
| Top | Top-of-rack switches (2) and horizontal cable manager | 3 |
| | Patch panels | 2 |
| | Servers (1U and 2U) | 28 |
| | Blanking panels | 4 |
| Bottom | Storage or UPS (heavy) | 4 |
| **PDUs** | **0U, vertical, in the side channels** | 0 |
| | **Total** | **41, with 1U spare** |

## 5.6 Other points

| Topic | Notes |
| --- | --- |
| **Edge and micro data centres** | Sealed, sometimes IP-rated cabinets with built-in cooling and security. TIA-942-C now classifies edge and micro-edge types **[CHECK]** |
| **In-rack detection** | Smoke or air-sampling detection in or near dense racks, per the fire design (Module 12) |
| **Environmental monitoring** | Temperature, humidity, leak and door sensors in the cabinet, via the PDU or a sensor hub |
| **Fire and gas suppression** | Perforations and door seals must be compatible with the suppression design |
| **Sustainability** | Steel racks are recyclable. Reuse racks where the standard (EIA-310) allows. Higher density saves floor space |
| **Procurement** | Specify width, **usable** depth, height, load ratings, hole type, door perforation, locks, PDU mounting, bonding and accessories, not just "42U rack" |

---

## Glossary

| Term | Meaning |
| --- | --- |
| Rack / cabinet / enclosure | Mounting frame / frame with panels and doors / same, often used interchangeably |
| U (rack unit) | 44.45 mm (1.75 in) of vertical mounting space |
| EIA-310, IEC 60297, DIN 41494 | The 19-inch rack standards |
| 2-post rack (relay, telco rack) | Open rack with two posts, equipment held by its front ears |
| 4-post rack | Front and rear posts, equipment on rails or shelves |
| Open-frame | No panels or doors |
| Static / dynamic load rating | Capacity when installed / when moved on casters |
| Usable depth | Space between the front and rear rails |
| Blanking panel | Cover for an unused U |
| 0U PDU | Vertical power strip mounted in the side channel, using no rack units |
| Basic / metered / monitored / switched PDU | Increasing levels of measurement and control |
| C13 / C19 | IEC 60320 outlets rated 10 A / 16 A |
| IEC 60309 | Industrial plug (blue 230 V, red 400 V) |
| Rack ATS / STS | Transfer switch that gives a single-corded device two sources |
| Audit trail | Record of who accessed which rack and when |
| Fail-secure / fail-safe | Lock stays locked / unlocks when power fails |
| OCP Open Rack | Open Compute 21-inch rack with a power busbar |
| Hot / cold aisle | Aisle behind racks (exhaust) / in front of racks (supply) |

## Exam takeaways

**8.1 (standards, width, depth, height)**

- **EIA-310 (IEC 60297, DIN 41494)**: panel **482.6 mm**, holes **465.1 mm** apart, clear opening **450.85 mm**, **1U = 44.45 mm**, **3 holes per U (15.875, 15.875, 12.7 mm)**. **Panel height = 44.45 n − 0.794.** **42U = 1,866.9 mm.**
- The standard **does not** fix **depth, outside width, doors or load**. **ETSI** is 21-inch (535 mm, 25 mm unit). **OCP Open Rack** is 21-inch with a 48 mm unit.
- **600 mm** cabinets for servers, **800 mm** for cable-dense distribution (**TIA-942-C: at least 800 mm in the MDA, IDA and HDA**), leaving room for **0U PDUs and vertical managers**. 800 mm cabinets don't match the **600 mm tile grid**.
- **Usable depth is less than the external depth.** Required depth = deepest equipment + front protrusions + rear cable allowance. Typical 1,000 to 1,200 mm.
- **42U** is the common height. Check the **ceiling and nozzle clearance** (460 mm). **Space is not the only limit: power, cooling and weight usually are.**
- **Static vs. dynamic load rating** (dynamic about a third lower). Check the **floor loading**.

**8.2 (rack types)**

- **2-post:** front-ear (cantilever) mounting, **light, shallow** gear, low load, **anchor to the floor**, open, cheap, **no security**. **4-post:** front and rear support, **servers and heavy equipment**, adjustable depth, high load.
- **4-post types and limits:** **open-frame** (no security, no air separation, can't become a cabinet), **enclosed cabinet** (restricted airflow, usable depth lost), **wide network cabinet** (footprint, tile grid), **fixed vs. adjustable rails** (wrong depth setting), **wall-mount** (shallow, light), **high-density**, **containment**, **rear-door**, **OCP** (not 19-inch compatible).

**8.3 (security)**

- Measures: **mechanical keys, PIN, RFID card, biometric, multi-factor, networked locks with an audit trail, door and panel sensors, lockable panels, cages, locking PDUs, cameras, seals.**
- Keys have **no audit trail**. Old 125 kHz cards are **cloneable**. **Biometric** can't be shared. **Fail-secure vs. fail-safe.** Choose the level by **sensitivity tier**. **PCI DSS, HIPAA, ISO 27001, SOC 2** need **audit trails**.

**8.4 (power rails)**

- **Basic, metered, monitored, switched, outlet-metered, rack ATS.** **0U vertical vs. 1U horizontal.** **C13 = 10 A, C19 = 16 A.**
- **230 V 32 A = 7.4 kW. 400 V three-phase 32 A = 22.2 kW. 80% continuous rule.** **Each A/B PDU sized for the whole rack, normally at 40 to 50%.** A rack with 7.4 kW PDUs on A and B supports **about 7.4 kW**, not 14.8. **Rack ATS for single-corded.** **Don't cascade PDUs.** Match plugs, add **locking outlets**, balance phases.

**8.5 (other)**

- **Blanking panels** in every empty U. **Seal** gaps. **Perforated doors.** **Airflow = P / (1.2 × 1.005 × ΔT).** **Heavy at the bottom.** **Bond each rack directly** (no daisy-chain). **Label** per TIA-606. **Separate power and data.** A rack is full at the **first** limit (U, kW, airflow or kg).

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **EIA/ECA-310** (revision E), **IEC 60297**, **DIN 41494** | 19-inch rack dimensions, rack unit and hole pattern |
| **ETSI ETS 300 119** | 21-inch telecom racks |
| **OCP Open Rack V3** base specification | Hyperscale racks |
| **ANSI/TIA-942-C** (2024) | 800 mm cabinets in distribution areas, floor loading |
| **ISO/IEC 22237**, **EN 50600-2-5** | Physical security classes |
| **BICSI 002** | Rack design guidance |
| **ANSI/TIA-606**, **ANSI/TIA-607** | Labelling and bonding |
| **EN 50174-2** | Power and data separation |
| **IEC 60320**, **IEC 60309** | C13/C19 outlets and industrial plugs |
| **NFPA 70** (NEC), UL convention | 80% continuous-load rule |
| **PCI DSS**, **HIPAA**, **ISO/IEC 27001**, **SOC 2** | Audit requirements that drive rack access control |
| Manufacturer data and basic physics | Load ratings and the airflow formula |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
