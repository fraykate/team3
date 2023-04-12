


const searchBtn = document.getElementById('search-btn');
searchBtn.addEventListener('click', (e) => {
  e.preventDefault();
  const load = document.querySelector('.load-animation');
  load.style.cssText = 'display:block';
  search();
});


const showCounter = (movie) => movie.length;

const likeCounter = (e, likeCount, likes) => {
  likes.forEach((eachLikes) => {
    let id;
    try {
      id = e.show.id;
    } catch (err) {
      id = e.id;
    }
    if (String(eachLikes.item_id) === String(id)) {
      likeCount = eachLikes.likes;
    }
  });

  return likeCount;
};

export { likeCounter, showCounter };
