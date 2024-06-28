// Función para mostrar el contenido de la pestaña inicial al cargar la página
function showTab(tabName) {
  openCity(event, tabName);
}

// Función para abrir las pestañas
function openCity(evt, cityName) {
  var i, tabcontent, tablinks;

  // Ocultar todo el contenido de las pestañas
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Eliminar la clase "active" de todos los enlaces de las pestañas
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Mostrar la pestaña seleccionada y agregar la clase "active" al enlace de la pestaña seleccionada
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

// Función para filtrar los elementos
function filterSelection(c, filterClass) {
  var x, i;
  x = document.getElementsByClassName(filterClass);
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    removeClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) addClass(x[i], "show");
  }
}

// Función para agregar una clase a un elemento
function addClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Función para eliminar una clase de un elemento
function removeClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// Mostrar la pestaña de inicio al cargar la página
document.addEventListener("DOMContentLoaded", function() {
  showTab('Inicio');
});
