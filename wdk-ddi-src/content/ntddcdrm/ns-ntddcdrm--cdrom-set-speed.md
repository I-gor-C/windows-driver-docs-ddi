---
UID: NS.ntddcdrm._CDROM_SET_SPEED
title: CDROM_SET_SPEED
author: windows-driver-content
description: The CDROM_SET_SPEED structure is used with the IOCTL_CDROM_SET_SPEED request to set the spindle speed of a CD-ROM drive during data transfers in which no data loss is permitted.
old-location: storage\cdrom_set_speed.htm
old-project: storage
ms.assetid: 42cffab4-d8a7-4dff-9f53-19aa2769a85c
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: CDROM_SET_SPEED, CDROM_SET_SPEED, *PCDROM_SET_SPEED
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CDROM_SET_SPEED
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

# CDROM_SET_SPEED structure



## -description
<p>The CDROM_SET_SPEED structure is used with the <a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-set-speed.md">IOCTL_CDROM_SET_SPEED</a> request to set the spindle speed of a CD-ROM drive during data transfers in which no data loss is permitted.</p>


## -syntax

````
typedef struct _CDROM_SET_SPEED {
  CDROM_SPEED_REQUEST RequestType;
  USHORT              ReadSpeed;
  USHORT              WriteSpeed;
  WRITE_ROTATION      RotationControl;
} CDROM_SET_SPEED, *PCDROM_SET_SPEED;
````


## -struct-fields
<dl>

### -field RequestType

<dd>
<p>A <a href="..\ntddcdrm\ne-ntddcdrm--cdrom-speed-request.md">CDROM_SPEED_REQUEST</a>-typed value that indicates the type of set speed operation for <a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-set-speed.md">IOCTL_CDROM_SET_SPEED</a> to perform.</p>
</dd>

### -field ReadSpeed

<dd>
<p>The read speed, in kilobytes per second.</p>
</dd>

### -field WriteSpeed

<dd>
<p>The write speed, in kilobytes per second.</p>
</dd>

### -field RotationControl

<dd>
<p>A <a href="..\ntddcdrm\ne-ntddcdrm--write-rotation.md">WRITE_ROTATION</a>-typed value that indicates whether the drive uses constant angular velocity (CAV) or constant linear velocity (CLV) rotation when it writes to a CD.</p>
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
<a href="..\ntddcdrm\ns-ntddcdrm--cdrom-set-streaming.md">CDROM_SET_STREAMING</a>
</dt>
<dt>
<a href="..\ntddcdrm\ne-ntddcdrm--cdrom-speed-request.md">CDROM_SPEED_REQUEST</a>
</dt>
<dt>
<a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-set-speed.md">IOCTL_CDROM_SET_SPEED</a>
</dt>
<dt>
<a href="..\ntddcdrm\ne-ntddcdrm--write-rotation.md">WRITE_ROTATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CDROM_SET_SPEED structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
