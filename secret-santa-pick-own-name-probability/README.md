# Secret Santa Pick Own Name Probability

This script estimates the probability that someone picks their own name in a Secret Santa draw using both a Monte Carlo simulation and a Taylor series method.

In a Secret Santa gift exchange, each participant should draw another participant’s name at random - but no one should draw their own name. This program simulates many random draws to estimate how often someone ends up picking their own name.

---

## 🧠 What it Does

- Runs a **Monte Carlo simulation** for the Secret Santa problem.
- Runs a **Taylor series calculation** for the Secret Santa problem.
- Estimates the probability that at least one person draws their own name.

---

## 📦 Requirements

- Python 3.8+
- TQDM

Install dependencies with:

```bash
pip install tqdm
```

## 🚀 Usage
```bash
python secret-santa-pick-own-name-probability -n <N> -it <ITERATIONS> [-p <PRECISION>] [--progress] 
```

### ⚙️ Arguments

| Argument          | Description                                          | Required |
|-------------------|------------------------------------------------------|----------|
| -n                | Number of people in the Secret Santa event (integer) | 🟢       |
| -it, --iterations | Number of Monte Carlo iterations (integer)           | 🟢       |
| -p                | Number of decimal digits in output (integer)         | ⚪        |
| --progress        | Enable to see progress bar                           | ⚪        |

### 📊 Example Commands

To run simple simulation, use

```bash
python secret-santa-pick-own-name-probability -n 15 -it 100000
```

Additionally, to see real-time progress of simulation, use `--progress` flag:

```bash
python secret-santa-pick-own-name-probability -n 15 -it 100000000 --progress
```

Also, you may override default 6 digits precision of output probability by usage of `-p` argument:

```bash
python secret-santa-pick-own-name-probability -n 15 -it 100000000 -p 10 --progress
```

### 📈 What You’ll See

#### ⏳ Progress Bar (if enabled)

While the simulation is running, you will see a progress bar in the terminal showing:

- current iteration
- total number of iterations
- progress percentage

This helps track long simulations in real time.

#### ✅ Result Output

After the simulation finishes, the program prints the estimated probability.

```text
Probability (Monte Carlo method): 0.6325700000
Probability (Taylor series method): 0.6321205588
```

### 📌 Notes

- The progress bar updates during the simulation.
- The result is printed only after all iterations are completed.
- The program is designed for CLI usage and long-running simulations.