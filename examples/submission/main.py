"""This is an example of a valid, functional submission."""
from pathlib import Path

from loguru import logger
import pandas as pd

NOTES_PATH = Path("data/test_notes.csv")
SUBMISSION_PATH = Path("submission.csv")


if __name__ == "__main__":
    # columns are note_id, text
    logger.info("Reading in notes data.")
    notes = pd.read_csv(NOTES_PATH)
    logger.info(f"Found {notes.shape[0]} notes.")

    # generating valid spans by predicting that the entirety of 
    # each note should be annotated with the concept_id 4596009
    # |Laryngeal structure (body structure)|. "Valid" predictions
    # don't have to be good...
    spans = []
    for note in notes.itertuples():
        note_id = note.note_id
        text = note.text
        start, end = 0, len(text)
        concept_id = 4596009
        spans.append([note_id, start, end, concept_id])
    
    logger.info(f"Generated {len(spans)} annotated spans.")
    headers = ['note_id', 'start', 'end', 'concept_id']
    spans_df = pd.DataFrame(columns=headers, data=spans)
    spans_df.to_csv(SUBMISSION_PATH, index=False)
