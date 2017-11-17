---
UID: NS.dispmprt._DXGK_DISPLAY_OWNERSHIP_FLAGS
title: DXGK_DISPLAY_OWNERSHIP_FLAGS
author: windows-driver-content
description: Structure filled in by OS upon successful completion of the DxgkCbAcquirePostDisplayOwnership2 callback to provide information about the display state a driver is inheriting.
old-location: display\dxgk_display_ownership_flags.htm
ms.assetid: F5CA04FD-5E2A-4C68-97CF-F3D425A958AA
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DISPLAY_OWNERSHIP_FLAGS
req.alt-loc: dispmprt.h
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
ms.keywords: DXGK_DISPLAY_OWNERSHIP_FLAGS, DXGK_DISPLAY_OWNERSHIP_FLAGS, *PDXGK_DISPLAY_OWNERSHIP_FLAGS
req.iface: 
---

# DXGK_DISPLAY_OWNERSHIP_FLAGS structure



## -description
<p>Structure filled in by OS upon successful completion of the DxgkCbAcquirePostDisplayOwnership2 callback to provide information about the display state a driver is inheriting.</p>


## -syntax

````
typedef struct _DXGK_DISPLAY_OWNERSHIP_FLAGS {
  union {
    struct {
      DXGK_FRAMEBUFFER_STATE FrameBufferState  :4;
    };
    UINT Value;
  };
} DXGK_DISPLAY_OWNERSHIP_FLAGS, *PDXGK_DISPLAY_OWNERSHIP_FLAGS;
````


## -struct-fields
<dl>

### -field <b>FrameBufferState</b>

<dd>
<p>Value indicating the state of the frame buffer.  See definition of DXGK_FRAMEBUFFER_STATE enum for details.  </p>
</dd>

### -field <b>Value</b>

<dd>
<p>The value used to operate over the combined bitfields.</p>
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
<dt>Dispmprt.h</dt>
</dl>
</td>
</tr>
</table>