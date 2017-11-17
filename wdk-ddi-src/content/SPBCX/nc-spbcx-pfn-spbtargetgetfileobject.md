---
UID: NC.spbcx.PFN_SPBTARGETGETFILEOBJECT
title: PFN_SPBTARGETGETFILEOBJECT
author: windows-driver-content
description: 
ms.assetid: 1eea7886-d124-4fa6-b04c-9208bf9f2e3e
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

# PFN_SPBTARGETGETFILEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBTARGETGETFILEOBJECT PfnSpbtargetgetfileobject; 

// Definition

WDFAPI PfnSpbtargetgetfileobject 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	SPBTARGET Target
)
{...}

PFN_SPBTARGETGETFILEOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param Target: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also