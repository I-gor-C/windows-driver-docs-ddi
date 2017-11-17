---
UID: NC.wdfresource.PFN_WDFIORESOURCEREQUIREMENTSLISTGETIORESLIST
title: PFN_WDFIORESOURCEREQUIREMENTSLISTGETIORESLIST
author: windows-driver-content
description: 
ms.assetid: 68b0d649-e8ea-429c-baa0-0da601224167
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfresource.h
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

# PFN_WDFIORESOURCEREQUIREMENTSLISTGETIORESLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCEREQUIREMENTSLISTGETIORESLIST PfnWdfioresourcerequirementslistgetioreslist; 

// Definition

WDFAPI PfnWdfioresourcerequirementslistgetioreslist 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESREQLIST RequirementsList
	ULONG Index
)
{...}

PFN_WDFIORESOURCEREQUIREMENTSLISTGETIORESLIST 


```

## -parameters

### -param DriverGlobals: 
### -param RequirementsList: 
### -param Index: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also