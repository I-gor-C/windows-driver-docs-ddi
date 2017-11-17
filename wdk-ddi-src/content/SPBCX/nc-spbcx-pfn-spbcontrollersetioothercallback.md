---
UID: NC.spbcx.PFN_SPBCONTROLLERSETIOOTHERCALLBACK
title: PFN_SPBCONTROLLERSETIOOTHERCALLBACK
author: windows-driver-content
description: 
ms.assetid: 69aee92f-0321-4b78-b637-47a9732752fd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# PFN_SPBCONTROLLERSETIOOTHERCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBCONTROLLERSETIOOTHERCALLBACK PfnSpbcontrollersetioothercallback; 

// Definition

WDFAPI PfnSpbcontrollersetioothercallback 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE FxDevice
	PFN_SPB_CONTROLLER_OTHER EvtSpbControllerIoOther
	PFN_WDF_IO_IN_CALLER_CONTEXT EvtIoInCallerContext
)
{...}

PFN_SPBCONTROLLERSETIOOTHERCALLBACK 


```

## -parameters

### -param DriverGlobals: 
### -param FxDevice: 
### -param EvtSpbControllerIoOther: 
### -param EvtIoInCallerContext: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also