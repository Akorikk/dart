# Reasoning Notes

Briefly document key decisions and tradeoffs for:
- embeddings endpoint selection,
- cosine similarity implementation,
- quota logic,
- analytics delta handling.


# Reasoning Notes
* The sentence-transformers all-MiniLM-L6-v2 model was selected because it provides fast, high-quality sentence embeddings optimized for cosine similarity tasks.
 
* Cosine similarity was implemented explicitly to ensure numerical transparency and avoid hidden framework behavior.

* Quota enforcement uses hard upper bounds on prompt and completion tokens to prevent abuse and ensure predictable resource usage.

* Analytics deltas are clamped and sanitized to protect downstream systems from counter resets, rollbacks, or anomalous spikes.
