from taggit.models import Tag


def TaggitTagListContext(request):
    tag_list = Tag.objects.all().order_by('-pk')[0:15]
    return {'universal_tags': tag_list}
