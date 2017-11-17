---
UID: NC.udecxusbendpoint.PFN_UDECXUSBENDPOINTINITSETCALLBACKS
title: *PFN_UDECXUSBENDPOINTINITSETCALLBACKS
author: windows-driver-content
description: 
ms.assetid: cd492c89-0566-4268-b15c-1bdf2bb4ea95
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

# *PFN_UDECXUSBENDPOINTINITSETCALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBENDPOINTINITSETCALLBACKS *PfnUdecxusbendpointinitsetcallbacks; 

// Definition

VOID *PfnUdecxusbendpointinitsetcallbacks 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBENDPOINT_INIT UdecxUsbEndpointInit
	PUDECX_USB_ENDPOINT_CALLBACKS EndpointCallbacks
)
{...}

*PFN_UDECXUSBENDPOINTINITSETCALLBACKS 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbEndpointInit: 
### -param EndpointCallbacks: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also