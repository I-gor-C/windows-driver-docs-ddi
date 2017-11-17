---
UID: NC.scutil.PNP_CALLBACK
title: PNP_CALLBACK
author: windows-driver-content
description: 
ms.assetid: f18e3457-71da-4a4e-9aad-0d743b7deb92
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: scutil.h
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

# PNP_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PNP_CALLBACK PnpCallback; 

// Definition

NTSTATUS PnpCallback 
(
	PDEVICE_OBJECT DeviceObject
	PIRP Irp
)
{...}

PNP_CALLBACK 


```

## -parameters

### -param DeviceObject: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also