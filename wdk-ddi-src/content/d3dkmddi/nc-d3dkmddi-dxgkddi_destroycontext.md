---
UID: NC:d3dkmddi.DXGKDDI_DESTROYCONTEXT
title: DXGKDDI_DESTROYCONTEXT
author: windows-driver-content
description: The DxgkDdiDestroyContext function destroys the specified graphics processing unit (GPU) context.
old-location: display\dxgkddidestroycontext.htm
old-project: display
ms.assetid: c21f62ab-c52e-43a2-a3a1-6fd6e5fbde01
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGKDDI_DESTROYCONTEXT, DmFunctions_b8cd0b48-a87b-4e6f-8811-49a1e0f46f2f.xml, DxgkDdiDestroyContext, DxgkDdiDestroyContext callback function [Display Devices], d3dkmddi/DxgkDdiDestroyContext, display.dxgkddidestroycontext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3dkmddi.h
api_name:
-	DxgkDdiDestroyContext
product:
- Windows
targetos: Windows
req.typenames: DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_DESTROYCONTEXT callback function
The <i>DxgkDdiDestroyContext</i> function destroys the specified graphics processing unit (GPU) context.

## Syntax

```
DXGKDDI_DESTROYCONTEXT DxgkddiDestroycontext;

NTSTATUS DxgkddiDestroycontext(
  IN_CONST_HANDLE hContext
)
{...}
```

## Parameters

`hContext`

[in] A handle to the context to destroy. The display miniport driver's <a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a> function previously returned this handle in the <b>hContext</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557567">DXGKARG_CREATECONTEXT</a> structure that the <i>pCreateContext</i> parameter of <i>DxgkDdiCreateContext </i>points to.


## Return Value

<i>DxgkDdiDestroyContext</i> returns STATUS_SUCCESS, or an appropriate error result if the context is not successfully destroyed.

## Remarks

A driver should free all resources that it allocated for the context and clean up any internal tracking data structures.

<i>DxgkDdiDestroyContext</i> should be made pageable.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dkmddi.h |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557567">DXGKARG_CREATECONTEXT</a>



<a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a>