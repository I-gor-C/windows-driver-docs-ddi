---
UID: NC.wdfdevice.PFN_WDFDEVICESETALIGNMENTREQUIREMENT
title: PFN_WDFDEVICESETALIGNMENTREQUIREMENT
author: windows-driver-content
description: 
ms.assetid: 430be8a1-4a3a-4eaa-9aa2-458f140ac772
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICESETALIGNMENTREQUIREMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICESETALIGNMENTREQUIREMENT PfnWdfdevicesetalignmentrequirement; 

// Definition

WDFAPI PfnWdfdevicesetalignmentrequirement 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	ULONG AlignmentRequirement
)
{...}

PFN_WDFDEVICESETALIGNMENTREQUIREMENT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param AlignmentRequirement: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also