import os
import json
import sys

if __name__ == "__main__":
    file_original_path = sys.argv[1]
    dir_dest = sys.argv[2]
    id_list = [int(arg) for arg in sys.argv[3:]]
    filtered_oracles = []
    new_removed_oracles = []
    # Read the file
    with open(file_original_path, "r") as file_original:
        oracles = json.load(file_original)
        print(f"Removing oracles with ids: {id_list} (total: {len(id_list)})")
        print(f"Before: {len(oracles)} oracles")
        for oracle in oracles:
            if oracle["id"] not in id_list:
                filtered_oracles.append(oracle)
            else:
                new_removed_oracles.append(oracle)
        assert len(filtered_oracles) == len(oracles) - len(id_list)
        print(f"After: {len(filtered_oracles)} oracles")
    # Update the original file
    with open(file_original_path, "w") as file_original:
        json.dump(filtered_oracles, file_original, indent=4)
    # Update the backup file
    file_backup_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "oracles-backup",
        dir_dest,
        f"{oracles[0]['projectName']}_backup.json"
    )
    with open(file_backup_path, "r") as file_backup:
        oracles_removed = json.load(file_backup)
    oracles_removed.extend(new_removed_oracles)
    with open(file_backup_path, "w") as file_backup:
        json.dump(oracles_removed, file_backup, indent=4)