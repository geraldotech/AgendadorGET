let tasks = []

async function loadTasks() {
  try {
    const response = await fetch('../install_windows/db/config.json')
    tasks = await response.json()

    renderTable()
  } catch (error) {
    console.error('Erro ao carregar JSON', error)
  }
}

function renderTable() {
  const tbody = document.querySelector('#taskTable tbody')
  tbody.innerHTML = ''

  tasks.tasks.forEach((task, index) => {
    const row = document.createElement('tr')
    row.innerHTML = `
              <td>${task.description}</td>
              <td><input type="text" value="${task.url}" onchange="editTask(${index}, 'url', this.value)"></td>
              <td><input type="time" value="${task.hora}" onchange="editTask(${index}, 'hora', this.value)"></td>
              <td>
                  <input type="checkbox"  id="${index}" ${task.status ? 'checked' : ''} 
                         onchange="editTask(${index}, 'status', this.checked)">
                  <label for="${index}">Alterar</label>
              </td>
              <td>
                  <button onclick="deleteTask(${index})">Excluir</button>
              </td>
              <td>
                  <button onclick="runTask('${task.url}')">Run now</button>
              </td>
          `
    tbody.appendChild(row)
  })
}

function editTask(index, field, value) {
  if (field === 'status') {
    tasks.tasks[index][field] = value === 'true' || value === true
  } else {
    tasks.tasks[index][field] = value
  }
  saveTasks()
}

function deleteTask(index) {
  if (confirm('Deletar esse agendamento?')) {
    tasks.tasks.splice(index, 1)
    saveTasks()
  }
}

function addTask() {
  const url = document.getElementById('newUrl').value.trim()
  const hora = document.getElementById('newHora').value
  const description = document.getElementById('newDescription').value.trim()

  if (url && hora && description) {
    tasks.tasks.push({ description, url, hora, status: true }) // Novo status padrão: true
    saveTasks()
    document.getElementById('newUrl').value = ''
    document.getElementById('newHora').value = ''
    document.getElementById('newDescription').value = ''
  } else {
    alert('Preencha todos os campos!')
  }
}

/* REENVIA OS DADOS */
async function saveTasks() {
  try {
    await fetch('save.php', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(tasks),
    })
    renderTable()
  } catch (error) {
    console.error('Erro ao salvar JSON', error)
  }
}

function openModal() {}

const dialogbox = document.querySelector('#dialogbox')
const dialog_open = document.querySelector('#open_modal')
const dialog_close = document.querySelector('#dialog_close')

dialog_open.onclick = function () {
  dialogbox.showModal()
}
dialog_close.onclick = function () {
  dialogbox.close()
}

loadTasks()

/* === MAKE FETCH REQUEST ===
PODERIA FAZER USANDO O PROPRIO JAVASCRIPT PORÉM PARA FAZER LOGS VAMOS CHAMAR UM ENDPOINT FEITO EM PHP
*/

function runTask(urlToSend) {
  fetch('get.php', {
    method: 'POST', // Define o método como POST
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({ url: urlToSend }), // Envia a URL como parâmetro
  })
    .then((req) => req.json())
    .then((res) => console.log(res))
    .catch((err) => console.error('Erro:', err))
}

// Exemplo de uso
//make_fetch('http://127.0.0.1:8080/PHP/General/Filesystem/CREATE/cretate_file_put_contents.php')
