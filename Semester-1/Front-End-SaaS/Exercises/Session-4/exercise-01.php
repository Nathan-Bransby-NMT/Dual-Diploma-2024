<<<<<<< HEAD
<?php
/**
 * Session 04 - Practice Exercise 1
 *
 * Problem Description
 *
 * Author:      Student Name <student email>
 * Version:     0.0
 *
 * Within this file you will find a number of TO DO statements
 * that will describe what needs to be completed in this exercise.
 *
 * Follow the instructions carefully.
 *
 */

// TODO:  1 Create a variable called phonetic.
$phonetic = NULL;
// TODO:  2 Add the Radio Phonetic alphabet to this variable as an
//        array of values
$phonetic = [Range('A', 'Z')];

// TODO:  3 Create a variable called symbols.
$symbols = NULL;

// TODO:  4 Add the symbols !@#$%^&<>? and a space as an array of values
$symbols = ['! ', '...'];

// TODO:  5 Create a new variable called password, and make sure it is empty
$password = NULL;

// TODO:  6 Create two new variables, word1 and word2 and make them empty
$word1 = $word2 = NULL;

// TODO:  7 Create two more variables, symbol1 and symbol2 and make them empty
$symbol1 = $symbol2 = NULL;

// TODO:  8 Use the mt_rand function to select a word from the phonetic
//          array, and store in word1
$word1 = $phonetic[mt_rand(0, count($phonetic))]

// TODO:  9 Use the mt_rand function to select a word from the phonetic
//          array, and store in word2

// TODO: 10 Use the mt_rand function to select a symbol from the symbols array,
//          and store in symbol1

// TODO: 11 Use the mt_rand function to select a word from the symbols array, and
//          store in symbol2

// TODO: 12 Use these four parts to create a new password in the form:
//          symbol1 word1 word2 symbol2

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- TODO: 13 make the title: Session 04 -->
    <title>TITLE GOES HERE</title>
</head>

<body class="bg-gray-100 flex flex-col min-h-screen">
<header class="bg-gray-800 text-white p-4">
    <div class="container mx-auto flex flex-row justify-between">
        <h1 class="text-3xl font-semibold">YOUR NAME GOES HERE</h1>
        <!-- TODO: 14 make the Topic "Exercise 01" -->
        <h2 class="text-2xl">TOPIC: Subtopic</h2>
    </div>
</header>
<main class="container mx-auto p-4 mt-4 gap-4 flex flex-col">
    <article class="bg-white rounded-lg shadow-md shadow-gray-500/20 p-6">
        <header>
        <!-- TODO: 15 make the heading "Password Maker" -->
            <h2 class="text-2xl font-semibold mb-4">OUTPUT HEADING</h2>
        </header>
        <section>
            <?php
            // TODO: Using a suitable method...
            // TODO: 16 Output the password in a <p>aragraph</p>
            // TODO: 17 Add the class 'text-xl' to the pargraph

            ?>
        </section>
    </article>

</main>
<footer class="bg-gray-900 text-gray-500 mt-auto h-auto py-8 px-8 mt-8 w-full">
    <section class="container mx-auto flex flex-row flex-wrap justify-between">
        <div class="w-1/2">
            <p>
                &copy; Copyright 2024 YOUR NAME HERE, All rights Reserved
            </p>
        </div>
        <div class="w-1/2">
            <p class="text-sm">
                Before using any content on this page, and any associated pages, files or other materials, must be
                sought from the author. Once permission is provided to use said content, a notice must be appended to
                your page stating "Used with permission from <strong>MY NAME HERE</strong>. Original located at <a
                        href="#HTTP_LINK_TO_SOURCE">HTTP_LINK_TO_SOURCE</a>." with a link to the source.
            </p>
        </div>
    </section>
</body>
<!-- TODO: 18 Test your solution. -->
<!-- TODO: 19 Resolve any errors, if they exist. -->
<!-- TODO: 20 Remove the comment from the top of the document that starts
            * Within this file you ...
           and ends with
            * and save your work.
