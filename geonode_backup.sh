#!/bin/bash

# Activate virtual environment
USER_HOME=/home/geosolutions

GEONODE_CODE_PATH="${USER_HOME}/nepal_geonode/"
GEONODE_VENV_PATH="${USER_HOME}/venvs/nepal_geonode/bin/activate"
BACKUP_FOLDER_PATH="${USER_HOME}/geonode_backup"

source $GEONODE_VENV_PATH

cd $GEONODE_CODE_PATH

# Make backup
python manage.py backup --force --backup-dir $BACKUP_FOLDER_PATH

# cd to backup folder path
cd $BACKUP_FOLDER_PATH

# Clean backup data
python "${GEONODE_CODE_PATH}/backup_cleaner.py"

# Sync only the backup files to remote service
rclone sync --include '*.zip' . drive:'Nepal Geonode/backup'
