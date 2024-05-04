<?

class MathematicTools {

    // Declaring a static attribute.
    public static $pi = 3.14;

    public static function add(...$nums) 
    {
        return array_sum($nums);
    }

}

/* Note - No longer accessed by: `$var->pi;` 

    * Calls <Class>::$<property/method>;
        (due to calling from the class itself)
*/

echo MathematicTools::$pi;
echo MathematicTools::add(1, 2, 3, 4, 5);
