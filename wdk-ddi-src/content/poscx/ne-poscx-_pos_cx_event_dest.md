---
UID: NE:poscx._POS_CX_EVENT_DEST
title: "_POS_CX_EVENT_DEST"
author: windows-driver-content
description: The POS_CX_EVENT_DEST defines which applications receive this event.
old-location: pos\pos_cx_event_dest.htm
old-project: pos
ms.assetid: 63D16B9E-82CC-4171-B80A-D0FA6F2066E2
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: POS_CX_EVENT_DEST, POS_CX_EVENT_DEST enumeration, POS_CX_EVENT_DEST_ALL, POS_CX_EVENT_DEST_DEVICE_OWNER, POS_CX_EVENT_DEST_INVALID, _POS_CX_EVENT_DEST, pos.pos_cx_event_dest, poscx/POS_CX_EVENT_DEST, poscx/POS_CX_EVENT_DEST_ALL, poscx/POS_CX_EVENT_DEST_DEVICE_OWNER, poscx/POS_CX_EVENT_DEST_INVALID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	poscx.h
api_name:
-	POS_CX_EVENT_DEST
product: Windows
targetos: Windows
req.typenames: POS_CX_EVENT_DEST
req.product: Windows 10 or later.
---

# _POS_CX_EVENT_DEST Enumeration
The POS_CX_EVENT_DEST defines which applications receive this event.

## Syntax
```
typedef enum _POS_CX_EVENT_DEST {
  POS_CX_EVENT_DEST_INVALID       ,
  POS_CX_EVENT_DEST_DEVICE_OWNER  ,
  POS_CX_EVENT_DEST_ALL           ,
  POS_CX_EVENT_DEST__MAX
} POS_CX_EVENT_DEST;
```

## Constants

<table>
            
                <tr>
                    <td>POS_CX_EVENT_DEST_INVALID</td>
                    <td>Specifies that no devices will receive this event.  This value should not be used.</td>
                </tr>
            
                <tr>
                    <td>POS_CX_EVENT_DEST_DEVICE_OWNER</td>
                    <td>Specifies that only the current claim owner will receive this event.</td>
                </tr>
            
                <tr>
                    <td>POS_CX_EVENT_DEST_ALL</td>
                    <td>Specifies that the event will be broadcast to all client handles.</td>
                </tr>
            
                <tr>
                    <td>POS_CX_EVENT_DEST__MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | poscx.h (include Poscx.h) |