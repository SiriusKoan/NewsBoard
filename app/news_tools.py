from os import getenv
from newsapi import NewsApiClient
from .db import db, Directories, Keywords

newsapi = NewsApiClient(api_key=getenv("NEWSAPIKEY"))


def get_directories(user_id):
    try:
        directories = Directories.query.filter_by(user_id=user_id).all()
        return [{"id": directory.ID, "name": directory.name, "keywords": [keyword.keyword for keyword in directory.keywords]} for directory in directories]
    except:
        return False


def create_directory(user_id, name):
    try:
        directory = Directories(user_id, name)
        db.session.add(directory)
        db.session.commit()
        return True
    except:
        return False


def update_directory():
    pass


def delete_directory():
    pass


def add_keyword(directory_id, keyword):
    if not Keywords.query.filter_by(directory_id=directory_id, keyword=keyword).all():
        db.session.add(Keywords(directory_id, keyword))
        db.session.commit()
        return True
    return False


def get_news(query, language):
    articles = newsapi.get_everything(q=query, language=language, sort_by="relevancy")
