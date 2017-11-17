---
UID: NS.dbgeng._INLINE_FRAME_CONTEXT
title: INLINE_FRAME_CONTEXT
author: windows-driver-content
description: Describes inline frame context.
old-location: debugger\inline_frame_context.htm
ms.assetid: 6EB52227-8685-4096-882F-64550A84DE4F
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: INLINE_FRAME_CONTEXT
req.alt-loc: Dbgeng.h
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
ms.keywords: INLINE_FRAME_CONTEXT, INLINE_FRAME_CONTEXT
req.iface: IDebugSystemObjects4
---

# INLINE_FRAME_CONTEXT structure



## -description
<p>Describes inline frame context. </p>


## -syntax

````
typedef union _INLINE_FRAME_CONTEXT {
  DWORD  ContextValue;
  struct  {
        BYTE FrameId;
        BYTE FrameType;
        WORD FrameSignature;
    };
} INLINE_FRAME_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>ContextValue</b>

<dd>
<p>A context value. </p>
</dd>

### -field <b>{
        BYTE FrameId;
        BYTE FrameType;
        WORD FrameSignature;
    }</b>

<dd>
<p>A structure that contains frame context information.  </p>
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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>