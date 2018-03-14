---
UID: NA:sensorsclassextension
ms.assetid: 9181ae48-c50e-3f5e-942d-1030b8e2c0b5
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Sensorsclassextension.h header



This header is used by Sensors. For more information, see
- [Sensors](../_sensors/index.md)

Sensorsclassextension.h contain these programming interfaces:


## Enumerations

| Title   | Description   |
| ---- |:---- |
| [LOCATION_DESIRED_ACCURACY enumeration](ne-sensorsclassextension-location_desired_accuracy.md) | The LOCATION_DESIRED_ACCURACY enumeration type defines values for the SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY property. |
| [MagnetometerAccuracy enumeration](ne-sensorsclassextension-magnetometeraccuracy.md) | Specifies the accuracy of the magnetometer. |
| [__MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0001 enumeration](ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0001.md) | The SensorState enumeration type specifies the current operational state of a sensor. |
| [__MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0002 enumeration](ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0002.md) | The SensorConnectionType enumeration type defines values for the SENSOR_CONNECTION_TYPE property. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [ISensorClassExtension interface](nn-sensorsclassextension-isensorclassextension.md) | The ISensorClassExtension interface provides methods that the sensor driver uses to communicate with the sensor platform (and, therefore, client applications) through the sensor class extension object. |
| [ISensorDriver interface](nn-sensorsclassextension-isensordriver.md) | The ISensorDriver interface provides callback methods that the sensor class extension uses to provide requests and notifications to the sensor driver. |

## Methods

| Title   | Description   |
| ---- |:----

# sensorsclassextension.h header



sensorsclassextension.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [ISensorClassExtension](nn-sensorsclassextension-isensorclassextension.md) | The ISensorClassExtension interface provides methods that the sensor driver uses to communicate with the sensor platform (and, therefore, client applications) through the sensor class extension object. |
| [ISensorDriver](nn-sensorsclassextension-isensordriver.md) | The ISensorDriver interface provides callback methods that the sensor class extension uses to provide requests and notifications to the sensor driver. |






## Enumerations
| Title | Description |
| ---- |:---- |
| [__MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0001](ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0001.md) | The SensorState enumeration type specifies the current operational state of a sensor. |
| [__MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0002](ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0002.md) | The SensorConnectionType enumeration type defines values for the SENSOR_CONNECTION_TYPE property. |
| [LOCATION_DESIRED_ACCURACY](ne-sensorsclassextension-location_desired_accuracy.md) | The LOCATION_DESIRED_ACCURACY enumeration type defines values for the SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY property. |
| [MagnetometerAccuracy](ne-sensorsclassextension-magnetometeraccuracy.md) | Specifies the accuracy of the magnetometer. |