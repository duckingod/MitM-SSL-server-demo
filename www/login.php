<?php
   ob_start();
   session_start();
?>

<?
   error_reporting(E_ALL);
   ini_set("display_errors", 1);
?>

<html lang = "en">
   
   <head>
      <title>Weak website QAQ</title>
      <link href = "css/bootstrap.min.css" rel = "stylesheet">
      <style> @import "style.css"; </style>
      
   </head>
	
   <body>
      
	<div class="login-page">
      <div class = "container form">
         <?php
            $msg = '';
            if (isset($_POST['login']) && !empty($_POST['username']) 
               && !empty($_POST['password'])) {
               if ($_POST['username'] == 'user' && 
                  $_POST['password'] == '1234') {
                  $_SESSION['valid'] = true;
                  $_SESSION['timeout'] = time();
                  $_SESSION['username'] = 'user';
               }else {
                  $msg = 'Wrong username or password';
               }
            }
	    if (isset($_SESSION['username']) && $_SESSION['username']!='')
                $msg = 'Welcome! ' . $_SESSION['username'];
        ?>
	<h4 class = "message"><?php echo $msg; ?></h4>
	<?php
		if (isset($_SESSION['username']) && $_SESSION['username']!='') {
			echo '<a href = "logout.php" tite = "Logout">Logout</a>';
		} else {
			include "login_form.php";
		}
	?>
      </div> <!-- /container -->
	</div>
   </body>
</html>
