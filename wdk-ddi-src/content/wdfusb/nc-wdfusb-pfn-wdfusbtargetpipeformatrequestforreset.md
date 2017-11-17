---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEFORMATREQUESTFORRESET
title: PFN_WDFUSBTARGETPIPEFORMATREQUESTFORRESET
author: windows-driver-content
description: 
ms.assetid: 298dcc55-b467-4754-8fc0-64f1d0a422ba
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

# PFN_WDFUSBTARGETPIPEFORMATREQUESTFORRESET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORRESET PfnWdfusbtargetpipeformatrequestforreset; 

// Definition

WDFAPI PfnWdfusbtargetpipeformatrequestforreset 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	WDFREQUEST Request
)
{...}

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORRESET 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also