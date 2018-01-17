---
UID: TP:sensors
ms.assetid: 8a7a095d-53d4-30a8-a1d2-4ef29c8a344d
ms.author: windowsdriverdev
ms.date: 01/16/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Sensors


Overview of the Sensors technology.

To develop Sensors, you need these headers:

 * [sensorsclassextension.h](..\sensorsclassextension\index.md)
 * [sensorscx.h](..\sensorscx\index.md)

For the programming guide, see [Sensors](https://docs.microsoft.com/en-us/windows-hardware/drivers/sensors).

## Functions

| Title   | Description   |
| ---- |:---- |
| [EVT_SENSOR_DRIVER_DISABLE_WAKE function](..\sensorscx\nc-sensorscx-evt_sensor_driver_disable_wake.md) | Callback to disable wake for the sensor. |
| [EVT_SENSOR_DRIVER_ENABLE_WAKE function](..\sensorscx\nc-sensorscx-evt_sensor_driver_enable_wake.md) | Callback to enable wake for the sensor. |
| [EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION function](..\sensorscx\nc-sensorscx-evt_sensor_driver_start_state_change_notification.md) | Used to start a state change notification. |
| [EVT_SENSOR_DRIVER_STOP_STATE_CHANGE_NOTIFICATION function](..\sensorscx\nc-sensorscx-evt_sensor_driver_stop_state_change_notification.md) | Used to stop a state change notification. |
| [SENSOR_CONFIG_INIT function](..\sensorscx\nf-sensorscx-sensor_config_init.md) | This function initializes a SENSOR_CONFIG structure. |
| [SENSOR_CONTROLLER_CONFIG_INIT function](..\sensorscx\nf-sensorscx-sensor_controller_config_init.md) | This function initializes a SENSOR_CONTROLLER_CONFIG structure. |
| [SensorsCxDeviceGetSensorList function](..\sensorscx\nf-sensorscx-sensorscxdevicegetsensorlist.md) | This function returns a list of sensor instances associated with a WDFDEVICE. |
| [SensorsCxDeviceInitConfig function](..\sensorscx\nf-sensorscx-sensorscxdeviceinitconfig.md) | This function configures the sensor device. |
| [SensorsCxDeviceInitialize function](..\sensorscx\nf-sensorscx-sensorscxdeviceinitialize.md) | This function initializes the sensor in the class extension. |
| [SensorsCxSensorCreate function](..\sensorscx\nf-sensorscx-sensorscxsensorcreate.md) | This function creates an instance of a sensor in the class extension. |
| [SensorsCxSensorDataReady function](..\sensorscx\nf-sensorscx-sensorscxsensordataready.md) | This function notifies the class extension that the driver has retrieved data. |
| [SensorsCxSensorInitialize function](..\sensorscx\nf-sensorscx-sensorscxsensorinitialize.md) | This function sets the enumeration properties of a sensor. |
| [SensorsCxStateChange function](..\sensorscx\nf-sensorscx-sensorscxstatechange.md) | Used to initialize a state change. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_SENSOR_CONFIG structure](..\sensorscx\ns-sensorscx-_sensor_config.md) | This structure contains information that the sensor driver passes to the class extension about each sensor. |
| [_SENSOR_CONTROLLER_CONFIG structure](..\sensorscx\ns-sensorscx-_sensor_controller_config.md) | This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [LOCATION_DESIRED_ACCURACY enumeration](..\sensorsclassextension\ne-sensorsclassextension-location_desired_accuracy.md) | The LOCATION_DESIRED_ACCURACY enumeration type defines values for the SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY property. |
| [MagnetometerAccuracy enumeration](..\sensorsclassextension\ne-sensorsclassextension-magnetometeraccuracy.md) | Specifies the accuracy of the magnetometer. |
| [__MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0001 enumeration](..\sensorsclassextension\ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0001.md) | The SensorState enumeration type specifies the current operational state of a sensor. |
| [__MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0002 enumeration](..\sensorsclassextension\ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0002.md) | The SensorConnectionType enumeration type defines values for the SENSOR_CONNECTION_TYPE property. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [ISensorClassExtension interface](..\sensorsclassextension\nn-sensorsclassextension-isensorclassextension.md) | The ISensorClassExtension interface provides methods that the sensor driver uses to communicate with the sensor platform (and, therefore, client applications) through the sensor class extension object. |
| [ISensorDriver interface](..\sensorsclassextension\nn-sensorsclassextension-isensordriver.md) | The ISensorDriver interface provides callback methods that the sensor class extension uses to provide requests and notifications to the sensor driver. |

## Methods

| Title   | Description   |
| ---- |:---- |
| [ISensorClassExtension::CleanupFile method](..\sensorsclassextension\nf-sensorsclassextension-isensorclassextension-cleanupfile.md) | The ISensorClassExtension |
| [ISensorClassExtension::Initialize method](..\sensorsclassextension\nf-sensorsclassextension-isensorclassextension-initialize.md) | The ISensorClassExtension |
| [ISensorClassExtension::PostEvent method](..\sensorsclassextension\nf-sensorsclassextension-isensorclassextension-postevent.md) | The ISensorClassExtension |
| [ISensorClassExtension::PostStateChange method](..\sensorsclassextension\nf-sensorsclassextension-isensorclassextension-poststatechange.md) | The ISensorClassExtension |
| [ISensorClassExtension::ProcessIoControl method](..\sensorsclassextension\nf-sensorsclassextension-isensorclassextension-processiocontrol.md) | The ISensorClassExtension |
| [ISensorClassExtension::Uninitialize method](..\sensorsclassextension\nf-sensorsclassextension-isensorclassextension-uninitialize.md) | The ISensorClassExtension |
| [ISensorDriver::OnClientConnect method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-onclientconnect.md) | The ISensorDriver |
| [ISensorDriver::OnClientDisconnect method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-onclientdisconnect.md) | The ISensorDriver |
| [ISensorDriver::OnClientSubscribeToEvents method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-onclientsubscribetoevents.md) | The ISensorDriver |
| [ISensorDriver::OnClientUnsubscribeFromEvents method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-onclientunsubscribefromevents.md) | The ISensorDriver |
| [ISensorDriver::OnGetDataFields method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-ongetdatafields.md) | The ISensorDriver |
| [ISensorDriver::OnGetProperties method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-ongetproperties.md) | The ISensorDriver |
| [ISensorDriver::OnGetSupportedDataFields method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-ongetsupporteddatafields.md) | The ISensorDriver |
| [ISensorDriver::OnGetSupportedEvents method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-ongetsupportedevents.md) | The ISensorDriver |
| [ISensorDriver::OnGetSupportedProperties method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-ongetsupportedproperties.md) | The ISensorDriver |
| [ISensorDriver::OnGetSupportedSensorObjects method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-ongetsupportedsensorobjects.md) | The ISensorDriver |
| [ISensorDriver::OnProcessWpdMessage method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-onprocesswpdmessage.md) | The ISensorDriver |
| [ISensorDriver::OnSetProperties method](..\sensorsclassextension\nf-sensorsclassextension-isensordriver-onsetproperties.md) | The ISensorDriver |
