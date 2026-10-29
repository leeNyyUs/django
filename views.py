
from django.http import HttpResponse


users = {
    "Умида": "Возраст: 15 лет. Город: Ташкент.",
    "Рабия": "Возраст: 12 лет. Город: Самарканд.",
    "Алия": "Возраст: 8 лет. Город: Бухара.",
}


def home(request):
    return HttpResponse("Главная страница")


def users_list(request):
    result = "<h4>Список пользователей</h4><ul>"

    for username in users:
        result += f'<li><a href="/users/{username}/">{username}</a></li>'

    result += "</ul>"
    return HttpResponse(result)


def user_info(request, username):
    info = users.get(username)

    if info:
        return HttpResponse(f"<h1>{username}</h1><p>{info}</p>")

    return HttpResponse("Пользователь не найден")


def forum(request):
    return HttpResponse("Форум")


def contacts(request):
    return HttpResponse("Контакты")


def archive(request):
    return HttpResponse("Архив")
