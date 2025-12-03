

import numpy as np
import time
import json

def run_benchmark(iters=50):
    
    x = np.random.rand(256, 256).astype(np.float32)
    y = np.random.rand(256, 256).astype(np.float32)

    latencies = []
    for _ in range(iters):
        t0 = time.time()
        _ = x @ y  
        latencies.append((time.time() - t0) * 1000.0)  # ms

    return {
        "mean_ms": float(np.mean(latencies)),
        "p95_ms": float(np.percentile(latencies, 95)),
        "runs": iters,
    }

if __name__ == "__main__":
    res = run_benchmark(iters=20)
    print("Benchmark result:", res)
    with open("perf_result.json", "w") as f:
        json.dump(res, f)
