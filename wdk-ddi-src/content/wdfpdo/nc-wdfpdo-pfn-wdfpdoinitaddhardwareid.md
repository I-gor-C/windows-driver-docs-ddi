---
UID: NC.wdfpdo.PFN_WDFPDOINITADDHARDWAREID
title: PFN_WDFPDOINITADDHARDWAREID
author: windows-driver-content
description: 
ms.assetid: d3451820-4a6f-41eb-aa31-f7a1f1478938
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

# PFN_WDFPDOINITADDHARDWAREID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITADDHARDWAREID PfnWdfpdoinitaddhardwareid; 

// Definition

WDFAPI PfnWdfpdoinitaddhardwareid 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PCUNICODE_STRING HardwareID
)
{...}

PFN_WDFPDOINITADDHARDWAREID 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param HardwareID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also