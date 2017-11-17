---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETIOINCALLERCONTEXTCALLBACK
title: PFN_WDFDEVICEINITSETIOINCALLERCONTEXTCALLBACK
author: windows-driver-content
description: 
ms.assetid: e961e696-aca8-4962-a573-c901390cec49
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICEINITSETIOINCALLERCONTEXTCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETIOINCALLERCONTEXTCALLBACK PfnWdfdeviceinitsetioincallercontextcallback; 

// Definition

WDFAPI PfnWdfdeviceinitsetioincallercontextcallback 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PFN_WDF_IO_IN_CALLER_CONTEXT EvtIoInCallerContext
)
{...}

PFN_WDFDEVICEINITSETIOINCALLERCONTEXTCALLBACK 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param EvtIoInCallerContext: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also