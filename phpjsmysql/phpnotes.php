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


include statement -- attempts to load a particular file and loads all its contents. Program execution continues if the file isn't found.
include_once -- ignores subsequent requests to include the file
Require -- fetches the file because it is necessary

encapsulation -- writing a class in a way that only its methods can be used to manipulate its properties



difference between public, protected and private
public: can be referenced anywhere, incuding by other classes and instances of the object
protected: referenced only by the objects class methods and those of any subclasses
private: referenced only by methods within the same class


static methods
called on a class, not on an object


Recap of Variable Scope

Local variables are accessible just from the part of your code where you define them. If they’re outside of a function, they can be accessed by all code outside of functions, classes, and so on. If a variable is inside a function, only that function can access the variable, and its value is lost when the function returns.

Global variables are accessible from all parts of your code.

Static variables are accessible only within the function that declared them but retain their value over multiple calls.


PHP sessions
Either creates or resumes a session based on an identifier that is sent to hte server via a GET or POST request or a Cookie.  The most common use case is when
a website won't let you comment or post without first prompiting a login.  How does it know? One way would be to place a cookie in the users browser and on
every request, the cookie is sent to the server where PHP can be used to determine what gets shown to the user.  Session_start() saves session data in files by default
but it is possible to save sessions in the databse

How are classes loaded in PHP?
Make use of autoloading
Whenever a class is instantiated a function is triggered.

Design Patterns
Singleton and Factory
A singleton pattern ensures that you always get back the same instance of whatever type you are retrieving, whereas the factory pattern generally gives you a different instance of each type.

The purpose of the singleton is where you want all calls to go through the same instance. An example of this might be a class that manages a disk cache, or gets data from a static dictionary; wherever it is important only one known instance interacts with the resource. This does make it less scalable.

The purpose of the factory is to create and return new instances. Often, these won't actually be the same type at all, but they will be implementations of the same base class. However, there may be many instances of each type

Difference between classes and interfaces
interface is a class without all the business logic.  in an interface all methods must be public and multiple inheritance is supported
all methods must be defined within the class that inherits them

Abstract classes can be declared with public and can define properties or variables
Abstract classes don't support multiple inheritance and be extended by only one abstract class .


$x = 2
$y = 4
$z = 6


if($z > $y > $x) {
    echo “true”;
}else{
    echo “false”;
}

prints false because $z > $y returns 1

Arrays

$paper = array('Copier', 'Inkjet', 'Laser', 'Photo');
$j = 0;
foreach($paper as $item) {
  echo "$j: $item<br>";
  ++$j;
}


Associative Arrays
$paper = array('copier' => "Copier & Multipurpose",
               'inkjet' => "Inkjet Printer",
               'laser' => "Laser Printer",
               'photo' => "Photographic Paper");
foreach($paper as $item => $description) {
  echo "$item: $description";
}

Using Explode
$temp = explode(' ', "This is a sentence with seven words");
print_r($temp);


Using Compact
create an array from variables and their values
$fname         = "Doctor";
$sname         = "Who";
$planet        = "Gallifrey";
$system        = "Gridlock";
$constellation = "Kasterborous";

$contact = compact('fname', 'sname', 'planet', 'system', 'constellation');

print_r($contact);

Compact plus Explode
$j       = 23;
$temp    = "Hello";
$address = "1 Old Street";
$age     = 61;

print_r(compact(explode(' ', 'j temp address age')));


Opening files
$fh = fopen('testfile.txt', 'w') or die('Failed to create file');
$text = <<<_END
LINE 1
Line 2
Line tres
_END;

fwrite($fh, $text) or die('Could not write to file');
fclose($fh);
echo "File 'testfile.txt' written succesfully";

Reading from files
$fh = fopen('textfile.txt', 'r') or die('File I/O error');
$line = fgets($fh);
fclose($fh);
echo $line; // LINE 1

Using fread
$fh = fopen('textfile.txt', 'r') or die('File I/O error');
$text = fread($fh, 3); // reads 3 characters
fclose($fh);
echo $text; // LIN

Reading an entire file
use file_get_contents
echo file_get_contents("testfile.txt")

// uploading a file
echo <<<_END
   <html><head><title>PHP Form Upload</title></head><body>
   <form method='post' action='upload.php' enctype='multipart/form-data'>
   Select File: <input type='file' name='filename' size='10'>
   <input type='submit' value='Upload'>
   </form>
_END;

 if ($_FILES)
 {
   $name = $_FILES['filename']['name'];
   move_uploaded_file($_FILES['filename']['tmp_name'], $name);
   echo "Uploaded image '$name'<br><img src='$name'>";
 }

 echo "</body></html>";

 // validation
