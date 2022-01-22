const form = document.getElementById('form');
const names = document.getElementById('names');
const cor = document.getElementById('course');
const semes = document.getElementById('semester');
const tupId = document.getElementById('tupcnum');
const or = document.getElementById('orno');
const cell = document.getElementById('phone');
const select = document.getElementById('system');
const specify = document.getElementById('others');
const macadd = document.getElementById('macadd');
const mail = document.getElementById('email');
const residence = document.getElementById('resid');
const agreed = document.getElementById('agree');
const image = document.getElementById('upload');
const username = document.getElementById('uname');
const password = document.getElementById('pass');

const patternTupId = /[T][U][P][C]-[0-9]{2}-[0-9]{4}/;
const patternAlpha = /^[a-zA-Z ]*$/g;
const patternMac = /^([0-9a-f]{2}([:-]|$)){6}$|([0-9a-f]{4}([.]|$)){3}$/gi;
const patternEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
const allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
//const regex = /[0][9][0-9]{9}/g;
var total = 0;

let currentDate = new Date();
let cDay = currentDate.getDate();
let cMonth = currentDate.getMonth() + 1;
let cYear = currentDate.getFullYear();
const tdate = cYear + "-" + "0" + cMonth + "-" + cDay;

const tip = document.getElementById('display');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    checkInputs();
});

function a(){
    const nameValue = names.value.trim();

    if (nameValue === ''){
        setInvalid(names, '');
    }else if(nameValue.length < 9){
        setInvalid(names, 'Too short!😭');
    }else if(!nameValue.match(patternAlpha)){
        setInvalid(names, 'Invalid input!😭');   
    }else{
        setValid(names);
    }
}

function b(){
    const corValue = cor.value.trim();

    if (corValue == ''){
        cor.style.borderColor = '#e74c3c';
        setInvalid(cor, '');
    }else{
        cor.style.borderColor = '#2ecc71';
        setValid(cor);
    }
}

function c(){
    const semesValue = semes.value.trim();

    if (semesValue == ''){
        semes.style.borderColor = '#e74c3c';
        setInvalid(semes, '');
    }else{
        semes.style.borderColor = '#2ecc71';
        setValid(semes);
    }
}

function d(){
    const tupIdValue = tupId.value.trim();

    if (tupIdValue === ''){
        setInvalid(tupId, '');
    }else if(!tupIdValue.match(patternTupId)){
        setInvalid(tupId, 'Invalid format!😭');
    }else{
        setValid(tupId);
    }
}

function e(){
    const orValue = or.value.trim();

    if (orValue === ''){
        setInvalid(or, '');
    }else if(orValue.length < 6){
        setInvalid(or, 'Too short!😭');
    }else{
        setValid(or);
    }
}

function f(){
    const cellValue = cell.value.trim();

    if (cellValue === ''){
        setInvalid(cell, '');
    }else if(cellValue.length < 11){
        setInvalid(cell, 'Wrong format!😭');
    }else{
        setValid(cell);
    }
}

function g(){
    const selectValue = select.value.trim();

    if (selectValue == ''){
        sysNotSelected();
    }else if(selectValue == 'Others'){
        sysSelected();
        specify.disabled = '';
    }else{
        setValid(select);
        specify.value = '';
        sysSelected();
    }
}

function h(){
    const specifyValue = specify.value.trim();

    if (specifyValue === ''){
        setInvalid(specify, '');
    }else if(specifyValue.length < 3){
        setInvalid(specify, 'Too short!😭');
    }else{
        setValid(specify);
    }
}

function i(){
    const macValue = macadd.value.trim();

    if (macValue === ''){
        setInvalid(macadd, '');
    }else if(!macValue.match(patternMac)){
        setInvalid(macadd, 'Invalid input!😭');
    }else{
        setValid(macadd);
    }
}

function j(){
    const mailValue = mail.value.trim();

    if (mailValue === ''){
        setInvalid(mail, '');
    }else if(!mailValue.match(patternEmail)){
        setInvalid(mail, 'Wrong format!😭');
    }else{
        setValid(mail);
    }
}

function k(){
    const residenceValue = residence.value.trim();

    if (residenceValue === ''){
        setInvalid(residence, '')
    }else if (residenceValue.length < 20){
        setInvalid(residence, 'Too short!😭')
    }else{
        setValid(residence);
    }
}

function l(){
    const imageValue = image.value.trim();

    if (!allowedExtensions.exec(imageValue)) {
        image.value = '';
        image.classList.add('is-invalid');
    }else{
        image.classList.replace('is-invalid' , 'is-valid');
    }
}

function m(){
    const usernameValue = username.value.trim();

    if (usernameValue === ''){
        setInvalid(username, '');
    }else if(usernameValue.length < 8){
        setInvalid(username, 'Too short!😭');
    }else if(!usernameValue.match(patternAlpha)){
        setInvalid(username, 'Invalid input!😭');   
    }else{
        setValid(username);
    }
}

function n(){
    const passwordValue = password.value.trim();

    if (passwordValue === ''){
        setInvalid(password, '');
    }else if(passwordValue.length < 8){
        setInvalid(password, 'Too short!😭');
    }else if(!passwordValue.match(patternAlpha)){
        setInvalid(password, 'Invalid input!😭');   
    }else{
        setValid(password);
    }
}

