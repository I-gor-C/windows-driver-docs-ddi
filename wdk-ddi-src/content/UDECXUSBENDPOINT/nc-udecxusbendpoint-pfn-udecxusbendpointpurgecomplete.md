---
UID: NC.udecxusbendpoint.PFN_UDECXUSBENDPOINTPURGECOMPLETE
title: *PFN_UDECXUSBENDPOINTPURGECOMPLETE
author: windows-driver-content
description: 
ms.assetid: e82cc3d2-c84e-4271-b71a-8236dc9306bc
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

# *PFN_UDECXUSBENDPOINTPURGECOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBENDPOINTPURGECOMPLETE *PfnUdecxusbendpointpurgecomplete; 

// Definition

VOID *PfnUdecxusbendpointpurgecomplete 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	UDECXUSBENDPOINT UdecxUsbEndpoint
)
{...}

*PFN_UDECXUSBENDPOINTPURGECOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbEndpoint: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also