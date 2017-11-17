---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_SET_DATA_INTERVAL
title: EVT_SENSOR_DRIVER_SET_DATA_INTERVAL
author: windows-driver-content
description: 
ms.assetid: b99f51c6-23be-4e8e-8274-76fff0a4db1a
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

# EVT_SENSOR_DRIVER_SET_DATA_INTERVAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_SET_DATA_INTERVAL EvtSensorDriverSetDataInterval; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverSetDataInterval 
(
	SENSOROBJECT Sensor
	ULONG DataRateMs
)
{...}

EVT_SENSOR_DRIVER_SET_DATA_INTERVAL PFN_SENSOR_DRIVER_SET_DATA_INTERVAL


```

## -parameters

### -param Sensor: 
### -param DataRateMs: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also