---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETPOWERPAGEABLE
title: PFN_WDFDEVICEINITSETPOWERPAGEABLE
author: windows-driver-content
description: 
ms.assetid: 566b2a7f-2eee-47d4-81b9-00f7251df437
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

# PFN_WDFDEVICEINITSETPOWERPAGEABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETPOWERPAGEABLE PfnWdfdeviceinitsetpowerpageable; 

// Definition

WDFAPI PfnWdfdeviceinitsetpowerpageable 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
)
{...}

PFN_WDFDEVICEINITSETPOWERPAGEABLE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also