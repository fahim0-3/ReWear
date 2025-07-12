console.log("I am loaded")
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".image-upload-box").forEach(function (box) {
        box.addEventListener("click", function () {
            let input = this.nextElementSibling;
            if (input && input.type === "file") {
                input.click();
            }
        });
    });

    document.querySelectorAll(".image-upload-input").forEach(function (input) {
        input.addEventListener("change", function () {
            let file = this.files[0];
            if (file) {
                let reader = new FileReader();
                reader.onload = function (e) {
                    input.previousElementSibling.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image">`;
                };
                reader.readAsDataURL(file);
            }
        });
    });
});
