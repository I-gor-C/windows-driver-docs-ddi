---
UID: NE.d3dkmthk._OUTPUTDUPL_CONTEXT_DEBUG_STATUS
title: OUTPUTDUPL_CONTEXT_DEBUG_STATUS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\outputdupl_context_debug_status.htm
ms.assetid: 3720b101-cac4-4f81-ae71-088ab03f8756
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
req.iface: 
---

# OUTPUTDUPL_CONTEXT_DEBUG_STATUS enumeration



## -description
<p>Reserved for system use. Do not use in your driver.</p>


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
<dl>

### -field <a id="OUTPUTDUPL_CONTEXT_DEBUG_STATUS_INACTIVE"></a><a id="outputdupl_context_debug_status_inactive"></a><b>OUTPUTDUPL_CONTEXT_DEBUG_STATUS_INACTIVE</b>

<dd></dd>

### -field <a id="OUTPUTDUPL_CONTEXT_DEBUG_STATUS_ACTIVE"></a><a id="outputdupl_context_debug_status_active"></a><b>OUTPUTDUPL_CONTEXT_DEBUG_STATUS_ACTIVE</b>

<dd></dd>

### -field <a id="OUTPUTDUPL_CONTEXT_DEBUG_STATUS_PENDING_DESTROY"></a><a id="outputdupl_context_debug_status_pending_destroy"></a><b>OUTPUTDUPL_CONTEXT_DEBUG_STATUS_PENDING_DESTROY</b>

<dd></dd>

### -field <a id="OUTPUTDUPL_CONTEXT_DEBUG_STATUS_FORCE_UINT32"></a><a id="outputdupl_context_debug_status_force_uint32"></a><b>OUTPUTDUPL_CONTEXT_DEBUG_STATUS_FORCE_UINT32</b>

<dd></dd>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>