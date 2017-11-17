---
UID: NC.wdfresource.PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER
title: PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER
author: windows-driver-content
description: 
ms.assetid: b4762104-5b2e-4129-9a1d-984d23bf546e
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

# PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER PfnWdfioresourcerequirementslistsetslotnumber; 

// Definition

WDFAPI PfnWdfioresourcerequirementslistsetslotnumber 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESREQLIST RequirementsList
	ULONG SlotNumber
)
{...}

PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER 


```

## -parameters

### -param DriverGlobals: 
### -param RequirementsList: 
### -param SlotNumber: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also