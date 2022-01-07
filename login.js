


function interactiveAdmin() {
    
    var user = document.forms['login']['user'];
    var password = document.forms['login']['password'];
    var email_error = document.getElementById("user_error");
    var pass_error = document.getElementById("pass_error");
    

    if (user.value != 'admin') {
        user.style.border = "2px solid red";
        user_error.style.display = "block";
        user.focus();
        return false;
    }
    if (password.value != '1234') {
        password.style.border = "2px solid red";
        pass_error.style.display = "block";
        password.focus();
        return false;
    }

    
}
user.addEventListener('textInput', user_Verify);
password.addEventListener('textInput', password_Verify);

function user_Verify() {
    if (user.value >= 5) {
        user.style.border = "2px solid rgb(4, 35,80)";
        user_error.style.display = "none";
        user.focus();
        return true;
    }}
function password_Verify() {
    if (password.value.length >= 4) {
        password.style.border = "2px solid rgb(4, 35,80)";
        pass_error.style.display = "none";
        password.focus();
        return true;
        }}
