document.getElementById('formCriarTarefa').addEventListener('submit', function(event) {
    event.preventDefault();
    const descricao = document.getElementById('descricao').value;
    fetch('/api/criar-tarefa', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ descricao: descricao }),
    })
    .then(response => {
        if (response.ok) {
            // Recarregar a lista de tarefas após adicionar uma nova
            carregarTarefas();
        } else {
            console.error('Erro ao criar tarefa:', response.statusText);
        }
    })
    .catch(error => console.error('Erro ao criar tarefa:', error));
});

// Listener para o botão de listar tarefas
document.getElementById('listarTarefasBtn').addEventListener('click', function() {
    carregarTarefas();
});

function carregarTarefas() {
    fetch('/api/tarefas')
        .then(response => response.json())
        .then(tarefas => {
            const listaTarefas = document.getElementById('tarefas');
            listaTarefas.innerHTML = ''; // Limpar a lista antes de adicionar as novas tarefas
            tarefas.forEach(tarefa => {
                const li = document.createElement('li');
                li.textContent = tarefa[1];
                
                // Botão para deletar tarefa
                const btnDeletar = document.createElement('button');
                btnDeletar.textContent = 'Deletar';
                btnDeletar.classList.add('delete-btn'); // Adiciona classe para estilização
                btnDeletar.addEventListener('click', function() {
                    deletarTarefa(tarefa[0]); // Passa o ID da tarefa para a função deletarTarefa
                });
                li.appendChild(btnDeletar);
                
                listaTarefas.appendChild(li);
            });
        })
        .catch(error => console.error('Erro ao buscar tarefas:', error));
}

function deletarTarefa(id) {
    fetch(`/api/excluir-tarefa/${id}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            // Recarregar a lista de tarefas após deletar
            carregarTarefas();
        } else {
            console.error('Erro ao excluir tarefa:', response.statusText);
        }
    })
    .catch(error => console.error('Erro ao excluir tarefa:', error));
}
