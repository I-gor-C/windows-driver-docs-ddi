---
UID: NS.d3dumddi._DXVAHDDDI_CUSTOM_RATE_DATA
title: DXVAHDDDI_CUSTOM_RATE_DATA
author: windows-driver-content
description: The DXVAHDDDI_CUSTOM_RATE_DATA structure describes the video content that a decode device processes.
old-location: display\dxvahdddi_custom_rate_data.htm
old-project: display
ms.assetid: 828c4c42-a74f-4737-b850-5c8299e5afd6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVAHDDDI_CUSTOM_RATE_DATA, DXVAHDDDI_CUSTOM_RATE_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_CUSTOM_RATE_DATA is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_CUSTOM_RATE_DATA
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

# DXVAHDDDI_CUSTOM_RATE_DATA structure



## -description
<p>The DXVAHDDDI_CUSTOM_RATE_DATA structure describes the video content that a decode device processes. </p>


## -syntax

````
typedef struct _DXVAHDDDI_CUSTOM_RATE_DATA {
  DXVAHDDDI_RATIONAL CustomRate;
  UINT               OutputFrames;
  BOOL               InputInterlaced;
  UINT               InputFramesOrFields;
} DXVAHDDDI_CUSTOM_RATE_DATA;
````


## -struct-fields
<dl>

### -field <b>CustomRate</b>

<dd>
<p>
      [in] A <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-rational.md">DXVAHDDDI_RATIONAL</a> structure that specifies a fractional value that represents the input and output frame rate. 
     </p>
</dd>

### -field <b>OutputFrames</b>

<dd>
<p>[in] The number of frames that the driver outputs. </p>
</dd>

### -field <b>InputInterlaced</b>

<dd>
<p>[in] A Boolean value that specifies whether the input stream is progressive (frame) or interlaced (field). </p>
</dd>

### -field <b>InputFramesOrFields</b>

<dd>
<p>[in] The number of the input frames or fields. </p>
</dd>
</dl>

## -remarks
<p>The driver can expose custom rates for the frame rate conversion or the inverse telecine. For example, the driver can provide the following information in the members of DXVAHDDDI_CUSTOM_RATE_DATA for the indicated operation:</p>

<p></p>

<p><b>CustomRate</b> = 2/1</p>

<p><b>OutputFrames</b> = 2</p>

<p><b>InputInterlaced</b> = <b>FALSE</b></p>

<p><b>InputFramesOrFields</b> = 1</p>

<p><b>CustomRate</b> = 4/5</p>

<p><b>OutputFrames</b> = 4</p>

<p><b>InputInterlaced</b> = <b>TRUE</b></p>

<p><b>InputFramesOrFields</b> = 10</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_CUSTOM_RATE_DATA is supported beginning with the Windows 7 operating system.</p>
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
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-rational.md">DXVAHDDDI_RATIONAL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_CUSTOM_RATE_DATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
