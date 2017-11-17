---
UID: NC.netrequest.PFN_NETREQUESTSETDATACOMPLETE
title: PFN_NETREQUESTSETDATACOMPLETE
author: windows-driver-content
description: 
ms.assetid: 7753ab3a-3722-4233-ad89-723087756b59
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

# PFN_NETREQUESTSETDATACOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTSETDATACOMPLETE PfnNetrequestsetdatacomplete; 

// Definition

WDFAPI PfnNetrequestsetdatacomplete 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
	NTSTATUS CompletionStatus
	UINT BytesRead
)
{...}

PFN_NETREQUESTSETDATACOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param CompletionStatus: 
### -param BytesRead: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also