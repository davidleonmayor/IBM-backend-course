#!/usr/bin/zsh

# Validate if the folders are passed
if [[ $# != 2 ]]; then
  echo "Usage: backup.sh target_directory_name destination_directory_name"
  exit 1
fi

# Validate if the folders exist
if [[ ! -d "$1" ]] || [[ ! -d "$2" ]]; then
  echo "Invalid directory path provided"
  exit 1
fi

# Variables
orig_dir="$1"
dest_dir="$2"
timestamp=$(date "+%Y%m%d_%H%M%S")
backup_filename="backup-$timestamp.tar.gz"

# Find files modified in the last 24 hours and archive them
cd "$orig_dir" || exit 1

# Backup ONLY files modified in last 24h
find . -type f -mtime -1 | tar -czf "/tmp/$backup_filename" -T -

# Move backup to destination directory
mv "/tmp/$backup_filename" "$dest_dir"

echo "Backup completed: $backup_filename"

