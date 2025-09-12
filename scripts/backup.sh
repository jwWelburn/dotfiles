#!/bin/bash
# Snapshot backup script for Arch Linux
# Creates timestamped backups of Documents, Downloads, Pictures, and Videos
# Keeps only the last 15 backups

# === CONFIG ===
SRC_HOME="$HOME"
DEST_BASE="/mnt/B/backups"
LOGFILE="/var/log/backup.log"
KEEP=15

# === DIRECTORIES TO BACK UP ===
DIRS=("Documents" "Downloads" "Pictures" "Videos")

# === TIMESTAMP FORMAT ===
# Folder structure: day/month/year/time
DATE_DAY=$(date +"%d")
DATE_MONTH=$(date +"%m")
DATE_YEAR=$(date +"%Y")
DATE_TIME=$(date +"%H-%M")

BACKUP_PATH="$DEST_BASE/$DATE_DAY/$DATE_MONTH/$DATE_YEAR/$DATE_TIME"

# === CREATE DESTINATION DIR ===
mkdir -p "$BACKUP_PATH"

echo "=== Backup started at $(date) ===" | tee -a "$LOGFILE"

for DIR in "${DIRS[@]}"; do
    SRC="$SRC_HOME/$DIR"
    DEST_DIR="$BACKUP_PATH/$DIR"

    if [ -d "$SRC" ]; then
        echo "Backing up $SRC to $DEST_DIR ..." | tee -a "$LOGFILE"
        rsync -a --delete "$SRC/" "$DEST_DIR/" >> "$LOGFILE" 2>&1
    else
        echo "WARNING: $SRC does not exist, skipping..." | tee -a "$LOGFILE"
    fi
done

echo "=== Backup finished at $(date) ===" | tee -a "$LOGFILE"
echo "" | tee -a "$LOGFILE"

# === CLEANUP OLD BACKUPS ===
ALL_BACKUPS=($(find "$DEST_BASE" -type d -mindepth 4 -maxdepth 4 | sort))
COUNT=${#ALL_BACKUPS[@]}

if (( COUNT > KEEP )); then
    REMOVE_COUNT=$(( COUNT - KEEP ))
    echo "Cleaning up $REMOVE_COUNT old backups..." | tee -a "$LOGFILE"
    for OLD in "${ALL_BACKUPS[@]:0:$REMOVE_COUNT}"; do
        echo "Removing $OLD" | tee -a "$LOGFILE"
        rm -rf "$OLD"
    done
fi

