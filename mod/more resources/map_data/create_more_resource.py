import os
import re
import sys

# Multipliers
ARABLE_MULT = 7
IRON_COAL_MULT = 5
SULFUR_MULT = 5
LOG_FISH_MULT = 10
LEAD_MULT = 5
GOLD_MULT = 3
OIL_RUBBER_MULT = 5

# Capped resources (building type -> multiplier)
CAPPED_MULTS = {
    "building_iron_mine": IRON_COAL_MULT,
    "building_coal_mine": IRON_COAL_MULT,
    "building_sulfur_mine": SULFUR_MULT,
    "building_lead_mine": LEAD_MULT,
    "building_gold_mine": GOLD_MULT,
    "building_logging_camp": LOG_FISH_MULT,
    "building_fishing_wharf": LOG_FISH_MULT,
}

# Directory containing the state files.
# Usage:
#   python create_more_resource.py                      -> updates ./state_regions/ in place
#   python create_more_resource.py <vanilla_dir>        -> reads the game's state_regions folder
#                                                          and writes the result to ./state_regions/
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "state_regions")
input_dir = sys.argv[1] if len(sys.argv) > 1 else output_dir

ARABLE_RE = re.compile(r"(\barable_land\s*=\s*)(\d+)")
CAPPED_RE = re.compile(r"\b(" + "|".join(CAPPED_MULTS) + r")(\s*=\s*)(\d+)")
# Oil, rubber and gold fields (discovered_amount is left untouched)
UNDISCOVERED_RE = re.compile(r"(\bundiscovered_amount\s*=\s*)(\d+)")


def multiply(content):
    content = ARABLE_RE.sub(lambda m: f"{m.group(1)}{int(m.group(2)) * ARABLE_MULT}", content)
    content = CAPPED_RE.sub(
        lambda m: f"{m.group(1)}{m.group(2)}{int(m.group(3)) * CAPPED_MULTS[m.group(1)]}",
        content,
    )
    content = UNDISCOVERED_RE.sub(
        lambda m: f"{m.group(1)}{int(m.group(2)) * OIL_RUBBER_MULT}", content
    )
    return content


# Function to update file content
def update_values_in_file(in_path, out_path):
    # Game files are UTF-8 with BOM; keep the BOM so the game reads them correctly
    with open(in_path, "r", encoding="utf-8-sig", newline="") as file:
        content = file.read()

    content = multiply(content)

    with open(out_path, "w", encoding="utf-8-sig", newline="") as file:
        file.write(content)

    print(f"Successfully updated: {out_path}")


os.makedirs(output_dir, exist_ok=True)

# Loop through files in the directory
for filename in sorted(os.listdir(input_dir)):
    in_path = os.path.join(input_dir, filename)

    # Process only .txt files
    if filename.endswith(".txt") and os.path.isfile(in_path):
        update_values_in_file(in_path, os.path.join(output_dir, filename))

print("All files in 'state_regions/' have been updated.")
