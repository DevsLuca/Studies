<div align="center">

# ⚔️ Who Wins the Battle?
### Predicting Pokémon Showdown winners from the first 30 turns

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-2C6FBB)
![Kaggle](https://img.shields.io/badge/Kaggle-competition-20BEFF?logo=kaggle&logoColor=white)
![No neural nets](https://img.shields.io/badge/neural%20nets-not%20allowed-lightgrey)

*Fundamentals of Data Science · Kaggle competition `fds-pokemon-battles-prediction-2026`*

**First Author · Second Author · Third Author** <!-- TODO: names -->

</div>

---

Thirty turns into a Generation 2 OverUsed battle, can you tell who's going to win?

We get Player 1's full team, Player 2's lead and a turn-by-turn log of the first 30 turns: who is on the field, their HP, status and the move used. The task is to predict whether Player 1 wins, using **classical machine learning only**.

> [!TIP]
> **TL;DR:** The winner isn't decided by the team you bring but by the damage you've taken. A simple *team-health tracker*, which remembers every Pokémon's last known HP, carries most of the signal. Our final blend reaches **0.673 accuracy** (chance: 0.500), and swapping algorithms barely moves that number.

---

## 📊 Results at a glance

| | Model | Accuracy |
| :---: | --- | :---: |
| 🎲 | Chance | 0.499 |
| 📋 | Logistic regression, pre-battle info only | 0.540 |
| 📏 | One rule: *"higher team health at turn 30 wins"* | 0.631 |
| 📈 | Logistic regression, all features | 0.666 ± 0.011 |
| 🌳 | LightGBM, tuned | 0.669 ± 0.012 |
| 🏆 | **0.6 × LightGBM + 0.4 × logistic regression** | **0.673 ± 0.012** |

The first three rows use 5-fold cross-validation. The last three use fresh 3×5 folds that were never used to make any choice.

🏁 Kaggle leaderboard: public **X.XXX** · private **X.XXX** <!-- TODO -->

---

## 💡 The story in four findings

### 1. Your team composition barely matters
Base stats, types, species, the lead matchup: all of it has tiny effects (Cohen's |d| < 0.06). A model that only sees pre-battle information scores **0.540**, just 4 points above a coin flip.

### 2. Looking at the active Pokémon isn't enough
The HP difference between the two Pokémon on the field reaches only AUC 0.560 at turn 30. It ignores the five Pokémon waiting on each bench, some of them already badly hurt.

### 3. Remember everyone's HP
So we built a **team-health tracker**: for each side and turn it stores the last HP seen for every Pokémon (0 once fainted, full HP if not yet seen). That single idea jumps to **AUC 0.715**, and on its own a one-line rule built on it already scores 0.631.

<div align="center">
<img src="report/figures/ablation.png" width="600" alt="Feature-group ablation: team health contributes far more than any other group">
</div>

An ablation (adding feature groups in random orders, and removing them one at a time) shows the tracker contributes **5.5 points** on average and is the only group the model can't do without. The other 13 groups mostly repeat what it already knows.

### 4. The algorithm isn't the bottleneck, the data is
Logistic regression, random forest, LightGBM, XGBoost and CatBoost all land between **0.660 and 0.672**. Tuning helps by fractions of a point. Meanwhile accuracy keeps climbing with every extra turn observed and every extra training battle:

<div align="center">
<img src="report/figures/curves.png" width="600" alt="Accuracy rises with observed turns and with training set size">
</div>

---

## 🔬 How we did it

<details>
<summary><b>Click to expand the full pipeline</b></summary>

<br>

1. **Data audit.** Removed 14 duplicate training battles (9,986 remain) and checked integrity: always 30 turns, always 6 Pokémon, balanced classes, no train/test shift. The declared lead doesn't actually start in about 30% of battles, so we added flags for it.
2. **Exploratory analysis.** Every analysis follows *question → hypothesis → evidence → conclusion → decision*, so each feature is tied to a specific finding.
3. **Feature engineering.** 388 features in 14 groups: team and lead stats, species, active HP, the tracker, faints, switches, status conditions, volatile effects, stat boosts, move types and counts of the 40 most used moves, plus P1 − P2 differences.
4. **Feature-group ablation.** We kept every group: boosted trees aren't hurt by weak features, and pruning on the same folds would make our score look better than it really is.
5. **Modelling.** Baselines, then random forest, LightGBM, XGBoost and CatBoost, with random hyperparameter search.
6. **Honest validation.** Exploration and tuning used one 5-fold split; every decision was re-tested on fresh 3×5 folds with different seeds.
7. **Blending.** The 0.6 / 0.4 weight was picked on one set of folds and confirmed on another, where it beat LightGBM alone in both evaluations.
8. **Interpretation.** ROC, calibration, error analysis and SHAP. The model is **89%** accurate on its most confident eighth of battles and **61%** on close ones.

</details>

> [!WARNING]
> **Known limitations**
> - The tracker is an estimate: healing on the bench is invisible, and unseen Pokémon are assumed to be at full HP.
> - Player 2's faints look under-recorded (0.50 vs 1.69 per battle for Player 1, despite a 50/50 win rate), so faint features for Player 2 are biased.
> - 7 test battles are identical to training battles. We did **not** copy their labels: every prediction comes from the model.

---

## 📁 What's in this repo

```
.
├── README.md
├── notebook/
│   └── pokemon-battle-prediction.ipynb   ← the full story: every step explained, all outputs saved
└── report/
    ├── main.pdf                          ← 1-page report in the course's CVPR format
    ├── main.tex, preamble.tex, sec/      ← LaTeX source
    ├── figures/                          ← report figures (PDF for LaTeX, PNG for this page)
    └── figs.py                           ← redraws the figures
```

📄 **In a hurry?** Read the [one-page report](report/main.pdf).
📓 **Want every detail?** Open the [notebook](notebook/pokemon-battle-prediction.ipynb). If GitHub won't display it, try [nbviewer](https://nbviewer.org/).

---

## 🚀 Run it yourself

**On Kaggle** (easiest)
1. Upload `notebook/pokemon-battle-prediction.ipynb` to a new Kaggle notebook.
2. **Add Input → Competitions → fds-pokemon-battles-prediction-2026**.
3. Run all. `submission.csv` appears in `/kaggle/working/`.

**Locally**
```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn lightgbm xgboost catboost
```
Download the competition files (`train.jsonl`, `test.jsonl`, `type_chart_gen2.csv`, `sample_submission.csv`) into a `data/` folder next to the notebook, then run all cells.

⏱️ A full run takes about 35–40 minutes on a Kaggle CPU, mostly the ablation and the model comparison. Everything uses a fixed seed (42), so you'll get the same numbers.

> [!NOTE]
> The competition data are **not** included here; download them from the Kaggle competition page.

**Rebuilding the report**
Upload `report/` to [Overleaf](https://www.overleaf.com/) (**New Project → Upload Project**), or compile locally:
```bash
cd report && pdflatex main && bibtex main && pdflatex main && pdflatex main
```
