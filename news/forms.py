from django.forms import ModelForm, widgets, ModelChoiceField, CharField, Select, DateTimeField, ModelMultipleChoiceField, Textarea
from .models import Post, Author, Category, CATEGORY_CHOICES


class PostForm(ModelForm):
    author = ModelChoiceField(queryset=Author.objects.all(), label='Автор:')
    categoryType = CharField(label='Статья или Новость:', widget=Select(choices=CATEGORY_CHOICES))
    postCategory = ModelMultipleChoiceField(label='Категория', queryset=Category.objects.all())
    title = CharField(label='Заголовок', max_length=255)
    text = CharField(label='Текст статьи', widget=Textarea())

    class Meta:
        model = Post
        fields = [
            'author', 'categoryType', 'postCategory', 'title', 'text',
        ]