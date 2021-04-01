from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB'] = 'minimarket'

mysql = MySQL(app)
@app.route('/')
def inicio():
    return 'La api funciona exitosamente'

@app.route('/categorias', methods=['GET','POST'])
def categorias():
    if request.method == 'GET':
        # hago una conexion con la base de datos
        cur = mysql.connection.cursor()
        # le digo que es lo que yo deseo
        cur.execute('SELECT * FROM T_CATEGORIAS')
        # el metodo fetchall() sirve para capturar todo el resultado, tambien existe el metodo fetchone() el cual devuelve la primera coincidencia del resultado
        data = cur.fetchall()
        # cierro la conexion y libero el tunnel
        cur.close()
        # print(data)
        resultado = []
        for row in data:
            categoria = {
                "cat_id":row[0],
                "cat_desc":row[1]
            }
            resultado.append(categoria)
        return jsonify({"ok":True,
        "content":resultado,
        "message": None})

    if request.method == 'POST':
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO T_CATEGORIAS (CAT_DESC) VALUES (%s)",(data['descripcion'],))
        # %s  esto significa poder pasar como parámetros a la base de datos.
        # sirve para guardar los cambios que estamos haciendo en la base de datos
        mysql.connection.commit()
        cur.close()
        return jsonify({
            'ok': True,
            'content':data,
            'message': 'Se agrego la categoria exitosamente'
        }), 201

@app.route('/productos', methods= ['GET','POST'])
def productos():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM T_PRODUCTOS")
        data = cur.fetchall()
        cur.close()
        resultado = []
        for row in data:
            resultado.append({
                'prod_id':row[0],
                'prod_desc':row[1],
                'prod_prec':float(row[2]),
                'cat_id': row[3]
            })
        return jsonify({
            'ok':True,
            'content':resultado,
            'message': None
        }), 200
    if request.method == 'POST':
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM T_CATEGORIAS WHERE CAT_ID = %s",(data['cat_id'],))
        resultado = cur.fetchone()
        if resultado:
            cur.execute("INSERT INTO T_PRODUCTOS (PROD_DESC, PROD_PREC, CAT_ID) VALUES (%s,%s,%s)",(data['prod_desc'],data['prod_prec'],data['cat_id'],))
            mysql.connection.commit()
            cur.close()
            return jsonify({
                'ok':True,
                'content':data,
                'message':'Se almaceno exitosamente el producto en la base de datos'
            }), 201
        else:
            cur.close()
            return jsonify({
                'ok':False,
                'content':'',
                'message':'La categoria no existe'
            }), 201
        
app.run(debug=True)