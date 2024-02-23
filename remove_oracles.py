import os
import json
import sys

if __name__ == "__main__":
    file_path = sys.argv[1]
    id_list = [int(arg) for arg in sys.argv[2:]]
    # Read the file
    with open(file_path, "r") as file:
        oracles = json.load(file)
        print(f"Removing oracles with ids: {id_list} (total: {len(id_list)})")
        print(f"Before: {len(oracles)} oracles")
        filtered_oracles = [oracle for oracle in oracles if oracle["id"] not in id_list]
        print(f"After: {len(filtered_oracles)} oracles")
        # Write the file
        with open(file_path, "w") as file:
            json.dump(filtered_oracles, file, indent=4)