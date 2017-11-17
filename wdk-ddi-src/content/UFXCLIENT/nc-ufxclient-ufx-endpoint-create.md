---
UID: NC.ufxclient.UFX_ENDPOINT_CREATE
title: UFX_ENDPOINT_CREATE
author: windows-driver-content
description: 
ms.assetid: 93676bf2-e62b-4b27-9297-b689f3c607b5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ufxclient.h
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

# UFX_ENDPOINT_CREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_ENDPOINT_CREATE UfxEndpointCreate; 

// Definition

NTSTATUS UfxEndpointCreate 
(
	PUFX_GLOBALS 
	UFXDEVICE 
	PUFXENDPOINT_INIT 
	PWDF_OBJECT_ATTRIBUTES 
	PWDF_IO_QUEUE_CONFIG 
	PWDF_OBJECT_ATTRIBUTES 
	PWDF_IO_QUEUE_CONFIG 
	PWDF_OBJECT_ATTRIBUTES 
	UFXENDPOINT * 
)
{...}

UFX_ENDPOINT_CREATE PFN_UFX_ENDPOINT_CREATE


```

## -parameters

### -param : 
### -param : 
### -param : 
### -param : 
### -param : 
### -param : 
### -param : 
### -param : 
### -param : 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also