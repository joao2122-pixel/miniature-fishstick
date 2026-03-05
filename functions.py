from service import connect

def insert_product(name, category, price, quantity = 1, provider = None): #CREATE
    with connect().cursor() as cursor:
        cursor.execute("""
        INSERT INTO products (name, category, price, quantity, provider)
        VALUES (%s, %s, %s, %s, %s)
        """, (name, category, price, quantity, provider))

def list_products(): #READ
    with connect().cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

def update_product(id, name,  category, price, quantity, provider): #UPDATE
    with connect().cursor() as cursor:
        cursor.execute(" UPDATE products SET name = %s, category = %s, price = %s, quantity = %s, provider = %s WHERE id = %s", (name, category, price, quantity, provider, id))
    return cursor.fetchall()

def delete_products(id): #DELETE
   with connect().cursor() as cursor: 
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))