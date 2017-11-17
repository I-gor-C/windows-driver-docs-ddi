---
UID: NS.ntddvdeo._DXGK_WIN32K_PARAM_DATA
title: DXGK_WIN32K_PARAM_DATA
author: windows-driver-content
description: The DXGK_WIN32K_PARAM_DATA structure is reserved for system use.
old-location: display\dxgk_win32k_param_data.htm
ms.assetid: a6bb2127-64f7-402d-906e-199d5ec1b313
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_WIN32K_PARAM_DATA
req.alt-loc: ntddvdeo.h
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
ms.keywords: DXGK_WIN32K_PARAM_DATA, DXGK_WIN32K_PARAM_DATA, *PDXGK_WIN32K_PARAM_DATA
req.iface: 
---

# DXGK_WIN32K_PARAM_DATA structure



## -description
<p>The DXGK_WIN32K_PARAM_DATA structure is reserved for system use.</p>


## -syntax

````
typedef struct _DXGK_WIN32K_PARAM_DATA {
  PVOID PathsArray;
  PVOID ModesArray;
  ULONG NumPathArrayElements;
  ULONG NumModeArrayElements;
  ULONG SDCFlags;
} DXGK_WIN32K_PARAM_DATA, *PDXGK_WIN32K_PARAM_DATA;
````


## -struct-fields
<dl>

### -field <b>PathsArray</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>ModesArray</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>NumPathArrayElements</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>NumModeArrayElements</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>SDCFlags</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddvdeo.h (include Ntddvdeo.h)</dt>
</dl>
</td>
</tr>
</table>