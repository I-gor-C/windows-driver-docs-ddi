---
UID: NE.d3dkmthk._OUTPUTDUPL_CONTEXT_DEBUG_STATUS
title: _OUTPUTDUPL_CONTEXT_DEBUG_STATUS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\outputdupl_context_debug_status.htm
old-project: display
ms.assetid: 3720b101-cac4-4f81-ae71-088ab03f8756
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _OUTPUTDUPL_CONTEXT_DEBUG_STATUS, OUTPUTDUPL_CONTEXT_DEBUG_STATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OUTPUTDUPL_CONTEXT_DEBUG_STATUS
req.alt-loc: D3dkmthk.h
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
---

# _OUTPUTDUPL_CONTEXT_DEBUG_STATUS enumeration



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef enum _OUTPUTDUPL_CONTEXT_DEBUG_STATUS { 
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS_INACTIVE         = 0,
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS_ACTIVE           = 1,
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS_PENDING_DESTROY  = 2,
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS_FORCE_UINT32     = 0xffffffff
} OUTPUTDUPL_CONTEXT_DEBUG_STATUS;
````


## -enum-fields

### -field OUTPUTDUPL_CONTEXT_DEBUG_STATUS_INACTIVE


### -field OUTPUTDUPL_CONTEXT_DEBUG_STATUS_ACTIVE


### -field OUTPUTDUPL_CONTEXT_DEBUG_STATUS_PENDING_DESTROY


### -field OUTPUTDUPL_CONTEXT_DEBUG_STATUS_FORCE_UINT32


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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>