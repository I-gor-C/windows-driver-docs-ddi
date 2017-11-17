---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOADCOUNT
title: PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOADCOUNT
author: windows-driver-content
description: 
ms.assetid: d67c9ab4-fc98-4713-baef-e6ca6c4bde81
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

# PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOADCOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOADCOUNT PfnNetpowersettingsgetprotocoloffloadcount; 

// Definition

WDFAPI PfnNetpowersettingsgetprotocoloffloadcount 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
)
{...}

PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOADCOUNT 


```

## -parameters

### -param DriverGlobals: 
### -param NetPowerSettings: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also