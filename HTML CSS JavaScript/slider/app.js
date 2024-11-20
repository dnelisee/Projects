const slider = document.querySelector(".slider");
const leftButton = document.getElementById("left-button");
const rightButton = document.getElementById("right-button");
const choiceButtons = document.querySelectorAll("input[type='radio']");

// event on choice buttons
for (let i = 0; i < 3; i++) {
  choiceButtons[i].onclick = () => {
    slider.setAttribute("bgImgValue", `${i}`);
    setBgImg();
  };
}

leftButton.onclick = () => {
  const currentBgImg = parseInt(slider.getAttribute("bgImgValue")); 
  slider.setAttribute("bgImgValue", `${(currentBgImg-1)%3}`);
  setBgImg();
}
rightButton.onclick = () => {
  const currentBgImg = parseInt(slider.getAttribute("bgImgValue")); 
  slider.setAttribute("bgImgValue", `${(currentBgImg+1)%3}`);
  setBgImg();
}

function setBgImg() {
  // get the current background image number 
  let currentBgImg = parseInt(slider.getAttribute("bgImgValue"));

  // that value must be in [0,1,2]
  currentBgImg = currentBgImg < 0 ? currentBgImg + 3 : currentBgImg;

  // change the background image 
  slider.style.backgroundImage = `url('images/${currentBgImg+1}.jpg')`;

  // change the input which is checked 
  for(let i = 0; i < 3; i++) {
    if(choiceButtons[i].checked) {
      choiceButtons[i].checked = false; 
      choiceButtons[currentBgImg].checked = true; 
      break;
    }
  }
} 