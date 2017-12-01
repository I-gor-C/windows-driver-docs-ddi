---
UID: NE.ntddcdrm._CDROM_SPEED_REQUEST
title: CDROM_SPEED_REQUEST
author: windows-driver-content
description: The CDROM_SPEED_REQUEST enumeration indicates which command that the CD-ROM class driver will use to set the spindle speed of a CD-ROM drive.
old-location: storage\cdrom_speed_request.htm
old-project: storage
ms.assetid: 147d2c1c-c12d-4c39-bec5-579ece083ee7
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: OUTPUT_PACKET, OUTPUT_PACKET, *POUTPUT_PACKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CDROM_SPEED_REQUEST
req.alt-loc: ntddcdrm.h
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

# CDROM_SPEED_REQUEST enumeration



## -description
<p>The CDROM_SPEED_REQUEST enumeration indicates which command that the CD-ROM class driver will use to set the spindle speed of a CD-ROM drive.</p>


## -syntax

````
typedef enum _CDROM_SPEED_REQUEST { 
  CdromSetSpeed      = 0,
  CdromSetStreaming  = 1
} CDROM_SPEED_REQUEST, *PCDROM_SPEED_REQUEST;
````


## -enum-fields
<dl>

### -field <a id="CdromSetSpeed"></a><a id="cdromsetspeed"></a><a id="CDROMSETSPEED"></a><b>CdromSetSpeed</b>

<dd>
<p>The CD-ROM class driver will use the SET CD SPEED command to set the spindle speed.</p>
</dd>

### -field <a id="CdromSetStreaming"></a><a id="cdromsetstreaming"></a><a id="CDROMSETSTREAMING"></a><b>CdromSetStreaming</b>

<dd>
<p>The CD-ROM class driver will use the SET STREAMING command to set the spindle speed.</p>
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
<dt>Ntddcdrm.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddcdrm\ns-ntddcdrm--cdrom-set-speed.md">CDROM_SET_SPEED</a>
</dt>
<dt>
<a href="..\ntddcdrm\ns-ntddcdrm--cdrom-set-streaming.md">CDROM_SET_STREAMING</a>
</dt>
<dt>
<a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-set-speed.md">IOCTL_CDROM_SET_SPEED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CDROM_SPEED_REQUEST enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
