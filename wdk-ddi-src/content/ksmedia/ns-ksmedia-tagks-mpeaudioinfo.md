---
UID: NS.ksmedia.tagKS_MPEAUDIOINFO
title: tagKS_MPEAUDIOINFO
author: windows-driver-content
description: The KS_MPEGAUDIOINFO structure describes an MPEG audio stream.
old-location: stream\ks_mpegaudioinfo.htm
old-project: stream
ms.assetid: df8a1e95-211a-47df-a904-4578cd0a7dc9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKS_MPEAUDIOINFO, KS_MPEGAUDIOINFO, *PKS_MPEGAUDIOINFO
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
req.alt-api: KS_MPEGAUDIOINFO
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

# tagKS_MPEAUDIOINFO structure



## -description
<p>The KS_MPEGAUDIOINFO structure describes an MPEG audio stream.</p>


## -syntax

````
typedef struct tagKS_MPEAUDIOINFO {
  DWORD dwFlags;
  DWORD dwReserved1;
  DWORD dwReserved2;
  DWORD dwReserved3;
} KS_MPEGAUDIOINFO, *PKS_MPEGAUDIOINFO;
````


## -struct-fields
<dl>

### -field dwFlags

<dd>
<p>Specifies the time base for audio timestamps. Reject the connection if undefined bits are not 0. The following flag is defined.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KS_MPEGAUDIOINFO_27MhzTimebase</p>
</td>
<td>
<p>Specifies that PTS and DTS timestamps advance at 27 MHz rather than 90 kHz.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field dwReserved1

<dd>
<p>Must be 0; otherwise, reject the connection.</p>
</dd>

### -field dwReserved2

<dd>
<p>Must be 0; otherwise, reject the connection.</p>
</dd>

### -field dwReserved3

<dd>
<p>Must be 0; otherwise, reject the connection.</p>
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