<?
  echo "a: [". TRUE . "]"; // 1
  echo "b: [". FALSE . "]";  // null

  echo strrev("Henry Spivey");
  echo str_repeat("Hip ", 2);
  echo strtoupper("hooray");

  // variable variable
  $varname = 'tireqty';
  $$varname = 5;
  // is the same as $tireqty = 5

  class sampleClass{};

  $myObj= new sampleClass();
  if ($myObj instanceof sampleClass)
    echo "true";

?>

functions that check each type like is_array, is_object or is_bool
is_null, resource (returned by database connections), callable (functions passed to other functions)


isset($var)
takes a variable name as an argument and returns true if it exists and false otherwise.

unset($var)
gets rid of the variable it is passed.

empty($var)
checks to see whether a variable exists and has a nonempty, nonzero value

reinterpreting variables
int intval(mixed var[, int base=10])

float floatval(mixed var)

string strval(mixed var)


gettype and settype
string gettype(mixed var); // returns bool, int, double (for floats, confusingly, for historical reasons), string, array, object, resource, or NULL.

bool settype(mixed var, string type);

A rarely used identity operator, which consists of three equals signs in a row, can be used to compare items without doing conversion.
What is implicit casting? conversion of one type of variable to another

$_REQUEST (array) contains the submitted form's variables
replacing a variable with its contents within a string is known as interpolation
Global variables declared in a script are visible throughout that script, but not inside functions.

post vs pre increment
$a++ vs ++$a
preincrement updates the variable and returns it
post increment returns the varialbe then updates it


reference operator - &
a reference is like an alias
$a = 5;
$b = &$a;
$a = 7; // both a and b are 7 because a and b point to the same piece of memory

type operator
use instanceof


include statement -- fetches a particular file and loads all its contents
include_once -- ignores subsequent requests to include the file

encapsulation -- writing a class in a way that only its methods can be used to manipulate its properties
