---
UID: NS:d3d10umddi.D3D11_1DDI_VIDEO_COLOR_RGBA
title: D3D11_1DDI_VIDEO_COLOR_RGBA
author: windows-driver-content
description: Specifies an RGB color value.
old-location: display\d3d11_1ddi_video_color_rgba.htm
old-project: display
ms.assetid: 0d97d6ef-87e6-4ba3-ab4b-aa5b22cb126b
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D11_1DDI_VIDEO_COLOR_RGBA, D3D11_1DDI_VIDEO_COLOR_RGBA structure [Display Devices], d3d10umddi/D3D11_1DDI_VIDEO_COLOR_RGBA, display.d3d11_1ddi_video_color_rgba
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
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
-	D3d10umddi.h
api_name:
-	D3D11_1DDI_VIDEO_COLOR_RGBA
product:
- Windows
targetos: Windows
req.typenames: D3D11_1DDI_VIDEO_COLOR_RGBA
---

# D3D11_1DDI_VIDEO_COLOR_RGBA structure
Specifies an RGB color value.

## Syntax
```
typedef struct D3D11_1DDI_VIDEO_COLOR_RGBA {
  float R;
  float G;
  float B;
  float A;
};
```

## Members


`R`

The red value.

`G`

The green value.

`B`

The blue value.

`A`

The alpha value. Values range from 0 (transparent) to 1 (opaque).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |