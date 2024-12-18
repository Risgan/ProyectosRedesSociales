package org.rest.backend.controller;

import org.rest.backend.model.Cliente;
import org.rest.backend.service.ClienteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Optional;

@RestController
public class ClienteController {

    @Autowired
    private ClienteService clienteService;

    @GetMapping("/cliente")
    public ResponseEntity<Object> getCliente(@RequestParam String tipoDocumento, @RequestParam String numeroDocumento) {
        // Verificación de parámetros
        if (tipoDocumento == null || numeroDocumento == null) {
            return new ResponseEntity<>("Tipo de documento y número de documento son obligatorios", HttpStatus.BAD_REQUEST);
        }

        if (!tipoDocumento.equals("C") && !tipoDocumento.equals("P")) {
            return new ResponseEntity<>("Tipo de documento inválido", HttpStatus.BAD_REQUEST);
        }

        try {
            // Buscar el cliente utilizando el servicio
            Optional<Cliente> clienteOptional = clienteService.getCliente(tipoDocumento, numeroDocumento);
            if (clienteOptional.isPresent()) {
                return new ResponseEntity<>(clienteOptional.get(), HttpStatus.OK);
            } else {
                return new ResponseEntity<>("Cliente no encontrado", HttpStatus.NOT_FOUND);
            }
        } catch (Exception e) {
            return new ResponseEntity<>("Error interno del servidor", HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}

