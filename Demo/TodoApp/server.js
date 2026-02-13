const express = require('express');
const app = express();
const path = require('path');

app.use(express.json());
app.use(express.static('public'));

let todos = [
  { id: 1, text: 'Học về Gemini Subagents', completed: false },
  { id: 2, text: 'Xây dựng Software Team Demo', completed: true }
];

// API: Lấy danh sách todos
app.get('/api/todos', (req, res) => {
  res.json(todos);
});

// API: Thêm todo mới
app.post('/api/todos', (req, res) => {
  const newTodo = {
    id: Date.now(),
    text: req.body.text,
    completed: false
  };
  todos.push(newTodo);
  res.status(201).json(newTodo);
});

// API: Xóa todo
app.delete('/api/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  todos = todos.filter(t => t.id !== id);
  res.status(204).send();
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
