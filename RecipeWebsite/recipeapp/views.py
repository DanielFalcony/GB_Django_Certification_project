import logging
from random import sample

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, RecipeEditForm
from .models import Author, Category

from .forms import RecipeAddForm
from .models import Recipe

logger = logging.getLogger(__name__)


# @login_required  # Декоратор, защиты доступа без логина
def index(request):
    return render(request, 'recipeapp/index.html')


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Author.objects.create(user=user)
            raw_password = form.cleaned_data.get('password1')
            logger.info(f'Создан новый пользователь {user=}')
            # выполняем аутентификацию
            author = authenticate(username=user.username, password=raw_password)
            login(request, author)
            logger.info(f'Пользователь {author=} произвел вход.')
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
            if request.user.is_authenticated:
                author, created = Author.objects.get_or_create(user=request.user)
                recipe_author = author
            recipe_category = form.cleaned_data['recipe_category']
            category, created = Category.objects.get_or_create(name=recipe_category)
            product_image = form.cleaned_data['product_image']
            logger.info(
                f'Получили данные: {recipe_name=}, {recipe_cooking_steps=}, {recipe_cooking_time=}, {recipe_author.user=}, '
                f'{recipe_category=}, {product_image=},')
            recipe = Recipe(name=recipe_name, description=recipe_description, cooking_steps=recipe_cooking_steps,
                            cooking_time=recipe_cooking_time, author=recipe_author, category=category,
                            img=product_image)
            recipe.save()
            message = 'Рецепт сохранен!'
    else:
        form = RecipeAddForm()
        message = 'Заполните форму!'
    return render(request, 'recipeapp/add_recipe.html', context={'form': form, 'message': message})


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author.user == request.user:
        if request.method == 'POST':
            form = RecipeEditForm(request.POST, request.FILES, instance=recipe)
            if form.is_valid():
                form.save()
        else:
            form = RecipeEditForm(instance=recipe)
        return render(request, 'recipeapp/edit_recipe.html',
                      {'form': form, 'recipe': recipe, 'message': 'Рецепт изменен успешно!'})


@login_required
def show_all_my_recipe(request):
    clear_recipes = Recipe.objects.filter(author_id=request.user.id)
    logger.info(f'Запрос на вывод рецептов пользователя {request.user=} выполнен успешно!')
    return render(request, 'recipeapp/show_all_my_recipe.html', {'clear_recipes': clear_recipes, 'user': request.user})


# @login_required  # Декоратор, защиты доступа без логина
def show_five_recipe(request):  # Показать 5 рецептов
    my_ids = Recipe.objects.values_list('id', flat=True)
    my_ids = list(my_ids)
    n = 5
    rand_ids = sample(my_ids, n)
    random_recipe = Recipe.objects.filter(id__in=rand_ids)
    logger.info(f'Зпрос на вывод 5 рецептов успешно выполнен: {rand_ids=}')
    return render(request, 'recipeapp/show_five_recipe.html',
                  {'random_recipe': random_recipe, 'message': 'Пять случайных рецептов:'})


# @login_required  # Декоратор, защиты доступа без логина
def show_full_recipe(request, recipe_id):  # Показать полный рецепт
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    logger.info(f'Зпрос на вывод 1 рецепта с ID:{recipe_id=} успешно выполнен: {recipe=}')
    return render(request, 'recipeapp/show_full_recipe.html', {'recipe': recipe})
