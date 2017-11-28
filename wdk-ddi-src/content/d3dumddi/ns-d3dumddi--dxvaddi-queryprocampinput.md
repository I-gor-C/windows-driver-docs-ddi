---
UID: NS.d3dumddi._DXVADDI_QUERYPROCAMPINPUT
title: DXVADDI_QUERYPROCAMPINPUT
author: windows-driver-content
description: The DXVADDI_QUERYPROCAMPINPUT structure describes a ProcAmp control property on a video stream that range information is requested for.
old-location: display\dxvaddi_queryprocampinput.htm
old-project: display
ms.assetid: 9ba7c42a-4140-4d8c-abb3-ae5f9285dbd9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVADDI_QUERYPROCAMPINPUT, DXVADDI_QUERYPROCAMPINPUT
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
req.alt-api: DXVADDI_QUERYPROCAMPINPUT
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
req.iface: 
---

# DXVADDI_QUERYPROCAMPINPUT structure



## -description
<p>The DXVADDI_QUERYPROCAMPINPUT structure describes a ProcAmp control property on a video stream that range information is requested for.</p>


## -syntax

````
typedef struct _DXVADDI_QUERYPROCAMPINPUT {
  const GUID        *pVideoProcGuid;
  DXVADDI_VIDEODESC VideoDesc;
  D3DDDIFORMAT      RenderTargetFormat;
  UINT              ProcAmpCap;
} DXVADDI_QUERYPROCAMPINPUT;
````


## -struct-fields
<dl>

### -field <b>pVideoProcGuid</b>

<dd>
<p>[in] A pointer to a GUID that represents the video processing device type. </p>
</dd>

### -field <b>VideoDesc</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562944">DXVADDI_VIDEODESC</a> structure that describes the video stream. </p>
</dd>

### -field <b>RenderTargetFormat</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the render target for the video processing device.</p>
</dd>

### -field <b>ProcAmpCap</b>

<dd>
<p>[in] A ProcAmp control property that range information is requested for. The ProcAmp control property can be one of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562917">DXVADDI_PROCAMPVALUES</a> structure. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562917">DXVADDI_PROCAMPVALUES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562939">DXVADDI_VALUERANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562944">DXVADDI_VIDEODESC</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_QUERYPROCAMPINPUT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
