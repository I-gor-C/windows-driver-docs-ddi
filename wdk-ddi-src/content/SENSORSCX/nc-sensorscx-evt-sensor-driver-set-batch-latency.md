---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_SET_BATCH_LATENCY
title: EVT_SENSOR_DRIVER_SET_BATCH_LATENCY
author: windows-driver-content
description: 
ms.assetid: 2c906537-17bb-4029-97ed-3615c1d7c641
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

# EVT_SENSOR_DRIVER_SET_BATCH_LATENCY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_SET_BATCH_LATENCY EvtSensorDriverSetBatchLatency; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverSetBatchLatency 
(
	SENSOROBJECT Sensor
	ULONG BatchLatencyMs
)
{...}

EVT_SENSOR_DRIVER_SET_BATCH_LATENCY PFN_SENSOR_DRIVER_SET_BATCH_LATENCY


```

## -parameters

### -param Sensor: 
### -param BatchLatencyMs: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also