---
UID: NE.ufs.UFS_PURGE_STATUS
title: UFS_PURGE_STATUS
author: windows-driver-content
description: Specifies the current status of a purge operation.
old-location: storage\ufs_purge_status.htm
old-project: storage
ms.assetid: 9BC978A9-FA5E-4A1E-9775-1DC9C270F5DC
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: UDECX_WDF_DEVICE_CONFIG, UDECX_WDF_DEVICE_CONFIG, *PUDECX_WDF_DEVICE_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ufs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFS_PURGE_STATUS
req.alt-loc: Ufs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UFS_PURGE_STATUS enumeration



## -description
<p>Specifies the current status of a purge operation.</p>


## -syntax

````
typedef enum _UFS_PURGE_STATUS { 
  UFS_PurgeStatusIdle           = 0,
  UFS_PurgeStatusInProgress     = 1,
  UFS_PurgeStatusInterrupted    = 2,
  UFS_PurgeStatusSuccess        = 3,
  UFS_PurgeStatusQueueNotEmpty  = 4,
  UFS_PurgeStatusFailure        = 5
} UFS_PURGE_STATUS;
````


## -enum-fields
<dl>

### -field UFS_PurgeStatusIdle

<dd>
<p>The status of the purge operation has already been read but was not returned.</p>
</dd>

### -field UFS_PurgeStatusInProgress

<dd>
<p>The purge operation is currently in progress.</p>
</dd>

### -field UFS_PurgeStatusInterrupted

<dd>
<p>The current purge operation was interrupted.</p>
</dd>

### -field UFS_PurgeStatusSuccess

<dd>
<p>The current purge operation was successful.</p>
</dd>

### -field UFS_PurgeStatusQueueNotEmpty

<dd>
<p>The current purge operation failed due to the logical queue being not empty.</p>
</dd>

### -field UFS_PurgeStatusFailure

<dd>
<p>The current purge operation failed.</p>
</dd>
</dl>

## -remarks
<p>When the <b>UFS_PURGE_STATUS</b> is equal to
the values 2, 3, 4, or 5, the
<b>UFS_PURGE_STATUS</b> is automatically
cleared to <b>UFS_PurgeStatusIdle</b> the first time
that it is read.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufs.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ufs\ne-ufs-ufs-attributes-descriptor.md">UFS_ATTRIBUTES_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20UFS_PURGE_STATUS enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
