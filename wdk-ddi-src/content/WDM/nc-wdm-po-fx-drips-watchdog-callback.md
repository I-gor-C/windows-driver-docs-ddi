---
UID: NC.wdm.PO_FX_DRIPS_WATCHDOG_CALLBACK
title: PO_FX_DRIPS_WATCHDOG_CALLBACK
author: windows-driver-content
description: 
ms.assetid: edf9f019-1cb1-4ba7-bcaa-9b665ed4a3fb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PO_FX_DRIPS_WATCHDOG_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PO_FX_DRIPS_WATCHDOG_CALLBACK PoFxDripsWatchdogCallback; 

// Definition

VOID PoFxDripsWatchdogCallback 
(
	PVOID Context
	PDEVICE_OBJECT PhysicalDeviceObject
	ULONG UniqueId
)
{...}

PO_FX_DRIPS_WATCHDOG_CALLBACK PPO_FX_DRIPS_WATCHDOG_CALLBACK


```

## -parameters

### -param Context: 
### -param PhysicalDeviceObject: 
### -param UniqueId: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also