---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTSETEXTENDEDPOLICY
title: PFN_WDFINTERRUPTSETEXTENDEDPOLICY
author: windows-driver-content
description: 
ms.assetid: edbadaff-fafb-4f86-9ff4-f56d8b814a91
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfinterrupt.h
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

# PFN_WDFINTERRUPTSETEXTENDEDPOLICY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTSETEXTENDEDPOLICY PfnWdfinterruptsetextendedpolicy; 

// Definition

WDFAPI PfnWdfinterruptsetextendedpolicy 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
	PWDF_INTERRUPT_EXTENDED_POLICY PolicyAndGroup
)
{...}

PFN_WDFINTERRUPTSETEXTENDEDPOLICY 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 
### -param PolicyAndGroup: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also