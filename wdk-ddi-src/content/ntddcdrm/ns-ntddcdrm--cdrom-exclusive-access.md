---
UID: NS.ntddcdrm._CDROM_EXCLUSIVE_ACCESS
title: CDROM_EXCLUSIVE_ACCESS
author: windows-driver-content
description: The CDROM_EXCLUSIVE_ACCESS structure is used with the IOCTL_CDROM_EXCLUSIVE_ACCESS request to query the access state of a CD-ROM device or to lock or unlock the device for exclusive access.
old-location: storage\cdrom_exclusive_access.htm
old-project: storage
ms.assetid: 95248a4a-1fc1-4985-baff-2fe77532d398
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: CDROM_EXCLUSIVE_ACCESS, CDROM_EXCLUSIVE_ACCESS, *PCDROM_EXCLUSIVE_ACCESS
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
req.alt-api: CDROM_EXCLUSIVE_ACCESS
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

# CDROM_EXCLUSIVE_ACCESS structure



## -description
<p>The CDROM_EXCLUSIVE_ACCESS structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559327">IOCTL_CDROM_EXCLUSIVE_ACCESS</a> request to query the access state of a CD-ROM device or to lock or unlock the device for exclusive access.</p>


## -syntax

````
typedef struct _CDROM_EXCLUSIVE_ACCESS {
  EXCLUSIVE_ACCESS_REQUEST_TYPE RequestType;
  ULONG                         Flags;
} CDROM_EXCLUSIVE_ACCESS, *PCDROM_EXCLUSIVE_ACCESS;
````


## -struct-fields
<dl>

### -field <b>RequestType</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff553766">EXCLUSIVE_ACCESS_REQUEST_TYPE</a>-typed enumeration value that specifies the type of operation.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A flag that specifies the characteristics of the operation. The meaning of the flag depends on the type of operation that <b>RequestType</b> specifies. The following table describes the possible values for <b>RequestType</b> and <b>Flags</b>:</p>
<table>
<tr>
<th>RequestType</th>
<th>Flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>ExclusiveAccessQueryState</b></p>
</td>
<td>
<p>Not applicable</p>
</td>
<td>
<p>Not applicable</p>
</td>
</tr>
<tr>
<td rowspan="2">
<p><b>ExclusiveAccessLockDevice</b></p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>Requires that the caller dismount the file system</p>
</td>
</tr>
<tr>
<td>
<p>CDROM_LOCK_IGNORE_VOLUME</p>
</td>
<td>
<p>Ignores the file system mount and locks the device</p>
</td>
</tr>
<tr>
<td>
<p><b>ExclusiveAccessUnlockDevice</b></p>
</td>
<td>
<p>CDROM_NO_MEDIA_NOTIFICATIONS</p>
</td>
<td>
<p>Prevents the sending of a media removal notification and a media arrival notification on an exclusive access unlock</p>
</td>
</tr>
</table>
<p> </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559327">IOCTL_CDROM_EXCLUSIVE_ACCESS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CDROM_EXCLUSIVE_ACCESS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
