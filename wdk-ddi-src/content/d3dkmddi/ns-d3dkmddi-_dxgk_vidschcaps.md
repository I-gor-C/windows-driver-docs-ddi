---
UID: NS:d3dkmddi._DXGK_VIDSCHCAPS
title: "_DXGK_VIDSCHCAPS"
author: windows-driver-content
description: The DXGK_VIDSCHCAPS structure identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that a driver can support.
old-location: display\dxgk_vidschcaps.htm
old-project: display
ms.assetid: 714741b5-aec1-4d79-8199-00e8d97e6637
ms.author: windowsdriverdev
ms.date: 3/29/2018
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
product:
- Windows
targetos: Windows
req.typenames: DXGK_VIDSCHCAPS
---

# _DXGK_VIDSCHCAPS structure
The DXGK_VIDSCHCAPS structure identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that a driver can support.

## Syntax
```
typedef struct _DXGK_VIDSCHCAPS {
  union {
    struct {
      UINT  : 1  MultiEngineAware;
      UINT  : 1  VSyncPowerSaveAware;
      UINT  : 1  PreemptionAware;
      UINT  : 1  NoDmaPatching;
      UINT  : 1  CancelCommandAware;
      UINT  : 1  No64BitAtomics;
      UINT  : 1  LowIrqlPreemptCommand;
      UINT  : 4  HwQueuePacketCap;
#if ...
      UINT  : 21 Reserved;
#elif
      UINT  : 25 Reserved;
#elif
      UINT  : 27 Reserved;
#else
      UINT  : 30 Reserved;
#endif
    };
    UINT Value;
  };
} DXGK_VIDSCHCAPS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available beginning with Windows Vista. Available beginning with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>



<a href="https://msdn.microsoft.com/c290c313-14ee-4554-9bb1-8adec1892426">DxgkDdiCancelCommand</a>



<a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a>



<a href="https://msdn.microsoft.com/c21f62ab-c52e-43a2-a3a1-6fd6e5fbde01">DxgkDdiDestroyContext</a>



<a href="https://msdn.microsoft.com/363be784-0e3b-4f9a-a643-80857478bbae">DxgkDdiPatch</a>



<a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a>



<a href="https://msdn.microsoft.com/fd634768-5e1e-4f40-82fd-5ef69148c3d7">DxgkDdiRender</a>