---
UID: NS.d3dkmthk._OUTPUTDUPL_CONTEXT_DEBUG_INFO
title: OUTPUTDUPL_CONTEXT_DEBUG_INFO
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\outputdupl_context_debug_info.htm
ms.assetid: 9b8915a2-e62e-474a-ac03-199ce6d252c2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OUTPUTDUPL_CONTEXT_DEBUG_INFO
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
ms.keywords: OUTPUTDUPL_CONTEXT_DEBUG_INFO, OUTPUTDUPL_CONTEXT_DEBUG_INFO
req.iface: 
---

# OUTPUTDUPL_CONTEXT_DEBUG_INFO structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _OUTPUTDUPL_CONTEXT_DEBUG_INFO {
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS Status;
  HANDLE                          ProcessID;
  UINT32                          AccumulatedPresents;
  LARGE_INTEGER                   LastPresentTime;
  LARGE_INTEGER                   LastMouseTime;
  CHAR                            ProcessName[DXGK_DIAG_PROCESS_NAME_LENGTH];
} OUTPUTDUPL_CONTEXT_DEBUG_INFO;
````


## -struct-fields
<dl>

### -field <b>Status</b>

<dd></dd>

### -field <b>ProcessID</b>

<dd></dd>

### -field <b>AccumulatedPresents</b>

<dd></dd>

### -field <b>LastPresentTime</b>

<dd></dd>

### -field <b>LastMouseTime</b>

<dd></dd>

### -field <b>ProcessName</b>

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