# CDCP Study Notes: Electrical Physics Foundations

*As of 2026-11-17*

Power travels from the power station to the server at very high voltage and is stepped down in stages, because high voltage means low current and low current means small heat losses. Everything else in these notes (transformers, three-phase, kVA) follows from that idea.

---

## 1. The big picture: from power station to server

| Stage | Typical voltage | What happens and why |
| --- | --- | --- |
| Power generation plant | Generated, then stepped up | Coal, nuclear, hydro and others produce AC power |
| Transmission towers | 400 to 800 kV | Very high voltage means low current, so little heat is lost over long distances |
| Regional substation | 800 kV down to 33 kV | First step-down by transformer |
| Local / building substation | 33 kV down to 415 V (or 400 V) | Final step-down to a voltage that equipment and people can safely use |
| Data centre | 415 V three-phase, 240 V single-phase (400/230 V in much of Europe) | Three-phase feeds large loads, single-phase feeds small ones |

Three questions these notes answer:

1. Why such high voltage over long distances? (Sections 2 and 3: Watt's law and I² × R losses)
2. How is the voltage changed? (Section 4: transformers, which need AC)
3. Why three-phase, and what do kVA, phase voltage and line voltage mean? (Sections 5 to 8)

The slide's figures (415/240 V) differ slightly from the European nominal values (400/230 V). Use whichever your course materials give.

---

## 2. Core quantities and Watt's law

For a fixed amount of power, voltage and current trade off: more of one means less of the other.

| Quantity | Symbol | Unit | Meaning |
| --- | --- | --- | --- |
| Voltage | V | volt (V) | The electrical "pressure", always a difference between two points |
| Current | I | ampere (A) | The flow of charge |
| Resistance | R | ohm (Ω) | How strongly a wire opposes the current |
| Power | P | watt (W) | The useful work delivered per second |

Watt's law (simplest form):

```
P = V × I
```

To deliver 1 MW you can send 1,000 V at 1,000 A, or 100,000 V at 10 A. The power is identical, but the second option needs 100 times less current.

Voltage is always measured between two points, like the height difference between the top and bottom of a waterfall. A reading of "230 V" only makes sense if you know which two points it was measured between.

For three-phase power the formula gains a factor (see section 8):

```
P = √3 × V_line × I × PF
```

---

## 3. Heat losses and why transmission uses high voltage

Every wire has resistance, and current flowing through it turns some power into heat:

```
P_loss = I² × R
```

The loss depends on the square of the current, so halving the current cuts the loss to a quarter. Worked example: deliver 1 MW through a line with 1 Ω resistance.

| Transmission voltage | Current | Loss in the line (I² × R) |
| --- | --- | --- |
| 1 kV | 1,000 A | 1,000,000 W (all of it wasted) |
| 10 kV | 100 A | 10,000 W (1%) |
| 100 kV | 10 A | 100 W (0.01%) |

Raising the voltage 100 times cuts the loss 10,000 times (100 squared). High voltage also allows thinner, cheaper cables.

Why step the voltage down again? High voltage needs huge insulation and clearances, is dangerous near people, and servers cannot run on it. So the voltage is reduced in stages, as shown in section 1.

In a data centre, the same logic means the heavy, high-current cabling (over 1,000 A at 415 V for a 1 MW site) is only needed for the short run inside the building. The long trip from the power station is done at low current.

---

## 4. Transformers

A transformer changes voltage by trading it for current, using two coils of wire wrapped around one iron core. The coils are not electrically connected. Energy passes between them only through the magnetic field in the iron.

- **Primary coil:** the input side, connected to the source (the 33 kV side in the slide).
- **Secondary coil:** the output side, connected to the load (the 415 V side).

Which coil is "primary" depends only on which way the power flows.

**How it works (Faraday's law).** A changing magnetic field through a coil induces a voltage in it.

1. AC in the primary coil creates a changing magnetic field.
2. The iron core guides that field to the secondary coil, because iron concentrates a magnetic field far better than air.
3. The changing field induces a voltage in the secondary coil.
4. Each turn of wire gets roughly the same small voltage, so more turns means more voltage.

**The turns ratio:**

```
V₂ / V₁ = N₂ / N₁
```

To step 33 kV down to 415 V (a ratio of about 80 : 1), the secondary has about 80 times fewer turns than the primary. The manufacturer chooses the turns to give the required output voltage. A gearbox is a good analogy: it trades speed for torque, a transformer trades voltage for current, and the turns ratio is the gear ratio.

Worked example: a 33 kV to 415 V step-down has a ratio of 33,000 / 415 ≈ 80 : 1. If the primary has 8,000 turns, the secondary has about 100 turns.

```
 33 kV in                                    415 V out
 (from utility)                          (to the data centre)

  ┌───────┐         iron core          ┌───────┐
  │ 8,000 │◄═══ magnetic field ═══════►│  100  │
  │ turns │                            │ turns │
  └───────┘                            └───────┘
   PRIMARY                              SECONDARY
```

**Power is almost conserved**, so when voltage goes down, current goes up by the same factor:

```
V₁ × I₁ ≈ V₂ × I₂
```

**Why AC?** Voltage is only induced while the field is changing. AC changes constantly, DC gives a steady field and induces nothing (apart from a brief pulse at switch-on). That is the main reason the grid uses AC. Modern HVDC lines exist for very long distances, but they need expensive converter stations at each end.

**Losses.** Real transformers are 98 to 99% efficient. The rest becomes heat:

- Copper losses: I² × R heating in the windings, rising with load.
- Core losses: eddy currents and hysteresis in the iron, present even with no load.

For a data centre this heat must be removed by the cooling system and counts toward PUE, which is why low-loss transformers matter for sustainability.

**Why we need it and how we use it.** Two facts drive the design: high voltage means low current, which keeps transmission losses small (section 3), and servers and equipment need low voltage. The transformer connects the two needs. The utility transmits at high voltage, and the data centre uses low voltage. A data centre almost always has one or more transformers at its edge, stepping the incoming medium voltage (for example 10 to 33 kV) down to 415 V or 400 V.

---

## 5. Three-phase power

Three-phase power uses three AC waves, each offset by 120° (one third of a cycle). It gives constant power and about twice as much power per wire as single-phase, which is why data centres use it for everything large.

**The problem with one wave.** Single-phase power hits zero twice every cycle, so a motor or compressor gets a pulsing push. It also needs a lot of copper for the power it delivers.

**Why three and not two.** Two waves 90° apart can also give smooth power (two-phase systems existed in the early 1900s). The real difference is cancellation:

- Three waves 120° apart always add up to zero, at every instant. With balanced loads, the return current in the neutral is zero, so each phase acts as the return path for the other two.
- Two waves 90° apart do not cancel, so they need a fourth wire or an overloaded shared return.

**Seeing the cancellation in numbers.** Take each wave's peak as 1 and look at one instant (θ = 0):

| System | Values at that instant | Sum |
| --- | --- | --- |
| Three-phase (120° apart) | L1 = 0, L2 = −0.866, L3 = +0.866 | 0 |
| Two-phase (90° apart) | A = 0, B = −1 | −1, and it keeps changing |

The three-phase sum is 0 at every instant, not just this one. At 50 Hz one cycle lasts 20 ms, so each phase peaks about 6.7 ms after the previous one. When one phase dips, the others make up for it, so total power stays constant and a three-phase motor gets steady torque.

| System | Wires | Total power | Power per wire |
| --- | --- | --- | --- |
| Single-phase | 2 | 1 × V × I | 0.5 × V × I |
| Two-phase (separate returns) | 4 | 2 × V × I | 0.5 × V × I |
| Three-phase | 3 (neutral not needed for balanced loads) | 3 × V × I | 1 × V × I |

Real example: a 32 A single-phase 230 V feed gives about 7.4 kW, while a 32 A three-phase 400 V feed gives about 22 kW from a similar cable.

**Other reasons three won.**

- Three coils 120° apart make a smooth rotating magnetic field, which is how induction motors (chiller compressors, fans, pumps) run without special hardware.
- Three-coil generators and star/delta transformer connections are simple to build.
- One system supplies two voltages (phase and line, section 6).
- Why not more than three? Six or twelve phases are used for large rectifiers, but three already gives constant power and perfect cancellation.

**Balance the phases.** Cancellation only works if the three phases carry similar loads. In a data centre, spread rack loads evenly across L1, L2 and L3. An unbalanced load causes neutral current, overheating, voltage imbalance and trips. Computer power supplies also create harmonic currents that add up in the neutral instead of cancelling, so data centres often use oversized neutrals.

---

## 6. Phase voltage, line voltage and the square root of 3

Phase voltage is measured from one phase wire to neutral. Line voltage is measured between two phase wires, and it is √3 (about 1.73) times larger.

**The wires.** A three-phase supply has four wires: L1, L2 and L3 (the three phases) and N (neutral, a common reference at about 0 V). A separate earth wire is for safety (see Module 6, Part 2).

In a star connection, the transformer's three secondary coils are joined at one common point. That point is the neutral, and the three free ends are L1, L2 and L3.

```
        coil 1 ──────── L1
       /
  ● ──── coil 2 ──────── L2      ● = star point
       \
        coil 3 ──────── L3

  The star point ● also goes out as the Neutral (N) wire
```

| Probes placed on | Name | Reading (400 V system) | Reading (415 V system) |
| --- | --- | --- | --- |
| L1 and N (or L2–N, L3–N) | Phase voltage | 230 V | 240 V |
| L1 and L2 (or L2–L3, L1–L3) | Line voltage | 400 V | 415 V |

Line voltage is larger because it spans two coils in series whose waves are out of step. Their voltages do not simply add (that would be 460 V), and they do not fully cancel, so you get √3 × 230 V ≈ 400 V.

**Where the square root comes from.** Line voltage is the difference of two phase voltages that are 120° apart:

```
V(L1-L2) = V(L1) − V(L2)
```

Two equal arrows of length V_phase at 120° form a triangle. Splitting it down the middle gives two right-angled triangles with a 60° angle, so:

```
V_line = 2 × V_phase × sin 60° = √3 × V_phase
```

Because sin 60° = √3 / 2. Equivalent forms:

```
V_phase = V_line / √3
230 × 1.732 ≈ 398 ≈ 400 V
240 × 1.732 ≈ 415 V
```

**Numerical check.** A 230 V RMS phase has a peak of 230 × 1.414 ≈ 325 V. At θ = 60°, L1 = 325 × sin(60°) = +281.5 V and L2 = 325 × sin(−60°) = −281.5 V. The difference is 281.5 − (−281.5) = 563 V, which is the peak of the line voltage. The formula agrees: √3 × 325 = 563 V. Converting back to RMS gives 563 / 1.414 ≈ 398 V, the familiar 400 V.

Why the angle matters: the difference of two equal waves depends on the angle between them.

| Angle between the two waves | Difference |
| --- | --- |
| 0° (in step) | 0 (they cancel) |
| 120° (three-phase) | 1.73 × V_phase |
| 180° (exactly opposite) | 2 × V_phase |

**In a data centre.** Single-phase rack PDUs connect between one phase and neutral (230 V). Chillers, UPS inputs and three-phase rack PDUs connect across all three phases (400 V). One supply provides both.

---

## 7. Apparent power (S), real power (P), reactive power (Q) and power factor

S is not the same as P. S is the total the cable and equipment must carry, P is the useful part, and the two are equal only when the power factor is 1.

| Quantity | Symbol | Unit | Meaning |
| --- | --- | --- | --- |
| Real (active) power | P | watt (W) | Does useful work (runs servers, spins fans) |
| Reactive power | Q | VAR | Flows back and forth, does no work, but still loads the wires |
| Apparent power | S | volt-ampere (VA) | Voltage × current, the total loading on the equipment |
| Power factor | PF | none (0 to 1) | The ratio P / S |

The relationships:

```
S = V × I
P = S × PF
S² = P² + Q²
```

Always S ≥ P. The three form a right-angled triangle with S as the longest side.

```
          /|
     S  /  |
      /    |  Q
    /      |
   /_______|
       P
```

S (VA) is the hypotenuse, P (W) is the useful part, and Q (VAR) is the part that does no work. The power factor is P / S, which equals the cosine of the angle between S and P.

Example: a rack draws 10 A at 230 V. S = 2,300 VA. With PF = 1, P = 2,300 W. With PF = 0.9, P = 2,070 W. In both cases the same 10 A flows and heats the cable.

Why PF is below 1: voltage and current are both waves. If they rise and fall exactly together (in phase), all the power is useful. Loads such as motors, and some older power supplies, draw current slightly out of step, which creates reactive power. Modern IT power supplies have a PF of about 0.95 to 1. Cooling-plant motors can be lower.

Analogy: P is the beer, Q is the foam, and S is the whole glass. The glass (cable, transformer) must be sized for both.

**Why transformers and UPS units are rated in kVA.** Heating in the windings depends on current, and current depends on S regardless of power factor. So the manufacturer states the rating in VA.

**Example:** a 100 kVA UPS with PF 0.9 can supply 90 kW of real load. Connecting 100 kW overloads it, even though 100 kW looks smaller than "100 kVA" on paper.

---

## 8. Current formulas and worked data centre examples

For three-phase equipment, current per phase is the apparent power divided by √3 times the line voltage.

**Derivation.** A three-phase system is three single-phase circuits working together.

1. Each phase carries S = V_phase × I, so the three together carry S = 3 × V_phase × I.
2. The quoted voltage is the line voltage, and V_phase = V_line / √3.
3. Substituting: S = 3 × (V_line / √3) × I, and since 3 / √3 = √3:

```
S = √3 × V_line × I     =>     I = S / (√3 × V_line)
```

With real power and power factor included:

```
P = √3 × V_line × I × PF     =>     I = P / (√3 × V_line × PF)
```

Single-phase for comparison: I = S / V.

**Worked examples (√3 ≈ 1.732)**

| Situation | Calculation | Result |
| --- | --- | --- |
| 1 MVA transformer, secondary at 415 V | 1,000,000 / (1.732 × 415) | about 1,391 A |
| Same transformer, primary at 33 kV | 1,000,000 / (1.732 × 33,000) | about 17.5 A |
| Chiller, 100 kW at 415 V, PF 0.9 | 100,000 / (1.732 × 415 × 0.9) | about 155 A per phase |
| 10 kVA three-phase load at 400 V | 10,000 / (1.732 × 400) | about 14.4 A per phase |
| 32 A rack feed, single-phase 230 V | 230 × 32 | about 7.4 kW |
| 32 A rack feed, three-phase 400 V, PF 1 | 1.732 × 400 × 32 | about 22 kW |

Cross-check on the 10 kVA load: 10 kVA split over 3 phases is 3.33 kVA per phase, each phase has 400 / 1.732 = 231 V across it, and 3,333 / 231 = 14.4 A.

**Why the 1 MVA example matters.** Power is the same on both sides of the transformer, but the voltage drops 80 times and the current rises about 80 times. For a 1 MW data centre, the utility cable at 33 kV carries only about 17.5 A (thin, cheap, tiny losses). Inside the building the same power at 415 V needs about 1,390 A, which means thick cables or busbars, large breakers and short runs. A transformer room is therefore placed close to the main switchboard.

**Option A: no transformer.** Imagine the utility delivered 415 V directly to a 1 MW site. The current would be 1,000,000 / (1.732 × 415) ≈ 1,390 A over the whole route from the utility substation to your building. One large cable carries roughly 500 to 600 A, so you would need three or four heavy cables per phase all the way, with large losses and enormous cost.

**Option B: a transformer at the building.**

| Where | Voltage | Current for 1 MW | What it means |
| --- | --- | --- | --- |
| Utility cable to your site | 33 kV | about 17.5 A | Thin, cheap cable, tiny losses |
| Inside your building, after the transformer | 415 V | about 1,390 A | Thick cables or busbars, but only over short distances |

You pay for the heavy 1,390 A cabling only for the short run inside the building. Design consequences:

- Put the transformer room close to the main switchboard to keep the high-current runs short.
- Rate the LV switchboard, busbars and breakers for over 1,000 A, which makes them large and expensive.
- Transformer losses of about 1 to 2% (10 to 20 kW at 1 MW) add to the cooling load and affect PUE.
- A transformer failure removes the whole site's utility supply, so the site then depends on the generator and UPS (redundancy, Module 6 Part 2).

---

## 9. Harmonics and generator sizing

Harmonics are unwanted extra waves riding on the normal AC wave, which distort its shape. They matter in data centres because servers, UPS units and cooling drives are all non-linear loads, and because generators are far more sensitive to harmonics than the utility grid is.

**The ideal wave and what a harmonic is.** Mains power should be a clean sine wave at the fundamental frequency (50 Hz in Europe, 60 Hz in the US). A harmonic is another sine wave at a whole-number multiple of that frequency:

| Harmonic | Frequency (50 Hz system) |
| --- | --- |
| 1st (fundamental) | 50 Hz |
| 3rd | 150 Hz |
| 5th | 250 Hz |
| 7th | 350 Hz |

Add a little 150 Hz and 250 Hz to the 50 Hz wave and the result is a lumpy, distorted wave instead of a clean sine. Think of a musical note: the pure note is the fundamental, and the overtones that change its sound are the harmonics.

**Where harmonics come from.** Non-linear loads draw current in short pulses rather than smoothly in step with the voltage:

- Server power supplies (switch-mode power supplies)
- UPS rectifiers, which convert AC to DC to charge the batteries
- Variable-speed drives on cooling fans and pumps
- LED lighting drivers

The distortion is measured as THD (total harmonic distortion), a percentage. Lower is better.

**Why they cause problems.**

- Extra heat in cables, transformers and generator windings.
- Neutral overload: third-harmonic currents from the three phases add up in the neutral instead of cancelling, which is why neutrals are often oversized.
- Distorted voltage, which can upset sensitive equipment.
- Nuisance trips, vibration and a worse power factor.

**Generator sets (EPI slide).** Generators act as the backup supply for the utility grid. Diesel is the most common choice, and alternatives are now considered because of sustainability requirements. The size of the generator set depends on:

- The kVA/kW requirement of the attached installation
- Harmonics returning from the connected installation
- Expected inrush currents on the generator during operation

**Why harmonics matter for generators.** A generator is a weaker source than the grid. It has a much higher internal impedance, so harmonic currents distort its output voltage far more and overheat its alternator windings. The UPS rectifier is the main culprit, because it is a large non-linear load sitting directly on the generator. That is why the slide's sizing table has a multiplier on the UPS load:

| Item | Multiplier |
| --- | --- |
| UPS load | × 1.0 or × 1.2, depending on harmonic levels |
| Cooling and lighting load | × 1.0 |
| Total gen-set capacity | Sum of the above, in kW |

The × 1.2 applies to a UPS with high harmonic distortion (for example a basic rectifier). The × 1.0 applies to a modern low-harmonic UPS (active front end or filters). Check your course materials for the exact threshold. The extra 20% is spare generator capacity that stops the harmonics from overloading it.

**Worked example.** UPS load 400 kW, cooling and lighting load 300 kW.

| Case | Calculation | Total gen-set capacity |
| --- | --- | --- |
| High-harmonic UPS | 400 × 1.2 + 300 × 1.0 | 780 kW |
| Low-harmonic UPS | 400 × 1.0 + 300 × 1.0 | 700 kW |

Better UPS technology can therefore mean a smaller, cheaper generator.

**Inrush current** is the brief surge when large motors (cooling fans, pumps) start. It can be several times their running current, and the generator must ride through it without its voltage collapsing.

---

## 10. Exam cheat sheet

Formulas to know:

| Topic | Formula | Notes |
| --- | --- | --- |
| Power | P = V × I | Single-phase, PF = 1 |
| Cable loss | P_loss = I² × R | Halve the current, loss drops to a quarter |
| Transformer ratio | V₂ / V₁ = N₂ / N₁ | More turns means more voltage |
| Transformer power | V₁ × I₁ ≈ V₂ × I₂ | Voltage down means current up |
| Line voltage | V_line = √3 × V_phase | 230 V gives about 400 V, 240 V gives about 415 V |
| Real power | P = S × PF | S ≥ P always |
| Power triangle | S² = P² + Q² | S in VA, P in W, Q in VAR |
| Three-phase apparent power | S = √3 × V_line × I | Gives I = S / (√3 × V_line) |
| Three-phase real power | P = √3 × V_line × I × PF | |
| PUE | Total facility energy / IT energy | Ideal 1.0 (from Module 6, Part 1) |

Key distinctions:

- Primary is the input coil, secondary is the output coil. They are linked only by a magnetic field.
- Phase voltage is one phase to neutral. Line voltage is between two phases.
- S (VA) is the total loading, P (W) is the useful part.
- Transformers and UPS units are rated in kVA, because heating depends on current.
- A transformer needs AC, because it only works with a changing magnetic field.
- Three-phase balanced loads need no neutral current. Unbalanced loads and harmonics do.

Harmonics and generator sizing:

- Harmonics are whole-number multiples of the fundamental frequency (3rd harmonic = 150 Hz on a 50 Hz system), caused by non-linear loads such as UPS rectifiers and server power supplies.
- Generator capacity = UPS load × 1.0 or 1.2 (by harmonic level) + cooling and lighting load × 1.0, with inrush current checked separately.
- Third harmonics add up in the neutral instead of cancelling.

Common mistakes:

- Treating kVA and kW as the same. A 100 kVA UPS at PF 0.9 gives 90 kW.
- Forgetting that lower voltage means higher current, and so thicker cabling.
- Using √3 for phase voltage when the quoted voltage is already the line voltage, or the reverse.
- Mixing the 400/230 V (Europe) and 415/240 V (your slide) nominal values. Use whichever your course materials give.
- Believing a transformer creates power. It only trades voltage for current.

---

## 11. Practice questions with answers

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
