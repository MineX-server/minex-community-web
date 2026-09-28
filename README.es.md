# MineX Community Web

**Aloja la entrada de tu comunidad. Juega con todos en MineX.**

[English](README.md) · [Acceso al piloto](docs/pilot.md) · [Hoja de ruta](docs/roadmap.md) · [Pruebas en VPS](docs/vps-test-plan.md)

MineX Community Web es un proyecto para que las comunidades puedan alojar un cliente web en su dominio y conectar a sus jugadores a los mismos mundos de MineX, conservando su cuenta y jugando con los demás usuarios.

La comunidad aloja la experiencia web. MineX mantiene los servidores compartidos, las cuentas y los servicios sensibles.

> **Estado actual: planificación pública y una vista previa local de instalación.**
> Esta versión todavía no permite jugar desde una instalación comunitaria. El primer piloto conectado necesitará aprobación manual de MineX. El repositorio aún no contiene el cliente jugable ni un instalador para conectarse al juego.

## Un MineX, muchas webs comunitarias

Queremos que una comunidad pueda compartir su propia dirección, recibir a sus jugadores y llevarlos al MineX existente sin administrar otro mundo de juego.

La experiencia prevista:

1. El jugador entra en la web de la comunidad.
2. Pulsa **Continuar con MineX**.
3. Inicia sesión en una página oficial de cuenta y vuelve a la comunidad.
4. Su navegador conecta con el servicio compartido de MineX.
5. Juega con los demás jugadores y conserva su identidad y progreso.

Cuando una operación sensible requiere aprobación, el jugador la revisa en una página oficial de MineX. La web comunitaria no recibe autoridad para aprobarla por él.

Este recorrido describe el objetivo del proyecto. La integración conectada sigue pendiente de implementación y pruebas.

## Qué puedes usar ahora

| Componente | Estado |
| --- | --- |
| Arquitectura pública y hoja de ruta | Disponibles |
| Plantilla para solicitar el piloto | Disponible; la solicitud no concede acceso |
| Vista previa local de la web | Disponible, sin conexión a cuentas, juego o pagos |
| Comprobaciones del contenido y pruebas | Disponibles para ejecución local y GitHub Actions |
| Login y admisión de instalaciones comunitarias | Pendientes de implementación y verificación central |
| Distribución del cliente jugable | Pendiente de revisar artefactos y dependencias |
| Instalador del piloto conectado | Planificado |
| Alta automática de operadores | Fase futura, después del piloto manual |

## Prueba local, sin contratar una VPS

Para este paso no necesitas cuenta MineX, API key ni wallet.
Descarga el repositorio, abre una terminal en su carpeta y usa Python 3.10 o posterior:

```bash
python3 tools/check_public.py
python3 -m unittest discover -s tests -v
python3 tools/preview.py --port 8787
```

Abre **http://127.0.0.1:8787**. Para terminar, pulsa `Ctrl+C`.

Verás una página de prueba de instalación. No tiene formulario de acceso ni motor de juego.
Que funcione demuestra que arranca este pequeño servicio web; no demuestra todavía que puedas entrar en MineX desde una web comunitaria.

El [plan para VPS](docs/vps-test-plan.md) explica cómo repetirlo mediante SSH y qué falta para ensayar una conexión real.

## Primer piloto: aprobación manual

Cuando este repositorio esté publicado, abre una incidencia con la plantilla **Community pilot request**.
Indica el nombre público de tu comunidad, región, tamaño aproximado del grupo y, opcionalmente, su dominio.
No hace falta comprar una VPS para solicitar participar.

Un responsable revisará la solicitud. Cuando el piloto conectado esté listo, MineX verificará el dominio, asignará una identidad de instalación y sus límites, y habilitará el acceso desde el servicio central.

**Una incidencia, etiqueta, copia del repositorio o modificación local no activa una instalación.** La aprobación en GitHub no será una credencial para entrar.

Leer el repositorio y usar la vista previa local no requiere aprobación. La revisión manual se aplica al acceso de una instalación al MineX central.

## Qué aloja cada parte

| Comunidad | MineX |
| --- | --- |
| Dominio y alojamiento de la web | Mundos compartidos y admisión al juego |
| Launcher y futuros archivos de cliente revisados | Cuentas, personajes, permisos y progreso |
| Configuración pública de su instalación | Login oficial y aprobación de operaciones |
| Disponibilidad de su web | Servicios privados de wallet y autorización financiera |

El paquete futuro conectará al MineX existente. No incluye los componentes privados necesarios para montar una copia independiente de nuestro servidor.

La integración existente de MineX con Solana continúa en servicios oficiales. Este repositorio no distribuye una implementación de wallet ni autoridad sobre los fondos de los jugadores.

## Centralización y controles

Las webs pueden estar repartidas entre comunidades, países y proveedores. Las cuentas, mundos y autorizaciones continúan bajo los servicios centrales de MineX.

En el futuro podríamos retirar nuestra web jugable y mantener las páginas oficiales de cuenta, aprobación y conexión. No se ha programado ni implementado esa retirada en este repositorio.

El diseño asume que un operador puede modificar todo su frontend. Por eso el permiso para jugar se separa del permiso para aprobar una operación sensible.
Reconocer una IP, un dominio o un estado declarado por el cliente no demuestra autorización.
La ofuscación no sustituye las verificaciones del servidor.

Son requisitos de aceptación del piloto conectado, no funciones que ya implemente esta vista previa.

## Participar

Son útiles las traducciones, mejoras de documentación, accesibilidad, pruebas de instalación y problemas reproducibles de la vista previa.
Los cambios se revisan antes de publicarse. La revisión de código y la aprobación de operadores son procesos separados.

Consulta [cómo contribuir](CONTRIBUTING.md), [el proceso del piloto](docs/pilot.md) y [la hoja de ruta](docs/roadmap.md).
La documentación técnica de esta primera versión está en inglés para facilitar la colaboración internacional.

No publiques contraseñas, claves SSH, OTP, credenciales de API ni datos de recuperación de wallets en incidencias. Para informar de un problema sensible, consulta [SECURITY.md](SECURITY.md).

## Licencia

La documentación, vista previa y herramientas originales publicadas aquí usan la [licencia MIT](LICENSE).
La licencia no concede derechos sobre la marca MineX, acceso al servicio, componentes privados ni código o recursos de juego de terceros. Las futuras distribuciones de cliente documentarán sus componentes y licencias por separado.
