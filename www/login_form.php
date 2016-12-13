
<div class = "container">

 <h2>Enter Username and Password</h2> 
 <form class = "form-signin" role = "form" 
    action = "<?php echo htmlspecialchars($_SERVER['PHP_SELF']); 
    ?>" method = "post">
    <input type = "text" class = "form-control" 
       name = "username" placeholder = "username = user" 
       required autofocus></br>
    <input type = "password" class = "form-control"
       name = "password" placeholder = "password = 1234" required>
    <button class = "btn btn-lg btn-primary btn-block" type = "submit" 
       name = "login">Login</button>
 </form>
		
 
</div> 
