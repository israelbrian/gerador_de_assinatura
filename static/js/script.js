const submitForm = document.getElementById('submitForm');
const divSignature = document.getElementById('divSignature');
const divImg = document.getElementById('divImg');
const imgAssPadrao = document.getElementById('imgAssPadrao');
const imgTitle = document.getElementById('imgTitle');

const url = '/api'
let imgUrlBlob = null

function downloadImage() {
    if (!imgUrlBlob) return

    const linkImg = document.createElement('a');
    linkImg.href = imgUrlBlob
    const nomeUsuario = document.getElementById('nomeUsuario').value
    const nomeArquivo = `${nomeUsuario}.png`;
    linkImg.download = `${nomeArquivo}`;
    divSignature.appendChild(linkImg);
    linkImg.click();
    divSignature.removeChild(linkImg);
    URL.revokeObjectURL(linkImg)
    document.getElementById('submitForm').reset()
}

function mostrarImg(imgUrl) {
    document.getElementById('btnManual').classList.remove('hidden');
    imgAssPadrao.src = imgUrl;
    imgAssPadrao.alt = 'assinatura_gerada';
    imgTitle.textContent = 'Assinatura gerada com sucesso!';
    divImg.appendChild(imgAssPadrao)

    const botaoAntigo = document.getElementById('btnDownload');
    if (botaoAntigo) {
        botaoAntigo.remove();
    }

    const botaoDownload = document.createElement('button');
    botaoDownload.id = 'btnDownload';
    botaoDownload.classList = 'bg-gray-900 text-white p-3 rounded-md my-4 hover:bg-slate-700'
    botaoDownload.textContent = 'Baixar Assinatura';
    botaoDownload.addEventListener('click', downloadImage);
    divSignature.appendChild(botaoDownload);
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

