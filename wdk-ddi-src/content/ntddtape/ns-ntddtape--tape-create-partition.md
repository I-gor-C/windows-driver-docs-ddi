---
UID: NS.ntddtape._TAPE_CREATE_PARTITION
title: TAPE_CREATE_PARTITION
author: windows-driver-content
description: The TAPE_CREATE_PARTITION structure is used in conjunction with the IOCTL_TAPE_CREATE_PARTITION request to create a specified number of fixed, select, or initiator partitions of a given size on the tape media.
old-location: storage\tape_create_partition.htm
ms.assetid: 5020d2c6-f435-4d22-98a3-23318ffc0baf
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddtape.h
req.include-header: Ntddtape.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TAPE_CREATE_PARTITION
req.alt-loc: ntddtape.h
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
ms.keywords: TAPE_CREATE_PARTITION, TAPE_CREATE_PARTITION, *PTAPE_CREATE_PARTITION
req.iface: 
---

# TAPE_CREATE_PARTITION structure



## -description
<p>The TAPE_CREATE_PARTITION structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560612">IOCTL_TAPE_CREATE_PARTITION</a> request to create a specified number of fixed, select, or initiator partitions of a given size on the tape media.</p>


## -syntax

````
typedef struct _TAPE_CREATE_PARTITION {
  ULONG Method;
  ULONG Count;
  ULONG Size;
} TAPE_CREATE_PARTITION, *PTAPE_CREATE_PARTITION;
````


## -struct-fields
<dl>

### -field <b>Method</b>

<dd>
<p>Indicates the method used to create the partitions. This member can have one of the following values: </p>
<table>
<tr>
<th>Method</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TAPE_FIXED_PARTITIONS</p>
</td>
<td>
<p>Partitions the tape based on the device's default definition of partitions. The <b>Count</b> and <b>Size</b> parameters are ignored. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_SELECT_PARTITIONS</p>
</td>
<td>
<p>Partitions the tape into the number of partitions specified by <b>Count</b>. The <b>Size</b> parameter is ignored. The size of the partitions is determined by the device's default partition size. For more specific information, refer to the documentation for your tape device.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_INITIATOR_PARTITIONS</p>
</td>
<td>
<p>Partitions the tape into the number and size of partitions specified by <b>Count</b> and <b>Size</b>, respectively, except for the last partition. The size of the last partition is the remainder of the tape. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Count</b>

<dd>
<p>Indicates the number of partitions to create.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Indicates the size of each partition, in bytes.</p>
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
<dt>Ntddtape.h (include Ntddtape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567932">TapeMiniCreatePartition</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560612">IOCTL_TAPE_CREATE_PARTITION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20TAPE_CREATE_PARTITION structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
