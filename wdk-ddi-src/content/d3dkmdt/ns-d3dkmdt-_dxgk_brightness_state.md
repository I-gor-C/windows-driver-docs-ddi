---
UID: NS:d3dkmdt._DXGK_BRIGHTNESS_STATE
title: "_DXGK_BRIGHTNESS_STATE"
author: windows-driver-content
description: Used to enable smooth brightness control for an integrated display panel.
old-location: display\dxgk_brightness_state.htm
old-project: display
ms.assetid: 60896a51-63c9-46fd-96ee-9cdbb72ac30c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_BRIGHTNESS_STATE, DXGK_BRIGHTNESS_STATE structure [Display Devices], _DXGK_BRIGHTNESS_STATE, d3dkmdt/DXGK_BRIGHTNESS_STATE, display.dxgk_brightness_state
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	HeaderDef
api_location:
-	D3dkmdt.h
api_name:
-	DXGK_BRIGHTNESS_STATE
product: Windows
targetos: Windows
req.typenames: DXGK_BRIGHTNESS_STATE
---

# _DXGK_BRIGHTNESS_STATE structure
Used to enable smooth brightness control for an integrated display panel. The display miniport driver must enable smooth brightness control when its <a href="https://msdn.microsoft.com/804046ff-0cc7-4ff0-be07-b574cb40fd2b">DxgkDdiSetBrightnessState</a> function is called and <i>BrightnessState</i>-&gt;<b>SmoothBrightness</b> is set to 1.Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers.

## Syntax
```
typedef struct _DXGK_BRIGHTNESS_STATE {
  union {
    struct {
      UINT  : 1  SmoothBrightness;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} DXGK_BRIGHTNESS_STATE;
```

## Members


## Remarks
Do not assume that the <b>SmoothBrightness</b> members of <b>DXGK_BRIGHTNESS_STATE</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/jj128359">DXGK_BRIGHTNESS_CAPS</a> are the same. <b>DXGK_BRIGHTNESS_STATE</b>.<b>SmoothBrightness</b> is used to enable  smooth brightness control on an integrated display panel. <b>DXGK_BRIGHTNESS_CAPS</b>.<b>SmoothBrightness</b> is used to query smooth brightness control capabilities of the display panel.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/804046ff-0cc7-4ff0-be07-b574cb40fd2b">DxgkDdiSetBrightnessState</a>