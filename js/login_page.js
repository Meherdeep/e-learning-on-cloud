var $loginMsg = $('.loginMsg'),
  $login = $('.login'),
  $signupMsg = $('.signupMsg'),
  $signup = $('.signup'),
  $frontbox = $('.frontbox');

$('#switch1').on('click', function() {
  $loginMsg.toggleClass("visibility");
  $frontbox.addClass("moving");
  $signupMsg.toggleClass("visibility");

  $signup.toggleClass('hide');
  $login.toggleClass('hide');
})

$('#switch2').on('click', function() {
  $loginMsg.toggleClass("visibility");
  $frontbox.removeClass("moving");
  $signupMsg.toggleClass("visibility");

  $signup.toggleClass('hide');
  $login.toggleClass('hide');
})

setTimeout(function(){
  $('#switch1').click()
},1000)

setTimeout(function(){
  $('#switch2').click()
},3000)

function login() {
    console.log('login enter');
    var email = document.getElementsByName('email')[0].value;
    var pass = document.getElementsByName('password')[0].value;

    request = new XMLHttpRequest();
    var req_url = 'http://localhost:5000/login?email=' + email + '&pass=' + pass;
    // console.log(req_url);
    //const redirectUrl = getQueryStringValue('redirect') || SERVER_URL;
    //const auth = new AuthHandler(SERVER_URL);

    request.open('GET', req_url, true);
    request.onload = function () {
      var data = this.response;
      console.log(data);

    if(data !== 'Bad'){
        window.location.href = './welcome';
        sessionStorage.setItem('uname', email);
        sessionStorage.setItem('fullname', data);
        console.log(data);
    }
    else{
        window.location.href = './login';
    }
    }
  request.send();
}
function signup() {
    console.log('signup enter');
    var name = document.getElementsByName('fullname')[0].value;
    var email = document.getElementsByName('email')[1].value;
    var pass = document.getElementsByName('password')[1].value;

    var request = new XMLHttpRequest();
    var req_url = 'http://localhost:5000/register?email=' + email + '&pass=' + pass + '&name=' + name;
    // console.log(req_url);
    request.open('GET', req_url, true);
    request.onload = function () {
        var data = this.response;
        console.log(data);
        window.location.href = './login';
    }
  request.send();
}