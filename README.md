# AI_Assignment


#  AI Game Play – Chess Agent with Minimax & Alpha-Beta Pruning

This project implements two classical AI algorithms — **Minimax** and **Alpha-Beta Pruning** — to play a full game of chess using the [gym-chess](https://github.com/iamlucaswolf/gym-chess) environment.

Agents evaluate the board, choose moves, and play against themselves. The game is recorded as a video and also logged into a `.csv` file for analysis. Randomness is introduced to ensure different gameplay every run.

---

## 📁 Project Structure

```
AI_GAME_PLAY/
├── alpha_beta_pruning/
│   ├── alpha_beta_agent.py
│   ├── run_alpha_beta.py
│   └── utils/
│       ├── __init__.py
│       └── recorder.py
├── minimax/
│   ├── minimax_agent.py
│   ├── run_minimax.py
│   └── utils/
│       ├── __init__.py
│       └── recorder.py
├── gameplay_alpha_beta.mp4        # Alpha-Beta video output
├── gameplay_minimax.mp4           # Minimax video output
├── results_alpha_beta.csv         # Alpha-Beta move log
├── results_minimax.csv            # Minimax move log
├── requirements.txt               # Dependencies
├── venv/                          # Python virtual environment
└── README.md
```

---

##  Algorithms Used

### 1. **Minimax**
- Explores all possible moves up to a given depth.
- Maximizes gain for the player and minimizes for the opponent.
- Randomness is added among equally good moves to diversify gameplay.

### 2. **Alpha-Beta Pruning**
- Optimized Minimax with branch pruning to skip unnecessary calculations.
- Yields the same result as Minimax but much faster.
- Random selection among equal evaluations for game variety.

---

##  Setup Instructions

###  Step 1: Create a Virtual Environment (Recommended)

To isolate this project from other Python packages:

```
python -m venv venv
```

###  Step 2: Activate the Virtual Environment

#### On Windows:
```
venv\Scripts\activate
```

#### On macOS/Linux:
```
source venv/bin/activate
```

###  Step 3: Install Dependencies

```
pip install -r requirements.txt
```

> This will install: `gym`, `gym-chess`, `python-chess`, `opencv-python`, `cairosvg`, `numpy`.

---

## 🖼 GTK for CairoSVG (REQUIRED for Recording)

**CairoSVG** requires **GTK** to convert SVG chess boards into PNG images for video.

### Install GTK (Windows):

1. Download GTK runtime:
   👉 [Download GTK Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)

2. Install it and add the `bin/` directory to your system `PATH`.

3. Restart terminal or IDE if needed.

---

## ▶ How to Run

### Run the Minimax Agent
```
python minimax/run_minimax.py
```

### Run the Alpha-Beta Agent
```
python alpha_beta_pruning/run_alpha_beta.py
```

---

##  Outputs

Each run generates:
-  `gameplay_minimax.mp4` or `gameplay_alpha_beta.mp4` — video recording of the game
-  `results_minimax.csv` or `results_alpha_beta.csv` — move-by-move logs with evaluations

---

##  Notes

- Every execution generates a **different** game due to small randomness in evaluation and tie-breaking.
- Board evaluation is based on material (piece values).
- These implementations are excellent demonstrations of classical AI search in two-player games.

---

##  Author 

- Created for educational and academic demonstration.

