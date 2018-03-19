---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD
title: PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD
author: windows-driver-content
description: Notifies the display miniport driver that the VideoProcessorBlt function is about to be called to read from a specified input view resource for a video processor.
old-location: display\videoprocessorinputviewreadafterwritehazard.htm
old-project: display
ms.assetid: 320cfd00-656a-47ce-912e-7196986deaae
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD, VideoProcessorInputViewReadAfterWriteHazard, VideoProcessorInputViewReadAfterWriteHazard callback function [Display Devices], d3d10umddi/VideoProcessorInputViewReadAfterWriteHazard, display.videoprocessorinputviewreadafterwritehazard
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
-	VideoProcessorInputViewReadAfterWriteHazard
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD callback function
Notifies the display miniport driver that the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorblt.md">VideoProcessorBlt</a> function is about to be called to read from a specified input view resource for a video processor. This resource had previously been written to by either the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videodecodersubmitbuffers.md">VideoDecoderSubmitBuffers</a> or the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_decryptionblt.md">DecryptionBlt(D3D11_1)</a> functions.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD Pfnd3d111DdiVideoprocessorinputviewreadafterwritehazard;

void Pfnd3d111DdiVideoprocessorinputviewreadafterwritehazard(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW,
   D3D10DDI_HRESOURCE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW`



`D3D10DDI_HRESOURCE`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_decryptionblt.md">DecryptionBlt(D3D11_1)</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorinputview.md">CreateVideoProcessorInputView</a>