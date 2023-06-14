function calcularMedia(notas: number[]): number {
    const total = notas.reduce((acc, nota) => acc + nota, 0);
    const media = total / notas.length;
    return media;
  }
  
  const n1 = 20;
  const n2 = 15;
  const n3 = 17.5;
  const notas = [n1, n2, n3];
  const media = calcularMedia(notas);
  console.log(media);
  