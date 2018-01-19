---
UID : NE:poscx._POS_CX_EVENT_PRIORITY
title : _POS_CX_EVENT_PRIORITY
author : windows-driver-content
description : The POS_CX_EVENT_PRIORITY defines the importance of the event and the order it will be delivered to the client application.
old-location : pos\pos_cx_event_priority.htm
old-project : pos
ms.assetid : 835DC1E4-2D49-4D43-A545-5D4288412EC6
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _POS_CX_EVENT_PRIORITY, POS_CX_EVENT_PRIORITY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : poscx.h
req.include-header : Poscx.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : POS_CX_EVENT_PRIORITY
req.alt-loc : poscx.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : POS_CX_EVENT_PRIORITY
req.product : Windows 10 or later.
---

# _POS_CX_EVENT_PRIORITY Enumeration
The POS_CX_EVENT_PRIORITY defines the importance of the event and the order it will be delivered to the client application.

## Syntax
````
typedef enum _POS_CX_EVENT_PRIORITY { 
  POS_CX_EVENT_PRIORITY_INVALID  = 0,
  POS_CX_EVENT_PRIORITY_DATA     = 1,
  POS_CX_EVENT_PRIORITY_CONTROL  = 2
} POS_CX_EVENT_PRIORITY;
````

## Constants

<table>

<tr>
<td>POS_CX_EVENT_PRIORITY_CONTROL</td>
<td>Control level priority delivered in FIFO.</td>
</tr>

<tr>
<td>POS_CX_EVENT_PRIORITY_DATA</td>
<td>Data level priority delivered in FIFO.</td>
</tr>

<tr>
<td>POS_CX_EVENT_PRIORITY_INVALID</td>
<td>Invalid priority. This value should not be used.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | poscx.h (include Poscx.h) |