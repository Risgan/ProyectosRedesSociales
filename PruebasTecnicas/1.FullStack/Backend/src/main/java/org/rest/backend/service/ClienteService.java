package org.rest.backend.service;

import org.rest.backend.model.Cliente;

import java.util.Optional;

public interface ClienteService {
    Optional<Cliente> getCliente(String tipoDocumento, String numeroDocumento);
}
