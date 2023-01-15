# Flask-RESTful-Exemplo
CRUD utilizando Python, MongoDB e a biblioteca Flask-RESTful

<li>
Precisa substituir username, password, host, port e database com os valores corretos para sua configuração.
</li>
<li>
E depois disso, você pode selecionar o banco de dados que deseja usar com o método client.database_name, e começar a trabalhar com as coleções.
</li>

<blockquote>Este exemplo cria uma classe Employee que herda de Resource e implementa os métodos GET, POST, PUT e DELETE para realizar operações CRUD na coleção employees do banco de dados MongoDB. A classe Api do Flask-RESTful é usada para adicionar a rota /employee/<string:id> e gerenciar as requisições HTTP.</blockquote>
