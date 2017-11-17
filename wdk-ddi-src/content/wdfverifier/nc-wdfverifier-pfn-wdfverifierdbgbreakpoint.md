---
UID: NC.wdfverifier.PFN_WDFVERIFIERDBGBREAKPOINT
title: *PFN_WDFVERIFIERDBGBREAKPOINT
author: windows-driver-content
description: 
ms.assetid: 12a6c645-5634-41cf-ac96-31d57fd0357d
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

# *PFN_WDFVERIFIERDBGBREAKPOINT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFVERIFIERDBGBREAKPOINT *PfnWdfverifierdbgbreakpoint; 

// Definition

VOID *PfnWdfverifierdbgbreakpoint 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
)
{...}

*PFN_WDFVERIFIERDBGBREAKPOINT 


```

## -parameters

### -param DriverGlobals: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also