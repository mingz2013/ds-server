#!/usr/bin/env bash


root_path=`pwd`

echo "$root_path"


source_path="$root_path/source"
bin_path="$root_path/bin"
log_path="$bin_path/log"

echo "$source_path"
echo "$bin_path"

if [ -d "$bin_path" ]; then
    rm -rf "$bin_path"
fi

mkdir "$bin_path"
mkdir "$log_path"
touch "$log_path/log.log"
touch "$log_path/debug.log"

cp -rf "$source_path/webroot/" "$bin_path"
cp -rf "$source_path/config/" "$bin_path"
cp -rf "$source_path/scripts/" "$bin_path"

for i in `find "$source_path" -name src`; do
    cp -rf "$i/"* "$bin_path";
done

