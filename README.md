Enunciado del Proyecto: Sistema de Gestión de Usuarios y Permisos para una Plataforma SaaS

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Descripción del Proyecto:
El proyecto consiste en desarrollar un sistema para gestionar usuarios y sus roles dentro de una plataforma SaaS (Software como Servicio), donde los usuarios pueden tener diferentes niveles de acceso (por ejemplo, Administradores, Moderadores y Usuarios) y realizar acciones específicas de acuerdo con su rol. El sistema debe gestionar la creación de usuarios, asignación de roles, acceso a funcionalidades específicas y la ejecución de diversas acciones, como cambiar configuraciones o realizar tareas dentro de la plataforma.

Objetivos del Proyecto:
Aplicación de la Programación Orientada a Objetos (POO):

Definir una clase base Usuario con atributos comunes como nombre, email, rol y métodos comunes como iniciar_sesion() y cerrar_sesion().
Crear clases derivadas como Administrador, Moderador y UsuarioRegular, que hereden de la clase base Usuario y tengan comportamientos específicos según el rol (por ejemplo, el Administrador puede modificar configuraciones del sistema, el Moderador puede gestionar contenido, etc.).
Uso de Encapsulamiento y Herencia:

Los atributos sensibles (como las contraseñas) deben estar encapsulados para evitar acceso directo.
Utilizar herencia para crear relaciones jerárquicas entre Usuario y sus roles, asegurando que los métodos comunes se hereden de la clase base, pero que cada rol tenga acciones y permisos específicos.
Polimorfismo y Métodos Abstractos:

Implementar polimorfismo para que el método realizar_accion() tenga diferentes implementaciones dependiendo del rol del usuario. Los Administradores, por ejemplo, podrán realizar más acciones que un Usuario Regular.
Usar clases abstractas para definir métodos comunes que deben ser implementados por todas las clases de rol, asegurando que cada tipo de usuario implemente su propio comportamiento.
Patrones de Diseño:

Singleton: Usar un patrón Singleton para la clase GestorUsuarios, garantizando que solo exista una instancia que administre todos los usuarios y sus roles dentro de la plataforma.
Factory: Implementar un patrón Factory para crear instancias de diferentes roles de usuarios (Administrador, Moderador, UsuarioRegular) sin que el código cliente dependa de las clases específicas.
Patrones de Diseño Avanzados:

Strategy: Usar el patrón Strategy para permitir que el sistema cambie la forma en que se asignan permisos y roles, basándose en una política de seguridad diferente según el tipo de usuario.
Observer: Aplicar el patrón Observer para notificar a los usuarios sobre cambios importantes (por ejemplo, actualización de políticas o nuevos permisos asignados) o cuando se detecte actividad sospechosa en su cuenta.
Uso de Clases Anónimas, Internas y Lambda Expressions:

Implementar clases anónimas o internas para funcionalidades específicas, como una clase que gestione la validación de contraseñas o una clase interna que verifique los permisos antes de ejecutar una acción.
Utilizar lambda expressions para realizar cálculos rápidos, como evaluar si un usuario tiene suficientes privilegios para ejecutar una acción específica, sin necesidad de crear una función completa.
Requerimientos del Sistema:
Gestión de Usuarios y Roles:

Crear una clase base Usuario con métodos comunes (iniciar_sesion(), cerrar_sesion()) y atributos (nombre, email, rol).
Crear las clases derivadas Administrador, Moderador y UsuarioRegular, con implementación de métodos específicos como gestionar_contenido() para Moderadores y modificar_configuraciones() para Administradores.
Patrones de Diseño:

Singleton: Implementar la clase GestorUsuarios con el patrón Singleton para garantizar que solo exista una instancia encargada de gestionar a todos los usuarios.
Factory: Crear una clase UsuarioFactory que genere usuarios con roles específicos sin exponer detalles internos al cliente.
Patrones Avanzados:

Strategy: Implementar estrategias para asignar permisos basadas en la política de seguridad de la empresa. Cada rol tendrá una estrategia diferente para manejar el acceso.
Observer: Implementar un sistema de notificaciones que avise a los usuarios cuando haya actualizaciones en sus permisos, cambios de rol o eventos de seguridad importantes.
Clases Anónimas y Lambda Expressions:

Usar clases internas para la validación de datos (como una clase que valide contraseñas).
Implementar expresiones lambda para realizar evaluaciones rápidas, como comprobar si un usuario tiene el rol adecuado antes de ejecutar una acción.
Entregables del Proyecto:
Código fuente completo de las clases base y derivadas para los usuarios y roles.
Implementación de los patrones de diseño Singleton, Factory, Strategy y Observer.
Documentación detallada sobre cómo se implementaron los patrones y la POO en el sistema.
Pruebas unitarias para verificar el comportamiento del sistema, asegurando que los usuarios y sus permisos sean gestionados correctamente.
Resumen:
Este proyecto te permitirá aplicar los conceptos fundamentales de la Programación Orientada a Objetos (POO), como herencia, polimorfismo, encapsulamiento y clases abstractas, junto con patrones de diseño como Singleton, Factory, Strategy y Observer en un escenario realista de gestión de usuarios y permisos en una plataforma SaaS. El sistema debe ser flexible, extensible y capaz de manejar distintos roles con diferentes permisos, y permitir la asignación dinámica de funciones en función del tipo de usuario. El uso de patrones de diseño avanzados optimizará la arquitectura del sistema, haciéndolo más modular y fácil de mantener.


