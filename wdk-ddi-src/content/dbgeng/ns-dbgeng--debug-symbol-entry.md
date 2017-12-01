---
UID: NS.dbgeng._DEBUG_SYMBOL_ENTRY
title: DEBUG_SYMBOL_ENTRY
author: windows-driver-content
description: The DEBUG_SYMBOL_ENTRY structure describes a symbol in a symbol group.
old-location: debugger\debug_symbol_entry.htm
old-project: debugger
ms.assetid: 31ffab25-ec34-42ff-bdde-c98fef003bfc
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: DEBUG_SYMBOL_ENTRY, DEBUG_SYMBOL_ENTRY, *PDEBUG_SYMBOL_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h, DbgHelp.h, DbgHelp.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_SYMBOL_ENTRY
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

# DEBUG_SYMBOL_ENTRY structure



## -description
<p>The DEBUG_SYMBOL_ENTRY structure describes a symbol in a symbol group.</p>


## -syntax

````
typedef struct _DEBUG_SYMBOL_ENTRY {
  ULONG64 ModuleBase;
  ULONG64 Offset;
  ULONG64 Id;
  ULONG64 Arg64;
  ULONG   Size;
  ULONG   Flags;
  ULONG   TypeId;
  ULONG   NameSize;
  ULONG   Token;
  ULONG   Tag;
  ULONG   Arg32;
  ULONG   Reserved;
}  DEBUG_SYMBOL_ENTRY, *PDEBUG_SYMBOL_ENTRY;
````


## -struct-fields
<dl>

### -field <b>ModuleBase</b>

<dd>
<p>The base address of the module in the target's virtual address space.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>The location of the symbol in the target's virtual address space.</p>
</dd>

### -field <b>Id</b>

<dd>
<p>The symbol ID of the symbol.  If the symbol ID is not known, <b>Id</b> is DEBUG_INVALID_OFFSET.</p>
</dd>

### -field <b>Arg64</b>

<dd>
<p>The interpretation of <b>Arg64</b> depends on the type of the symbol.  If the value is not known, <b>Arg64</b> is zero.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of the symbol's value.  This might not be known or might not completely represent all of the data for a symbol.  For example, a function's code might be split among multiple regions and the size only describes one region.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Symbol entry flags.  Currently, no flags are defined.</p>
</dd>

### -field <b>TypeId</b>

<dd>
<p>The type ID of the symbol.</p>
</dd>

### -field <b>NameSize</b>

<dd>
<p>The size, in characters, of the symbol's name.  If the size is not known, <b>NameSize</b> is zero.</p>
</dd>

### -field <b>Token</b>

<dd>
<p>The managed token of the symbol.  If the token value is not known or the symbol does not have a token, <b>Token</b> is zero.</p>
</dd>

### -field <b>Tag</b>

<dd>
<p>The symbol tag for the type of the symbol.  This is a value from the <b>SymTagEnum</b> enumeration.</p>
</dd>

### -field <b>Arg32</b>

<dd>
<p>The interpretation of <b>Arg32</b> depends on the type of the symbol.  Currently, the value of <b>Arg32</b> is the register that holds the value or a pointer to the value of the symbol. If the symbol is not held in a register, or the register is not known, <b>Arg32</b> is zero.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Set to zero.</p>
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
<dt>DbgEng.h (include DbgEng.h, DbgHelp.h, or DbgHelp.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="debugger.getsymbolentryinformation2">IdebugSymbolGroup2::GetSymbolEntryInformation</a>
</dt>
<dt>
<a href="debugger.getsymbolentryinformation">IdebugSymbols3::GetSymbolEntryInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20DEBUG_SYMBOL_ENTRY structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
