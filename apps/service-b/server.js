const express = require("express");
const client = require('prom-client');

const { Pool } = require("pg");
const register = client.register;

const requestCounter = new client.Counter({
    name: 'app_requests_total',
    help: 'Total number of requests',
  });

app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

app.get('/test', (req, res) => {
    requestCounter.inc();
    res.send('Hello, world! from service-b');
  });

const app = express();
const pool = new Pool({
    user: "postgres",
    host: "postgres",
    database: "mydb",
    password: "password",
    port: 5432,
});
app.get('/check', (req, res) => {
    res.status(200).send({ status: 'success', message: 'Service B is running!' });
});
app.get("/process", async (req, res) => {
    try {
        const result = await pool.query("SELECT NOW()");
        res.json({ message: "Data from PostgreSQL", timestamp: result.rows[0].now });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(5000, () => console.log("Service B is running on port 5000"));
