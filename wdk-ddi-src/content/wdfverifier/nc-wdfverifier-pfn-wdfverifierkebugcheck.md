---
UID: NC.wdfverifier.PFN_WDFVERIFIERKEBUGCHECK
title: *PFN_WDFVERIFIERKEBUGCHECK
author: windows-driver-content
description: 
ms.assetid: 44fa82d4-8b8f-406b-bbfc-66d3697ba0d5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfverifier.h
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

# *PFN_WDFVERIFIERKEBUGCHECK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFVERIFIERKEBUGCHECK *PfnWdfverifierkebugcheck; 

// Definition

VOID *PfnWdfverifierkebugcheck 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	ULONG BugCheckCode
	ULONG_PTR BugCheckParameter1
	ULONG_PTR BugCheckParameter2
	ULONG_PTR BugCheckParameter3
	ULONG_PTR BugCheckParameter4
)
{...}

*PFN_WDFVERIFIERKEBUGCHECK 


```

## -parameters

### -param DriverGlobals: 
### -param BugCheckCode: 
### -param BugCheckParameter1: 
### -param BugCheckParameter2: 
### -param BugCheckParameter3: 
### -param BugCheckParameter4: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also