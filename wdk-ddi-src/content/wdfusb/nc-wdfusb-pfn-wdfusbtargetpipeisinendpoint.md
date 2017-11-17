---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEISINENDPOINT
title: PFN_WDFUSBTARGETPIPEISINENDPOINT
author: windows-driver-content
description: 
ms.assetid: 497a4eb3-c7d8-4977-854b-9ef8f5851339
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

# PFN_WDFUSBTARGETPIPEISINENDPOINT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEISINENDPOINT PfnWdfusbtargetpipeisinendpoint; 

// Definition

WDFAPI PfnWdfusbtargetpipeisinendpoint 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
)
{...}

PFN_WDFUSBTARGETPIPEISINENDPOINT 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also