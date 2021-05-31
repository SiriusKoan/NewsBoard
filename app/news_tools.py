from os import getenv
from datetime import datetime
from newsapi import NewsApiClient
from .db import db, Users, Directories, Keywords

newsapi = NewsApiClient(api_key=getenv("NEWSAPIKEY"))


def get_directories(user_id):
    try:
        directories = Directories.query.filter_by(user_id=user_id).all()
        return [
            {
                "id": directory.ID,
                "name": directory.name,
                "keywords": [keyword.value for keyword in directory.keywords],
            }
            for directory in directories
        ]
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


def delete_directory(directory_id):
    if directory := Directories.query.filter_by(ID=directory_id).first():
        keywords = Keywords.query.filter_by(directory_id=directory_id).all()
        for keyword in keywords:
            db.session.delete(keyword)
        db.session.delete(directory)
        db.session.commit()
        return True
    else:
        return False


def render_directory(user_id, directory_name):
    if directory := Directories.query.filter_by(
        user_id=user_id, name=directory_name
    ).first():
        user = Users.query.filter_by(ID=user_id).first()
        language = user.lang
        news = dict()
        for keyword in directory.keywords:
            news[keyword.value] = get_news(keyword.value, language)
        return {"name": directory_name, "news": news}
    else:
        return False


def add_keyword(directory_id, keyword):
    if not Keywords.query.filter_by(directory_id=directory_id, value=keyword).all():
        db.session.add(Keywords(directory_id, keyword))
        db.session.commit()
        return True
    return False


def get_news(query, language):
    today = datetime.now().strftime("%Y-%m-%d")
    articles = newsapi.get_everything(
        q=query,
        language=language,
        sort_by="popularity",
        from_param=today,
        to=today,
    )
    if articles["status"] == "ok":
        return articles["articles"][:7]
    return False
