---
UID: NC.classpnp.PCLASS_SET_WMI_DATABLOCK
title: PCLASS_SET_WMI_DATABLOCK
author: windows-driver-content
description: 
ms.assetid: 02b5285f-0be4-462d-8cc6-e04375e3fdeb
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

# PCLASS_SET_WMI_DATABLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_SET_WMI_DATABLOCK PclassSetWmiDatablock; 

// Definition

NTSTATUS PclassSetWmiDatablock 
(
	PDEVICE_OBJECT DeviceObject
	PIRP Irp
	ULONG GuidIndex
	ULONG BufferSize
	PUCHAR Buffer
)
{...}

PCLASS_SET_WMI_DATABLOCK 


```

## -parameters

### -param DeviceObject: 
### -param Irp: 
### -param GuidIndex: 
### -param BufferSize: 
### -param Buffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also