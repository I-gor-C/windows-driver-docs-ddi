---
UID: NC.classpnp.PCLASS_QUERY_WMI_DATABLOCK
title: PCLASS_QUERY_WMI_DATABLOCK
author: windows-driver-content
description: 
ms.assetid: 23535dea-464a-48e9-ab1e-9887ee3e5250
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

# PCLASS_QUERY_WMI_DATABLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_QUERY_WMI_DATABLOCK PclassQueryWmiDatablock; 

// Definition

NTSTATUS PclassQueryWmiDatablock 
(
	PDEVICE_OBJECT DeviceObject
	PIRP Irp
	ULONG GuidIndex
	ULONG BufferAvail
	PUCHAR Buffer
)
{...}

PCLASS_QUERY_WMI_DATABLOCK 


```

## -parameters

### -param DeviceObject: 
### -param Irp: 
### -param GuidIndex: 
### -param BufferAvail: 
### -param Buffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also