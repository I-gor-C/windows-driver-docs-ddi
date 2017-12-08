---
UID: NF.dbgeng.IDebugSymbols2.GetOffsetByName
title: IDebugSymbols2::GetOffsetByName
author: windows-driver-content
description: The GetOffsetByName method returns the location of a symbol identified by name.
old-location: debugger\getoffsetbyname.htm
old-project: debugger
ms.assetid: b6915215-3654-446b-b30d-b891f439a379
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSymbols2, GetOffsetByName, IDebugSymbols2::GetOffsetByName
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
req.alt-api: IDebugSymbols.GetOffsetByName,IDebugSymbols2.GetOffsetByName,IDebugSymbols3.GetOffsetByName
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
req.iface: IDebugSymbols2
---

# IDebugSymbols2::GetOffsetByName method



## -description
<p>The <b>GetOffsetByName</b>  method returns the location of a symbol identified by name.</p>


## -syntax

````
HRESULT GetOffsetByName(
  [in]  PCSTR    Symbol,
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param Symbol [in]

<dd>
<p>Specifies the name of the symbol to locate.  The name may be qualified by a module name (for example, <b>mymodule!main</b>).</p>
</dd>

### -param Offset [out]

<dd>
<p>Receives the location in the target's memory address space of the base of the symbol's memory allocation.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, the name <i>Symbol</i> was not unique and multiple symbols with that name were found.  One of these symbols was arbitrarily chosen and returned.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>No symbol could be found with the specified name.</p>

<p> </p>

## -remarks
<p>If the name <i>Symbol</i> is not unique and <b>GetOffsetByName</b> finds multiple symbols with that name, then the ambiguity will be resolved arbitrarily.  In this case the value S_FALSE will be returned.  <a href="debugger.startsymbolmatch">StartSymbolMatch</a> can be used to initiate a search to determine which is the desired result.</p>

<p><b>GetNameByOffset</b> does not support pattern matching (e.g. wildcards).  To find a symbol using pattern matching use <b>StartSymbolMatch</b>.</p>

<p>If the module name for the symbol is known, it is best to qualify the symbol name with the module name.  Otherwise the engine will search the symbols for all modules until it finds a match; this can take a long time if it has to load the symbol files for a lot of modules.  If the symbol name is qualified with a module name, the engine only searches the symbols for that module.  </p>

<p>For more information about symbols and symbol names, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols.md">IDebugSymbols</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getnamebyoffset">GetNameByOffset</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols::GetOffsetByName method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
