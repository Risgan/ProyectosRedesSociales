import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Cliente } from '../interface/cliente';

@Injectable({
  providedIn: 'root',
})
export class ClienteService {
  private baseUrl = 'http://localhost:8090'; 
  private cliente: Cliente | null = null; 

  constructor(private http: HttpClient) {}

  
  obtenerCliente(tipoDocumento: string, numeroDocumento: string): Observable<Cliente> {
    const url = `${this.baseUrl}/cliente?tipoDocumento=${tipoDocumento}&numeroDocumento=${numeroDocumento}`;
    return this.http.get<Cliente>(url);
  }

  
  guardarCliente(cliente: Cliente): void {
    this.cliente = cliente;
  }

  
  obtenerClienteGuardado(): Cliente | null {
    return this.cliente;
  }
}
