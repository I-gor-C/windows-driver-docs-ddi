---
UID: NC.usbcamdi.PFNUSBCAMD_BulkReadWrite
title: PFNUSBCAMD_BulkReadWrite
author: windows-driver-content
description: 
ms.assetid: 74c24c69-127d-4517-893b-f81612f47ca2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbcamdi.h
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

# PFNUSBCAMD_BulkReadWrite callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNUSBCAMD_BulkReadWrite PfnusbcamdBulkreadwrite; 

// Definition

NTSTATUS PfnusbcamdBulkreadwrite 
(
	PVOID DeviceContext
	USHORT PipeIndex
	PVOID Buffer
	ULONG BufferLength
	PCOMMAND_COMPLETE_FUNCTION CommandComplete
	PVOID CommandContext
)
{...}

PFNUSBCAMD_BulkReadWrite 


```

## -parameters

### -param DeviceContext: 
### -param PipeIndex: 
### -param Buffer: 
### -param BufferLength: 
### -param CommandComplete: 
### -param CommandContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also