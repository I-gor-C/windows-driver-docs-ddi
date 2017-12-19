---
UID: NS.D3DUMDDI._DXVADDI_VIDEOPROCESSORINPUT
title: _DXVADDI_VIDEOPROCESSORINPUT
author: windows-driver-content
description: The DXVADDI_VIDEOPROCESSORINPUT structure describes a video stream that is processed by a video processing device type.
old-location: display\dxvaddi_videoprocessorinput.htm
old-project: display
ms.assetid: 539d32a5-4566-4b8e-b9de-da8d5be3c2f2
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DXVADDI_VIDEOPROCESSORINPUT, DXVADDI_VIDEOPROCESSORINPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_VIDEOPROCESSORINPUT
req.alt-loc: d3dumddi.h
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
---

# _DXVADDI_VIDEOPROCESSORINPUT structure



## -description
The DXVADDI_VIDEOPROCESSORINPUT structure describes a video stream that is processed by a video processing device type.



## -syntax

````
typedef struct _DXVADDI_VIDEOPROCESSORINPUT {
  const GUID        *pVideoProcGuid;
  DXVADDI_VIDEODESC VideoDesc;
  D3DDDIFORMAT      RenderTargetFormat;
} DXVADDI_VIDEOPROCESSORINPUT;
````


## -struct-fields

### -field pVideoProcGuid

[in] A pointer to a GUID that represents the video processing device type. 


### -field VideoDesc

[in] A <a href="display.dxvaddi_videodesc">DXVADDI_VIDEODESC</a> structure that describes the video stream. 


### -field RenderTargetFormat

[in] A <a href="display.d3dddiformat">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the render target for the video processing device.


## -remarks
When the D3DDDICAPS_GETVIDEOPROCESSORRTFORMATCOUNT, D3DDDICAPS_GETVIDEOPROCESSORRTFORMATS, D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT, or D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATS <a href="display.d3dddicaps_type">D3DDDICAPS_TYPE</a>-type value is sent in a call to the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a> function, the driver ignores the <b>RenderTargetFormat</b> member of DXVADDI_VIDEOPROCESSORINPUT.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dddiarg_getcaps">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="display.d3dddicaps_type">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="display.d3dddiformat">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="display.dxvaddi_videodesc">DXVADDI_VIDEODESC</a>
</dt>
<dt>
<a href="display.dxvaddi_videoprocessorcaps">DXVADDI_VIDEOPROCESSORCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOPROCESSORINPUT structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

