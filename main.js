var arrows = document.querySelectorAll(".arrow-main");

arrows.forEach(function (arrow) {
  arrow.addEventListener("click", function (e) {
    e.preventDefault();

    if (!arrow.classList.contains("animate")) {
      arrow.classList.add("animate");
      setTimeout(function () {
        arrow.classList.remove("animate");
      }, 1600);
    }
  });
});

function redirectTo(page) {
  window.location.href = page;
}
