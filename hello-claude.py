import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"],
    max_retries=3,
)

def ask(prompt: str) -> str:
    try:
        resp = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}],
        )
        block = resp.content[0]
        return block.text if block.type == "text" else ""
    except anthropic.RateLimitError:
        return "Rate limited — retry after a short backoff."
    except anthropic.AuthenticationError:
        return "Invalid API key."
    except anthropic.APIStatusError as e:
        return f"API error {e.status_code}: {e.message}"
