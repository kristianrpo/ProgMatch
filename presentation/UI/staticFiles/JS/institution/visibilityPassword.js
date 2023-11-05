const hidePassword = document.getElementById('hidePassword');
const viewPassword = document.getElementById('viewPassword');
let visibility = false;

viewPassword.addEventListener('click', function() {
if (visibility) {
    hidePassword.style.display = 'none';
    viewPassword.innerText = 'View password';
} else {
    hidePassword.style.display = 'block';
    viewPassword.innerText = 'Hide password';
}
visibility = !visibility;
});