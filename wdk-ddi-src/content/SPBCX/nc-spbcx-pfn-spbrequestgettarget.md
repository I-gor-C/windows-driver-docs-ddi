---
UID: NC.spbcx.PFN_SPBREQUESTGETTARGET
title: PFN_SPBREQUESTGETTARGET
author: windows-driver-content
description: 
ms.assetid: 49b36dd7-6d0c-4d83-ae6a-d74a4e600148
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

# PFN_SPBREQUESTGETTARGET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBREQUESTGETTARGET PfnSpbrequestgettarget; 

// Definition

WDFAPI PfnSpbrequestgettarget 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	SPBREQUEST SpbRequest
)
{...}

PFN_SPBREQUESTGETTARGET 


```

## -parameters

### -param DriverGlobals: 
### -param SpbRequest: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also