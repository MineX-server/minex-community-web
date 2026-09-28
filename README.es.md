# MineX Community Web

**Creando webs comunitarias de código abierto para un único MineX compartido.**

[English](README.md) · [Resumen del proyecto](docs/project-brief.md) · [Hoja de ruta](docs/roadmap.md)

La idea es sencilla: una comunidad instala la web de MineX en su VPS o dominio. Los jugadores entran en esa web, inician sesión mediante MineX y llegan a los mismos mundos que todos los demás. Su cuenta, personaje y progreso siguen en MineX.

Piensa en cada VPS como otra **puerta de entrada** al mismo juego en la nube. Aloja la web; no crea otro mundo de MineX ni funciona como un nodo de blockchain.

*Un mundo compartido debería ser más grande que cualquiera de las webs que lo abren.*

> **Qué funciona hoy:** este repositorio incluye una vista previa de instalación de código abierto, documentación y pruebas. Puedes ejecutar la vista previa en un ordenador o una VPS. **Todavía no abre el juego.** El cliente jugable y la conexión con MineX son trabajo pendiente; las primeras instalaciones conectadas necesitarán aprobación manual.

## Cómo debería funcionar

1. Una comunidad instala el futuro paquete web en su VPS.
2. Un jugador entra en la web de esa comunidad.
3. Inicia sesión en una página oficial de MineX.
4. Su navegador entra en el MineX compartido, con los mismos mundos y jugadores.

MineX mantiene el juego, las cuentas y los servicios sensibles. La web de una comunidad puede recibir jugadores, pero no aprobar operaciones de cuenta o wallet por ellos.

## ¿Por qué muchas puertas?

El objetivo es que cualquiera pueda alojar una puerta en su propia VPS, sin depender de que MineX mantenga todas las webs. Las comunidades de distintos países pueden elegir dónde alojar la suya.

Si una web cierra o deja de estar disponible en una región, un jugador debería poder entrar por otra, siempre que el servicio compartido de MineX sea accesible. Encontraría la misma cuenta, personaje, progreso y acceso a su wallet de MineX. Un jugador existente no tendría que registrarse de nuevo en cada web; un jugador nuevo crearía una sola cuenta MineX mediante el acceso oficial.

Así dependemos menos de una única web y las comunidades pueden ayudar de verdad a mantener MineX accesible. Esto no hace que el juego compartido sea independiente de los servidores de MineX. La idea es dar más resistencia a la puerta de entrada mientras todos siguen jugando juntos.

## Prueba lo que ya existe

Necesitas Git y Python 3.10 o posterior. Esto inicia una **página de prueba**, no el juego:

```bash
git clone https://github.com/MineX-server/minex-community-web.git
cd minex-community-web
python3 tools/preview.py --port 8787
```

Abre <http://127.0.0.1:8787> en ese ordenador. Para detener la vista previa, pulsa `Ctrl+C`.

Para comprobar el paquete:

```bash
python3 tools/check_public.py
python3 -m unittest discover -s tests -v
```

Si usas una VPS mediante SSH, sigue el [plan de pruebas en VPS](docs/vps-test-plan.md). La vista previa no pide contraseña de MineX, wallet ni clave de API.

## Qué falta

| Ahora | Objetivo |
| --- | --- |
| Vista previa pública, pruebas y plan de instalación | Paquete jugable para el navegador, revisado |
| [Solicitudes de comunidades interesadas](https://github.com/MineX-server/minex-community-web/issues/new?template=pilot-request.yml) | Instalaciones aprobadas y conectadas a MineX |
| MineX opera el juego compartido | Jugadores entrando desde muchas webs comunitarias |

La [hoja de ruta](docs/roadmap.md) muestra qué debemos construir y probar antes de poder decir «instálalo y juega». [@MineX-server](https://github.com/MineX-server) es el primer operador interesado registrado. Puedes [añadir tu comunidad a la lista](https://github.com/MineX-server/minex-community-web/issues/new?template=pilot-request.yml); una solicitud no activa por sí sola un servidor. Consulta el [proceso del piloto](docs/pilot.md).

## ¿Por qué código abierto y Solana?

Queremos que la **capa de alojamiento web** sea reutilizable para que comunidades de distintos lugares ayuden a entrar en el mismo MineX y su economía conectada con Solana. La wallet del jugador sigue vinculada a su cuenta MineX, no a la web comunitaria que visita. Este repositorio no publica una wallet, una API privada ni un sistema de aprobación financiera. No es una propuesta de token ni de play-to-earn.

Las webs pueden repartirse entre VPS independientes. Los mundos y las cuentas siguen bajo MineX: hablamos de **alojamiento web distribuido**, no de un juego totalmente descentralizado. El [resumen del proyecto](docs/project-brief.md) separa lo que ya es público de los próximos hitos.

## Participa y consulta los detalles

Empieza por [CONTRIBUTING.md](CONTRIBUTING.md). Consulta la [arquitectura](docs/architecture.md), las [pruebas](docs/testing.md) y la [notificación de problemas de seguridad](SECURITY.md). Nunca publiques contraseñas, OTP, claves SSH ni datos de recuperación de wallets en una incidencia.

Los archivos originales de este repositorio usan la [licencia MIT](LICENSE). La licencia no concede derechos sobre la marca MineX, servicios privados ni código o recursos de juego de terceros. Un futuro cliente jugable necesitará su propia revisión de dependencias y distribución.
