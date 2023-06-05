const content = document.getElementById('content');
const heading = document.getElementById("heading");
const para = document.getElementById('para');
const starter = document.getElementById('starter');
const startBtn = document.getElementById('start-btn');


content.addEventListener('animationend', () => {
  heading.classList.add('rise')

  heading.addEventListener('transitionend', () => {
    para.classList.add('rise')
  })

  para.addEventListener('transitionend', () => {
    starter.classList.add('rise')
  })

  starter.addEventListener('transitionend', () => {
    startBtn.style.opacity = `1`
  })
})
