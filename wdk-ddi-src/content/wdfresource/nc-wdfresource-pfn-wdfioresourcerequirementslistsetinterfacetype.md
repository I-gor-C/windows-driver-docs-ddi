---
UID: NC.wdfresource.PFN_WDFIORESOURCEREQUIREMENTSLISTSETINTERFACETYPE
title: PFN_WDFIORESOURCEREQUIREMENTSLISTSETINTERFACETYPE
author: windows-driver-content
description: 
ms.assetid: 510aadaa-10a9-4fbf-a84a-5bd022ce395e
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

# PFN_WDFIORESOURCEREQUIREMENTSLISTSETINTERFACETYPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCEREQUIREMENTSLISTSETINTERFACETYPE PfnWdfioresourcerequirementslistsetinterfacetype; 

// Definition

WDFAPI PfnWdfioresourcerequirementslistsetinterfacetype 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESREQLIST RequirementsList
	_Strict_type_match_ INTERFACE_TYPE
)
{...}

PFN_WDFIORESOURCEREQUIREMENTSLISTSETINTERFACETYPE 


```

## -parameters

### -param DriverGlobals: 
### -param RequirementsList: 
### -param INTERFACE_TYPE: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also