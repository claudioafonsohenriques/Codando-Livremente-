interface Aluno {
    nome: string;
    idade: number;
    turma: string;
  }
  
  function cadastrarAluno(nome: string, idade: number,Sexo: string, turma: string, Matricula: number, contacto: number): Aluno {
    const aluno: Aluno = {
      nome: nome,
      idade: idade,
      turma: turma,
    };
    return aluno;
  }
  
  // Exemplo de uso
  const aluno1 = cadastrarAluno("Claúdio Afonso Henriques", 17, "Masculino" , "II11A", 68630, 935358417 );
  console.log(aluno1);
  