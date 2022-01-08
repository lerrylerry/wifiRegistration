// valid
function valid(add){
    document.getElementById(add).style.color = "whitesmoke";
    document.getElementById(add).style.borderColor = "green";
    document.getElementById(add).style.backgroundColor = "black";
    document.getElementById(add).style.fontFamily = "cursive";
    document.getElementById(add).style.fontWeight = "bold";
}

// invalid
function invalid(add){
    document.getElementById(add).style.borderColor = "red";
    document.getElementById(add).style.backgroundColor = "black";
}

// empty field
function empty(add){
    var check = document.getElementById(add).value;

    if (check.length == 0 || check.length < 3 || check == ""){
        document.getElementById(add).addEventListener(invalid(add));
        
    }else{
        document.getElementById(add).addEventListener(valid(add));
    }
        
}

// First Name
function nameLength(){
    var fname = document.getElementById("first").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!fname.match(regex) || fname.length < 3){
        document.getElementById("first").addEventListener(invalid("first"));
        return false;

    }else{
        document.getElementById("first").addEventListener(valid("first"));
        return true;
    }
    
}

// Middle Name
function nameLength2(){
    var mname = document.getElementById("second").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!mname.match(regex) || mname.length < 3){
        document.getElementById("second").addEventListener(invalid("second"));
        return false;

    }else{
        document.getElementById("second").addEventListener(valid("second"));
        return true;
    }
    
}

// Last Name
function nameLength3(){
    var lname = document.getElementById("third").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!lname.match(regex) || lname.length < 3){
        document.getElementById("third").addEventListener(invalid("third"));
        return false;

    }else{
        document.getElementById("third").addEventListener(valid("third"));
        return true;
    }
    
}

// Semester
function sem(){
    var x = document.getElementById("semester").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!x.match(regex) || x.length < 3){
        document.getElementById("semester").addEventListener(invalid("semester"));
        return false;

    }else{
        document.getElementById("semester").addEventListener(valid("semester"));
        return true;
    }
    
}

// course
function course(){
    var x = document.getElementById("course").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!x.match(regex)){
        document.getElementById("course").addEventListener(invalid("course"));
        return false;

    }else{
        document.getElementById("course").addEventListener(valid("course"));
        return true;
    }
    
}

// mac address
function mac(){
    var x = document.getElementById("macaddress").value;
	var pattern = /^([0-9a-f]{2}([:-]|$)){6}$|([0-9a-f]{4}([.]|$)){3}$/i;
	
	if (pattern.test(x)){
        document.getElementById("macaddress").addEventListener(valid("macaddress"));
        return true;
	}
	else{
		document.getElementById("macaddress").addEventListener(invalid("macaddress"));
        return false;
	}
}

// tupc-id
function tupcnum(){
    var x = document.getElementById("studentno").value;
    var regex = /[T][U][P][C]-[0-9]{2}-[0-9]{4}/;

    if(x.match(regex)){
        document.getElementById("studentno").addEventListener(valid("studentno"));
        return true;

    }
        document.getElementById("studentno").addEventListener(invalid("studentno"));
        return false;
}

// unfinished
function autoTextgmail(){
    var x = document.getElementById("emailadd").value;
    var search = /\b@gsfe.tupcavite.edu.ph\b/g;
    var y = x.match(search);

    alert(x);
    alert("Found Text/s: " + y);

    if (y.length != 0 || y.length <= 22){

        alert("too short gmail");
        return false;
    }
        alert("Correct");
        return true;
    
}

// Specify, Others
function Specify(){
    var x = document.getElementById("others").value;
    let pattern = /[a-zA-z]/g; 
    let result = x.match(pattern);

    if (result.length < 3)
    {
        document.getElementById("others").addEventListener(invalid("others"))
        return false;        

    }
        document.getElementById("others").addEventListener(valid("others"))
        return true;
    
}

// email address
function ValidateEmail(){
    var mail = document.getElementById("emailadd").value;
    var regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    
    if (mail.match(regex)){
        document.getElementById("emailadd").addEventListener(valid("emailadd"));
        return true;
    }
        document.getElementById("emailadd").addEventListener(invalid("emailadd"));
        return false;
}

// cellphone number
function cellNo(){
    var x = document.getElementById("phoneno").value;
    var regex = /[0][9][0-9]{9}/g;

    if (x.match(regex)){
        document.getElementById("phoneno").addEventListener(valid("phoneno"));
        return true;

    }
        document.getElementById("phoneno").addEventListener(invalid("phoneno"));
        return false;
}

// Faculty Name
function facname(){
    var fname = document.getElementById("faculty").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!fname.match(regex)){
        document.getElementById("faculty").addEventListener(invalid("faculty"));
        return false;

    }else{
        document.getElementById("faculty").addEventListener(empty("faculty"));
        return true;
    }
    
}

// Only letters
function restrictAlphabets(e){
    var x = e.which || e.keycode;
    if((x>=48 && x<=57))
        return true;
    else
        return false;
}

// only alphabets
function onlyAlphabets(e){
    var x = e.which || e.keycode;
    if((x>=65 && x<=90)||(x>=97 && x<=122))
        return true;
    else
        return false;
}

// system/device
function device(){
    var x = document.getElementById("system").value;
    var g = document.getElementById("others");

    if (x == "Smartphone" || x == "Laptop" || x == "Tablet" || x == "PC" || x == "Desktop"){
        g.value = "";
        document.getElementById("others").style.borderStyle = "solid";
        document.getElementById("others").style.borderWidth = "3px";
        document.getElementById("others").style.borderColor = "blue";
        document.getElementById("others").style.padding = "5px";
        document.getElementById("others").style.backgroundColor = "whitesmoke";
        document.getElementById("others").disabled = "true";
        document.getElementById("system").addEventListener(valid("system"));
        

    }if (x == "Others"){
        document.getElementById("others").disabled = "";
        document.getElementById("system").addEventListener(valid("system"));
        
    }if (x == ""){
        g.value = "";
        document.getElementById("others").disabled = "true";   
    }

}

// checkbox
function agreed(){
    if(document.getElementById("agree").checked == true){
        return true;
    }
        return false;   
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

// home address
function home(){
    var x = document.getElementById("residenceAdd").value;

    if (x.length == 0 || x.length < 20 || x.length == ""){
        document.getElementById("residenceAdd").addEventListener(invalid("residenceAdd"));
        return false;
    }
        document.getElementById("residenceAdd").addEventListener(valid("residenceAdd"));
        return true;
}

// OR
function OR(){
    var x = document.getElementById("orno").value;

    if (x.length < 6){
        document.getElementById("orno").addEventListener(invalid("orno"));
        return false;
    }
        document.getElementById("orno").addEventListener(valid("orno"));
        return true;
}

// uname
function uname(){
    var x = document.getElementById("name").value;

    if (x.length < 6){
        document.getElementById("name").addEventListener(invalid("name"));
        return false;
    }
        document.getElementById("name").addEventListener(valid("name"));
        return true;
}

// upass
function upass(){
    var x = document.getElementById("password").value;

    if (x.length < 6){
        document.getElementById("password").addEventListener(invalid("password"));
        return false;
    }
        document.getElementById("password").addEventListener(valid("password"));
        return true;
}

// Confirm Form Submission
