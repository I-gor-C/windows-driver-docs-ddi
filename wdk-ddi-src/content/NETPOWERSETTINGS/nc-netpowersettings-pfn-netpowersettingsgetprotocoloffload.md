---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOAD
title: PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOAD
author: windows-driver-content
description: 
ms.assetid: 2bff9edd-fcfc-40c3-95a2-e99ef638f473
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

# PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOAD PfnNetpowersettingsgetprotocoloffload; 

// Definition

WDFAPI PfnNetpowersettingsgetprotocoloffload 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
	ULONG Index
)
{...}

PFN_NETPOWERSETTINGSGETPROTOCOLOFFLOAD 


```

## -parameters

### -param DriverGlobals: 
### -param NetPowerSettings: 
### -param Index: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also