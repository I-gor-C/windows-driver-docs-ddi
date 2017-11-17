---
UID: NC.netrequest.PFN_NETREQUESTGETPORTNUMBER
title: PFN_NETREQUESTGETPORTNUMBER
author: windows-driver-content
description: 
ms.assetid: c8a18d91-4bba-4963-a946-93c90de4bae3
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

# PFN_NETREQUESTGETPORTNUMBER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTGETPORTNUMBER PfnNetrequestgetportnumber; 

// Definition

WDFAPI PfnNetrequestgetportnumber 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
)
{...}

PFN_NETREQUESTGETPORTNUMBER 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also