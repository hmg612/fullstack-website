import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))


def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_db = MONGO_CONN.blog_session_db.blog_db
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_db = MONGO_CONN.blog_session_db.blog_db
    return blog_db
