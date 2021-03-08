from django import template
import datetime

register = template.Library()

@register.inclusion_tag("tags/footer.html")
def get_footer():
	year = str(datetime.datetime.today().year)
	return {'year':year}
