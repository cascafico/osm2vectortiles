#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

source utils.sh

readonly BUCKET_NAME=${BUCKET_NAME:-osm2vectortiles-jobs}
readonly BEANSTALKD_HOST=${BEANSTALKD_HOST:-"beanstalkd"}

function export_remote_mbtiles() {
    exec python export_remote.py "$DEST_PROJECT_DIR" \
        --host="$BEANSTALKD_HOST" \
        --bucket="$BUCKET_NAME"
}

function main() {
    copy_source_project
    cleanup_dest_project
    replace_db_connection
    export_remote_mbtiles
}

main
