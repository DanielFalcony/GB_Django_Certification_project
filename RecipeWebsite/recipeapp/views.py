import logging

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Author

from .forms import RecipeAddForm
from .models import Recipe

logger = logging.getLogger(__name__)


@login_required  # Декоратор, защиты доступа без логина
def index(request):
    return render(request, 'recipeapp/index.html')


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            author = form.save()
            Author.objects.create(author=author)
            raw_password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            author = authenticate(username=author.username, password=raw_password)
            login(request, author)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'recipeapp/signup.html', {'form': form})


@login_required  # Декоратор, защиты доступа без логина
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeAddForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            recipe_name = form.cleaned_data['recipe_name']
            recipe_description = form.cleaned_data['recipe_description']
            recipe_cooking_steps = form.cleaned_data['recipe_cooking_steps']
            recipe_cooking_time = form.cleaned_data['recipe_cooking_time']
            recipe_author = form.cleaned_data['recipe_author']  # Поменять на нужного Юзера
            recipe_category = form.cleaned_data['recipe_category']
            product_image = form.cleaned_data['product_image']
            logger.info(
                f'Получили данные: {recipe_name=}, {recipe_cooking_steps=}, {recipe_cooking_time=}, {recipe_author=}, '
                f'{recipe_category=}, {product_image=},')
            recipe = Recipe(name=recipe_name, description=recipe_description, cooking_steps=recipe_cooking_steps,
                            cooking_time=recipe_cooking_time, author=recipe_author, category=recipe_category,
                            img=product_image)
            recipe.save()
            message = 'Рецепт сохранен!'
    else:
        form = RecipeAddForm()
        message = 'Заполните форму!'
    return render(request, 'recipeapp/add_recipe.html', context={'form': form, 'message': message})
