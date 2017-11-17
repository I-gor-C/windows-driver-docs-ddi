---
UID: NS.ksmedia.tagKS_DATARANGE_VIDEO_VBI
title: tagKS_DATARANGE_VIDEO_VBI
author: windows-driver-content
description: The KS_DATARANGE_VIDEO_VBI structure describes a range of data formats containing vertical blanking interval (VBI) data.
old-location: stream\ks_datarange_video_vbi.htm
ms.assetid: 83801ea2-1beb-4b73-8906-ffefee67a2ac
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
req.alt-api: KS_DATARANGE_VIDEO_VBI
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
ms.keywords: tagKS_DATARANGE_VIDEO_VBI, KS_DATARANGE_VIDEO_VBI, *PKS_DATARANGE_VIDEO_VBI
req.iface: 
---

# tagKS_DATARANGE_VIDEO_VBI structure



## -description
<p>The KS_DATARANGE_VIDEO_VBI structure describes a range of data formats containing vertical blanking interval (VBI) data.</p>


## -syntax

````
typedef struct tagKS_DATARANGE_VIDEO_VBI {
  KSDATARANGE                 DataRange;
  BOOL                        bFixedSizeSamples;
  BOOL                        bTemporalCompression;
  DWORD                       StreamDescriptionFlags;
  DWORD                       MemoryAllocationFlags;
  KS_VIDEO_STREAM_CONFIG_CAPS ConfigCaps;
  KS_VBIINFOHEADER            VBIInfoHeader;
} KS_DATARANGE_VIDEO_VBI, *PKS_DATARANGE_VIDEO_VBI;
````


## -struct-fields
<dl>

### -field <b>DataRange</b>

<dd>
<p>Specifies major, minor, and specifier identifiers of the range of formats being described.</p>
</dd>

### -field <b>bFixedSizeSamples</b>

<dd>
<p>Specifies that all the samples are the same size if set to <b>TRUE</b>.</p>
</dd>

### -field <b>bTemporalCompression</b>

<dd>
<p>Specifies whether each sample can stand independently on its own, without relying on previous or future samples.</p>
</dd>

### -field <b>StreamDescriptionFlags</b>

<dd>
<p>Unused and should be set to zero.</p>
</dd>

### -field <b>MemoryAllocationFlags</b>

<dd>
<p>Unused and should be set to zero.</p>
</dd>

### -field <b>ConfigCaps</b>

<dd>
<p>Specifies the configuration of the stream, including scaling, cropping, and frame and data rates.</p>
</dd>

### -field <b>VBIInfoHeader</b>

<dd>
<p>Indicates VBI-specific information for the range of formats being described.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567706">KS_VIDEO_STREAM_CONFIG_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567692">KS_VBIINFOHEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DATARANGE_VIDEO_VBI structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
