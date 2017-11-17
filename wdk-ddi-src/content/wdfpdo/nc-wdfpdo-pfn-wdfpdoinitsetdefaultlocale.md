---
UID: NC.wdfpdo.PFN_WDFPDOINITSETDEFAULTLOCALE
title: PFN_WDFPDOINITSETDEFAULTLOCALE
author: windows-driver-content
description: 
ms.assetid: a1f1c66a-0762-426f-aafc-97ea51753956
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

# PFN_WDFPDOINITSETDEFAULTLOCALE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITSETDEFAULTLOCALE PfnWdfpdoinitsetdefaultlocale; 

// Definition

WDFAPI PfnWdfpdoinitsetdefaultlocale 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	LCID LocaleId
)
{...}

PFN_WDFPDOINITSETDEFAULTLOCALE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param LocaleId: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also