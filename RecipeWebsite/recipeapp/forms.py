from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль:', strip=False,
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                help_text='Не менее 12 знаков, включая строчные, заглавные буквы, спецсимволы и цифры')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class RecipeAddForm(forms.Form):
    recipe_name = forms.CharField(label='Название рецепта:', max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите название рецепта'}))
    recipe_description = forms.CharField(label='Описание рецепта:', widget=forms.Textarea(
        attrs={'placeholder': 'Введите описание рецепта'}))
    recipe_cooking_steps = forms.CharField(label='Шаги приготовления:', required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Введите шаги приготовления.'}))
    recipe_cooking_time = forms.IntegerField(label='Введите время приготовления в минутах:', min_value=1, required=True,
                                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    recipe_category = forms.CharField(label='Категория рецепта', widget=forms.TextInput(
        attrs={'placeholder': 'Укажите категорию рецепта:'}))
    recipe_image = forms.ImageField(label='Изображение рецепта:')


class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'img', 'category']
