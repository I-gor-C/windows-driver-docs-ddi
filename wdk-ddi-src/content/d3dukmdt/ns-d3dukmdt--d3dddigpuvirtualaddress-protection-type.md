---
UID: NS.d3dukmdt._D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE
title: D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE
author: windows-driver-content
description: D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE specifies the protection on the graphics processing unit (GPU) virtual address that is mapped.
old-location: display\d3dddigpuvirtualaddress_protection_type.htm
old-project: display
ms.assetid: CA46EEC4-5F3D-4E4C-8C83-6D91BE301C68
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE, D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE
req.alt-loc: d3dukmdt.h
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

# D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE structure



## -description
<p><b>D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE</b> specifies the protection on the graphics processing unit (GPU) virtual address that is mapped.</p>


## -syntax

````
typedef struct _D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE {
  union {
    struct {
      UINT64 Write  :1;
      UINT64 Execute  :1;
      UINT64 Zero  :1;
      UINT64 NoAccess  :1;
      UINT64 SystemUseOnly  :1;
      UINT64 Reserved  :59;
    };
    UINT64 Value;
  };
} D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE;
````


## -struct-fields
<dl>

### -field <b>Write</b>

<dd>
<p>The pages will be allowed read-write access.</p>
</dd>

### -field <b>Execute</b>

<dd>
<p>The pages will be allowed execute access.</p>
</dd>

### -field <b>Zero</b>

<dd>
<p>The pages will be put to the <i>zero</i> state.</p>
</dd>

### -field <b>NoAccess</b>

<dd>
<p>The pages will be put to the <i>invalid</i> state.</p>
</dd>

### -field <b>SystemUseOnly</b>

<dd>
<p>This member is for system use only and should not be set by the user mode driver.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>The consolidated value of the structure's members.</p>
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
<p>Windows 10</p>
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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>