-->
<!-- TODO: 21 Update the version to 1.0 -->
<!-- TODO: Finally remove all TODO comments from the code. -->
</html>
=======
<?php
/**
 * Session 04 - Practice Exercise 1
 *
 * Problem Description
 *
 * Author:      Student Name <student email>
 * Version:     0.0
 *
 * Within this file you will find a number of TO DO statements
 * that will describe what needs to be completed in this exercise.
 *
 * Follow the instructions carefully.
 *
 */

// TODO:  1 Create a variable called phonetic.
$phonetic = NULL;
// TODO:  2 Add the Radio Phonetic alphabet to this variable as an
//        array of values
$phonetic = [Range('A', 'Z')];

// TODO:  3 Create a variable called symbols.
$symbols = NULL;

// TODO:  4 Add the symbols !@#$%^&<>? and a space as an array of values
$symbols = ['! ', '...'];

// TODO:  5 Create a new variable called password, and make sure it is empty
$password = NULL;

// TODO:  6 Create two new variables, word1 and word2 and make them empty
$word1 = $word2 = NULL;

// TODO:  7 Create two more variables, symbol1 and symbol2 and make them empty
$symbol1 = $symbol2 = NULL;

// TODO:  8 Use the mt_rand function to select a word from the phonetic
//          array, and store in word1
$word1 = $phonetic[mt_rand(0, count($phonetic))]

// TODO:  9 Use the mt_rand function to select a word from the phonetic
//          array, and store in word2

// TODO: 10 Use the mt_rand function to select a symbol from the symbols array,
//          and store in symbol1

// TODO: 11 Use the mt_rand function to select a word from the symbols array, and
//          store in symbol2

// TODO: 12 Use these four parts to create a new password in the form:
//          symbol1 word1 word2 symbol2

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- TODO: 13 make the title: Session 04 -->
    <title>TITLE GOES HERE</title>
</head>

<body class="bg-gray-100 flex flex-col min-h-screen">
<header class="bg-gray-800 text-white p-4">
    <div class="container mx-auto flex flex-row justify-between">
        <h1 class="text-3xl font-semibold">YOUR NAME GOES HERE</h1>
        <!-- TODO: 14 make the Topic "Exercise 01" -->
        <h2 class="text-2xl">TOPIC: Subtopic</h2>
    </div>
</header>
<main class="container mx-auto p-4 mt-4 gap-4 flex flex-col">
    <article class="bg-white rounded-lg shadow-md shadow-gray-500/20 p-6">
        <header>
        <!-- TODO: 15 make the heading "Password Maker" -->
            <h2 class="text-2xl font-semibold mb-4">OUTPUT HEADING</h2>
        </header>
        <section>
            <?php
            // TODO: Using a suitable method...
            // TODO: 16 Output the password in a <p>aragraph</p>
            // TODO: 17 Add the class 'text-xl' to the pargraph

            ?>
        </section>
    </article>

</main>
<footer class="bg-gray-900 text-gray-500 mt-auto h-auto py-8 px-8 mt-8 w-full">
    <section class="container mx-auto flex flex-row flex-wrap justify-between">
        <div class="w-1/2">
            <p>
                &copy; Copyright 2024 YOUR NAME HERE, All rights Reserved
            </p>
        </div>
        <div class="w-1/2">
            <p class="text-sm">
                Before using any content on this page, and any associated pages, files or other materials, must be
                sought from the author. Once permission is provided to use said content, a notice must be appended to
                your page stating "Used with permission from <strong>MY NAME HERE</strong>. Original located at <a
                        href="#HTTP_LINK_TO_SOURCE">HTTP_LINK_TO_SOURCE</a>." with a link to the source.
            </p>
        </div>
    </section>
</body>
<!-- TODO: 18 Test your solution. -->
<!-- TODO: 19 Resolve any errors, if they exist. -->
<!-- TODO: 20 Remove the comment from the top of the document that starts
            * Within this file you ...
           and ends with
            * and save your work.
-->
<!-- TODO: 21 Update the version to 1.0 -->
<!-- TODO: Finally remove all TODO comments from the code. -->
</html>
>>>>>>> 63d1fc3979b4aa9218d141eedd12d7d0c9ec49f0
