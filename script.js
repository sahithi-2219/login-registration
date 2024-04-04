document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // For simplicity, let's just check if the username is 'user' and password is 'password'
    if (username === 'user' && password === 'password') {
        alert('Login successful!');
        window.location.href = 'secured_page.html'; // Redirect to secured page
    } else {
        alert('Invalid username or password. Please try again.');
    }
});
