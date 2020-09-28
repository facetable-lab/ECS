let button = document.querySelector('.btn-change-theme');
let page = document.querySelector('.page');

button.onclick = function() {
  page.classList.toggle('light-theme');
  page.classList.toggle('dark-theme');
};
