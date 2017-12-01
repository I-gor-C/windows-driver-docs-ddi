---
UID: NF.dbgeng.IDebugSymbolGroup2.GetSymbolEntryInformation
title: IDebugSymbolGroup2::GetSymbolEntryInformation
author: windows-driver-content
description: The GetSymbolEntryInformation method returns information about a symbol in a symbol group.
old-location: debugger\getsymbolentryinformation2.htm
old-project: debugger
ms.assetid: ee8ea970-04ee-4bf5-9e81-7d5baf0eac0d
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbolGroup2, GetSymbolEntryInformation, IDebugSymbolGroup2::GetSymbolEntryInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbolGroup2.GetSymbolEntryInformation
req.alt-loc: dbgeng.h
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
req.iface: IDebugSymbolGroup2
---

# IDebugSymbolGroup2::GetSymbolEntryInformation method



## -description
<p>The <b>GetSymbolEntryInformation</b> method returns information about a symbol in a symbol group.</p>


## -syntax

````
HRESULT GetSymbolEntryInformation(
  [in]  ULONG               Index,
  [out] PDEBUG_SYMBOL_ENTRY Entry
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>The index of the symbol whose information iyou want.  The index of a symbol is an identification number. The index ranges from zero through the number of symbols in the symbol group minus one.</p>
</dd>

### -param <i>Entry</i> [out]

<dd>
<p>The information about the symbol.  For more information about this structure, see <a href="..\dbgeng\ns-dbgeng--debug-symbol-entry.md">DEBUG_SYMBOL_ENTRY</a>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>For more information about symbol groups, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554702">Scopes and Symbol Groups</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup2.md">IDebugSymbolGroup2</a>
</dt>
<dt>
<a href="..\dbgeng\ns-dbgeng--debug-symbol-entry.md">DEBUG_SYMBOL_ENTRY</a>
</dt>
<dt>
<a href="debugger.getnumbersymbols">GetNumberSymbols</a>
</dt>
<dt>
<a href="debugger.getsymbolentryinformation">IDebugSymbols3::GetSymbolEntryInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup2::GetSymbolEntryInformation method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
