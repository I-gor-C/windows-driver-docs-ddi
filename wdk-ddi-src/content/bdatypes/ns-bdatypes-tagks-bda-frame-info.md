---
UID: NS.bdatypes.tagKS_BDA_FRAME_INFO
title: tagKS_BDA_FRAME_INFO
author: windows-driver-content
description: The KS_BDA_FRAME_INFO structure describes BDA extensions to the KSSTREAM_HEADER structure, which describes a packet of data to be read from or written to a streaming driver pin.
old-location: stream\ks_bda_frame_info.htm
old-project: stream
ms.assetid: df261323-f372-49e7-990a-03c1c5cb743d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagKS_BDA_FRAME_INFO, KS_BDA_FRAME_INFO, *PKS_BDA_FRAME_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: Bdamedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_BDA_FRAME_INFO
req.alt-loc: bdatypes.h
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

# tagKS_BDA_FRAME_INFO structure



## -description
<p>The KS_BDA_FRAME_INFO structure describes BDA extensions to the KSSTREAM_HEADER structure, which describes a packet of data to be read from or written to a streaming driver pin. </p>


## -syntax

````
typedef struct tagKS_BDA_FRAME_INFO {
  ULONG ExtendedHeaderSize;
  DWORD dwFrameFlags;
  ULONG ulEvent;
  ULONG ulChannelNumber;
  ULONG ulSubchannelNumber;
  ULONG ulReason;
} KS_BDA_FRAME_INFO, *PKS_BDA_FRAME_INFO;
````


## -struct-fields
<dl>

### -field <b>ExtendedHeaderSize</b>

<dd>
<p>Size, in bytes, of the BDA extensions described in this extended header structure.</p>
</dd>

### -field <b>dwFrameFlags</b>

<dd>
<p>Flags specific to BDA extensions. </p>
</dd>

### -field <b>ulEvent</b>

<dd>
<p>Identifier of an event.</p>
</dd>

### -field <b>ulChannelNumber</b>

<dd>
<p>Channel number of a television program.</p>
</dd>

### -field <b>ulSubchannelNumber</b>

<dd>
<p>Subchannel number of a television program.</p>
</dd>

### -field <b>ulReason</b>

<dd>
<p>Identifies the reason the packet was transferred.</p>
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
<dt>Bdatypes.h (include Bdamedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567138">KSSTREAM_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_BDA_FRAME_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
