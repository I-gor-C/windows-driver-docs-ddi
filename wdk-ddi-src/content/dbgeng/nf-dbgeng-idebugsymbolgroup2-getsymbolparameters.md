---
UID: NF.dbgeng.IDebugSymbolGroup2.GetSymbolParameters
title: IDebugSymbolGroup2::GetSymbolParameters
author: windows-driver-content
description: The GetSymbolParameters method returns the symbol parameters that describe the specified symbols in a symbol group.
old-location: debugger\getsymbolparameters.htm
old-project: debugger
ms.assetid: e6390a7c-bbe1-47d7-9411-d710c4ab58a8
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbolGroup2, GetSymbolParameters, IDebugSymbolGroup2::GetSymbolParameters
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
req.alt-api: IDebugSymbolGroup.GetSymbolParameters,IDebugSymbolGroup2.GetSymbolParameters
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

# IDebugSymbolGroup2::GetSymbolParameters method



## -description
<p>The <b>GetSymbolParameters</b> method returns the symbol parameters that describe the specified <a href="debugger.symbols#symbols#symbols">symbols</a> in a symbol group.</p>


## -syntax

````
HRESULT GetSymbolParameters(
  [in]  ULONG                    Start,
  [in]  ULONG                    Count,
  [out] PDEBUG_SYMBOL_PARAMETERS Params
);
````


## -parameters
<dl>

### -param <i>Start</i> [in]

<dd>
<p>The index in the symbol group of the first symbol whose parameters you want.  The index of a symbol is an identification number. This number ranges from zero through the number of symbols in the symbol group minus one.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>The number of symbol parameters that you want.</p>
</dd>

### -param <i>Params</i> [out]

<dd>
<p>The symbol parameters.  This array must hold at least <i>Count</i> elements.  For a description of these parameters, see <a href="..\dbgeng\ns-dbgeng--debug-symbol-parameters.md">DEBUG_SYMBOL_PARAMETERS</a>.</p>
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
<a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup.md">IDebugSymbolGroup</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup2.md">IDebugSymbolGroup2</a>
</dt>
<dt>
<a href="..\dbgeng\ns-dbgeng--debug-symbol-parameters.md">DEBUG_SYMBOL_PARAMETERS</a>
</dt>
<dt>
<a href="debugger.getnumbersymbols">GetNumberSymbols</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup::GetSymbolParameters method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
