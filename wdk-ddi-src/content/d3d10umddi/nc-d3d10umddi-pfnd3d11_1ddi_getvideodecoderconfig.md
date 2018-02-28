---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERCONFIG
title: PFND3D11_1DDI_GETVIDEODECODERCONFIG
author: windows-driver-content
description: Queries the video decoder configuration for a specified video operation.
old-location: display\getvideodecoderconfig.htm
old-project: display
ms.assetid: e13cb42b-258e-4fa6-8dc0-8983b118af3c
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: PFND3D11_1DDI_GETVIDEODECODERCONFIG, d3d10umddi/pfnGetVideoDecoderConfig, display.getvideodecoderconfig, pfnGetVideoDecoderConfig, pfnGetVideoDecoderConfig callback function [Display Devices]
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
-	pfnGetVideoDecoderConfig
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETVIDEODECODERCONFIG callback function
Queries the video decoder configuration for a specified video operation.

## Syntax

```
PFND3D11_1DDI_GETVIDEODECODERCONFIG Pfnd3d111DdiGetvideodecoderconfig;

void Pfnd3d111DdiGetvideodecoderconfig(
   D3D10DDI_HDEVICE,
  CONST D3D11_1DDI_VIDEO_DECODER_DESC *,
   UINT,
  D3D11_1DDI_VIDEO_DECODER_CONFIG *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`UINT`



`*`




## Return Value

This callback function does not return a value.

## Remarks

The Microsoft Direct3D runtime verifies that the <i>pDecodeDesc</i> and <i>Index</i> parameter data is valid before it calls the <b>GetVideoDecoderConfig</b> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_decoder_desc.md">D3D11_1DDI_VIDEO_DECODER_DESC</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_decoder_config.md">D3D11_1DDI_VIDEO_DECODER_CONFIG</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideodecoderconfigcount.md">GetVideoDecoderConfigCount</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_GETVIDEODECODERCONFIG callback function%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>