interface Tarefa {
    descricao: string;
    concluida: boolean;
  }
  
  function adicionarTarefa(descricao: string): Tarefa {
    const tarefa: Tarefa = {
      descricao: descricao,
      concluida: false,
    };
    return tarefa;
  }
  
  // Exemplo de uso
  const tarefa1 = adicionarTarefa("Claúdio Fazer exercícios de Matemática");
  console.log(tarefa1);
  