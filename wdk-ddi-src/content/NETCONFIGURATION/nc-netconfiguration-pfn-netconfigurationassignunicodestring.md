---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONASSIGNUNICODESTRING
title: PFN_NETCONFIGURATIONASSIGNUNICODESTRING
author: windows-driver-content
description: 
ms.assetid: 53fef4ad-4674-4a0a-a14a-357999199c49
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

# PFN_NETCONFIGURATIONASSIGNUNICODESTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONASSIGNUNICODESTRING PfnNetconfigurationassignunicodestring; 

// Definition

WDFAPI PfnNetconfigurationassignunicodestring 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PCUNICODE_STRING ValueName
	PCUNICODE_STRING Value
)
{...}

PFN_NETCONFIGURATIONASSIGNUNICODESTRING 


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