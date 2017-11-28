---
UID: NS.ksmedia.tagKS_VBIINFOHEADER
title: tagKS_VBIINFOHEADER
author: windows-driver-content
description: The KS_VBIINFOHEADER structure describes raw vertical blanking interval (VBI) streams.
old-location: stream\ks_vbiinfoheader.htm
old-project: stream
ms.assetid: 4424be3a-6e73-449c-b5fb-5cbc1109490d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagKS_VBIINFOHEADER, KS_VBIINFOHEADER, *PKS_VBIINFOHEADER
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
req.alt-api: KS_VBIINFOHEADER
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

# tagKS_VBIINFOHEADER structure



## -description
<p>The KS_VBIINFOHEADER structure describes raw vertical blanking interval (VBI) streams.</p>


## -syntax

````
typedef struct tagKS_VBIINFOHEADER {
  ULONG StartLine;
  ULONG EndLine;
  ULONG SamplingFrequency;
  ULONG MinLineStartTime;
  ULONG MaxLineStartTime;
  ULONG ActualLineStartTime;
  ULONG ActualLineEndTime;
  ULONG VideoStandard;
  ULONG SamplesPerLine;
  ULONG StrideInBytes;
  ULONG BufferSize;
} KS_VBIINFOHEADER, *PKS_VBIINFOHEADER;
````


## -struct-fields
<dl>

### -field <b>StartLine</b>

<dd>
<p>Specifies the line number of the first digitized VBI line.</p>
</dd>

### -field <b>EndLine</b>

<dd>
<p>Specifies the line number of the last digitized VBI line.</p>
</dd>

### -field <b>SamplingFrequency</b>

<dd>
<p>Specifies the sampling frequency in hertz (Hz).</p>
</dd>

### -field <b>MinLineStartTime</b>

<dd>
<p>Specifies the shortest possible interval from the leading edge of H-sync in 10-nanosecond units (that is, in hundredths of microseconds).</p>
</dd>

### -field <b>MaxLineStartTime</b>

<dd>
<p>Specifies the longest possible interval from the leading edge of H-sync in 10-nanosecond units (that is, in hundredths of microseconds).</p>
</dd>

### -field <b>ActualLineStartTime</b>

<dd>
<p>Specifies the actual starting point of VBI digitization from the leading edge of H-sync in 10-nanosecond units (that is, in hundredths of microseconds).</p>
</dd>

### -field <b>ActualLineEndTime</b>

<dd>
<p>Specifies the actual ending point for VBI digitization from the leading edge of H-sync in 10-nanosecond units (that is, in hundredths of microseconds).</p>
</dd>

### -field <b>VideoStandard</b>

<dd>
<p>Specifies one or more (logically ORed) values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a> enumeration.</p>
</dd>

### -field <b>SamplesPerLine</b>

<dd>
<p>Specifies the number of samples digitized per video line.</p>
</dd>

### -field <b>StrideInBytes</b>

<dd>
<p>Specifies the stride in bytes between the first sample on a given line and the first sample on the next line. This value can be larger than <b>SamplesPerLine</b>.</p>
</dd>

### -field <b>BufferSize</b>

<dd>
<p>Specifies the size in bytes of the buffer to store the entire digitized VBI signal.</p>
</dd>
</dl>

## -remarks
<p>VBI streams are usually converted to NABTS, CC, and WST streams by downstream filters.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_VBIINFOHEADER structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
