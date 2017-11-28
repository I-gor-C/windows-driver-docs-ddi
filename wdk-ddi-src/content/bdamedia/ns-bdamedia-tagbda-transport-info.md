---
UID: NS.bdamedia.tagBDA_TRANSPORT_INFO
title: tagBDA_TRANSPORT_INFO
author: windows-driver-content
description: The BDA_TRANSPORT_INFO structure describes formatting for a stream connection.
old-location: stream\bda_transport_info.htm
old-project: stream
ms.assetid: 995a1d2f-8e2b-426e-a08c-283124ce905e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagBDA_TRANSPORT_INFO, BDA_TRANSPORT_INFO, *PBDA_TRANSPORT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdamedia.h
req.include-header: Bdamedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_TRANSPORT_INFO
req.alt-loc: bdamedia.h
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

# tagBDA_TRANSPORT_INFO structure



## -description
<p>The BDA_TRANSPORT_INFO structure describes formatting for a stream connection. </p>


## -syntax

````
typedef struct tagBDA_TRANSPORT_INFO {
  ULONG          ulcbPhyiscalPacket;
  ULONG          ulcbPhyiscalFrame;
  ULONG          ulcbPhyiscalFrameAlignment;
  REFERENCE_TIME AvgTimePerFrame;
} BDA_TRANSPORT_INFO, *PBDA_TRANSPORT_INFO;
````


## -struct-fields
<dl>

### -field <b>ulcbPhyiscalPacket</b>

<dd>
<p>Size, in bytes, of a physical packet (for example, the size of a satellite link payload). </p>
</dd>

### -field <b>ulcbPhyiscalFrame</b>

<dd>
<p>Size, in bytes, of each physical frame (0 indicates no hardware requirement).</p>
</dd>

### -field <b>ulcbPhyiscalFrameAlignment</b>

<dd>
<p>Capture buffer alignment in bytes (0 and 1 indicate no alignment requirements).</p>
</dd>

### -field <b>AvgTimePerFrame</b>

<dd>
<p>REFERENCE TIME value that indicates the video frame's average display time, in 100-nanosecond units. </p>
</dd>
</dl>

## -remarks
<p>A BDA_TRANSPORT_INFO structure in conjunction with a KSDATARANGE structure makes up a KS_DATARANGE_BDA_TRANSPORT data range. A data range describes a range of data formats. </p>

<p>Pins of filters specify the data ranges they support to enable stream connections to pins of other filters that also support those data ranges.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bdamedia.h (include Bdamedia.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567346">KS_DATARANGE_BDA_TRANSPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563533">KSPIN_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BDA_TRANSPORT_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
