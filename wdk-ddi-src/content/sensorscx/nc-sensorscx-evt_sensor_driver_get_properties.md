---
UID: NC:sensorscx.EVT_SENSOR_DRIVER_GET_PROPERTIES
title: EVT_SENSOR_DRIVER_GET_PROPERTIES
author: windows-driver-content
description: This callback function returns the properties for a given sensor.
old-location: sensors\evtsensorgetproperties.htm
old-project: sensors
ms.assetid: 259C37C9-DE8C-4BC8-B18A-CDD96B97056D
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: EVT_SENSOR_DRIVER_GET_PROPERTIES, EvtSensorGetProperties, EvtSensorGetProperties callback function [Sensor Devices], sensors.evtsensorgetproperties, sensorscx/EvtSensorGetProperties
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: sensorscx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: "_requires_same_"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	SensorsCx.h
api_name:
-	EvtSensorGetProperties
product: Windows
targetos: Windows
req.typenames: SensorConnectionType
req.product: Windows 10 or later.
---


# EVT_SENSOR_DRIVER_GET_PROPERTIES callback function
This callback function returns the properties for a given sensor.

## Syntax

```
EVT_SENSOR_DRIVER_GET_PROPERTIES EvtSensorDriverGetProperties;

_IRQL_requires_same_ NTSTATUS EvtSensorDriverGetProperties(
  SENSOROBJECT Sensor,
  PSENSOR_COLLECTION_LIST pProperties,
  PULONG pSize
)
{...}
```

## Parameters

`Sensor`

A reference to a sensor object.

`pProperties`

A list of properties and their values for the specified <b>Sensor</b>. For more information, see <a href="..\sensorsdef\ns-sensorsdef-sensor_collection_list.md">SENSOR_COLLECTION_LIST</a>.

`pSize`

The size of pProperties.


## Return Value

This function returns STATUS_SUCCESS when completed successfully.

<b>Note</b> The class extension (CX) only uses the NT_SUCCESS macro to determine if the call to the driver’s Evt function was successful, but does not take any action if the function failed or does not return STATUS_SUCCESS.

## Remarks

This function must be implemented by the driver and is called by the class extension.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | sensorscx.h |
| **IRQL** | "_requires_same_" |