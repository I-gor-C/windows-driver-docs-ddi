---
UID: NS.ntifs.__PUBLIC_OBJECT_TYPE_INFORMATION
title: PUBLIC_OBJECT_TYPE_INFORMATION
author: windows-driver-content
description: The PUBLIC_OBJECT_TYPE_INFORMATION structure holds the type name of the object.
old-location: ifsk\public_object_type_information.htm
old-project: ifsk
ms.assetid: 7b80c3df-befe-4648-ab61-78cfb8d4b7ef
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: PUBLIC_OBJECT_TYPE_INFORMATION, PUBLIC_OBJECT_TYPE_INFORMATION, *PPUBLIC_OBJECT_TYPE_INFORMATION
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
req.alt-api: PUBLIC_OBJECT_TYPE_INFORMATION
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

# PUBLIC_OBJECT_TYPE_INFORMATION structure



## -description
<p>The PUBLIC_OBJECT_TYPE_INFORMATION structure holds the type name of the object.</p>


## -syntax

````
typedef struct __PUBLIC_OBJECT_TYPE_INFORMATION {
  UNICODE_STRING TypeName;
  ULONG          Reserved[22];
} PUBLIC_OBJECT_TYPE_INFORMATION, *PPUBLIC_OBJECT_TYPE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>TypeName</b>

<dd>
<p>Specifies the type name of the object.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. </p>
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