---
UID: NE.d3dumddi._DXVAHDDDI_FILTER
title: DXVAHDDDI_FILTER
author: windows-driver-content
description: The DXVAHDDDI_FILTER enumeration contains values that identify the filter range, which the driver should retrieve when the driver's GetCaps function is called with the D3DDDICAPS_DXVAHD_GETVPFILTERRANGE value set.
old-location: display\dxvahdddi_filter.htm
ms.assetid: dbf65c28-b4f2-4930-8d01-050c45f87bb4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_FILTER is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_FILTER
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# DXVAHDDDI_FILTER enumeration



## -description
<p>The DXVAHDDDI_FILTER enumeration contains values that identify the filter range, which the driver should retrieve when the driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPFILTERRANGE value set. </p>


## -syntax

````
typedef enum _DXVAHDDDI_FILTER { 
  DXVAHDDDI_FILTER_BRIGHTNESS          = 0,
  DXVAHDDDI_FILTER_CONTRAST            = 1,
  DXVAHDDDI_FILTER_HUE                 = 2,
  DXVAHDDDI_FILTER_SATURATION          = 3,
  DXVAHDDDI_FILTER_NOISE_REDUCTION     = 4,
  DXVAHDDDI_FILTER_EDGE_ENHANCEMENT    = 5,
  DXVAHDDDI_FILTER_ANAMORPHIC_SCALING  = 6
} DXVAHDDDI_FILTER;
````


## -enum-fields
<dl>

### -field <a id="DXVAHDDDI_FILTER_BRIGHTNESS"></a><a id="dxvahdddi_filter_brightness"></a><b>DXVAHDDDI_FILTER_BRIGHTNESS</b>

<dd>
<p>A value that specifies the filter range of the brightness ProcAmp. </p>
</dd>

### -field <a id="DXVAHDDDI_FILTER_CONTRAST"></a><a id="dxvahdddi_filter_contrast"></a><b>DXVAHDDDI_FILTER_CONTRAST</b>

<dd>
<p>A value that specifies the filter range of the contrast ProcAmp. </p>
</dd>

### -field <a id="DXVAHDDDI_FILTER_HUE"></a><a id="dxvahdddi_filter_hue"></a><b>DXVAHDDDI_FILTER_HUE</b>

<dd>
<p>A value that specifies the filter range of the hue ProcAmp. </p>
</dd>

### -field <a id="DXVAHDDDI_FILTER_SATURATION"></a><a id="dxvahdddi_filter_saturation"></a><b>DXVAHDDDI_FILTER_SATURATION</b>

<dd>
<p>A value that specifies the filter range of the saturation ProcAmp. </p>
</dd>

### -field <a id="DXVAHDDDI_FILTER_NOISE_REDUCTION"></a><a id="dxvahdddi_filter_noise_reduction"></a><b>DXVAHDDDI_FILTER_NOISE_REDUCTION</b>

<dd>
<p>A value that specifies the filter range of the noise reduction filter. </p>
</dd>

### -field <a id="DXVAHDDDI_FILTER_EDGE_ENHANCEMENT"></a><a id="dxvahdddi_filter_edge_enhancement"></a><b>DXVAHDDDI_FILTER_EDGE_ENHANCEMENT</b>

<dd>
<p>A value that specifies the filter range of the edge enhancement filter. </p>
</dd>

### -field <a id="DXVAHDDDI_FILTER_ANAMORPHIC_SCALING"></a><a id="dxvahdddi_filter_anamorphic_scaling"></a><b>DXVAHDDDI_FILTER_ANAMORPHIC_SCALING</b>

<dd>
<p>A value that specifies that the filter range of anamorphic scaling. </p>
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
<p>DXVAHDDDI_FILTER is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_FILTER enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
