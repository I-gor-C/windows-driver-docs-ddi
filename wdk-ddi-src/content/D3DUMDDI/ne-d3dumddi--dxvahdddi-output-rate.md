---
UID: NE.d3dumddi._DXVAHDDDI_OUTPUT_RATE
title: DXVAHDDDI_OUTPUT_RATE
author: windows-driver-content
description: The DXVAHDDDI_OUTPUT_RATE enumeration contains values that identify the output rate that the driver should use.
old-location: display\dxvahdddi_output_rate.htm
ms.assetid: 61418263-3159-413d-844f-83556ce6baf0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_OUTPUT_RATE is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_OUTPUT_RATE
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

# DXVAHDDDI_OUTPUT_RATE enumeration



## -description
<p>The DXVAHDDDI_OUTPUT_RATE enumeration contains values that identify the output rate that the driver should use. </p>


## -syntax

````
typedef enum _DXVAHDDDI_OUTPUT_RATE { 
  DXVAHDDDI_OUTPUT_RATE_NORMAL  = 0,
  DXVAHDDDI_OUTPUT_RATE_HALF    = 1,
  DXVAHDDDI_OUTPUT_RATE_CUSTOM  = 2
} DXVAHDDDI_OUTPUT_RATE;
````


## -enum-fields
<dl>

### -field <a id="DXVAHDDDI_OUTPUT_RATE_NORMAL"></a><a id="dxvahdddi_output_rate_normal"></a><b>DXVAHDDDI_OUTPUT_RATE_NORMAL</b>

<dd>
<p>A value that specifies that the driver should use normal output rate, which is when one progressive frame becomes one progressive frame and one interlaced frame (two fields) becomes two progressive frames. </p>
</dd>

### -field <a id="DXVAHDDDI_OUTPUT_RATE_HALF"></a><a id="dxvahdddi_output_rate_half"></a><b>DXVAHDDDI_OUTPUT_RATE_HALF</b>

<dd>
<p>A value that specifies that the driver should use half output rate, which is when one progressive frame becomes one progressive frame and one interlaced frame (two fields) becomes one progressive frame.</p>
</dd>

### -field <a id="DXVAHDDDI_OUTPUT_RATE_CUSTOM"></a><a id="dxvahdddi_output_rate_custom"></a><b>DXVAHDDDI_OUTPUT_RATE_CUSTOM</b>

<dd>
<p>A value that specifies that the driver should use a custom output rate for the frame rate conversion or the inverse telecine. For more information about custom output rate, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563045">DXVAHDDDI_CUSTOM_RATE_DATA</a>. </p>
</dd>
</dl>

## -remarks
<p>For more information about output rate, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563092">DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563066">DXVAHDDDI_STREAM_DATA</a>.</p>

<p>For more information about output rate, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563092">DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563066">DXVAHDDDI_STREAM_DATA</a>.</p>

<p>For more information about output rate, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563092">DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563066">DXVAHDDDI_STREAM_DATA</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_OUTPUT_RATE is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563045">DXVAHDDDI_CUSTOM_RATE_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563066">DXVAHDDDI_STREAM_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563092">DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_OUTPUT_RATE enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
