---
UID: NS.dbgeng._DEBUG_SYMBOL_SOURCE_ENTRY
title: DEBUG_SYMBOL_SOURCE_ENTRY
author: windows-driver-content
description: The DEBUG_SYMBOL_SOURCE_ENTRY structure describes a section of the source code and a corresponding region of the target's memory.
old-location: debugger\debug_symbol_source_entry.htm
old-project: debugger
ms.assetid: 595d5a90-6ec8-4841-a38b-c0cbf26ed082
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEBUG_SYMBOL_SOURCE_ENTRY, DEBUG_SYMBOL_SOURCE_ENTRY, *PDEBUG_SYMBOL_SOURCE_ENTRY
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
req.alt-api: DEBUG_SYMBOL_SOURCE_ENTRY
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

# DEBUG_SYMBOL_SOURCE_ENTRY structure



## -description
<p>The DEBUG_SYMBOL_SOURCE_ENTRY structure describes a section of the source code and a corresponding region of the target's memory.</p>


## -syntax

````
typedef struct _DEBUG_SYMBOL_SOURCE_ENTRY {
  ULONG64 ModuleBase;
  ULONG64 Offset;
  ULONG64 FileNameId;
  ULONG64 EngineInternal;
  ULONG   Size;
  ULONG   Flags;
  ULONG   FileNameSize;
  ULONG   StartLine;
  ULONG   EndLine;
  ULONG   StartColumn;
  ULONG   EndColumn;
  ULONG   Reserved;
} DEBUG_SYMBOL_SOURCE_ENTRY, *PDEBUG_SYMBOL_SOURCE_ENTRY;
````


## -struct-fields
<dl>

### -field ModuleBase

<dd>
<p>The base address, in the target's virtual address space, of the module that the source symbol came from.</p>
</dd>

### -field Offset

<dd>
<p>The location of the memory corresponding to the source code in the target's virtual address space.</p>
</dd>

### -field FileNameId

<dd>
<p>Identifier for the source code file name. If this information is not available, <b>FieldNameId</b> is set to zero.</p>
</dd>

### -field EngineInternal

<dd>
<p>Reserved for internal debugger engine use.</p>
</dd>

### -field Size

<dd>
<p>The size of the region of memory corresponding to the source code. If this information is not available, <b>Size</b> is set to one.</p>
</dd>

### -field Flags

<dd>
<p>Set to zero.</p>
</dd>

### -field FileNameSize

<dd>
<p>The number of characters in the source filename, including the terminator. </p>
</dd>

### -field StartLine

<dd>
<p>The line number of the start of the region of source code in the file. The number of the first line in the file is one. If this information is not available, <b>StartLine</b> is set to DEBUG_ANY_ID.</p>
</dd>

### -field EndLine

<dd>
<p>The line number of the end of the region of source code in the file. The number of the first line in the file is one. If this information is not available, <b>StartLine</b> is set to DEBUG_ANY_ID.</p>
</dd>

### -field StartColumn

<dd>
<p>The column number of the start of the region of source code. The number of the first column is one. If this information is not available, <b>StartLine</b> is set to DEBUG_ANY_ID.</p>
</dd>

### -field EndColumn

<dd>
<p>The column number of the end of the region of source code. The number of the first column is one. If this information is not available, <b>StartLine</b> is set to DEBUG_ANY_ID.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for future use.</p>
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
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>