---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_START_SENSOR
title: EVT_SENSOR_DRIVER_START_SENSOR
author: windows-driver-content
description: 
ms.assetid: dbb2c46c-f527-4ada-8b73-fef0e1e8faeb
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

# EVT_SENSOR_DRIVER_START_SENSOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_START_SENSOR EvtSensorDriverStartSensor; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverStartSensor 
(
	SENSOROBJECT Sensor
)
{...}

EVT_SENSOR_DRIVER_START_SENSOR PFN_SENSOR_DRIVER_START_SENSOR


```

## -parameters

### -param Sensor: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also