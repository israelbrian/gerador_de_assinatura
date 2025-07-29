const inputPhoneNumber = document.getElementById('phoneNumber');

inputPhoneNumber.addEventListener('input', (event) =>  {
  const target = event.target;

  // 1. Remove tudo que não for dígito.
  let value = target.value.replace(/\D/g, '');

  // 2. Limita o tamanho para 10 dígitos (telefone fixo com DDD).
  value = value.substring(0, 10);

  // 3. Aplica a máscara de forma progressiva.
  value = value.replace(/^(\d{2})(\d)/, '($1) $2'); // Adiciona parênteses e espaço após o DDD.
  value = value.replace(/(\d{4})(\d)/, '$1-$2');   // Adiciona o hífen.

  // 4. Atualiza o valor do campo.
  target.value = value;
});

