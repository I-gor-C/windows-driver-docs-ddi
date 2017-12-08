---
UID: NE.ntddcdrm._WRITE_ROTATION
title: WRITE_ROTATION
author: windows-driver-content
description: The WRITE_ROTATION enumeration specifies whether a CD-ROM drive uses constant linear velocity (CLV) rotation or constant angular velocity (CAV) rotation when it writes to a CD.
old-location: storage\write_rotation.htm
old-project: storage
ms.assetid: e3569e38-cb56-4e33-baba-c479fc4368da
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
req.alt-api: WRITE_ROTATION
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

# WRITE_ROTATION enumeration



## -description
<p>The WRITE_ROTATION enumeration specifies whether a CD-ROM drive uses constant linear velocity (CLV) rotation or constant angular velocity (CAV) rotation when it writes to a CD.</p>


## -syntax

````
typedef enum _WRITE_ROTATION { 
  CdromDefaultRotation  = 0,
  CdromCAVRotation      = 1
} WRITE_ROTATION, *PWRITE_ROTATION;
````


## -enum-fields
<dl>

### -field CdromDefaultRotation

<dd>
<p>The CD-ROM drive uses the (default) constant linear velocity (CLV) method when it writes to a CD.</p>
</dd>

### -field CdromCAVRotation

<dd>
<p>The CD-ROM drive uses the (default) constant angular velocity (CAV) method when it writes to a CD.</p>
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
<a href="..\ntddcdrm\ne-ntddcdrm--cdrom-speed-request.md">CDROM_SPEED_REQUEST</a>
</dt>
<dt>
<a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-set-speed.md">IOCTL_CDROM_SET_SPEED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20WRITE_ROTATION enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
