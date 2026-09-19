

const datosIniciales = {
    nombre: "Mario",
    apellido: "Santos",
    fechaNacimiento: "1990-01-01"
};


function mostrarMensajeBienvenida(datos) {
    const mensajeBienvenida = document.getElementById('mensajeBienvenida');
    mensajeBienvenida.textContent = `¡Bienvenido/a ${datos.nombre} ${datos.apellido}!`;
}


function calcularDiasVividos(fechaNacimiento) {
    const fechaNac = new Date(fechaNacimiento);
    const hoy = new Date();
    const diferencia = hoy - fechaNac;
    return Math.floor(diferencia / (1000 * 60 * 60 * 24));
}


function mostrarDiasVividos(dias) {
    const mensajeDias = document.getElementById('mensajeDias');
    mensajeDias.textContent = `Has vivido aproximadamente ${dias} días desde tu nacimiento.`;
}


document.addEventListener('DOMContentLoaded', () => {
    mostrarMensajeBienvenida(datosIniciales);
});


document.getElementById('formularioDatos').addEventListener('submit', (e) => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const fechaNacimiento = document.getElementById('fechaNacimiento').value;

    const datosUsuario = {
        nombre,
        apellido,
        fechaNacimiento
    };

    mostrarMensajeBienvenida(datosUsuario);
    const diasVividos = calcularDiasVividos(fechaNacimiento);
    mostrarDiasVividos(diasVividos);
}); 