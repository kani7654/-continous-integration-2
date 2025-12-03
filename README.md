# Performance Benchmark CI Pipeline 

This project automates a lightweight performance benchmark using **GitHub Actions** to simulate on-device inference performance tracking.

##  Goals
- Automatically benchmark performance on each commit
- Detect performance issues early in development
- Upload performance reports for review
- Demonstrate CI testing similar to Snapdragon workflows

---

##  What the CI Does

On every push or Pull Request:

1️ Install dependencies  
2️ Run a NumPy matrix-multiplication benchmark  
3️ Measure:
   - Mean latency (ms)
   - p95 latency
   - Number of inference iterations  

4️ Upload performance results (`perf_result.json`) as CI artifacts

If benchmark runs successfully → CI passes   
If anything fails → CI stops 
