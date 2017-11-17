---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETPOWERPOLICYOWNERSHIP
title: PFN_WDFDEVICEINITSETPOWERPOLICYOWNERSHIP
author: windows-driver-content
description: 
ms.assetid: 1e18e57a-95a7-40ec-8a83-4bcaa6d1a0ca
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

# PFN_WDFDEVICEINITSETPOWERPOLICYOWNERSHIP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETPOWERPOLICYOWNERSHIP PfnWdfdeviceinitsetpowerpolicyownership; 

// Definition

WDFAPI PfnWdfdeviceinitsetpowerpolicyownership 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	BOOLEAN IsPowerPolicyOwner
)
{...}

PFN_WDFDEVICEINITSETPOWERPOLICYOWNERSHIP 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param IsPowerPolicyOwner: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also