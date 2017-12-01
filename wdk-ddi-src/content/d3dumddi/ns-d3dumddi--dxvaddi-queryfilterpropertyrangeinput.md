---
UID: NS.d3dumddi._DXVADDI_QUERYFILTERPROPERTYRANGEINPUT
title: DXVADDI_QUERYFILTERPROPERTYRANGEINPUT
author: windows-driver-content
description: The DXVADDI_QUERYFILTERPROPERTYRANGEINPUT structure describes a filter setting on a video stream that range information is requested for.
old-location: display\dxvaddi_queryfilterpropertyrangeinput.htm
old-project: display
ms.assetid: d073d326-6cc6-4216-b312-809d707aef3b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVADDI_QUERYFILTERPROPERTYRANGEINPUT, DXVADDI_QUERYFILTERPROPERTYRANGEINPUT
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
req.alt-api: DXVADDI_QUERYFILTERPROPERTYRANGEINPUT
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

# DXVADDI_QUERYFILTERPROPERTYRANGEINPUT structure



## -description
<p>The DXVADDI_QUERYFILTERPROPERTYRANGEINPUT structure describes a filter setting on a video stream that range information is requested for.</p>


## -syntax

````
typedef struct _DXVADDI_QUERYFILTERPROPERTYRANGEINPUT {
  const GUID        *pVideoProcGuid;
  DXVADDI_VIDEODESC VideoDesc;
  D3DDDIFORMAT      RenderTargetFormat;
  UINT              FilterSetting;
} DXVADDI_QUERYFILTERPROPERTYRANGEINPUT;
````


## -struct-fields
<dl>

### -field <b>pVideoProcGuid</b>

<dd>
<p>[in] A pointer to a GUID that represents the video processing device type. </p>
</dd>

### -field <b>VideoDesc</b>

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videodesc.md">DXVADDI_VIDEODESC</a> structure that describes the video stream.</p>
</dd>

### -field <b>RenderTargetFormat</b>

<dd>
<p>[in] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the render target for the video processing device.</p>
</dd>

### -field <b>FilterSetting</b>

<dd>
<p>[in] A filter setting that range information is requested for. This member can be one of the following settings:</p>
<ul>
<li>
<p>DXVADDI_NOISEFILTER_LUMALEVEL</p>
</li>
<li>
<p>DXVADDI_NOISEFILTER_LUMATHREASHOLD</p>
</li>
<li>
<p>DXVADDI_NOISEFILTER_LUMARADIUS</p>
</li>
<li>
<p>DXVADDI_NOISEFILTER_CHROMALEVEL</p>
</li>
<li>
<p>DXVADDI_NOISEFILTER_CHROMATHREASHOLD</p>
</li>
<li>
<p>DXVADDI_NOISEFILTER_CHROMARADIUS</p>
</li>
<li>
<p>DXVADDI_DETAILFILTER_LUMALEVEL</p>
</li>
<li>
<p>DXVADDI_DETAILFILTER_LUMATHREASHOLD</p>
</li>
<li>
<p>DXVADDI_DETAILFILTER_LUMARADIUS</p>
</li>
<li>
<p>DXVADDI_DETAILFILTER_CHROMALEVEL</p>
</li>
<li>
<p>DXVADDI_DETAILFILTER_CHROMATHREASHOLD</p>
</li>
<li>
<p>DXVADDI_DETAILFILTER_CHROMARADIUS</p>
</li>
</ul>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ne-d3dumddi--d3dddicaps-type.md">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-valuerange.md">DXVADDI_VALUERANGE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videodesc.md">DXVADDI_VIDEODESC</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_QUERYFILTERPROPERTYRANGEINPUT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
