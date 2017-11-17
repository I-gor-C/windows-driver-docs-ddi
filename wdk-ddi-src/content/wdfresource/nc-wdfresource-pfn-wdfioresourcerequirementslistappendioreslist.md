---
UID: NC.wdfresource.PFN_WDFIORESOURCEREQUIREMENTSLISTAPPENDIORESLIST
title: PFN_WDFIORESOURCEREQUIREMENTSLISTAPPENDIORESLIST
author: windows-driver-content
description: 
ms.assetid: b54bf85c-3f06-4e3a-b617-a1d48852ae43
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

# PFN_WDFIORESOURCEREQUIREMENTSLISTAPPENDIORESLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCEREQUIREMENTSLISTAPPENDIORESLIST PfnWdfioresourcerequirementslistappendioreslist; 

// Definition

WDFAPI PfnWdfioresourcerequirementslistappendioreslist 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESREQLIST RequirementsList
	WDFIORESLIST IoResList
)
{...}

PFN_WDFIORESOURCEREQUIREMENTSLISTAPPENDIORESLIST 


```

## -parameters

### -param DriverGlobals: 
### -param RequirementsList: 
### -param IoResList: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also