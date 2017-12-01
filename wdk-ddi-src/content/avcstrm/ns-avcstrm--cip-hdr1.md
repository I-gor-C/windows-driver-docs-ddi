---
UID: NS.avcstrm._CIP_HDR1
title: CIP_HDR1
author: windows-driver-content
description: The CIP_HDR1 structure describes the generic data structure of the two quadlet CIP headers (first quadlet of the pair).
old-location: stream\cip_hdr1.htm
old-project: stream
ms.assetid: 15450f33-cb86-4c1d-87d7-2d77a1d66a81
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: CIP_HDR1, CIP_HDR1, *PCIP_HDR1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: avcstrm.h
req.include-header: Avcstrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CIP_HDR1
req.alt-loc: avcstrm.h
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

# CIP_HDR1 structure



## -description
<p>The CIP_HDR1 structure describes the generic data structure of the two quadlet CIP headers (first quadlet of the pair).</p>


## -syntax

````
typedef struct _CIP_HDR1 {
  ULONG DBC  :8;
  ULONG Rsv00  :2;
  ULONG SPH  :1;
  ULONG QPC  :3;
  ULONG FN  :2;
  ULONG DBS  :8;
  ULONG SID  :6;
  ULONG Bit00  :2;
} CIP_HDR1, *PCIP_HDR1;
````


## -struct-fields
<dl>

### -field <b>DBC</b>

<dd>
<p>Data block counter. This is not used by subunit driver. It must be set to 0.</p>
</dd>

### -field <b>Rsv00</b>

<dd>
<p>Reserved bits. Do not use this. It must be 0:0.</p>
</dd>

### -field <b>SPH</b>

<dd>
<p>Specifies a source packet header. A value of 1 indicates the presence of a source packet header. A value of 0 indicates no source packet header.</p>
</dd>

### -field <b>QPC</b>

<dd>
<p>Quadlet padding count (0..7 quadlets).</p>
</dd>

### -field <b>FN</b>

<dd>
<p>Specifies the fractional number.</p>
</dd>

### -field <b>DBS</b>

<dd>
<p>Specifies the data block size in quadlets.</p>
</dd>

### -field <b>SID</b>

<dd>
<p>Specifies the source node ID (ID of transmitter). Not used by the subunit driver. Must be set to 0.</p>
</dd>

### -field <b>Bit00</b>

<dd>
<p>Must be set to 0:0.</p>
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
<dt>Avcstrm.h (include Avcstrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\avcstrm\ns-avcstrm--cip-hdr2-fdf.md">CIP_HDR2_FDF</a>
</dt>
<dt>
<a href="..\avcstrm\ns-avcstrm--cip-hdr2-mpegts.md">CIP_HDR2_MPEGTS</a>
</dt>
<dt>
<a href="..\avcstrm\ns-avcstrm--cip-hdr2-syt.md">CIP_HDR2_SYT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20CIP_HDR1 structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
