#!/bin/bash

# Wrapper script to run Streamlit with SSL verification disabled
# This is necessary for internal Bayer APIs with self-signed certificates

# Disable SSL warnings
export PYTHONWARNINGS="ignore:Unverified HTTPS request"

# Disable SSL verification for the process
export REQUESTS_CA_BUNDLE=""
export CURL_CA_BUNDLE=""

# Alternatively, to use the Bayer CA bundle (currently causes issues with httpx):
# export SSL_CERT_FILE="/Users/gmeax/bayer-scripts/ssl-certificates/monsanto_all.pem"
# export REQUESTS_CA_BUNDLE="/Users/gmeax/bayer-scripts/ssl-certificates/monsanto_all.pem"

# Set Python to not verify SSL (workaround for httpx/openai client)
export PYTHONHTTPSVERIFY=0

echo "🔧 SSL verification disabled for this session"
echo "🚀 Starting Streamlit app..."
echo ""

# Run streamlit with uv
uv run streamlit run ui/streamlit_app.py
