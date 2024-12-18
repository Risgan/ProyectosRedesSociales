package org.rest.backend.service;

import org.rest.backend.model.Cliente;
import org.rest.backend.repository.ClienteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class ClienteServiceImpl implements ClienteService {

    @Autowired
    private ClienteRepository clienteRepository;

    @Override
    public Optional<Cliente> getCliente(String tipoDocumento, String numeroDocumento) {
        return clienteRepository.findByTipoDocumentoAndNumeroDocumento(tipoDocumento, numeroDocumento);
    }
}

