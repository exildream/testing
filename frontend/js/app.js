(function () {
  const tg = window.Telegram.WebApp;
  const user = tg.initDataUnsafe?.user;
  if (user) {
    const welcome = document.getElementById('welcome');
    welcome.textContent = `Привет, ${user.first_name}!`;
  }
})();
