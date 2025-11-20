#!/usr/bin/env python3
"""
Wrapper to run Streamlit with SSL verification disabled for httpx
This patches httpx.AsyncClient before mcp_agent imports it
"""

import sys
import os

# Monkey-patch httpx before any imports
import httpx

_original_async_client_init = httpx.AsyncClient.__init__

def _patched_async_client_init(self, *args, **kwargs):
    # Force verify=False if not explicitly set
    if 'verify' not in kwargs:
        kwargs['verify'] = False
    return _original_async_client_init(self, *args, **kwargs)

httpx.AsyncClient.__init__ = _patched_async_client_init

print("🔧 Patched httpx.AsyncClient to disable SSL verification")
print("🚀 Starting Streamlit...")

# Now run streamlit
from streamlit.web import cli as st_cli

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "ui/streamlit_app.py"]
    sys.exit(st_cli.main())
