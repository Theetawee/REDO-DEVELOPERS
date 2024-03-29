from django.conf import settings
from django.utils.translation import get_language, get_language_info
from django.urls import reverse


def hreflang_context(request):
    language_info = {
        lang_code: get_language_info(lang_code) for lang_code, _ in settings.LANGUAGES
    }
    current_language = get_language()
    hreflang_tags = ""

    for lang_code, lang_info in language_info.items():
        # Construct the alternate URL with language prefix
        alternate_url = reverse(request.resolver_match.view_name)
        if current_language in alternate_url:
            alternate_url = alternate_url.split(current_language)[1]
        # Append the language code to the URL
        alternate_url_with_lang = f"/{lang_code}{alternate_url}"
        # Construct the full URL with the host
        full_url = f"https://{request.get_host()}{alternate_url_with_lang}"
        hreflang_tags += (
            f'<link rel="alternate" hreflang="{lang_code}" href="{full_url}" />\n'
        )

    return {"hreflang_tags": hreflang_tags}
