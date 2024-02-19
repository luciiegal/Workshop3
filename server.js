const express = require('express');
const bodyParser = require('body-parser');
const connectDB = require('./database');
const Product = require('./models/Product');

connectDB();

const app = express();
app.use(bodyParser.json());

// Products Routes
app.get('/products', async (req, res) => {
  const products = await Product.find({});
  res.json(products);
});

app.get('/products/:id', async (req, res) => {
  const product = await Product.findById(req.params.id);
  res.json(product);
});

app.post('/products', async (req, res) => {
  const newProduct = new Product(req.body);
  await newProduct.save();
  res.status(201).json(newProduct);
});

app.put('/products/:id', async (req, res) => {
  const updatedProduct = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(updatedProduct);
});

app.delete('/products/:id', async (req, res) => {
  await Product.findByIdAndDelete(req.params.id);
  res.json({ message: 'Product deleted' });
});

// Simplified for brevity; add orders and cart routes similarly

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
