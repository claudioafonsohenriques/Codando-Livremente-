import 'Aluno'
interface Aluno {
    nome: string;
    matricula: number;
    mensalidadePaga: boolean;
  }
  
  function registrarPagamento(aluno: Aluno): void {
    aluno.mensalidadePaga = true;
    console.log(`Pagamento registrado para o aluno ${aluno.nome}`);
  }
  
  // Exemplo de uso
  const aluno1: Aluno = {
    nome: "Pedro",
    matricula: 987654,
    mensalidadePaga: false,
  };
  
  registrarPagamento(aluno1);
  console.log(aluno1);
  