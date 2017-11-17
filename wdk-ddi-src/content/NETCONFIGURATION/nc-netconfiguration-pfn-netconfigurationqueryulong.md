---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONQUERYULONG
title: PFN_NETCONFIGURATIONQUERYULONG
author: windows-driver-content
description: 
ms.assetid: ac321741-6e9c-4fa4-ba7b-b2d85e2c947e
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

# PFN_NETCONFIGURATIONQUERYULONG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONQUERYULONG PfnNetconfigurationqueryulong; 

// Definition

WDFAPI PfnNetconfigurationqueryulong 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	NET_CONFIGURATION_QUERY_ULONG_FLAGS Flags
	PCUNICODE_STRING ValueName
	PULONG Value
)
{...}

PFN_NETCONFIGURATIONQUERYULONG 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param Flags: 
### -param ValueName: 
### -param Value: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also