---
UID: NC.wdfpdo.PFN_WDFPDOINITASSIGNINSTANCEID
title: PFN_WDFPDOINITASSIGNINSTANCEID
author: windows-driver-content
description: 
ms.assetid: 2a6c3c05-3a86-4603-80f7-b7df6feaed89
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

# PFN_WDFPDOINITASSIGNINSTANCEID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITASSIGNINSTANCEID PfnWdfpdoinitassigninstanceid; 

// Definition

WDFAPI PfnWdfpdoinitassigninstanceid 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PCUNICODE_STRING InstanceID
)
{...}

PFN_WDFPDOINITASSIGNINSTANCEID 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param InstanceID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also