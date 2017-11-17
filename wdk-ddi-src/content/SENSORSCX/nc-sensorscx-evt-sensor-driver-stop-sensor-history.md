---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_STOP_SENSOR_HISTORY
title: EVT_SENSOR_DRIVER_STOP_SENSOR_HISTORY
author: windows-driver-content
description: 
ms.assetid: c065bb5c-b607-4607-8bc4-affeea33bbb7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sensorscx.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# EVT_SENSOR_DRIVER_STOP_SENSOR_HISTORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_STOP_SENSOR_HISTORY EvtSensorDriverStopSensorHistory; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverStopSensorHistory 
(
	SENSOROBJECT Sensor
)
{...}

EVT_SENSOR_DRIVER_STOP_SENSOR_HISTORY PFN_SENSOR_DRIVER_STOP_SENSOR_HISTORY


```

## -parameters

### -param Sensor: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also