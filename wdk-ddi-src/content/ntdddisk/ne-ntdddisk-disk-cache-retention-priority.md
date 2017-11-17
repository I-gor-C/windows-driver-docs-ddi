---
UID: NE.ntdddisk.DISK_CACHE_RETENTION_PRIORITY
title: DISK_CACHE_RETENTION_PRIORITY
author: windows-driver-content
description: The DISK_CACHE_RETENTION_PRIORITY enumeration is used in conjunction with the IOCTL_DISK_GET_CACHE_INFORMATION request and the structure DISK_CACHE_INFORMATION to indicate which kinds data are to be held in the cache on a preferential basis.
old-location: storage\disk_cache_retention_priority.htm
ms.assetid: 238d0b22-bd35-4e8d-9bb5-283af2bbb75b
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DISK_CACHE_RETENTION_PRIORITY
req.alt-loc: ntdddisk.h
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
ms.keywords: READ_ELEMENT_ADDRESS_INFO, READ_ELEMENT_ADDRESS_INFO, *PREAD_ELEMENT_ADDRESS_INFO
req.iface: 
---

# DISK_CACHE_RETENTION_PRIORITY enumeration



## -description
<p>The DISK_CACHE_RETENTION_PRIORITY enumeration is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559451">IOCTL_DISK_GET_CACHE_INFORMATION</a> request and the structure <a href="https://msdn.microsoft.com/library/windows/hardware/ff552580">DISK_CACHE_INFORMATION</a> to indicate which kinds data are to be held in the cache on a preferential basis. </p>


## -syntax

````
typedef enum  { 
  EqualPriority       = 0,
  KeepPrefetchedData  = 1,
  KeepReadData        = 2
} DISK_CACHE_RETENTION_PRIORITY;
````


## -enum-fields
<dl>

### -field <a id="EqualPriority"></a><a id="equalpriority"></a><a id="EQUALPRIORITY"></a><b>EqualPriority</b>

<dd>
<p>Indicates that no data is held in the cache on a preferential basis. All types of data have equal access to cache memory. </p>
</dd>

### -field <a id="KeepPrefetchedData"></a><a id="keepprefetcheddata"></a><a id="KEEPPREFETCHEDDATA"></a><b>KeepPrefetchedData</b>

<dd>
<p>Indicates that a preference is to be given to prefetched data. </p>
</dd>

### -field <a id="KeepReadData"></a><a id="keepreaddata"></a><a id="KEEPREADDATA"></a><b>KeepReadData</b>

<dd>
<p>Indicates that a preference is to be given to data cached from a READ operation.</p>
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
<dt>Ntdddisk.h (include Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552580">DISK_CACHE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559451">IOCTL_DISK_GET_CACHE_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20DISK_CACHE_RETENTION_PRIORITY enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
