---
UID: NC:sensorscx.EVT_SENSOR_DRIVER_SET_DATA_INTERVAL
title: EVT_SENSOR_DRIVER_SET_DATA_INTERVAL
author: windows-driver-content
description: This callback function sets the data interval for a specified sensor.
old-location: sensors\evtsensorsetdatainterval.htm
old-project: sensors
ms.assetid: 56A1D005-C060-4C6E-8CA4-0BAC4FBADABE
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: EVT_SENSOR_DRIVER_SET_DATA_INTERVAL, EvtSensorSetDataInterval, EvtSensorSetDataInterval callback function [Sensor Devices], sensors.evtsensorsetdatainterval, sensorscx/EvtSensorSetDataInterval
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
-	EvtSensorSetDataInterval
product: Windows
targetos: Windows
req.typenames: SensorConnectionType
req.product: Windows 10 or later.
---


# EVT_SENSOR_DRIVER_SET_DATA_INTERVAL callback function
This callback function sets the data interval for a specified sensor.

## Syntax

```
EVT_SENSOR_DRIVER_SET_DATA_INTERVAL EvtSensorDriverSetDataInterval;

_IRQL_requires_same_ NTSTATUS EvtSensorDriverSetDataInterval(
  SENSOROBJECT Sensor,
  ULONG DataRateMs
)
{...}
```

## Parameters

`Sensor`

A reference to a sensor object.

`DataRateMs`




## Return Value

This function returns STATUS_SUCCESS when completed successfully.

<b>Note</b> The class extension (CX) only uses the NT_SUCCESS macro to 
		  determine if the call to the driver’s Evt function was successful, 
		  but does not take any action if the function failed or does not return STATUS_SUCCESS.

## Remarks

This function must be implemented by the driver and is called by the class extension.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | sensorscx.h |
| **IRQL** | "_requires_same_" |