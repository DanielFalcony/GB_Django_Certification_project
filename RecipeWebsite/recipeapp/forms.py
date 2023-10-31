from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль:', strip=False,
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                help_text='Одна большая буква и т.д.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class RecipeAddForm(forms.Form):
    recipe_name = forms.CharField(max_length=100, required=True, label='Название рецепта:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите название Рецепта'}))
    recipe_description = forms.CharField(label='Описание рецепта:',
                                         widget=forms.Textarea(attrs={'placeholder': 'Введите описание товара.'}))
    recipe_cooking_steps = forms.CharField(label='Шаги приготовления:', required=True,
                                           widget=forms.Textarea(attrs={'placeholder': 'Введите шаги приготовления.'}))
    recipe_cooking_time = forms.IntegerField(label='Введите время приготовления в минутах:', min_value=1, required=True,
                                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # recipe_author = forms.CharField(label='Автор рецепта', widget=forms.TextInput(
    #     attrs={'placeholder': 'Укажите автора рецепта'}))
    recipe_category = forms.CharField(label='Категория рецепта', widget=forms.TextInput(
        attrs={'placeholder': 'Укажите категорию рецепта'}))
    product_image = forms.ImageField(label='Изображение товара:')


class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'img', 'category']
