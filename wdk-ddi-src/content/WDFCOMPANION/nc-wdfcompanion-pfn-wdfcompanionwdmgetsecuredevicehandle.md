---
UID: NC.wdfcompanion.PFN_WDFCOMPANIONWDMGETSECUREDEVICEHANDLE
title: PFN_WDFCOMPANIONWDMGETSECUREDEVICEHANDLE
author: windows-driver-content
description: 
ms.assetid: 2e3ba846-10c4-4a1a-912b-b06bab0464b3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcompanion.h
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

# PFN_WDFCOMPANIONWDMGETSECUREDEVICEHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMPANIONWDMGETSECUREDEVICEHANDLE PfnWdfcompanionwdmgetsecuredevicehandle; 

// Definition

WDFAPI PfnWdfcompanionwdmgetsecuredevicehandle 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOMPANION Companion
)
{...}

PFN_WDFCOMPANIONWDMGETSECUREDEVICEHANDLE 


```

## -parameters

### -param DriverGlobals: 
### -param Companion: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also