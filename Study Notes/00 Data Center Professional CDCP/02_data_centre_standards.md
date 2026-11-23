# Module 2: Data Centre Standards

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section in these notes |
| --- | --- | --- |
| 2.1 | Standards | Sections 1 to 4 |
| 2.2 | Additional Standards | Section 5 |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-2-data-centre-standards) |

**Objectives (from your slide).** After this module you should be able to describe and understand: data centre standards and guidelines, standards for sub-components, and international vs. national standards.

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course says something different, use your course. Editions named here were current in November 2026 and will change over time.

---

# Lesson 2.1: Standards

## 1. Why standards matter

Standards give the industry:

- a **common language** (everyone means the same thing by "Tier III" or "Class 3"),
- a **proven design baseline** instead of reinventing everything,
- a way to **measure and compare** facilities (customers, auditors, insurers),
- a basis for **certification** and **contracts** (SLAs, procurement),
- better **safety, quality and interoperability**.

### Standard vs. guideline vs. regulation

| | Wording | Status | Example |
| --- | --- | --- | --- |
| **Standard** | "shall" (requirements) | Voluntary, unless a contract, customer or law requires it. Needed to claim compliance | ANSI/TIA-942, EN 50600 |
| **Guideline / best practice** | "should" (recommendations) | Advice | ASHRAE thermal guidelines, EU Code of Conduct |
| **Regulation / code** | Legal text | **Mandatory by law** | Building codes, electrical regulations (NEC, BS 7671), fire codes |

**Precedence:** law and codes **override** voluntary standards. If a standard conflicts with a local code, the code wins.

### Standard vs. certification

| Term | Meaning |
| --- | --- |
| **Standard** | The document that defines the requirements |
| **Compliance** | The owner states that the facility meets the standard |
| **Certification** | An **independent body** audits the facility and issues a certificate |

## 2. Who writes standards

| Level | Body | Examples |
| --- | --- | --- |
| **International** | **ISO** (International Organization for Standardization), **IEC** (International Electrotechnical Commission), joint **ISO/IEC**, **ITU** (telecommunications) | ISO/IEC 22237, ISO/IEC 27001, IEC 62040 |
| **Regional (Europe)** | **CEN**, **CENELEC**, **ETSI** | EN 50600, EN 50310, ETSI EN 300 253 |
| **National** | ANSI (USA), BSI (UK), DIN (Germany), NEN (Netherlands), AFNOR (France) | ANSI/TIA-942, BS 7671, DIN VDE 0100 |
| **Industry associations** | TIA, BICSI, IEEE, NFPA, ASHRAE, The Green Grid, Uptime Institute | ANSI/TIA-942, BICSI 002, NFPA 75, ASHRAE TC 9.9 |

**How they relate (Europe):** an international standard (ISO/IEC) can be adopted by CENELEC as an EN, and each member country then publishes it as a national standard (for example "BS EN", "DIN EN", "NEN-EN"). EN 50600 and ISO/IEC 22237 are deliberately aligned.

### International vs. national standards

| | International | National |
| --- | --- | --- |
| Scope | Many countries, global use | One country |
| Development | Consensus across member bodies | National committee, often adapting international ones |
| Strength | Common approach for global operators | Matches local law, codes and practice |
| Weakness | May need local adaptation | May not suit sites abroad |

**Choose standards by where the site is and who the customers are.** A US-based design might follow TIA-942. A European one will likely follow EN 50600. A global operator may meet both.

## 3. The main data centre standards

| Standard | Origin | What it is |
| --- | --- | --- |
| **Uptime Institute Tier Standard** | Uptime Institute (private organisation) | A classification of **topology** (redundancy and maintainability), Tier I to IV, plus **Operational Sustainability** |
| **ANSI/TIA-942** | USA (TIA) | The data centre **telecommunications infrastructure** standard: architecture, telecommunications, electrical, mechanical, fire, security. **Rated 1 to 4** |
| **EN 50600** / **ISO/IEC 22237** | Europe (CENELEC) / International | A multi-part **facilities and infrastructure** standard with **Availability Classes 1 to 4**, **Protection Classes 1 to 4** and **Energy Efficiency Enablement Levels** |
| **ANSI/BICSI 002** | BICSI | Design and implementation **best practices** that complement the standards above. A companion, **BICSI 009**, covers **operations** |

**Editions to know [CHECK]:** ANSI/TIA-942-C (published May 2024, replacing 942-B; it folds in the edge data centre addendum and adds guidance on higher rack densities and liquid cooling), ANSI/BICSI 002-2024 and BICSI 009-2024. ISO/IEC 22237 is published part by part, with some parts still technical specifications.

### Uptime Institute Tiers

