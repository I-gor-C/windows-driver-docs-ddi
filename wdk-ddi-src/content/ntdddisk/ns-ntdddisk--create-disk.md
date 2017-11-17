---
UID: NS.ntdddisk._CREATE_DISK
title: CREATE_DISK
author: windows-driver-content
description: The CREATE_DISK structure is used with the IOCTL_DISK_CREATE_DISK IOCTL to initialize a disk with an empty partition table. The partition table styles are master boot record (MBR) or GUID partition table (GPT).
old-location: storage\create_disk.htm
ms.assetid: 20989831-5ff0-4457-9dae-ceaf34830a2e
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CREATE_DISK
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
ms.keywords: CREATE_DISK, CREATE_DISK, *PCREATE_DISK
req.iface: 
---

# CREATE_DISK structure



## -description
<p>The CREATE_DISK structure is used with the  <a href="https://msdn.microsoft.com/library/windows/hardware/ff559436">IOCTL_DISK_CREATE_DISK</a>  IOCTL to initialize a disk with an empty partition table. The partition table styles are master boot record (MBR)  or GUID partition table (GPT).</p>


## -syntax

````
typedef struct _CREATE_DISK {
  PARTITION_STYLE PartitionStyle;
  union {
    CREATE_DISK_MBR Mbr;
    CREATE_DISK_GPT Gpt;
  };
} CREATE_DISK, *PCREATE_DISK;
````


## -struct-fields
<dl>

### -field <b>PartitionStyle</b>

<dd>
<p>Takes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563773">PARTITION_STYLE</a> enumerated value that specifies the type of partition table to use when formatting the disk.</p>
</dd>

### -field <b>Mbr</b>

<dd>
<p>Contains the signature used to initialize an MBR-style disk partition for the first time. This member is valid when <b>PartitionStyle</b> is PARTITION_STYLE_MBR. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552490">CREATE_DISK_MBR</a>.</p>
</dd>

### -field <b>Gpt</b>

<dd>
<p>Contains data used to initialize a GPT-style disk partition for the first time. This member is valid when <b>PartitionStyle</b> is PARTITION_STYLE_GPT. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552486">CREATE_DISK_GPT</a>. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559436">IOCTL_DISK_CREATE_DISK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552490">CREATE_DISK_MBR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552486">CREATE_DISK_GPT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563773">PARTITION_STYLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20CREATE_DISK structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
