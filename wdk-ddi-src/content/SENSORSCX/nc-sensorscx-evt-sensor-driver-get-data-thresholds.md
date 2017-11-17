---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_GET_DATA_THRESHOLDS
title: EVT_SENSOR_DRIVER_GET_DATA_THRESHOLDS
author: windows-driver-content
description: 
ms.assetid: 92bc55ae-c602-43be-bff9-37156409d95d
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

# EVT_SENSOR_DRIVER_GET_DATA_THRESHOLDS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_GET_DATA_THRESHOLDS EvtSensorDriverGetDataThresholds; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverGetDataThresholds 
(
	SENSOROBJECT Sensor
	PSENSOR_COLLECTION_LIST pThresholds
	PULONG pSize
)
{...}

EVT_SENSOR_DRIVER_GET_DATA_THRESHOLDS PFN_SENSOR_DRIVER_GET_DATA_THRESHOLDS


```

## -parameters

### -param Sensor: 
### -param pThresholds: 
### -param pSize: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also