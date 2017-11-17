---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_CANCEL_HISTORY_RETRIEVAL
title: EVT_SENSOR_DRIVER_CANCEL_HISTORY_RETRIEVAL
author: windows-driver-content
description: 
ms.assetid: 1c9ad9f7-67d7-4284-b632-347a565d5686
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

# EVT_SENSOR_DRIVER_CANCEL_HISTORY_RETRIEVAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_CANCEL_HISTORY_RETRIEVAL EvtSensorDriverCancelHistoryRetrieval; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverCancelHistoryRetrieval 
(
	SENSOROBJECT Sensor
	PULONG pBytesWritten
)
{...}

EVT_SENSOR_DRIVER_CANCEL_HISTORY_RETRIEVAL PFN_SENSOR_DRIVER_CANCEL_HISTORY_RETRIEVAL


```

## -parameters

### -param Sensor: 
### -param pBytesWritten: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also