| Tier | Name | Redundancy | Distribution paths | Key trait | Commonly quoted availability | Downtime per year |
| --- | --- | --- | --- | --- | --- | --- |
| **I** | Basic Capacity | N | Single | No redundancy. Maintenance needs a shutdown | 99.671% | about 28.8 h |
| **II** | Redundant Capacity Components | N+1 | Single | Redundant components, but a single path | 99.741% | about 22 h |
| **III** | Concurrently Maintainable | N+1 | Multiple (one active) | Any component can be maintained **without shutting down IT** | 99.982% | about 1.6 h |
| **IV** | Fault Tolerant | 2N or 2(N+1) | Multiple active | Survives **any single failure** with no impact | 99.995% | about 26 min |

> **[CHECK]** The percentages are the commonly quoted figures. Uptime itself says the Tier is a statement about **topology**, not a guaranteed availability number.

**The two key jumps:**

- **Tier II to III:** adds **concurrent maintainability** (multiple distribution paths, so maintenance needs no shutdown).
- **Tier III to IV:** adds **fault tolerance** (a whole path can fail with no impact).

**Uptime certifications [CHECK]:**

| Certification | What it covers |
| --- | --- |
| **Tier Certification of Design Documents** | The design on paper |
| **Tier Certification of Constructed Facility** | The built facility, tested on site |
| **Operational Sustainability** | How the site is **managed and operated**, its building characteristics and its location |

Uptime's point: good topology alone does not protect you if the site is badly operated, so **management and operations** carry weight.

### ANSI/TIA-942

TIA-942 describes how to **build and configure** a data centre to the reliability level the owner needs, with four **ratings**:

| Rating | Description |
| --- | --- |
| **Rated-1** | Basic: single-capacity components and a single, non-redundant path |
| **Rated-2** | Redundant capacity components, but a single path |
| **Rated-3** | Concurrently maintainable |
| **Rated-4** | Fault tolerant |

It covers **architecture, telecommunications cabling, electrical, mechanical, fire protection, physical security and monitoring**. It is also the basis of the **TIA-942 certification programme**, in which facilities are independently audited against the ratings. It applies to enterprise, colocation, hyperscale and edge data centres.

### EN 50600 and ISO/IEC 22237

EN 50600 (Europe) and ISO/IEC 22237 (international) are closely aligned **multi-part** standards. They classify a facility on three criteria:

