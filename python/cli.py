import time
import json
import math
import click
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)


def _json_print(obj):
    print(json.dumps(obj, indent=2))


def cosine_sim(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def compute_safe_delta(prev, curr):
    MAX_DELTA = 100 * 1024 * 1024
    if curr < prev:
        return 0
    delta = curr - prev
    return min(delta, MAX_DELTA)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--text", required=True, help="Input text (docA|docB for embeddings)")
@click.option("--task", required=True, type=click.Choice(["infer", "embed"]))
def run(task, text):
    t0 = time.time()

    try:
        if task == "embed":
            if "|" not in text:
                _json_print({"status": 400, "error": "Invalid input: expected docA|docB"})
                return

            docA, docB = text.split("|", 1)

            embA = model.encode(docA.strip()).tolist()
            embB = model.encode(docB.strip()).tolist()

            latency_ms = int((time.time() - t0) * 1000)
            sim = cosine_sim(embA, embB)

            _json_print({
                "status": 200,
                "latency_ms": latency_ms,
                "vector_dim": len(embA),
                "similarity_score": round(sim, 6)
            })

        else:
            _json_print({
                "status": 200,
                "latency_ms": int((time.time() - t0) * 1000),
                "output": f"infer stub: {text}"
            })

    except Exception as e:
        _json_print({"status": 500, "error": str(e)})


if __name__ == "__main__":
    cli()
