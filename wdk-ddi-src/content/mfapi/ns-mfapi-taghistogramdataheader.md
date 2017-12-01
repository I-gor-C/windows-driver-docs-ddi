---
UID: NS.mfapi.tagHistogramDataHeader
title: tagHistogramDataHeader
author: windows-driver-content
description: The HistogramDataHeader structure describes the blob format for the MF_CAPTURE_METADATA_HISTOGRAM attribute.
old-location: stream\histogramdataheader.htm
old-project: stream
ms.assetid: 42DD34AB-570B-4F71-90BE-7E3AFDB66A84
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagHistogramDataHeader, HistogramDataHeader
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mfapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HistogramDataHeader
req.alt-loc: mfapi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# tagHistogramDataHeader structure



## -description
<p>The  <b>HistogramDataHeader</b> structure describes the blob format for the <b>MF_CAPTURE_METADATA_HISTOGRAM</b> attribute.  </p>


## -syntax

````
typedef struct tagHistogramDataHeader {
  ULONG Size;
  ULONG ChannelMask;
  ULONG Linear;
} HistogramDataHeader;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size in bytes of this header + all following histogram data.</p>
</dd>

### -field <b>ChannelMask</b>

<dd>
<p>Mask of the color channel for the histogram data.</p>
</dd>

### -field <b>Linear</b>

<dd>
<p>1 if linear, 0 if nonlinear.</p>
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
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.histogramblobheader">HistogramBlobHeader</a>
</dt>
<dt>
<a href="stream.histogramgrid">HistogramGrid</a>
</dt>
<dt>
<a href="stream.histogramheader">HistogramHeader</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20HistogramDataHeader structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
