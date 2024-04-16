document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("signupForm");
    var createAccountBtn = document.getElementById("createaccount");
    var newPasswordInput = document.getElementById("newpassword");
    var confirmPasswordInput = document.getElementById("confirmpassword");
    var Errorpswd = document.getElementById("Errorpswd");

    function validatePassword() {
        if (newPasswordInput.value !== confirmPasswordInput.value) {
            Errorpswd.textContent = "Les mots de passe ne correspondent pas";
            createAccountBtn.disabled = true;
        } else {
            Errorpswd.textContent = "";
            createAccountBtn.disabled = false;
        }
    }

    newPasswordInput.addEventListener("input", validatePassword);
    confirmPasswordInput.addEventListener("input", validatePassword);
});
