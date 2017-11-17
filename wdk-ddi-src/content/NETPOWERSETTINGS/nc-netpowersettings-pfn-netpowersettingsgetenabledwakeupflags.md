---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSGETENABLEDWAKEUPFLAGS
title: PFN_NETPOWERSETTINGSGETENABLEDWAKEUPFLAGS
author: windows-driver-content
description: 
ms.assetid: 4c391741-64af-4130-bc04-6c624e17bff5
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

# PFN_NETPOWERSETTINGSGETENABLEDWAKEUPFLAGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSGETENABLEDWAKEUPFLAGS PfnNetpowersettingsgetenabledwakeupflags; 

// Definition

WDFAPI PfnNetpowersettingsgetenabledwakeupflags 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
)
{...}

PFN_NETPOWERSETTINGSGETENABLEDWAKEUPFLAGS 


```

## -parameters

### -param DriverGlobals: 
### -param NetPowerSettings: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also