# Module 11: Designing a Scalable Network Infrastructure

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section |
| --- | --- | --- |
| 11.1 | Structured Cabling System | [Section 1](#111-structured-cabling-system) |
| 11.2 | Copper Cables | [Section 2](#112-copper-cables) |
| 11.3 | Fibre Cables | [Section 3](#113-fibre-cables) |
| 11.4 | Cabling as per TIA-942 | [Section 4](#114-cabling-as-per-tia-942) |
| 11.5 | Testing the Cabling Infrastructure | [Section 5](#115-testing-the-cabling-infrastructure) |
| 11.6 | Network Redundancy | [Section 6](#116-network-redundancy) |
| 11.7 | Building to Building Connectivity | [Section 7](#117-building-to-building-connectivity) |
| 11.8 | Network Monitoring | [Section 8](#118-network-monitoring) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-11-designing-a-scalable-network-infrastructure) |

**Objectives (from your slide).** After this module you should be able to describe and understand:

- The importance of the network cabling infrastructure
- Planning considerations
- The various copper and fibre network technologies with its pros and cons
- TIA-942 cabling system topology
- Testing and verification of cabling system
- How to achieve network diversity and redundancy
- Options of connecting multiple sites

| Objective | Where it is covered |
| --- | --- |
| **Importance of the network cabling infrastructure** | 11.1 |
| **Planning considerations** | 11.1 (section 1.5), and the design points in 11.2 to 11.4 |
| **Copper and fibre technologies, pros and cons** | 11.2 and 11.3 |
| **TIA-942 cabling system topology** | 11.4 |
| **Testing and verification** | 11.5 |
| **Network diversity and redundancy** | 11.6 |
| **Connecting multiple sites** | 11.7 (and 11.6 for resilience) |

Lesson 11.8 (network monitoring) is in your index but not in the objectives, so it is covered as an extra.

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course gives a different number, use your course. Only the **objectives slide** was available for this module (not the lesson slides), so check the glossary and figures against your course. Related earlier material: power and data cable separation (6.18 in `06-2`), common mode noise and bonding (6.26 and 6.27), racks and cable management (Module 8), the topology of rooms (Module 3), and TIA-942 and EN 50600 (Module 2).

## The big picture

The network is how a data centre delivers its service, and the **cabling** is its physical layer: the part that is **hardest to change** and **longest-lived**. Servers are replaced every few years, switches every five to seven, but the cable plant is expected to serve **10 to 25 years** and several generations of equipment **[CHECK]**.

```
Carriers ──► Entrance Room ──► Main Distribution Area (core) ──► Horizontal Distribution Areas ──► Equipment racks
              (ER)               (MDA)                              (HDA, aggregation)               (EDA)
```

---

# 11.1 Structured cabling system

## 1.1 What it is

A **structured cabling system** is a **standards-based, hierarchical and modular** cabling infrastructure: cables, connectors, patch panels and pathways laid out in a **defined topology**, independent of the applications that run over it. Any device can be connected to any port by changing a **patch cord**, not by pulling new cable.

| | **Structured cabling** | **Point-to-point cabling** |
| --- | --- | --- |
| **Layout** | Cables run to patch panels in distribution areas, patch cords make the connections | Each device is cabled directly to the device it talks to |
| **Changes** | Moves, adds and changes are **patch cord changes** (minutes) | New cable runs, often a construction job under live load |
| **Growth** | Planned: spare capacity and pathways | Ad hoc: congestion and "spaghetti" |
| **Testing and documentation** | Each link is tested and recorded | Rarely documented |
| **Standards** | TIA-568, ISO/IEC 11801, EN 50173, TIA-942 | None |
| **Cost** | Higher first cost | Cheaper first, costlier over life |
| **Best for** | The permanent plant | Short, fixed links inside one rack (for example direct-attach cables) |

## 1.2 Why it matters (the importance of the cabling)

| Reason | Detail |
| --- | --- |
| **It is the physical layer of everything** | A faulty connector or cable can look like an application, switch or server fault |
| **Long life** | Cabling outlives several generations of equipment, so a poor choice is locked in for 10 to 15 years or more **[CHECK]** |
| **Hard and costly to change** | Re-pulling cable in a live hall is among the most disruptive and expensive operations. Labour dominates the cost, not the cable |
| **Small share of cost, large share of risk** | Cabling is a modest part of the build cost but a failure can affect many services |
| **Speed and density** | Link speeds climb (10G, 25G, 100G, 400G, 800G) and the cabling must carry them |
| **Reliability and availability** | Redundant, diverse pathways are part of Tier and Rated levels (Module 2) |
| **Operations** | Documented, labelled, tested cabling shortens troubleshooting and lowers MTTR |
| **Airflow and space** | Cable bulk blocks airflow and fills trays, which affects cooling (Module 9) |
| **Interoperability and warranty** | Standard components work across vendors, and many manufacturers give system warranties only on certified installations |

## 1.3 The subsystems (TIA-568)

| Subsystem | Role |
| --- | --- |
| **Entrance facility / entrance room** | Where outside plant cabling enters the building and connects to the internal cabling (the **demarcation** point with carriers) |
| **Equipment room / main distribution** | Houses core network equipment and the main cross-connect |
| **Backbone cabling** | Links the entrance room, main distribution and other distribution areas |
| **Telecommunications room** | Serves a floor or area (offices, operations centre) |
| **Horizontal cabling** | From the distribution area to the **outlet** at the equipment or work area |
| **Work area / equipment cords** | The patch cords at each end |

(The data centre version of these spaces, ER, MDA, IDA, HDA, ZDA and EDA, is in 11.4.)

## 1.4 The standards family

| Standard | Covers |
| --- | --- |
| **ANSI/TIA-568** series | Generic cabling: **568.0 and 568.1** (general), **568.2-E** (balanced twisted-pair copper, published November 2024), **568.3-E** (optical fibre, 2022), **568.5-1** (single-pair) |
| **ANSI/TIA-569** | Pathways and spaces |
| **ANSI/TIA-606** | Administration: labelling and records |
| **ANSI/TIA-607** | Bonding and grounding |
| **ANSI/TIA-758** | Outside plant (customer-owned) |
| **ANSI/TIA-942-C** | Data centre telecommunications infrastructure (May 2024) |
| **ISO/IEC 11801** series | International generic cabling, including **11801-5** for data centres |
| **ISO/IEC 14763-2 and -3** | Planning and installation, and testing of optical fibre cabling |
| **EN 50173** series | European generic cabling (including **EN 50173-5** for data centres) |
| **EN 50174-1, -2, -3** | Installation planning and practice, including **separation of power and data** |
| **EN 50600-2-4 / ISO/IEC 22237-5** | Telecommunications cabling infrastructure in data centres |

**Naming:** the American **TIA** names the **cable category** ("Category 6A"), the international **ISO/IEC** names the **channel class** ("Class EA"). They are close but not identical, and ISO limits are generally tighter. A specification that cites "TIA-568" without a revision letter is ambiguous: ask which edition.

## 1.5 Planning considerations

| Topic | What to decide |
| --- | --- |
| **Capacity and growth** | Port counts now and in 5 to 10 years. Leave **spare ports, spare fibres and spare pathway capacity**. A guide is to overprovision conduit and tray capacity by about **40%** at build time **[CHECK]** |
| **Speed roadmap** | Plan for the **next two or three speed steps** (25G, 100G, 400G, 800G), not just today's. The cabling must outlive the electronics |
| **Media choice** | Copper (Cat6A) vs. multimode vs. single-mode (11.2 and 11.3), driven by distance, speed, power and cost |
| **Topology** | Top-of-rack, end-of-row or middle-of-row (below), centralised or distributed cross-connects, and the TIA-942 spaces (11.4) |
| **Pathways and spaces** | Overhead trays vs. under-floor, tray fill (about 50%), separation of **fibre and copper**, and of **power and data** (EN 50174-2), 90° crossings, bend radius, fire stops |
| **Density** | Ports per rack, cabinet width (800 mm cabinets in distribution areas, Module 8), vertical managers |
| **Cable management and labelling** | A label scheme (TIA-606) agreed before installation, with both ends of every cable labelled |
| **Fire performance** | LSZH or equivalent, local fire classes (Module 6.15) |
| **Redundancy** | **Diverse A/B pathways**, redundant entrance and distribution areas (11.4 and 11.6) |
| **Testing and documentation** | Define the test standard, limits and reports in the specification (11.5) |
| **Warranty and installer competence** | Certified system and trained installers |
| **Environment** | Temperature, humidity, EMI (Module 7) and airflow (Module 9) |
| **Power over Ethernet** | PoE heating in bundles (11.2) |
| **Cost** | Compare **total cost**: cable, labour, optics and power over the life |

### Switch placement: top-of-rack, end-of-row, middle-of-row

| | **Top-of-rack (ToR)** | **End-of-row (EoR)** | **Middle-of-row (MoR)** |
| --- | --- | --- | --- |
| **Where the switch is** | In each rack (or each pair of racks) | At the end of the row | In the middle of the row |
| **Server links** | **Short in-rack** (direct-attach or short cords) | **Horizontal cabling** from every rack to the end of the row (up to 100 m copper) | Horizontal cabling to the middle (shorter runs than EoR) |
| **Cabling out of the rack** | **Few uplinks** (fibre) | Many cables per rack | Many cables per rack, shorter |
| **Number of switches** | Many (one or two per rack) | Fewer | Fewer |
| **Pros** | Least horizontal cabling, easy growth by rack, suits high speed | Fewer switches to manage, better port utilisation | Shorter cable runs than EoR |
| **Cons** | More switches, more uplink ports, power and licences, port waste in half-empty racks | Heavy cable bundles, harder to change, more tray space | As EoR, with mixed benefits |
| **TIA-942 mapping** | EDA with the switch as part of the equipment (HDA function in the rack) | HDA at the end of the row | HDA in the row |

**Worked example.** **20 racks** with **20 servers** each and **2 links per server**:

```
End-of-row:  20 × 20 × 2 = 800 horizontal cables to the end of the row
Top-of-rack: 800 short in-rack links, plus uplinks: 20 racks × 2 switches × 2 uplinks = 80 fibre uplinks
```

ToR cuts the **runs out of the racks** by a factor of 10 (800 down to 80) but needs 40 switches rather than a few.

---

# 11.2 Copper cables

## 2.1 Balanced twisted pair

A twisted-pair cable has **four pairs** of insulated copper conductors, **twisted** around each other. The twisting makes the two wires of a pair pick up noise equally, so the receiver (which reads the **difference**) rejects it (balanced signalling, 6.27 in `06-3`). Different twist rates in each pair reduce **crosstalk** between the pairs.

### Shielding notation (ISO/IEC 11801)

The code is **overall shield / pair shield + TP**:

| Code | Construction |
| --- | --- |
| **U/UTP** | **Unshielded** pairs, no overall shield (the common "UTP") |
| **F/UTP** | **Foil** overall, unshielded pairs |
| **U/FTP** | No overall shield, **foil on each pair** |
| **S/FTP** | **Braid** overall, **foil on each pair** |
| **SF/UTP** | Braid and foil overall, unshielded pairs |

Shielded cable gives better **EMI immunity and alien crosstalk** performance, but needs **proper bonding** (earthing) at the connectors and panels, and costs more and is stiffer. Shielded cables must be grounded properly (see 6.26 and 6.27: a screen that carries circulating current becomes a noise source).

## 2.2 Categories and classes

| TIA category | ISO/IEC class | Bandwidth | Supports (typical) | Maximum channel |
| --- | --- | --- | --- | --- |
| **Cat 5e** | Class D | 100 MHz | 1000BASE-T (1 Gb/s). Qualified links can carry 2.5GBASE-T | 100 m |
| **Cat 6** | Class E | 250 MHz | 1000BASE-T. **10GBASE-T only over a short, quiet channel** | 100 m for 1G. **About 37 to 55 m for 10G** |
| **Cat 6A** | **Class EA** | **500 MHz** | **10GBASE-T** | **100 m** |
| Cat 7 (ISO only) | Class F | 600 MHz | 10GBASE-T. Needs GG45 or TERA connectors for full performance | 100 m |
| Cat 7A (ISO only) | Class FA | 1,000 MHz | Specialised | 100 m |
| **Cat 8.1** | Class I | **2,000 MHz** | **25GBASE-T and 40GBASE-T** with RJ45 | **30 m** (two connectors) |
| **Cat 8.2** | Class II | 2,000 MHz | As Cat 8.1, with TERA or GG45 | **30 m** |

Key points:

- **TIA recognises Cat 5e, 6, 6A and 8 (8.1 and 8.2).** **Cat 7 and 7A are ISO classes only**, not TIA categories. A "Cat 7" cable fitted with ordinary RJ45 plugs cannot be certified as Cat 7 and behaves as a Cat 6A channel.
- **Cat 6A is the data centre default** for horizontal copper: full 10 Gb/s at 100 m.
- **Cat 6 and 10GBASE-T:** the figure usually quoted is 55 m, but TIA TSB-155-A is more conservative and puts it nearer **37 m** unless the crosstalk environment is favourable. Treat it as a **37 to 55 m range**.
- **Cat 8** is for **short switch-to-server links**. The 30 m limit is built into IEEE 802.3bq.
- **IEEE 802.3** defines the PHYs: **1000BASE-T** (ab), **2.5GBASE-T and 5GBASE-T** (bz), **10GBASE-T** (an), **25GBASE-T and 40GBASE-T** (bq). No BASE-T standard exists above 40G.

### The 100 m channel

```
Permanent link  (installed, certified)  ≤ 90 m
Patch cords at both ends (total)        ≤ 10 m
Channel (what the network uses)         ≤ 100 m
```

**Worked example.** A 90 m permanent link with **3 m + 3 m** of cords gives a 96 m channel (fine). With **15 m** of cords the total is 105 m, which is **outside** the standard, and the cords alone use more than the 10 m allowance.

## 2.3 Power over Ethernet (PoE)

| Standard | Power at the switch port |
| --- | --- |
| IEEE 802.3af (PoE) | 15.4 W |
| IEEE 802.3at (PoE+) | 30 W |
| IEEE 802.3bt Type 3 | up to 60 W |
| IEEE 802.3bt Type 4 | up to 90 W (some quote up to 100 W) |

**Heat in bundles:** current through the cable warms it, and a large bundle cannot shed the heat. High-power PoE in big bundles may need **larger conductors**, **smaller bundles**, or a higher category (TIA TSB-184-A). **Cat 5e is not recommended for Type 3 or Type 4** **[CHECK]**. The 2024 edition of TIA-568.2 also applies **DC resistance unbalance** testing to Cat 5e, 6 and 6A.

## 2.4 Connectors and cords

| Item | Notes |
| --- | --- |
| **RJ45 (8P8C)** | The standard connector. Wiring **T568A** (the TIA recommendation for new work) or **T568B** (common). **Never mix** the two on one cable or in one installation |
| **GG45 and TERA** | Non-RJ45 connectors for Cat 7 and Cat 8.2 |
| **Keystone jacks and patch panels** | Must be the **same category** as the cable: a Cat 6A cable on Cat 6 hardware certifies as Cat 6 |
| **Solid vs. stranded cable** | Solid copper for the permanent link, stranded for patch cords (higher attenuation, hence the 10 m allowance) |
| **Direct-attach copper (DAC)** | Twinax cable with fixed transceiver ends, **passive up to about 3 to 5 m**, for server to top-of-rack. Cheap, low power and low latency, but short and not structured cabling |
| **Active optical cable (AOC)** | Fixed fibre cable with transceivers, a few metres to tens of metres |

## 2.5 Installation rules **[CHECK]**

| Rule | Reason |
| --- | --- |
| **Keep untwisting at the connector to about 13 mm or less** | Crosstalk (NEXT) failures usually come from untwisted pairs |
| **Bend radius about four times the cable diameter** | Tight bends degrade return loss |
| **Pulling tension within the maker's limit (commonly about 110 N, 25 lbf)** | Stretching changes the pair geometry |
| **Don't over-tighten cable ties or crush cable** | Deforms the pairs |
| **Separate from power cables** | Interference (EN 50174-2, 6.18) |
| **Keep within the 90 m permanent link** | Standard limit |
| **Bond shielded cables correctly** | A floating or looped screen causes noise (6.26 and 6.27) |

## 2.6 Pros and cons of copper

| Pros | Cons |
| --- | --- |
| **Low cost** and familiar | **Distance limit** (100 m, and 30 m for Cat 8) |
| Easy to terminate and repair | **Bulky**: poor density and airflow compared with fibre |
| Supports **PoE** | **Speed ceiling**: practical to 10G (25 and 40G only over 30 m) |
| Large installed base | Higher **power per port** and latency at 10GBASE-T than short-reach optics **[CHECK]** |
| No optics to buy | **EMI and crosstalk** sensitivity (UTP) |
| | Heating in PoE bundles |
| | Needs shielding and bonding in electrically noisy areas |

**Where copper fits:** management and out-of-band networks, PoE devices (cameras, access points, sensors), 1G and 10G servers at moderate distance, and short in-rack links (DAC).

---

# 11.3 Fibre cables

## 3.1 Principle

Optical fibre carries data as **pulses of light** guided down a glass **core** by **total internal reflection** at the boundary with the **cladding**. It has **no electrical conductivity**, so it is **immune to EMI and ground potential differences** (6.27 in `06-3`).

| Type | Core | How it carries light |
| --- | --- | --- |
| **Single-mode (SMF)** | About **9 µm** | One path (mode). No modal dispersion. Long distances |
| **Multimode (MMF)** | **50 µm** (62.5 µm in old OM1) | Many paths. The pulses spread (modal dispersion), so **reach falls as the speed rises** |

**Light speed in fibre:** the refractive index is about 1.47, so light travels at about 3 × 10⁸ / 1.47 = **2.04 × 10⁸ m/s**, which is **about 4.9 µs per km** (rounded to **5 µs/km**). This matters for latency (11.7).

## 3.2 Fibre types

| Type | Core and use | Colour | Bandwidth (at 850 nm) |
| --- | --- | --- | --- |
| **OM1** | 62.5 µm, legacy LED era | Orange | Not laser-optimised |
| **OM2** | 50 µm, legacy | Orange | Not laser-optimised |
| **OM3** | 50 µm, **laser-optimised** (2002) | **Aqua** | 2,000 MHz·km |
| **OM4** | 50 µm, laser-optimised | **Aqua** (or erika violet) | **4,700 MHz·km** |
| **OM5** | 50 µm **wideband** (850 to 953 nm), for **SWDM** | **Lime green** | 4,700 MHz·km at 850 nm, plus 953 nm |
| **OS1a** | Single-mode, **inside plant** | Yellow | Attenuation up to 1.0 dB/km |
| **OS2** | Single-mode, **outside plant and long links** | **Yellow** | Attenuation up to 0.4 dB/km **[CHECK]** |

**Jacket colour is a convention, not a guarantee.** Always read the printed legend on the cable. Single-mode is specified as **ITU-T G.652.D** (or the bend-tolerant **G.657.A1**) and **ISO/IEC 11801 OS2**.

OM1 and OM2 will not support 10G beyond about 33 to 82 m, and should be replaced in a new design.

## 3.3 Reach of Ethernet over fibre

Reach is a property of the **optical application (the transceiver standard)**, not of the fibre alone. As the speed doubles, multimode reach roughly **halves**.

### Multimode (850 nm) **[CHECK]**

| Application | OM3 | OM4 | OM5 |
| --- | --- | --- | --- |
| **10GBASE-SR** | 300 m | **400 m** | 400 m |
| **40GBASE-SR4** | 100 m | **150 m** | 150 m |
| **100GBASE-SR4** | 70 m | **100 m** | 100 m |
| **100G SWDM4** (duplex, 4 wavelengths) | | 100 m | **150 m** |
| **400GBASE-SR8** (OM4) | | about 100 m | about 100 m |
| **400G SR4.2** (BiDi, 8 fibres) | | 100 m | **150 m** |
| **400GBASE-VR4, 800GBASE-VR8** (100G per lane) | 30 m | **50 m** | 50 m |

OM5 gives **no extra reach** with single-wavelength 850 nm optics. Its advantage appears only with **multi-wavelength (SWDM)** optics. Some vendor tables quote 550 m for 10G on OM4, but that is an engineered-link claim outside the IEEE value of 400 m.

### Single-mode **[CHECK]**

| Application | Reach |
| --- | --- |
| 10GBASE-LR, **100GBASE-LR4** | **10 km** |
| **400GBASE-DR4** (parallel, 8 fibres) | **500 m** |
| **400GBASE-FR4** (duplex) | **2 km** |
| 400G LR variants | about 6 to 10 km |
| **ER** optics | **40 km** |
| **ZR** optics | **80 km** (vendor and OIF convention) |
| Amplified DWDM | Hundreds to thousands of km |

For campus and building-to-building work, **OS2 with LR optics covers anything under 10 km**: the fibre will not be the limit, the optics will.

## 3.4 Choosing multimode or single-mode

| | **Multimode (OM4/OM5)** | **Single-mode (OS2)** |
| --- | --- | --- |
| **Fibre cost** | Higher per metre | Lower per metre |
| **Optics (transceivers)** | **Cheaper** (850 nm VCSEL) | More expensive (but the gap is narrowing) |
| **Reach** | Shrinks with speed (100 m at 100G and 400G) | Same fibre for any speed and any distance in the building |
| **Future-proofing** | Limited | **Excellent**: replace the optics, not the fibre |
| **Typical use** | Short links inside a hall (up to about 100 m) | **Backbone, trunks, campus, DCI**; more and more inside the hall |

**Illustration (vendor example, prices vary [CHECK]).** 1,600 transceivers: SR4 (multimode) at about $80 each is $128,000, and LR4 (single-mode) at about $500 each is $800,000, a difference of **$672,000**. The fibre is a small part of the cost, but a **trunk pulled once in OS2 never needs re-pulling** for a speed upgrade.

**Rules of thumb:** under about 100 m inside a hall, multimode is cost-effective. Over about 550 m, or for any trunk expected to outlive the current speed, use **single-mode**. If in doubt for a long-lived pathway, install the higher grade (OM4 rather than OM3, or OS2).

## 3.5 Connectors

| Connector | Notes |
| --- | --- |
| **LC** | Small **duplex** connector. The standard for equipment and patch panels |
| **SC** | Larger, older, still common in telecom |
| **MPO / MTP** | **Multi-fibre** push-on connector (12, 16, 24 fibres) for **parallel optics** (SR4, DR4, SR8) and high-density trunks |
| **UPC vs. APC** | Single-mode polish: **UPC** (blue) flat with a slight dome, **APC** (green) **angled 8°** to reduce back-reflection. **Never mate APC with UPC** |

### MPO polarity (TIA-568.3)

Polarity makes sure a transmit fibre at one end arrives at a receive position at the other. Three methods:

| Method | Description |
| --- | --- |
| **A** | Straight-through trunk (key-up to key-down) with a flip in one patch cord |
| **B** | Reversed trunk (key-up to key-up). Common for parallel optics |
| **C** | Pair-flipped trunk |

Choose **one method** and use it **end to end**. A common architecture is **MPO trunks between distribution areas, terminated in cassettes that break out to LC duplex** at the cabinet.

### Cleaning and inspection

**Dirty end-faces are the most common cause of failed fibre links.** Always **inspect, clean, inspect, then mate** (end-face inspection per IEC 61300-3-35), and keep dust caps on.

## 3.6 Transceivers and form factors

| Form factor | Typical speeds |
| --- | --- |
| **SFP / SFP+ / SFP28** | 1G / 10G / 25G |
| **QSFP+ / QSFP28** | 40G / 100G |
| **QSFP-DD / OSFP** | 400G / 800G |
| **DAC / AOC** | Short links, fixed ends |

Modules report **digital optical monitoring** values (temperature, supply voltage, transmit and receive power, bias current), used in monitoring (11.8).

## 3.7 Cable construction and handling **[CHECK]**

| Item | Notes |
| --- | --- |
| **Tight-buffered** | Indoor cable |
| **Loose-tube** | Outdoor and campus, water-blocked |
| **Ribbon and armoured** | High count, rodent and crush protection |
| **LSZH** | Low smoke, zero halogen jacket |
| **Bend-insensitive fibre** | Lower loss in tight bends (G.657.A1) |
| **Bend radius** | Commonly about 10 times the cable diameter at rest and about 20 times while pulling |
| **Fibre count** | Duplex links need 2 fibres. **SR4/DR4** use **8 of 12**. **400G SR8** uses **16**. TIA-942-C recommends **at least 2 fibres** on every run |

### Worked example 1: fibre count (SWDM vs. parallel)

400 links at 100G:

```
100GBASE-SR4 (parallel): 8 fibres per link   → 400 × 8 = 3,200 fibres
100G SWDM4 on OM5 (duplex): 2 fibres per link → 400 × 2 = 800 fibres   (75% fewer)
```

### Worked example 2: does the run fit?

A **120 m** run is needed for **100GBASE-SR4**. OM4 supports **100 m**, so it does **not** fit. Options: use OM5 with SWDM4 (150 m), use single-mode (LR4), shorten the run, or move the equipment.

### Worked example 3: the loss budget in a real channel

A 100GBASE-SR4 channel over OM4 has a maximum loss of about **1.5 dB** (400GBASE-SR4 over OM4 about 1.8 dB). The fibre itself contributes little:

```
OM4, 100 m: 0.1 km × 3.5 dB/km = 0.35 dB
```

| Connections (mated pairs) | Loss per pair | Total | Verdict (limit 1.5 dB) |
| --- | --- | --- | --- |
| 2 | 0.35 dB (low-loss) | 0.35 + 0.70 = **1.05 dB** | Passes |
| 4 | 0.50 dB | 0.35 + 2.00 = **2.35 dB** | **Fails** |

So the number of **patch points** is limited by the application's loss budget, not the 100 m reach. Each extra cassette or patch panel uses a share of it. Use **low-loss connectors** and keep the connection count down.

## 3.8 Pros and cons of fibre

| Pros | Cons |
| --- | --- |
| **High bandwidth and long distance** | Optics are an extra cost, and **cleanliness** is critical |
| **Immune to EMI**, no ground loops, no crosstalk | Cannot carry power (no PoE) |
| **Small and light**: density and airflow | Needs skilled termination and testing |
| **Electrically safe** between buildings | Loss budgets and polarity to manage |
| Future-proof (single-mode) | Bend sensitivity and fragility |
| Secure (hard to tap without detection) | Higher cost at the edge for low-speed ports |

---

# 11.4 Cabling as per TIA-942

## 4.1 The data centre spaces and the topology

ANSI/TIA-942-C defines a **hierarchical star topology** with these spaces:

```
 Carriers / access providers
        │              │
   ┌────┴─────┐   ┌────┴─────┐
   │ ER (1)   │   │ ER (2)   │       Entrance Room(s): carrier cables enter, demarcation
   └────┬─────┘   └────┬─────┘
        └──────┬───────┘   backbone cabling
          ┌────┴─────┐
          │   MDA    │              Main Distribution Area: Main Cross-connect (MC), core switches and routers
          └────┬─────┘
        backbone│  (to IDA and HDAs)
      ┌────────┴────────┐
 ┌────┴─────┐     ┌─────┴────┐
 │ IDA (opt)│     │   HDA    │      Intermediate (optional) and Horizontal Distribution Areas
 └────┬─────┘     └─────┬────┘      Horizontal Cross-connect (HC), aggregation / access switches
      │  horizontal cabling ≤ 100 m channel
   ┌──┴───┐        ┌────┴─────┐
   │ HDA  │        │ ZDA (opt)│     Zone Distribution Area: optional consolidation point
   └──┬───┘        └────┬─────┘
      │                 │
     EDA               EDA          Equipment Distribution Areas: racks and cabinets (equipment outlets)
```

| Space | Function | Contains |
| --- | --- | --- |
| **ER** (Entrance Room) | Where **external cabling from carriers enters** the building and meets the internal cabling. The **demarcation point** with the access provider | Carrier equipment, demarcation, protectors, the first patch panels. May be **outside the computer room** (better security) or combined with the MDA. Needs the **same power and cooling redundancy** as the computer room. **Several ERs** may be needed for resilience or distance |
| **MDA** (Main Distribution Area) | **The centre of the cabling system.** At least one is required | **Main cross-connect (MC)**, core switches and routers, SAN directors. All backbone cabling terminates here. Centrally located so that carrier and backbone distances are not exceeded |
| **IDA** (Intermediate Distribution Area) | **Optional** sub-distribution layer in very large facilities (several rooms, halls or floors) | Intermediate cross-connect (IC) between the MDA and the HDAs |
| **HDA** (Horizontal Distribution Area) | Distributes cabling to the equipment areas. At least one is required | **Horizontal cross-connect (HC)** and the LAN, SAN and management **access or aggregation switches** serving a zone (end-of-row or middle-of-row) |
| **ZDA** (Zone Distribution Area) | **Optional consolidation point** between the HDA and the EDAs | **Passive connections only** (no active equipment, no cross-connect). Cables from the HDA to the ZDA are shorter in number. Suits modular or pre-cabled halls |
| **EDA** (Equipment Distribution Area) | **The racks and cabinets** holding servers and storage | Patch panels or equipment outlets (EO), top-of-rack switches |
| **TR** (Telecommunications Room) | Serves **offices, operations centre and support spaces** outside the computer room | Office LAN switches |

### The cabling subsystems

| Subsystem | Between | Notes |
| --- | --- | --- |
| **Backbone cabling** | ER and MDA, MDA and IDA, MDA and HDA, IDA and HDA (and optionally HDA to HDA) | **Star topology.** Length depends on the application. **Centralised optical fibre cabling** (pull-through, interconnect or splice at the HDA) is allowed |
| **Horizontal cabling** | HDA (or ZDA) and the **EDA** | Maximum **100 m channel** for copper (**90 m** permanent link plus cords). A ZDA shortens the permissible length |

### Cross-connect and interconnect

| | **Cross-connect** | **Interconnect** |
| --- | --- | --- |
| **Method** | Two sets of patch panels, joined by **patch cords** | One panel: equipment connects with a cord directly to the permanent cable |
| **Flexibility** | **High**: changes are made at the panel | Lower: changes are made at the equipment |
| **Connections in the channel** | **More** (more loss, more places for faults) | **Fewer** (lower loss) |
| **Typical use** | Main distribution (MC, HC) where flexibility matters | Where loss is tight (high-speed fibre) |

TIA-942 also describes **basic**, **reduced** (small sites collapse ER, MDA and HDA into one space) and **distributed** (multiple ERs) topologies.

## 4.2 What is new in TIA-942-C (May 2024) **[CHECK]**

| Change | Detail |
| --- | --- |
| **800 mm cabinets** | **At least 800 mm** wide cabinets in the MDA, IDA and HDA (Module 8) |
| **Two fibres minimum** | **At least 2 optical fibres** (or 2 balanced twisted-pair cables) recommended for **every horizontal and backbone run** |
| **Single-pair cabling** | **Recognised** for horizontal IoT and control (for example SP1-400 up to 400 m and SP1-1000 up to 1,000 m) |
| **Any TIA-568.3 connector in distribution areas** | **LC or MPO** is still required at the **equipment outlet** |
| **Edge data centres** | The earlier edge addendum is folded in |
| **Immersion cooling** | A new annex on liquid immersion cooling compatibility |
| **Sustainability and monitoring** | Added provisions |

## 4.3 Recognised media

| Medium | Recognised for |
| --- | --- |
| **Balanced twisted pair, Cat 6A or better** (Cat 8 for short links) | Horizontal cabling |
| **Multimode fibre OM3, OM4, OM5** | Horizontal and backbone inside the hall |
| **Single-mode fibre OS1a, OS2** | Backbone, long runs, campus |
| **Single-pair balanced cable** | IoT and control |
| **Coaxial** | Legacy carrier circuits (E1, T1, T3), declining |

## 4.4 Pathways

| Rule | Detail |
| --- | --- |
| **Hot and cold aisles** | Telecom cabling is generally routed in or above the **hot aisle** (under an access floor), **power under the cold aisle**, so trays don't block cold air (Module 9) |
| **Separate fibre and copper** | In separate trays, and **protect fibre** from heavy copper bundles |
| **Separate power and data** | Per **EN 50174-2** (6.18 in `06-2`) |
| **Fill and bend radius** | Tray fill about 50%, minimum bend radius respected |
| **Rear clearance** | About **1 m** at the rear of racks is preferable |
| **Shared-tenant areas** | Solid-bottom tray, or a minimum height above the floor, for security |
| **Fire stops and coordination with other trades** | Penetrations sealed, routes coordinated with power, cooling and sprinklers |

## 4.5 Administration and labelling (TIA-606)

- **Every rack and cabinet is labelled front and back**, with a unique identifier. With an access floor, a common scheme uses the **floor tile coordinates** (for example AA, AB, BA).
- **Both ends of every cable** carry the same unique label, recorded in a database (**TIA-606**).
- Label **patch panels, ports, pathways and spaces**.
- Keep **records** current: they are the baseline for troubleshooting and monitoring (11.8).

## 4.6 Redundancy in the cabling (Rated levels)

| Rated level | Cabling infrastructure |
| --- | --- |
| **Rated-1 and 2** | A **single** path for each subsystem (Rated-2 adds redundant components) |
| **Rated-3** | **Redundant, physically separated pathways** (separate conduits and trays, not just separate ports), redundant access provider services |
| **Rated-4** | As Rated-3, plus **redundant entrance room, main distribution area and backbone cabling**, each **independent** |

**Secondary entrance room:** in TIA-942 guidance the carrier equipment must be able to **operate independently**, with about **20 m of separation** from the primary ER and **separate fire protection zones** **[CHECK]**. Redundancy also covers **maintenance holes and entrance pathways** and **access provider services** (two carriers on diverse routes, 11.6).

**A common audit failure:** routing "redundant" paths through a **shared tray "for simplicity"**. That satisfies nothing: the paths share a failure mode.

## 4.7 Worked examples

**Horizontal length.** The farthest rack is **60 m** (route length, not straight line) from the HDA, plus **10 m** of cords:

```
60 + 10 = 70 m channel (within the 100 m limit)
```

Always measure the **routed** length: cable follows trays, rises and drops, and slack loops, which often add **20 to 30%** to a straight-line estimate **[CHECK]**.

**Backbone fibre count.** The MDA serves **10 HDAs**, each with **24 fibres**, on **two separate paths** (A and B):

```
Fibres = 10 × 2 × 24 = 480 fibres
MPO-24 trunks = 480 / 24 = 20 trunks
```

---

# 11.5 Testing the cabling infrastructure

## 5.1 Why test, and what "testing" means

The cable plant is **passive and long-lived**: a poor termination, a kinked cable or a dirty connector will cause **intermittent errors for years**. Testing proves the plant meets the standard, gives a **baseline** for later troubleshooting, and is often required for the **manufacturer's warranty**.

| Level | Question it answers | Typical tool |
| --- | --- | --- |
| **Verification** | Is it connected correctly? (continuity, wiring, polarity) | Cable tester, tone generator, visual fault locator |
| **Qualification** | Can it support a **particular application** (for example 10GBASE-T)? | Qualification tester |
| **Certification** | Does it **meet the full standard** (TIA or ISO limits) with a recorded pass or fail? | **Certification tester (field certifier), OLTS and OTDR** |

Data centre acceptance uses **certification**, with the standard and limit set named in the specification.

## 5.2 Copper testing (TIA-568.2-E and ISO/IEC 11801)

Copper is tested as a **permanent link** (installed cabling, tested by the installer with permanent-link adapters, up to 90 m) or as a **channel** (end to end including patch cords, up to 100 m). The **permanent link is what the installer certifies**, the **channel is what the network uses**. A channel that just passes the permanent link test can still **fail** once cords are added.

| Parameter | What it measures | Typical cause of failure |
| --- | --- | --- |
| **Wire map** | Opens, shorts, crossed, reversed or **split pairs**, shield continuity | Miswiring, bad termination |
| **Length** | Electrical length of each pair | Over 90 m |
| **Propagation delay and delay skew** | Signal time and the difference between pairs | Very long or mismatched pairs |
| **Insertion loss (attenuation)** | Signal lost along the link | Over-length, poor connections, wrong cable |
| **NEXT and power-sum NEXT** | **Near-end crosstalk**: signal leaking between pairs at the transmit end | **Untwisted pairs at the connector** (the classic fault), poor connectors |
| **ACR-F and PS ACR-F** (formerly ELFEXT) | **Far-end crosstalk** relative to the signal | Cable and connector quality |
| **Return loss** | Reflections from impedance mismatch | Kinks, poor terminations, bad connectors |
| **Alien crosstalk (PS ANEXT, PS AACR-F)** | Noise coupled from **neighbouring cables** | Tight bundling (Cat 6A and 10GBASE-T), tested on a sample basis |
| **DC loop resistance and resistance unbalance** | Conductor resistance and its difference between wires of a pair | Poor contacts, thin conductors. Matters for **PoE** |

Other points **[CHECK]**:

- The **tester accuracy level** must suit the category: **Level 2G** for Cat 6A (to 500 MHz) and **Level VI** for Cat 8 (to 2 GHz).
- **Test cords and adapters** must be in good condition and the tester **calibrated** (typically annually).
- **Component matching**: a Cat 6A cable on Cat 6 connectors certifies as **Cat 6**.
- The report names the **limit set** (for example "TIA Cat 6A Channel"), the date, the tester serial number and calibration date.
- The **2024** TIA-568.2-E edition applies **DC resistance unbalance** testing to Cat 5e, 6 and 6A.
- Field testing is also covered by **EN 50346** (Europe).

## 5.3 Fibre testing (TIA-568.3-E and ISO/IEC 14763-3)

### Tier 1 and Tier 2

| | **Tier 1 (basic)** | **Tier 2 (extended)** |
| --- | --- | --- |
| **Instrument** | **OLTS** (optical loss test set: a light source and a power meter) | **OTDR** (optical time-domain reflectometer) **in addition to** Tier 1 |
| **Measures** | **End-to-end insertion loss**, **length** and **polarity** | A **trace** and an **event table** showing every connector, splice and fault with its distance, loss and reflectance |
| **Result** | Pass or fail against the loss budget | Locates and characterises each component |
| **When** | **Every** link | When specified, for **splices, outside plant, long links, or fault finding** |

**Tier 2 does not replace Tier 1.** An OTDR event loss is not comparable with the OLTS insertion loss and should not be compared with the calculated budget.

### OLTS procedure

1. **Inspect and clean** every connector end-face (IEC 61300-3-35) before testing.
2. **Set the reference** (zero the instrument) using the specified method (TIA-526-14, one-jumper or three-jumper). The **method must be recorded**, because 1-jumper and 3-jumper results can differ by about **0.75 dB** **[CHECK]**.
3. Test at **both wavelengths**: **850 and 1300 nm** for multimode, **1310 and 1550 nm** for single-mode.
4. Test **bidirectionally** where required, and average.
5. Verify **polarity** (a visual fault locator can do it) and record the **length**.

### OTDR procedure

- Use **launch and receive cables** (typically **100 to 500 m**) so that the first and last connectors are not lost in the instrument's **dead zone**.
- Set the correct **index of refraction**.
- Test in **both directions** for spliced links.
- Typical guidance: marginal event losses above about **0.75 dB for a connector**, **0.1 dB for a fusion splice** and **0.3 dB for a mechanical splice**.

### The loss budget

```
Maximum loss (dB) = fibre length (km) × attenuation (dB/km)
                  + number of mated connector pairs × 0.75 dB
                  + number of splices × 0.3 dB
```

TIA-568.3 maximum values **[CHECK]**:

| Item | Maximum |
| --- | --- |
| **Multimode fibre at 850 nm** | **3.5 dB/km** |
| **Multimode fibre at 1300 nm** | 1.5 dB/km |
| **Single-mode OS1a (inside plant)** | 1.0 dB/km |
| **Single-mode OS2** | 0.4 dB/km |
| **Mated connector pair** | **0.75 dB** |
| **Splice** | **0.3 dB** (fusion splices are typically 0.1 dB or less) |

**Worked example 1.** A **200 m OM4** link at 850 nm with **2 mated pairs** and **no splices**:

```
Budget = 0.2 × 3.5 + 2 × 0.75 = 0.7 + 1.5 = 2.2 dB
Measured 1.4 dB → pass.   Measured 2.5 dB → fail.
```

**Worked example 2.** A **2 km OS2** link with **4 mated pairs** and **1 splice**:

```
Budget = 2 × 0.4 + 4 × 0.75 + 1 × 0.3 = 0.8 + 3.0 + 0.3 = 4.1 dB
```

**The application can be tighter than the standard.** The standards' connector allowance (0.75 dB per pair) is generous. A 100GBASE-SR4 channel on OM4 allows only about **1.5 dB in total** (11.3), so the **tighter** of the two limits governs, and **low-loss connectors** are needed. When the equipment is known, use **the transceiver's own power budget**: the minimum transmit power minus the receiver sensitivity.

### Other fibre checks

| Test | Purpose |
| --- | --- |
| **End-face inspection** | Dirt and damage (IEC 61300-3-35). The commonest cause of failure |
| **Visual fault locator (VFL)** | Continuity, polarity, find breaks and tight bends |
| **Optical return loss (ORL)** | Reflections on single-mode links |
| **MPO testing** | Per-fibre loss and polarity of **multi-fibre** connectors, using MPO test equipment |
| **Chromatic and polarisation mode dispersion** | Long-haul and DCI links (11.7) |

## 5.4 Documentation and acceptance

| Item | Detail |
| --- | --- |
| **Test reports** | Native tester files plus a PDF summary, one result per link, with the **limit set**, wavelengths, reference method, cord type and length, date, tester and calibration |
| **As-built documentation** | Route diagrams, splice plans, labels, cable and reel data, bill of materials |
| **Acceptance criteria** | Written in the specification: standard, limits, sampling (100% of links for certification) |
| **Re-test** | After any move, add or change, and after repairs |
| **Baseline** | The first certified results become the **reference for future troubleshooting** |
| **Periodic checks** | Inspect and clean connectors, review monitoring data |

## 5.5 Common failures and quick causes

| Symptom | Likely cause |
| --- | --- |
| Link up but many errors at 10G on copper | NEXT or alien crosstalk, run too long for Cat 6, untwisted termination |
| Wire map fail | Miswiring or a split pair |
| High fibre loss on one link | Dirty or damaged end-face, bad connector, tight bend |
| High loss on all links through one panel | A contaminated adapter or cassette |
| Link works at 10G but not 100G | Loss budget or reach limit exceeded, wrong fibre grade |
| Intermittent faults after a move | A disturbed connector, a kinked cable |

---

# 11.6 Network redundancy

## 6.1 The principle

**Redundancy** means spare capacity or a second path. **Diversity** means the paths are **physically independent**, so that **one event cannot take out both**. Redundancy without diversity is a false comfort: two "redundant" cables in the **same duct** fail together (a **common-mode failure**).

Every layer needs its own redundancy:

| Layer | Redundancy |
| --- | --- |
| **Facility and pathways** | Two entrance rooms, separate pathways, separate trays |
| **Carriers** | Two or more carriers on **diverse routes** |
| **Devices** | Two of each network device, dual power supplies on A and B power |
| **Links** | Multiple links in a bundle (LAG) |
| **Logical** | Routing protocols, multipath, fast failure detection |
| **Site** | A second data centre (11.7) |

## 6.2 Physical diversity

| Measure | Detail |
| --- | --- |
| **Two entrance rooms or meet-me rooms** | In separate fire zones and about **20 m or more** apart **[CHECK]**, each able to operate independently, with its own power and cooling |
| **Separate entrance pathways** | **Different maintenance holes, conduits and building entry points**, ideally from **different directions** |
| **Two or more carriers** | On **physically diverse routes**: ask for **route maps**, because two carriers often share the same duct, bridge, river crossing or central office |
| **Diverse carrier equipment power** | Not both on the same power path |
| **Internal pathway diversity** | **A and B** cabling in **separate trays, conduits or rooms** (11.4) |
| **Separate A and B networks** | On different power paths and in different racks |
| **Avoid "backhoe fade"** | A single excavation cutting a single duct is the classic cause of lost connectivity |

## 6.3 Network architecture: spine and leaf

Modern data centres use a **spine-leaf (Clos) fabric** instead of the old three-tier tree.

```
        Spine 1   Spine 2   Spine 3   Spine 4
          │ ╲ ╱ │   │ ╲ ╱ │   │ ╲ ╱ │   │
   ┌──────┴──┴──┴───┴──┴──┴───┴──┴──┴───┴──┐   every leaf connects to every spine
 Leaf A    Leaf B    Leaf C    Leaf D       (leaf = top-of-rack, or end-of-row access switch)
   │ ╲       │ ╱       │         │
 Servers (each server dual-homed to two leaves)
```

| Element | Redundancy role |
| --- | --- |
| **Every leaf to every spine** | **All links are active** (routed, no blocked links) |
| **ECMP** (equal-cost multi-path) | Traffic is **spread across all spines**. Each flow is hashed (usually on the 5-tuple) to one path so packets stay in order |
| **At least two spines** | One spine is a single point of failure |
| **Dual-homed servers** | Two NICs, one to each of **two leaf switches** |
| **MLAG / vPC or EVPN multihoming (ESI-LAG)** | Presents the two leaves as one logical device to the server, using **LACP** (IEEE 802.1AX) |
| **Border leaves in pairs** | The pair connects the fabric to WAN routers, firewalls, internet and other sites |
| **eBGP routing (RFC 7938)** | Simple, scalable, fast failure containment. **BFD** detects link failure in milliseconds |
| **Layer 2 only at the edge** | Spanning Tree runs only on server-facing ports, with protections |
| **VRRP / HSRP** | Only if an application needs a static default gateway |
| **Out-of-band management network** | A **separate** network (and ideally a separate carrier) so you can still reach equipment when the production network is down |
| **Storage networks** | Two **independent SAN fabrics (A and B)**, dual-port adapters and multipathing |

### What a failure costs

With **N spines** and one failure, the remaining bandwidth is (N − 1) / N:

| Spines | Bandwidth left after one fails |
| --- | --- |
| 2 | 50% |
| 4 | **75%** |
| 8 | 87.5% |

### Oversubscription

```
Oversubscription = server-facing bandwidth / uplink bandwidth
```

**Worked example.** A leaf has **48 × 25G** server ports and **8 × 100G** uplinks:

```
Down = 48 × 25 = 1,200 Gb/s      Up = 8 × 100 = 800 Gb/s      Ratio = 1,200 / 800 = 1.5 : 1
Using only 4 uplinks: 1,200 / 400 = 3 : 1
After losing one of 8 uplinks: 1,200 / 700 = 1.71 : 1
```

Typical targets: about **3:1** for general compute, **1:1 (non-blocking)** for storage and **GPU training clusters**. **Plan for the failed state**, not just the healthy one.

## 6.4 Redundancy toward the outside (WAN and internet)

| Measure | Detail |
| --- | --- |
| **Dual routers and carriers** | Two edge routers, two carriers, diverse physical routes |
| **BGP multihoming** | BGP to two or more ISPs, so traffic survives the loss of one |
| **Internet exchange (IX) presence** | Direct peering lowers dependence on transit |
| **SD-WAN** | Policy-based use of several links (MPLS, internet, wireless) |
| **Cloud on-ramps** | Two circuits to each cloud region, on diverse paths |
| **DNS and anycast** | Resilient name resolution and service addresses |

## 6.5 Failure detection and recovery times

| Mechanism | Typical speed |
| --- | --- |
| **BFD** (bidirectional forwarding detection) | Milliseconds to detect |
| **Optical 1+1 protection** | Under **5 ms** |
| **IP and MPLS fast reroute, SONET/SDH rings** | Under **50 ms** |
| **ECMP across diverse paths at the IP layer** | Fast, increasingly used instead of transport protection |
| **Spanning Tree convergence** | Seconds (one reason to keep it out of the fabric) |

## 6.6 Availability arithmetic: why diversity matters

**Two independent links** of **99.9%** each, in parallel:

```
Availability = 1 − (0.001)² = 99.9999%
```

But if both links **share a duct** with an availability of **99.95%**, the duct is in series with both:

```
Availability = 0.9995 × 0.999999 = about 99.95%
```

The shared duct **caps** the result: the second link adds almost nothing. The gain comes only from **independent paths**.

## 6.7 Good practice

- **Draw the paths**: for every critical service, trace **each physical hop** (building entry, tray, cabinet, switch, power feed) and look for **shared** parts.
- **Test failover** on a schedule, in a controlled window, with a rollback plan.
- **Monitor** link state and optical power (11.8) so a degraded path is seen before the second one fails.
- **Keep the A and B networks identical**, so either can carry the full load.
- **Document** the routes, carriers and circuit IDs (TIA-606).
- **Change control**: most outages follow a change.

---

# 11.7 Building to building connectivity

## 7.1 Why sites are connected

| Use | Example |
| --- | --- |
| **Campus** | Several buildings or halls on one site sharing core services |
| **Disaster recovery** | A primary and a secondary data centre with replicated data |
| **Active-active and workload mobility** | Services running in two sites |
| **Metro and regional interconnect** | Multiple facilities in a city or region (data centre interconnect, **DCI**) |
| **Cloud and carrier connectivity** | Private links to cloud providers, internet exchanges and customers |
| **Back-end AI clusters spanning sites** | Very high bandwidth and low latency between sites |

## 7.2 Distance classes

| Class | Distance | Typical technology |
| --- | --- | --- |
| **Campus** | **Under 10 km** | Single-mode fibre with grey (direct-detect) optics, such as LR (10 km) |
| **Metro** | **10 to 120 km** | Passive DWDM, or **coherent pluggable optics (400ZR)** |
| **Regional and long haul** | **Over 120 km** (and beyond about 500 km) | Full coherent line systems with amplifiers |

**Technology follows distance:** the same 100G or 400G "pipe" needs a different optic at 500 m, at 10 km and at 80 km.

## 7.3 The options

| Option | What it is | Who runs the optics | Pros | Cons |
| --- | --- | --- | --- | --- |
| **Dark fibre** | An **unlit fibre pair** (owned, or leased on a long-term right of use). You light it with your own optics | **You** | Highest capacity at the lowest per-bit cost, **full control**, lowest latency, you choose the technology and upgrade freely | Needs a route to exist, long lead time, you run and monitor the optical layer, one fibre pair is one path unless you buy a second route |
| **Managed wavelength (DWDM service)** | A **provider-operated optical channel** (for example a 100G or 400G wavelength) between the two sites | **The provider** | High capacity, predictable point-to-point, no optical line system to run | Priced per circuit, limited to the provider's footprint, **your optics must fit the provider's system** |
| **Your own DWDM or CWDM system** | Multiplexers put many wavelengths on one fibre pair | **You** (on dark fibre) | Multiplies capacity of an existing fibre pair **without civil work** | Needs optical engineering, amplifiers and monitoring |
| **Carrier Ethernet (EPL / EVPL)** | **EPL**: private point-to-point Layer 2 Ethernet. **EVPL**: several virtual Ethernet services on one port | The provider | Simple, familiar to network teams | Capacity and sites limited by the provider, you depend on the service level agreement |
| **MPLS or IP VPN** | **Managed routed (Layer 3)** connectivity between many sites | The provider | Suits many sites, provider-managed routing and quality of service | Costlier per bit, less control, provider lock-in |
| **Internet with IPsec, or SD-WAN** | Encrypted tunnels over internet access, or policy-based use of several links | You, over the provider's access | **Cheapest and fastest to deploy**, good as a backup or for small sites | **No performance guarantee** (latency, jitter, loss), shared capacity |
| **Cloud on-ramps** | Private circuits to a cloud region (Direct Connect, ExpressRoute, Cloud Interconnect) | The provider | Predictable path to cloud services | Connects to a cloud, **not a site-to-site solution** by itself |
| **Wireless (microwave, free-space optics)** | Radio or laser link through the air | You | Quick for short gaps or as a backup where cable cannot be laid | **Lower capacity**, weather and alignment sensitivity **[CHECK]** |
| **Software-defined network as a service** | Programmable connectivity over provider infrastructure | The provider | Quick changes in sites and capacity | Dependence on the provider's platform |

Most real designs **combine** options: a **primary** (dark fibre or managed wavelength) plus a **physically diverse backup** (a second carrier route, an encrypted internet or SD-WAN path).

## 7.4 DWDM, CWDM and coherent optics

| Technology | How it works | Capacity (illustration) |
| --- | --- | --- |
| **CWDM** (coarse WDM) | A few widely spaced wavelengths (typically 8 or 18 channels) on one fibre pair | **8 channels × 10G = 80G** on a fibre pair that carried 10G |
| **DWDM** (dense WDM) | Many closely spaced wavelengths: **80 or more channels** on a 50 GHz grid in the C-band | 80 channels × 400G = **32 Tb/s** per fibre pair |
| **Coherent detection** | The receiver mixes the light with a local laser and uses a **digital signal processor** to recover amplitude, phase and polarisation, compensating dispersion | Reaches 1,000+ km, against under about 120 km for direct detection |
| **400ZR** (OIF Implementation Agreement, April 2020) | A **400G coherent pluggable** (QSFP-DD) for DCI. **Amplified** point-to-point links of up to **120 km**, and an **unamplified** application with an **11 dB** loss budget | Typically **80 to 120 km** amplified, **about 40 to 80 km** unamplified |
| **ZR+ and OpenZR+** | Higher-power, longer-reach, multi-rate coherent pluggables for regional links and ROADM networks | **Interoperability must be verified** between vendors |
| **800ZR** (agreement October 2024) | The same idea at 800G | Single-span amplified 80 to 120 km |

**IP over DWDM:** a coherent ZR module plugged **straight into a router or switch port** produces a DWDM-ready wavelength, so a separate **transponder shelf disappears**, saving space, power and cost. This holds best for **single-span, point-to-point** links you control end to end. Multi-hop ROADM networks often still favour transponders.

### Worked example: how far will 400ZR go unamplified?

The unamplified application allows **11 dB** of loss. Single-mode fibre at 1550 nm loses about **0.25 dB/km**. Allow **4 connectors at 0.5 dB** and **2 dB** of margin for ageing and repairs:

```
Fibre budget = 11 − (4 × 0.5) − 2 = 7 dB
Reach = 7 / 0.25 = about 28 km
```

The "80 to 120 km" figure is a **ceiling for amplified links under ideal conditions**, not a promise on your fibre. **Size a coherent link on the measured loss budget and OSNR (optical signal-to-noise ratio), not on nameplate kilometres.**

## 7.5 Distance and latency

Light travels at about **2 × 10⁸ m/s** in fibre, so each kilometre adds **about 5 µs one way** (10 µs round trip).

| Route length | One way | Round trip |
| --- | --- | --- |
| 10 km | 50 µs | 100 µs |
| 50 km | 250 µs | 500 µs |
| **100 km** | **500 µs (0.5 ms)** | **1.0 ms** |
| **120 km** | **600 µs** | 1.2 ms |

These figures are **propagation only**. Equipment, FEC and queuing add more. Adding more wavelengths adds **bandwidth, not speed**.

**Why it matters:**

- **Synchronous replication** (a write is acknowledged only after both sites have it) is practical only at **short distances**, commonly **up to about 100 km** (round trip about 1 ms) **[CHECK]**.
- **Asynchronous replication** tolerates much longer distances, at the cost of a non-zero **RPO** (Module 1).
- For **AI clusters**, conference estimates put the practical radius of cross-site work at about **50 km for inference** and about **100 km for synchronous training**, and far more for asynchronous training **[CHECK]**.
- The trade-off with **disaster recovery** distance (Module 3): far enough not to share hazards, near enough for the replication method.

## 7.6 Campus cabling between buildings

| Practice | Detail |
| --- | --- |
| **Use single-mode fibre (OS2), armoured or loose-tube outdoor cable** | Long reach, upgradable, **no electrical connection** between buildings |
| **Avoid copper between buildings** | Different ground potentials, lightning and surge currents (6.26 and 6.27) |
| **Underground duct banks with maintenance holes** | Protected from weather and vehicles. Aerial routes are more exposed |
| **At least two diverse routes into each building**, entering at **separate points** | A single trench is a single point of failure (11.6) |
| **Separate entrance rooms** | Each route terminates in its own entrance room (11.4) |
| **Spare fibres and spare ducts** | Fibre is cheap, trenching is not. Provision generously |
| **Outside plant standard** | **TIA-758** (customer-owned outside plant) **[CHECK]** |
| **Lightning protection and bonding** | Bond any metallic armour or strength member at the entrance |
| **Documentation and route records** | Fibre maps, duct plans, maintenance hole locations |

## 7.7 Resilience and security

| Topic | Practice |
| --- | --- |
| **Diverse routes** | Verify that the **primary and backup are physically independent** (11.6): different ducts, different directions, different central offices |
| **Protection** | Optical 1+1 protection (under 5 ms), rings, IP-layer ECMP over diverse paths |
| **Two sites, two carriers** | At least two carrier relationships for critical links |
| **Encryption** | **MACsec** (Layer 2) or **IPsec** (Layer 3) on inter-site links, with key management |
| **Physical protection** | Secure maintenance holes and entrances, route monitoring |
| **Monitoring** | Optical power, OTDR baseline, link state (11.8) |
| **Test both directions, under load and on the protected route** | Before the link is accepted |

## 7.8 Commercial and practical points

| Point | Detail |
| --- | --- |
| **Lead time** | New fibre routes and dark fibre take **months** (permits, rights of way, construction) |
| **Right of use / lease terms** | Term, price, maintenance responsibilities, who repairs and how fast |
| **Service level agreement** | Availability, repair time, latency commitments, credits |
| **Route verification** | Request **route diagrams and maintenance hole lists** and check diversity yourself |
| **Total cost** | Fibre or circuit, optics, line system, power, monitoring and operations |

---

# 11.8 Network monitoring

## 8.1 Why monitor

| Reason | Benefit |
| --- | --- |
| **Detect faults before users do** | Shorter detection time (MTTD) |
| **Locate the fault quickly** | Shorter repair time (MTTR), so higher availability |
| **Capacity planning** | See growth in traffic and ports before they run out |
| **Check service levels** | Evidence for SLAs and customer reports |
| **Security** | Unusual flows and failed logins are visible |
| **Change validation** | Confirm that a change did what was intended |

**Monitoring and availability:** availability = MTBF / (MTBF + MTTR). With an MTBF of **5,000 hours**:

```
MTTR 4 hours: 5,000 / 5,004 = 99.920%
MTTR 1 hour:  5,000 / 5,001 = 99.980%
```

Faster detection and diagnosis cut the **repair time**, which lifts availability without changing the equipment.

## 8.2 What to monitor

| Layer | What to watch |
| --- | --- |
| **Physical layer** | **Optical power** (transmit and receive), transceiver temperature, cable and connector health, link up or down. The certified test results are the **baseline** |
| **Link** | Port status, **errors (CRC and frame errors)**, discards, utilisation, flaps |
| **Device** | CPU, memory, temperature, fans, power supplies |
| **Routing and switching** | BGP and routing neighbours, route flaps, spanning tree and MLAG state |
| **Traffic** | Flows by source, destination, port and protocol |
| **Latency and quality** | Delay, jitter and packet loss, measured by synthetic probes |
| **Security** | Failed logins, configuration changes, unexpected flows |
| **Inventory and topology** | Which device connects to which, firmware versions |
| **Configuration** | Backups, and detection of unauthorised changes |
| **Environment** | Temperature, humidity and power at the network equipment (Modules 6, 9 and 14) |

## 8.3 Protocols and tools

| Tool or protocol | What it does |
| --- | --- |
| **SNMP** (v1, v2c, **v3**) | **Polling** of device counters and status, plus **traps** (device-initiated alerts), using MIBs. **Use v3** (authentication and encryption) |
| **Syslog** | Event messages from devices to a central log collector or SIEM |
| **NetFlow, IPFIX, sFlow** | **Flow records or sampled packets**: who is talking to whom, how much. Used for capacity, top talkers and attack detection |
| **Streaming telemetry (gNMI, gRPC)** | The device **pushes** data continuously, model-driven, with high frequency. Replaces or complements SNMP polling |
| **LLDP / CDP** | Neighbour discovery: builds the **topology map** automatically |
| **ICMP (ping, traceroute), BFD** | Reachability and fast failure detection |
| **Port mirroring, network TAPs, packet capture** | Deep inspection and troubleshooting |
| **Digital optical monitoring (DOM/DDM)** | Transceivers report temperature, voltage, bias current and **transmit and receive power** |
| **OTDR** | Trace of a fibre: finds degradation and breaks. Baseline versus now |
| **DCIM and building management** | Correlates network assets with power, cooling and space |
| **Automated infrastructure management (AIM)** | **Intelligent patch panels** that detect what is plugged in and keep the cabling database accurate (ISO/IEC 18598) **[CHECK]** |
| **Dashboards and metrics systems** | For example Prometheus and Grafana, or commercial network and observability platforms |

**Correlate logical and physical data.** A BGP flap can be a **logical** fault or a **physical** one (a dirty connector or a micro-bend). Only combining routing data with **optical power and error counters** tells them apart.

## 8.4 Polling versus streaming

SNMP gives an **average over the polling interval** (commonly 1 to 5 minutes). Short bursts disappear into the average.

**Worked example.** A 100G link runs at **100% for 30 seconds**, then idle, in a **5-minute (300 s)** polling window:

```
Average utilisation seen by the poller = 30 / 300 = 10%
```

The monitoring shows a calm link while the application suffered 30 seconds of congestion and packet loss. **Streaming telemetry** at 1-second intervals shows the burst.

## 8.5 Optical power trending

Receive power drifts as connectors get dirty, cables are bent, or patching is disturbed.

**Worked example.** A link's **receive power** falls from **−2.0 dBm** to **−6.5 dBm** over several months:

```
Loss increase = −2.0 − (−6.5) = 4.5 dB
```

A 4.5 dB change is large (the link's loss has nearly tripled in power terms) and points to a **dirty or damaged connector, a bend, or a cable being disturbed**. Trending it **before** the link fails is exactly what monitoring is for.

## 8.6 Alarms, thresholds and operations

| Practice | Detail |
| --- | --- |
| **Baselines and thresholds** | Set alerts from **normal behaviour** and the standard's limits. Typical utilisation alerts fire at about **70 to 80%** sustained **[CHECK]** |
| **Avoid alert fatigue** | Alert on what needs action. Group related alarms (a failed spine causes many) |
| **Escalation and runbooks** | Who is called, in what order, and what steps to take |
| **NOC** | A staffed network operations centre (Module 3) with dashboards and procedures |
| **Out-of-band monitoring** | The monitoring must **not depend on the network it watches**. Use a separate management network |
| **Redundant monitoring** | The monitoring system itself needs backup and a second collector |
| **Secure the tools** | SNMPv3, authentication, restricted access, log retention |
| **Integrate with change management** | Pre- and post-change checks, and record the baseline after each change |
| **Link cabling records to monitoring** | The labelled cabling database (TIA-606) tells you which cable a port really connects to |
| **Capacity planning** | Trend utilisation, port usage, optical power and growth, to plan upgrades before limits are reached |

## 8.7 Key metrics

| Metric | Meaning |
| --- | --- |
| **Availability** | Time the service is up |
| **Latency, jitter, packet loss** | Quality of the path |
| **Utilisation** | Share of link capacity in use |
| **Error rate** | CRC, FCS and discard counts |
| **MTTD / MTTR** | Mean time to detect / repair |
| **Capacity headroom** | Spare ports, bandwidth and optical margin |

---

## Glossary

| Term | Meaning |
| --- | --- |
| Structured cabling | Standards-based, hierarchical cabling with patch panels and defined pathways |
| ER, MDA, IDA, HDA, ZDA, EDA | Entrance room, main, intermediate, horizontal, zone and equipment distribution areas |
| MC / IC / HC | Main / intermediate / horizontal cross-connect |
| EO | Equipment outlet |
| Horizontal / backbone cabling | HDA or ZDA to equipment / between distribution areas |
| Permanent link / channel | Installed cabling (90 m) / end to end with cords (100 m) |
| Cross-connect / interconnect | Patch panels joined by cords / direct connection to the equipment |
| ToR / EoR / MoR | Top-, end- or middle-of-row switch placement |
| Cat 5e / 6 / 6A / 8 | TIA twisted-pair categories (100 / 250 / 500 / 2,000 MHz) |
| Class D / E / EA / F / FA / I / II | ISO/IEC channel classes |
| U/UTP, F/UTP, S/FTP | Cable shielding notations |
| PoE | Power over Ethernet |
| DAC / AOC | Direct-attach copper / active optical cable |
| OM1 to OM5 | Multimode fibre grades |
| OS1a / OS2 | Single-mode fibre (inside plant / outside plant) |
| LC / SC / MPO | Fibre connectors (duplex / duplex / multi-fibre) |
| UPC / APC | Flat polish / 8° angled polish |
| SWDM | Shortwave wavelength division multiplexing (over OM5) |
| Parallel optics | Several fibres per direction (SR4, DR4, SR8) |
| OLTS / OTDR | Optical loss test set / optical time-domain reflectometer |
| Tier 1 / Tier 2 testing | Loss, length and polarity / plus OTDR trace |
| Loss budget | Maximum allowed loss: fibre + connectors + splices |
| Dead zone | Distance after a reflective event where an OTDR can't measure |
| NEXT / ACR-F / return loss | Near-end crosstalk / far-end crosstalk relative to the signal / reflections |
| Redundancy / diversity | Spare capacity / physical independence of paths |
| Common-mode failure | One cause taking out several "redundant" paths |
| Spine-leaf (Clos) | Fabric where every leaf connects to every spine |
| ECMP | Equal-cost multi-path routing |
| MLAG / EVPN multihoming | Dual-homing a server to two switches |
| Oversubscription | Server-facing bandwidth divided by uplink bandwidth |
| BFD | Bidirectional forwarding detection |
| DCI | Data centre interconnect |
| Dark fibre / wavelength service | Unlit fibre you light yourself / a provider-operated optical channel |
| CWDM / DWDM | Coarse / dense wavelength division multiplexing |
| 400ZR / ZR+ | 400G coherent DCI pluggable / extended-reach versions |
| IP over DWDM | Coherent optics in the router, no separate transponder |
| EPL / EVPL | Ethernet private line / Ethernet virtual private line |
| SNMP / syslog / NetFlow / IPFIX / sFlow | Monitoring protocols |
| gNMI / streaming telemetry | Push-based, model-driven device data |
| DOM / DDM | Digital optical monitoring in transceivers |
| AIM | Automated infrastructure management (intelligent patching) |
| MTTD / MTTR | Mean time to detect / repair |

## Exam takeaways

**11.1 (structured cabling, planning)**

- **Structured cabling** is standards-based, hierarchical and modular: changes are **patch cord changes**. It is the **longest-lived, hardest-to-change** layer (about 10 to 25 years), so plan for **growth, the speed roadmap, spare pathways and diversity**.
- **TIA names categories, ISO names classes.** TIA-568.2-E (copper), 568.3-E (fibre), TIA-569, -606, -607, TIA-942-C. ISO/IEC 11801, EN 50173/50174.
- **ToR** has few uplinks out of each rack but many switches. **EoR** has many horizontal cables and fewer switches.

**11.2 and 11.3 (copper and fibre)**

- **Copper:** **Cat 5e 100 MHz, Cat 6 250 MHz, Cat 6A 500 MHz, Cat 8 2,000 MHz.** **Cat 6A: 10G at 100 m** (the default). **Cat 6: 10G only about 37 to 55 m.** **Cat 8: 25 and 40G at 30 m.** **Channel = 90 m permanent link + 10 m cords.** Cat 7 is **ISO only**. **S/FTP** = braid overall and foil per pair. **Never mix T568A and T568B.** PoE: **15.4, 30, 60 and 90 W**. DAC about 3 to 5 m.
- **Fibre:** **OS2 9 µm single-mode**, **OM 50 µm multimode**. **OM3 aqua 2,000, OM4 aqua or violet 4,700, OM5 lime green, OS2 yellow.** Multimode reach **halves as speed doubles**: **10G 300/400 m, 40G 100/150 m, 100G 70/100 m (OM3/OM4).** OM5 helps only with **SWDM** (100G 150 m). **Single-mode: LR 10 km, ER 40 km, ZR 80 km, DR4 500 m, FR4 2 km.** Multimode for short runs (cheap optics), **single-mode for trunks and anything long-lived**.
- **MPO** for parallel optics (**polarity A, B, C**, one method end to end). **UPC blue, APC green, never mixed.** **Clean and inspect** every connector.
- **The loss budget limits the number of connections**, not only distance.

**11.4 (TIA-942 topology)**

- **ER, MDA (MC, core), IDA (optional), HDA (HC), ZDA (optional, passive), EDA.** **Backbone in a star**, **horizontal up to 100 m channel (90 m permanent link).** At least one MDA and one HDA.
- **TIA-942-C:** **800 mm cabinets** in MDA, IDA and HDA, **at least 2 fibres** on each run, **single-pair** cabling, edge and immersion content.
- **Rated-3/4:** **physically separated pathways**, secondary ER about **20 m** apart. **A shared tray is not redundancy.** Telecom in the **hot aisle**, power in the cold aisle, **fibre and copper separate**, **label both ends** (TIA-606).

**11.5 (testing)**

- **Verification, qualification, certification.** Copper: **permanent link vs. channel**; tests **wire map, length, insertion loss, NEXT, PS NEXT, ACR-F, return loss, alien crosstalk, DC resistance**; **Level 2G for Cat 6A, Level VI for Cat 8**.
- **Fibre: Tier 1 = OLTS** (loss, length, polarity, **two wavelengths**, bidirectional); **Tier 2 = OTDR added** (launch cables, event table). **Loss budget = length × attenuation + 0.75 per connector pair + 0.3 per splice**; **3.5 dB/km at 850 nm, 0.4 dB/km OS2**. **The application budget can be tighter.** Record the reference method, clean first, keep reports and baselines.

**11.6 and 11.7 (redundancy, multiple sites)**

- **Redundancy is spare capacity, diversity is independence.** **A shared duct is a common-mode failure.** Two entrance rooms, two carriers on diverse routes, A/B pathways.
- **Spine-leaf:** every leaf to every spine, **ECMP**, at least **2 spines** (**4 spines: 75% after one fails**), **dual-homed servers** (MLAG or EVPN multihoming), **border leaves in pairs**, **eBGP and BFD**, **out-of-band management**. **Oversubscription = down / up.**
- **Sites:** **dark fibre, managed wavelength, own DWDM/CWDM, Carrier Ethernet (EPL/EVPL), MPLS/IP VPN, internet + IPsec/SD-WAN, cloud on-ramps, wireless.** Distance classes **campus <10 km, metro 10 to 120 km, long haul >120 km.** **400ZR: 80 to 120 km amplified, 11 dB unamplified.** **5 µs per km** (100 km = 0.5 ms one way, 1 ms round trip). **OS2 between buildings, diverse routes, no copper.** Encrypt (MACsec, IPsec).

**11.8 (monitoring)**

- **SNMP** (use v3), **syslog**, **NetFlow/IPFIX/sFlow**, **streaming telemetry (gNMI)**, **LLDP**, **DOM** and **OTDR**, **DCIM**. **Polling averages hide bursts** (30 s at 100% in 300 s shows 10%). **Correlate logical and physical data.** Trend optical power. **Out-of-band** monitoring. Faster detection lowers MTTR and raises availability.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **ANSI/TIA-568.2-E** (November 2024) | Copper categories, channel and permanent link, testing, DC resistance unbalance |
| **ANSI/TIA-568.3-E** (2022) | Optical fibre cabling, loss limits, connector and splice allowances |
| **ANSI/TIA-568.5-1** | Single-pair cabling |
| **TIA TSB-155-A** | 10GBASE-T over Cat 6 (37 to 55 m) |
| **TIA TSB-184-A** | Power delivery over twisted pair, heating in bundles |
| **ANSI/TIA-942-C** (May 2024) | Topology (ER, MDA, IDA, HDA, ZDA, EDA), 800 mm cabinets, two-fibre minimum, redundancy |
| **ANSI/TIA-569, -606, -607, -758** | Pathways and spaces, administration, bonding, outside plant |
| **TIA-526-14 (OFSTP-14), TIA-526-7** | Installed multimode and single-mode insertion loss test methods |
| **TIA-492AAAC / AAAD / AAAE** | OM3, OM4, OM5 fibre specifications |
| **ISO/IEC 11801** series (including **11801-5**) | Generic cabling classes and optical channel limits |
| **ISO/IEC 14763-2 and -3** | Planning, installation and testing |
| **EN 50173** series, **EN 50174-1, -2, -3**, **EN 50346** | European cabling, installation and separation, field testing of copper |
| **EN 50600-2-4 / ISO/IEC 22237-5** | Telecommunications cabling infrastructure in data centres |
| **IEEE 802.3** (an, bq, bz, af/at/bt, ae, ba, cm, cu, and the dj and ds projects) | Ethernet PHYs, PoE, multimode and single-mode reach, and the roadmap |
| **ITU-T G.652.D / G.657.A1** | Single-mode fibre |
| **IEC 61300-3-35** | Fibre end-face inspection |
| **OIF 400ZR (April 2020) and 800ZR (October 2024) Implementation Agreements** | Coherent DCI pluggables |
| **RFC 7938** (BGP in data centres), **RFC 7432** (EVPN), **IEEE 802.1AX** | Routing, multihoming and link aggregation in spine-leaf fabrics |
| **ISO/IEC 18598** | Automated infrastructure management |
| **Uptime Institute and TIA-942 Rated levels** | Redundant pathways and entrance rooms |
| Vendor and industry technical papers (NVIDIA, Cisco, Arista, Corning, Fluke Networks, MapYourTech and others, 2026) | Reach tables, oversubscription examples, DCI options, test practice |
| Standard optics and network engineering | Latency, loss budget, availability and oversubscription formulas |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
