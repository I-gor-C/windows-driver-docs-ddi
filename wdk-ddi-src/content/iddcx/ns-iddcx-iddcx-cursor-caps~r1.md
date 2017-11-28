---
UID: NS.iddcx.IDDCX_CURSOR_CAPS~r1
title: IDDCX_CURSOR_CAPS
author: windows-driver-content
description: Gives information about the capabilities of the cursor.
old-location: display\iddcx_cursor_caps.htm
old-project: display
ms.assetid: 3bd92999-07f3-43bb-a826-4fea3e19168a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_CURSOR_CAPS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_CURSOR_CAPS
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDDCX_CURSOR_CAPS structure



## -description
<p>
                 Gives information about the capabilities of the cursor.
             </p>


## -syntax

````
typedef struct IDDCX_CURSOR_CAPS {
  UINT                     Size;
  IDDCX_XOR_CURSOR_SUPPORT ColorXorCursorSupport;
  BOOL                     AlphaCursorSupport;
  UINT                     MaxX;
  UINT                     MaxY;
} IDDCX_CURSOR_CAPS, *IDDCX_CURSOR_CAPS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>
                     Total size of the structure.
                 </p>
</dd>

### -field <b>ColorXorCursorSupport</b>

<dd>
<p>
                     Indicates what level of support the driver has for XOR masks in the 32-bit masked color cursor format.</p>
<div class="alert"><b>Note</b>  The OS first converts any monochrome cursor to a color mask cursor.</div>
<div> </div>
</dd>

### -field <b>AlphaCursorSupport</b>

<dd>
<p>
                     Indicates if the adapter supports the 32-bit alpha cursor format. Most cursors are alpha format.
                 </p>
</dd>

### -field <b>MaxX</b>

<dd>
<p>
                     The maximum width supported for all supported cursor types.
                 </p>
</dd>

### -field <b>MaxY</b>

<dd>
<p>
                     The maximum height support for all cursor types.
                 </p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>