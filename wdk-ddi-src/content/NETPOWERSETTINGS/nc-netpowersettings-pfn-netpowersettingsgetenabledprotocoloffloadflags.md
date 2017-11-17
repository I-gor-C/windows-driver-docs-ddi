---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSGETENABLEDPROTOCOLOFFLOADFLAGS
title: PFN_NETPOWERSETTINGSGETENABLEDPROTOCOLOFFLOADFLAGS
author: windows-driver-content
description: 
ms.assetid: 917bf3c0-96cf-4ee7-8b14-9dea1fc290a4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netpowersettings.h
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

# PFN_NETPOWERSETTINGSGETENABLEDPROTOCOLOFFLOADFLAGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSGETENABLEDPROTOCOLOFFLOADFLAGS PfnNetpowersettingsgetenabledprotocoloffloadflags; 

// Definition

WDFAPI PfnNetpowersettingsgetenabledprotocoloffloadflags 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
)
{...}

PFN_NETPOWERSETTINGSGETENABLEDPROTOCOLOFFLOADFLAGS 


```

## -parameters

### -param DriverGlobals: 
### -param NetPowerSettings: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also