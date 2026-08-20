#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 TARGET_DIRECTORY" >&2
  exit 2
fi

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
template_dir="$script_dir/../template"
target_dir=$1

if [ -e "$target_dir" ]; then
  if [ ! -d "$target_dir" ] || [ "$(find "$target_dir" -mindepth 1 -maxdepth 1 -print -quit)" ]; then
    echo "Refusing to overwrite non-empty target: $target_dir" >&2
    exit 1
  fi
else
  mkdir -p "$target_dir"
fi

cp -R "$template_dir/." "$target_dir/"
echo "Created research workspace at: $target_dir"
echo "Next: edit .agents/context/project.md and research/NOW.md"
