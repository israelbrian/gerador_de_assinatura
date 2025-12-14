const capitalize = require("./utils");

describe("capitalize", () => {
  test("deve capitalizar a primeira letra de uma string minúscula", () => {
    expect(capitalize("israel")).toBe("Israel");
  });

  test("deve lidar com uma string toda em maiúsculas", () => {
    expect(capitalize("TESTE")).toBe("Teste");
  });

  test("deve retornar uma string vazia para entrada nula ou inválida", () => {
    expect(capitalize(null)).toBe("");
    expect(capitalize(123)).toBe("");
  });
});
