from db.run_sql import run_sql
from models.owner import Owner
from models.animal import Animal

def save(owner):
    sql = "INSERT INTO owners (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [owner.first_name, owner.last_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    owner.id = id
    return owner