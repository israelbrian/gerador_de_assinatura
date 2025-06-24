const submitForm = document.getElementById('submitForm');
const divImg = document.getElementById('divImg');
const div_img = document.getElementById('div-img');
const imgAssPadrao = document.getElementById('imgAssPadrao');
const imgTitle = document.getElementById('imgTitle');

const url = 'http://127.0.0.1/api'
let imgUrlBlob = null

function downloadImage() {
    if (!imgUrlBlob) return

    const linkImg = document.createElement('a');
    linkImg.href = imgUrlBlob
    const nomeUsuario = document.getElementById('nomeUsuario').value
    const nomeArquivo = `${nomeUsuario}.png`;
    linkImg.download = `${nomeArquivo}`;
    divImg.appendChild(linkImg);
    linkImg.click();
    divImg.removeChild(linkImg);
    URL.revokeObjectURL(linkImg)
    document.getElementById('submitForm').reset()
}

function mostrarImg(imgUrl) {
    imgAssPadrao.src = imgUrl;
    imgAssPadrao.alt = 'assinatura_gerada';
    imgTitle.textContent = 'Assinatura gerada com sucesso!';
    div_img.appendChild(imgAssPadrao)

    const botaoAntigo = document.getElementById('btnDownload');
    if (botaoAntigo) {
        botaoAntigo.remove();
    }

    const botaoDownload = document.createElement('button');
    botaoDownload.id = 'btnDownload';
    botaoDownload.classList = 'bg-gray-900 text-white p-3 rounded-md my-4 hover:bg-neutral-800'
    botaoDownload.textContent = 'Baixar Assinatura';
    botaoDownload.addEventListener('click', downloadImage);
    divImg.appendChild(botaoDownload);
}

submitForm.addEventListener('submit', async (e) => {
    e.preventDefault()
const dadosUsuario = {
    'nome': document.getElementById('nomeUsuario').value, 
    'cargo': document.getElementById('cargoUsuario').value,
    'telefone_fixo': document.getElementById('telFixoUsuario').value,
    'email': document.getElementById('emailUsuario').value,
    'orgao': document.getElementById('orgaoUsuario').value,
    'andar': document.getElementById('andarUsuario').value
}

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
        
    } catch (error) {
        console.error('Erro ao enviar os dados:', error);
    }
})

