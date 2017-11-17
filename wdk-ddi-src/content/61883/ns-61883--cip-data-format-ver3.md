---
UID: NS.61883._CIP_DATA_FORMAT_VER3
title: CIP_DATA_FORMAT_VER3
author: windows-driver-content
description: This structure is used by CipDataFormat.
old-location: ieee\cip_data_format_ver3.htm
ms.assetid: A7EDC949-A2C6-43E9-9CA0-886FEE5282F5
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CIP_DATA_FORMAT_VER3
req.alt-loc: 61883.h
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
ms.keywords: CIP_DATA_FORMAT_VER3, CIP_DATA_FORMAT_VER3, *PCIP_DATA_FORMAT_VER3
---

# CIP_DATA_FORMAT_VER3 structure



## -description
<p>This structure is used by  	<b>CipDataFormat</b>.</p>


## -syntax

````
typedef struct _CIP_DATA_FORMAT_VER3 {
  UCHAR   FMT;
  UCHAR   FDF_hi;
  UCHAR   FDF_mid;
  UCHAR   FDF_lo;
  BOOLEAN bHeader;
  UCHAR   Padding;
  UCHAR   BlockSize;
  UCHAR   Fraction;
  ULONG   BlockPeriod;
  ULONG   BlockPeriodRemainder;
  ULONG   BlocksPerPacket;
} CIP_DATA_FORMAT_VER3, *PCIP_DATA_FORMAT_VER3;
````


## -struct-fields
<dl>

### -field <b>FMT</b>

<dd>
<p>This member is either known, or discovered by an AV/C command.</p>
</dd>

### -field <b>FDF_hi</b>

<dd>
<p>This member is either known, or discovered by an AV/C command.</p>
</dd>

### -field <b>FDF_mid</b>

<dd>
<p>This member is either known, or discovered by an AV/C command.</p>
</dd>

### -field <b>FDF_lo</b>

<dd>
<p>This member is either known, or discovered by an AV/C command.</p>
</dd>

### -field <b>bHeader</b>

<dd>
<p>This member is SPH as defined by IEC-61883.</p>
</dd>

### -field <b>Padding</b>

<dd>
<p>This member is QPC as defined by IEC-61883.</p>
</dd>

### -field <b>BlockSize</b>

<dd>
<p>This member is DBS as defined by IEC-61883.</p>
</dd>

### -field <b>Fraction</b>

<dd>
<p>This member is FN as defined by IEC-61883.</p>
</dd>

### -field <b>BlockPeriod</b>

<dd>
<p>This member is the number of 1394 ticks to send a data block.</p>
</dd>

### -field <b>BlockPeriodRemainder</b>

<dd>
<p>This member is the remainder of 1394 ticks to send a data block.</p>
</dd>

### -field <b>BlocksPerPacket</b>

<dd>
<p>This member is the number of blocks per packet; used for blocking mode only</p>
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
<dt>61883.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20CIP_DATA_FORMAT_VER3 structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
