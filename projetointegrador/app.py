
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL,MySQLdb 
 
app = Flask(__name__)
        
app.secret_key = "caircocoders-ednalan"
        
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '97855818'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
      
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route("/search",methods=["POST","GET"])
def search():
    idade = request.form["idade"]
    idioma = request.form["idioma"]
    escolaridade = request.form["escolaridade"]
    dependentes = request.form["dependentes"]
    pcd = request.form["pcd"]
    genero = request.form["genero"]
    checkIda = request.form["checkIdade"]
    checkIdi = request.form["checkIdioma"]
    checkEsc = request.form["checkEscolaridade"]
    checkDep = request.form["checkDependentes"]
    checkPcd = request.form["checkPCD"]
    checkGen = request.form["checkGenero"]
    
    #Verificação dos ChecksBox
    idadeBus = ''
    idiomaBus = ''
    escolaridadeBus = ''
    generoBus = ''
    dependentesBus =''
    pcdBus =''
    if checkIda == 'Idade' :
        idadeBus = idade
    if checkIdi == 'Idioma':
        idiomaBus = idioma
    if checkEsc == 'Escolaridade':
        escolaridadeBus = escolaridade
    if checkGen == 'Genero':
        generoBus = genero
    if checkDep == 'Dependentes':
        dependentesBus = dependentes
    if checkPcd == 'PCD':
        pcdBus = pcd
    #Fazendo a busca no BD
    cursor = mysql.connection.cursor()
    query = "SELECT * from cdd WHERE data_nascimento LIKE '%{}%' AND idiomas LIKE '%{}%' AND nivel_escoladidade LIKE '%{}%' AND dependentes LIKE '%{}%' AND pcd LIKE '%{}%' AND genero LIKE '%{}%'".format(idadeBus,idiomaBus ,escolaridadeBus ,dependentesBus,pcdBus,generoBus)
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', cdd=result, numrows=numrows)})

if __name__ == "__main__":
    app.run(debug=True)