const form = document.querySelector("form");
const divMsg = document.getElementById("divMsg");
const email = document.getElementById("email")?.innerText;
const password = document.getElementById("password")?.innerText;

form?.addEventListener("submit", (e)=>{
  e.preventDefault();

  alert(email);
  let msg = "";
  if (password?.length < 4) {
    msg = "⚠️ Your password must have at least 4 characters.\n" ; // 📩🔑
  }
  if (! (email?.includes("gmail.com"))) {
    msg += "⚠️ Please enter a correct email address!"
  }
  divMsg?.innerText = msg;

},false);
