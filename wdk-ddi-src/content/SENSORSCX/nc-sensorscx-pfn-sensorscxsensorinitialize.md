---
UID: NC.sensorscx.PFN_SENSORSCXSENSORINITIALIZE
title: *PFN_SENSORSCXSENSORINITIALIZE
author: windows-driver-content
description: 
ms.assetid: 896165c7-64ef-4aaa-b3f8-c4401553bff0
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

# *PFN_SENSORSCXSENSORINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_SENSORSCXSENSORINITIALIZE *PfnSensorscxsensorinitialize; 

// Definition

NTSTATUS *PfnSensorscxsensorinitialize 
(
	PSENSORSCX_DRIVER_GLOBALS DriverGlobals
	SENSOROBJECT Sensor
	PSENSOR_CONFIG pSensorConfig
)
{...}

*PFN_SENSORSCXSENSORINITIALIZE 


```

## -parameters

### -param DriverGlobals: 
### -param Sensor: 
### -param pSensorConfig: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also