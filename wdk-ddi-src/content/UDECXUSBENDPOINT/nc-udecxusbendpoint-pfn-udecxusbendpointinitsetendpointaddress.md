---
UID: NC.udecxusbendpoint.PFN_UDECXUSBENDPOINTINITSETENDPOINTADDRESS
title: *PFN_UDECXUSBENDPOINTINITSETENDPOINTADDRESS
author: windows-driver-content
description: 
ms.assetid: 941345dd-108e-4eda-9abb-760d16ba8fc2
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

# *PFN_UDECXUSBENDPOINTINITSETENDPOINTADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBENDPOINTINITSETENDPOINTADDRESS *PfnUdecxusbendpointinitsetendpointaddress; 

// Definition

VOID *PfnUdecxusbendpointinitsetendpointaddress 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBENDPOINT_INIT Init
	UCHAR EndpointAddress
)
{...}

*PFN_UDECXUSBENDPOINTINITSETENDPOINTADDRESS 


```

## -parameters

### -param DriverGlobals: 
### -param Init: 
### -param EndpointAddress: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also