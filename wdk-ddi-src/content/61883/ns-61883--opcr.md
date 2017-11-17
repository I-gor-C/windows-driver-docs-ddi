---
UID: NS.61883._OPCR
title: OPCR
author: windows-driver-content
description: The OPCR structure contains initialization values for an output plug.
old-location: ieee\opcr.htm
ms.assetid: fbd6fa74-eb39-4240-947e-1edec1365a83
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 61883.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OPCR
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
ms.keywords: OPCR, OPCR, *POPCR
---

# OPCR structure



## -description
<p>The OPCR structure contains initialization values for an output plug. </p>


## -syntax

````
typedef struct _OPCR {
  ULONG Payload  :10;
  ULONG OverheadID  :4;
  ULONG DataRate  :2;
  ULONG Channel  :6;
  ULONG Reserved  :2;
  ULONG PPCCounter  :6;
  ULONG BCCCounter  :1;
  ULONG OnLine  :1;
} OPCR, *POPCR;
````


## -struct-fields
<dl>

### -field <b>Payload</b>

<dd>
<p>Specifies the connection speed. </p>
</dd>

### -field <b>OverheadID</b>

<dd>
<p>Specifies, for an unconnected output plug, the upper bounds for the bandwidth that the output plug needs for the transmission of an isochronous packet. </p>
</dd>

### -field <b>DataRate</b>

<dd>
<p>Indicates the bit rate that the output plug uses to transmit an isochronous packet. </p>
</dd>

### -field <b>Channel</b>

<dd>
<p>Indicates the channel number that the output plug shall use to transmit the isochronous data flow, for a suspended output plug. For an active output plug it indicates the actual channel number that the output plug uses to transmit the isochronous data flow. For an unconnected output plug it has no meaning.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>PPCCounter</b>

<dd>
<p>Indicates the number of point-to-point connections to the output plug. </p>
</dd>

### -field <b>BCCCounter</b>

<dd>
<p>Indicates, when one, that there is a broadcast-out connection to the output plug. When zero it indicates that there is no connection. </p>
</dd>

### -field <b>OnLine</b>

<dd>
<p>Indicates, when one, that the corresponding output plug is on-line. When zero it indicates that the output plug is off-line.</p>
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
<dt>61883.h (include 61883.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537010">AV_PCR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20OPCR structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
