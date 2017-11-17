---
UID: NC.classpnp.PCLASS_ADD_DEVICE
title: PCLASS_ADD_DEVICE
author: windows-driver-content
description: 
ms.assetid: 9b9b42d3-6357-427b-9f88-b7fda1e3fdb5
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

# PCLASS_ADD_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_ADD_DEVICE PclassAddDevice; 

// Definition

NTSTATUS PclassAddDevice 
(
	PDRIVER_OBJECT DriverObject
	PDEVICE_OBJECT Pdo
)
{...}

PCLASS_ADD_DEVICE 


```

## -parameters

### -param DriverObject: 
### -param Pdo: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also