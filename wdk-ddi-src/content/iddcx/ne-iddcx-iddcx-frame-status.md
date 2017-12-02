---
UID: NE.iddcx.IDDCX_FRAME_STATUS
title: IDDCX_FRAME_STATUS
author: windows-driver-content
description: Defines the processing status of the frame.
old-location: display\iddcx_frame_status.htm
old-project: display
ms.assetid: 437050ae-d1b7-48ce-9955-98f1d1b2e15a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: WcsTranslateColors
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_FRAME_STATUS
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
req.iface: 
---

# IDDCX_FRAME_STATUS enumeration



## -description
<p>
                     Defines the processing status of the frame.
                </p>


## -syntax

````
typedef enum _IDDCX_FRAME_STATUS { 
  IDDCX_FRAME_STATUS_UNINITIALIZED  = 0,
  IDDCX_FRAME_STATUS_COMPLETED      = 1,
  IDDCX_FRAME_STATUS_DROPPED        = 2,
  IDDCX_FRAME_STATUS_ERROR          = 3
} IDDCX_FRAME_STATUS;
````


## -enum-fields
<dl>

### -field IDDCX_FRAME_STATUS_UNINITIALIZED

<dd>
<p>
                        
                    Indicates that an <b>IDDCX_FRAME_STATUS</b> variable has not yet been assigned a meaningful value.</p>
</dd>

### -field IDDCX_FRAME_STATUS_COMPLETED

<dd>
<p>
                        Indicates that the frame was processed completely and sent to the device
                    </p>
</dd>

### -field IDDCX_FRAME_STATUS_DROPPED

<dd>
<p>
                        Indicates that the driver stopped processing this frame to start on a newer frame. This normally happens if it is taking a long time to process/transmit the frame
                    </p>
</dd>

### -field IDDCX_FRAME_STATUS_ERROR

<dd>
<p>
                        Indicates that the driver stopped processing this frame because the driver hit an internal error
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