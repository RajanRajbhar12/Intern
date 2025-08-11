
function saveUser() {
   
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    fetch('http://localhost:8000/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        alert('User saved successfully!');
       
    })
   
}


function checkUser() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
   
    if (!email || !password) {
        alert('Please fill both email and password');
        return;
    }
    
 
    fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Login successful!');
          
        } else {
            alert('Wrong email or password!');
        }
    })
    .catch(error => {
        alert('Something went wrong!');
        console.log('Error:', error);
    });
}

function add() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;

    fetch('http://localhost:8000/calc/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ num1: num1, num2: num2 })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('result').textContent = "Result: " + data.result;
    })
    
}


function sub(){
    const num1=document.getElementById('num1').value;
    const num2=document.getElementById('num2').value;
    fetch('http://localhost:8000/calc/sub',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify({num1:num1,num2:num2})
    })
    .then(response=>response.json())
    .then(data =>{
        document.getElementById('result').textContent="Result:"+data.result;
    })
}

function div(){
    const num1=document.getElementById('num1').value;
    const num2=document.getElementById('num2').value;
    fetch('http://localhost:8000/calc/div',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify({num1:num1,num2:num2})
    })
    .then(response=>response.json())
    .then(data =>{
        document.getElementById('result').textContent="Result:"+data.result;
    })
}
function mul(){
    const num1=document.getElementById('num1').value;
    const num2=document.getElementById('num2').value;
    fetch('http://localhost:8000/calc/mul',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify({num1:num1,num2:num2})
    })
    .then(response=>response.json())
    .then(data =>{
        document.getElementById('result').textContent="Result:"+data.result;
    })
}
