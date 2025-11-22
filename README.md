# DeepCode Fork

> **Note**: This is a fork of the original [DeepCode](https://github.com/HKUDS/DeepCode) project by HKUDS.
> 
> **Original Project**: [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode)  
> **Full Documentation**: See the [original repository](https://github.com/HKUDS/DeepCode) for complete details, architecture, and results.
>
> **Credit**: All core functionality and architecture belong to the original DeepCode team at HKU Data Science Lab.

---

## What is DeepCode?

DeepCode is an AI-powered multi-agent system that automatically converts research papers and text descriptions into working code.

**Key Features:**
- 📄 **Paper2Code**: Convert research papers into implementations
- 🎨 **Text2Web**: Generate frontend code from descriptions  
- ⚙️ **Text2Backend**: Create backend services from requirements

---

## Quick Start

### 1. Install UV (Recommended)

```bash
# Install UV package manager
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone and Setup

```bash
# Clone this repository
git clone https://github.com/Asad-Ismail/paper-implementation-DC.git
cd paper-implementation-DC

# Create virtual environment and install dependencies
uv venv --python=3.13
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### 3. Configure API Keys

Edit `mcp_agent.secrets.yaml` with your API keys:

```yaml
# Required: Add your LLM API key
openai:
  api_key: "your-api-key-here"
  base_url: "https://api.openai.com/v1"  # or your custom endpoint

# Optional: For Claude models
anthropic:
  api_key: "your-anthropic-key"
```

**Verify your LLM connection:**
```bash
uv run python verify_llm_connection.py
```

### 4. Run DeepCode

**Web UI (Recommended):**
```bash
uv run streamlit run ui/streamlit_app.py
```

**CLI:**
```bash
uv run python cli/main_cli.py
```

---

## Usage Examples

### Web Interface
1. Launch the web UI: `uv run streamlit run ui/streamlit_app.py`
2. Upload a research paper PDF or enter your requirements
3. Select the task type (Paper2Code, Text2Web, or Text2Backend)
4. Click "Generate" and watch the agents work

### CLI Interface
```bash
# Start the CLI
uv run python cli/main_cli.py

# Follow the prompts to:
# - Upload papers/documents
# - Describe what you want to build
# - Select implementation options
```

---

## Important Configuration Files

- `mcp_agent.secrets.yaml` - API keys and credentials
- `mcp_agent.config.yaml` - Tool and agent configuration
- `requirements.txt` - Python dependencies

---

## Common Issues

**API Key Errors**: Make sure your API keys are correctly set in `mcp_agent.secrets.yaml`

**Import Errors**: Ensure you activated the virtual environment: `source .venv/bin/activate`

**Missing Dependencies**: Run `uv pip install -r requirements.txt` again

---

## Learn More

For detailed documentation, architecture details, and experimental results, visit the original project:

🔗 **Original DeepCode Repository**: https://github.com/HKUDS/DeepCode

---

## License

This project inherits the license from the original DeepCode project. Please refer to the [LICENSE](LICENSE) file.
