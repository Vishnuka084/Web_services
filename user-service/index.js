const express = require('express');
const app = express();

app.use(express.json());

app.post('/register', (req, res) => {
  res.json({ message: 'User Registered' });
});

app.listen(3001, () => {
  console.log('User service running on port 3001');
});