---
UID: NS.dispmprt._DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
title: DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgkarg_system_display_enable_flags.htm
old-project: display
ms.assetid: f23d6692-4c9d-48eb-8d7f-ef70334494b1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS, DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS, *PDXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
req.alt-loc: Dispmprt.h
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
---

# DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS structure



## -description
<p>Reserved for system use. Do not use it in your driver.
</p>


## -syntax

````
typedef struct _DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT   Value;
  };
} DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS, *PDXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS;
````


## -struct-fields
<dl>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Reserved for system use.</p>
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
<dt>Dispmprt.h</dt>
</dl>
</td>
</tr>
</table>