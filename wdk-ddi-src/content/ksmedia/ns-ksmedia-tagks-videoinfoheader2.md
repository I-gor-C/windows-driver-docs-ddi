---
UID: NS.ksmedia.tagKS_VIDEOINFOHEADER2
title: tagKS_VIDEOINFOHEADER2
author: windows-driver-content
description: The KS_VIDEOINFOHEADER2 structure describes the details of a video stream, including bob or weave settings, copy protection, and pixel aspect ratio.
old-location: stream\ks_videoinfoheader2.htm
old-project: stream
ms.assetid: 4eb909fe-7ba2-4208-b713-54252022a5cf
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKS_VIDEOINFOHEADER2, KS_VIDEOINFOHEADER2, *PKS_VIDEOINFOHEADER2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_VIDEOINFOHEADER2
req.alt-loc: ksmedia.h
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

# tagKS_VIDEOINFOHEADER2 structure



## -description
<p>The KS_VIDEOINFOHEADER2 structure describes the details of a video stream, including bob or weave settings, copy protection, and pixel aspect ratio.</p>


## -syntax

````
typedef struct tagKS_VIDEOINFOHEADER2 {
  RECT                rcSource;
  RECT                rcTarget;
  DWORD               dwBitRate;
  DWORD               dwBitErrorRate;
  REFERENCE_TIME      AvgTimePerFrame;
  DWORD               dwInterlaceFlags;
  DWORD               dwCopyProtectFlags;
  DWORD               dwPictAspectRatioX;
  DWORD               dwPictAspectRatioY;
  union {
    DWORD dwControlFlags;
    DWORD dwReserved1;
  };
  DWORD               dwReserved2;
  KS_BITMAPINFOHEADER bmiHeader;
} KS_VIDEOINFOHEADER2, *PKS_VIDEOINFOHEADER2;
````


## -struct-fields
<dl>

### -field <b>rcSource</b>

<dd>
<p>Specifies a clipping rectangle that selects the portion of the active video signal to use. </p>
</dd>

### -field <b>rcTarget</b>

<dd>
<p>Specifies a rectangle that indicates what part of the target buffer to use.</p>
</dd>

### -field <b>dwBitRate</b>

<dd>
<p>Specifies a value that indicates the video stream's appropriate data rate, in bits per second.</p>
</dd>

### -field <b>dwBitErrorRate</b>

<dd>
<p>Specifies a value that indicates the video stream's data error rate, in bit errors per second.</p>
</dd>

### -field <b>AvgTimePerFrame</b>

<dd>
<p>Specifies the average time per frame, in 100-nanosecond units.</p>
</dd>

### -field <b>dwInterlaceFlags</b>

<dd>
<p>Specifies interlace information. Undefined flags must be set to zero, or the connection may be rejected. This member can be set to one or more (logical OR) values that are defined in <i>ksmedia.h</i>:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KS_INTERLACE_IsInterlaced</p>
</td>
<td>
<p>Indicates an interlace stream. If 0, then the other KS_INTERLACE_Xxx bits are irrelevant.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_1FieldPerSample</p>
</td>
<td>
<p>Indicates one field per media sample. If zero, indicates two fields per media sample.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_Field1First</p>
</td>
<td>
<p>Indicates that Field 1 is first. If zero, indicates that Field 2 is first. Top field in PAL is Field 1, top field in NTSC is Field 2.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_UNUSED</p>
</td>
<td>
<p>Unused.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_FieldPatternMask</p>
</td>
<td>
<p>Indicates the bits used to specify field pattern.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_FieldPatField1Only</p>
</td>
<td>
<p>Indicates that a stream never contains a Field 2.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_FieldPatField2Only</p>
</td>
<td>
<p>Indicates that a stream never contains a Field 1.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_FieldPatBothRegular</p>
</td>
<td>
<p>Indicates that there will be a Field 2 for every Field 1.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_FieldPatBothIrregular</p>
</td>
<td>
<p>Indicates a random pattern of Field 1s and Field 2s.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_DisplayModeMask</p>
</td>
<td>
<p>Invalid for video capture.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_DisplayModeBobOnly</p>
</td>
<td>
<p>Invalid for video capture.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_DisplayModeWeaveOnly</p>
</td>
<td>
<p>Invalid for video capture.</p>
</td>
</tr>
<tr>
<td>
<p>KS_INTERLACE_DisplayModeBobOrWeave</p>
</td>
<td>
<p>Invalid for video capture.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwCopyProtectFlags</b>

<dd>
<p>Specifies a KSCOPYPROTECTRestrictDuplication value (0x00000001) to indicate if duplication of a stream should be restricted. If undefined, specify zero or the connection will be rejected.</p>
</dd>

### -field <b>dwPictAspectRatioX</b>

<dd>
<p>Specifies the <i>x</i> dimension of the picture-aspect ratio (for example, 16 for a 16 × 9 display). The value is expressed in inches-by-inches, not pixels-by-pixels.</p>
</dd>

### -field <b>dwPictAspectRatioY</b>

