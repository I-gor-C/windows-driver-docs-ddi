---
UID: NC.wdfrequest.PFN_WDFREQUESTIMPERSONATE
title: PFN_WDFREQUESTIMPERSONATE
author: windows-driver-content
description: 
ms.assetid: d168bfd4-9a69-446c-9258-a325369fc94b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTIMPERSONATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTIMPERSONATE PfnWdfrequestimpersonate; 

// Definition

WDFAPI PfnWdfrequestimpersonate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	SECURITY_IMPERSONATION_LEVEL ImpersonationLevel
	PFN_WDF_REQUEST_IMPERSONATE EvtRequestImpersonate
	PVOID Context
)
{...}

PFN_WDFREQUESTIMPERSONATE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param ImpersonationLevel: 
### -param EvtRequestImpersonate: 
### -param Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also