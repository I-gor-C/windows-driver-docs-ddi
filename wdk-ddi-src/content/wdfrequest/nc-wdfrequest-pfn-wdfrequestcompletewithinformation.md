---
UID: NC.wdfrequest.PFN_WDFREQUESTCOMPLETEWITHINFORMATION
title: PFN_WDFREQUESTCOMPLETEWITHINFORMATION
author: windows-driver-content
description: 
ms.assetid: 8e77d31b-4a96-43e1-b20d-48ff7a07f95b
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

# PFN_WDFREQUESTCOMPLETEWITHINFORMATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTCOMPLETEWITHINFORMATION PfnWdfrequestcompletewithinformation; 

// Definition

WDFAPI PfnWdfrequestcompletewithinformation 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	NTSTATUS Status
	ULONG_PTR Information
)
{...}

PFN_WDFREQUESTCOMPLETEWITHINFORMATION 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Status: 
### -param Information: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also