from sqlalchemy import create_engine, select, text

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/birthdays")
conn = engine.connect()
result = conn.execute(text("SELECT * FROM persons;"))

