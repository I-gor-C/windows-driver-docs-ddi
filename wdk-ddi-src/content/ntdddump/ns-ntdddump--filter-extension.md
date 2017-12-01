---
UID: NS.ntdddump._FILTER_EXTENSION
title: FILTER_EXTENSION
author: windows-driver-content
description: The crash dump driver passes a pointer to a FILTER_EXTENSION structure when the filter driver callback routines are called.
old-location: storage\filter_extension.htm
old-project: storage
ms.assetid: 1113e917-3273-4ba7-8702-fe90a22fb024
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: FILTER_EXTENSION, FILTER_EXTENSION, *PFILTER_EXTENSION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddump.h
req.include-header: Ntdddump.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista and Windows Server 2008.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILTER_EXTENSION
req.alt-loc: ntdddump.h
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

# FILTER_EXTENSION structure



## -description
<p>The crash dump driver passes a pointer to a FILTER_EXTENSION structure when the filter driver callback routines are called.</p>


## -syntax

````
typedef struct _FILTER_EXTENSION {
  FILTER_DUMP_TYPE    DumpType;
  PDEVICE_OBJECT      DeviceObject;
  DISK_GEOMETRY       Geometry;
  LARGE_INTEGER       DiskSize;
  DISK_PARTITION_INFO PartitionInfo;
  PVOID               DumpData;
} FILTER_EXTENSION, *PFILTER_EXTENSION;
````


## -struct-fields
<dl>

### -field <b>DumpType</b>

<dd>
<p>This parameter indicates the type of dump that this instance of the filter driver is loaded on.</p>
</dd>

### -field <b>DeviceObject</b>

<dd>
<p>A pointer to the device object of the dump volume. This pointer points to the top of the dump volume stack.</p>
</dd>

### -field <b>Geometry</b>

<dd>
<p>The disk geometry of the dump device in <a href="..\ntdddisk\ns-ntdddisk--disk-geometry.md">DISK_GEOMETRY</a> format.</p>
</dd>

### -field <b>DiskSize</b>

<dd>
<p>Size of the disk.</p>
</dd>

### -field <b>PartitionInfo</b>

<dd>
<p>The partition information in <a href="..\ntdddisk\ns-ntdddisk--disk-partition-info.md">DISK_PARTITION_INFO</a> format.</p>
</dd>

### -field <b>DumpData</b>

<dd>
<p>A pointer to the context data that is provided by the filter driver in <a href="..\ntdddump\ns-ntdddump--filter-initialization-data.md">FILTER_INITIALIZATION_DATA</a>.</p>
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
<p>Available starting with Windows Vista and Windows Server 2008.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdddump.h (include Ntdddump.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntdddisk\ns-ntdddisk--disk-geometry.md">DISK_GEOMETRY</a>
</dt>
<dt>
<a href="..\ntdddisk\ns-ntdddisk--disk-partition-info.md">DISK_PARTITION_INFO</a>
</dt>
<dt>
<a href="..\ntdddump\ns-ntdddump--filter-initialization-data.md">FILTER_INITIALIZATION_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FILTER_EXTENSION structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
