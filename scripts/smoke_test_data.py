from pathlib import Path

import pandas as pd
import typer


def main(train_notes_path: Path, train_annotations_path: Path):
    # Read training data
    train_notes = pd.read_csv(train_notes_path)
    train_annotations = pd.read_csv(train_annotations_path)

    # Subset to smoke test notes
    smoke_test_note_ids = ["12204158-DS-10", "11417242-DS-18", "11810606-DS-7"]
    smoke_notes = train_notes[train_notes.note_id.isin(smoke_test_note_ids)]
    smoke_annotations = train_annotations[train_annotations.note_id.isin(smoke_test_note_ids)]

    # Write to expected places in data/
    smoke_notes.to_csv("data/test_notes.csv", index=False)
    smoke_annotations.to_csv("data/smoke_test_annotations.csv", index=False)


if __name__ == "__main__":
    typer.run(main)
