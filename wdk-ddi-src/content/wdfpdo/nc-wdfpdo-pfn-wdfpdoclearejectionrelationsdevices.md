---
UID: NC.wdfpdo.PFN_WDFPDOCLEAREJECTIONRELATIONSDEVICES
title: PFN_WDFPDOCLEAREJECTIONRELATIONSDEVICES
author: windows-driver-content
description: 
ms.assetid: 54956877-8711-4c69-b462-54720b95404f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfpdo.h
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

# PFN_WDFPDOCLEAREJECTIONRELATIONSDEVICES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOCLEAREJECTIONRELATIONSDEVICES PfnWdfpdoclearejectionrelationsdevices; 

// Definition

WDFAPI PfnWdfpdoclearejectionrelationsdevices 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_WDFPDOCLEAREJECTIONRELATIONSDEVICES 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also