from django import template

register = template.Library()

@register.inclusion_tag('pages/word_list_page.html')
def word_list_header_title(value: str, arg: str):
    (french, english) = arg.split(",")
    return '''
    <div> hello </div>
    '''