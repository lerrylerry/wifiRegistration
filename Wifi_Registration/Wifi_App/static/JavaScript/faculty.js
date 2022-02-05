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
const faculty = document.getElementById('facultys');
const image = document.getElementById('upload');
const time = document.getElementById('date');

const patternAlpha = /^[a-zA-Z ]*$/g;
const patternMac = /^([0-9a-f]{2}([:-]|$)){6}$|([0-9a-f]{4}([.]|$)){3}$/gi;
const patternEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
const allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
const regex = /[0][9][0-9]{9}/g;
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
    }else if(!cellValue.match(regex)){
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
    }else if(!cellValue.match(regex)){
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
    
    //if (nameValue != '' && departValue != '' && designValue != '' && macValue != '' && selectValue != '' || specifyValue != ''
    //&& mailValue != '' && cellValue != '' && facultyValue != '' && imageValue != '' && timeValue != ''){}
    if (total == 11){
        //form.reset();//reset the form upon submission
        //window.location.replace("success")//once submitted no return
        //document.getElementById('form').submit()//try muna to!
        window.location.href="/faculty/success.html/";//show success page
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

// file upload validation
function validateFileupload(){
    var fileInput = document.getElementById("Agreement");
              
    var filePath = fileInput.value;
          
    var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
              
    if (!allowedExtensions.exec(filePath)) {
        alert('Invalid file type');
        fileInput.value = '';
        return false;
    }
        return true;
}

// Confirm Form Submission


$('#names').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#department').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#designation').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#macadd').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#system').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#others').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#email').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#phone').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#system').tooltip({title: "Please select item in the list👍", placement:"top",  trigger: "hover"});
$('#others').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#facultys').tooltip({title: "Please fill out this field👍", placement:"top",  trigger: "hover"});
$('#date').tooltip({title: "Enter current date👍", placement:"top",  trigger: "hover"});
$('#upload').tooltip({title: "Submit image file('png','jpg','jpg')👍", placement:"top",  trigger: "hover"});

$("input[type='file']").click(function () {
    $("input[id='upload']").click();
});
 $("input[id='upload']").change(function (e) {
     var $this = $(this);
     $this.next().html($this.val().split('\\').pop());
});