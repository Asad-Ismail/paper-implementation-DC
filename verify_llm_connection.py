#!/usr/bin/env python3
"""
Final verification that config will work with mcp_agent
"""

import asyncio
import yaml
import httpx
from openai import AsyncOpenAI
from openai import OpenAI
import pprint

async def test_final_config():
    print("=" * 70)
    print("Final Configuration Test for MCP Agent")
    print("=" * 70)
    
    # Load actual config
    with open('mcp_agent.secrets.yaml', 'r') as f:
        secrets = yaml.safe_load(f)
    
    with open('mcp_agent.config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    api_key = secrets['openai']['api_key']
    base_url = secrets['openai']['base_url']
    verify = secrets['openai'].get('verify', True)
    model = config['openai']['default_model']



    client = OpenAI(api_key=api_key, base_url="https://chat.int.bayer.com/api/v2")
    all_models = client.models.list()
    print("*"*100)
    print(f"Available models: {all_models.data}")
    print("*"*100)
    
    print(f"\nConfiguration:")
    print(f"  API Key: {api_key[:20]}...")
    print(f"  Base URL: {base_url}")
    print(f"  SSL Verify: {verify}")
    print(f"  Model: {model}")
    
    # Test async call (like mcp_agent uses)
    print(f"\nTesting async call with model '{model}'...")
    
    try:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        http_client_kwargs = {}
        if verify is False:
            http_client_kwargs['verify'] = False
        elif isinstance(verify, str):
            http_client_kwargs['verify'] = verify
        
        async with AsyncOpenAI(
            api_key=api_key,
            base_url=base_url,
            http_client=httpx.AsyncClient(**http_client_kwargs) if http_client_kwargs else None
        ) as client:
            # Test with system prompt (like ResearchAnalyzerAgent)
            response = await client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Respond concisely."},
                    {"role": "user", "content": "Say 'Configuration verified successfully' and nothing else"}
                ],
                max_tokens=20,
                temperature=0
            )
            
            content = response.choices[0].message.content
            print(f"\n✅ SUCCESS!")
            print(f"   Model used: {response.model}")
            print(f"   Response: {content}")
            print(f"   Tokens: {response.usage.total_tokens if response.usage else 'N/A'}")
            
            print("\n" + "=" * 70)
            print("🎉 Configuration is valid! The Streamlit app should work now.")
            print("=" * 70)
            print("\nRestart the Streamlit app:")
            print("  uv run streamlit run ui/streamlit_app.py")
            
            return True
            
    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        print("\n" + "=" * 70)
        print("Configuration still has issues. Error details:")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    asyncio.run(test_final_config())
