---
UID: NC:d3dkmddi.DXGKDDI_UNMAPCPUHOSTAPERTURE
title: DXGKDDI_UNMAPCPUHOSTAPERTURE
author: windows-driver-content
description: DxgkDdiUnmapCpuHostAperture is used to unmap a previously mapped range of the CPU host aperture.
old-location: display\dxgkddiunmapcpuhostaperture.htm
old-project: display
ms.assetid: AFE6B92F-49DB-47F9-90BC-F75B5F37178D
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGKDDI_UNMAPCPUHOSTAPERTURE, DxgkDdiUnmapCpuHostAperture, DxgkDdiUnmapCpuHostAperture callback function [Display Devices], d3dkmddi/DxgkDdiUnmapCpuHostAperture, display.dxgkddiunmapcpuhostaperture
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
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
-	d3dkmddi.h
api_name:
-	DxgkDdiUnmapCpuHostAperture
product:
- Windows
targetos: Windows
req.typenames: DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_UNMAPCPUHOSTAPERTURE callback function
<b>DxgkDdiUnmapCpuHostAperture</b> is used to unmap a previously mapped range of the CPU host aperture.

## Syntax

```
DXGKDDI_UNMAPCPUHOSTAPERTURE DxgkddiUnmapcpuhostaperture;

NTSTATUS DxgkddiUnmapcpuhostaperture(
  IN_CONST_HANDLE hAdapter,
  IN_CONST_PDXGKARG_UNMAPCPUHOSTAPERTURE pArgs
)
{...}
```

## Parameters

`hAdapter`

A handle to the display adapter.

`pArgs`

A <a href="https://msdn.microsoft.com/library/windows/hardware/dn906826">DXGKARG_UNMAPCPUHOSTAPERTURE</a> structure that describes the operation.


## Return Value

Returns <b>STATUS_SUCCESS</b> if it succeeds. Otherwise, it returns one of the error codes defined in <b>Ntstatus.h</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Desktop |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn906826">DXGKARG_UNMAPCPUHOSTAPERTURE</a>