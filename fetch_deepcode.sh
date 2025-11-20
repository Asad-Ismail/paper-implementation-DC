#!/bin/bash

# Script to fetch DeepCode repository without git history
# This will download the code into a 'deepcode' directory

echo "📥 Fetching DeepCode repository..."

# Create a temporary directory for cloning
TEMP_DIR=$(mktemp -d)
DEEPCODE_DIR="deepcode"

# Clone the repository with depth 1 (shallow clone)
git clone --depth 1 https://github.com/HKUDS/DeepCode.git "$TEMP_DIR"

# Remove the .git directory to strip git history
rm -rf "$TEMP_DIR/.git"

# Move contents to deepcode directory
if [ -d "$DEEPCODE_DIR" ]; then
    echo "⚠️  'deepcode' directory already exists. Removing it..."
    rm -rf "$DEEPCODE_DIR"
fi

mv "$TEMP_DIR" "$DEEPCODE_DIR"

echo "✅ DeepCode code fetched successfully to ./$DEEPCODE_DIR"
echo "📂 Contents:"
ls -la "$DEEPCODE_DIR"

echo ""
echo "🎉 Done! The code is now in the 'deepcode' directory without any git configuration."
