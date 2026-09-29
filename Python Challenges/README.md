# 🐍 Python Challenges

A collection of short Python quizzes to test your knowledge, spot tricky behavior, and learn something new along the way.

Each challenge shows a small code snippet. Your job: figure out what it prints (or if it breaks) **before** running it.

---

## How It Works

1. Read the code snippet.
2. Pick your answer (a, b, or c).
3. Click the **Show Answer** dropdown to check yourself.
4. Run the code to see it for yourself.

No cheating, no peeking. 😉

---

## Example Challenge

### Python Challenge #1

```python
x = 9
y = x
x = 7
print(y)
```

**Answers**

- a) 7
- b) 9
- c) Error

<details>
<summary>Show Answer</summary>

**b) 9**

When you write `y = x`, `y` gets the value `9` at that moment. Reassigning `x` to `7` afterward doesn't change `y`, because `y` points to the value `9`, not to the variable `x`.

</details>

---

## Folder Structure

```
quizzes/
├── README.md
├── challenge_01.md
├── challenge_02.md
└── ...
```

Each challenge lives in its own file so it's easy to add, edit, and share.

---

## Challenge Template

Want to add a new quiz? Copy this format:

````markdown
### Python Challenge #N

```python
# your code here
```

**Answers**

- a) ...
- b) ...
- c) ...

<details>
<summary>Show Answer</summary>

**Correct answer: ...**

Short explanation of why.

</details>
````

---

## Contributing

Ideas for new challenges are welcome. To contribute:

1. Fork this repository.
2. Add your challenge using the template above.
3. Make sure the code runs and the answer is correct.
4. Open a pull request.

---

## Topics Covered

- Variables and assignment
- Data types
- Lists, tuples, dictionaries, and sets
- Loops and conditionals
- Functions and scope
- Common gotchas and edge cases

*(More coming soon!)*

---

Happy coding! 🚀
