const patterns = {
  fullName: /^[A-Za-zÀ-ú\s]{5,}$/,
  jobTitle: /^.{5,}$/,
  phoneNumber: /^\(\d{2}\)\s\d{4}-\d{4}$/,
  telephoneNumber: /^\(\d{2}\)\s\d{5}-\d{4}$/,
  // email: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/,
  email: /^[a-zA-Z.]+@saude\.mg\.gov\.br$/,
  department: /^.{5,}$/,
  adress: /^[A-Za-z0-9.,\-\sÀ-ú°\º\/\\\\]{5,}$/,
};

function handleInputError(input, message) {
  input.classList.add("error");
  if (!input.dataset.originalPlaceholder) {
    input.dataset.originalPlaceholder = input.placeholder;
  }
  input.placeholder = message;
  input.value = "";
}

function clearInputError(input) {
  input.classList.remove("error");
  input.placeholder = input.dataset.originalPlaceholder || "";
}

export function validateForm() {
  const formInputs = document.querySelectorAll("#submitForm input[name]");
  const errors = {};

  formInputs.forEach((input) => {
    const pattern = patterns[input.id];

    // Se o campo for opcional (telephoneNumber) e estiver vazio, pula a validação.
    if (input.id === 'telephoneNumber' && input.value.trim() === '') {
      return;
    }
    if (pattern && !pattern.test(input.value)) {
      errors[input.id] = `Valor inválido. Siga o ${input.placeholder}  `;
    }
  });

  formInputs.forEach((input) => {
    errors[input.id]
      ? handleInputError(input, errors[input.id])
      : clearInputError(input);
  });

  return Object.keys(errors).length === 0;
}
