---
UID: NS.hidclass._HID_XFER_PACKET
title: HID_XFER_PACKET
author: windows-driver-content
description: The HID_XFER_PACKET structure contains information about a HID report that the HID class driver uses with I/O requests to get or set a report.
old-location: hid\hid_xfer_packet.htm
old-project: hid
ms.assetid: b256e6fd-d44f-482a-836d-a812634b4b3a
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HID_XFER_PACKET, HID_XFER_PACKET, *PHID_XFER_PACKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidclass.h
req.include-header: Hidport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HID_XFER_PACKET
req.alt-loc: hidclass.h
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

# HID_XFER_PACKET structure



## -description
<p>The HID_XFER_PACKET structure contains information about a HID report that the HID class driver uses with I/O requests to get or set a report.</p>


## -syntax

````
typedef struct _HID_XFER_PACKET {
  PUCHAR reportBuffer;
  ULONG  reportBufferLen;
  UCHAR  reportId;
} HID_XFER_PACKET, *PHID_XFER_PACKET;
````


## -struct-fields
<dl>

### -field <b>reportBuffer</b>

<dd>
<p>Pointer to a report buffer.</p>
</dd>

### -field <b>reportBufferLen</b>

<dd>
<p>Specifies the length of the report at <b>reportBuffer</b>.</p>
</dd>

### -field <b>reportId</b>

<dd>
<p>Specifies the report ID of the report contained at <b>reportBuffer</b>. This parameter is optional, and, if not specified, should be set to zero.</p>
</dd>
</dl>

## -remarks
<p>The HID class driver uses this structure to specify information about a HID report when it uses an I/O request to get or set a report.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidclass.h (include Hidport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541100">IOCTL_HID_GET_FEATURE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541126">IOCTL_HID_GET_INPUT_REPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541176">IOCTL_HID_SET_FEATURE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541196">IOCTL_HID_SET_OUTPUT_REPORT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HID_XFER_PACKET structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
