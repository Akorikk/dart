# Benchmarks

Fill this table after running 10 calls.

| Run | Latency (ms) |
|-----|--------------|
| 1   |     76      |
| 2   |     89          |
| 3   |     96         |
| 4   |     105         |
| 5   |     76         |
| 6   |     80         |
| 7   |     88         |
| 8   |     71         |
| 9   |     76        |
| 10  |     83         |

**Min:**  71 ms
**Max:**  105 ms
**Average:**  84.0 ms
**P95:**  105 ms

## RCA (3–5 sentences)
Benchmarks were collected after an initial warm-up run to measure steady-state performance.  
Latency remains stable because embeddings are computed locally using a preloaded model.  
Minor variance is caused by CPU scheduling and background system load.  
The absence of network calls eliminates external latency and reduces tail latency.

