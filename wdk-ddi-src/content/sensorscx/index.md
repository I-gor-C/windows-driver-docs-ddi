---
UID: NA:sensorscx
ms.assetid: 5d44f356-17a0-30d5-84f5-5fb6532ee25b
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# sensorscx.h header



sensorscx.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [EVT_SENSOR_DRIVER_DISABLE_WAKE](nc-sensorscx-evt_sensor_driver_disable_wake.md) | Callback to disable wake for the sensor. |
| [EVT_SENSOR_DRIVER_ENABLE_WAKE](nc-sensorscx-evt_sensor_driver_enable_wake.md) | Callback to enable wake for the sensor. |
| [EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION](nc-sensorscx-evt_sensor_driver_start_state_change_notification.md) | Used to start a state change notification. |
| [EVT_SENSOR_DRIVER_STOP_STATE_CHANGE_NOTIFICATION](nc-sensorscx-evt_sensor_driver_stop_state_change_notification.md) | Used to stop a state change notification. |
| [SENSOR_CONFIG_INIT](nf-sensorscx-sensor_config_init.md) | This function initializes a SENSOR_CONFIG structure. |
| [SENSOR_CONTROLLER_CONFIG_INIT](nf-sensorscx-sensor_controller_config_init.md) | This function initializes a SENSOR_CONTROLLER_CONFIG structure. |
| [SensorsCxDeviceGetSensorList](nf-sensorscx-sensorscxdevicegetsensorlist.md) | This function returns a list of sensor instances associated with a WDFDEVICE. |
| [SensorsCxDeviceInitConfig](nf-sensorscx-sensorscxdeviceinitconfig.md) | This function configures the sensor device. |
| [SensorsCxDeviceInitialize](nf-sensorscx-sensorscxdeviceinitialize.md) | This function initializes the sensor in the class extension. |
| [SensorsCxSensorCreate](nf-sensorscx-sensorscxsensorcreate.md) | This function creates an instance of a sensor in the class extension. |
| [SensorsCxSensorDataReady](nf-sensorscx-sensorscxsensordataready.md) | This function notifies the class extension that the driver has retrieved data. |
| [SensorsCxSensorInitialize](nf-sensorscx-sensorscxsensorinitialize.md) | This function sets the enumeration properties of a sensor. |
| [SensorsCxStateChange](nf-sensorscx-sensorscxstatechange.md) | Used to initialize a state change. |



## Structures
| Title | Description |
| ---- |:---- |
| [_SENSOR_CONFIG](ns-sensorscx-_sensor_config.md) | This structure contains information that the sensor driver passes to the class extension about each sensor. |
| [_SENSOR_CONTROLLER_CONFIG](ns-sensorscx-_sensor_controller_config.md) | This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call. |