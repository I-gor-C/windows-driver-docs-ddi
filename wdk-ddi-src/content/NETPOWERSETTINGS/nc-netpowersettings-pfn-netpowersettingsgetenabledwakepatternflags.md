---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSGETENABLEDWAKEPATTERNFLAGS
title: PFN_NETPOWERSETTINGSGETENABLEDWAKEPATTERNFLAGS
author: windows-driver-content
description: 
ms.assetid: ea6f029b-ec19-48ee-b601-19a7be91c11e
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

# PFN_NETPOWERSETTINGSGETENABLEDWAKEPATTERNFLAGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSGETENABLEDWAKEPATTERNFLAGS PfnNetpowersettingsgetenabledwakepatternflags; 

// Definition

WDFAPI PfnNetpowersettingsgetenabledwakepatternflags 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
)
{...}

PFN_NETPOWERSETTINGSGETENABLEDWAKEPATTERNFLAGS 


```

## -parameters

### -param DriverGlobals: 
### -param NetPowerSettings: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also