#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define package name
PACKAGE_NAME="terminal_garden"

echo "Starting project restructuring into a Python package..."

# 1. Create Package Directory and __init__.py
echo "Creating package directory '${PACKAGE_NAME}'..."
mkdir -p ${PACKAGE_NAME}
touch ${PACKAGE_NAME}/__init__.py

# 2. Move Python Modules into the Package
echo "Moving Python modules into the package directory..."
PY_FILES=("garden.py" "commands.py" "plant.py" "weather.py" "storage.py")

for FILE in "${PY_FILES[@]}"; do
    if [ -f "$FILE" ]; then
        mv "$FILE" "${PACKAGE_NAME}/"
        echo "Moved $FILE to ${PACKAGE_NAME}/"
    else
        echo "Warning: $FILE not found in the root directory."
    fi
done

# 3. Update Import Statements in Moved Modules
echo "Updating import statements in the moved modules..."
for FILE in "${PY_FILES[@]}"; do
    PACKAGE_FILE="${PACKAGE_NAME}/${FILE}"
    if [ -f "$PACKAGE_FILE" ]; then
        sed -i "s/from \(plant\|weather\|storage\) import/from ${PACKAGE_NAME}.\1 import/g" "${PACKAGE_FILE}"
        sed -i "s/from commands import/from ${PACKAGE_NAME}.commands import/g" "${PACKAGE_FILE}"
        echo "Updated imports in ${PACKAGE_FILE}"
    fi
done

# 4. Update Import Statements in Tests
echo "Updating import statements in test modules..."
TEST_FILES=("plant.py" "weather.py" "storage.py" "test_garden.py")

for TEST_FILE in "${TEST_FILES[@]}"; do
    TEST_PATH="tests/${TEST_FILE}"
    if [ -f "$TEST_PATH" ]; then
        sed -i "s/from \(plant\|weather\|storage\) import/from ${PACKAGE_NAME}.\1 import/g" "${TEST_PATH}"
        sed -i "s/from commands import/from ${PACKAGE_NAME}.commands import/g" "${TEST_PATH}"
        echo "Updated imports in ${TEST_PATH}"
    fi
done

# 5. Update setup.py
echo "Updating setup.py to recognize the new package structure..."

# Backup the original setup.py
cp setup.py setup.py.bak

# Replace find_packages() to include the new package
sed -i "s/find_packages()/find_packages(include=['${PACKAGE_NAME}', '${PACKAGE_NAME}.*'])/" setup.py

# Update entry_points to point to the package's garden module
sed -i "s/entry_points={\s*'console_scripts': \[/entry_points={\n        'console_scripts': \[/g" setup.py
sed -i "/'console_scripts': \[/a \ \ \ \ \ \ \ \ 'terminal-garden=${PACKAGE_NAME}.garden:main'," setup.py

echo "Updated setup.py."

# 6. Clean Up Build and Cache Directories
echo "Cleaning up build and cache directories..."
rm -rf build/ terminal_garden.egg-info/ __pycache__/
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "Cleaned up build and cache directories."

# 7. Reinstall the Package
echo "Reinstalling the package..."
pip3 uninstall -y terminal-garden || true
pip3 install .

# 8. Verify Installation
echo "Verifying installation by running the 'terminal-garden' command..."
if command -v terminal-garden &> /dev/null
then
    echo "Installation successful. Running 'terminal-garden'..."
    terminal-garden
else
    echo "Error: 'terminal-garden' command not found. Please check your setup."
fi

echo "Project restructuring completed successfully."