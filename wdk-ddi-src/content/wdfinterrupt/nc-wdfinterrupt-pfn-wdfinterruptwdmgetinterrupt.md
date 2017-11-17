---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTWDMGETINTERRUPT
title: *PFN_WDFINTERRUPTWDMGETINTERRUPT
author: windows-driver-content
description: 
ms.assetid: e4ddaee4-b2a8-4d67-91ba-340828fff0b3
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

# *PFN_WDFINTERRUPTWDMGETINTERRUPT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFINTERRUPTWDMGETINTERRUPT *PfnWdfinterruptwdmgetinterrupt; 

// Definition

PKINTERRUPT *PfnWdfinterruptwdmgetinterrupt 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
)
{...}

*PFN_WDFINTERRUPTWDMGETINTERRUPT 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 



## -returns

Returns PKINTERRUPT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also