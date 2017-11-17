---
UID: NC.ufxclient.EVT_UFX_DEVICE_TESTHOOK
title: EVT_UFX_DEVICE_TESTHOOK
author: windows-driver-content
description: 
ms.assetid: 04cfe0b1-64c5-4d2c-b637-989c7fee5306
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

# EVT_UFX_DEVICE_TESTHOOK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UFX_DEVICE_TESTHOOK EvtUfxDeviceTesthook; 

// Definition

NTSTATUS EvtUfxDeviceTesthook 
(
	UFXDEVICE 
	PVOID 
	size_t 
	PVOID 
	size_t 
)
{...}

EVT_UFX_DEVICE_TESTHOOK PFN_UFX_DEVICE_TESTHOOK


```

## -parameters

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