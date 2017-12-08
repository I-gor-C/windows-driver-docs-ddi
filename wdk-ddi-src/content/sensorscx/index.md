# Sensorscx.h header


This header is used by Sensors. For more information, see
- [Sensors](../_sensors/index.md)

Sensorscx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [SENSOR_CONFIG_INIT function](nf-sensorscx-sensor-config-init.md) | This function initializes a SENSOR_CONFIG structure. |
| [SENSOR_CONTROLLER_CONFIG_INIT function](nf-sensorscx-sensor-controller-config-init.md) | This function initializes a SENSOR_CONTROLLER_CONFIG structure. |
| [SensorsCxDeviceGetSensorList function](nf-sensorscx-sensorscxdevicegetsensorlist.md) | This function returns a list of sensor instances associated with a WDFDEVICE. |
| [SensorsCxDeviceInitConfig function](nf-sensorscx-sensorscxdeviceinitconfig.md) | This function configures the sensor device. |
| [SensorsCxDeviceInitialize function](nf-sensorscx-sensorscxdeviceinitialize.md) | This function initializes the sensor in the class extension. |
| [SensorsCxSensorCreate function](nf-sensorscx-sensorscxsensorcreate.md) | This function creates an instance of a sensor in the class extension. |
| [SensorsCxSensorDataReady function](nf-sensorscx-sensorscxsensordataready.md) | This function notifies the class extension that the driver has retrieved data. |
| [SensorsCxSensorInitialize function](nf-sensorscx-sensorscxsensorinitialize.md) | This function sets the enumeration properties of a sensor. |
| [SensorsCxStateChange function](nf-sensorscx-sensorscxstatechange.md) | Used to initialize a state change. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_SENSOR_DRIVER_DISABLE_WAKE callback](nc-sensorscx-evt-sensor-driver-disable-wake.md) | Callback to disable wake for the sensor. |
| [EVT_SENSOR_DRIVER_ENABLE_WAKE callback](nc-sensorscx-evt-sensor-driver-enable-wake.md) | Callback to enable wake for the sensor. |
| [EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION callback](nc-sensorscx-evt-sensor-driver-start-state-change-notification.md) | Used to start a state change notification. |
| [EVT_SENSOR_DRIVER_STOP_STATE_CHANGE_NOTIFICATION callback](nc-sensorscx-evt-sensor-driver-stop-state-change-notification.md) | Used to stop a state change notification. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [SENSOR_CONFIG structure](ns-sensorscx--sensor-config.md) | This structure contains information that the sensor driver passes to the class extension about each sensor. |
| [SENSOR_CONTROLLER_CONFIG structure](ns-sensorscx--sensor-controller-config.md) | This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call. |
