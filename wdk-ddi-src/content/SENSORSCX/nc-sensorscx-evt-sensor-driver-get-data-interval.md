---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_GET_DATA_INTERVAL
title: EVT_SENSOR_DRIVER_GET_DATA_INTERVAL
author: windows-driver-content
description: 
ms.assetid: 17f97ef5-8190-4145-950b-de268f61ca9b
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

# EVT_SENSOR_DRIVER_GET_DATA_INTERVAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_GET_DATA_INTERVAL EvtSensorDriverGetDataInterval; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverGetDataInterval 
(
	SENSOROBJECT Sensor
	PULONG pDataRateMs
)
{...}

EVT_SENSOR_DRIVER_GET_DATA_INTERVAL PFN_SENSOR_DRIVER_GET_DATA_INTERVAL


```

## -parameters

### -param Sensor: 
### -param pDataRateMs: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also