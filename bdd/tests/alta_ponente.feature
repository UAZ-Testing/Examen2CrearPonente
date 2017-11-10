Feature: Registrar ponente
  Como administrador del sistema
  Quiero dar de alta un ponente
  Con la finalidad de que esté disponible para asignarlo en el programa de un congreso

  Scenario: Registrar a ponente Manuel Haro
    Given se muestra la lista de ponentes
    And cada ponente tiene <Nombre>
    And cada ponente tiene <Primer Apellido>
    And cada ponente tiene <Segundo Apellido>
    And cada ponente tiene un botón <Editar Ponente>
    And cada ponente tiene un botón <Eliminar Ponente>
    When se hace click en el botón <Nuevo Ponente>
    And se llena en <Nombre> "Manuel Martín"
    And se llena en <Primer Apellido> "Haro"
    And se llena en <Segundo Apellido> "Márquez"
    And se hace click en el botón <Guardar Ponente>
    Then se redirige a la lista de ponentes
    And se muestra el mensaje <Ponente creado con éxito>
    And se muestra el ponente creado en la lista de ponentes
    And se finaliza la aplicación


  Scenario: Registrar a ponente Sin nombre
    Given se muestra la lista de ponentes
    And cada ponente tiene <Nombre>
    And cada ponente tiene <Primer Apellido>
    And cada ponente tiene <Segundo Apellido>
    And cada ponente tiene un botón <Editar Ponente>
    And cada ponente tiene un botón <Eliminar Ponente>
    When se hace click en el botón <Nuevo Ponente>
    And se llena en <Primer Apellido> "Haro"
    And se llena en <Segundo Apellido> "Márquez"
    And se hace click en el botón <Guardar Ponente>
    Then se muestra el error "El nombre es requerido"
    And se finaliza la aplicación