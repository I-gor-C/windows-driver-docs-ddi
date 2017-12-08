---
UID: NS.DISPMPRT._DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
title: _DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgkarg_system_display_enable_flags.htm
old-project: display
ms.assetid: f23d6692-4c9d-48eb-8d7f-ef70334494b1
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS, DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS, *PDXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
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
---

# _DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS structure



## -description
Reserved for system use. Do not use it in your driver.



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

### -field Reserved

Reserved for system use.

### -field Value

Reserved for system use.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h</dt>
</dl>
</td>
</tr>
</table>