#!/bin/bash
source_dir=.

set +e
flake8 --format=html --htmldir=flake8-report --count  $source_dir > flake8-report.txt
exit_code=$?
flake8 $source_dir
cat flake8-report.txt
python3 ci/createBadges.py lint

if [ $exit_code -ne 0 ]; then
  echo "flake8 failed, exiting..."
  exit $exit_code
fi