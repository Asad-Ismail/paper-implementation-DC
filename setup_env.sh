#!/bin/bash

# Script to install uv, create a virtual environment, and activate it
# Run with: source setup_env.sh

echo "🚀 Setting up Python environment with uv..."

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Add uv to PATH for current session
    export PATH="$HOME/.cargo/bin:$PATH"
else
    echo "✅ uv is already installed"
fi

# Create virtual environment with uv (Python 3.10+ required for deepcode-hku)
echo "🔨 Creating virtual environment with Python 3.10+..."
uv venv --python 3.10

# Activate the virtual environment
echo "✨ Activating virtual environment..."
source .venv/bin/activate

uv pip install deepcode-hku

# Verify activation
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment activated successfully!"
    echo "Virtual environment location: $VIRTUAL_ENV"
    echo "🐍 Python version: $(python --version)"
else
    echo "❌ Failed to activate virtual environment"
    exit 1
fi

echo ""
echo "🎉 Setup complete! Your virtual environment is ready to use."
echo "💡 To deactivate, run: deactivate"
