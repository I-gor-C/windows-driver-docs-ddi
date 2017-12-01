---
UID: NF.dbgeng.IDebugSymbolGroup2.AddSymbol
title: IDebugSymbolGroup2::AddSymbol
author: windows-driver-content
description: The AddSymbol method adds a symbol to a symbol group.
old-location: debugger\addsymbol.htm
old-project: debugger
ms.assetid: b77de459-b5ac-4752-89eb-f24fdde36134
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbolGroup2, AddSymbol, IDebugSymbolGroup2::AddSymbol
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
req.alt-api: IDebugSymbolGroup.AddSymbol,IDebugSymbolGroup2.AddSymbol
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
req.iface: IDebugSymbolGroup2
---

# IDebugSymbolGroup2::AddSymbol method



## -description
<p>The <b>AddSymbol</b>  method adds a symbol to a <a href="debugger.s#symbol_group#symbol_group"><i>symbol group</i></a>.</p>


## -syntax

````
HRESULT AddSymbol(
  [in]      PCSTR  Name,
  [in, out] PULONG Index
);
````


## -parameters
<dl>

### -param <i>Name</i> [in]

<dd>
<p>The symbol's name.  <i>Name</i> is examined as an expression to determine the symbol's <a href="debugger.t#type#type"><i>type</i></a>.  This expression can include pointer, array, and structure dereferencing (for example, <b>*my_pointer</b>, <b>my_array[1]</b>, or <b>my_struct.some_field</b>).</p>
</dd>

### -param <i>Index</i> [in, out]

<dd>
<p>The index of the entry in the symbol group.  When you are calling <b>AddSymbol</b> or <a href="debugger.addsymbolwide">AddSymbolWide</a>, <i>Index</i> should point to the index of the symbol that you want. Or, if <i>Index</i> points to DEBUG_ANY_ID, the symbol is appended to the end of the list.   </p>
<p>When this method returns, <i>Index</i> points to the actual index of the symbol.  The index of a symbol is an identification number. The index ranges from zero through the number of symbols in the symbol group minus one.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>The symbol name in <i>Name</i> is evaluated by the <a href="https://msdn.microsoft.com/e5d3ac7f-fd79-48bb-b927-9ad72570dcbe">C++ expression evaluator</a> and can contain any C++ expression (for example, <b>x+y</b>).</p>

<p>If the index that you want is less than the size of the symbol group, the new symbol is added at the desired index.  If the desired index is larger than the size of the symbol group, the new symbol is added to the end of the list (as in the case of DEBUG_ANY_ID).</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup.md">IDebugSymbolGroup</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup2.md">IDebugSymbolGroup2</a>
</dt>
<dt>
<a href="debugger.getnumbersymbols">GetNumberSymbols</a>
</dt>
<dt>
<a href="debugger.removesymbolbyindex">RemoveSymbolByIndex</a>
</dt>
<dt>
<a href="debugger.removesymbolbyname">RemoveSymbolByName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup::AddSymbol method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
