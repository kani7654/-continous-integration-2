import onnxruntime as ort
import numpy as np
import time
import json

MODEL = "model.onnx"

def run_benchmark(model_path, iters=50):
    sess = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])
    inp = sess.get_inputs()[0]
    shape = inp.shape
    shape = [1 if isinstance(d, str) or d is None else d for d in shape]
    x = np.random.rand(*shape).astype(np.float32)

    latencies = []
    for _ in range(iters):
        t0 = time.time()
        sess.run(None, {inp.name: x})
        latencies.append((time.time() - t0) * 1000)

    return {
        "mean_ms": float(np.mean(latencies)),
        "p95_ms": float(np.percentile(latencies, 95)),
        "runs": iters,
    }

if __name__ == "__main__":
    res = run_benchmark(MODEL, iters=20)
    print("Benchmark result:", res)
    with open("perf_result.json", "w") as f:
        json.dump(res, f)
