---
UID: NC:d3d10umddi.PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW
title: PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW
author: windows-driver-content
description: Releases resources for the video decoder output view that were created through a call to the CreateVideoDecoderOutputView function.
old-location: display\destroyvideodecoderoutputview.htm
old-project: display
ms.assetid: acb174e5-09cc-41e9-8b30-8c64f6193f7b
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW, d3d10umddi/pfnDestroyVideoDecoderOutputView, display.destroyvideodecoderoutputview, pfnDestroyVideoDecoderOutputView, pfnDestroyVideoDecoderOutputView callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
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
-	UserDefined
api_location:
-	D3d10umddi.h
api_name:
-	pfnDestroyVideoDecoderOutputView
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW callback function
Releases resources for the video decoder output view that were created through a call to the <a href="https://msdn.microsoft.com/a5a32b4e-799c-4d18-995d-f804e6dff85c">CreateVideoDecoderOutputView</a> function.

## Syntax

```
PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW Pfnd3d111DdiDestroyvideodecoderoutputview;

void Pfnd3d111DdiDestroyvideodecoderoutputview(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEODECODEROUTPUTVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEODECODEROUTPUTVIEW`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/a5a32b4e-799c-4d18-995d-f804e6dff85c">CreateVideoDecoderOutputView</a>