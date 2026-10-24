#!/bin/sh
set -eu

echo "BUILD START"
mkdir -p staticfiles_build/static
cp -R static/. staticfiles_build/static/
echo "BUILD END"