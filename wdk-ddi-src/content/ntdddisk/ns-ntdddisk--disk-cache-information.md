---
UID: NS.ntdddisk._DISK_CACHE_INFORMATION
title: DISK_CACHE_INFORMATION
author: windows-driver-content
description: The DISK_CACHE_INFORMATION structure is used with the IOCTL_DISK_GET_CACHE_INFORMATION request to retrieve cache information.
old-location: storage\disk_cache_information.htm
old-project: storage
ms.assetid: 17ea8b6b-d41f-4224-880a-49443756d0de
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DISK_CACHE_INFORMATION, DISK_CACHE_INFORMATION, *PDISK_CACHE_INFORMATION
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
req.alt-api: DISK_CACHE_INFORMATION
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
req.iface: 
---

# DISK_CACHE_INFORMATION structure



## -description
<p>The DISK_CACHE_INFORMATION structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559451">IOCTL_DISK_GET_CACHE_INFORMATION</a> request to retrieve cache information.</p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>ParametersSavable</b>

<dd>
<p>Indicates, when set to 1, that the device is capable of saving any parameters in nonvolatile storage.</p>
</dd>

### -field <b>ReadCacheEnabled</b>

<dd>
<p>Indicates, when set to 1, that the read cache is enabled.</p>
</dd>

### -field <b>WriteCacheEnabled</b>

<dd>
<p>Indicates, when set to 1, that the write cache is enabled.</p>
</dd>

### -field <b>ReadRetentionPriority</b>

<dd>
<p>Determines the likelihood of various types of data remaining in the cache. By means of this value, for instance, data cached from a READ or WRITE operation might be given a different priority than data cached under other circumstances, such as prefetch operations. Thus a value of <b>EqualPriority</b> indicates that no data is held in the cache on a preferential basis. When <b>ReadRetentionPriority</b> is set to <b>EqualPriority</b>, all types of data have equal access to cache memory. On the other hand, a value of <b>KeepPrefetchedData</b> indicates that a preference is to be given to prefetched data while a value of <b>KeepReadData</b> indicates that a preference is to be given to data cached from a READ operation. For more information about the values that can be assigned to this member see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552583">DISK_CACHE_RETENTION_PRIORITY</a> enumeration. </p>
</dd>

### -field <b>WriteRetentionPriority</b>

<dd>
<p>See discussion under <b>ReadRetentionPriority</b>.</p>
</dd>

### -field <b>DisablePrefetchTransferLength</b>

<dd>
<p>Disables prefetching. Prefetching might be disabled whenever the number of blocks requested exceeds the value in <b>DisablePrefetchTransferLength</b>. When zero, prefetching is disabled no matter what the size of the block request.</p>
</dd>

### -field <b>PrefetchScalar</b>

<dd>
<p>When <b>TRUE</b>, Indicates that <b>ScalarPrefetch.Maximum</b> should be used together with the transfer length to calculate the amount of data that can be prefetched. When <b>FALSE</b>, <b>BlockPrefetch.Maximum</b> will be the maximum number of disk blocks that can be prefetched.</p>
</dd>

### -field <b>ScalarPrefetch</b>

<dd>
<dl>

### -field <b>Minimum</b>

<dd>
<p>Contains the scalar multiplier of the transfer length of the request when <b>PrefetchScalar</b> is <b>TRUE</b>. If <b>PrefetchScalar</b> is <b>TRUE</b>, the value in <b>ScalarPrefetch.Minimum</b> is multiplied by the transfer length to obtain the minimum amount of data that can be prefetched into the cache on a disk operation. </p>
</dd>

### -field <b>Maximum</b>

<dd>
<p>Contains the scalar multiplier of the transfer length of the request when <b>PrefetchScalar</b> is <b>TRUE</b>. If <b>PrefetchScalar</b> is <b>TRUE</b>, the value in <b>ScalarPrefetch.Maximum</b> is multiplied by the transfer length to obtain the maximum amount of data that can be prefetched into the cache on a disk operation. </p>
</dd>

### -field <b>MaximumBlocks</b>

<dd>
<p>Contains the maximum size, in blocks, of the transfer length. </p>
</dd>
</dl>
</dd>

### -field <b>BlockPrefetch</b>

<dd>
<dl>

### -field <b>Minimum</b>

<dd>
<p>Contains the scalar multiplier of the transfer length of the request when <b>PrefetchScalar</b> is <b>TRUE</b>. If <b>PrefetchScalar</b> is <b>TRUE</b>, the value in <b>ScalarPrefetch.Minimum</b> is multiplied by the transfer length to obtain the minimum amount of data that can be prefetched into the cache on a disk operation. </p>
</dd>

### -field <b>Maximum</b>

<dd>
<p>Contains the scalar multiplier of the transfer length of the request when <b>PrefetchScalar</b> is <b>TRUE</b>. If <b>PrefetchScalar</b> is <b>TRUE</b>, the value in <b>ScalarPrefetch.Maximum</b> is multiplied by the transfer length to obtain the maximum amount of data that can be prefetched into the cache on a disk operation. </p>
</dd>
</dl>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559451">IOCTL_DISK_GET_CACHE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552580">DISK_CACHE_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DISK_CACHE_INFORMATION structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
