---
UID: NS.ksmedia.tagKS_VBI_FRAME_INFO
title: tagKS_VBI_FRAME_INFO
author: windows-driver-content
description: The KS_VBI_FRAME_INFO structure extends the KSSTREAM_HEADER structure for vertical blanking interval (VBI) streams.
old-location: stream\ks_vbi_frame_info.htm
ms.assetid: ae6ba1c3-0729-41bd-9fd5-62969bf4b70c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_VBI_FRAME_INFO
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
ms.keywords: tagKS_VBI_FRAME_INFO, KS_VBI_FRAME_INFO, *PKS_VBI_FRAME_INFO
req.iface: 
---

# tagKS_VBI_FRAME_INFO structure



## -description
<p>The KS_VBI_FRAME_INFO structure extends the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567138">KSSTREAM_HEADER</a> structure for vertical blanking interval (VBI) streams.</p>


## -syntax

````
typedef struct tagKS_VBI_FRAME_INFO {
  ULONG                  ExtendedHeaderSize;
  DWORD                  dwFrameFlags;
  LONGLONG               PictureNumber;
  LONGLONG               DropCount;
  DWORD                  dwSamplingFrequency;
  KS_TVTUNER_CHANGE_INFO TvTunerChangeInfo;
  KS_VBIINFOHEADER       VBIInfoHeader;
} KS_VBI_FRAME_INFO, *PKS_VBI_FRAME_INFO;
````


## -struct-fields
<dl>

### -field <b>ExtendedHeaderSize</b>

<dd>
<p>Specifies the size of this structure.</p>
</dd>

### -field <b>dwFrameFlags</b>

<dd>
<p>Specifies flags indicating additional information about the frame captured. During capture, the minidriver sets this member to one of the following values that are defined in <i>ksmedia.h</i>:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KS_VBI_FLAG_FIELD1</p>
</td>
<td>
<p>Indicates the first field of a two-field sequence</p>
</td>
</tr>
<tr>
<td>
<p>KS_VBI_FLAG_FIELD2</p>
</td>
<td>
<p>Indicates the second field of a two-field sequence</p>
</td>
</tr>
<tr>
<td>
<p>KS_VBI_FLAG_MV_PRESENT</p>
</td>
<td>
<p>Indicates Macrovision protection scheme</p>
</td>
</tr>
<tr>
<td>
<p>KS_VBI_FLAG_MV_HARDWARE</p>
</td>
<td>
<p>Indicates Macrovision hardware support</p>
</td>
</tr>
<tr>
<td>
<p>KS_VBI_FLAG_MV_DETECTED</p>
</td>
<td>
<p>Indicates Macrovision detected</p>
</td>
</tr>
<tr>
<td>
<p>KS_VBI_FLAG_TVTUNER_CHANGE</p>
</td>
<td>
<p>Indicates that the <b>TvTunerChangeInfo</b> member structure contains valid data</p>
</td>
</tr>
<tr>
<td>
<p>KS_VBI_FLAG_VBIINFOHEADER_CHANGE</p>
</td>
<td>
<p>Indicates that the <b>VBIInfoHeader</b> member structure contains valid data</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PictureNumber</b>

<dd>
<p>Specifies a count representing the current picture number. Initialize or update this value on transition into KSSTATE_ACQUIRE.</p>
</dd>

### -field <b>DropCount</b>

<dd>
<p>Specifies the number of pictures that were not captured. When capturing video, the minidriver sets this member. This counter should be incremented whenever a frame should have been captured but was not; this condition usually arises when no buffers were available during capture. Initialize or update this value on transition into KSSTATE_ACQUIRE.</p>
</dd>

### -field <b>dwSamplingFrequency</b>

<dd>
<p>Specifies the sampling frequency in hertz (Hz).</p>
</dd>

### -field <b>TvTunerChangeInfo</b>

<dd>
<p>Specifies information about the current VBI data source, including country/region code, analog video standard, and channel. This member is only valid if <b>dwFrameFlags</b> specifies the KS_VBI_FLAG_TVTUNER_CHANGE flag. </p>
</dd>

### -field <b>VBIInfoHeader</b>

<dd>
<p>Specifies information about the current VBI data source, including start line, end line, sampling frequency, and video standard. This member is only valid if <b>dwFrameFlags</b> specifies the KS_VBI_FLAG_VBIINFOHEADER_CHANGE flag.</p>
</dd>
</dl>

## -remarks
<p>The KS_VBI_FRAME_INFO structure provides a way to return information about a captured frame, as well as providing tuning information to VBI decoders.</p>

<p>The <b>PictureNumber</b> member count represents the count of the current picture based on the format used to open the stream. This count is calculated in one of two ways, depending on the device:</p>

<p>Measure the time since the stream was started and divide by the frame duration. This method is appropriate for devices that do not provide their own clock. For example: <i>PictureNumber = (CurrentStreamTime − StartStreamTime) / FrameDuration</i></p>

<p>Add together the count of frames captured and the count of frames dropped. This method is appropriate for devices that provide their own clock. For example: <i>PictureNumber = FramesCaptured + FramesDropped</i></p>

<p>When calculating the <b>PictureNumber</b> and <b>DropCount</b>, it is important to use the frame duration specified when the stream was opened, which may not necessarily match the rate at which the device is actually producing images. For example, a USB camera may only produce images at 7.5 fps, but a client could open the stream at 8 fps. In this case, all calculations should use the 8 fps number. For more information about updating <b>PictureNumber</b> and <b>DropCount</b> see <a href="NULL">Capturing Video</a>.</p>

<p>The <b>dwSamplingFrequency</b> member is not used by Microsoft VBI codecs, but may be used by other WDM codecs. It must be the same as the <b>VBIInfoHeader</b>.<i>SamplingFrequency</i> member. A minidriver indicates a change in sampling frequency by setting the KS_VBI_FLAG_VBIINFOHEADER_CHANGE bit in the <b>dwFrameFlags</b> member, and filling in all members, including <b>dwSamplingFrequency</b>, in the <b>VBIInfoHeader</b> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567138">KSSTREAM_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567691">KS_TVTUNER_CHANGE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567692">KS_VBIINFOHEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_VBI_FRAME_INFO structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
