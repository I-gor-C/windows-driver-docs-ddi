---
UID: NC.netrequest.PFN_NETREQUESTGETTYPE
title: PFN_NETREQUESTGETTYPE
author: windows-driver-content
description: 
ms.assetid: 6c5cd030-4e31-4a75-bacc-0dd07cdf2a24
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrequest.h
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

# PFN_NETREQUESTGETTYPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTGETTYPE PfnNetrequestgettype; 

// Definition

WDFAPI PfnNetrequestgettype 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
)
{...}

PFN_NETREQUESTGETTYPE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also