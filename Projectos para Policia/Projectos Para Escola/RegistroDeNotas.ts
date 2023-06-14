interface Nota {
    materia: string;
    valor: number;
  }
  
  function registrarNota(materia: string, valor: number): Nota {
    const nota: Nota = {
      materia: materia,
      valor: valor,
    };
    return nota;
  }
  
  // Exemplo de uso
  const nota1 = registrarNota("Matemática", 8.5);
  console.log(nota1);
  