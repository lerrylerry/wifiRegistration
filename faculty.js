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

    if(!fname.match(regex)){
        document.getElementById("first").addEventListener(invalid("first"));
        return false;

    }else{
        document.getElementById("first").addEventListener(empty("first"));
        return true;
    }
    
}

// Middle Name
function nameLength2(){
    var fname = document.getElementById("second").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!fname.match(regex)){
        document.getElementById("second").addEventListener(invalid("second"));
        return false;

    }else{
        document.getElementById("second").addEventListener(empty("second"));
        return true;
    }
    
}

// Last Name
function nameLength3(){
    var fname = document.getElementById("third").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!fname.match(regex)){
        document.getElementById("third").addEventListener(invalid("third"));
        return false;

    }else{
        document.getElementById("third").addEventListener(empty("third"));
        return true;
    }
    
}

// Department
function dept(){
    var fname = document.getElementById("department").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!fname.match(regex)){
        document.getElementById("department").addEventListener(invalid("department"));
        return false;

    }else{
        document.getElementById("department").addEventListener(empty("department"));
        return true;
    }
    
}

// Designation
function design(){
    var fname = document.getElementById("designation").value;
    var regex = /^[a-z][a-z\s]*$/;

    if(!fname.match(regex)){
        document.getElementById("designation").addEventListener(invalid("designation"));
        return false;

    }else{
        document.getElementById("designation").addEventListener(empty("designation"));
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

// gmail
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

// date
function times(){
    let currentDate = new Date();
    let cDay = currentDate.getDate();
    let cMonth = currentDate.getMonth() + 1;
    let cYear = currentDate.getFullYear();
    var tdate = cYear + "-" + "0" + cMonth + "-" + "0" + cDay;
    const date1 = document.getElementById("date");

    if (date1.value != tdate)
    {
        document.getElementById("date").addEventListener(invalid("date"))
        return false;
    }
        document.getElementById("date").addEventListener(valid("date"))
        return true;
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

// Confirm Form Submission