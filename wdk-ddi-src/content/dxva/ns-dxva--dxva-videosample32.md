---
UID: NS.dxva._DXVA_VideoSample32
title: DXVA_VideoSample32
author: windows-driver-content
description: The DXVA_VideoSample32 structure is used for forwarding 32-bit DXVA_DeinterlaceBltEx calls on 64-bit drivers.
old-location: display\dxva_videosample32.htm
old-project: display
ms.assetid: 78609b64-38fa-4431-bc74-8a83fe687a45
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVA_VideoSample32, DXVA_VideoSample32
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: This structure applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.Only compiles for a 64-bit version of the operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_VideoSample32
req.alt-loc: dxva.h
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

# DXVA_VideoSample32 structure



## -description
<p>The DXVA_VideoSample32 structure is used for forwarding  32-bit <a href="https://msdn.microsoft.com/library/windows/hardware/ff563915">DXVA_DeinterlaceBltEx</a> calls on 64-bit drivers.</p>


## -syntax

````
typedef struct _DXVA_VideoSample32 {
  REFERENCE_TIME   rtStart;
  REFERENCE_TIME   rtEnd;
  DWORD            SampleFormat;
  DWORD            SampleFlags;
  DWORD            lpDDSSrcSurface;
  RECT             rcSrc;
  RECT             rcDst;
  DXVA_AYUVsample2 Palette[16];
} DXVA_VideoSample32;
````


## -struct-fields
<dl>

### -field <b>rtStart</b>

<dd>
<p>Specifies the start time of the sample.</p>
</dd>

### -field <b>rtEnd</b>

<dd>
<p>Specifies the end time of the sample.</p>
</dd>

### -field <b>SampleFormat</b>

<dd>
<p>Specifies the format of the sample as defined by values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563967">DXVA_ExtendedFormat</a> enumeration type. </p>
</dd>

### -field <b>SampleFlags</b>

<dd>
<p>Specifies a collection of flags that indicate changes in the current sample frame from the previous sample frame. This member is a bitwise-OR of one or more of the flags in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564037">DXVA_SampleFlags</a> enumeration type.</p>
</dd>

### -field <b>lpDDSSrcSurface</b>

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551733">DD_SURFACE_LOCAL</a> structure that represents the sample.</p>
</dd>

### -field <b>rcSrc</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that describes the upper-left and lower-right points of a rectangle on the source surface. These points define the area of the source data for the bit-block transfer and its position on the source surface.</p>
</dd>

### -field <b>rcDst</b>

<dd>
<p>Specifies a RECT structure that describes the upper-left and lower-right points of a rectangle on the destination surface. These points define the area in which the bit-block transfer should occur and its position on the destination surface.</p>
</dd>

### -field <b>Palette</b>

<dd>
<p>Specifies an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563116">DXVA_AYUVsample2</a> structures that represent a complete 16-color palette for palletized video substream pixel formats. The driver uses this palette to composite the substream sample. For nonpalletized pixel formats, the palette is zero and can be ignored.</p>
</dd>
</dl>

## -remarks
<p>The compiler adds 4 bytes of padding to align the structure to 8 bytes.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.Only compiles for a 64-bit version of the operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563116">DXVA_AYUVsample2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563915">DXVA_DeinterlaceBltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563967">DXVA_ExtendedFormat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564037">DXVA_SampleFlags</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564045">DXVA_SampleFormat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551733">DD_SURFACE_LOCAL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_VideoSample32 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
