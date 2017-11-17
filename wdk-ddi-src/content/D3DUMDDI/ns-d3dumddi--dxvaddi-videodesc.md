---
UID: NS.d3dumddi._DXVADDI_VIDEODESC
title: DXVADDI_VIDEODESC
author: windows-driver-content
description: The DXVADDI_VIDEODESC structure describes a video stream.
old-location: display\dxvaddi_videodesc.htm
ms.assetid: 19121888-ad5c-4596-a7ec-a95fbffda685
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_VIDEODESC
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
ms.keywords: DXVADDI_VIDEODESC, DXVADDI_VIDEODESC
req.iface: 
---

# DXVADDI_VIDEODESC structure



## -description
<p>The DXVADDI_VIDEODESC structure describes a video stream.</p>


## -syntax

````
typedef struct _DXVADDI_VIDEODESC {
  UINT                   SampleWidth;
  UINT                   SampleHeight;
  DXVADDI_EXTENDEDFORMAT SampleFormat;
  D3DDDIFORMAT           Format;
  DXVADDI_FREQUENCY      InputSampleFreq;
  DXVADDI_FREQUENCY      OutputFrameFreq;
  UINT                   UABProtectionLevel;
  UINT                   Reserved;
} DXVADDI_VIDEODESC;
````


## -struct-fields
<dl>

### -field <b>SampleWidth</b>

<dd>
<p>[in] The width of the video sample, in pixels.</p>
</dd>

### -field <b>SampleHeight</b>

<dd>
<p>[in] The height of the video sample, in pixels.</p>
</dd>

### -field <b>SampleFormat</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure that describes the extended format of the video sample.</p>
</dd>

### -field <b>Format</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a> structure that describes the extended format of the video sample.</p>
</dd>

### -field <b>InputSampleFreq</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562911">DXVADDI_FREQUENCY</a> structure that defines the frequency of incoming video.</p>
</dd>

### -field <b>OutputFrameFreq</b>

<dd>
<p>[in] A DXVADDI_FREQUENCY structure that defines the frame rate of output video.</p>
</dd>

### -field <b>UABProtectionLevel</b>

<dd>
<p>[in] A UINT value that specifies the level of data protection that is required when the user accessible bus is present.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] Reserved. Do not use this member.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562911">DXVADDI_FREQUENCY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEODESC structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
