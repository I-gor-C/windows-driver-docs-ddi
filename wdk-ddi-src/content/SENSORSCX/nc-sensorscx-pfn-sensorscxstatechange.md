---
UID: NC.sensorscx.PFN_SENSORSCXSTATECHANGE
title: *PFN_SENSORSCXSTATECHANGE
author: windows-driver-content
description: 
ms.assetid: 312a7205-ed03-4e69-be63-ed8aa1f1120e
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

# *PFN_SENSORSCXSTATECHANGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_SENSORSCXSTATECHANGE *PfnSensorscxstatechange; 

// Definition

VOID *PfnSensorscxstatechange 
(
	PSENSORSCX_DRIVER_GLOBALS DriverGlobals
	SENSOROBJECT Sensor
	SENSOR_STATE State
)
{...}

*PFN_SENSORSCXSTATECHANGE 


```

## -parameters

### -param DriverGlobals: 
### -param Sensor: 
### -param State: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also