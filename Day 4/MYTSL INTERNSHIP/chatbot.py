"""Simple terminal chatbot using a chat-completions API.

Usage:
  1) Set your API key in the environment:
       export OPENAI_API_KEY="..."
     or
       export GROQ_API_KEY="..."
  2) Run:
       python3 chatbot.py

  Type `exit` to quit.

Notes:
  - This script uses the OpenAI-compatible Chat Completions endpoint.
  - If you use a different provider, adjust CHAT_API_BASE_URL as needed.
"""

import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict, List



def _load_env_file(path: str = ".env") -> None:
    """Lightweight .env loader (no external dependencies).

    Supports lines like:
      KEY="value"
      KEY=value
      # comments
    """
    if not os.path.exists(path):
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")

                # Don't override existing environment variables.
                os.environ.setdefault(key, val)
    except Exception:
        # Fail silently; env vars may already be set.
        return


_load_env_file(".env")


# Provider/base URL + model.
# OpenAI-style default; override if using Groq (or others).
BASE_URL = os.environ.get("CHAT_API_BASE_URL", "https://api.openai.com/v1")
MODEL = os.environ.get("CHAT_MODEL", "gpt-3.5-turbo")

# Optional configuration.
CHAT_SYSTEM_PROMPT = os.environ.get("CHAT_SYSTEM_PROMPT", "You are a helpful assistant.")
TEMPERATURE = float(os.environ.get("CHAT_TEMPERATURE", "0.7"))
REQUEST_TIMEOUT_S = float(os.environ.get("CHAT_REQUEST_TIMEOUT_S", "60"))

# Supported API key env vars (auto-detect).
API_KEY_CANDIDATES = ["OPENAI_API_KEY", "GROQ_API_KEY"]







def _pick_api_key() -> str:
    for key_name in API_KEY_CANDIDATES:
        val = os.environ.get(key_name)
        if val:
            return val
    missing = ", ".join(API_KEY_CANDIDATES)
    raise RuntimeError(
        f"Missing API key. Set one of these environment variables: {missing}."
    )


def _post_json(url: str, payload: dict, headers: dict) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_S) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8")
        except Exception:
            pass
        raise RuntimeError(
            f"HTTP {e.code} from API. Response body: {body[:2000]}"
        ) from e


def chat(messages: List[Dict[str, str]]) -> str:
    api_key = _pick_api_key()
    url = f"{BASE_URL}/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": TEMPERATURE,
    }

    result = _post_json(url=url, payload=payload, headers=headers)

    # OpenAI-compatible response shape:
    # { choices: [ { message: { role, content }, ... } ] }
    try:
        content = result["choices"][0]["message"]["content"]
        if not isinstance(content, str):
            raise TypeError("content is not a string")
        return content.strip()
    except Exception as e:
        raise RuntimeError(f"Unexpected API response: {result}") from e



def main() -> None:
    print("Terminal Chatbot (type 'exit' to quit)")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if user_input.lower() == "exit":
            print("Goodbye!")
            return

        if not user_input:
            continue

        try:
            assistant_reply = chat(user_input)
        except Exception as exc:
            print(f"Error: {exc}")
            continue

        print(f"Assistant: {assistant_reply}")


if __name__ == "__main__":
    main()

