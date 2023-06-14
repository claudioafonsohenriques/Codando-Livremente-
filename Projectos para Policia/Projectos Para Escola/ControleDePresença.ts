interface Presenca {
    aluno: string;
    presente: boolean;
  }
  
  function marcarPresenca(aluno: string, presente: boolean): Presenca {
    const presenca: Presenca = {
      aluno: aluno,
      presente: presente,
    };
    return presenca;
  }
  
  // Exemplo de uso
  const presencaAluno1 = marcarPresenca("ClauddioAfonso Henriques", true);
  console.log(presencaAluno1);
  