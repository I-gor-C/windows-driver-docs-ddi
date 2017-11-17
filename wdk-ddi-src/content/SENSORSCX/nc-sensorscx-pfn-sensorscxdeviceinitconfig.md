---
UID: NC.sensorscx.PFN_SENSORSCXDEVICEINITCONFIG
title: *PFN_SENSORSCXDEVICEINITCONFIG
author: windows-driver-content
description: 
ms.assetid: 142cd399-7e9c-4124-a1e8-9558b8fef254
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

# *PFN_SENSORSCXDEVICEINITCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_SENSORSCXDEVICEINITCONFIG *PfnSensorscxdeviceinitconfig; 

// Definition

NTSTATUS *PfnSensorscxdeviceinitconfig 
(
	PSENSORSCX_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT pFxDeviceInit
	PWDF_OBJECT_ATTRIBUTES pFdoAttributes
	ULONG Flags
)
{...}

*PFN_SENSORSCXDEVICEINITCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param pFxDeviceInit: 
### -param pFdoAttributes: 
### -param Flags: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also