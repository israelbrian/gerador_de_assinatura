const submitForm = document.getElementById('submitForm');
const divImg = document.getElementById('divImg');

const nomeUsuario = document.getElementById('nomeUsuario')
const cargoUsuario = document.getElementById('cargoUsuario')
const telFixoUsuario = document.getElementById('telFixoUsuario')
const emailUsuario = document.getElementById('emailUsuario')
const orgaoUsuario = document.getElementById('orgaoUsuario')
const andarUsuario = document.getElementById('andarUsuario')

const url = 'http://127.0.0.1:5000/api'
// console.log(dadosUsuario);

function mostrarData(imgUrl) {
    divImg.innerHTML = '' // Limpa o conteúdo anterior
    const dataImg = document.createElement('img');
    // dataImg.src = `data:image/png;base64,${imgUrl}`;
    dataImg.src = imgUrl;
    dataImg.alt = 'assinatura_gerada';
    divImg.appendChild(dataImg)
}

submitForm.addEventListener('submit', async (e) => {
    e.preventDefault()
    // dados dos usuários
const dadosUsuario = {
    'nome': document.getElementById('nomeUsuario').value, 
    'cargo': document.getElementById('cargoUsuario').value,
    'telefone_fixo': document.getElementById('telFixoUsuario').value,
    'email': document.getElementById('emailUsuario').value,
    'orgao': document.getElementById('orgaoUsuario').value,
    'andar': document.getElementById('andarUsuario').value
}

    // if (!nomeUsuario || !cargoUsuario || !telFixoUsuario || !emailUsuario || !orgaoUsuario || !andarUsuario) {
    //     alert('Preencha todos os campos!');
    //     return;
    // }
    // Envia a mensagem via POST para a API
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(dadosUsuario)
        })

        const blob = await response.blob();
        const imgUrl = URL.createObjectURL(blob);
        mostrarData(imgUrl); 
        console.log('Dados enviados com sucesso:', imgUrl);
        // document.write(data)
        
    } catch (error) {
        console.error('Erro ao enviar os dados:', error);
        // console.log('Erro ao enviar os dados. Tente novamente mais tarde.');
    }
})