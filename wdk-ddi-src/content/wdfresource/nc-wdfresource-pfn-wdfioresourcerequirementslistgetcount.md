---
UID: NC.wdfresource.PFN_WDFIORESOURCEREQUIREMENTSLISTGETCOUNT
title: PFN_WDFIORESOURCEREQUIREMENTSLISTGETCOUNT
author: windows-driver-content
description: 
ms.assetid: 6c8aa5a0-b8e1-4583-8b90-009dbd605b70
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

# PFN_WDFIORESOURCEREQUIREMENTSLISTGETCOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCEREQUIREMENTSLISTGETCOUNT PfnWdfioresourcerequirementslistgetcount; 

// Definition

WDFAPI PfnWdfioresourcerequirementslistgetcount 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESREQLIST RequirementsList
)
{...}

PFN_WDFIORESOURCEREQUIREMENTSLISTGETCOUNT 


```

## -parameters

### -param DriverGlobals: 
### -param RequirementsList: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also