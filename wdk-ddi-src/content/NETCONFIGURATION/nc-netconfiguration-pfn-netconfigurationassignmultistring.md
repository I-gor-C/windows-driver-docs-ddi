---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONASSIGNMULTISTRING
title: PFN_NETCONFIGURATIONASSIGNMULTISTRING
author: windows-driver-content
description: 
ms.assetid: b9a291c3-9a1a-4b8f-874e-ebeccc582010
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

# PFN_NETCONFIGURATIONASSIGNMULTISTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONASSIGNMULTISTRING PfnNetconfigurationassignmultistring; 

// Definition

WDFAPI PfnNetconfigurationassignmultistring 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PCUNICODE_STRING ValueName
	WDFCOLLECTION Collection
)
{...}

PFN_NETCONFIGURATIONASSIGNMULTISTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param ValueName: 
### -param Collection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also