---
UID: NC.wdfwmi.PFN_WDFWMIPROVIDERCREATE
title: PFN_WDFWMIPROVIDERCREATE
author: windows-driver-content
description: 
ms.assetid: d7fa6a9b-a431-4eba-9ed1-5462e09403a3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfwmi.h
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

# PFN_WDFWMIPROVIDERCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWMIPROVIDERCREATE PfnWdfwmiprovidercreate; 

// Definition

WDFAPI PfnWdfwmiprovidercreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_WMI_PROVIDER_CONFIG WmiProviderConfig
	PWDF_OBJECT_ATTRIBUTES ProviderAttributes
	WDFWMIPROVIDER *WmiProvider
)
{...}

PFN_WDFWMIPROVIDERCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param WmiProviderConfig: 
### -param ProviderAttributes: 
### -param *WmiProvider: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also