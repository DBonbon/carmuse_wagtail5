from urllib.parse import urlparse, urlunparse
from django.http import QueryDict
from catalog.models import PaintingCategory as Category #Tag
from catalog.models import PaintingPageTag as Tag
from django.template import Library, loader
# from blog.md_converter.utils import render_markdown

register = Library()


# @register.simple_tag()
# def post_page_date_slug_url(post_page, blog_page):
#     post_date = post_page.post_date
#     url = blog_page.full_url + blog_page.reverse_subpage(
#         "post_by_date_slug",
#         args=(
#             post_date.year,
#             "{0:02}".format(post_date.month),
#             "{0:02}".format(post_date.day),
#             post_page.slug,
#         ),
#     )
#     return url


@register.inclusion_tag('catalog/components/tags_list.html',
                        takes_context=True)
def tags_list(context):
    tags = Tag.objects.all()
    return {
        'request': context['request'],
        'painting_index_page': context['painting_index_page'],
        'tags': tags
    }


@register.inclusion_tag('catalog/components/categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'painting_index_page': context['painting_index_page'],
        'categories': categories
    }



@register.inclusion_tag("catalog/components/painting_categories_list.html", takes_context=True)
def painting_categories_list(context):
    page = context["page"]
    categories = page.painting_categories.all()
    return {
        "request": context["request"],
        "categories": categories,
    }


@register.inclusion_tag("catalog/components/painting_tags_list.html", takes_context=True)
def painting_tags_list(context):
    page = context["page"]
    painting_tags = page.tags.all()
    return {
        "request": context["request"],
        "painting_tags": painting_tags,
    }

#
# @register.simple_tag
# def url_replace(request, **kwargs):
#     """
#     This tag can help us replace or add querystring
#     TO replace the page field in URL
#     {% url_replace request page=page_num %}
#     """
#     (scheme, netloc, path, params, query, fragment) = urlparse(request.get_full_path())
#     query_dict = QueryDict(query, mutable=True)
#     for key, value in kwargs.items():
#         query_dict[key] = value
#     query = query_dict.urlencode()
#     return urlunparse((scheme, netloc, path, params, query, fragment))
#
#
# @register.filter(name='markdown')
# def markdown(value):
#     return render_markdown(value)
#
