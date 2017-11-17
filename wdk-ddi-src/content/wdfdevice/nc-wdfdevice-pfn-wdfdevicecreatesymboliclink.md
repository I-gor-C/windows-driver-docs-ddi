---
UID: NC.wdfdevice.PFN_WDFDEVICECREATESYMBOLICLINK
title: PFN_WDFDEVICECREATESYMBOLICLINK
author: windows-driver-content
description: 
ms.assetid: f99b892b-4dc4-4b0b-93aa-27e92297c8ef
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

# PFN_WDFDEVICECREATESYMBOLICLINK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICECREATESYMBOLICLINK PfnWdfdevicecreatesymboliclink; 

// Definition

WDFAPI PfnWdfdevicecreatesymboliclink 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PCUNICODE_STRING SymbolicLinkName
)
{...}

PFN_WDFDEVICECREATESYMBOLICLINK 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param SymbolicLinkName: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also