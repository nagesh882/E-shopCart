from category.models import Category


# I have created here menu link for all categories
# this link we can use everyware in templates


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)