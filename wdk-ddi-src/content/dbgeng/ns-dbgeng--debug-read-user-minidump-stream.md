---
UID: NS.dbgeng._DEBUG_READ_USER_MINIDUMP_STREAM
title: DEBUG_READ_USER_MINIDUMP_STREAM
author: windows-driver-content
description: Describes a user minidump to read.
old-location: debugger\debug_read_user_minidump_stream.htm
old-project: debugger
ms.assetid: 07005D52-E851-4AE8-95D8-ED8E26C43DC6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEBUG_READ_USER_MINIDUMP_STREAM, DEBUG_READ_USER_MINIDUMP_STREAM, *PDEBUG_READ_USER_MINIDUMP_STREAM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_READ_USER_MINIDUMP_STREAM
req.alt-loc: DbgEng.h
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
req.iface: IDebugSystemObjects4
---

# DEBUG_READ_USER_MINIDUMP_STREAM structure



## -description
<p>Describes a user minidump to read.</p>


## -syntax

````
typedef struct _DEBUG_READ_USER_MINIDUMP_STREAM {
  ULONG   StreamType;
  ULONG   Flags;
  ULONG64 Offset;
  PVOID   Buffer;
  ULONG   BufferSize;
  ULONG   BufferUsed;
} DEBUG_READ_USER_MINIDUMP_STREAM, *PDEBUG_READ_USER_MINIDUMP_STREAM;
````


## -struct-fields
<dl>

### -field <b>StreamType</b>

<dd>
<p>The type of stream.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>The offset of stream.</p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>Specifies the beginning of the buffer to read.</p>
</dd>

### -field <b>BufferSize</b>

<dd>
<p>Specifies the length of the buffer to read.</p>
</dd>

### -field <b>BufferUsed</b>

<dd>
<p>The buffer used value.</p>
</dd>
</dl>

## -remarks
<p>The DEBUG_REQUEST_READ_USER_MINIDUMP_STREAM <a href="https://msdn.microsoft.com/library/windows/hardware/ff554564">Request</a> operation reads a stream from a user-mode minidump target.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>