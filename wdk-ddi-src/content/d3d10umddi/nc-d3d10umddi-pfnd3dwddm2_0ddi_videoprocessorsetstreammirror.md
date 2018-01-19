---
UID : NC:d3d10umddi.PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR
title : PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR
author : windows-driver-content
description : Indicates whether the stream should be flipped vertically or horizontally. Optional for Windows Display Driver Model (WDDM) 2.0, or later, drivers.
old-location : display\videoprocessorsetstreammirror.htm
old-project : display
ms.assetid : 945BD212-7B48-41FD-B11F-FB03DB073BD4
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnVideoProcessorSetStreamMirror
req.alt-loc : D3d10umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR callback function
Indicates whether the stream should be flipped vertically or horizontally. Optional for Windows Display Driver Model (WDDM) 2.0, or later, drivers.

## Syntax

```
PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR Pfnd3dwddm20DdiVideoprocessorsetstreammirror;

void Pfnd3dwddm20DdiVideoprocessorsetstreammirror(
  D3D10DDI_HDEVICE hDevice,
  D3D11_1DDI_HVIDEOPROCESSOR hVideoProcessor,
  UINT StreamIndex,
  BOOL Enable,
  BOOL FlipHorizontal,
  BOOL FlipVertical
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context). The Direct3D runtime passed the user-mode driver this handle as the <b>hDevice</b> member of the <a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_createdevice.md">D3DDDIARG_CREATEDEVICE</a> structure at device creation.

`hVideoProcessor`

Handle to the video processor object.

`StreamIndex`

Indicates the input stream.

`Enable`

Indicates whether mirroring support is enabled or disabled.

`FlipHorizontal`

Indicates whether the input stream should be flipped horizontally.



<div class="alert"><b>Note</b>  This should be ignored when <b>Enable</b> is <b>FALSE</b>.</div>
<div> </div>

`FlipVertical`

Indicates whether the input stream should be flipped vertically.



<div class="alert"><b>Note</b>  This should be ignored when <b>Enable</b> is <b>FALSE</b>.
</div>
<div> </div>


## Return Value

This callback function does not return a value.

## Remarks

Operations are conceptually applied in the following order:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_createdevice.md">D3DDDIARG_CREATEDEVICE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>