---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONQUERYMULTISTRING
title: PFN_NETCONFIGURATIONQUERYMULTISTRING
author: windows-driver-content
description: 
ms.assetid: d0d96d97-7241-4b6c-8a32-8179661daf6d
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

# PFN_NETCONFIGURATIONQUERYMULTISTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONQUERYMULTISTRING PfnNetconfigurationquerymultistring; 

// Definition

WDFAPI PfnNetconfigurationquerymultistring 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PCUNICODE_STRING ValueName
	PWDF_OBJECT_ATTRIBUTES StringsAttributes
	WDFCOLLECTION Collection
)
{...}

PFN_NETCONFIGURATIONQUERYMULTISTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param ValueName: 
### -param StringsAttributes: 
### -param Collection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also