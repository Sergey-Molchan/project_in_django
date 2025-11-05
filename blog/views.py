from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/templates/blog_list.html'

    def get_queryset(self):
        return Blog.object.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/templates/blog_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count +=1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/templates/blog_form.html'
    fields = ['title', 'content', 'image', 'is_published']


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/templates/blog_form.html'
    fields = ['title', 'content', 'image', 'is_published']

    def get_success_url(self):
        # Перенаправляем на страницу статьи
        return reverse('blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')