# Alert Message Challenge

Alright, in the last lesson, we looked at the `$_FILES` superglobal and how to upload files. In this lesson, I want you to try out a challenge.

## Challenge

After the form is submitted, display two messages: one for the form submission and one for the file upload. You can display them how you want. Both messages at the top or the submission message at the top and the file upload message near the file field. If the file does not upload, it should also display that message. You should also check to see if the title and description are empty. You can use the `empty()` function. You could color code the messages so that they are green if they are success messages and red if they are error messages.

Also, try and only show the submitted box if all of the tests pass. So you may have to move the `$submitted = true;` inside of the if statement.

This is a pretty difficult challenge if you are new to PHP, so do not be discouraged if you can't quite do it. The point of this is to get you thinking about how you would do this and to get you to try and figure it out. If you can't figure it out, you can look at the solution below. There are so many ways to do this as well, so if you did it differently, that is 100% fine.

## Hints

- You could create an array of messages and then loop through them to display them.
- You could make it an array of arrays and have the first element be the message and the second element be the color/status.

## Solution

I will show you my code and then explain what I did:

```php
<?php
$title = '';
$description = '';
$submitted = false;
$messages = []; // Initialize the messages array

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['submit'])) {
  $title = isset($_POST['title']) ? htmlspecialchars($_POST['title']) : '';
  $description = isset($_POST['description']) ? htmlspecialchars($_POST['description']) : '';

  if (empty($title)) {
    $messages[] = ['text' => 'Title is required', 'color' => 'text-red-500'];
    $submitted = false;
  }

  if (empty($description)) {
    $messages[] = ['text' => 'Description is required', 'color' => 'text-red-500'];
    $submitted = false;
  }

  $file = $_FILES['logo'];

  // Check for upload errors
  if ($file['error'] === UPLOAD_ERR_OK) {
    // Specify the destination directory
    $uploadDir = 'uploads/';

    // Create the directory if it doesn't exist
    if (!is_dir($uploadDir)) {
      mkdir($uploadDir, 0755, true);
    }

    // Create a unique filename
    $filename = uniqid() . '_' . $file['name'];

    // Move the uploaded file to the destination directory
    if (move_uploaded_file($file['tmp_name'], $uploadDir . $filename)) {
      // Add a success message to the array
      $messages[] = ['text' => 'File uploaded successfully!', 'color' => 'text-green-500'];
      // Set the submitted flag to true
      $submitted = true;
    } else {
      $messages[] = ['text' => 'Error uploading file.', 'color' => 'text-red-500'];
    }
  } else {
    $messages[] = ['text' => 'File upload error', 'color' => 'text-red-500'];
  }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Create Job Listing</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100">
  <div class="flex justify-center items-center h-screen">
    <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h1 class="text-2xl font-semibold mb-6">Create Job Listing</h1>
      <!-- Display messages using a loop -->
      <?php foreach ($messages as $message) : ?>
        <p class="<?= $message['color']; ?>"><?= $message['text'] ?></p>
      <?php endforeach; ?>
      <form action="<?= $_SERVER['PHP_SELF']; ?>" method="post" enctype="multipart/form-data">
        <div class="mb-4">
          <label for="title" class="block text-gray-700 font-medium">Title</label>
          <input type="text" id="title" name="title" placeholder="Enter job title" class="w-full px-4 py-2 border rounded focus:ring focus:ring-blue-300 focus:outline-none" value="<?= $title ?>">
        </div>
        <div class="mb-6">
          <label for="description" class="block text-gray-700 font-medium">Description</label>
          <textarea id="description" name="description" placeholder="Enter job description" class="w-full px-4 py-2 border rounded focus:ring focus:ring-blue-300 focus:outline-none"><?= $description ?></textarea>
        </div>
        <div class="mb-4">
          <label for="resume" class="block text-gray-700 font-medium">Logo</label>
          <input type="file" id="logo" name="logo" class="w-full px-4 py-2 border rounded focus:ring focus:ring-blue-300 focus:outline-none">
        </div>
        <div class="flex items-center justify-between">
          <button type="submit" name="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 focus:outline-none">
            Create Listing
          </button>
          <a href="#" class="text-blue-500 hover:underline">Back to Listings</a>
        </div>
      </form>

      <!-- Display submitted data -->
      <?php if ($submitted) : ?>
        <div class="mt-6 p-4 border rounded bg-gray-200">
          <h2 class="text-lg font-semibold">Submitted Job Listing:</h2>
          <p><strong>Title:</strong> <?= $title ?></p>
          <p><strong>Description:</strong> <?= $description ?></p>
        </div>
      <?php endif; ?>
    </div>
  </div>
</body>

</html>
```

- First, I initialize the `$messages` array.
- Then, I add a message to the array if the title or description is empty. A message includes the text and the color.
- Then, I check to see if the file uploaded successfully. If it did, I add a success message to the array. If it did not, I add an error message to the array.
- I moved the `$submitted = true;` inside of the if statement so that it is only set to true if all of the tests pass.
- Then, I loop through the messages array and display the messages.

If you did something different, that is totally fine. There are so many ways to do this. I hope you enjoyed this challenge and I hope you learned something from it.
