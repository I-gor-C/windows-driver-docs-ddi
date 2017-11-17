---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEWDMGETPIPEHANDLE
title: PFN_WDFUSBTARGETPIPEWDMGETPIPEHANDLE
author: windows-driver-content
description: 
ms.assetid: 0d02ff92-323d-4109-9779-1e81144c9708
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBTARGETPIPEWDMGETPIPEHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEWDMGETPIPEHANDLE PfnWdfusbtargetpipewdmgetpipehandle; 

// Definition

WDFAPI PfnWdfusbtargetpipewdmgetpipehandle 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE UsbPipe
)
{...}

PFN_WDFUSBTARGETPIPEWDMGETPIPEHANDLE 


```

## -parameters

### -param DriverGlobals: 
### -param UsbPipe: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also