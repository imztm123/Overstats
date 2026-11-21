from __future__ import annotations

"""是区吗（shiqu）独立 LLM 配置。

本文件由 astrbot_plugin_overstats 的 auto 一键部署流程按插件面板中的
shiqu_llm_* 配置自动生成并覆盖（deploy/ops/config_writer.py）。
环境变量 OVERSTATS_SHIQU_LLM_* 优先级高于此处的默认值。

⚠️ 仓库里只保留空 Key 的占位版本；真实 api_key 由插件在部署时写入本地，
   不要把它提交上来。
"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ShiquLLMConfig:
    base_url: str = ''
    api_key: str = ''
    model: str = ''
    stream: bool = False
    timeout_seconds: int = 300
    retry: int = 0
    strict: bool = True
    json_mode: bool = True

    @property
    def chat_url(self) -> str:
        base = str(self.base_url or "").rstrip("/")
        if base.endswith("/chat/completions"):
            return base
        if base.endswith("/v1") or base.endswith("/openai"):
            return f"{base}/chat/completions"
        return f"{base}/chat/completions"


def _get(name: str, default: str = "") -> str:
    env_value = os.getenv(f"OVERSTATS_{name}")
    if env_value:
        return env_value.strip()
    return str(default or "").strip()


def _parse_bool(value: str, default: bool = True) -> bool:
    text = str(value or "").strip().lower()
    if not text:
        return default
    return text in {"1", "true", "yes", "on"}


def get_shiqu_llm_config() -> ShiquLLMConfig:
    return ShiquLLMConfig(
        base_url=_get("SHIQU_LLM_BASE_URL", ''),
        api_key=_get("SHIQU_LLM_API_KEY", ''),
        model=_get("SHIQU_LLM_MODEL", ''),
        stream=_parse_bool(_get("SHIQU_LLM_STREAM", False), False),
        timeout_seconds=int(_get("SHIQU_LLM_TIMEOUT", 300) or 300),
        retry=int(_get("SHIQU_LLM_RETRY", 0) or 0),
        strict=_parse_bool(_get("SHIQU_LLM_STRICT", "true"), True),
        json_mode=_parse_bool(_get("SHIQU_LLM_JSON_MODE", "true"), True),
    )


def is_shiqu_llm_configured() -> bool:
    cfg = get_shiqu_llm_config()
    return bool(cfg.base_url and cfg.api_key and cfg.model)


def get_shiqu_match_count(default: int = 12) -> int:
    try:
        return max(2, min(25, int(_get("SHIQU_MATCH_COUNT", str(default)) or default)))
    except (TypeError, ValueError):
        return default
