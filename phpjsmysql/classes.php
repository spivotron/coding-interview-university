<?php
  $object = new User;
  print_r($object);
  // print_r makes it human readable

  /**
   *
   */
  class User
  {
    public $name, $password;
    function save_user() {
      echo "save user goes here";
    }
  }


?>
