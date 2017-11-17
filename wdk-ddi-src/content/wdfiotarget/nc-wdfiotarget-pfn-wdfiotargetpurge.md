---
UID: NC.wdfiotarget.PFN_WDFIOTARGETPURGE
title: *PFN_WDFIOTARGETPURGE
author: windows-driver-content
description: 
ms.assetid: cab01a1f-0d8a-4c35-9c21-bb727afec2c1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# *PFN_WDFIOTARGETPURGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFIOTARGETPURGE *PfnWdfiotargetpurge; 

// Definition

VOID *PfnWdfiotargetpurge 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	_Strict_type_match_ WDF_IO_TARGET_PURGE_IO_ACTION Action
)
{...}

*PFN_WDFIOTARGETPURGE 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param Action: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also