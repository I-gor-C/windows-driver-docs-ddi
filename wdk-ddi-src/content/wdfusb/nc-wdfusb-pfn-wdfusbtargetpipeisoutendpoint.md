---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEISOUTENDPOINT
title: PFN_WDFUSBTARGETPIPEISOUTENDPOINT
author: windows-driver-content
description: 
ms.assetid: 59e45c05-84c4-4db9-9df8-6b1e41d8f26d
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

# PFN_WDFUSBTARGETPIPEISOUTENDPOINT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEISOUTENDPOINT PfnWdfusbtargetpipeisoutendpoint; 

// Definition

WDFAPI PfnWdfusbtargetpipeisoutendpoint 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
)
{...}

PFN_WDFUSBTARGETPIPEISOUTENDPOINT 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also