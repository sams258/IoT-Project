# Tutorial on How to Build a Temperature and Humidity Sensor (Indahouse)

## Author

Sam El Saati (se223xm)

## Project Overview

This project that I have named **IndaHouse** involves building a temperature and humidity monitoring system using a Raspberry Pi Pico WH, a DHT11 sensor, and a MongoDB backend. The data collected by the sensor is logged into a MongoDB database and visualized using MongoDB Atlas Charts. The entire system is developed using MicroPython for the Pico WH, Node.js for the backend, and Thonny as the IDE. This project is ideal for smart home applications where monitoring indoor environmental conditions is crucial.

**Estimated Time to Complete:** Approximately 4-6 hours

## Objective

The primary goal of this project is to create a cost-effective and reliable system for monitoring indoor temperature and humidity levels. This data can be used to gain insights into home comfort levels, detect unusual environmental changes, and potentially trigger alerts or automated actions based on the sensor readings.

- **Why This Project:** I chose this project because it provides valuable insights into environmental conditions within the home, which can be crucial for maintaining a comfortable and healthy living environment.
- **Purpose:** The device serves to monitor indoor climate conditions, which can help in making informed decisions about heating, cooling, and humidity control.
- **Insights:** By analyzing the data over time, trends in temperature and humidity can be identified, allowing for optimization of heating, ventilation, and air conditioning (HVAC) systems.

## Material

### List of Materials

- **Raspberry Pi Pico WH**: Microcontroller with built-in Wi-Fi, used as the main processing unit.

