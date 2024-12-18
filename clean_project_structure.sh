#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting project structure cleanup..."

# 1. Remove Duplicate Source Files from Root Directory
DUPLICATE_FILES=("plant.py" "weather.py" "storage.py")

echo "Removing duplicate source files from root directory..."
for FILE in "${DUPLICATE_FILES[@]}"; do
    if [ -f "$FILE" ]; then
        echo "Removing $FILE from root directory..."
        rm "$FILE"
    else
        echo "Warning: $FILE not found in root directory. Skipping."
    fi
done

# 2. Rename Test Files to Follow Naming Conventions
TEST_DIR="tests"
echo "Renaming test files in '$TEST_DIR/' directory to follow 'test_*.py' convention..."

# Ensure the tests directory exists
if [ -d "$TEST_DIR" ]; then
    for TEST_FILE in "$TEST_DIR"/*.py; do
        BASENAME=$(basename "$TEST_FILE")
        # Skip files that already follow the convention
        if [[ $BASENAME != test_* ]]; then
            NEW_NAME="test_${BASENAME}"
            echo "Renaming $BASENAME to $NEW_NAME..."
            mv "$TEST_FILE" "$TEST_DIR/$NEW_NAME"
        else
            echo "$BASENAME already follows the naming convention. Skipping."
        fi
    done
else
    echo "Error: '$TEST_DIR/' directory does not exist."
    exit 1
fi

# 3. Delete Unnecessary Files and Directories
UNNECESSARY_FILES=("setup.py.bak")
UNNECESSARY_DIRS=("build" "terminal_garden.egg-info" "dist")

echo "Deleting unnecessary backup files..."
for FILE in "${UNNECESSARY_FILES[@]}"; do
    if [ -f "$FILE" ]; then
        echo "Removing $FILE..."
        rm "$FILE"
    else
        echo "Warning: $FILE not found. Skipping."
    fi
done

echo "Deleting unnecessary directories..."
for DIR in "${UNNECESSARY_DIRS[@]}"; do
    if [ -d "$DIR" ]; then
        echo "Removing directory $DIR..."
        rm -rf "$DIR"
    else
        echo "Warning: Directory $DIR not found. Skipping."
    fi
done

# 4. Verify Project Structure
echo "Verifying the updated project structure..."
tree

echo "Project structure cleanup completed successfully!"