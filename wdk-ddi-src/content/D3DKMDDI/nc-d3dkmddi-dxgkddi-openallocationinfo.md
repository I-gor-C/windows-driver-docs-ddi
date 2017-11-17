---
UID: NC.d3dkmddi.DXGKDDI_OPENALLOCATIONINFO
title: DXGKDDI_OPENALLOCATIONINFO
author: windows-driver-content
description: 
ms.assetid: 1e80cc3e-58e2-4983-9952-f7150579cc58
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
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

# DXGKDDI_OPENALLOCATIONINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_OPENALLOCATIONINFO DxgkddiOpenallocationinfo; 

// Definition

NTSTATUS DxgkddiOpenallocationinfo 
(
	IN_CONST_HANDLE hDevice
	IN_CONST_PDXGKARG_OPENALLOCATION pOpenAllocation
)
{...}

DXGKDDI_OPENALLOCATIONINFO PDXGKDDI_OPENALLOCATIONINFO


```

## -parameters

### -param hDevice: 
### -param pOpenAllocation: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also