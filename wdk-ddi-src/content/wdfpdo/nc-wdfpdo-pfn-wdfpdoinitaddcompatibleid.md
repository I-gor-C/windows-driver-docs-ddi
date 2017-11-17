---
UID: NC.wdfpdo.PFN_WDFPDOINITADDCOMPATIBLEID
title: PFN_WDFPDOINITADDCOMPATIBLEID
author: windows-driver-content
description: 
ms.assetid: 04be7f19-a764-4964-b95f-2f04b3ad9e96
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

# PFN_WDFPDOINITADDCOMPATIBLEID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITADDCOMPATIBLEID PfnWdfpdoinitaddcompatibleid; 

// Definition

WDFAPI PfnWdfpdoinitaddcompatibleid 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PCUNICODE_STRING CompatibleID
)
{...}

PFN_WDFPDOINITADDCOMPATIBLEID 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param CompatibleID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also