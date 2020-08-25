from SerialBus import SerialBusTCP, SerialBusDevice
import sensor_device

serialbus = SerialBusTCP()
serialbus.connect('localhost', 6964)
device = SerialBusDevice(7, serialbus, device_type = sensor_device)
print(device.get_value(sensor_device.DATA))
