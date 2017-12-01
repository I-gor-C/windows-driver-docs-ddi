---
UID: NF.dbgeng.IDebugSymbolGroup.OutputAsType
title: IDebugSymbolGroup::OutputAsType
author: windows-driver-content
description: The OutputAsType method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type.
old-location: debugger\outputastype.htm
old-project: debugger
ms.assetid: ab8c19c8-73c0-4c70-9a5d-9cf9d182157d
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbolGroup, OutputAsType, IDebugSymbolGroup::OutputAsType
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
req.alt-api: IDebugSymbolGroup.OutputAsType,IDebugSymbolGroup2.OutputAsType
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
req.iface: IDebugSymbolGroup
---

# IDebugSymbolGroup::OutputAsType method



## -description
<p>The <b>OutputAsType</b>  method changes the type of a symbol in a symbol group.  The symbol's entry is updated to represent the new type. </p>


## -syntax

````
HRESULT OutputAsType(
  [in] ULONG Index,
  [in] PCSTR Type
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>The index of the entry in this symbol group.  The <i>index</i> of a symbol is an identification number. The index ranges from zero through the number of symbols in the symbol group minus one.</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>The name of the type of the symbol that you want.  If the name begins with an exclamation mark (<b>!</b>), the name is treated as an extension.  For more information about how to use an extension as a type, see the Remarks section.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>Because the children of the new entry type might differ from the children of the old entry type, the <b>OutputAsType</b> method removes all of the children of the entry from the symbol group.  You can add the children back by using the <a href="debugger.expandsymbol">ExpandSymbol</a> method.</p>

<p>If <i>Type</i> is an extension, the address of the symbol is passed to the extension.  Every line of output from the extension becomes a child symbol of the specified symbol.  These child symbols are text and you cannot manipulate them in any way.  For example, if the name of a variable is <b>@$teb</b>, you can change its type to <b>!teb</b>.</p>

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
<a href="debugger.expandsymbol">ExpandSymbol</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup::OutputAsType method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
