const form = document.getElementById('form');
const names = document.getElementById('names');
const depart = document.getElementById('department');
const design = document.getElementById('designation');
const macadd = document.getElementById('macadd');
const select = document.getElementById('system');
const specify = document.getElementById('others');
const mail = document.getElementById('email');
const cell = document.getElementById('phone');
const agreed = document.getElementById('agree');
const faculty = document.getElementById('faculty');
const image = document.getElementById('upload');
const time = document.getElementById('date');
const patternAlpha = /^[a-zA-Z ]*$/g;
const patternMac = /^([0-9a-f]{2}([:-]|$)){6}$|([0-9a-f]{4}([.]|$)){3}$/gi;
const patternEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
const allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
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
    const departValue = depart.value.trim();

    if (departValue === ''){
        setInvalid(depart, '');
    }else if(departValue.length < 5){
        setInvalid(depart, 'Too short!😭');
    }else if(!departValue.match(patternAlpha)){
        setInvalid(depart, 'Invalid input!😭');
    }else{
        setValid(depart);
    }
}

function c(){
    const designValue = design.value.trim();

    if (designValue === ''){
        setInvalid(design, '');
    }else if(designValue.length < 5){
        setInvalid(design, 'Too short!😭');
    }else if(!designValue.match(patternAlpha)){
        setInvalid(design, 'Invalid input!😭');
    }else{
        setValid(design);
    }
}

function d(){
    const macValue = macadd.value.trim();

    if (macValue === ''){
        setInvalid(macadd, '');
    }else if(!macValue.match(patternMac)){
        setInvalid(macadd, 'Invalid input!😭');
    }else{
        setValid(macadd);
    }
}

function e(){
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

function f(){
    const specifyValue = specify.value.trim();

    if (specifyValue === ''){
        setInvalid(specify, '');
    }else if(specifyValue.length < 3){
        setInvalid(specify, 'Too short!😭');
    }else{
        setValid(specify);
    }
}

function g(){
    const mailValue = mail.value.trim();

    if (mailValue === ''){
        setInvalid(mail, '');
    }else if(!mailValue.match(patternEmail)){
        setInvalid(mail, 'Wrong format!😭');
    }else{
        setValid(mail);
    }
}

function h(){
    const cellValue = cell.value.trim();

    if (cellValue === ''){
        setInvalid(cell, '');
    }else if(cellValue.length < 11){
        setInvalid(cell, 'Wrong format!😭');
    }else{
        setValid(cell);
    }
}

function i(){
    const facultyValue = faculty.value.trim();

    if (facultyValue === ''){
        setInvalid(faculty, '');
    }else if(facultyValue.length < 9){
        setInvalid(faculty, 'Too short!😭');
    }else if(!facultyValue.match(patternAlpha)){
        setInvalid(faculty, 'Invalid input!😭');   
    }else{
        setValid(faculty);
    }
}

function j(){
    const imageValue = image.value.trim();

    if (!allowedExtensions.exec(imageValue)) {
        image.value = '';
        image.classList.add('is-invalid');
    }else{
        image.classList.replace('is-invalid' , 'is-valid');
    }
}

function k(){
    const timeValue = time.value.trim();

    if (timeValue === ''){
        setInvalid(time, '');
    }else if (time.value != tdate){
        setInvalid(time, 'Invalid time😭');
        //alert(time.value + " == " + tdate);
    }else{
        setValid(time);
    }
}

function checkInputs(){
    const nameValue = names.value.trim();
    const departValue = depart.value.trim();
    const designValue = design.value.trim();
    const macValue = macadd.value.trim();
    const selectValue = select.value.trim();
    const specifyValue = specify.value.trim();
    const mailValue = mail.value.trim();
    const cellValue = cell.value.trim();
    const facultyValue = faculty.value.trim();
    const imageValue = image.value.trim();
    const timeValue = time.value.trim();

    
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

    if (departValue === ''){
        setInvalid(depart, '');
    }else if(departValue.length < 5){
        setInvalid(depart, 'Too short!😭');
    }else if(!departValue.match(patternAlpha)){
        setInvalid(depart, 'Invalid input!😭');
    }else{
        setValid(depart);
        check();
    }

    if (designValue === ''){
        setInvalid(design, '');
    }else if(designValue.length < 5){
        setInvalid(design, 'Too short!😭');
    }else if(!designValue.match(patternAlpha)){
        setInvalid(design, 'Invalid input!😭');
    }else{
        setValid(design);
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
    
    if (mailValue === ''){
        setInvalid(mail, '');
    }else if(!mailValue.match(patternEmail)){
        setInvalid(mail, 'Wrong format!😭');
    }else{
        setValid(mail);
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

    if (agreed.checked){
        check();
    }else{
        agreed.focus();
    }

    if (facultyValue === ''){
        setInvalid(faculty, '');
    }else if(facultyValue.length < 9){
        setInvalid(faculty, 'Too short!😭');
    }else if(!facultyValue.match(patternAlpha)){
        setInvalid(faculty, 'Invalid input!😭');   
    }else{
        setValid(faculty);
        check();
    }

    if (!allowedExtensions.exec(imageValue)) {
        image.value = '';
        image.classList.add('is-invalid');
    }else{
        image.classList.replace('is-invalid' , 'is-valid');
        check();
    }

    if (timeValue === ''){
        setInvalid(time, '');
    }else if (time.value != tdate){
        setInvalid(time, 'Invalid time😭');
        //alert(time.value + " == " + tdate);
    }else{
        setValid(time);
        check();
    }
    
    if (nameValue != '' && departValue != '' && designValue != '' && macValue != '' && selectValue != '' || specifyValue != ''
     && mailValue != '' && cellValue != '' && facultyValue != '' && imageValue != '' && timeValue != ''){
    }if (total == 11){
        alert("You Have Successfully Submitted The Form✨🥳🎉");
        total = 0;
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