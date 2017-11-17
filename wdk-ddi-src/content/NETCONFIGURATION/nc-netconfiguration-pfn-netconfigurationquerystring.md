---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONQUERYSTRING
title: PFN_NETCONFIGURATIONQUERYSTRING
author: windows-driver-content
description: 
ms.assetid: 6967dad7-4077-48f0-bb0b-9bc982341070
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

# PFN_NETCONFIGURATIONQUERYSTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONQUERYSTRING PfnNetconfigurationquerystring; 

// Definition

WDFAPI PfnNetconfigurationquerystring 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PCUNICODE_STRING ValueName
	PWDF_OBJECT_ATTRIBUTES StringAttributes
	WDFSTRING *WdfString
)
{...}

PFN_NETCONFIGURATIONQUERYSTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param ValueName: 
### -param StringAttributes: 
### -param *WdfString: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also