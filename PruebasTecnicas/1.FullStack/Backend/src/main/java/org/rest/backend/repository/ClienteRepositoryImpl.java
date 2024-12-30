package org.rest.backend.repository;

import org.rest.backend.model.Cliente;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public class ClienteRepositoryImpl implements ClienteRepository {

    @Override
    public Optional<Cliente> findByTipoDocumentoAndNumeroDocumento(String tipoDocumento, String numeroDocumento) {
        if ("C".equals(tipoDocumento) && "23445322".equals(numeroDocumento)) {
            Cliente cliente = new Cliente(
                "Juan", 
                "Carlos", 
                "Pérez", 
                "González", 
                "1234567890", 
                "Calle Falsa 123", 
                "Bogotá"
            );
            return Optional.of(cliente);
        }
        return Optional.empty();
    }
}
