# Get current directory
current_dir=$(realpath "$(dirname "${BASH_SOURCE[@]}")")

# Arguments and setup check
if [ ! $# -eq 1 ]; then
  echo -e "remove_from_csv.sh: Incorrect number of arguments. Expected 1 argument, but got ${#}".
  exit 1
fi

csv_file="${1}"

while IFS=, read -r oracles_file oracle_id; do
  echo "python3 remove_oracles.py ${current_dir}/oracles-dataset/${oracles_file} miscellaneous ${oracle_id}"
  python3 remove_oracles.py "${current_dir}/oracles-dataset/${oracles_file}" miscellaneous "$oracle_id"
done < "$csv_file"