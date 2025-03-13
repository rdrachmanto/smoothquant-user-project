from datasets import load_dataset

# Load the dataset
ds = load_dataset("Jackmin108/c4-en-validation", split="validation")

# Save to JSONL file
ds.to_json("c4-en-validation.jsonl", orient="records", lines=True)
