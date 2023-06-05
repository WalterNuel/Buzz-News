const interests = document.getElementById('interests')
// const int_width = interests.clientWidth

const subMain = document.getElementById('s_main')
const subTopics = document.getElementById('s_topics')

window.onscroll = () => {
  let scrollTop = window.scrollY;
  let viewportHeight = window.innerHeight;
  let contentHeight = interests.getBoundingClientRect().height;
  let subMainHeight = subMain.getBoundingClientRect().height;


  if (scrollTop > contentHeight) {
    // interests.clientWidth = interests.parentElement.clientWidth
    // interests.style.position = 'fixed'
    interests.style.top = `0px`
    // interests.style.width = `${int_width}px`
  } else {
    interests.style.position = ''
  }

  if (scrollTop >= subMainHeight - viewportHeight) {
    subMain.style.top = `0px`
    subMain.style.position = `sticky`
  } else {
    subMain.style.position = ``
  }
}

