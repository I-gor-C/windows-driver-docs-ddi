---
UID: NC.netpowersettings.PFN_NETPOWERSETTINGSISPROTOCOLOFFLOADENABLED
title: PFN_NETPOWERSETTINGSISPROTOCOLOFFLOADENABLED
author: windows-driver-content
description: 
ms.assetid: 7592c90c-b7b5-4731-9c47-31899fdeee62
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

# PFN_NETPOWERSETTINGSISPROTOCOLOFFLOADENABLED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPOWERSETTINGSISPROTOCOLOFFLOADENABLED PfnNetpowersettingsisprotocoloffloadenabled; 

// Definition

WDFAPI PfnNetpowersettingsisprotocoloffloadenabled 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETPOWERSETTINGS NetPowerSettings
	PNDIS_PM_PROTOCOL_OFFLOAD NdisProtocolOffload
)
{...}

PFN_NETPOWERSETTINGSISPROTOCOLOFFLOADENABLED 


```

## -parameters

### -param DriverGlobals: 
### -param NetPowerSettings: 
### -param NdisProtocolOffload: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also