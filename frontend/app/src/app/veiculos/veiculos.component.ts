import {Component, OnInit} from '@angular/core';
import {CommonModule} from "@angular/common";
import {HttpClientModule} from '@angular/common/http';
import {ApiService} from '../api.service';
import {Veiculo} from '../models/veiculo.model';
import {RouterModule} from "@angular/router";
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-veiculos',
  standalone: true,
  imports: [CommonModule, HttpClientModule, RouterModule, FormsModule],
  templateUrl: 'veiculos.component.html',
  styleUrl: 'veiculos.component.css'
})
export class VeiculosComponent implements OnInit {
  veiculos: any[] = [];
  filteredVeiculos: Veiculo[] = [];
  isLoading: boolean = true;

  // Search and filters
  searchTerm = '';
  selectedYear = '';
  selectedBrand = '';

  // Sorting
  sortColumn = 'marca';
  sortDirection: 'asc' | 'desc' = 'asc';

  // Pagination
  currentPage = 1;
  itemsPerPage = 10;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.loadVeiculos();
  }

  loadVeiculos(): void {
    this.isLoading = true;
    this.apiService.getVeiculos().subscribe({
      next: (veiculos) => {
        this.veiculos = veiculos;
        this.applyFilters();
        this.isLoading = false;
      },
      error: (err) => {
        console.error('Erro ao carregar veículos!:', err);
        this.isLoading = false;
      }
    });
  }

  get yearOptions(): number[] {
    const years = new Set<number>();
    this.veiculos.forEach(v => years.add(v.ano));
    return Array.from(years).sort((a, b) => b - a);
  }

  get brandOptions(): string[] {
    const brands = new Set<string>();
    this.veiculos.forEach(v => brands.add(v.marca));
    return Array.from(brands).sort();
  }

  applyFilters(): void {
    this.filteredVeiculos = this.veiculos.filter(veiculo => {
      const matchesSearch = !this.searchTerm ||
        Object.values(veiculo).some(val =>
          String(val).toLowerCase().includes(this.searchTerm.toLowerCase())
        );
      const matchesYear = !this.selectedYear || veiculo.ano === +this.selectedYear;
      const matchesBrand = !this.selectedBrand || veiculo.marca === this.selectedBrand;

      return matchesSearch && matchesYear && matchesBrand;
    });

    this.sortData();
    this.currentPage = 1;
  }

  sortData(): void {
    this.filteredVeiculos.sort((a, b) => {
      const valA = a[this.sortColumn as keyof Veiculo];
      const valB = b[this.sortColumn as keyof Veiculo];

      if (valA == null) return 1;
      if (valB == null) return -1;

      if (valA < valB) return this.sortDirection === 'asc' ? -1 : 1;
      if (valA > valB) return this.sortDirection === 'asc' ? 1 : -1;
      return 0;
    });
  }

  sort(column: string): void {
    if (this.sortColumn === column) {
      this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
      this.sortColumn = column;
      this.sortDirection = 'asc';
    }
    this.sortData();
  }

  addVeiculo(): void {
    // Implementar a lógica para adicionar um novo veículo
  }

  editVeiculo(veiculo: any): void {
    // Implementar a lógica para editar um veículo existente
  }

  deleteVeiculo(id: number): void {
    if (confirm('Quer mesmo deletar este veículo?')) {
      this.apiService.deleteVeiculo(id).subscribe({
        next: () => {
          this.veiculos = this.veiculos.filter(v => v.id !== id);
          this.applyFilters();
        },
        error: (err) => console.error('Error ao deletar veículo!:', err)
      });
    }
  }

  // Pagination methods
  get totalPages(): number {
    return Math.ceil(this.filteredVeiculos.length / this.itemsPerPage);
  }

  get paginatedVeiculos(): Veiculo[] {
    const start = (this.currentPage - 1) * this.itemsPerPage;
    return this.filteredVeiculos.slice(start, start + this.itemsPerPage);
  }

  getPages(): number[] {
    const pages = [];
    const maxVisiblePages = 5;
    let startPage = Math.max(1, this.currentPage - Math.floor(maxVisiblePages / 2));
    let endPage = startPage + maxVisiblePages - 1;

    if (endPage > this.totalPages) {
      endPage = this.totalPages;
      startPage = Math.max(1, endPage - maxVisiblePages + 1);
    }

    for (let i = startPage; i <= endPage; i++) {
      pages.push(i);
    }

    return pages;
  }

  prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
    }
  }

  nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
    }
  }

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
