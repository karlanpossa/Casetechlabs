#Case Back-End: Desenvolvimento da lógica de negócios

from flask import Flask, request, jsonify

app = Flask(__name__)

#1. BANCO DE DADOS
gestaopessoas = [] #a listagem vazia está sendo utilizada para armazenar os dados das pessoas/clientes cadastradas em memória enquanto o Flask estiver em execução.

class Funcionario:
        def __init__(self, nome, data_nascimento, cpf, estado_civil, endereço):
            self.nome = nome
            self.data_nascimento = data_nascimento
            self.cpf = cpf
            self.estado_civil = estado_civil
            self.endereço = endereço
        
        
#2. ENDPOINTS
@app.route('/cadastro', methods=['POST'])
def cadastro_fun():
    dados_fun = request.get_json()
    novo_cadastro = Funcionario(dados_fun['nome'], dados_fun['data_nascimento'], dados_fun['cpf'], dados_fun['estado_civil'], dados_fun['endereço'])
    gestaopessoas.append(novo_cadastro) #adicionando o novo cadastro no banco de dados com a função append
    return jsonify({'message': 'Cadastro concluído com sucesso!'})

@app.route('/leitura', methods=['GET'])
def listagem_fun():
    ordem_alfabetica = sorted(gestaopessoas, key=lambda Funcionario: Funcionario['nome'])
    return jsonify(gestaopessoas) #fazendo uma busca pelo comando "GET" e resultando na listagem de todos os funcionários cadastrados armazenados no banco de dados

@app.route('/atualização/<cpf>', methods=['PUT']) #definindo a atualização/pesquisa do funcionário a partir do CPF, mas poderia ser um ID, matrícula, etc.
def atualização_fun(cpf):
    dados_fun = request.get_json()
    for Funcionario in gestaopessoas #looping 
        if Funcionario['cpf'] == cpf:
            Funcionario['nome'] = dados_fun['nome']   
            Funcionario['data_nascimento'] = dados_fun['data_nascimento']
            Funcionario['estado_civil'] = dados_fun['estado_civil']
            Funcionario['endereço'] = dados_fun['endereço']
            return jsonify ({'message': 'Atualização concluída com sucesso!'})
        return jsonify (['error': 'Funcionário não encontrado!'])
    
@app.route('/excluir/<cpf>', methods=['DELETE'])
def excluir_fun(cpf):
    dados_fun = request.get_json()
    for Funcionario in gestaopessoas
    if Funcionario['cpf'] == cpf:
        gestaopessoas.remove(Funcionario)
        return jsonify ({'message': 'Exclusão concluída com sucesso!'})
    return jsonify (['error': 'Funcionário não encontrado!'])
    
    
#3. RUN API
app.run(host='localhost') #por padrão: port 5000