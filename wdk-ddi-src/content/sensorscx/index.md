---
UID: NA:sensorscx
---

# Sensorscx.h header

## -description

This header is used by Sensors. For more information, see
- [Sensors](../_sensors/index.md)

Sensorscx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [SENSOR_CONFIG_INIT function](nf-sensorscx-sensor_config_init.md) | This function initializes a SENSOR_CONFIG structure. |
| [SENSOR_CONTROLLER_CONFIG_INIT function](nf-sensorscx-sensor_controller_config_init.md) | This function initializes a SENSOR_CONTROLLER_CONFIG structure. |
| [SensorsCxDeviceGetSensorList function](nf-sensorscx-sensorscxdevicegetsensorlist.md) | This function returns a list of sensor instances associated with a WDFDEVICE. |
| [SensorsCxDeviceInitConfig function](nf-sensorscx-sensorscxdeviceinitconfig.md) | This function configures the sensor device. |
| [SensorsCxDeviceInitialize function](nf-sensorscx-sensorscxdeviceinitialize.md) | This function initializes the sensor in the class extension. |
| [SensorsCxSensorCreate function](nf-sensorscx-sensorscxsensorcreate.md) | This function creates an instance of a sensor in the class extension. |
| [SensorsCxSensorDataReady function](nf-sensorscx-sensorscxsensordataready.md) | This function notifies the class extension that the driver has retrieved data. |
| [SensorsCxSensorInitialize function](nf-sensorscx-sensorscxsensorinitialize.md) | This function sets the enumeration properties of a sensor. |
| [SensorsCxStateChange function](nf-sensorscx-sensorscxstatechange.md) | Used to initialize a state change. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_SENSOR_CONFIG structure](ns-sensorscx-_sensor_config.md) | This structure contains information that the sensor driver passes to the class extension about each sensor. |
| [_SENSOR_CONTROLLER_CONFIG structure](ns-sensorscx-_sensor_controller_config.md) | This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call. |
