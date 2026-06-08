"""
Backend i18n helper.

Usage in a route:
    from src.i18n import get_t
    t = get_t(request)
    raise HTTPException(400, t("auth.passwordTooShort"))

Or rely on the I18nMiddleware (registered in app.py) which automatically
translates the `detail` field of error responses based on Accept-Language.
"""

import json
import os
from functools import lru_cache
from typing import Callable

_LOCALES_DIR = os.path.join(os.path.dirname(__file__), '..', 'locales')

@lru_cache(maxsize=4)
def _load(lang: str) -> dict:
    path = os.path.join(_LOCALES_DIR, f'py_{lang}.json')
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def _detect_lang(accept_language: str | None) -> str:
    if not accept_language:
        return 'en'
    al = accept_language.lower()
    if 'zh' in al:
        return 'zh'
    return 'en'

def get_t(request) -> Callable[[str], str]:
    """Return a translator bound to the request's preferred language."""
    lang = _detect_lang(request.headers.get('accept-language'))
    zh = _load('zh')
    en = _load('en')

    def t(key: str) -> str:
        if lang == 'zh':
            return zh.get(key) or en.get(key) or key
        return en.get(key) or key

    return t


def translate_detail(detail: str, accept_language: str | None) -> str:
    """
    Translate a known error detail string.
    Called by I18nMiddleware to post-process error responses.
    """
    lang = _detect_lang(accept_language)
    if lang == 'en':
        return detail
    zh = _load('zh')
    # Look up by value in English dict, return Chinese equivalent
    en = _load('en')
    for key, en_val in en.items():
        if en_val == detail:
            return zh.get(key, detail)
    return detail
