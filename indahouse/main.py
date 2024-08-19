import machine
import dht
import time
import network
import urequests

# WiFi credentials
SSID = 'iPhone 11'
PASSWORD = '12345679'

# Backend URL
backend_url = 'http://172.20.10.8/api/sensor-data'

# Initialize DHT11 sensor
dht_sensor = dht.DHT11(machine.Pin(15))

# Initialize RGB LED
red_led = machine.Pin(16, machine.Pin.OUT)
green_led = machine.Pin(17, machine.Pin.OUT)
blue_led = machine.Pin(18, machine.Pin.OUT)

# Initialize Piezo Speaker
piezo = machine.Pin(9, machine.Pin.OUT)


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    max_attempts = 10  # Maximum number of attempts to connect
    attempt = 0

    while not wlan.isconnected() and attempt < max_attempts:
        attempt += 1
        print(f'Attempting to connect to WiFi: {attempt}')
        time.sleep(2)  # Wait 2 seconds between attempts

    if wlan.isconnected():
        print('Connected to WiFi:', wlan.ifconfig())
    else:
        print('Failed to connect to WiFi after several attempts.')
        # Handle connection failure (reset, alert, etc.)


def send_data(temp, humidity):
    data = {
        'temperature': temp,
        'humidity': humidity
    }
    response = urequests.post(backend_url, json=data)
    response.close()


def main():
    connect_wifi()

    # Set up PWM for the RGB LED
    red_led_pwm = machine.PWM(machine.Pin(16))
    blue_led_pwm = machine.PWM(machine.Pin(18))
    red_led_pwm.freq(1000)
    blue_led_pwm.freq(1000)

    # Set duty cycle to 50% for lower brightness (half intensity)
    red_led_pwm.duty_u16(32768)
    blue_led_pwm.duty_u16(32768)

    while True:
        try:
            dht_sensor.measure()
            temperature = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            print('Temperature:', temperature, 'C')
            print('Humidity:', humidity, '%')

            # Turn on the RGB LED to display purple (red + blue)
            red_led_pwm.duty_u16(32768)  # 50% brightness
            blue_led_pwm.duty_u16(32768)  # 50% brightness
            # Make the speaker beep once
            piezo.value(1)
            time.sleep(0.2)  # Beep duration
            piezo.value(0)

            # Keep the LED on for the remaining 4.8 seconds
            time.sleep(4.8)
            red_led.value(0)

            # Send data to the backend
            send_data(temperature, humidity)

        except OSError:
            print('Failed to read sensor.')

        time.sleep(60)  # Wait 60 seconds before next reading


if __name__ == '__main__':
    main()
