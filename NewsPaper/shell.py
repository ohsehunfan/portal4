from random import random

from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

first_user = User.objects.create_user(username='first', email='gekjrb@mail.ru', password='gorilla')
second_user = User.objects.create_user(username='second', email='eokn@mail.ru', password='sunny')

first = Author.objects.create(user = first_user)
second = Author.objects.create(user = second_user)

sport = Category.objects.create(name = "Спорт")
science = Category.objects.create(name = "Наука")
movies = Category.objects.create(name = "Фильмы")
nature = Category.objects.create(name = "Природа")

article1 = Post.objects.create(author = first, post_type = Post.article, title = "Статья")
article2 = Post.objects.create(author = first, post_type = Post.article, title = "Статья2")
news = Post.objects.create(author = second, post_type = Post.news, title = "Новость")

PostCategory.objects.create(post = article1, category_1 = science, category_2 = nature)
PostCategory.objects.create(post = article2, category_1 = nature, category_2 = science)
PostCategory.objects.create(post = news, category_1 = movies, category_2 = sport)
PostCategory.objects.create(post = news, category_1 = sport, category_2 = movies)

comment_1 = Comment.objects.create(post = article1, user = first, text = "Комментарий")
comment_2 = Comment.objects.create(post = article2, user = first, text = "Комментарий")
comment_3 = Comment.objects.create(post = news, user = second, text = "Комментарий")
comment_4 = Comment.objects.create(post = news, user = second, text = "Комментарий")

like = [article1,
        article2,
        news,
        comment_1,
        comment_2,
        comment_3,
        comment_4
]

for i in range(100):
        random_obj = random.choice(like)
        if i % 2:
            random_obj.like()
        else:
            random_obj.dislike()

rating_first = (sum([post.rating*3 for post in Post.objects.filter(author=first)])
                    + sum([comment.rating for comment in Comment.objects.filter(user=first.user)])
                    + sum([comment.rating for comment in Comment.objects.filter(post__author=first)]))
first.update_rating(rating_first)

rating_second = (sum([post.rating*3 for post in Post.objects.filter(author=second)])
                    + sum([comment.rating for comment in Comment.objects.filter(user=second.user)])
                    + sum([comment.rating for comment in Comment.objects.filter(post__author=second)]))
second.update_rating(rating_second)

best_author = Author.objects.all().order_by('-rating')[0]

print("Лучший автор")
print("username:", best_author.user.username)
print("Рейтинг:", best_author.rating)
print("")


best_article = Post.objects.filter(post_type=Post.article).order_by('-rating')[0]
print("Лучшая статья")
print("Дата:", best_article.created)
print("Автор:", best_article.author.user.username)
print("Рейтинг:", best_article.rating)
print("Заголовок:", best_article.title)
print("Превью:", best_article.preview())
print("")


print("Комментарии к ней")
for comment in Comment.objects.filter(post = best_article):
        print("Дата:", comment.created)
        print("Автор:", comment.user.username)
        print("Рейтинг:", comment.rating)
        print("Комментарий:", comment.text)
        print("")




