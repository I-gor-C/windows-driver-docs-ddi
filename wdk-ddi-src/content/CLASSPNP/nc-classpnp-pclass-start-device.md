---
UID: NC.classpnp.PCLASS_START_DEVICE
title: PCLASS_START_DEVICE
author: windows-driver-content
description: 
ms.assetid: 685180dc-d0d7-40fa-8a4b-9a21dfc21ce9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_START_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_START_DEVICE PclassStartDevice; 

// Definition

NTSTATUS PclassStartDevice 
(
	PDEVICE_OBJECT DeviceObject
)
{...}

PCLASS_START_DEVICE 


```

## -parameters

### -param DeviceObject: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also