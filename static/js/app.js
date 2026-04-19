if ("serviceworker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceworker
      .register("static/js/serviceworker.js")
      .then((res) => console.log("service worker registered"))
      .catch((err) => console.log("service worker not registered", err));
  });
}

function formatDates() {
  const isSmall = window.innerWidth <= 800;
  const cells = document.querySelectorAll(".date-cell");

  cells.forEach((cell) => {
    const original = cell.dataset.original;
    console.log(original);

    if (!original) return;

    if (isSmall) {
      // yyyy-mm-dd → dd-mm-yy
      const [y, m, d] = original.split("-");
      cell.textContent = `${y.slice(2)}/${m}/${d}`;
    } else {
      // restore original
      cell.textContent = original;
    }
  });
}

// run on load + resize
window.addEventListener("load", formatDates);
window.addEventListener("resize", formatDates);
