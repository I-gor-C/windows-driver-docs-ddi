---
UID: NS.iddcx.IDDCX_CURSOR_SHAPE_INFO
title: IDDCX_CURSOR_SHAPE_INFO
author: windows-driver-content
description: Gives information about the shape of the cursor.
old-location: display\iddcx_cursor_shape_info.htm
old-project: display
ms.assetid: 58ed8f04-616f-4eea-b6e1-07f322c37dbb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_CURSOR_SHAPE_INFO,
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
req.alt-api: IDDCX_CURSOR_SHAPE_INFO
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

# IDDCX_CURSOR_SHAPE_INFO structure



## -description
<p>Gives information about the shape of the cursor.</p>


## -syntax

````
typedef struct IDDCX_CURSOR_SHAPE_INFO {
  UINT                    Size;
  UINT                    ShapeId;
  IDDCX_CURSOR_SHAPE_TYPE CursorType;
  UINT                    Width;
  UINT                    Height;
  UINT                    Pitch;
  UINT                    XHot;
  UINT                    YHot;
} IDDCX_CURSOR_SHAPE_INFO, *IDDCX_CURSOR_SHAPE_INFO;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>
                     Total size of the structure.
                 </p>
</dd>

### -field ShapeId

<dd>
<p>
                     Unique id for the current cursor image. This is incremented each time a cursor image is set, even if that image has been set before. The id is used to check if the current cursor image the driver has cached has changed and cannot be used in any way to allow caching for animated cursor sequences.
                 </p>
</dd>

### -field CursorType

<dd>
<p>
                     Indicates the type of cursor data written to the cursor shape buffer.
                 </p>
</dd>

### -field Width

<dd>
<p>
                     Width in pixels of the cursor shape written to the shape buffer.
                 </p>
</dd>

### -field Height

<dd>
<p>
                     Height in pixels of the cursor shape written to the shape buffer.
                 </p>
</dd>

### -field Pitch

<dd>
<p>
                     Pitch in bytes of the cursor shape written to the shape buffer.
                 </p>
</dd>

### -field XHot

<dd>
<p>
                     X position of the cursor hotspot relative to the top-left of the cursor.
                 </p>
</dd>

### -field YHot

<dd>
<p>
                     Y position of the cursor hotspot relative to the top-left of the cursor.
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