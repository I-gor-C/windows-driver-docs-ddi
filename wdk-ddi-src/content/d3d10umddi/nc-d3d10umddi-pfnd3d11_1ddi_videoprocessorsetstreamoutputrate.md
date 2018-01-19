---
UID : NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE
title : PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE
author : windows-driver-content
description : Sets the rate at which the video processor produces output frames for an input stream.
old-location : display\videoprocessorsetstreamoutputrate.htm
old-project : display
ms.assetid : fc1236f2-fcbf-4b3f-978f-a34260b78159
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnVideoProcessorSetStreamOutputRate
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


# PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE callback function
Sets the rate at which the video processor produces output frames for an input stream.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE Pfnd3d111DdiVideoprocessorsetstreamoutputrate;

void Pfnd3d111DdiVideoprocessorsetstreamoutputrate(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
   UINT,
   D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE,
   BOOL,
  CONST DXGI_RATIONAL *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`UINT`



`D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE`



`BOOL`



`*`




## Return Value

This callback function does not return a value.

## Remarks

The standard output rates that are defined by  <a href="..\d3d10umddi\ne-d3d10umddi-d3d11_1ddi_video_processor_output_rate.md">D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE</a> enumeration values are normal frame-rate (<b>D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_NORMAL</b>) and half frame-rate (<b>D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_HALF</b>). 

If the driver supports custom rates for rate conversion or inverse telecine, it can use a custom rate if the <i>OutputRate</i> parameter is set to <b>D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE_CUSTOM</b>. The custom rate is specified by the <i>pCustomRate</i> parameter.

Depending on the output rate, the driver might have to convert the frame rate. If so, the value of the <i>RepeatFrame</i> parameter controls whether the driver creates interpolated frames or repeats input frames.

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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d11_1ddi_video_processor_output_rate.md">D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcustomrate.md">GetVideoProcessorCustomRate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>