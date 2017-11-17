---
UID: NC.udecxusbendpoint.PFN_UDECXUSBENDPOINTINITFREE
title: *PFN_UDECXUSBENDPOINTINITFREE
author: windows-driver-content
description: 
ms.assetid: 2ee82269-5144-4c52-86fa-5c6beccb7a44
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxusbendpoint.h
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

# *PFN_UDECXUSBENDPOINTINITFREE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBENDPOINTINITFREE *PfnUdecxusbendpointinitfree; 

// Definition

VOID *PfnUdecxusbendpointinitfree 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBENDPOINT_INIT Init
)
{...}

*PFN_UDECXUSBENDPOINTINITFREE 


```

## -parameters

### -param DriverGlobals: 
### -param Init: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also