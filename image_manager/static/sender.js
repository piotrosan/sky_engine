const imageSaveButton = document.querySelector("#saveImage");
imageSaveButton.addEventListener(
    "click",
    (event) => {
        const formData = new FormData();
        formData.append("image", document.getElementById("image").src);

        const request = new Request("https://localhost:8080/", {
          method: "POST",
          body: formData
        });

        fetch(request)
          .then((response) => {
            if (response.status === 200) {
              return response.json();
            } else {
              throw new Error("Something went wrong on API server!");
            }
          })
          .catch((error) => {
            console.error(error);
          });
})