const submitForm = document.getElementById('submitForm');
const divImg = document.getElementById('divImg');
const imgAssPadrao = document.getElementById('imgAssPadrao');
const imgTitle = document.getElementById('imgTitle');

const nomeUsuario = document.getElementById('nomeUsuario')
const cargoUsuario = document.getElementById('cargoUsuario')
const telFixoUsuario = document.getElementById('telFixoUsuario')
const emailUsuario = document.getElementById('emailUsuario')
const orgaoUsuario = document.getElementById('orgaoUsuario')
const andarUsuario = document.getElementById('andarUsuario')

const url = 'http://127.0.0.1:5000/api'
// console.log(dadosUsuario);

function mostrarData(imgUrl) {
    imgAssPadrao.src = imgUrl;
    imgAssPadrao.alt = 'assinatura_gerada';
    imgTitle.textContent = 'Assinatura gerada com sucesso!';
    divImg.appendChild(imgAssPadrao)

    // const imgUrl2 = imgUrl

    // downloadImage(imgUrl2); // Chama a função para baixar a imagem

    //logica de download da imagem
    // const linkImg = document.createElement('a');
    // linkImg.href = imgUrl;
    // linkImg.download = 'assinatura_gerada.png';
    // divImg.appendChild(linkImg);
    // linkImg.click();
    // divImg.removeChild(linkImg);
    // URL.revokeObjectURL(imgUrl)
}

// function downloadImage(imgUrl2) {
//     const linkImg = document.createElement('a');
//     linkImg.href = imgUrl2;
//     linkImg.download = 'assinatura_gerada.png';
//     divImg.appendChild(linkImg);
//     linkImg.click();
//     // divImg.removeChild(linkImg);
//     URL.revokeObjectURL(imgUrl2)
// }

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
        // função para baixar a imagem
        // function downloadImage(imgUrl) {
        // const linkImg = document.createElement('a');
        // linkImg.href = imgUrl2;
        // linkImg.download = 'assinatura_gerada.png';
        // divImg.appendChild(linkImg);
        // linkImg.click();
        // }
        // divImg.removeChild(linkImg);
        //  URL.revokeObjectURL(imgUrl2)
        console.log('Dados enviados com sucesso:', imgUrl, blob);
        // document.write(data)
        
    } catch (error) {
        console.error('Erro ao enviar os dados:', error);
        // console.log('Erro ao enviar os dados. Tente novamente mais tarde.');
    }
})