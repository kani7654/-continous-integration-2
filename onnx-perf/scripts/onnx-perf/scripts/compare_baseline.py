import json
import sys

BASELINE = "baseline_perf.json"
CURRENT = "perf_result.json"

THRESHOLD = 1.10  # fail if mean latency increased by 10% or more

if __name__ == "__main__":
    with open(BASELINE, "r") as f:
        baseline = json.load(f)
    with open(CURRENT, "r") as f:
        current = json.load(f)

    b_mean = baseline["mean_ms"]
    c_mean = current["mean_ms"]

    ratio = c_mean / b_mean
    print(f"Baseline mean: {b_mean}, Current mean: {c_mean}, ratio: {ratio:.3f}")

    if ratio > THRESHOLD:
        print("Performance regression detected — failing")
        sys.exit(1)
    else:
        print("Performance OK")