function checkInputs(){
    const nameValue = names.value.trim();
    const corValue = cor.value.trim();
    const semesValue = semes.value.trim();
    const tupIdValue = tupId.value.trim();
    const orValue = or.value.trim();
    const cellValue = cell.value.trim();
    const selectValue = select.value.trim();
    const specifyValue = specify.value.trim();
    const macValue = macadd.value.trim();
    const mailValue = mail.value.trim();
    const residenceValue = residence.value.trim();
    const imageValue = image.value.trim();
    const usernameValue = username.value.trim();
    const passwordValue = password.value.trim();
    
    if (nameValue === ''){
        setInvalid(names, '');
    }else if(nameValue.length < 9){
        setInvalid(names, 'Too short!😭');
    }else if(!nameValue.match(patternAlpha)){
        setInvalid(names, 'Invalid input!😭');   
    }else{
        setValid(names);
        check();
    }

    if (corValue == ''){
        cor.style.borderColor = '#e74c3c';
        setInvalid(cor, '');
    }else{
        cor.style.borderColor = '#2ecc71';
        setValid(cor);
        check()
    }

    if (semesValue === ''){
        semes.style.borderColor = '#e74c3c';
        setInvalid(semes, '');
    }else{
        semes.style.borderColor = '#2ecc71';
        setValid(semes);
        check()
    }

    if (tupIdValue === ''){
        setInvalid(tupId, '');
    }else if(!tupIdValue.match(patternTupId)){
        setInvalid(tupId, 'Invalid format!😭');
    }else{
        setValid(tupId);
        check();
    }

    if (orValue === ''){
        setInvalid(or, '');
    }else if(orValue.length < 6){
        setInvalid(or, 'Too short!😭');
    }else{
        setValid(or);
        check();
    }

    if (cellValue === ''){
        setInvalid(cell, '');
    }else if(cellValue.length < 11){
        setInvalid(cell, 'Wrong format!😭');
    }else{
        setValid(cell);
        check();
    }

    if (selectValue == ''){
        sysNotSelected();
    }else if(selectValue == 'Others'){
        sysSelected();
        specify.disabled = '';
    }else{
        setValid(select);
        specify.value = '';
        sysSelected();
        check();
    }

    if (specifyValue === ''){
        setInvalid(specify, '');
    }else if(specifyValue.length < 3){
        setInvalid(specify, 'Too short!😭');
    }else{
        setValid(specify);
        check();
    }

    if (macValue === ''){
        setInvalid(macadd, '');
    }else if(!macValue.match(patternMac)){
        setInvalid(macadd, 'Invalid input!😭');
    }else{
        setValid(macadd);
        check();
    }
    
    if (mailValue === ''){
        setInvalid(mail, '');
    }else if(!mailValue.match(patternEmail)){
        setInvalid(mail, 'Wrong format!😭');
    }else{
        setValid(mail);
        check();
    }

    if (residenceValue === ''){
        setInvalid(residence, '')
    }else if (residenceValue.length < 20){
        setInvalid(residence, 'Too short!😭')
    }else{
        setValid(residence);
        check();
    }

    if (agreed.checked){
        check();
    }else{
        agreed.focus();
    }

    if (!allowedExtensions.exec(imageValue)) {
        image.value = '';
        image.classList.add('is-invalid');
    }else{
        image.classList.replace('is-invalid' , 'is-valid');
        check();
    }

    if (usernameValue === ''){
        setInvalid(username, '');
    }else if(usernameValue.length < 8){
        setInvalid(username, 'Too short!😭');
    }else if(!usernameValue.match(patternAlpha)){
        setInvalid(username, 'Invalid input!😭');   
    }else{
        setValid(username);
        check();
    }

    if (passwordValue === ''){
        setInvalid(password, '');
    }else if(passwordValue.length < 8){
        setInvalid(password, 'Too short!😭');
    }else if(!passwordValue.match(patternAlpha)){
        setInvalid(password, 'Invalid input!😭');   
    }else{
        setValid(password);
        check();
    }
  
    //if (nameValue != '' && departValue != '' && designValue != '' && macValue != '' && selectValue != '' || specifyValue != ''
    // && mailValue != '' && cellValue != '' && passwordValue != '' && imageValue != '' && usernameValue != '' && passwordValue != ''
    // && residenceValue != '' && orValue != '' ){}
    if (total == 14){
        form.reset();//reset the form upon submission
        window.location.href="success.html";//show success page
        window.location.replace("success.html")//once submitted no return
    }else{
        alert("Please leave no blank spaces and enter correct details!😭😭😭")
        total = 0;
    }
    
}
    
function setInvalid(input,message){
    const formGroup = input.parentElement;
    const small = formGroup.querySelector('small');

    small.innerText = message;

    formGroup.className = 'form-group error';
}

function setValid(input){
    const formGroup = input.parentElement;
    formGroup.className = 'form-group success';
}

function check(){
    total = total + 1;
}

function sysSelected(){
    select.style.borderColor = '#2ecc71';
    specify.disabled = 'true';
}

function sysNotSelected(){
    select.style.borderColor = '#e74c3c';
    setInvalid(select, '');
}

$('#names').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#course').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#semester').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#tupcnum').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#orno').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#macadd').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#system').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#others').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#email').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#phone').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#system').tooltip({title: "Please select item in the list👍", placement:"top",  trigger: "hover"});
$('#others').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#uname').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#pass').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#resid').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#upload').tooltip({title: "Submit image file('png','jpg','jpg')👍", placement:"top",  trigger: "hover"});

$("input[type='file']").click(function () {
    $("input[id='upload']").click();
});
 $("input[id='upload']").change(function (e) {
     var $this = $(this);
     $this.next().html($this.val().split('\\').pop());
});