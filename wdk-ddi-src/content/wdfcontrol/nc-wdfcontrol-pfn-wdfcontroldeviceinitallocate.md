---
UID: NC.wdfcontrol.PFN_WDFCONTROLDEVICEINITALLOCATE
title: PFN_WDFCONTROLDEVICEINITALLOCATE
author: windows-driver-content
description: 
ms.assetid: be791e01-be38-448f-b495-d86d587e2bf7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcontrol.h
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

# PFN_WDFCONTROLDEVICEINITALLOCATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCONTROLDEVICEINITALLOCATE PfnWdfcontroldeviceinitallocate; 

// Definition

WDFAPI PfnWdfcontroldeviceinitallocate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
	CONST UNICODE_STRING
)
{...}

PFN_WDFCONTROLDEVICEINITALLOCATE 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 
### -param UNICODE_STRING: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also