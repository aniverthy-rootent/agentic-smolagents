"""Deterministic offline "LLM" so every example runs with no API key.

It does not understand language; it produces a structured, role-aware reply so
you can watch the orchestration (hand-offs, state, tool calls) work end to end.
Swap in a real model by following the README of each repository.
"""
from __future__ import annotations

import hashlib
import re


def _digest(text: str, n: int = 3) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z\-]{3,}", text)
    seen: list[str] = []
    for w in words:
        lw = w.lower()
        if lw not in seen:
            seen.append(lw)
    if not seen:
        return ["input"]
    h = int(hashlib.sha256(text.encode()).hexdigest(), 16)
    start = h % len(seen)
    return [seen[(start + i) % len(seen)] for i in range(min(n, len(seen)))]


def offline_complete(system: str, user: str) -> str:
    """Return a deterministic, role-flavoured response."""
    role = system.strip().split("\n", 1)[0][:80] or "Agent"
    keys = ", ".join(_digest(user))
    snippet = " ".join(user.split())[:110]
    return (
        f"[{role}] key points: {keys}. "
        f"Considered input: '{snippet}'. "
        f"Recommendation: proceed with the next step."
    )
