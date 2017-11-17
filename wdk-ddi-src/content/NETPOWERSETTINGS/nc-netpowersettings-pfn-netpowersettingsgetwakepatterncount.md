---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSGETWAKEPATTERNCOUNT
title: PFN_NETPOWERSETTINGSGETWAKEPATTERNCOUNT
author: windows-driver-content
description: 
ms.assetid: d63efac6-b3d8-452c-9fa2-748af9bd641c
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

# PFN_NETPOWERSETTINGSGETWAKEPATTERNCOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSGETWAKEPATTERNCOUNT PfnNetpowersettingsgetwakepatterncount; 

// Definition

WDFAPI PfnNetpowersettingsgetwakepatterncount 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
)
{...}

PFN_NETPOWERSETTINGSGETWAKEPATTERNCOUNT 


```

## -parameters

### -param DriverGlobals: 
### -param NetPowerSettings: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also