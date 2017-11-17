---
UID: NC.netrequest.PFN_NETREQUESTQUERYDATACOMPLETE
title: PFN_NETREQUESTQUERYDATACOMPLETE
author: windows-driver-content
description: 
ms.assetid: 09fc3b61-581c-44ce-880e-646ffbc65ba1
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

# PFN_NETREQUESTQUERYDATACOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTQUERYDATACOMPLETE PfnNetrequestquerydatacomplete; 

// Definition

WDFAPI PfnNetrequestquerydatacomplete 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
	NTSTATUS CompletionStatus
	UINT BytesWritten
)
{...}

PFN_NETREQUESTQUERYDATACOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param CompletionStatus: 
### -param BytesWritten: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also