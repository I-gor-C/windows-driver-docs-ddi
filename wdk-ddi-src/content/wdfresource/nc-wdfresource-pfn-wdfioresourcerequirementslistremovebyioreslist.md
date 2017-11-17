---
UID: NC.wdfresource.PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVEBYIORESLIST
title: PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVEBYIORESLIST
author: windows-driver-content
description: 
ms.assetid: c11b80dc-5757-4e97-ab4d-0b5544b6c1af
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

# PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVEBYIORESLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVEBYIORESLIST PfnWdfioresourcerequirementslistremovebyioreslist; 

// Definition

WDFAPI PfnWdfioresourcerequirementslistremovebyioreslist 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESREQLIST RequirementsList
	WDFIORESLIST IoResList
)
{...}

PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVEBYIORESLIST 


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