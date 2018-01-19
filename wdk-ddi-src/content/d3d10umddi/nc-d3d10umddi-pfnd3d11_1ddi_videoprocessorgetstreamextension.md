---
UID : NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION
title : PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION
author : windows-driver-content
description : Returns the private state data for a video processor stream to an application.
old-location : display\videoprocessorgetstreamextension.htm
old-project : display
ms.assetid : e2c91e9c-f8ab-48ba-b98a-332cb0ac7077
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
req.alt-api : pfnVideoProcessorGetStreamExtension
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


# PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION callback function
Returns the private state data for a video processor stream to an application.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION Pfnd3d111DdiVideoprocessorgetstreamextension;

HRESULT Pfnd3d111DdiVideoprocessorgetstreamextension(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
   UINT,
  CONST GUID *,
   UINT,
  void *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`UINT`



`*`



`UINT`



`*`




## Return Value

<b>VideoProcessorGetStreamExtension</b> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The private state data was returned successfully.
<dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl>The graphics adapter was removed.

<dl>
<dt><b>E_FAIL</b></dt>
</dl>
        The display miniport driver cannot set the requested private state data for the video processor.
<dl>
<dt><b>E_INVALIDARG</b></dt>
</dl>Parameters were validated and determined to be incorrect.

## Remarks

The Microsoft Direct3D runtime does not validate any parameter data before it calls the  <b>VideoProcessorGetStreamExtension</b> function.

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
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>