---
UID: NC.wdfresource.PFN_WDFIORESOURCELISTCREATE
title: PFN_WDFIORESOURCELISTCREATE
author: windows-driver-content
description: 
ms.assetid: b48e6a11-ff6a-4971-a0c4-158676e59456
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

# PFN_WDFIORESOURCELISTCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCELISTCREATE PfnWdfioresourcelistcreate; 

// Definition

WDFAPI PfnWdfioresourcelistcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESREQLIST RequirementsList
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFIORESLIST *ResourceList
)
{...}

PFN_WDFIORESOURCELISTCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param RequirementsList: 
### -param Attributes: 
### -param *ResourceList: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also