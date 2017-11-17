---
UID: NC.wdfresource.PFN_WDFIORESOURCEREQUIREMENTSLISTINSERTIORESLIST
title: PFN_WDFIORESOURCEREQUIREMENTSLISTINSERTIORESLIST
author: windows-driver-content
description: 
ms.assetid: 25d14b1d-1501-4363-8280-fdb551e27faa
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

# PFN_WDFIORESOURCEREQUIREMENTSLISTINSERTIORESLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCEREQUIREMENTSLISTINSERTIORESLIST PfnWdfioresourcerequirementslistinsertioreslist; 

// Definition

WDFAPI PfnWdfioresourcerequirementslistinsertioreslist 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESREQLIST RequirementsList
	WDFIORESLIST IoResList
	ULONG Index
)
{...}

PFN_WDFIORESOURCEREQUIREMENTSLISTINSERTIORESLIST 


```

## -parameters

### -param DriverGlobals: 
### -param RequirementsList: 
### -param IoResList: 
### -param Index: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also