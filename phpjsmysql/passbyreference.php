<?
  // $names = fix_names("william", "henry");
  // echo $names[0] . " " . $names[1];
  //
  // function fix_names($n1, $n2) {
  //   $n1 = ucfirst(strtolower($n1))
  //   $n2 = ucfirst(strtolower($n2))
  //   return array($n1, $n2);
  // }
  //  OR

  $names = array("william", "henry");
  echo $names[0] . " " . $names[1];
  fix_names($names[0], $names[1]);
  echo $names[0] . " " . $names[1];
  function fix_names(&$n1, &$n2) {
    $n1 = ucfirst(strtolower($n1));
    $n2 = ucfirst(strtolower($n2));

  }



?>
