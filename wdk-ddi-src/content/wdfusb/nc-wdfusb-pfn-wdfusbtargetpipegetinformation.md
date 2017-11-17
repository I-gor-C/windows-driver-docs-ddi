---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEGETINFORMATION
title: PFN_WDFUSBTARGETPIPEGETINFORMATION
author: windows-driver-content
description: 
ms.assetid: fab669ba-a48c-4a0e-bdf5-f073604f6a98
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

# PFN_WDFUSBTARGETPIPEGETINFORMATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEGETINFORMATION PfnWdfusbtargetpipegetinformation; 

// Definition

WDFAPI PfnWdfusbtargetpipegetinformation 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	PWDF_USB_PIPE_INFORMATION PipeInformation
)
{...}

PFN_WDFUSBTARGETPIPEGETINFORMATION 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param PipeInformation: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also