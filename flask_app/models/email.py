from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module

class User:
  def __init__(self,data):
    self.id = data['id']
    self.email = data['email']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def save(cls,data):
    query = "INSERT into users (email) VALUES (%(email)s);"
    return connectToMySQL('email_validation').query_db(query,data)

  @classmethod
  def get_one(cls, data):
    query = "SELECT * FROM users WHERE id=%(id)s"
    result = connectToMySQL('email_validation').query_db(query, data) # [{name: "blah"}]
    return cls(result[0])

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM users"
    result = connectToMySQL('email_validation').query_db(query)
    emails = []
    for row in result:
      emails.append(cls(row))
    return result

  @staticmethod
  def validate_user( user ):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # this is an object
    is_valid = True
    # test whether a field matches the pattern
    if not EMAIL_REGEX.match(user['email']): # if the REGEX oject that has been given the user inputed passcode does not compile, it is false.
      # flash("Invalid email address!")
      print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
      is_valid = False
    return is_valid