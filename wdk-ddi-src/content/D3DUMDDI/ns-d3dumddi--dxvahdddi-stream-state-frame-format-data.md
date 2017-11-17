---
UID: NS.d3dumddi._DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA
title: DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA
author: windows-driver-content
description: The DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA structure describes data that specifies the frame format of the input.
old-location: display\dxvahdddi_stream_state_frame_format_data.htm
ms.assetid: e04e21e7-6d13-4705-8cc9-cc1b00bf04e4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA
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
ms.keywords: DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA, DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA
req.iface: 
---

# DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA structure



## -description
<p>The DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA structure describes data that specifies the frame format of the input. </p>


## -syntax

````
typedef struct _DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA {
  DXVAHDDDI_FRAME_FORMAT FrameFormat;
} DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA;
````


## -struct-fields
<dl>

### -field <b>FrameFormat</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff563056">DXVAHDDDI_FRAME_FORMAT</a>-typed value that indicates the frame format of the input stream. The default value is DXVAHDDDI_FRAME_FORMAT_PROGRESSIVE, which indicates progressive format. </p>
</dd>
</dl>

## -remarks
<p>The Direct3D runtime specifies the DXVAHDDDI_STREAM_STATE_FRAME_FORMAT state in the <b>State</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543098">D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE</a> structure in a call to the driver's <a href="https://msdn.microsoft.com/b48fbe58-056a-4c3b-8e1e-c65515c21ee4">SetVideoProcessStreamState</a> function to set the frame format of the input stream.</p>

<p>The driver might not set the DXVAHDDDI_INPUT_FORMAT_CAPS_RGB_INTERLACED value in the <b>InputFormatCaps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563113">DXVAHDDDI_VPDEVCAPS</a> structure when the driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPDEVCAPS value set. If so and if the input stream is RGB format type, the interlaced frame format is ignored and assumed to be progressive.</p>

<p>The driver also might not set the DXVAHDDDI_INPUT_FORMAT_CAPS_PALETTE_INTERLACED value in the <b>InputFormatCaps</b> member of DXVAHDDDI_VPDEVCAPS. If so and if the input stream is palettized format type, the interlaced frame format is ignored and assumed to be progressive.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543098">D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563056">DXVAHDDDI_FRAME_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563113">DXVAHDDDI_VPDEVCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b48fbe58-056a-4c3b-8e1e-c65515c21ee4">SetVideoProcessStreamState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
