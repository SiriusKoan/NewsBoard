from os import getenv
from multiprocessing import Pool
from datetime import datetime, timedelta
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


def add_directory(user_id, name):
    try:
        directory = Directories(user_id, name)
        db.session.add(directory)
        db.session.commit()
        return True
    except:
        return False


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
        news = dict()
        language = user.lang
        args = [(keyword.value, language) for keyword in directory.keywords]
        with Pool(8) as pool:
            results = pool.starmap(get_news, args)
            for i, keyword in enumerate(directory.keywords):
                news[keyword.value] = results[i]

        # for development
        # news = {
        #     "A": [
        #         {
        #             "url": "https://google.com",
        #             "urlToImage": "https://google.com",
        #             "title": "meow",
        #             "source": {"name": "author"},
        #         },
        #         {
        #             "url": "https://google.com",
        #             "urlToImage": "https://google.com",
        #             "title": "meow",
        #             "source": {"name": "author"},
        #         },
        #     ],
        #     "B": [
        #         {
        #             "url": "https://google.com",
        #             "urlToImage": "https://google.com",
        #             "title": "meow2",
        #             "source": {"name": "author"},
        #         }
        #     ],
        # }
        return {"name": directory_name, "id": directory.ID, "news": news}
    else:
        return False


def add_keyword(directory_id, value):
    # check illegal characters
    value = value.replace("_", " ")
    value = value.strip()
    # there cannot be two same keywords in one directory
    if not Keywords.query.filter_by(directory_id=directory_id, value=value).all():
        db.session.add(Keywords(directory_id, value))
        db.session.commit()
        return True
    return False


def delete_keyword(directory_id, value):
    keyword = Keywords.query.filter_by(directory_id=directory_id, value=value).first()
    if keyword:
        db.session.delete(keyword)
        db.session.commit()
        return True
    return False


def get_news(query, language="en"):
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    args = {
        "q": query,
        "language": language,
        "sort_by": "popularity",
        "from_param": yesterday,
        "to": today,
        "page_size": 7,
    }
    articles = newsapi.get_everything(**args)
    if articles["status"] == "ok":
        return articles["articles"]
    return False
