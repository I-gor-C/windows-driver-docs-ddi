---
UID: NS:ntdddisk._DISK_CACHE_INFORMATION
title: "_DISK_CACHE_INFORMATION"
author: windows-driver-content
description: The DISK_CACHE_INFORMATION structure is used with the IOCTL_DISK_GET_CACHE_INFORMATION request to retrieve cache information.
old-location: storage\disk_cache_information.htm
old-project: storage
ms.assetid: 17ea8b6b-d41f-4224-880a-49443756d0de
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ntdddisk/PDISK_CACHE_INFORMATION, ntdddisk/DISK_CACHE_INFORMATION, DISK_CACHE_INFORMATION, _DISK_CACHE_INFORMATION, DISK_CACHE_INFORMATION structure [Storage Devices], PDISK_CACHE_INFORMATION structure pointer [Storage Devices], *PDISK_CACHE_INFORMATION, storage.disk_cache_information, structs-disk_def992c5-6103-4eab-8598-4d52808e6b8c.xml, PDISK_CACHE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
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
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntdddisk.h
apiname:
-	DISK_CACHE_INFORMATION
product: Windows
targetos: Windows
req.typenames: DISK_CACHE_INFORMATION, *PDISK_CACHE_INFORMATION
---

# _DISK_CACHE_INFORMATION structure
The DISK_CACHE_INFORMATION structure is used with the <a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_cache_information.md">IOCTL_DISK_GET_CACHE_INFORMATION</a> request to retrieve cache information.

## Syntax
````
typedef struct _DISK_CACHE_INFORMATION {
  BOOLEAN                       ParametersSavable;
  BOOLEAN                       ReadCacheEnabled;
  BOOLEAN                       WriteCacheEnabled;
  DISK_CACHE_RETENTION_PRIORITY ReadRetentionPriority;
  DISK_CACHE_RETENTION_PRIORITY WriteRetentionPriority;
  USHORT                        DisablePrefetchTransferLength;
  BOOLEAN                       PrefetchScalar;
  union {
    struct {
      USHORT Minimum;
      USHORT Maximum;
      USHORT MaximumBlocks;
    } ScalarPrefetch;
    struct {
      USHORT Minimum;
      USHORT Maximum;
    } BlockPrefetch;
  };
} DISK_CACHE_INFORMATION, *PDISK_CACHE_INFORMATION;
````

## Members


`DisablePrefetchTransferLength`

Disables prefetching. Prefetching might be disabled whenever the number of blocks requested exceeds the value in <b>DisablePrefetchTransferLength</b>. When zero, prefetching is disabled no matter what the size of the block request.

`DUMMYUNIONNAME`



`ParametersSavable`

Indicates, when set to 1, that the device is capable of saving any parameters in nonvolatile storage.

`PrefetchScalar`

When <b>TRUE</b>, Indicates that <b>ScalarPrefetch.Maximum</b> should be used together with the transfer length to calculate the amount of data that can be prefetched. When <b>FALSE</b>, <b>BlockPrefetch.Maximum</b> will be the maximum number of disk blocks that can be prefetched.

`ReadCacheEnabled`

Indicates, when set to 1, that the read cache is enabled.

`ReadRetentionPriority`

Determines the likelihood of various types of data remaining in the cache. By means of this value, for instance, data cached from a READ or WRITE operation might be given a different priority than data cached under other circumstances, such as prefetch operations. Thus a value of <b>EqualPriority</b> indicates that no data is held in the cache on a preferential basis. When <b>ReadRetentionPriority</b> is set to <b>EqualPriority</b>, all types of data have equal access to cache memory. On the other hand, a value of <b>KeepPrefetchedData</b> indicates that a preference is to be given to prefetched data while a value of <b>KeepReadData</b> indicates that a preference is to be given to data cached from a READ operation. For more information about the values that can be assigned to this member see the <a href="..\ntdddisk\ne-ntdddisk-disk_cache_retention_priority.md">DISK_CACHE_RETENTION_PRIORITY</a> enumeration.

`WriteCacheEnabled`

Indicates, when set to 1, that the write cache is enabled.

`WriteRetentionPriority`

See discussion under <b>ReadRetentionPriority</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntdddisk.h (include Ntdddisk.h) |

## See Also

<a href="..\ntdddisk\ns-ntdddisk-_disk_cache_information.md">DISK_CACHE_INFORMATION</a>



<a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_cache_information.md">IOCTL_DISK_GET_CACHE_INFORMATION</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DISK_CACHE_INFORMATION structure%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>