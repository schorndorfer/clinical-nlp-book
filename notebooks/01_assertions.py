# /// script
# requires-python = ">=3.12"
# dependencies = ["marimo>=0.20,<1"]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import re
    from collections import Counter

    return Counter, mo, re


@app.cell
def _(mo):
    mo.md("""
    # Assertion context in fictional notes

    **Teaching example only.** These notes are synthetic. Never paste real patient
    information into this notebook. Each example has exactly one mention of
    *pneumonia*; its gold label describes that mention, not a diagnosis.
    """)
    return


@app.cell
def _():
    examples = (
        ("Assessment: pneumonia.", "present"),
        ("No evidence of pneumonia.", "absent"),
        ("Pneumonia in 2019, resolved.", "historical"),
        ("History of pneumonia, now resolved.", "historical"),
        ("Rule out pneumonia.", "possible"),
        ("Possible pneumonia on imaging.", "possible"),
        ("Mother had pneumonia.", "other_experiencer"),
        ("No fever today. Assessment: pneumonia.", "present"),
        ("Pneumonia is not present.", "absent"),
        ("Patient denies pneumonia.", "absent"),
    )
    return (examples,)


@app.cell
def _(mo):
    window = mo.ui.slider(1, 12, value=5, label="Words to inspect before the mention")
    window
    return (window,)


@app.cell
def _(re):
    def classify(note: str, n_words: int) -> str:
        """A deliberately limited, pre-mention cue baseline (not for clinical use)."""
        mention = re.search(r"\bpneumonia\b", note, flags=re.IGNORECASE)
        if mention is None:
            raise ValueError("This exercise requires exactly one pneumonia mention")
        prefix = re.findall(r"\b\w+\b", note[: mention.start()].lower())
        context = " ".join(prefix[-n_words:])
        if "mother had" in context or "father had" in context:
            return "other_experiencer"
        if "no" in prefix[-n_words:]:
            return "absent"
        if "history of" in context or "prior" in prefix[-n_words:]:
            return "historical"
        if "rule out" in context or "possible" in prefix[-n_words:]:
            return "possible"
        return "present"

    return (classify,)


@app.cell
def _(classify, examples, window):
    results = [
        {"note": note, "gold": gold, "predicted": classify(note, window.value)}
        for note, gold in examples
    ]
    return (results,)


@app.cell
def _(mo, results):
    mo.vstack(
        [mo.md("## Predictions\nCompare errors as you move the cue-window slider."), mo.ui.table(results)]
    )
    return


@app.cell
def _(Counter, mo, results):
    labels = ("present", "absent", "historical", "possible", "other_experiencer")
    correct = sum(row["gold"] == row["predicted"] for row in results)
    pairs = Counter((row["gold"], row["predicted"]) for row in results)
    header = "| Gold \\ Predicted | " + " | ".join(labels) + " |"
    separator = "|---|" + "---:|" * len(labels)
    rows = [
        "| " + gold + " | " + " | ".join(str(pairs[gold, predicted]) for predicted in labels) + " |"
        for gold in labels
    ]
    mo.md(
        f"## Evaluation\nExact-match accuracy: **{correct}/{len(results)}** "
        f"({correct / len(results):.0%}).\n\n"
        + "\n".join([header, separator, *rows])
        + "\n\nThis tiny, curated set cannot measure real-world clinical performance."
    )
    return


if __name__ == "__main__":
    app.run()
