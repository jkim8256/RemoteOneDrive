const search = document.querySelector("#search");
const input = search.querySelector("input");

function handleSubmit(event) {
  event.preventDefault();
  const link = "http://google.com/search?q=";
  console.log(link + input.value);
  window.location.replace(link + input.value);
}

search.addEventListener("submit", handleSubmit);

const RESTID = "rest";

search.classList.add(RESTID);
