---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSGETWAKEPATTERN
title: PFN_NETPOWERSETTINGSGETWAKEPATTERN
author: windows-driver-content
description: 
ms.assetid: 97467064-d6a5-4f62-88c7-1f429c47c9f0
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

# PFN_NETPOWERSETTINGSGETWAKEPATTERN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSGETWAKEPATTERN PfnNetpowersettingsgetwakepattern; 

// Definition

WDFAPI PfnNetpowersettingsgetwakepattern 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
	ULONG Index
)
{...}

PFN_NETPOWERSETTINGSGETWAKEPATTERN 


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