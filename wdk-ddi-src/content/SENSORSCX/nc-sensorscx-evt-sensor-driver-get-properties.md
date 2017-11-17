---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_GET_PROPERTIES
title: EVT_SENSOR_DRIVER_GET_PROPERTIES
author: windows-driver-content
description: 
ms.assetid: 435f1358-371a-4757-a7cd-359f70353018
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

# EVT_SENSOR_DRIVER_GET_PROPERTIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_GET_PROPERTIES EvtSensorDriverGetProperties; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverGetProperties 
(
	SENSOROBJECT Sensor
	PSENSOR_COLLECTION_LIST pProperties
	PULONG pSize
)
{...}

EVT_SENSOR_DRIVER_GET_PROPERTIES PFN_SENSOR_DRIVER_GET_PROPERTIES


```

## -parameters

### -param Sensor: 
### -param pProperties: 
### -param pSize: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also