---
UID: NS.ntddstor._DEVICE_COPY_OFFLOAD_DESCRIPTOR
title: DEVICE_COPY_OFFLOAD_DESCRIPTOR
author: windows-driver-content
description: Used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to describe the copy offload capabilities of a storage device.
old-location: storage\device_copy_offload_descriptor.htm
old-project: storage
ms.assetid: 192684D1-3D01-4EAA-989F-2E21E7187B3B
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEVICE_COPY_OFFLOAD_DESCRIPTOR, DEVICE_COPY_OFFLOAD_DESCRIPTOR, *PDEVICE_COPY_OFFLOAD_DESCRIPTOR
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
req.alt-api: DEVICE_COPY_OFFLOAD_DESCRIPTOR
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

# DEVICE_COPY_OFFLOAD_DESCRIPTOR structure



## -description
<p>Used in conjunction with the 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request to describe the copy offload capabilities of a storage device.</p>


## -syntax

````
typedef struct _DEVICE_COPY_OFFLOAD_DESCRIPTOR {
  ULONG      Version;
  ULONG      Size;
  ULONG      MaximumTokenLifetime;
  ULONG      DefaultTokenLifetime;
  ULONGULONG MaximumTransferSize;
  ULONGULONG OptimalTransferCount;
  ULONG      MaximumDataDescriptors;
  ULONG      MaximumTransferLengthPerDescriptor;
  ULONG      OptimalTransferLengthPerDescriptor;
  USHORT     OptimalTransferLengthGranularity;
  UCHAR      Reserved[2];
} DEVICE_COPY_OFFLOAD_DESCRIPTOR, *PDEVICE_COPY_OFFLOAD_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Contains the size of this structure, in bytes. The value of this member will change as members are added to 
      the structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the total size of the data returned, in bytes. This may include data that follows this 
      structure.</p>
</dd>

### -field <b>MaximumTokenLifetime</b>

<dd>
<p>The maximum lifetime of the token, in seconds.</p>
</dd>

### -field <b>DefaultTokenLifetime</b>

<dd>
<p>The default lifetime of the token, in seconds.</p>
</dd>

### -field <b>MaximumTransferSize</b>

<dd>
<p>The maximum transfer size, in bytes.</p>
</dd>

### -field <b>OptimalTransferCount</b>

<dd>
<p>The optimal transfer size, in bytes.</p>
</dd>

### -field <b>MaximumDataDescriptors</b>

<dd>
<p>The maximum number of data descriptors.</p>
</dd>

### -field <b>MaximumTransferLengthPerDescriptor</b>

<dd>
<p>The maximum transfer length, in blocks, per descriptor.</p>
</dd>

### -field <b>OptimalTransferLengthPerDescriptor</b>

<dd>
<p>The optimal transfer length, in blocks, per descriptor.</p>
</dd>

### -field <b>OptimalTransferLengthGranularity</b>

<dd>
<p>The granularity of the optimal transfer length, in blocks. Transfer lengths that are not an even multiple 
      of this length may be delayed.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DEVICE_COPY_OFFLOAD_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
