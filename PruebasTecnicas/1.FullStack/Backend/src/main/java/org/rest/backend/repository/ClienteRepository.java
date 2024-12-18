package org.rest.backend.repository;

import org.rest.backend.model.Cliente;

import java.util.Optional;

public interface ClienteRepository {
    Optional<Cliente> findByTipoDocumentoAndNumeroDocumento(String tipoDocumento, String numeroDocumento);
}
