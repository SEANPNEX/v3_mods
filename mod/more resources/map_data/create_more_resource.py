import os
import re

# Multipliers
ARABLE_MULT = 7
IRON_COAL_MULT = 5
SULFUR_MULT = 5
LOG_FISH_MULT = 10
LEAD_MULT = 5
GOLD_MULT = 3
OIL_RUBBER_MULT = 5

# Directory containing the state files
state_regions_dir = "state_regions/"

# Regular expressions and corresponding multipliers
patterns = [
    (r"(arable_land\s*=\s*)(\d+)", ARABLE_MULT),
    (r"(.*sulfur.*?\s*=\s*)(\d+)", SULFUR_MULT),
    (r"(.*lead.*?\s*=\s*)(\d+)", LEAD_MULT),
    (r"(.*gold.*?\s*=\s*)(\d+)", GOLD_MULT),
    (r"(.*(iron|coal).*?\s*=\s*)(\d+)", IRON_COAL_MULT),
    (r"(.*(logging|fishing)\s*=\s*)(\d+)", LOG_FISH_MULT),
    (r"(undiscovered_amount\s*=\s*)(\d+)", OIL_RUBBER_MULT),
]

# Function to update file content
def update_values_in_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Update the values using the defined patterns
    for pattern, multiplier in patterns:
        content = re.sub(
            pattern,
            lambda m: f"{m.group(1)}{int(m.group(3) if m.lastindex == 3 else m.group(2)) * multiplier}",
            content,
        )

    # Overwrite the file with updated content
    with open(file_path, "w") as file:
        file.write(content)

    print(f"Successfully updated: {file_path}")

# Loop through files in the directory
for filename in os.listdir(state_regions_dir):
    file_path = os.path.join(state_regions_dir, filename)

    # Process only .txt files
    if filename.endswith(".txt") and os.path.isfile(file_path):
        update_values_in_file(file_path)

print("All files in 'state_regions/' have been updated.")
