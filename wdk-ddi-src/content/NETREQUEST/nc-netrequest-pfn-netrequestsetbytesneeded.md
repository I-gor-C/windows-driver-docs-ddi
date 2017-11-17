---
UID: NC.netrequest.PFN_NETREQUESTSETBYTESNEEDED
title: PFN_NETREQUESTSETBYTESNEEDED
author: windows-driver-content
description: 
ms.assetid: 68db14f7-71c6-44b1-82bc-f02cef26ea72
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

# PFN_NETREQUESTSETBYTESNEEDED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTSETBYTESNEEDED PfnNetrequestsetbytesneeded; 

// Definition

WDFAPI PfnNetrequestsetbytesneeded 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
	UINT BytesNeeded
)
{...}

PFN_NETREQUESTSETBYTESNEEDED 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param BytesNeeded: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also