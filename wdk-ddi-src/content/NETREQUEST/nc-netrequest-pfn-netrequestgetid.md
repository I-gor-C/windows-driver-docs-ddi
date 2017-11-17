---
UID: NC.netrequest.PFN_NETREQUESTGETID
title: PFN_NETREQUESTGETID
author: windows-driver-content
description: 
ms.assetid: dca74491-b7ab-4287-ba8b-eaaa2646ae02
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

# PFN_NETREQUESTGETID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTGETID PfnNetrequestgetid; 

// Definition

WDFAPI PfnNetrequestgetid 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
)
{...}

PFN_NETREQUESTGETID 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also