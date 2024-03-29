from django import template
from django.utils.translation import get_language, get_language_info
from django.conf import settings

register = template.Library()


@register.filter
def redo_class(field, css_class):
    if css_class:
        field.field.widget.attrs["class"] = css_class

    return field


@register.filter
def redo_holder(field, placeholder):
    if placeholder:
        field.field.widget.attrs["placeholder"] = placeholder

    return field


@register.filter
def is_input(field):
    field.field.widget.attrs["class"] = (
        "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
    )


# custom_tags.py


register = template.Library()


@register.simple_tag
def hreflang_tags():
    language_info = {
        lang_code: get_language_info(lang_code) for lang_code, _ in settings.LANGUAGES
    }
    current_language = get_language()
    hreflang_tags = ""

    for lang_code, lang_info in language_info.items():
        if lang_code != current_language:
            hreflang_tags += f'<link rel="alternate" hreflang="{lang_code}" href="{lang_info["code"]}" />\n'

    return hreflang_tags
