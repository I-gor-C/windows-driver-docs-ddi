---
UID: NS:d3dkmddi._DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH
title: "_DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH"
author: windows-driver-content
description: The DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure contains a D3DKMDT_VIDPN_PRESENT_PATH structure, which contains arguments for the DxgkDdiUpdateActiveVidPnPresentPath function.
old-location: display\dxgkarg_updateactivevidpnpresentpath.htm
old-project: display
ms.assetid: 6a4d43fd-f118-4424-93e8-57f72b56f929
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH, DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure [Display Devices], DmStructs_b8d80ff5-189d-4bd2-8b3f-f5ebeadee78f.xml, _DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH, d3dkmddi/DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH, display.dxgkarg_updateactivevidpnpresentpath
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
-	DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH
product: Windows
targetos: Windows
req.typenames: DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH
---

# _DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure
The DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure contains a <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_present_path.md">D3DKMDT_VIDPN_PRESENT_PATH</a> structure, which contains arguments for the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_updateactivevidpnpresentpath.md">DxgkDdiUpdateActiveVidPnPresentPath</a> function.

## Syntax
````
typedef struct _DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH {
  D3DKMDT_VIDPN_PRESENT_PATH VidPnPresentPathInfo;
} DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH;
````

## Members


`VidPnPresentPathInfo`

A <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_present_path.md">D3DKMDT_VIDPN_PRESENT_PATH</a> structure that contains the arguments required by <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_updateactivevidpnpresentpath.md">DxgkDdiUpdateActiveVidPnPresentPath</a>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_updateactivevidpnpresentpath.md">DxgkDdiUpdateActiveVidPnPresentPath</a>