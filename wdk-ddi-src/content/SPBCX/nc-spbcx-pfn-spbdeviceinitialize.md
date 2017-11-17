---
UID: NC.spbcx.PFN_SPBDEVICEINITIALIZE
title: PFN_SPBDEVICEINITIALIZE
author: windows-driver-content
description: 
ms.assetid: a7e65fd9-4de7-4be4-bb37-768f5524c486
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# PFN_SPBDEVICEINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBDEVICEINITIALIZE PfnSpbdeviceinitialize; 

// Definition

WDFAPI PfnSpbdeviceinitialize 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE FxDevice
	PSPB_CONTROLLER_CONFIG Config
)
{...}

PFN_SPBDEVICEINITIALIZE 


```

## -parameters

### -param DriverGlobals: 
### -param FxDevice: 
### -param Config: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also