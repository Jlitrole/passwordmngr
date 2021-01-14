import psycopg2

def store_passwords(password, user_email, username, url, app_name):
  try:
      connection = connect()
      cursos - connection.cursor()
