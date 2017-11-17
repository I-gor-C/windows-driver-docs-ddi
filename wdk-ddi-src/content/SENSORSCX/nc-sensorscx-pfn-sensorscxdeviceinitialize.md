---
UID: NC.sensorscx.PFN_SENSORSCXDEVICEINITIALIZE
title: *PFN_SENSORSCXDEVICEINITIALIZE
author: windows-driver-content
description: 
ms.assetid: 4543ba40-a2ae-424f-a0e1-76f8b3c4d1ac
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

# *PFN_SENSORSCXDEVICEINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_SENSORSCXDEVICEINITIALIZE *PfnSensorscxdeviceinitialize; 

// Definition

NTSTATUS *PfnSensorscxdeviceinitialize 
(
	PSENSORSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE FxDevice
	PSENSOR_CONTROLLER_CONFIG pSensorConfig
)
{...}

*PFN_SENSORSCXDEVICEINITIALIZE 


```

## -parameters

### -param DriverGlobals: 
### -param FxDevice: 
### -param pSensorConfig: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also