---
UID: NE:ufs.UFS_PURGE_STATUS
title: UFS_PURGE_STATUS
author: windows-driver-content
description: Specifies the current status of a purge operation.
old-location: storage\ufs_purge_status.htm
old-project: storage
ms.assetid: 9BC978A9-FA5E-4A1E-9775-1DC9C270F5DC
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UFS_PURGE_STATUS, UFS_PURGE_STATUS enumeration [Storage Devices], UFS_PurgeStatusFailure, UFS_PurgeStatusIdle, UFS_PurgeStatusInProgress, UFS_PurgeStatusInterrupted, UFS_PurgeStatusQueueNotEmpty, UFS_PurgeStatusSuccess, storage.ufs_purge_status, ufs/UFS_PURGE_STATUS, ufs/UFS_PurgeStatusFailure, ufs/UFS_PurgeStatusIdle, ufs/UFS_PurgeStatusInProgress, ufs/UFS_PurgeStatusInterrupted, ufs/UFS_PurgeStatusQueueNotEmpty, ufs/UFS_PurgeStatusSuccess
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ufs.h
api_name:
-	UFS_PURGE_STATUS
product:
- Windows
targetos: Windows
req.typenames: UFS_PURGE_STATUS
req.product: Windows 10 or later.
---

# UFS_PURGE_STATUS Enumeration
Specifies the current status of a purge operation.

## Syntax
```
typedef enum UFS_PURGE_STATUS {
  UFS_PurgeStatusIdle           ,
  UFS_PurgeStatusInProgress     ,
  UFS_PurgeStatusInterrupted    ,
  UFS_PurgeStatusSuccess        ,
  UFS_PurgeStatusQueueNotEmpty  ,
  UFS_PurgeStatusFailure
} ;
```

## Constants

<table>
            
                <tr>
                    <td>UFS_PurgeStatusIdle</td>
                    <td>The status of the purge operation has already been read but was not returned.</td>
                </tr>
            
                <tr>
                    <td>UFS_PurgeStatusInProgress</td>
                    <td>The purge operation is currently in progress.</td>
                </tr>
            
                <tr>
                    <td>UFS_PurgeStatusInterrupted</td>
                    <td>The current purge operation was interrupted.</td>
                </tr>
            
                <tr>
                    <td>UFS_PurgeStatusSuccess</td>
                    <td>The current purge operation was successful.</td>
                </tr>
            
                <tr>
                    <td>UFS_PurgeStatusQueueNotEmpty</td>
                    <td>The current purge operation failed due to the logical queue being not empty.</td>
                </tr>
            
                <tr>
                    <td>UFS_PurgeStatusFailure</td>
                    <td>The current purge operation failed.</td>
                </tr>
</table>

## Remarks

When the <b>UFS_PURGE_STATUS</b> is equal to
the values 2, 3, 4, or 5, the
<b>UFS_PURGE_STATUS</b> is automatically
cleared to <b>UFS_PurgeStatusIdle</b> the first time
that it is read.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ufs.h |

## See Also

<a href="https://msdn.microsoft.com/695D8FE9-FADB-488F-A5F7-7715EAD48DD6">UFS_ATTRIBUTES_DESCRIPTOR</a>