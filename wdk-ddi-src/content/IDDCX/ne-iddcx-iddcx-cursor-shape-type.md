---
UID: NE.iddcx.IDDCX_CURSOR_SHAPE_TYPE
title: IDDCX_CURSOR_SHAPE_TYPE
author: windows-driver-content
description: Describes the type of cursor.
old-location: display\iddcx_cursor_shape_type.htm
ms.assetid: 8aced7c9-e1be-4ec0-8b59-77cee011a71e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_CURSOR_SHAPE_TYPE
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
req.irql: _requires_same_
ms.keywords: WcsTranslateColors
req.iface: 
---

# IDDCX_CURSOR_SHAPE_TYPE enumeration



## -description
<p>
                    Describes the type of cursor.
                </p>


## -syntax

````
typedef enum _IDDCX_CURSOR_SHAPE_TYPE { 
  IDDCX_CURSOR_SHAPE_TYPE_UNINITIALIZED  = 0,
  IDDCX_CURSOR_SHAPE_TYPE_MASKED_COLOR   = 1,
  IDDCX_CURSOR_SHAPE_TYPE_ALPHA          = 2
} IDDCX_CURSOR_SHAPE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="IDDCX_CURSOR_SHAPE_TYPE_UNINITIALIZED"></a><a id="iddcx_cursor_shape_type_uninitialized"></a><b>IDDCX_CURSOR_SHAPE_TYPE_UNINITIALIZED</b>

<dd>
<p>
                        
                    Indicates that the cursor shape is uninitialized</p>
</dd>

### -field <a id="IDDCX_CURSOR_SHAPE_TYPE_MASKED_COLOR"></a><a id="iddcx_cursor_shape_type_masked_color"></a><b>IDDCX_CURSOR_SHAPE_TYPE_MASKED_COLOR</b>

<dd>
<p>
                        Indicates this is a masked-color cursor shape
                    </p>
</dd>

### -field <a id="IDDCX_CURSOR_SHAPE_TYPE_ALPHA"></a><a id="iddcx_cursor_shape_type_alpha"></a><b>IDDCX_CURSOR_SHAPE_TYPE_ALPHA</b>

<dd>
<p>
                        Indicates this is a 32bpp alpha cursor
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