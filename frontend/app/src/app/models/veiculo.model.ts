export interface Veiculo {
  id: number;
  marca: string;
  nome: string;
  ano: number;
  descricao: string;
  vendido: boolean;
  created?: Date;
  updated?: Date;
}
