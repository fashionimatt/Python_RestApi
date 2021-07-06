from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def paging(request, resDict):

    # 페이징 기능 분리 : resArr, users(return)
    page = request.GET.get('page', 1)
    paginator = Paginator(resDict, 10)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return users
