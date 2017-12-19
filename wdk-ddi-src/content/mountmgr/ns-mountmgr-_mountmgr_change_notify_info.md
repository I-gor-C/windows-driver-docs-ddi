---
UID: NS.MOUNTMGR._MOUNTMGR_CHANGE_NOTIFY_INFO
title: _MOUNTMGR_CHANGE_NOTIFY_INFO
author: windows-driver-content
description: The MOUNTMGR_CHANGE_NOTIFY_INFO structure is used by the mount manager to send epic numbers to its clients and vice versa.
old-location: storage\mountmgr_change_notify_info.htm
old-project: storage
ms.assetid: 3b1bb2be-2abb-414a-bf68-9d06e53c2808
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _MOUNTMGR_CHANGE_NOTIFY_INFO, *PMOUNTMGR_CHANGE_NOTIFY_INFO, MOUNTMGR_CHANGE_NOTIFY_INFO, PMOUNTMGR_CHANGE_NOTIFY_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mountmgr.h
req.include-header: Mountmgr.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MOUNTMGR_CHANGE_NOTIFY_INFO
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
---

# _MOUNTMGR_CHANGE_NOTIFY_INFO structure



## -description
The MOUNTMGR_CHANGE_NOTIFY_INFO structure is used by the mount manager to send epic numbers to its clients and vice versa. 



## -syntax

````
typedef struct _MOUNTMGR_CHANGE_NOTIFY_INFO {
  ULONG EpicNumber;
} MOUNTMGR_CHANGE_NOTIFY_INFO, *PMOUNTMGR_CHANGE_NOTIFY_INFO;
````


## -struct-fields

### -field EpicNumber

Contains the value of a counter used by the mount manager to determine if a client has up-to-date information concerning changes in mount manager's persistent ID database. 


## -remarks
For a general discussion of the mount manager and how it communicates with its clients, see <a href="storage.supporting_mount_manager_requests_in_a_storage_class_driver">Supporting Mount Manager Requests in a Storage Class Driver</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="..\mountmgr\ni-mountmgr-ioctl_mountmgr_change_notify.md">IOCTL_MOUNTMGR_CHANGE_NOTIFY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MOUNTMGR_CHANGE_NOTIFY_INFO structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

