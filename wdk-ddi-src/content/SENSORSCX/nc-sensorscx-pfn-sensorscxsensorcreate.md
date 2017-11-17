---
UID: NC.sensorscx.PFN_SENSORSCXSENSORCREATE
title: *PFN_SENSORSCXSENSORCREATE
author: windows-driver-content
description: 
ms.assetid: 909e3053-bf01-4dae-88ad-0584785ccde4
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

# *PFN_SENSORSCXSENSORCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_SENSORSCXSENSORCREATE *PfnSensorscxsensorcreate; 

// Definition

NTSTATUS *PfnSensorscxsensorcreate 
(
	PSENSORSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE FxDevice
	PWDF_OBJECT_ATTRIBUTES pSensorAttributes
	PSENSOROBJECT pSensor
)
{...}

*PFN_SENSORSCXSENSORCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param FxDevice: 
### -param pSensorAttributes: 
### -param pSensor: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also