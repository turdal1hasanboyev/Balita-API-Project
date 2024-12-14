from django.shortcuts import render

from django.views import View


class CustomPageNotFoundPageView(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)

custom_page_not_found_page_view = CustomPageNotFoundPageView.as_view()
