---
UID: NC.wdfresource.PFN_WDFCMRESOURCELISTGETCOUNT
title: PFN_WDFCMRESOURCELISTGETCOUNT
author: windows-driver-content
description: 
ms.assetid: 378d0c71-bc8c-40d3-b1c3-5ad7dff7532e
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

# PFN_WDFCMRESOURCELISTGETCOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCMRESOURCELISTGETCOUNT PfnWdfcmresourcelistgetcount; 

// Definition

WDFAPI PfnWdfcmresourcelistgetcount 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCMRESLIST List
)
{...}

PFN_WDFCMRESOURCELISTGETCOUNT 


```

## -parameters

### -param DriverGlobals: 
### -param List: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also