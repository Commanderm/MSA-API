# task_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    description = data.get('description')
    if not description:
        return jsonify({'error': 'Task description is required'}), 400
    user_id = data.get('user_id')  # предполагаем, что user_id передается в запросе
    task = {'description': description, 'user_id': user_id}
    tasks.append(task)
    return jsonify({'message': 'Task created successfully'}), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Реализация получения информации о задаче с task_id
    return jsonify({'task_id': task_id, 'description': 'Task description'})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Реализация обновления задачи с task_id
    return jsonify({'message': 'Task updated'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Реализация удаления задачи с task_id
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True, port='5001',host='0.0.0.0')