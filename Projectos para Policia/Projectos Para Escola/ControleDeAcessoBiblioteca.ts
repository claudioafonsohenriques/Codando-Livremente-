import 'Aluno'
interface Aluno {
    nome: string;
    matricula: number;
    livroEmprestado?: string;
  }

  
  
  function emprestarLivro(aluno: Aluno, livro: string): void {
    aluno.livroEmprestado = livro;
    console.log(`Livro ${livro} emprestado para o aluno ${aluno.nome}`);
  }
  
  // Exemplo de uso
  const aluno1: Aluno = {
    nome: "Claúdio Afonso Henriques",
    matricula: 68630,
  };
  
  emprestarLivro(aluno1, "Tecnicas De Linguagens De Programação");
  console.log(aluno1);
  