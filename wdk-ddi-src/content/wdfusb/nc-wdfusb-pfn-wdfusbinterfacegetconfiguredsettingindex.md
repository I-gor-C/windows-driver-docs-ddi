---
UID: NC.wdfusb.PFN_WDFUSBINTERFACEGETCONFIGUREDSETTINGINDEX
title: PFN_WDFUSBINTERFACEGETCONFIGUREDSETTINGINDEX
author: windows-driver-content
description: 
ms.assetid: a31c0426-30e5-48b4-834f-8f856c709945
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBINTERFACEGETCONFIGUREDSETTINGINDEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBINTERFACEGETCONFIGUREDSETTINGINDEX PfnWdfusbinterfacegetconfiguredsettingindex; 

// Definition

WDFAPI PfnWdfusbinterfacegetconfiguredsettingindex 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBINTERFACE Interface
)
{...}

PFN_WDFUSBINTERFACEGETCONFIGUREDSETTINGINDEX 


```

## -parameters

### -param DriverGlobals: 
### -param Interface: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also