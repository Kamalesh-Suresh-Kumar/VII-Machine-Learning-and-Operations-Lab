function showMessage() {
    const message = document.getElementById("message");
    const info = document.getElementById("info");
    message.textContent = "CI/CD pipeline verified successfully!";
    info.textContent = "Version 2 deployed using Jenkins.";
}