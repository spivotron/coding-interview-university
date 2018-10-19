<?php
  $object = new User;
  print_r($object);

  $object->name= "Henry";
  $object->password = "1234";
  print_r($object);
  $object->save_user();
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


  // cloning objects
  $object1 = new User();
  $object1->name = "Henry";
  $object2 = clone $object1;
  $object2->name = "William";

  echo "object 1 name = ". $object1->name . "\n";
  echo "object 2 name = ". $object2->name . "\n";

  // Constructors
  class newUser {
    public $username, $password;
    function __construct() {
      $this->username = "Guest";
    }

    // Destructors: Release resources by cleaning up
    function __destruct() {

    }

    function get_password() {
      return $this->password;
    }

    function set_password($pass) {
      $this->password = $pass;
    }

  }

  $newUserTest = new newUser();
  print_r($newUserTest->get_password());
  $newUserTest->set_password("hayyyy");
  print_r($newUserTest->get_password());

  Translate::lookup();
  class Translate {
    const ENGLISH = 0;
    const SPANISH = 1;
    const FRENCH  = 2;
    const GERMAN  = 3;

    static function lookup() {
      echo self::SPANISH;
    }
  }



  class Example {
    var $name = "Henry"; // same as public but deprecated
    public $age = 24;
    protected $usercount; // outside code won't have access to this but extending classes should inherit it
    private function admin() {
      // admin code goes here
    }


  }

  // Static methods
  // A static method has no access to any object properties


  class StaticUser {
    static function pwd_string() {
      echo "Please enter your password";
    }
  }
  StaticUser::pwd_string();
  // Static properties
  // Interesting becuase they store data about the whole class, not a particular object of that class
  // cannot be directly accessed within an instance of the class
  $temp = new Test();

  class Test {
    static $static_prop = "I'm static";

    static function get_sp() {
      return self::$static_prop;
    }
  }

  echo "Test A: " . Test::$static_prop . "\n";
  echo "Test A.5: " . Test::get_sp()        . "\n";
  echo "Test B: " . $temp->get_sp()        . "\n";
  echo "Test C: " . $temp->static_prop . "\n"; // won't work because $temp is an object


  // inheritance
  class Subscriber extends newUser {
      public $phone, $email;
      function display() {
        echo "Name:  " . $this->name     . "\n";
        echo "Pass:  " . $this->password . "\n";
        echo "Phone: " . $this->phone    . "\n";
        echo "Email: " . $this->email;
      }
  }


  $object           = new Subscriber;
  $object->name     = "Fred";
  $object->password = "pword";
  $object->phone    = "012 345 6789";
  $object->email    = "fred@bloggs.com";
  $object->display();


  // subclass constructors
  $object = new Tiger();
  echo "Tigers have...\n";
  echo "Fur: " . $object->fur . "\n";
  echo "Stripes: " . $object->stripes;

  class Wildcat {
    public $fur;
    function __construct() {
      $this->fur = "TRUE";
    }
  }

  class Tiger extends Wildcat {
    public $stripes;
    function __construct() {
      parent::__construct();
      $this->stripes = "TRUE";
    }
  }

  // Singleton
  // class Singleton {
  //   private static $instance = null;
  //
  //   private function __construct() {
  //     // private constructor prevents the direct creation of objects from the class
  //     // stuff
  //   }
  //
  //   public static function getInstance() {
  //     if (self::instance == null){
  //       self::instance = new Singleton();
  //     }
  //     return self::instance;
  //   }
  // }

    // DB Connection Singleton
    class ConnectDB {
      private static $instance=  null;
      private $conn;

      private $host = 'localhost';
      private $user = 'root';
      private $pass= 'root';
      private $name = 'vexata';

      private function __construct() {
        $this->conn = new PDO("mysql: host={$this->host};dbname={$this->name}", $this->user, $this->pass, array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES 'utf8'"));

      }

      public static function getInstance() {
        if (!self::$instance) {
          self::$instance = new ConnectDB();
        }
        return self::instance;
      }

      public function getConnection() {
        return $this->conn;
      }

    }


    $instance = ConnectDb::getInstance();
    $conn = $instance->getConnection();
    var_dump($conn);


    class Automobile {
      private $vehicleMake;
      private $vehicleModel;

      public function __construct($make, $model) {
        $this->vehicleMake = $make;
        $this->vehicleModel = $model;
      }

      public function getMakeAndModel() {
        return $this->vehicleMake . ' ' . $this->vehicleModel;
      }

    }

    class AutomobileFactory {
      public static function create($make, $model) {
        return new Automobile($make, $model);
      }
    }

    $veyron = AutomobileFactory::create('Bugatti', 'Veyron');
    print_r($veyron->getMakeAndModel())



?>
