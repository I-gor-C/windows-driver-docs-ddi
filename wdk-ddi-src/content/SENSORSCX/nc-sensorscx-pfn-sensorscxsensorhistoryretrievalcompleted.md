---
UID: NC.sensorscx.PFN_SENSORSCXSENSORHISTORYRETRIEVALCOMPLETED
title: *PFN_SENSORSCXSENSORHISTORYRETRIEVALCOMPLETED
author: windows-driver-content
description: 
ms.assetid: a1d7aecd-084e-4554-9bf0-564fbe40cbb6
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

# *PFN_SENSORSCXSENSORHISTORYRETRIEVALCOMPLETED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_SENSORSCXSENSORHISTORYRETRIEVALCOMPLETED *PfnSensorscxsensorhistoryretrievalcompleted; 

// Definition

VOID *PfnSensorscxsensorhistoryretrievalcompleted 
(
	PSENSORSCX_DRIVER_GLOBALS DriverGlobals
	SENSOROBJECT Sensor
	ULONG BytesWritten
	NTSTATUS InStatus
)
{...}

*PFN_SENSORSCXSENSORHISTORYRETRIEVALCOMPLETED 


```

## -parameters

### -param DriverGlobals: 
### -param Sensor: 
### -param BytesWritten: 
### -param InStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also