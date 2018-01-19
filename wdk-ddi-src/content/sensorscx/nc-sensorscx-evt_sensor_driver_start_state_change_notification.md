---
UID : NC:sensorscx.EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION
title : EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION
author : windows-driver-content
description : Used to start a state change notification.
old-location : sensors\evt_sensor_driver_start_state_change_notification.htm
old-project : sensors
ms.assetid : 93C2ABCE-15C9-4EE4-A9B5-A81788DB608C
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : ISensorDriver, ISensorDriver::OnSetProperties, OnSetProperties
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : sensorscx.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION
req.alt-loc : sensorscx.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : _requires_same_
req.typenames : SensorConnectionType
req.product : Windows 10 or later.
---


# EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION function
Used to start a state change notification.

## Syntax

```
EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION EvtSensorDriverStartStateChangeNotification;

_IRQL_requires_same_ NTSTATUS EvtSensorDriverStartStateChangeNotification(
  SENSOROBJECT Sensors
)
{...}
```

## Parameters

`Sensors`

Holds information on the sensors handled by the sensor driver.


## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | sensorscx.h |
| **Library** |  |
| **IRQL** | _requires_same_ |
| **DDI compliance rules** |  |