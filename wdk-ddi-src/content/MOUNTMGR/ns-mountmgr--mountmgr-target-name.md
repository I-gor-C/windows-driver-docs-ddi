---
UID: NS.mountmgr._MOUNTMGR_TARGET_NAME
title: MOUNTMGR_TARGET_NAME
author: windows-driver-content
description: The MOUNTMGR_TARGET_NAME structure contains the nonpersistent target device name for a device and is used by mount manager clients with the IOCTL_MOUNTMGR_KEEP_LINKS_WHEN_OFFLINE request to tell the mount manager to keep the symbolic link for a device active even after the device has gone offline.
old-location: storage\mountmgr_target_name.htm
ms.assetid: 7a9cdc0d-0275-4ef9-a570-8788f77099af
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mountmgr.h
req.include-header: Mountmgr.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MOUNTMGR_TARGET_NAME
req.alt-loc: mountmgr.h
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
ms.keywords: MOUNTMGR_TARGET_NAME, MOUNTMGR_TARGET_NAME, *PMOUNTMGR_TARGET_NAME
req.iface: 
---

# MOUNTMGR_TARGET_NAME structure



## -description
<p>The MOUNTMGR_TARGET_NAME structure contains the nonpersistent target device name for a device and is used by mount manager clients with the  <a href="https://msdn.microsoft.com/library/windows/hardware/ff560468">IOCTL_MOUNTMGR_KEEP_LINKS_WHEN_OFFLINE</a> request to tell the mount manager to keep the symbolic link for a device active even after the device has gone offline. </p>


## -syntax

````
typedef struct _MOUNTMGR_TARGET_NAME {
  USHORT DeviceNameLength;
  WCHAR  DeviceName[1];
} MOUNTMGR_TARGET_NAME, *PMOUNTMGR_TARGET_NAME;
````


## -struct-fields
<dl>

### -field <b>DeviceNameLength</b>

<dd>
<p>Contains the length, in bytes, of the device name stored in <b>DeviceName</b>. </p>
</dd>

### -field <b>DeviceName</b>

<dd>
<p>Contains the nonpersistent target device name. </p>
</dd>
</dl>

## -remarks
<p>Nonpersistent target names must contain the full path of a target object name in the system object tree. For example: "\Device\HarddiskVolume1". For a discussion of the different between symbolic links, unique IDs, and nonpersistent device names, see <a href="NULL">Supporting Mount Manager Requests in a Storage Class Driver</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mountmgr.h (include Mountmgr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560468">IOCTL_MOUNTMGR_KEEP_LINKS_WHEN_OFFLINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MOUNTMGR_TARGET_NAME structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
