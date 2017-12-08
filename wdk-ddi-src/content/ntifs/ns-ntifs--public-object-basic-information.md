---
UID: NS.ntifs._PUBLIC_OBJECT_BASIC_INFORMATION
title: PUBLIC_OBJECT_BASIC_INFORMATION
author: windows-driver-content
description: The PUBLIC_OBJECT_BASIC_INFORMATION structure holds a subset of the full information that is available for an object.
old-location: ifsk\public_object_basic_information.htm
old-project: ifsk
ms.assetid: 2190f88e-6905-4e58-9523-2b6d4864c776
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PUBLIC_OBJECT_BASIC_INFORMATION, PUBLIC_OBJECT_BASIC_INFORMATION, *PPUBLIC_OBJECT_BASIC_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Microsoft Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PUBLIC_OBJECT_BASIC_INFORMATION
req.alt-loc: ntifs.h
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

# PUBLIC_OBJECT_BASIC_INFORMATION structure



## -description
<p>The PUBLIC_OBJECT_BASIC_INFORMATION structure holds a subset of the full information that is available for an object.</p>


## -syntax

````
typedef struct _PUBLIC_OBJECT_BASIC_INFORMATION {
  ULONG       Attributes;
  ACCESS_MASK GrantedAccess;
  ULONG       HandleCount;
  ULONG       PointerCount;
  ULONG       Reserved[10];
} PUBLIC_OBJECT_BASIC_INFORMATION, *PPUBLIC_OBJECT_BASIC_INFORMATION;
````


## -struct-fields
<dl>

### -field Attributes

<dd>
<p>Specifies the attributes of the object.</p>
</dd>

### -field GrantedAccess

<dd>
<p>Specifies a mask that represents the granted access to the object.</p>
</dd>

### -field HandleCount

<dd>
<p>Specifies the number of handles to the object.</p>
</dd>

### -field PointerCount

<dd>
<p>Specifies the number of pointers at an object.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use.</p>
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
<p>This structure is available starting with Microsoft Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>