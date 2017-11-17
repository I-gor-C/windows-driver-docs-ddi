---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETEXCLUSIVE
title: PFN_WDFDEVICEINITSETEXCLUSIVE
author: windows-driver-content
description: 
ms.assetid: 777ce5ae-1a40-4fd9-85d5-be87884191d2
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

# PFN_WDFDEVICEINITSETEXCLUSIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETEXCLUSIVE PfnWdfdeviceinitsetexclusive; 

// Definition

WDFAPI PfnWdfdeviceinitsetexclusive 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	BOOLEAN IsExclusive
)
{...}

PFN_WDFDEVICEINITSETEXCLUSIVE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param IsExclusive: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also