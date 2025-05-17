const request = new Request("https://localhost:8080/", {
  method: "POST",
  body: { 'image': document.getElementById("image").src },
});