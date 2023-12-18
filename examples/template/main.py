"""This is a template for the expected code submission format."""
from pathlib import Path

NOTES_PATH = Path("data/test_notes.csv")
SUBMISSION_PATH = Path("submission.csv")


def main():
    with NOTES_PATH.open("r") as f:
        # Run inference on the notes
        ...
        pass

    with SUBMISSION_PATH.open("w") as f:
        # Write predicted annotations to the output file
        ...
        pass
    
if __name__ == "__main__":
    main()