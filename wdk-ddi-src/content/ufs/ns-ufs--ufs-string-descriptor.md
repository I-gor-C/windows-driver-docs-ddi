---
UID: NS.ufs._UFS_STRING_DESCRIPTOR
title: UFS_STRING_DESCRIPTOR
author: windows-driver-content
description: The UFS_STRING_DESCRIPTOR structure describes either the Manufacturer Name, Product Name, OEM ID, or Serial Number as a string.
old-location: storage\ufs_string_descriptor.htm
old-project: storage
ms.assetid: 1F32DA95-6801-4C48-B3C4-A47C3E1C678B
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: UFS_STRING_DESCRIPTOR, UFS_STRING_DESCRIPTOR, *PUFS_STRING_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ufs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFS_STRING_DESCRIPTOR
req.alt-loc: Ufs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UFS_STRING_DESCRIPTOR structure



## -description
<p>The <b>UFS_STRING_DESCRIPTOR</b> structure describes either the Manufacturer Name, Product Name, OEM ID, or Serial Number as a string. </p>


## -syntax

````
typedef struct _UFS_STRING_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR String[UFS_MAX_UNICODE_STRING_LEN];
} UFS_STRING_DESCRIPTOR, *PUFS_STRING_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLength</b>

<dd>
<p>Specifies the length, in bytes, of this descriptor.</p>
</dd>

### -field <b>bDescriptorIDN</b>

<dd>
<p>Specifies the type of the descriptor. This descriptor will have a value of <b>UFS_DESC_STRING_IDN</b>.</p>
</dd>

### -field <b>String</b>

<dd>
<p>Contains either the Manufacturer Name, Product Name, OEM ID, or Serial Number as a string.</p>
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
<dt>Ufs.h</dt>
</dl>
</td>
</tr>
</table>