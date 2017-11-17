---
UID: NC.classpnp.PCLASS_READ_WRITE
title: PCLASS_READ_WRITE
author: windows-driver-content
description: 
ms.assetid: 6a29746c-ae63-453e-9f64-1ab48e1ec29a
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

# PCLASS_READ_WRITE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_READ_WRITE PclassReadWrite; 

// Definition

NTSTATUS PclassReadWrite 
(
	PDEVICE_OBJECT DeviceObject
	PIRP Irp
)
{...}

PCLASS_READ_WRITE 


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