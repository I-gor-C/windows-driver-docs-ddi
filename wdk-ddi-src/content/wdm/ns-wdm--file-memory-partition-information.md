---
UID: NS.wdm._FILE_MEMORY_PARTITION_INFORMATION
title: FILE_MEMORY_PARTITION_INFORMATION
author: windows-driver-content
description: Stores information about memory partition. This structure is used by the ZwSetInformationFile function.
old-location: ifsk\_file_memory_partition_information.htm
old-project: ifsk
ms.assetid: 1d74aec3-dbc5-4494-ba52-135e3f545c1b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FILE_MEMORY_PARTITION_INFORMATION, FILE_MEMORY_PARTITION_INFORMATION, *PFILE_MEMORY_PARTITION_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_MEMORY_PARTITION_INFORMATION
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# FILE_MEMORY_PARTITION_INFORMATION structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Stores information about memory partition. This structure is used by the <b>ZwSetInformationFile</b> function.</p>


## -syntax

````
typedef struct _FILE_MEMORY_PARTITION_INFORMATION {
  ULONG_PTR OwnerPartitionHandle;
  union {
    struct {
      UCHAR NoCrossPartitionAccess;
      UCHAR Spare[3];
    } DUMMYSTRUCTNAME;
    ULONG AllFlags;
  } Flags;
} FILE_MEMORY_PARTITION_INFORMATION, FILE_MEMORY_PARTITION_INFORMATION;
````


## -struct-fields
<dl>

### -field OwnerPartitionHandle

<dd>
<p>Handle to the specified partition.</p>
</dd>

### -field Flags

<dd>
<dl>

### -field DUMMYSTRUCTNAME

<dd>
<dl>

### -field NoCrossPartitionAccess

<dd>
<p>Determines whether cross-partition access is allowed.</p>
</dd>
</dl>
</dd>

### -field AllFlags

<dd>
<p>Bitwise of all flags. </p>
</dd>
</dl>
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
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>