---
UID: NF.dbgeng.IDebugSymbolGroup2.ExpandSymbol
title: IDebugSymbolGroup2::ExpandSymbol
author: windows-driver-content
description: The ExpandSymbol method adds or removes the children of a symbol from a symbol group.
old-location: debugger\expandsymbol.htm
old-project: debugger
ms.assetid: 314fdeea-10be-4cb3-8bd7-9b1b4b12e534
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbolGroup2, ExpandSymbol, IDebugSymbolGroup2::ExpandSymbol
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
req.alt-api: IDebugSymbolGroup.ExpandSymbol,IDebugSymbolGroup2.ExpandSymbol
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

# IDebugSymbolGroup2::ExpandSymbol method



## -description
<p>The <b>ExpandSymbol</b> method adds or removes the children of a symbol from a symbol group.</p>


## -syntax

````
HRESULT ExpandSymbol(
  [in] ULONG Index,
  [in] BOOL  Expand
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>The index of the symbol whose children will be added or removed.  The index of a symbol is an identification number. The index ranges from zero through the number of symbols in the symbol group minus one.</p>
</dd>

### -param <i>Expand</i> [in]

<dd>
<p>A Boolean value that specifies whether to add or remove the symbols children from the symbol group.  If <i>Expand</i> is true, the children are added.  If <i>Expand</i> is false, the children are removed.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The symbol has no children to add.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The depth of the symbol is DEBUG_SYMBOL_EXPANSION_LEVEL_MASK,  which is the maximum depth. This depth prevented the specified symbol's children from being added to this symbol group.</p>

<p> </p>

<p>This method can also return other error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>For more information about symbol groups, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554702">Scopes and Symbol Groups</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550838">IDebugSymbolGroup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550846">IDebugSymbolGroup2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547975">GetNumberSymbols</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup::ExpandSymbol method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
