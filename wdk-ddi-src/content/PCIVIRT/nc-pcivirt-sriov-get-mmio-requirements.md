---
UID: NC.pcivirt.SRIOV_GET_MMIO_REQUIREMENTS
title: SRIOV_GET_MMIO_REQUIREMENTS
author: windows-driver-content
description: 
ms.assetid: 6ee4d942-5a11-44dd-a0ac-42449ce910c5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: pcivirt.h
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

# SRIOV_GET_MMIO_REQUIREMENTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SRIOV_GET_MMIO_REQUIREMENTS SriovGetMmioRequirements; 

// Definition

NTSTATUS SriovGetMmioRequirements 
(
	PVOID Context
	USHORT VfIndex
	ULONG BlockId
	PVOID Buffer
	ULONG Length
)
{...}

SRIOV_GET_MMIO_REQUIREMENTS PSRIOV_GET_MMIO_REQUIREMENTS


```

## -parameters

### -param Context: 
### -param VfIndex: 
### -param BlockId: 
### -param Buffer: 
### -param Length: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also