# Session 2 - PEST Revision

- PEST is a framework built for Laravel with a focus on functional style and simplicity.

- creates a `pest.php` file

- dont need name spaces in pest PHP

Example test with PEST

```php
test('string', function() {
    $this->assertTru(true);
});
```

---

Pest has no classes, so how can we set shared properties across tests. How can we execute code before or after each test in a file? That's where Pest's lifecycle hooks come in handy! Let's take a look at using them in our project.

One killer Pest feature is the Expectation API. It's fluent, powerful and extensible. Let's use it to add some checks to our tests and compare it with something you may already be familiar with: assertions. As a bonus, we'll also look at adding helper functions in our Pest.php file to smooth out logging a test user into the application.

So, you've seen expectations. But you ain't seen nothing yet. Let's revisit the same test from the last episode and add some magic. We'll look at creating our very own expectation by extending the Expectation API. Then, I'll introduce you to Higher Order Expectations, which can make testing Eloquent models a breeze!

What if you want to run the same test with variations of data? Do you need to copy and paste the entire contents of the test each time? Not at all! Let's look at datasets, a super sleek way to repeat tests and catch edge cases in your application logic.

A basic dataset will get you there 90% of the time, but occasionally you'll need a little extra power. What if we want to combine two or more different arrays of data to create a single dataset with every possible iteration? Let's take a look at combined datasets, which do all of the hard work for us.

One really cool feature of Pest PHP is supplementing a test by chaining methods onto the end of it. Let's take a look at three such methods: group, throws and skip. We'll discuss what problem each method solves and how using those methods fits into running your test suite as a whole.

As your test suite grows, you'll want feedback on where you can improve and you'll want to ensure your tests continue to run quickly so that you can push new features out fast. Let's take a look at how Pest's gorgeous coverage output helps you see where you might need to add more tests and look at how Pest's first party parallel plugin can greatly speed up the time it takes to execute your test suite.

The Arch plug-in is brand new for v2. Rather than testing how your code works, it tests how your code is written. The amazing thing is that it uses the exact same syntax you're used to for writing any other Pest test!

You can now override built-in expectations to test custom use-cases. That might sound confusing at first, so let's break it down with a couple of real-world examples. It's a power feature to be sure, but a useful one!
