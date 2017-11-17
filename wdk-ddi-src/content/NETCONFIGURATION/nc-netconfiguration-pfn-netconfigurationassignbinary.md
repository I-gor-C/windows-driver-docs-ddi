---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONASSIGNBINARY
title: PFN_NETCONFIGURATIONASSIGNBINARY
author: windows-driver-content
description: 
ms.assetid: ec5c7e17-5d76-4c38-8931-918080371f09
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

# PFN_NETCONFIGURATIONASSIGNBINARY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONASSIGNBINARY PfnNetconfigurationassignbinary; 

// Definition

WDFAPI PfnNetconfigurationassignbinary 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PCUNICODE_STRING ValueName
	PVOID Buffer
	ULONG BufferLength
)
{...}

PFN_NETCONFIGURATIONASSIGNBINARY 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param ValueName: 
### -param Buffer: 
### -param BufferLength: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also