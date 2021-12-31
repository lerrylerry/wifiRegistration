function display(){
    var firstname1 = document.getElementById("first").value;
    var middlename1 = document.getElementById("second").value;
    var lastname1 = document.getElementById("third").value;
    var department1 = document.getElementById("department").value;
    var designation1 = document.getElementById("designation").value;
    var macaddress1 = document.getElementById("macaddress").value;
    var emailadd1 = document.getElementById("emailadd").value;
    var phoneno1 = document.getElementById("phoneno").value;
    var others1 = document.getElementById("others").value;
    var system1 = document.getElementById("system").value;




    document.writeln("The First Name " + firstname1 + "<br>")
    document.writeln("The Middle Name " + middlename1 + "<br>")
    document.writeln("The Last Name " + lastname1 + "<br>")
    document.writeln("The Department " + department1 + "<br>")
    document.writeln("The Designation " + designation1 + "<br>")
    document.writeln("The Mac Address " + macaddress1 + "<br>")
    document.writeln("The Email Address " + emailadd1 + "<br>")
    document.writeln("The Phone Number " + phoneno1 + "<br>")
    document.writeln("The Others " + others1 + "<br>")
    document.writeln("The Combobox " + system1)
}