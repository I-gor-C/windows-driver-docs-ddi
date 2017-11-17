---
UID: NC.netrequest.PFN_NETREQUESTCOMPLETEWITHOUTINFORMATION
title: PFN_NETREQUESTCOMPLETEWITHOUTINFORMATION
author: windows-driver-content
description: 
ms.assetid: 24199d33-bcc9-4979-9ca7-585aa4c9513d
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

# PFN_NETREQUESTCOMPLETEWITHOUTINFORMATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTCOMPLETEWITHOUTINFORMATION PfnNetrequestcompletewithoutinformation; 

// Definition

WDFAPI PfnNetrequestcompletewithoutinformation 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
	NTSTATUS CompletionStatus
)
{...}

PFN_NETREQUESTCOMPLETEWITHOUTINFORMATION 


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