<dd>
<p>Specifies the <i>y</i> dimension of the picture aspect ratio (for example, 9 for 16 × 9 display). The value is expressed in inches-by-inches, not pixels-by-pixels.</p>
</dd>

### -field <b>dwControlFlags</b>

<dd>
<p>In operating systems prior to Windows Vista, this member was named <b>dwReserved1</b> and was required to be zero. In Windows Vista, <b>dwReserved1</b> was combined in a union with a new member named <b>dwControlFlags</b>. If used, <b>dwControlFlags</b> contains a bitwise OR of the flags in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>AMCONTROL_USED</p>
</td>
<td>
<p>Indicates the <b>dwControlFlags</b> flags are used.</p>
</td>
</tr>
<tr>
<td>
<p>AMCONTROL_PAD_TO_4x3</p>
</td>
<td>
<p>The image should be padded and displayed in a 4 x 3 area.</p>
</td>
</tr>
<tr>
<td>
<p>AMCONTROL_PAD_TO_16x9</p>
</td>
<td>
<p>The image should be padded and displayed in a 16 x 9 area.</p>
</td>
</tr>
<tr>
<td>
<p>AMCONTROL_COLORINFO_PRESENT</p>
</td>
<td>
<p>Additional color information is contained in the upper 24 bits of the <b>dwControlFlags</b> field.</p>
</td>
</tr>
</table>
<p> </p>
<p>The AMCONTROL_USED flag provides backward compatibility with older filters. If the AMCONTROL_USED flag is not set, the remaining bits in this field should be ignored. If a filter uses any other flags, it should set the AMCONTROL_USED flag. </p>
<p>The two AMCONTROL_PAD_xxx flags are used by decoders to determine the aspect ratio of the output rectangle.</p>
<p>If the AMCONTROL_COLORINFO_PRESENT flag is set, it means the upper 24 bits of the dwControlFlags field are treated as a <a href="..\dxva\ns-dxva--dxva-extendedformat.md">DXVA_ExtendedFormat</a> structure. </p>
<p>See the Remarks section later in this topic for more information about <b>dwControlFlags</b>.</p>
</dd>

### -field <b>dwReserved1</b>

<dd>
<p>This member is for backward compatibility. See <b>dwControlFlags </b>for more information.</p>
</dd>

### -field <b>dwReserved2</b>

<dd>
<p>Reserved for system use. Must be set to zero or the connection will be rejected.</p>
</dd>

### -field <b>bmiHeader</b>

<dd>
<p>Indicates a <a href="stream.ks_bitmapinfoheader">KS_BITMAPINFOHEADER</a> structure that contains color and dimension information for the video image bitmap.</p>
</dd>
</dl>

## -remarks
<p>To describe a video stream without bob or weave settings, use <a href="stream.ks_videoinfoheader">KS_VIDEOINFOHEADER</a>.</p>

<p>The KS_VIDEOINFOHEADER2 structure is identical to the DirectShow <a href="http://go.microsoft.com/fwlink/p/?linkid=96751">VIDEOINFOHEADER2</a> structure.</p>

<p>Capture minidrivers that produce video fields (instead of frames) must use the <a href="stream.ks_datarange_video2">KS_DATARANGE_VIDEO2</a> structure, which contains the KS_VIDEOINFOHEADER2 structure.</p>

<p>A source filter can request that the sink filter take only a section of the video by providing values that effectively define a clipping rectangle in the <b>rcSource</b> member. However, if the sink filter does not check for the clipping rectangle on connection, the sink filter simply renders all of the video, effectively ignoring any clipping information passed from the source filter to the sink filter.</p>

<p>Ideally, a sink filter checks <b>rcSource</b> and if the sink filter does not support image extraction, and the rectangle is <i>not</i> empty, then it rejects the connection. A filter should use the Win32 function <b>SetRectEmpty</b> to reset a rectangle to all zeros (and set <b>IsRectEmpty</b> to later check the rectangle).</p>

<p>The <b>rcTarget</b> member specifies the destination rectangle for the video. Most source filters set this member to all zeros. A downstream filter can request that the video be placed in a particular area of the buffers that it supplies. In this case, it calls the Win32 function <b>QueryAccept</b> with a nonempty target.</p>

<p>If the AMCONTROL_COLORINFO_PRESENT flag is set in the <b>dwControlFlags</b> member, you can cast the <b>dwControlFlags</b> value to a <a href="..\dxva\ns-dxva--dxva-extendedformat.md">DXVA_ExtendedFormat</a> structure to access the extended color information. For more information, see <a href="http://go.microsoft.com/fwlink/p/?linkid=96751">VIDEOINFOHEADER2</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ks_bitmapinfoheader">KS_BITMAPINFOHEADER</a>
</dt>
<dt>
<a href="stream.ks_datarange_video2">KS_DATARANGE_VIDEO2</a>
</dt>
<dt>
<a href="stream.ks_videoinfoheader">KS_VIDEOINFOHEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_VIDEOINFOHEADER2 structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
