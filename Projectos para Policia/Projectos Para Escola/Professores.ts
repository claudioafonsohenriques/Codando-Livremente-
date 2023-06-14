interface Professor {
    nome: string;
    disciplina: string;
  }
  
  function cadastrarProfessor(nome: string, disciplina: string): Professor {
    const professor: Professor = {
      nome: nome,
      disciplina: disciplina,
    };
    return professor;
  }
  
 
  const professor1 = cadastrarProfessor("Maria", "Matemática");
  console.log(professor1);
  