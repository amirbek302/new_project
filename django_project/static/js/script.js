document.querySelectorAll('.theme-picker input').forEach(radio => {
  radio.addEventListener('change', (e) => {
    // Inject the theme value to HTML element node
    document.documentElement.setAttribute('data-theme', e.target.value);
  });
});