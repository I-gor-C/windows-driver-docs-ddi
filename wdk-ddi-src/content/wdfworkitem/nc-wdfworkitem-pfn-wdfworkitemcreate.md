---
UID: NC.wdfworkitem.PFN_WDFWORKITEMCREATE
title: PFN_WDFWORKITEMCREATE
author: windows-driver-content
description: 
ms.assetid: c15995c8-bf80-4a60-960b-4f0307285625
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfworkitem.h
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

# PFN_WDFWORKITEMCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWORKITEMCREATE PfnWdfworkitemcreate; 

// Definition

WDFAPI PfnWdfworkitemcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_WORKITEM_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFWORKITEM *WorkItem
)
{...}

PFN_WDFWORKITEMCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Config: 
### -param Attributes: 
### -param *WorkItem: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also