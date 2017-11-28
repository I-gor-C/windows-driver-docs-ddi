---
UID: NS.ntddstor._STORAGE_DEVICE_RESILIENCY_DESCRIPTOR
title: STORAGE_DEVICE_RESILIENCY_DESCRIPTOR
author: windows-driver-content
description: Reserved for system use.
old-location: storage\storage_device_resiliency_descriptor.htm
old-project: storage
ms.assetid: 71351CB7-1295-4797-802C-23A6B1C2C53F
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, *PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_DEVICE_RESILIENCY_DESCRIPTOR
req.alt-loc: ntddstor.h
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

# STORAGE_DEVICE_RESILIENCY_DESCRIPTOR structure



## -description
<p>Reserved for system use.</p>


## -syntax

````
typedef struct _STORAGE_DEVICE_RESILIENCY_DESCRIPTOR {
  ULONG Version;
  ULONG Size;
  ULONG NameOffset;
  ULONG NumberOfLogicalCopies;
  ULONG NumberOfPhysicalCopies;
  ULONG PhysicalDiskRedundancy;
  ULONG NumberOfColumns;
  ULONG Interleave;
} STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, *PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Contains the size of this structure, in bytes. The value of this member will change as members are added to 
      the structure. Set to 
      <code>sizeof(STORAGE_DEVICE_RESILIENCY_DESCRIPTOR)</code>.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the total size of the data returned, in bytes. This may include data that follows this 
      structure.</p>
</dd>

### -field <b>NameOffset</b>

<dd>
<p>Byte offset to the null-terminated ASCII string containing the resiliency properties Name. For devices with 
      no Name property, this will be zero.</p>
</dd>

### -field <b>NumberOfLogicalCopies</b>

<dd>
<p>Number of logical copies of data that are available.</p>
</dd>

### -field <b>NumberOfPhysicalCopies</b>

<dd>
<p>Number of complete copies of data that are stored.</p>
</dd>

### -field <b>PhysicalDiskRedundancy</b>

<dd>
<p>Number of disks that can fail without leading to data loss.</p>
</dd>

### -field <b>NumberOfColumns</b>

<dd>
<p>Number of columns in the storage device.</p>
</dd>

### -field <b>Interleave</b>

<dd>
<p>Size of a stripe unit of the storage device, in bytes. This is also referred to as the stripe width or 
      interleave of the storage device.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_DEVICE_RESILIENCY_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
