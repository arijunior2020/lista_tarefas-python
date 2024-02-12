from flask import request, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lista:lista123@172.18.0.2/lista_tarefa'
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Adicionando suporte para migrações

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

# Rota para criar uma nova tarefa
@app.route('/criar-tarefa', methods=['POST'])
def criar_tarefa():
    data = request.json
    nova_tarefa = Task(description=data['descricao'])

    try:
        db.session.add(nova_tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa criada com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro ao criar tarefa', 'details': str(e)}), 500

# Rota para excluir uma tarefa pelo ID
@app.route('/excluir-tarefa/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    tarefa = Task.query.get(id)

    if not tarefa:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    try:
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa excluída com sucesso!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro ao excluir tarefa', 'details': str(e)}), 500

# Rota para listar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = Task.query.all()
    return jsonify([(tarefa.id, tarefa.description) for tarefa in tarefas])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True, use_reloader=True)
