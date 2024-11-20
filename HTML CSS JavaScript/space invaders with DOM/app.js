const gameArea = document.getElementById("gameArea");
const messageP = document.getElementById("messageP");
const messageScore = document.getElementById("score");
const pauseButton = document.getElementById("pauseButton");
const continueButton = document.getElementById("continueButton");

const nbDivX = 20; // number of divs in a line
const nbDivY = 20; // number of lines divs

const nbX = nbDivX; // number of invaders in a line at the begining
const nbY = 1; // number of lines invaders at the begining

let allDivs;
// invaderArray will contains indexes of all divs which
//   have the class invader
let invadersIndexArray = [];
let playerIndex;
let score = 0;
let invadersId;

function createGameAreaAndCharacters() {
  // construction of divs in the game area
  for (let i = 1; i <= 400; i++) {
    let div = document.createElement("div");
    gameArea.appendChild(div);
  }

  // get all div of the game area
  allDivs = gameArea.getElementsByTagName("div");

  // fill invaders array
  for (let i = 0; i < nbY; i++) {
    let array_i = [];

    for (let j = i * nbDivX; j <= i * nbDivX + nbX - 1; j++) {
      array_i.push(j);
    }

    invadersIndexArray.push(array_i);
  }

  // set player position
  playerIndex = nbDivX * (nbDivY - 2) + parseInt(nbDivX / 2);

  // display invaders on the screen
  displayOrRemoveInvaders("display");

  // display player on the screen
  allDivs[playerIndex].classList.add("player");
}

function displayOrRemoveInvaders(action) {
  if (action === "display") {
    invadersIndexArray.forEach((array_i) => {
      array_i.forEach((invaderIndex) => {
        allDivs[invaderIndex].classList.add("invader");
      });
    });
  } else if (action === "remove") {
    invadersIndexArray.forEach((array_i) => {
      array_i.forEach((invaderIndex) => {
        allDivs[invaderIndex].classList.remove("invader");
      });
    });
  }
}

function randomNumber(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

function moveAndAddInvaders() {
  // remove invaders from the screen
  displayOrRemoveInvaders("remove");

  // add a new line of invaders
  let array_i = [];
  // that line will have a random length
  let nbInvader = randomNumber(parseInt(nbDivX / 4), nbDivX);

  for (let i = 0; i < nbInvader; i++) {
    // add a random invader
    array_i.push(randomNumber(0, nbDivX));
  }
  // add in the invaders array at the first line
  invadersIndexArray.unshift(array_i);

  // move all invaders
  for (let i = 0; i < invadersIndexArray.length; i++) {
    for (let j = 0; j < invadersIndexArray[i].length; j++) {
      invadersIndexArray[i][j] += nbDivX;
    }
  }
  // remove all invaders which are not in the game area
  for (let i = 0; i < invadersIndexArray.length; i++) {
    invadersIndexArray[i] = invadersIndexArray[i].filter(
      (invaderIndex) => invaderIndex <= nbDivX * nbDivY - 1
    );
  }
  // display invaders on the screen
  displayOrRemoveInvaders("display");

  // gameover ?
  if (gameOver()) {
    // animate the player
    allDivs[playerIndex].classList.add("boom");

    // stop invaders evolution
    clearInterval(invadersId);

    // display the message on the screen
    messageP.innerHTML = "GAME OVER !";

    // stop any possibility of moving the player
    document.removeEventListener("keydown", movePlayer);

    // stop any possibility of fire
    document.removeEventListener("keypress", fire, false);
  }
}

function gameOver() {
  for (let i = invadersIndexArray.length - 1; i >= 0; i--) {
    for (let j = 0; j < invadersIndexArray[i].length; j++) {
      if (
        invadersIndexArray[i][j] === playerIndex - 1 ||
        invadersIndexArray[i][j] === playerIndex ||
        invadersIndexArray[i][j] === playerIndex + 1
      ) {
        // game over
        return true;
      }
    }
  }
  return false;
}
function displayOrRemovePlayer(action, position) {
  if (action === "display") {
    allDivs[position].classList.add("player");
  } else if (action === "remove") {
    allDivs[position].classList.remove("player");
  }
}
function movePlayer(e) {
  let oldPlayerIndex = playerIndex;

  if (e.keyCode === 37) {
    // left direction
    if (playerIndex % nbDivX != 0) {
      // the player is not at the border of game area
      playerIndex -= 1;
    }
  } else if (e.keyCode === 38) {
    // up direction
    if (playerIndex > 2 * nbDivX) {
      // the player is under the second line
      playerIndex -= nbDivX;
    }
  } else if (e.keyCode === 39) {
    // right direction
    if ((playerIndex + 1) % nbDivX != 0) {
      // the player is not at the border of game area
      playerIndex += 1;
    }
  } else if (e.keyCode === 40) {
    // down direction
    if (playerIndex < (nbDivY - 1) * nbDivX) {
      // the player is up the last line
      playerIndex += nbDivX;
    }
  }

  displayOrRemovePlayer("remove", oldPlayerIndex);
  displayOrRemovePlayer("display", playerIndex);
}

function fire(e) {
  let bulletId;
  let currentBullet = playerIndex;

  function collision() {
    if (allDivs[currentBullet].classList.contains("invader")) {
      // there is a collision
      score += 1;
      messageScore.innerHTML = score;
      allDivs[currentBullet].classList.remove("invader");
      allDivs[currentBullet].classList.remove("bullet");
      allDivs[currentBullet].classList.add("boom");

      // remove the invader from invaders array
      for (let i = 0; i < invadersIndexArray.length; i++) {
        invadersIndexArray[i] = invadersIndexArray[i].filter(
          (invaderIndex) => invaderIndex !== currentBullet
        );
      }

      // after 250ms remove the class boom form the div
      setTimeout(() => {
        allDivs[currentBullet].classList.remove("boom");
      }, 250);

      clearInterval(bulletId);
    }
  }

  function moveBullet() {
    allDivs[currentBullet].classList.remove("bullet");
    currentBullet -= nbDivX;

    if (currentBullet < 0) {
      // the bullet is not yet in the game area, we delete it.
      clearInterval(bulletId);
    } else {
      // the bullet is yet in the game area
      allDivs[currentBullet].classList.add("bullet");

      // look for the collision
      collision();
    }
  }

  // we will fire with space (touche espace du clavier)
  if (e.keyCode === 32) {
    // space
    bulletId = setInterval(moveBullet, 100);
  }
}

function pause() {
  if (gameArea.classList.contains("defile")) {
    gameArea.classList.remove("defile");
  }
  clearInterval(invadersId);
}
function continueR() {
  if (!gameArea.classList.contains("defile")) {
    gameArea.classList.add("defile");
  }
  if (!(messageP.innerHTML === "GAME OVER !")) {
    invadersId = setInterval(moveAndAddInvaders, 1500);
  }
}

pauseButton.addEventListener("click", pause, false);
continueButton.addEventListener("click", continueR, false);

createGameAreaAndCharacters();
document.addEventListener("keydown", movePlayer, false);
document.addEventListener("keypress", fire, false);
invadersId = setInterval(moveAndAddInvaders, 1500);