![pico-wh](https://hackmd.io/_uploads/rkDogUo9A.png)

- **DHT11 Temperature and Humidity Sensor**: Sensor used to measure temperature and humidity.

![DHT11-sensor](https://hackmd.io/_uploads/SJV2gUi9C.png)

- **RGB LED Module**: Provides visual feedback when readings are taken.

![led-module](https://hackmd.io/_uploads/B1GpxIs9R.png)

- **Piezo Speaker**: Emits a sound to indicate data logging.

![piezo-speaker](https://hackmd.io/_uploads/BJRTxIo9R.png)

- **Jumper Wires**: Used for connections between the Pico and other components.

![jumper-wires](https://hackmd.io/_uploads/H1R-WIo5C.png)

- **Breadboard**: For prototyping the circuit.

![bread-board](https://hackmd.io/_uploads/SJxm-8s9A.png)

- **Cable Stripper**: For stripping cables in a clean professional way (optional).

![cable-stripper](https://hackmd.io/_uploads/BJeD-Lj9C.png)

### Specifications and Costs

- **Raspberry Pi Pico WH**: SEK 109 - Bought from [Electrokit](https://www.electrokit.com/raspberry-pi-pico-wh)
- **DHT11 Sensor**: SEK 49 - Available on [Electrokit](https://www.electrokit.com/digital-temperatur-och-fuktsensor-dht11)
- **RGB LED Module**: SEK 22 - Available on [Electrokit](https://www.electrokit.com/led-modul-rgb)
- **Piezo Speaker**: SEK 39 - Available on [Electrokit](https://www.electrokit.com/piezohogtalare-aktiv)
- **Jumper Wires**: SEK 55 - Pack from [Electrokit](https://www.electrokit.com/labbsladd-40-pin-30cm-hane/hane)
- **Breadboard**: SEK 69 - Available on [Electrokit](https://www.electrokit.com/kopplingsdack-840-anslutningar)
- **Cable stripper**: SEK 169 - Available on [Electrokit](https://www.electrokit.com/kabelskalare-awg30-20) _(Optional)_

## Computer Setup

### Chosen IDE

- **Thonny**: This is the chosen IDE for developing and uploading MicroPython code to the Raspberry Pi Pico WH. It is simple, user-friendly, and supports direct interaction with MicroPython environments.

### Steps to Set Up

1. **Install Thonny**: Download and install Thonny from [thonny.org](https://thonny.org/).
2. **Install MicroPython on Pico**:
   - Connect the Pico WH to your computer while holding down the BOOTSEL button.
   - Download the MicroPython UF2 file from [micropython.org](https://micropython.org/download/rp2-pico/).
   - Drag and drop the UF2 file onto the `RPI-RP2` drive that appears when you connect the Pico.
3. **Upload Code**:
   - Write your MicroPython code in Thonny.
   - Save the script as `main.py` on the Pico to run automatically on startup.

### Required Computer Setup

- **Node.js Installation**: Install Node.js from [nodejs.org](https://nodejs.org/) to run the backend server.
- **MongoDB Setup**: Set up a MongoDB Atlas account for cloud database storage and visualization.

## Putting Everything Together

### Circuit Diagram

![diagram1](https://hackmd.io/_uploads/Hy3zOk6qC.png)

_(circuit diagram)_

### Connections

- **DHT11 Sensor**:
  - Data Pin -> GPIO 15
  - VCC -> 3.3V
  - GND -> Ground
- **RGB LED Module**:
  - Red Pin -> GPIO 16
  - Green Pin -> GPIO 17
  - Blue Pin -> GPIO 18
  - GND -> Ground
- **Piezo Speaker**:
  - Positive Pin -> GPIO 9
  - Negative Pin -> Ground

### Electrical calculations:

#### **1. Component Specifications**

- **Raspberry Pi Pico WH:**

  - Operating Voltage: 3.3V (logic level)
  - GPIO Max Current per Pin: 12mA
  - Total Max Current for All GPIOs: 50mA

- **DHT11 Sensor:**

  - Operating Voltage: 3.3V - 5V
  - Current Consumption: 0.3mA (during measurement)

- **RGB LED Module:**

  - Operating Voltage: 3.3V
  - Current per Color (Red, Green, Blue): Typically 20mA per channel at full brightness

- **Piezo Speaker:**
  - Operating Voltage: 3.3V - 5V
  - Current Consumption: Typically 20mA

#### **2. Current Draw Calculations with PWM**

#### **DHT11 Sensor:**

- **Current Consumption:** 0.3mA

#### **RGB LED Module:**

- **PWM Settings:** The red and blue LEDs are both set to 50% brightness (50% duty cycle).
- **Current per LED at 50% Duty Cycle:**
  - Red LED: 20mA \* 0.5 = 10mA
  - Blue LED: 20mA \* 0.5 = 10mA
  - **Total Current for RGB LED (Purple):** 10mA (Red) + 10mA (Blue) = **20mA**

#### **Piezo Speaker:**

- **Current Consumption:** 20mA

#### **3. Total Current Draw**

Adding up the current draw from all components:

- **DHT11 Sensor:** 0.3mA
- **RGB LED Module (Purple at 50% brightness):** 20mA
- **Piezo Speaker:** 20mA

**Total Current Consumption:**

- **Total:** 0.3mA + 20mA + 20mA = **40.3mA**

#### **4. Power Supply Considerations**

The total current draw from all GPIOs is 40.3mA, which is under the 50mA recommended limit for the Raspberry Pi Pico WH. This means the Pico WH should be able to handle the load without issues.

#### **Voltage Considerations**

All components are operating at 3.3V, which is the standard output from the Raspberry Pi Pico WH, so there are no voltage level issues.

IndaHouse is now optimized for power consumption, and should operate reliably within the specifications of the Raspberry Pi Pico WH.

## Platform

### Chosen Platform: MongoDB Atlas

- **Functionality**: MongoDB Atlas provides a robust, cloud-based NoSQL database solution with built-in visualization tools.
- **Scalability**: MongoDB Atlas scales seamlessly from development to production environments, with options for free and paid subscriptions.
- **Reason for Choosing**: MongoDB Atlas was chosen for its ease of use, scalability, and integrated data visualization capabilities.

## The Code

### Core Functionality

#### Connecting to Wi-Fi

```python
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to Wi-Fi:', wlan.ifconfig())
```

_This function handles the Wi-Fi connection process, ensuring the Raspberry Pi Pico WH is connected to your home network before starting with data logging._

#### Reading Sensor Data and Sending It to the Backend

```python
def main():
    connect_wifi()
    while True:
        try:
            dht_sensor.measure()
            temperature = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            send_data(temperature, humidity)
            print(f"Data sent: Temp={temperature}, Humidity={humidity}")
        except OSError as e:
            print('Failed to read sensor or send data:', e)
        time.sleep(60)
```

_This loop continuously reads the temperature and humidity every 60 seconds, sending the data to the Node.js backend. Smooth error handling is added to avoid crash of the script_

## Transmitting the Data / Connectivity

### Data Transmission

- **Frequency:** Data is transmitted every 60 seconds.
- **Protocol:** The Raspberry Pi Pico WH uses HTTP over Wi-Fi to send data to the Node.js backend.
- **Data Format:** The data is sent as a JSON payload containing temperature, humidity, and a timestamp.

### Design Choices

- **Wi-Fi** was chosen for its ubiquity and ease of integration with home networks.
- **HTTP POST requests** were used for simplicity and compatibility with the Node.js backend.

## Presenting the Data

### Data Visualization

- **Platform:** MongoDB Atlas Charts
- **Dashboard:** The MongoDB Atlas Charts dashboard visualizes the temperature and humidity data over time, offering insights into trends and anomalies.

### Example Dashboard

![charts](https://hackmd.io/_uploads/HyBk2HsqC.png)

_(screenshot of the MongoDB Atlas Charts dashboard)_

### Data Persistence

- **Frequency of Data Storage:** Data is stored in MongoDB every 60 seconds.
- **Database Choice:** MongoDB was chosen for its flexibility and scalability, which suits both development and production environments.

## Finalizing the Design

### Final Results

- The temperature and humidity monitoring system was successfully implemented, with real-time data visualization in MongoDB Atlas Charts.
- The system proved to be reliable and could be expanded with additional sensors or integrated into larger smart home systems.

### Final Thoughts

- **What Went Well:** The project was straightforward and provided valuable insights into environmental monitoring.
- **Improvements:** Future iterations could include more advanced sensors, automated alerts, or integration with other smart home systems.

### Pictures / Videos

![board](https://hackmd.io/_uploads/ryz6pBo90.png)

_(picture of the final setup showing the Raspberry Pi Pico WH, sensor, and the other components on the breadboard.)_

{%youtube 1RgMqwnBYuA %}
_(promotional video about the project, produced fully by me.)_

{%youtube TODFrJAMpig %}
_(video showing the project in action, reading, sending, receiving, etc....)_
