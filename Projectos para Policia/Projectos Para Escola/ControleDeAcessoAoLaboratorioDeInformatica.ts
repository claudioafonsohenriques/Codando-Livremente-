import 'Aluno'
interface Aluno {
    nome: string;
    matricula: number;
    horarioAcesso?: string;
  }
  
  function permitirAcesso(aluno: Aluno, horario: string): void {
    aluno.horarioAcesso = horario;
    console.log(`Acesso permitido ao aluno ${aluno.nome} no horário ${horario}`);
  }
  
  // Exemplo de uso
  const aluno1: Aluno = {
    nome: "Maria",
    matricula: 654321,
  };
  
  permitirAcesso(aluno1, "09:30 - 12:05");
  console.log(aluno1);
  