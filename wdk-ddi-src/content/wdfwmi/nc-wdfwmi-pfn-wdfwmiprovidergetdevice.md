---
UID: NC.wdfwmi.PFN_WDFWMIPROVIDERGETDEVICE
title: PFN_WDFWMIPROVIDERGETDEVICE
author: windows-driver-content
description: 
ms.assetid: a9067820-dafe-4a11-b7d2-f303245b7cb3
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

# PFN_WDFWMIPROVIDERGETDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWMIPROVIDERGETDEVICE PfnWdfwmiprovidergetdevice; 

// Definition

WDFAPI PfnWdfwmiprovidergetdevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFWMIPROVIDER WmiProvider
)
{...}

PFN_WDFWMIPROVIDERGETDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param WmiProvider: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also