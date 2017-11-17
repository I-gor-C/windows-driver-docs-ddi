---
UID: NC.parallel.PPARCHIP_SET_CHIP_MODE
title: PPARCHIP_SET_CHIP_MODE
author: windows-driver-content
description: 
ms.assetid: ad8a9bfc-92df-432b-aa1f-a5e7ecbaeb7b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: parallel.h
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

# PPARCHIP_SET_CHIP_MODE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPARCHIP_SET_CHIP_MODE PparchipSetChipMode; 

// Definition

NTSTATUS PparchipSetChipMode 
(
	PVOID SetChipContext
	UCHAR ChipMode
)
{...}

PPARCHIP_SET_CHIP_MODE 


```

## -parameters

### -param SetChipContext: 
### -param ChipMode: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also