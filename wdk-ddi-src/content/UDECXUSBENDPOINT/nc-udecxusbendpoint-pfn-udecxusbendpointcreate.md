---
UID: NC.udecxusbendpoint.PFN_UDECXUSBENDPOINTCREATE
title: *PFN_UDECXUSBENDPOINTCREATE
author: windows-driver-content
description: 
ms.assetid: c4f070a7-c80f-4f1d-a152-27bfe66f9a0a
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

# *PFN_UDECXUSBENDPOINTCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBENDPOINTCREATE *PfnUdecxusbendpointcreate; 

// Definition

NTSTATUS *PfnUdecxusbendpointcreate 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBENDPOINT_INIT *EndpointInit
	PWDF_OBJECT_ATTRIBUTES Attributes
	UDECXUSBENDPOINT *UdecxUsbEndpoint
)
{...}

*PFN_UDECXUSBENDPOINTCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param *EndpointInit: 
### -param Attributes: 
### -param *UdecxUsbEndpoint: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also