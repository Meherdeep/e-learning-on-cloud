function certify(){
    var email = sessionStorage.getItem('uname');
    var request = new XMLHttpRequest();
    var req_url = 'http://localhost:5000/uid?email=' + email;
    // console.log(req_url);
    request.open('GET', req_url, true);
    request.onload = function () {
        var uid = this.response;
        var fullname = sessionStorage.getItem('fullname');
        console.log(uid);
        console.log(fullname);
        document.getElementById("uid").innerText = uid;
        document.getElementById("fullname").innerText = fullname;
    }
    request.send();
}
