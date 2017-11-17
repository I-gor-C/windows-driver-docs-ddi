---
UID: NC.wdfdevice.PFN_WDFDEVICEINITASSIGNSDDLSTRING
title: PFN_WDFDEVICEINITASSIGNSDDLSTRING
author: windows-driver-content
description: 
ms.assetid: 3709cce3-33b6-41c1-b071-53dae06f2edc
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

# PFN_WDFDEVICEINITASSIGNSDDLSTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITASSIGNSDDLSTRING PfnWdfdeviceinitassignsddlstring; 

// Definition

WDFAPI PfnWdfdeviceinitassignsddlstring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PCUNICODE_STRING SDDLString
)
{...}

PFN_WDFDEVICEINITASSIGNSDDLSTRING 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param SDDLString: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also