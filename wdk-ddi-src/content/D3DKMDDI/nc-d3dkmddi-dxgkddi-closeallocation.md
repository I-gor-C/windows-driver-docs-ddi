---
UID: NC.d3dkmddi.DXGKDDI_CLOSEALLOCATION
title: DXGKDDI_CLOSEALLOCATION
author: windows-driver-content
description: 
ms.assetid: e0ae94f9-5944-4337-82fa-76e078e993eb
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

# DXGKDDI_CLOSEALLOCATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_CLOSEALLOCATION DxgkddiCloseallocation; 

// Definition

NTSTATUS DxgkddiCloseallocation 
(
	IN_CONST_HANDLE hDevice
	IN_CONST_PDXGKARG_CLOSEALLOCATION pCloseAllocation
)
{...}

DXGKDDI_CLOSEALLOCATION PDXGKDDI_CLOSEALLOCATION


```

## -parameters

### -param hDevice: 
### -param pCloseAllocation: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also