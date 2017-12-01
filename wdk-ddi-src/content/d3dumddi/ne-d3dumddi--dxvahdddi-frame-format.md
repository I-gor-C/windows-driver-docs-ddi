---
UID: NE.d3dumddi._DXVAHDDDI_FRAME_FORMAT
title: DXVAHDDDI_FRAME_FORMAT
author: windows-driver-content
description: The DXVAHDDDI_FRAME_FORMAT enumeration contains values that identify the frame format.
old-location: display\dxvahdddi_frame_format.htm
old-project: display
ms.assetid: 82fded96-9321-47a8-8bdd-65c5a75951ac
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_FRAME_FORMAT is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_FRAME_FORMAT
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

# DXVAHDDDI_FRAME_FORMAT enumeration



## -description
<p>The DXVAHDDDI_FRAME_FORMAT enumeration contains values that identify the frame format. </p>


## -syntax

````
typedef enum _DXVAHDDDI_FRAME_FORMAT { 
  DXVAHDDDI_FRAME_FORMAT_PROGRESSIVE                    = 0,
  DXVAHDDDI_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST     = 1,
  DXVAHDDDI_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST  = 2
} DXVAHDDDI_FRAME_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="DXVAHDDDI_FRAME_FORMAT_PROGRESSIVE"></a><a id="dxvahdddi_frame_format_progressive"></a><b>DXVAHDDDI_FRAME_FORMAT_PROGRESSIVE</b>

<dd>
<p>A value that specifies that the frame format is progressive. </p>
</dd>

### -field <a id="DXVAHDDDI_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST"></a><a id="dxvahdddi_frame_format_interlaced_top_field_first"></a><b>DXVAHDDDI_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST</b>

<dd>
<p>A value that specifies that the frame format is interlaced with two fields. The top (even) field is displayed first. </p>
</dd>

### -field <a id="DXVAHDDDI_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST"></a><a id="dxvahdddi_frame_format_interlaced_bottom_field_first"></a><b>DXVAHDDDI_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST</b>

<dd>
<p>A value that specifies that the frame format is interlaced with two fields. The bottom (odd) field is displayed first. </p>
</dd>
</dl>

## -remarks
<p>The <a href="wdkgloss.f#wdkgloss.fourcc#wdkgloss.fourcc"><i>FOURCC</i></a> format of the surface defines whether the interlaced fields are interleaved or not. For example, NV12 is an interlaced format with interleaved fields whereas NV24 is an interlaced format with non-interleaved fields.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_FRAME_FORMAT is supported beginning with the Windows 7 operating system.</p>
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
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-stream-state-frame-format-data.md">DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_FRAME_FORMAT enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
