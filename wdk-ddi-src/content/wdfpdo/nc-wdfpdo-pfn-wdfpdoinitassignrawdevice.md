---
UID: NC.wdfpdo.PFN_WDFPDOINITASSIGNRAWDEVICE
title: PFN_WDFPDOINITASSIGNRAWDEVICE
author: windows-driver-content
description: 
ms.assetid: ce9a3074-503f-455e-a13d-87c30de08f67
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

# PFN_WDFPDOINITASSIGNRAWDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITASSIGNRAWDEVICE PfnWdfpdoinitassignrawdevice; 

// Definition

WDFAPI PfnWdfpdoinitassignrawdevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	CONST GUID
)
{...}

PFN_WDFPDOINITASSIGNRAWDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param GUID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also