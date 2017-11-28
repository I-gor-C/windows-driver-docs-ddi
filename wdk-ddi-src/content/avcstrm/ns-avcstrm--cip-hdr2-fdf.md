---
UID: NS.avcstrm._CIP_HDR2_FDF
title: CIP_HDR2_FDF
author: windows-driver-content
description: The CIP_HDR2_FDF structure describes the second quadlet of a CIP header pair.
old-location: stream\cip_hdr2_fdf.htm
old-project: stream
ms.assetid: 10f01d72-25cc-4a5a-b6e3-8475f09b12e4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: CIP_HDR2_FDF, CIP_HDR2_FDF, *PCIP_HDR2_FDF
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
req.alt-api: CIP_HDR2_FDF
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

# CIP_HDR2_FDF structure



## -description
<p>The CIP_HDR2_FDF structure describes the second quadlet of a CIP header pair.</p>


## -syntax

````
typedef struct _CIP_HDR2_FDF {
  ULONG FDF  :24;
  ULONG FMT  :6;
  ULONG Bit10  :2;
} CIP_HDR2_FDF, *PCIP_HDR2_FDF;
````


## -struct-fields
<dl>

### -field <b>FDF</b>

<dd>
<p>Format dependent field. This is not used for opening a stream. These must be set to 0.</p>
</dd>

### -field <b>FMT</b>

<dd>
<p>CIP format. For example, 000000 = DV and 100000 = MPEG2TS.</p>
</dd>

### -field <b>Bit10</b>

<dd>
<p>Must be set to 1:0</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557668">CIP_HDR1</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20CIP_HDR2_FDF structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
