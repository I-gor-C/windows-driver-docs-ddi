---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSGETENABLEDMEDIASPECIFICWAKEUPEVENTS
title: PFN_NETPOWERSETTINGSGETENABLEDMEDIASPECIFICWAKEUPEVENTS
author: windows-driver-content
description: 
ms.assetid: 8d64f5aa-abfc-466a-affa-e0170e0de40f
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

# PFN_NETPOWERSETTINGSGETENABLEDMEDIASPECIFICWAKEUPEVENTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSGETENABLEDMEDIASPECIFICWAKEUPEVENTS PfnNetpowersettingsgetenabledmediaspecificwakeupevents; 

// Definition

WDFAPI PfnNetpowersettingsgetenabledmediaspecificwakeupevents 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
)
{...}

PFN_NETPOWERSETTINGSGETENABLEDMEDIASPECIFICWAKEUPEVENTS 


```

## -parameters

### -param DriverGlobals: 
### -param NetPowerSettings: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also