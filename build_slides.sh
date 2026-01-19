#!/bin/bash
# Build all Slidev lectures for GitHub Pages

REPO_NAME="coding_essential_for_astronomers"

for i in {1..22}; do
    LECTURE="Lecture${i}_Slides"
    SRC_DIR="slides_sources/${LECTURE}"
    DEST_DIR="docs/slides/${LECTURE}"
    
    if [ -d "$SRC_DIR" ]; then
        echo "Building ${LECTURE}..."
        
        # Create package.json
        cat > "${SRC_DIR}/package.json" << EOF
{
  "name": "lecture${i}-slides",
  "private": true,
  "scripts": {
    "build": "slidev build --base /${REPO_NAME}/slides/${LECTURE}/"
  },
  "dependencies": {
    "@slidev/cli": "^0.50.0",
    "@slidev/theme-default": "latest"
  }
}
EOF
        
        # Install and build
        cd "$SRC_DIR"
        npm install --silent 2>/dev/null
        npm run build 2>/dev/null
        cd - > /dev/null
        
        # Copy to docs/slides
        mkdir -p "$DEST_DIR"
        rm -rf "${DEST_DIR:?}/"*
        cp -r "${SRC_DIR}/dist/"* "$DEST_DIR/"
        
        echo "✓ ${LECTURE} built"
    else
        echo "⚠ ${LECTURE} source not found"
    fi
done

echo "All slides built!"
