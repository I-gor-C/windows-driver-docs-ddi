---
UID: NS.ntddstor._STORAGE_READ_CAPACITY
title: STORAGE_READ_CAPACITY
author: windows-driver-content
description: The STORAGE_READ_CAPACITY contains the disk read capacity information returned from a IOCTL_STORAGE_READ_CAPACITIY request.
old-location: storage\storage_read_capacity.htm
ms.assetid: 891F04C5-277B-4197-942E-68ED21019950
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_READ_CAPACITY
req.alt-loc: Ntddstor.h
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
ms.keywords: STORAGE_READ_CAPACITY, STORAGE_READ_CAPACITY, *PSTORAGE_READ_CAPACITY
req.iface: 
---

# STORAGE_READ_CAPACITY structure



## -description
<p>The <b>STORAGE_READ_CAPACITY</b> contains the disk read capacity information returned from a <a href="https://msdn.microsoft.com/FC4CFD33-5632-400A-90E5-583C6D6DFFD9">IOCTL_STORAGE_READ_CAPACITIY</a> request. </p>


## -syntax

````
typedef struct _STORAGE_READ_CAPACITY {
  ULONG         Version;
  ULONG         Size;
  ULONG         BlockLength;
  LARGE_INTEGER NumberOfBlocks;
  LARGE_INTEGER DiskLength;
} STORAGE_READ_CAPACITY, *PSTORAGE_READ_CAPACITY;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure. Set to <b>sizeof</b>(STORAGE_READ_CAPACITY).</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure. Set to <b>sizeof</b>(STORAGE_READ_CAPACITY).</p>
</dd>

### -field <b>BlockLength</b>

<dd>
<p>The number of bytes per block on disk.</p>
</dd>

### -field <b>NumberOfBlocks</b>

<dd>
<p>The total number of blocks on the disk.</p>
</dd>

### -field <b>DiskLength</b>

<dd>
<p>The total disk size in bytes.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
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
<a href="https://msdn.microsoft.com/FC4CFD33-5632-400A-90E5-583C6D6DFFD9">IOCTL_STORAGE_READ_CAPACITIY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20STORAGE_READ_CAPACITY structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
