---
UID: NS.MOUNTDEV._MOUNTDEV_UNIQUE_ID
title: _MOUNTDEV_UNIQUE_ID
author: windows-driver-content
description: The MOUNTDEV_UNIQUE_ID structure contains a unique volume ID that a mount manager client provides to the mount manager in response to an IOCTL_MOUNTDEV_QUERY_UNIQUE_ID request.
old-location: storage\mountdev_unique_id.htm
old-project: storage
ms.assetid: cc6cbda8-4056-41e7-98f9-927a99e66081
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _MOUNTDEV_UNIQUE_ID, *PMOUNTDEV_UNIQUE_ID, MOUNTDEV_UNIQUE_ID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mountdev.h
req.include-header: Mountmgr.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MOUNTDEV_UNIQUE_ID
req.alt-loc: mountdev.h
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
---

# _MOUNTDEV_UNIQUE_ID structure



## -description
The MOUNTDEV_UNIQUE_ID structure contains a unique volume ID that a mount manager client provides to the mount manager in response to an <a href="..\mountdev\ni-mountdev-ioctl_mountdev_query_unique_id.md">IOCTL_MOUNTDEV_QUERY_UNIQUE_ID</a> request. 


## -syntax

````
typedef struct _MOUNTDEV_UNIQUE_ID {
  USHORT UniqueIdLength;
  UCHAR  UniqueId[1];
} MOUNTDEV_UNIQUE_ID, *PMOUNTDEV_UNIQUE_ID;
````


## -struct-fields

### -field UniqueIdLength

Contains the length of the unique volume ID. 

### -field UniqueId

Contains the unique volume ID as an array of bytes. 

## -remarks
For a discussion of unique volume IDs and how the mount manager uses them, see <a href="storage.supporting_mount_manager_requests_in_a_storage_class_driver">Supporting Mount Manager Requests in a Storage Class Driver</a>. 

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Mountdev.h (include Mountmgr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.ioctl_mountdev_unique_id_change_notify">IOCTL_MOUNTDEV_UNIQUE_ID_CHANGE_NOTIFY</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MOUNTDEV_UNIQUE_ID structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
