import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ClienteService } from '../../services/cliente.service';
import { Cliente } from '../../interface/cliente';

@Component({
  selector: 'app-resumen-page',
  imports: [],
  templateUrl: './resumen-page.component.html',
  styleUrl: './resumen-page.component.scss'
})
export class ResumenPageComponent implements OnInit {
  cliente!: Cliente;

  constructor(
    private router: Router,
    private clienteService: ClienteService
  ) {}

  ngOnInit() {
   this.cliente = this.clienteService.obtenerClienteGuardado()!;
  }

  volver() {
    this.router.navigate(['/']);
  }
}