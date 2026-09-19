document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formularioContacto');
    const mensajeExito = document.getElementById('mensajeExito');
    const modalExito = document.getElementById('modalExito');

    
    function validarEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    
    function mostrarError(campo, mensaje) {
        const errorDiv = document.getElementById('error' + campo.charAt(0).toUpperCase() + campo.slice(1));
        const input = document.getElementById(campo);
        
        errorDiv.textContent = mensaje;
        errorDiv.style.display = 'block';
        input.classList.add('error');
    }

    
    function limpiarError(campo) {
        const errorDiv = document.getElementById('error' + campo.charAt(0).toUpperCase() + campo.slice(1));
        const input = document.getElementById(campo);
        
        errorDiv.style.display = 'none';
        input.classList.remove('error');
    }

   
    function mostrarMensajeExito(nombre) {
        mensajeExito.textContent = `Gracias por su contacto ${nombre}! En breve le estaré respondiendo.`;
        modalExito.style.display = 'flex';
    }

    function cerrarModal() {
        modalExito.style.display = 'none';
    }

   
    window.cerrarModal = cerrarModal;

    // Cerrar el modal
    modalExito.addEventListener('click', function(e) {
        if (e.target === modalExito) {
            cerrarModal();
        }
    });

    // Validacion
    function validarCampo(campo, nombreCampo) {
        const valor = document.getElementById(campo).value.trim();
        
        if (valor === '') {
            mostrarError(campo, `El ${nombreCampo} es requerido`);
            return false;
        }
        
        if (campo === 'correo' && !validarEmail(valor)) {
            mostrarError(campo, 'Por favor, ingrese un correo electrónico válido');
            return false;
        }
        
        limpiarError(campo);
        return true;
    }

    
    ['nombre', 'correo', 'asunto', 'mensaje'].forEach(campo => {
        const input = document.getElementById(campo);
        input.addEventListener('input', () => {
            if (input.value.trim() !== '') {
                validarCampo(campo, campo);
            }
        });
    });

   
    formulario.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const campos = {
            nombre: 'nombre',
            correo: 'correo electrónico',
            asunto: 'asunto',
            mensaje: 'mensaje'
        };

        let formularioValido = true;

        
        for (let [campo, nombreCampo] of Object.entries(campos)) {
            if (!validarCampo(campo, nombreCampo)) {
                formularioValido = false;
            }
        }

        if (formularioValido) {
            const nombre = document.getElementById('nombre').value;
            mostrarMensajeExito(nombre);
            
            // Resetear el form
            formulario.reset();
            
            
            ['nombre', 'correo', 'asunto', 'mensaje'].forEach(campo => {
                limpiarError(campo);
            });
        }
    });
}); 