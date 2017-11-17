---
UID: NC.sensorscx.PFN_SENSORSCXSENSORDATAREADY
title: *PFN_SENSORSCXSENSORDATAREADY
author: windows-driver-content
description: 
ms.assetid: 66e97a45-f1cb-489b-92f0-72922166362c
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

# *PFN_SENSORSCXSENSORDATAREADY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_SENSORSCXSENSORDATAREADY *PfnSensorscxsensordataready; 

// Definition

VOID *PfnSensorscxsensordataready 
(
	PSENSORSCX_DRIVER_GLOBALS DriverGlobals
	SENSOROBJECT Sensor
	PSENSOR_COLLECTION_LIST pSensorData
)
{...}

*PFN_SENSORSCXSENSORDATAREADY 


```

## -parameters

### -param DriverGlobals: 
### -param Sensor: 
### -param pSensorData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also