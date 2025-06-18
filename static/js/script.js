const submitForm = document.getElementById('submitForm');
const divImg = document.getElementById('divImg');
const imgAssPadrao = document.getElementById('imgAssPadrao');
const imgTitle = document.getElementById('imgTitle');

// const nomeUsuario = document.getElementById('nomeUsuario')
// const cargoUsuario = document.getElementById('cargoUsuario')
// const telFixoUsuario = document.getElementById('telFixoUsuario')
// const emailUsuario = document.getElementById('emailUsuario')
// const orgaoUsuario = document.getElementById('orgaoUsuario')
// const andarUsuario = document.getElementById('andarUsuario')

const url = 'http://127.0.0.1:5000/api'
let imgUrlBlob = null
// console.log(dadosUsuario);

// submitForm.addEventListener('click', function() {
//     document.getElementById('submitForm').reset()
// }) 

// function limparForm() {
//     document.getElementById('submitForm').reset()
//     document.getElementById('nomeUsuario').value = ''
//     Criar alguma logica que limpe os campos do formulario :
// }

function downloadImage() {
    if (!imgUrlBlob) return

    const linkImg = document.createElement('a');
    linkImg.href = imgUrlBlob
    const nomeUsuario = document.getElementById('nomeUsuario').value
    // nomeUsuario.toLowerCase().replace(/ /g, '_');
    const nomeArquivo = `${nomeUsuario}.png`;
    linkImg.download = `${nomeArquivo}`;
    // linkImg.download = `{nomeUsuario}.png`;
    // Adiciona o link ao corpo do documento, clica nele, e depois remove
    divImg.appendChild(linkImg);
    linkImg.click();
    divImg.removeChild(linkImg);
    // URL.revokeObjectURL(imgUrl)
}

function mostrarImg(imgUrl) {
    imgAssPadrao.src = imgUrl;
    imgAssPadrao.alt = 'assinatura_gerada';
    imgTitle.textContent = 'Assinatura gerada com sucesso!';
    divImg.appendChild(imgAssPadrao)
    divImg.style.display = 'block'; // Garante que a div da imagem esteja visível

    // Primeiro, remove qualquer botão de download antigo que possa existir
    const botaoAntigo = document.getElementById('btnDownload');
    if (botaoAntigo) {
        botaoAntigo.remove();
    }

    const botaoDownload = document.createElement('button');
    botaoDownload.id = 'btnDownload'; // Damos um ID para encontrá-lo e removê-lo depois
    botaoDownload.classList = 'bg-black text-white p-3 rounded-md ml-3 mb-1 mt-1 hover:bg-white hover:text-black'
    botaoDownload.textContent = 'Baixar Assinatura';
    botaoDownload.addEventListener('click', downloadImage); // add event listener 'click' para o botão
    divImg.appendChild(botaoDownload); // Adiciona o botão de download à divImg, abaixo da img
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
        imgUrlBlob = URL.createObjectURL(blob);
        mostrarImg(imgUrl); 
        console.log('Dados enviados com sucesso:', imgUrl,);
        // document.write(data)
        
    } catch (error) {
        console.error('Erro ao enviar os dados:', error);
        // console.log('Erro ao enviar os dados. Tente novamente mais tarde.');
    }
})

