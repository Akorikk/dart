# System Design — Scaling to 10k req/min

Write ~10–15 sentences covering:
- batching strategy,
- embedding caching,
- backpressure + rejection policies,
- retry & exponential backoff,
- observability (metrics/logs/traces),
- degraded/fallback behavior,
- capacity planning notes.


# System Design — Scaling to 10k req/min

To scale DartCodeAI to 10k requests per minute, I would place an API gateway in front of the service to handle authentication and rate limiting.  
Embedding requests would be batched to improve throughput and reduce per-request overhead on the model.  
A caching layer keyed by a hash of the input text would store frequently requested embeddings to avoid recomputation.  
Backpressure would be applied using bounded queues, rejecting or delaying requests when capacity is exceeded.  
Retry logic with exponential backoff and jitter would handle transient failures safely.  
Observability would include metrics such as request latency percentiles, error rates, and throughput, along with structured logs.  
Distributed tracing would help identify bottlenecks across the request lifecycle.  
In degraded mode, the system would return cached embeddings or partial responses if the embedding service becomes unavailable.  
Capacity planning would be based on sustained p95 latency rather than average latency to ensure reliability under load.
