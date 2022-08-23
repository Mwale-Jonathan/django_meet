// Toasts
const toastElList = document.querySelectorAll('.toast')
const toastList = [...toastElList].map(
    toastEl => new bootstrap.Toast(toastEl).show()
)

// Avater Images
function generateAvatar(
text,
foregroundColor = "white",
backgroundColor = "black"
) {
const canvas = document.createElement("canvas");
const context = canvas.getContext("2d");

canvas.width = 200;
canvas.height = 200;

// Draw background
context.fillStyle = backgroundColor;
context.fillRect(0, 0, canvas.width, canvas.height);

// Draw text
context.font = "bold 100px Assistant";
context.fillStyle = foregroundColor;
context.textAlign = "center";
context.textBaseline = "middle";
context.fillText(text, canvas.width / 2, canvas.height / 2);

return canvas.toDataURL("image/png");
}

let avatars = document.querySelectorAll('#avatar');

for (var avatar in avatars) {
    let initials = avatars[avatar].getAttribute('data-initials');

    document.getElementById("avatar").src = generateAvatar(
    initials.toUpperCase(),
    "white",
    "#30304F"
    );
}
