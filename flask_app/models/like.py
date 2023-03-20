from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Likes:
    db_name = "bright_ideas"

    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.idea_id = data['idea_id']

    @classmethod
    def like_idea(cls, data):
        query = "INSERT INTO bright_ideas.likes (user_id, idea_id) VALUES (%(user_id)s, %(id)s);"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results  
        
    @classmethod
    def remove_like(cls, data):
        query = "DELETE FROM bright_ideas.likes WHERE user_id = %(user_id)s AND idea_id = %(idea_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results