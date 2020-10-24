**Peticiones HTTP**

* *GET*
Solicita una representación del recurso especificado. Las peticiones deberán solo recuperar datos.

* *HEAD*
El servidor responde con líneas y headers, pero no con el body de la respuesta.
* *POST*
Cuando se requiere enviar información al servidor como, por ejemplo, un archivo de actualización, información de formulario, etc. Se usa cuando se necesita enviar una entidad para algún recurso determinado.
* *PUT*
Solicita que el servidor almacene el cuerpo de la entidad en una ubicación específica dada por el URL.
* *DELETE*
Es utilizado para solicitar al servidor que elimine un archivo en una ubicación específica dada por la URL. Es decir, este método elimina un recurso determinado.
* *CONNECT*
Es usado por el cliente para establecer una conexión de red con un servidor web mediante HTTP misma que se establece en forma de un túnel.
* *OPTIONS*
Representa una solicitud de información acerca de las opciones de comunicación disponibles en el canal de solicitud/respuesta identificada por el Request-URI. Describe las opciones de comunicación existentes de un recurso destino
* *TRACE*
Se utiliza para realizar pruebas de eco (de retornos) de mensajes en el camino que existe hacia un recurso determinado. Muy utilizado para la depuración y el desarrollo.
* *PATCH*
Utilizado para aplicar modificaciones parciales a un recurso

**Códigos de respuesta HTTP**
Es el mensaje que envía el servidor al cliente tras haber recibido una petición o HTTP request. 

**Respuestas informativas (100–199)**
* *100* **continue**
respuesta provisional indica que todo hasta ahora está bien y que el cliente debe continuar con la solicitud o ignorarla si ya está terminada.
* *101* **Switching protocol**  Indica que el servidor acepta el cambio de protocolo propuesto por el agente de usuario.
* *102* **Processing** El servidor ha recibido la solicitud y aún se encuentra procesandola

**Respuestas satisfactorias (200–299)**
* *200* **OK** Solicitud exitosa
* *201* **created** Solictiud exitosa y nuevo recurso como consecuencia
* *202* **accepted** Solicitud recibida, pero no actuado. Es una petición "sin compromiso", no hay manera en HTTP que permite enviar una respuesta asíncrona para el resultado  de la solicitud
* *203* **Non-Authoritative Information**  Exito, pero contenido no se ha obtenido de la fuente originalmente solicitada, sino que se recoge de una copia local o de un tercero
* *204* **No content**  La petición se ha completado con éxito pero su respuesta no tiene ningún contenido, aunque los encabezados pueden ser útiles.
* *205* **Reset content** Petición exitosa, pero respuesta no tiene contenidos y además, el agente de usuario tiene que inicializar la página donde realizó la petición.
* *206* **Partial content**  La petición servirá parcialmente el contenido solicitado. Ej (carga de descargas interrumpidas)

**Redirecciones (300–399)**
* *300* **Multiple choice** Solicitud tiene más de una posible respuesta. 
* *301* **Moved permanently** la URI  del recurso solicitado ha sido cambiado
* *302* **Found**  la URI solicitada ha sido cambiado temporalmente
* *303* **See other** Dirige al cliente a un nuevo recurso solicitado a otra dirección usando una petición GET.
* *304* **Not modified** Respuesta no modificada. El cliente puede continuar usando la misma versión almacenada en su caché.


**Errores de los clientes (400–499)**
* *400* **Bad request** El servidor no pudo interpretar la solicitud dada una sintaxis inválida.
* *401* **Unauthorized** Es necesario autenticar para obtener la respuesta solicitada
* *402* **Payment required** Utilizado en sistemas digitales de pagos. No está siendo usado actualmente.
* *403* **Forbidden** El servidor está rechazando otorgar una respuesta apropiada, a pesar de que el cliente dispone de los permisos
* *404* **Not Found** El servidor no pudo encontrar el contenido solicitado
* *405* **Method not allowed** Método solicitado conocido por el servidor pero ha sido deshabilitado.
* *408* **Request Timeout** El servidor quiere desconectar unaa conexión sin usar. 
* *451* **Unavailable for legal reasons** El usuario solicita un recurso ilegal, como alguna página web censurada por algún gobierno.

**Errores de los servidores (500–599)**.
* *500* **Internal Server Error** El servidor ha encontrado una situación que no sabe cómo manejarla.
* *501* **Not implemented** método solicitado no está soportado por el servidor y no puede ser manejado
* *502* **Bad Getaway** Mientras trabaja como una puerta de enlace para obtener una respuesta para la petición, esta fue inválida.
* *503* **Service unavailable** El servidor no está listo para manejar la petición (mantenimiento o sobrecarga)
* *504* **Gateway Timeout** Cuando el servidor está actuando como una puerta de enlace y no puede obtener una respuesta a tiempo
* *505* **HTTP Version Not Supported** La versión de HTTP usada para la petición no es soportada.
* *507* **Insufficient storage** Error de configuración interna. La varaible manejada no es adecuada para finalizar el proceso de negociación.



Referencias:

* **Google Cloud: Google Talent Solution**. *Códigos de respuesta HTTP* Tomado de (24/10/20):  https://cloud.google.com/talent-solution/job-search/docs/http-response-codes?hl=es-419
* **MDN web docs**. *Códigos de estado de respuesta HTTP*. Tomado de (24/10/20): https://developer.mozilla.org/es/docs/Web/HTTP/Status
* **MDN web docs**. *Métodos de petición HTTP*. Tomado de (24/10/20): https://developer.mozilla.org/es/docs/Web/HTTP/Methods
* **Yo soy dev**. *Peticiones HTTP ( GET, POST, PUT, DELETE, ETC)* https://yosoy.dev/peticiones-http-get-post-put-delete-etc/
