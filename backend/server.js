import express from "express";
import mongoose from "mongoose";
import bodyParser from "body-parser";
import cors from "cors";
import dotenv from "dotenv";

dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

// MongoDB connection
mongoose.connect(process.env.MONGO_URI);

// Define a schema for sensor data
const sensorDataSchema = new mongoose.Schema({
  temperature: Number,
  humidity: Number,
  timestamp: { type: Date, default: Date.now },
});

const SensorData = mongoose.model("SensorData", sensorDataSchema);

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Route to receive sensor data
app.post("/api/sensor-data", async (req, res) => {
  try {
    const { temperature, humidity } = req.body;
    console.log(
      `Received data - Temperature: ${temperature}°C, Humidity: ${humidity}%`
    ); // Logs temperature and humidity to the console

    const newSensorData = new SensorData({ temperature, humidity });
    await newSensorData.save();

    res.status(201).send("Data logged successfully");
  } catch (err) {
    console.error("Error logging data:", err); // Logs detailed error to the console
    res.status(500).json({ message: "Error logging data", error: err.message });
  }
});

app.listen(port, () => {
  console.log(`Connected to MongoDB`);
  console.log(`Server running on port ${port}`);
});
