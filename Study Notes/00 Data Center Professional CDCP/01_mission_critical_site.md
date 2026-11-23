# Module 1: The Mission Critical Site

Detailed notes, following the lesson-level index of the EPI course.

| Lesson | Title | Section in these notes |
| --- | --- | --- |
| 1.1 | Data Centres: The Foundation of Every Organization | [Section 1](#11-data-centres-the-foundation-of-every-organisation) |
| 1.2 | Types of Data Centres | [Section 2](#12-types-of-data-centres) |
| 1.3 | Consequences and Cost of Unavailability | [Section 3](#13-consequences-and-cost-of-unavailability) |
| 1.4 | Complexity and Risk Factors for Data Centres | [Section 4](#14-complexity-and-risk-factors-for-data-centres) |
| 1.5 | Main Causes for Data Centre Unavailability | [Section 5](#15-main-causes-for-data-centre-unavailability) |
| | Knowledge Test | [Practice questions](00_knowledge_tests.md#module-1-the-mission-critical-site) |

**Objectives (from your slide).** After this module you should be able to describe and understand: the various layers in the business, types of data centres, why the mission critical site is important, the various elements of a mission critical site, and the various causes for unavailability.

> **Conventions.** **[CHECK]** marks a figure or statement from general industry practice or outside research, not from your slides. If your course says something different, use your course. Statistics are dated, so confirm the year your course uses.

---

## 1.1 Data centres: the foundation of every organisation

### What a data centre is

A **data centre** is a facility that houses an organisation's IT systems (servers, storage, network equipment) together with the **infrastructure that keeps them running**: power, cooling, fire protection, physical security and monitoring.

It exists to **process, store, move and protect** an organisation's data and applications, and to keep them available around the clock.

### Why it is the foundation

Almost every organisation now runs on IT: banks, hospitals, airlines, retailers, governments, broadcasters, factories. When the data centre stops, the business processes that depend on it stop too.

### The layers in the business

A business is a stack, and each layer depends on the one below it:

| Layer | Examples |
| --- | --- |
| **Business processes** | Online sales, payroll, banking transactions, patient records |
| **Applications / information systems** | ERP, email, databases, web shops |
| **IT infrastructure** | Servers, storage, network equipment |
| **Site (facility) infrastructure** | Power, cooling, fire protection, security, the building |

**Key idea:** if the bottom layer fails, everything above it fails. A cooling failure can stop a business process worth millions per hour. This is why the facility is treated as **mission critical**, not as "a room with computers". Your slides may name the layers slightly differently, but the dependency chain is the point.

### Mission critical

A **mission critical** facility or system is one whose failure causes **serious consequences** for the organisation's ability to operate. The term describes the *importance* of the function, and it drives the level of redundancy, protection and operational discipline the site needs.

### Two useful terms: white space and grey space

| Term | Meaning |
| --- | --- |
| **White space** | The area that holds the IT equipment (the computer room, racks, rows) |
| **Grey space** | The support areas: power rooms, UPS and battery rooms, generators, cooling plant, storage, offices |

You will meet both terms again in the building and power modules.

### The site infrastructure vs. the IT infrastructure

| | IT infrastructure | Site infrastructure |
| --- | --- | --- |
| What | Servers, storage, network | Power, cooling, fire, security, building |
| Typical lifespan | A few years | 15 to 25 years or more **[CHECK]** |
| Who usually manages it | IT department | Facilities / data centre operations |

This lifespan difference matters: the site must be designed to support several generations of IT equipment, which is why **scalability and modularity** are key design principles.

---

## 1.2 Types of data centres

### By ownership and operating model

| Type | Who owns the building and equipment | Notes |
| --- | --- | --- |
| **Enterprise (corporate / on-premises)** | One organisation, for its own use | Full control, full responsibility, highest capital cost |
| **Colocation** | The provider owns the building, power and cooling. You rent space and bring **your own equipment** | Shared facility. Variants: *retail* (a rack or cage) and *wholesale* (large halls) |
| **Managed hosting** | The provider owns the hardware and runs it for you | You rent a service, not space |
| **Cloud** | Provider-run infrastructure delivering virtualised services on demand | Pay-as-you-use, scalable |
| **Hyperscale** | Very large facilities operated by the major cloud providers | Huge scale and standardisation |
| **Edge** | Small sites close to users or devices | Low latency |
| **Modular / containerised** | Prefabricated units deployed quickly | Fast roll-out and phased growth |

**Colocation vs. managed hosting** is a classic exam contrast: in colocation **you supply the equipment**, in managed hosting **the provider does**.

### By size (indicative)

| Size | Description |
| --- | --- |
| **Server room / closet** | A few racks inside an office building, often with limited redundancy |
| **Small to medium data centre** | A dedicated room or building, tens to hundreds of racks |
| **Large / enterprise** | Hundreds to thousands of racks, full redundancy |
| **Hyperscale** | Tens of thousands of servers or more |

### Choosing a model

| Factor | Own (enterprise) | Colocation | Cloud |
| --- | --- | --- | --- |
| Control | Highest | High (over your own equipment) | Lowest |
| Up-front cost | Highest | Medium | Lowest |
| Time to deploy | Slowest | Medium | Fastest |
| Scalability | Limited by what you build | Good | Excellent |
| Facility responsibility | You | The provider | The provider |

Many organisations use a **hybrid** of these.

---

## 1.3 Consequences and cost of unavailability

### Types of consequence

| Category | Examples |
| --- | --- |
| **Direct financial** | Lost sales and revenue, lost transactions, lost productivity (staff who cannot work), recovery and repair costs |
| **Contractual** | **SLA** (service level agreement) penalties and service credits to customers |
| **Legal and regulatory** | Fines for breaching data protection or sector rules, mandatory reporting |
| **Reputation** | Loss of customer trust, customers moving to competitors, negative press |
| **Data loss** | Lost or corrupted data, which may be unrecoverable |
| **Safety** | In healthcare, transport, emergency services and utilities, an outage can endanger lives |

Direct costs are the easiest to count. Reputation and customer loss often cost more in the long run.

### Estimating the cost of downtime

A simple model:

```
Cost per hour = lost revenue per hour
              + lost productivity per hour
              + recovery costs
              + penalties and fines
```

**Worked example (illustrative figures).** An online retailer:

| Item | Calculation | Per hour |
| --- | --- | --- |
| Lost revenue | €30,000 of sales each hour | €30,000 |
| Lost productivity | 100 staff × €40/h × 50% unable to work | €2,000 |
| Recovery | Extra engineers and repairs | €3,000 |
| SLA penalties | Credits to business customers | €5,000 |
| **Total** | | **€40,000 per hour** |

### What each "nine" is worth

Using €40,000 per hour of downtime:

| Availability | Downtime per year | Annual downtime cost |
| --- | --- | --- |
| 99% | 87.6 hours | €3,504,000 |
| 99.9% | 8.76 hours | €350,400 |
| 99.99% | 52.6 minutes (0.877 h) | €35,080 |
| 99.999% | 5.26 minutes (0.0877 h) | €3,508 |

Going from 99% to 99.9% saves about €3.15 million a year in this example. Each further nine saves less in absolute terms, but costs more to build. The sensible target is where **the cost of the extra availability equals the cost of the downtime it prevents**.

| As availability rises... | Cost of redundancy | Cost of downtime | Total cost |
| --- | --- | --- | --- |
| Low | Low | **High** | High |
| Medium | Medium | Medium | **Lowest (the sweet spot)** |
| Very high | **High** | Low | High |

The aim is the point where **extra spending on resilience stops paying for itself**. Mission critical sites (banks, hospitals) sit at the higher-availability end because their downtime cost is far higher.

### Related terms

| Term | Meaning |
| --- | --- |
| **SLA** | Service level agreement: the availability and response the provider promises, with penalties if missed |
| **RTO** | Recovery time objective: the longest acceptable time to restore service after an outage |
| **RPO** | Recovery point objective: the longest acceptable period of **data loss**, measured in time |

**Example:** an RPO of 15 minutes means backups or replication must run at least every 15 minutes. An RTO of 4 hours means service must be back within 4 hours.

### Current statistics **[CHECK]**

From the Uptime Institute's 2026 annual outage analysis (based on its 2025 survey):

- **57%** of respondents said their most recent major outage cost more than **$100,000**.
- **One in five** said it cost more than **$1 million**, for the second year running.
- About **one in ten** said their last outage had serious or severe impacts.
- Outage frequency per site has been **declining for five years**, but the pace of improvement has slowed, and each outage tends to be costlier.

---

## 1.4 Complexity and risk factors for data centres

### Why a data centre is complex

- **Many interdependent systems:** power, cooling, network, fire protection, security, building management. A failure in one often affects the others (for example a power loss stops the cooling, which causes overheating).
- **Many suppliers and technologies**, which must work together.
- **24/7 operation:** work is done on live systems, with no quiet period.
- **Constant change:** new equipment, growing power density, software and firmware updates.
- **Long lifetime:** equipment of different ages and generations in one building.
- **Redundancy itself adds complexity:** more components, more switching states, more ways to make a mistake. This is why the dual-path slide in Module 6 is labelled "not preferred".

### Risk

```
Risk = likelihood of an event × impact if it happens
```

**Risk management steps:**

1. **Identify** the risks (what could go wrong).
2. **Analyse** them (how likely, how bad).
3. **Evaluate** them against what the organisation will accept.
4. **Treat** them.

**Ways to treat a risk:**

| Treatment | Meaning | Example |
| --- | --- | --- |
| **Avoid** | Remove the cause | Choose a site outside a flood plain |
| **Reduce** | Lower the likelihood or impact | Add redundancy, improve procedures |
| **Transfer** | Pass it to another party | Insurance, contracts, cloud failover |
| **Accept** | Live with it, knowingly | A low-impact, low-likelihood risk |

A **risk matrix** plots likelihood against impact, so the high-likelihood, high-impact risks get attention first.

### Risk factor categories

| Category | Examples | Typical mitigation |
| --- | --- | --- |
| **Location and environment** | Flood, earthquake, storms, neighbours | Site selection (Module 3) |
| **Building and construction** | Weak structure, leaks, poor layout | Construction requirements (Module 3 and 4) |
| **Power** | Grid failure, UPS or generator failure, overload | Redundancy, testing (Module 6) |
| **Cooling** | Chiller or pump failure, blocked airflow, leaks | Redundant cooling, monitoring (Modules 9 and 10) |
| **Fire** | Electrical fire, battery fire | Detection and suppression (Module 12) |
| **Security** | Intrusion, sabotage, theft | Layered security (Module 13) |
| **Network** | Fibre cut, carrier outage | Diverse routes and carriers (Module 11) |
| **Human factors** | Error, poor procedures, fatigue, inadequate training | Procedures, training, change control |
| **Ageing and maintenance** | Worn equipment, missed maintenance | Maintenance and replacement programmes |
| **External dependencies** | Utility, telecom carriers, suppliers, cloud providers | Multiple suppliers, contracts, monitoring |
| **Capacity and density** | Power and cooling limits reached by growth | Capacity management, modular design |

### Single points of failure and common-mode failures

| Term | Meaning |
| --- | --- |
| **Single point of failure (SPOF)** | One component whose failure stops the whole system |
| **Common-mode failure** | One cause that takes out several "redundant" components at once (a shared bus, a shared fuel supply, a flood affecting both A and B rooms) |
| **Cascading failure** | One failure that triggers further failures (a UPS fails, then the overloaded survivor fails) |

A good design hunts for **SPOFs and common-mode failures**, since redundancy only helps if the backups are genuinely independent.

### Current observations **[CHECK]**

The Uptime Institute's 2026 analysis comments that:

- Operators face growing **system complexity**, **grid instability** and **co-dependencies**.
- Failures are increasingly linked to **interactions between systems** (software, networks, external dependencies) rather than a single failed component.
- **Resiliency assessments** still tend to focus on internal systems more than external and systemic risks.
- **Human error** is a contributing factor in roughly nine out of ten outages, and **failure to follow procedures** is the leading human-error driver.

---

## 1.5 Main causes for data centre unavailability

### Planned vs. unplanned

| | Planned | Unplanned |
| --- | --- | --- |
| Examples | Scheduled maintenance, upgrades, migrations | Failures, accidents, disasters |
| Control | Scheduled, can be prepared and communicated | Sudden, no warning |
| Design response | **Concurrent maintainability** lets maintenance happen without downtime | Redundancy, monitoring, procedures |

### Unplanned causes

| Cause | Typical failures | Design response |
| --- | --- | --- |
| **Power problems** | Utility outage, UPS battery failure, generator fails to start, ATS or STS failure, breaker trip, overload | Redundant paths, regular testing, maintenance (Module 6) |
| **Cooling failure** | Chiller or pump failure, loss of power to cooling, refrigerant or water leak, blocked airflow | Redundant units, monitoring, containment (Modules 9 and 10) |
| **Human error** | Wrong switch operated, wrong procedure, mislabelled equipment, unauthorised change, fatigue | Procedures, training, labelling, change control |
| **Fire and water** | Electrical or battery fire, burst pipe, roof leak, flood | Detection and suppression, leak detection, site choice (Modules 3, 12) |
| **IT hardware and software** | Server failure, software bug, firmware fault, bad configuration change | Redundant servers, testing, staged change management |
| **Network failures** | Fibre cut, carrier outage, router failure | Diverse routes and carriers (Module 11) |
| **Natural disasters** | Flood, earthquake, storm, extreme heat | Site selection, structure, DR site |
| **Sabotage / security breach** | Intentional damage, intrusion, cyber attack | Layered security (Module 13) |

### Current statistics **[CHECK]** (Uptime Institute, 2026)

- **Power remains the leading cause of impactful outages.** Failures involving **UPS systems, transfer switches and generators** are dominant.
- **Network and connectivity** problems are rising, and tend to cause longer disruptions.
- **IT and software** faults are a major source, with firmware and software faults now the largest share of IT-related outages.
- **Major fires** have increased gradually, with **lithium-ion batteries in UPS systems** a clear contributing factor.
- **Third-party providers** (cloud, telecoms, colocation) account for about **two-thirds** of publicly reported outages.

### The failure-rate "bathtub curve"

Equipment failure rates follow a pattern over its life:

| Phase | Failure rate | Cause |
| --- | --- | --- |
| **Early life (infant mortality)** | High, falling | Manufacturing defects, installation errors. Commissioning and burn-in tests catch these |
| **Useful life** | Low and roughly constant | Random failures |
| **Wear-out** | Rising | Ageing, corrosion, battery degradation. Preventive replacement is needed |

This is why **commissioning tests**, **planned maintenance** and **lifecycle replacement** matter.

### The availability formula revisited

```
Availability = MTBF / (MTBF + MTTR)
```

You can reduce the impact of the causes above by **increasing MTBF** (fewer failures, through redundancy, quality and maintenance) or by **reducing MTTR** (faster repair, through spare parts, trained staff, clear procedures and monitoring).

**Worked example.** MTBF = 10,000 h, MTTR = 4 h:

```
Availability = 10,000 / 10,004 = 0.9996 → 99.96%
```

If repairs take only 1 hour: 10,000 / 10,001 = **99.99%**.

### The elements of a mission critical site

These are the modules of your syllabus, and each guards against one or more of the causes above:

| Element | Module |
| --- | --- |
| Location, building and construction | 3 |
| Raised floor / suspended ceiling | 4 |
| Lighting | 5 |
| Power infrastructure | 6 |
| Electromagnetic fields | 7 |
| Equipment racks | 8 |
| Cooling infrastructure | 9 |
| Water supply | 10 |
| Network infrastructure | 11 |
| Fire protection | 12 |
| Physical security and safety | 13 |
| Auxiliary systems (monitoring, and so on) | 14 |

**The unifying design principle is redundancy, with no single point of failure.**

---

## Glossary

| Term | Meaning |
| --- | --- |
| Mission critical | Failure causes serious consequences for the organisation |
| White space / grey space | IT equipment area / support infrastructure area |
| Availability | Percentage of time a system is working |
| MTBF / MTTR | Mean time between failures / mean time to repair |
| SLA | Service level agreement |
| RTO / RPO | Recovery time objective / recovery point objective |
| SPOF | Single point of failure |
| Common-mode failure | One cause affecting several redundant parts |
| Concurrent maintainability | Maintenance without taking IT down |

## Exam takeaways

- The business is a **dependency stack**, and the site infrastructure is the foundation.
- Know the **data centre types**, and especially **colocation vs. managed hosting**.
- Know the **consequences** of downtime (direct, contractual, legal, reputation, data loss) and the **cost per hour** idea.
- Know the **availability table** and **Availability = MTBF / (MTBF + MTTR)**.
- **Risk = likelihood × impact**. Know the four treatments: avoid, reduce, transfer, accept.
- A **SPOF** is one failure that stops everything. A **common-mode failure** defeats redundancy.
- **Power** is the leading cause of impactful outages, and **human error** is a contributing factor in most.
- Redundancy helps, but **complexity itself is a risk**.

---

## Standards and references used

| Standard or source | Used for in these notes |
| --- | --- |
| Uptime Institute **Annual Outage Analysis 2026** (2025 survey data) | Outage cost, cause and frequency statistics (1.3 to 1.5) |
| Reliability engineering definitions | Availability = MTBF / (MTBF + MTTR), downtime per year (8,760 hours), the "nines" table, the bathtub curve |
| **ISO 22301** (business continuity) | Terminology for RTO and RPO |
| **ISO 31000** (risk management) | The four risk treatments: avoid, reduce, transfer, accept |

Figures marked **[CHECK]** come from general industry practice rather than a named standard.
