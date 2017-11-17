---
UID: NC.spbcx.PFN_SPBREQUESTCOMPLETE
title: PFN_SPBREQUESTCOMPLETE
author: windows-driver-content
description: 
ms.assetid: e67a8eb3-bb29-4a8b-874b-3f969b84dcc3
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

# PFN_SPBREQUESTCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBREQUESTCOMPLETE PfnSpbrequestcomplete; 

// Definition

WDFAPI PfnSpbrequestcomplete 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	SPBREQUEST Request
	NTSTATUS CompletionStatus
)
{...}

PFN_SPBREQUESTCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param CompletionStatus: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also