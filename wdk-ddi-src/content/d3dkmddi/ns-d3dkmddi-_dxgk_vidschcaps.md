---
UID: NS:d3dkmddi._DXGK_VIDSCHCAPS
title: "_DXGK_VIDSCHCAPS"
author: windows-driver-content
description: The DXGK_VIDSCHCAPS structure identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that a driver can support.
old-location: display\dxgk_vidschcaps.htm
old-project: display
ms.assetid: 714741b5-aec1-4d79-8199-00e8d97e6637
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_VIDSCHCAPS, DXGK_VIDSCHCAPS structure [Display Devices], DmStructs_01f721e4-8585-46b1-a911-9fa904a29f7e.xml, _DXGK_VIDSCHCAPS, d3dkmddi/DXGK_VIDSCHCAPS, display.dxgk_vidschcaps
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available beginning with Windows Vista.
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
-	DXGK_VIDSCHCAPS
product: Windows
targetos: Windows
req.typenames: DXGK_VIDSCHCAPS
---

# _DXGK_VIDSCHCAPS structure
The DXGK_VIDSCHCAPS structure identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that a driver can support.

## Syntax
````
typedef struct _DXGK_VIDSCHCAPS {
  union {
    struct {
      UINT MultiEngineAware  :1;
      UINT VSyncPowerSaveAware  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
      UINT PreemptionAware  :1;
      UINT NoDmaPatching  :1;
      UINT CancelCommandAware  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
      UINT No64BitAtomics  :1;
      UINT Reserved  :26;
#else 
      UINT Reserved  :27;
#endif 
#else 
      UINT Reserved  :30;
#endif 
    };
    UINT Value;
  };
} DXGK_VIDSCHCAPS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available beginning with Windows Vista. Available beginning with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_patch.md">DxgkDdiPatch</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createcontext.md">DxgkDdiCreateContext</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_cancelcommand.md">DxgkDdiCancelCommand</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_destroycontext.md">DxgkDdiDestroyContext</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_render.md">DxgkDdiRender</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_present.md">DxgkDdiPresent</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_drivercaps.md">DXGK_DRIVERCAPS</a>