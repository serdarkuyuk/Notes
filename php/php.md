php -v
php -S localhost:4000

```php
$characterName = "Serdar";
$characterAge = 58;
echo("hello World serdar");
echo "There once was a man name $characterName <br>";
echo "He was $characterAge years old <br>";
echo strtoupper($characterName);
echo strlen($characterName);
echo $characterName[0];
echo "mike"[0];
$characterName[0] = "T";
echo $characterName;
echo str_replace("Serdar", "kuyuk", $characterName);
echo substr($characterName, 3);
echo substr($characterName, 8, 3);
$num = 10
$num += 10
$num++
$num--
echo abs()
echo pow(2, 4)
echo sqrt()
echo max(), min()
round()
ceil(), floor()


<form action="index.php" method="get">
        Tell your name : <input type"text" name="name">
        <input type="submit">
</form>

    Your name is <?php echo $_GET["name"] ?>
type="number"
type="password"

method="post"  > $_POST["name"]
```
