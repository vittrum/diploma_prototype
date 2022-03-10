#!/bin/bash

flake8 item.py
echo "Item checked with flake"
mypy item.py
echo "Item checked with mypy"

