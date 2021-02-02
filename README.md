# pygroup-web-Perez-Miguel

**Autorización y autenticación**


**OAuth2**
Es el protócolo industrial estandar para la autorización. OAuth 2.0 se enefoca en la simpicaidad para el desarrollador proveendo de flujos específicos  para aplicaciones web, de cliente, mobile phones, etc. Es un framework de autorización que le permite a las aplicaciones obtener acceso limitado a cuentas de usuario en un servicio HTTP, como Facebook, GitHub. Delega la autenticación del usuario al servicio que aloja la cuenta del mismo y autoriza a las aplicaciones de terceros el acceso a dicha cuenta de usuario.

(<img src="https://assets.digitalocean.com/articles/translateddiagrams32918/Abstract-Protocol-Flow-Spanish@2x.png" width="45%"></img>

Antes de utilizar OAuth, debes registrar tu aplicación con el servicio. Esto se hace a través de un formulario de registro en la parte del “desarrollador” o “API” del sitio web del servicio, en el cual proporcionarás la siguiente información (y posiblemente detalles de tu aplicación):

* Nombre de la aplicación
* Sitio web de la aplicación
* Redirect URI o Callback URL
* Redirect URI es donde el servicio reorientará al usuario después de que se autorice (o deniegue) su solicitud y, por consiguiente, la parte de su aplicación que manejará códigos de autorización o tokens de acceso.


**OpenID**

Se pudede definir OpenID Connect como un servicio de identidad, que se utilizará para autenticar a los usuarios finales. Puede ser utilizado en dos direcciones:

* Como proveedores del servicio, somos capaces de garantizar la identidad del usuario y podemos brindar un interfaz de estándar abierto a terceros.
* Como consumidores del servicio, eliminamos la necesidad de mantener y securizar passwords y perfiles de usuario, y podemos centrarnos en ofrecer la funcionalidad de nuestro producto.

está pensado para la autenticación y OAuth para la autorización. Este añade las siguientes funcionalidades que complementan a OAuth:

* Un ID token que nos permite saber quién es el usuario.
* Un nuevo endpoint, UserInfo, que nos permite recuperar más información del usuario.
* Un conjunto de scopes estándar.
* Un conjunto de claims que nos permite obtener datos del sujeto.

Uno de los factores de uso más importantes de OpenID Connect es que está basado en estándares abiertos, es más fácil usar el servicio de un tercero que ya ha implementado el proceso de registro de un usuario y el almacenamiento seguro de sus contraseñas y datos privados. Además si lo pensamos como usuarios, tampoco queremos rellenar en cada nuevo sitio todos nuestros datos, ¿en cuántas ocasiones no hemos probado un sitio nuevo por no rellenar un formulario gigante? ¿cuánto ha costado a la empresa tener este proceso?

Otro elemento importante a tener en cuenta es que el uso de un protocolo como OpenID Connect no valida inmediatamente una identidad, es decir, aunque algunos proveedores de identidad como Google o Facebook provean este servicio no tiene porqué ser un servicio confiable. Es siempre más fiable la información provista por agencias gubernamentales o similares que han validado efectivamente la identidad, y que puede ser utilizada con fines legales.

**SAML Authentication**
El Lenguaje de marcado para confirmaciones de seguridad (SAML, por sus siglas en inglés) es un estándar abierto que permite que las credenciales de seguridad sean compartidas por múltiples computadoras a través de una red. Describe un marco que permite que una computadora realice algunas funciones de seguridad en nombre de otra o más computadoras:

* Autenticación: Determinar que los usuarios son quienes dicen ser
* Autorización: Determinar si los usuarios tienen derecho a acceder a ciertos sistemas o contenidos

SAML tiene diversas utilidades. Una de sus funciones es la de hacer declaraciones sobre las propiedades y autorizaciones de un usuario para otros usuarios o empresas asociadas, pero en especial sobre aplicaciones, es decir, a los "proveedores de servicios". Esto es posible gracias a que el identity provider, base de datos central en la que se almacena la correspondiente información del usuario, utiliza aserciones en un formato XML. Pero además, cuenta con otros componentes, como protocolos, enlaces y perfiles.

* **Aserciones**
Una aserción SAML es el documento XML creado por el proveedor de identidad que envía al proveedor de servicios, y puede contener una o más declaraciones. De hecho, existen tres tipos diferentes de aserciones SAML, que se especifican en SAML 2.0: autenticación, atributo y decisión de autorización.

* **Protocolos**
La especificación SAML 2.0 define un conjunto de protocolos de consulta / respuesta. A través de ellos, la aplicación puede solicitar o consultar una aserción, o bien solicitar a un usuario que se autentifique

* **Bindings
Las asignaciones de mensajes SAML en los protocolos estándar de mensajería o comunicación se denominan "enlaces de protocolo SAML" o simplemente "enlaces".

* **Perfiles
Una de las principales cualidades de SAML es su gran flexibilidad, que facilita su uso para una amplia variedad de propósitos. No obstante, hay que tener en cuenta que esa flexibilidad puede ser la causa de que algunas aplicaciones no lo admitan. Aunque en estos casos existe una solución que consiste en limitarla. La forma de hacerlo es usar los llamados perfiles

Referencias:

* **OAuth2**. *OAuth2 (17/12/20): https://oauth.net/2/
* **Mitchell Anicas**. *Una introducción a OAuth 2 (17/12/20): https://www.digitalocean.com/community/tutorials/una-introduccion-a-oauth-2-es
* **JOAQUIN COPETE**. *Breve introducción a OpenID Connect*. Tomado de (17/12/20): http://www.arquitectoit.com/api-management/breve-introduccion-open-id-connect/
* **Equipo NTS**. *¿Qué es SAML?*. Tomado de (17/12/20): https://www.nts-solutions.com/blog/saml-que-es.html


