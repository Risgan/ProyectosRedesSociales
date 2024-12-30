import { Routes } from '@angular/router';
import { IngresoPageComponent } from './pages/ingreso-page/ingreso-page.component';
import { ResumenPageComponent } from './pages/resumen-page/resumen-page.component';

export const routes: Routes = [
    { path: '', redirectTo: 'ingreso', pathMatch: 'full' },
    { path: 'ingreso', component: IngresoPageComponent }, 
    { path: 'resumen', component: ResumenPageComponent },
    { path: '**', redirectTo: 'ingreso' }
];
