// Función para mostrar el contenido de la pestaña inicial al cargar la página
function showTab(tabName) {
    var tabcontent = document.getElementsByClassName("tabcontent");
    var tablinks = document.getElementsByClassName("tablinks");
  
    // Ocultar todos los contenidos de las pestañas y remover la clase 'active' de los enlaces
    for (var i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Mostrar el contenido de la pestaña seleccionada y agregar la clase 'active' al enlace correspondiente
    document.getElementById(tabName).style.display = "block";
    for (var i = 0; i < tablinks.length; i++) {
      if (tablinks[i].getAttribute('onclick').includes(tabName)) {
        tablinks[i].className += " active";
      }
    }
  }
  
  // Función para cambiar de pestaña al hacer clic en un enlace
  function openCity(evt, cityName) {
    showTab(cityName); // Mostrar la pestaña correspondiente
    evt.currentTarget.className += " active"; // Agregar la clase 'active' al enlace clicado
  }