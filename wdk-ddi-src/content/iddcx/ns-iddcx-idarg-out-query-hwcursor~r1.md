---
UID: NS.iddcx.IDARG_OUT_QUERY_HWCURSOR~r1
title: IDARG_OUT_QUERY_HWCURSOR
author: windows-driver-content
description: Gives information about the coordinates and shape of the current cursor.
old-location: display\idarg_out_query_hwcursor.htm
old-project: display
ms.assetid: 813d6aa6-0442-4f30-9fd6-b3aec2e0e11d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_OUT_QUERY_HWCURSOR,
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
req.alt-api: IDARG_OUT_QUERY_HWCURSOR
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

# IDARG_OUT_QUERY_HWCURSOR structure



## -description
<p>
                 Gives information about the coordinates and shape of the current cursor.</p>


## -syntax

````
typedef struct DARG_OUT_QUERY_HWCURSOR {
  BOOL                    IsCursorVisible;
  INT                     X;
  INT                     Y;
  BOOL                    IsCursorShapeUpdated;
  IDDCX_CURSOR_SHAPE_INFO CursorShapeInfo;
} IDARG_OUT_QUERY_HWCURSOR, *IDARG_OUT_QUERY_HWCURSOR;
````


## -struct-fields
<dl>

### -field IsCursorVisible

<dd>
<p>
                      [out] Indicates if the cursor is visible or not.
                 </p>
</dd>

### -field X

<dd>
<p>
                     [out] If the cursor is viable, this is the screen coordinate of the top-left hand pixel in the cursor image.</p>
<div class="alert"><b>Note</b>  NOTE : This can be negative. For example, when there is a hot-spot in the center of cursor it is placed in the top-left of the screen</div>
<div> </div>
</dd>

### -field Y

<dd>
<p>
                     [out] If the cursor is viable, this is the screen coordinate of the top-left hand pixel in the cursor image.</p>
<div class="alert"><b>Note</b>  NOTE : This can be negative. For example, when there is a hot-spot in the center of cursor it is placed in the top-left of the screen</div>
<div> </div>
</dd>

### -field IsCursorShapeUpdated

<dd>
<p>
                     [out] Indicates if the cursor shape has been updated since the last time the driver was called. If it has been updated, the OS updates the <b>CursorShapeInfo</b> structure and copies the new cursor image data into the <a href="..\iddcx\ns-iddcx-idarg-in-query-hwcursor.md">IDARG_IN_QUERY_HWCURSOR</a> buffer <b>pShapeBuffer</b>.
                 </p>
</dd>

### -field CursorShapeInfo

<dd>
<p>
                     [out] If the cursor is visible, then the OS copies the current cursor info into this buffer. If the cursor is not visible, the OS zeros this structure.
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