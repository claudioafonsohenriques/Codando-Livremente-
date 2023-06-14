interface Evento {
    nome: string;
    data: string;
  }
  
  function adicionarEvento(nome: string, data: string): Evento {
    const evento: Evento = {
      nome: nome,
      data: data,
    };
    return evento;
  }
  
  // Exemplo de uso
  const evento1 = adicionarEvento("Apresentação de Teatro", "14/06/2023");
  console.log(evento1);
  