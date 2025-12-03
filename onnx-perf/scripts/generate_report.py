import json

if __name__ == "__main__":
    with open("perf_result.json", "r") as f:
        r = json.load(f)

    print("## Performance report")
    print()
    print(f"- Mean latency: {r['mean_ms']:.2f} ms")
    print(f"- P95 latency: {r['p95_ms']:.2f} ms")
    print(f"- Runs: {r['runs']}")
