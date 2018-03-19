---
UID: NC:d3dkmddi.DXGKDDI_SETROOTPAGETABLE
title: DXGKDDI_SETROOTPAGETABLE
author: windows-driver-content
description: DxgkDdiSetRootPageTable sets the root page table for the given context. This function is used to notify a context when its associated root page table is resized or moved in memory.
old-location: display\dxgkddisetrootpagetable.htm
old-project: display
ms.assetid: BC9E7A2D-690D-4EC2-8D16-22C5FEBA574A
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGKDDI_SETROOTPAGETABLE, DxgkDdiSetRootPageTable, DxgkDdiSetRootPageTable callback function [Display Devices], d3dkmddi/DxgkDdiSetRootPageTable, display.dxgkddisetrootpagetable, dispmprt/DxgkDdiSetRootPageTable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	dispmprt.h
-	d3dkmddi.h
api_name:
-	DxgkDdiSetRootPageTable
product: Windows
targetos: Windows
req.typenames: DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_SETROOTPAGETABLE callback function
<b>DxgkDdiSetRootPageTable</b> sets the root page table for the given context. This function is used to notify a context when its associated root page table is resized or moved in memory.


This is level 1 synchronization function. The targeted context is guaranteed to be idled (i.e. not scheduled) while its root page table is being updated.

## Syntax

```
DXGKDDI_SETROOTPAGETABLE DxgkddiSetrootpagetable;

void DxgkddiSetrootpagetable(
  IN_CONST_HANDLE hAdapter,
  IN_CONST_PDXGKARG_SETROOTPAGETABLE pSetPageTable
)
{...}
```

## Parameters

`hAdapter`

A handle to the display adapter.

`pSetPageTable`

The <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setrootpagetable.md">DXGKARG_SETROOTPAGETABLE</a> structure that describes the operation.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Desktop |
| **Header** | d3dkmddi.h |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setrootpagetable.md">DXGKARG_SETROOTPAGETABLE</a>