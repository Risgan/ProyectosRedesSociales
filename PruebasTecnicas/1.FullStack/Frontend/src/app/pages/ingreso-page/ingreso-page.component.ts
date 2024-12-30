import { Component } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ClienteService } from '../../services/cliente.service';

@Component({
  selector: 'app-ingreso-page',
  imports: [ReactiveFormsModule, FormsModule],
  templateUrl: './ingreso-page.component.html',
  styleUrl: './ingreso-page.component.scss'
})
export class IngresoPageComponent {

  tipoDocumento: string = '';
  numeroDocumento: string = '';
  botonActivo: boolean = false;

  constructor(
    private router: Router,
    private clienteService: ClienteService
  ) {}

  validarFormulario() {
    this.botonActivo =
      this.tipoDocumento.length > 0 &&
      this.numeroDocumento.length >= 10 &&
      this.numeroDocumento.length <= 13;
  }

  formatNumeroDocumento() {
    this.numeroDocumento = this.numeroDocumento.replace(/\D/g, '');
    this.numeroDocumento = new Intl.NumberFormat('es-CO').format(
      parseInt(this.numeroDocumento) || 0
    );
  }

  buscarCliente() {

    this.clienteService.obtenerCliente(this.tipoDocumento, this.numeroDocumento.replace(/\D/g, '')).subscribe(
      (cliente) => {
        this.clienteService.guardarCliente(cliente);
        this.router.navigate(['/resumen']);
      },
      (error) => {
        console.error(error);
        this.router.navigate(['/resumen']);

      }
    );
  }
}