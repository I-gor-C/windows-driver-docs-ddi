---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONASSIGNULONG
title: PFN_NETCONFIGURATIONASSIGNULONG
author: windows-driver-content
description: 
ms.assetid: 5a6dc215-6db6-4f01-852a-ced29e84ee9e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netconfiguration.h
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

# PFN_NETCONFIGURATIONASSIGNULONG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONASSIGNULONG PfnNetconfigurationassignulong; 

// Definition

WDFAPI PfnNetconfigurationassignulong 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PCUNICODE_STRING ValueName
	ULONG Value
)
{...}

PFN_NETCONFIGURATIONASSIGNULONG 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param ValueName: 
### -param Value: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also