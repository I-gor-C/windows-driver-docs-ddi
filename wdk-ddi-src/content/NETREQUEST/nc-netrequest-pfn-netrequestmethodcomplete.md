---
UID: NC.netrequest.PFN_NETREQUESTMETHODCOMPLETE
title: PFN_NETREQUESTMETHODCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 4dc6a0fa-1d72-4b6c-96f7-347b708e2410
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

# PFN_NETREQUESTMETHODCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTMETHODCOMPLETE PfnNetrequestmethodcomplete; 

// Definition

WDFAPI PfnNetrequestmethodcomplete 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
	NTSTATUS CompletionStatus
	UINT BytesRead
	UINT BytesWritten
)
{...}

PFN_NETREQUESTMETHODCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param CompletionStatus: 
### -param BytesRead: 
### -param BytesWritten: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also