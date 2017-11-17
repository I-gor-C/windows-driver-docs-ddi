---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_START_HISTORY_RETRIEVAL
title: EVT_SENSOR_DRIVER_START_HISTORY_RETRIEVAL
author: windows-driver-content
description: 
ms.assetid: f8738c3c-6468-48aa-8a00-08fc5d3b5b43
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

# EVT_SENSOR_DRIVER_START_HISTORY_RETRIEVAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_START_HISTORY_RETRIEVAL EvtSensorDriverStartHistoryRetrieval; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverStartHistoryRetrieval 
(
	SENSOROBJECT Sensor
	PSENSOR_COLLECTION_LIST pHistory
	ULONG HistorySizeInBytes
)
{...}

EVT_SENSOR_DRIVER_START_HISTORY_RETRIEVAL PFN_SENSOR_DRIVER_START_HISTORY_RETRIEVAL


```

## -parameters

### -param Sensor: 
### -param pHistory: 
### -param HistorySizeInBytes: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also