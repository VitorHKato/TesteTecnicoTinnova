import { Routes } from '@angular/router';
import {VeiculosComponent} from "./veiculos/veiculos.component";

export const routes: Routes = [
    { path: 'veiculos', component: VeiculosComponent },
    { path: 'veiculos/novo', component: VeiculosComponent },
    { path: 'veiculos/editar/:id', component: VeiculosComponent },
    { path: '', redirectTo: '/veiculos', pathMatch: 'full' }
];
