---
UID: NC.dispmprt.DXGKDDI_GETVIRTUALGPUINFO
title: DXGKDDI_GETVIRTUALGPUINFO
author: windows-driver-content
description: 
ms.assetid: e213c6f8-9aa3-4056-afee-ef41ed9bf63b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dispmprt.h
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

# DXGKDDI_GETVIRTUALGPUINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_GETVIRTUALGPUINFO DxgkddiGetvirtualgpuinfo; 

// Definition

NTSTATUS DxgkddiGetvirtualgpuinfo 
(
	HANDLE Context
	DXGKARG_GETVIRTUALGPUINFO * pArgs
)
{...}

DXGKDDI_GETVIRTUALGPUINFO PDXGKDDI_GETVIRTUALGPUINFO


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also