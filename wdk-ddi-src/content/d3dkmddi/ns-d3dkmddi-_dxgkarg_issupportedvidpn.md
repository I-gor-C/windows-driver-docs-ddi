---
UID: NS:d3dkmddi._DXGKARG_ISSUPPORTEDVIDPN
title: "_DXGKARG_ISSUPPORTEDVIDPN"
author: windows-driver-content
description: The DXGKARG_ISSUPPORTEDVIDPN structure contains arguments for the DxgkDdiIsSupportedVidPn function. The DxgkDdiIsSupportedVidPn function determines whether a specified video present network (VidPN) is supported on a display adapter.
old-location: display\dxgkarg_issupportedvidpn.htm
old-project: display
ms.assetid: 37f9f40d-6d32-4eeb-8161-282a84ee89dc
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*INOUT_PDXGKARG_ISSUPPORTEDVIDPN, DXGKARG_ISSUPPORTEDVIDPN, DXGKARG_ISSUPPORTEDVIDPN structure [Display Devices], DmStructs_03198868-50e6-47a1-9119-0fa3bff21ec0.xml, _DXGKARG_ISSUPPORTEDVIDPN, d3dkmddi/DXGKARG_ISSUPPORTEDVIDPN, display.dxgkarg_issupportedvidpn"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
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
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGKARG_ISSUPPORTEDVIDPN
product: Windows
targetos: Windows
req.typenames: DXGKARG_ISSUPPORTEDVIDPN
---

# _DXGKARG_ISSUPPORTEDVIDPN structure
The DXGKARG_ISSUPPORTEDVIDPN structure contains arguments for the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_issupportedvidpn.md">DxgkDdiIsSupportedVidPn</a> function. The <i>DxgkDdiIsSupportedVidPn</i> function determines whether a specified video present network (VidPN) is supported on a display adapter.

## Syntax
````
typedef struct _DXGKARG_ISSUPPORTEDVIDPN {
  D3DKMDT_HVIDPN hDesiredVidPn;
  BOOLEAN        IsVidPnSupported;
} DXGKARG_ISSUPPORTEDVIDPN;
````

## Members


`hDesiredVidPn`

A handle to the VidPN object in question.

`IsVidPnSupported`

A Boolean variable that receives <b>TRUE</b> if the VidPN is supported and <b>FALSE</b> if the VidPN is not supported.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_issupportedvidpn.md">DxgkDdiIsSupportedVidPn</a>