| Criterion | Classes |
| --- | --- |
| **Availability** | Availability Class 1 to 4 (for power supply, power distribution, environmental control and telecommunications cabling) |
| **Physical security** | Protection Class 1 to 4 |
| **Energy efficiency** | Energy Efficiency Enablement Levels (the facility's ability to measure and manage energy use) |

The class is chosen from a **business risk and operating cost analysis**.

| EN 50600 part | Topic |
| --- | --- |
| EN 50600-1 | General concepts |
| EN 50600-2-1 | Building construction |
| EN 50600-2-2 | Power supply and distribution |
| EN 50600-2-3 | Environmental control (cooling) |
| EN 50600-2-4 | Telecommunications cabling infrastructure |
| EN 50600-2-5 | Security systems |
| EN 50600-2-6 | Management and operational information systems |
| EN 50600-3-1 | Management and operational information |
| EN 50600-4-x | Key performance indicators (PUE, REF, ERF, CUE, WUE) |

**[CHECK]** ISO/IEC 22237 has a similar structure (parts 1 to 7), with its own numbering. The KPI series is **ISO/IEC 30134**, mirrored in Europe by EN 50600-4.

**Out of scope:** both series leave **safety and EMC** to other standards and regulations, and don't cover the selection of IT equipment.

### BICSI 002 and 009

BICSI 002 is a **design standard** with **best practices** on every major system (site, architecture, electrical, mechanical, telecommunications, fire, security, commissioning). Its approach is to complement TIA, CENELEC and ISO/IEC. It uses its own **Class F0 to F4** facility classes **[CHECK]**.

### Comparison

| | Uptime | TIA-942 | EN 50600 / ISO/IEC 22237 | BICSI 002 |
| --- | --- | --- | --- | --- |
| Type | Classification of topology and operations | Prescriptive infrastructure standard | Holistic multi-part standard | Design best practice |
| Levels | Tier I to IV | Rated 1 to 4 | Availability Class 1 to 4 | Class F0 to F4 **[CHECK]** |
| Focus | Redundancy, maintainability, operations | Telecoms, plus power, cooling, security | Whole facility, with security and efficiency classes | Design practice |
| Certification | Uptime | TIA-942 programme | Accredited auditors | (guidance) |

**Same idea, different words.** Don't mix the terms in an exam answer:

| Uptime | TIA-942 | EN 50600 / ISO/IEC 22237 |
| --- | --- | --- |
| Tier I to IV | Rated 1 to 4 | Availability Class 1 to 4 |

## 4. Standards for sub-components

A data centre is made of subsystems, each with its own standard family:

| Area | Typical standards |
| --- | --- |
| **Electrical installation** | IEC 60364, NFPA 70 (NEC), BS 7671 |
| **UPS** | IEC 62040 |
| **Cabling** | ISO/IEC 11801, ANSI/TIA-568, EN 50173, EN 50174 |
| **Pathways and spaces** | ANSI/TIA-569 |
| **Administration and labelling** | ANSI/TIA-606 |
| **Grounding and bonding** | ANSI/TIA-607, EN 50310, ISO/IEC 30129 |
| **Cooling and environment** | ASHRAE TC 9.9 thermal guidelines |
| **Fire detection and suppression** | NFPA 72, NFPA 75, NFPA 2001, EN 54, ISO 14520, EN 15004 |
| **Physical security** | EN 50131 (alarm systems), EN 50132 (CCTV), EN 50133 (access control) |
| **Lightning protection** | IEC 62305 |
| **Lighting and emergency lighting** | EN 12464-1, EN 1838 |
| **Raised floors** | EN 12825, CISCA |
| **Efficiency metrics** | ISO/IEC 30134 (PUE and others), ISO 50001 |
| **Information security** | ISO/IEC 27001 |
| **Business continuity** | ISO 22301 |
| **IT service management** | ISO/IEC 20000 |

You don't need to memorise every number. Learn **which topic maps to which standard family**, and know the headline ones: TIA-942, EN 50600, Uptime Tiers, BICSI, ASHRAE, NFPA and ISO 27001.

---

# Lesson 2.2: Additional Standards

These are the standards and frameworks that sit **around** the core data centre standards: efficiency, security, compliance, operations and sustainability.

## 5. Additional standards by theme

### Energy, efficiency and sustainability

| Standard / programme | What it is |
| --- | --- |
| **ISO/IEC 30134 series** | The KPIs: **PUE**, REF, ERF, CUE, WUE, ITEEsv, ITEUsv. Mirrored by **EN 50600-4** |
| **The Green Grid** | Industry body that introduced **PUE** and related metrics |
| **EU Code of Conduct for Data Centre Energy Efficiency** | Voluntary best-practice programme in Europe |
| **ISO 50001** | Energy management system |
| **ISO 14001** | Environmental management system |
| **ASHRAE 90.4** | Energy standard for data centres **[CHECK]** |
| **LEED / BREEAM** | Green building certification schemes |

### Thermal and environmental

| Standard | What it is |
| --- | --- |
| **ASHRAE TC 9.9 Thermal Guidelines** | Recommended and allowable temperature and humidity ranges for IT equipment, by equipment class |
| **ETSI EN 300 019** | Environmental conditions for telecom equipment |

### Information security and compliance

| Standard | What it is |
| --- | --- |
| **ISO/IEC 27001** | Information security management system (ISMS). Focuses on organisation and process, and **complements** the physical standards |
| **SOC 2 / SSAE 18 / ISAE 3402** | Audit reports on a service provider's controls |
| **PCI DSS** | Payment card data security |
| **HIPAA** | US health information rules |
| **GDPR** | EU data protection law (a **regulation**, mandatory) |
| **NIS2** (EU) | EU cybersecurity directive, affecting essential and important entities **[CHECK]** |

### Quality, service and continuity

| Standard | What it is |
| --- | --- |
| **ISO 9001** | Quality management |
| **ISO 22301** | Business continuity management |
| **ISO/IEC 20000** | IT service management |
| **ITIL** | IT service management framework (a framework, not a certifiable standard) |

### Safety, fire and building

| Standard | What it is |
| --- | --- |
| **NFPA 75** | Fire protection of IT equipment |
| **NFPA 72 / EN 54** | Fire alarm and detection |
| **NFPA 2001 / ISO 14520 / EN 15004** | Clean agent (gas) suppression systems |
| **IEC 62305** | Lightning protection |
| **Local building and fire codes** | Mandatory, and take precedence |

### Cabling and infrastructure

| Standard | What it is |
| --- | --- |
| **ANSI/TIA-568** | Commercial building telecommunications cabling |
| **ISO/IEC 11801** | International generic cabling |
| **EN 50173 / EN 50174** | European cabling systems, and their installation planning and practices |
| **ANSI/TIA-606** | Labelling and administration |
| **ANSI/TIA-607 / EN 50310** | Bonding and grounding |

### Operations and management

| Standard | What it is |
| --- | --- |
| **BICSI 009** | Data centre operations and maintenance best practice |
| **Uptime Operational Sustainability** | Management, operations, building and site criteria |
| **EN 50600-3-1** | Operational information and processes |
| **ISO/IEC 22237-7** | Management and operational information **[CHECK]** |

### Open and hyperscale

| Programme | What it is |
| --- | --- |
| **Open Compute Project (OCP)** | Open hardware designs for efficient, scalable data centres |

## 6. How to choose and combine standards

A real project uses several at once, each for a different job:

| Question | Typical answer |
| --- | --- |
| What **availability** should the facility deliver? | A Tier, Rated level or Availability Class, from a business risk analysis |
| How do I **design** each system? | EN 50600 parts, TIA-942, BICSI 002 |
| How do I **cable** it? | ISO/IEC 11801, TIA-568, EN 50173/50174 |
| How do I **protect** it? | NFPA, EN 54, EN 50131 |
| How do I **measure efficiency**? | ISO/IEC 30134 (PUE and others) |
| How do I manage **information security**? | ISO/IEC 27001 |
| What is **legally required**? | Local building, electrical and fire codes, plus privacy and cyber law |

**Worked example.** A colocation provider in Germany wants to sell to banks:

1. **Law first:** German building, electrical and fire regulations, and GDPR.
2. **Facility class:** EN 50600 Availability Class 3 (concurrently maintainable) with a matching Protection Class, possibly with Uptime Tier III as well, because customers recognise it.
3. **Efficiency:** report PUE per ISO/IEC 30134 and run an ISO 50001 energy management system.
4. **Security and assurance:** ISO/IEC 27001 and a SOC 2 type report for customers' auditors.
5. **Continuity:** ISO 22301.
6. **Cabling and bonding:** EN 50173/50174 and EN 50310.

## Glossary

| Term | Meaning |
| --- | --- |
| Standard / guideline | "Shall" / "should" |
| Regulation / code | Mandatory by law |
| Certification | Independent audit against a standard |
| Tier / Rated / Availability Class | Uptime / TIA-942 / EN 50600 level terms |
| Concurrent maintainability | Maintenance without taking IT down |
| Fault tolerance | A single failure causes no IT impact |
| PUE | Total facility energy ÷ IT energy |
| ISMS | Information security management system |

## Exam takeaways

- **Standard** = "shall", **guideline** = "should", **regulation** = law. Law **overrides** voluntary standards.
- **Certification** is an independent audit, not just a claim of compliance.
- Know who writes standards: **ISO/IEC** (international), **CEN/CENELEC/ETSI** (Europe), **ANSI, BSI, DIN** (national), plus **TIA, BICSI, NFPA, ASHRAE, Uptime** (industry).
- Know the four headline documents: **Uptime Tiers, TIA-942, EN 50600 / ISO/IEC 22237, BICSI 002**, and their level terms.
- Know **Tier I to IV** and the two jumps (II to III, III to IV).
- EN 50600 has **three classifications**: availability, protection (security) and energy efficiency enablement.
- Uptime also certifies **operational sustainability**, since topology alone is not enough.
- Each subsystem has its own **standard family**.
- Standards are **combined** in a real project, and the **law comes first**.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| **Uptime Institute Tier Standard** (Topology; Operational Sustainability) | Tier I to IV definitions, redundancy, certification types |
| **ANSI/TIA-942-C** (May 2024) | Rated 1 to 4, scope and certification |
| **EN 50600** series (CENELEC) | Availability, protection and energy efficiency classes, and the part list |
| **ISO/IEC 22237** series | The international counterpart of EN 50600 |
| **ANSI/BICSI 002-2024**, **BICSI 009-2024** | Design best practice (002) and operations (009) |
| **ISO/IEC 30134** series | Efficiency KPIs such as PUE |
| IEC 60364, NFPA 70, BS 7671 | Electrical installation |
| IEC 62040 | UPS |
| ISO/IEC 11801, ANSI/TIA-568, -569, -606, EN 50173, EN 50174 | Cabling, pathways, labelling and installation |
| ANSI/TIA-607, EN 50310, ISO/IEC 30129 | Grounding and bonding |
| ASHRAE TC 9.9, ASHRAE 90.4 | Thermal guidelines and the data centre energy standard |
| NFPA 72, 75, 2001, EN 54, ISO 14520, EN 15004 | Fire detection and suppression |
| EN 50131, EN 50132, EN 50133 | Alarm, CCTV and access control systems |
| IEC 62305 | Lightning protection |
| EN 12464-1, EN 1838, EN 12825 | Lighting, emergency lighting, raised floors |
| ISO/IEC 27001, ISO 22301, ISO/IEC 20000, ISO 9001, ISO 14001, ISO 50001 | Management system standards |
| PCI DSS, HIPAA, SOC 2 / SSAE 18, GDPR, NIS2 | Compliance and legal regimes |
| EU Code of Conduct for Data Centres, LEED, BREEAM, Open Compute Project | Programmes and certification schemes |

The Tier availability percentages are the commonly quoted indicative figures, not a guarantee. Editions are those current in November 2026. Figures marked **[CHECK]** come from general industry practice rather than a named standard.
