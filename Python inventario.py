
Estructura del repositorio
--------------------------
- inventario.py      -> Código principal (Producto, Inventario, menú).
- inventario.db      -> Creado automáticamente por el programa.
- README.md          -> Este archivo.

Notas sobre diseño
------------------
- Se utiliza `dict` para acceso rápido por ID.
- Se utiliza un índice invertido (`_index_nombre`) para acelerar búsquedas por palabra.
- La persistencia se hace con SQLite y se carga al iniciar para sincronizar memoria/DB.

Autor
-----
Tu Nombre - Curso / Asignatura
