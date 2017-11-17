---
UID: NC.ufxclient.UFX_DEVICE_CREATE
title: UFX_DEVICE_CREATE
author: windows-driver-content
description: 
ms.assetid: b7f14b06-6f33-4e42-8ca9-2e6361f131fb
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

# UFX_DEVICE_CREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_CREATE UfxDeviceCreate; 

// Definition

NTSTATUS UfxDeviceCreate 
(
	PUFX_GLOBALS 
	WDFDEVICE 
	PUFX_DEVICE_CALLBACKS 
	PUFX_DEVICE_CAPABILITIES 
	PWDF_OBJECT_ATTRIBUTES 
	UFXDEVICE * 
)
{...}

UFX_DEVICE_CREATE PFN_UFX_DEVICE_CREATE


```

## -parameters

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