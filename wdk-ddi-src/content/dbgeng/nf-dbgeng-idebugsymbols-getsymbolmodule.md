---
UID: NF.dbgeng.IDebugSymbols.GetSymbolModule
title: IDebugSymbols::GetSymbolModule
author: windows-driver-content
description: The GetSymbolModule method returns the base address of module which contains the specified symbol.
old-location: debugger\getsymbolmodule.htm
old-project: debugger
ms.assetid: f3774204-86c3-467b-96ba-739f19d300e3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols, GetSymbolModule, IDebugSymbols::GetSymbolModule
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
req.alt-api: IDebugSymbols.GetSymbolModule,IDebugSymbols2.GetSymbolModule,IDebugSymbols3.GetSymbolModule
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
req.iface: IDebugSymbols
---

# IDebugSymbols::GetSymbolModule method



## -description
<p>The <b>GetSymbolModule</b> method returns the base address of module which contains the specified symbol.</p>


## -syntax

````
HRESULT GetSymbolModule(
  [in]  PCSTR    Symbol,
  [out] PULONG64 Base
);
````


## -parameters
<dl>

### -param <i>Symbol</i> [in]

<dd>
<p>Specifies the name of the symbol to look up.  See the Remarks section for details of the syntax of this name.</p>
</dd>

### -param <i>Base</i> [out]

<dd>
<p>Receives the location in the target's memory address space of the base of the module.  For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552231">Modules</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The symbol or module could not be found.</p>

<p> </p>

## -remarks
<p>The string <i>Symbol</i> must contain an exclamation point ( <b>!</b> ).  If <i>Symbol</i> is a module-qualified symbol name (for example, <b>mymodules!main</b>) or if the module name is omitted (for example, <b>!main</b>), the engine will search for this symbol and return the module in which it is found.  If <i>Symbol</i> contains just a module name (for example, <b>mymodule!</b>) the engine returns the first module with this module name.</p>

<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

<p>The string <i>Symbol</i> must contain an exclamation point ( <b>!</b> ).  If <i>Symbol</i> is a module-qualified symbol name (for example, <b>mymodules!main</b>) or if the module name is omitted (for example, <b>!main</b>), the engine will search for this symbol and return the module in which it is found.  If <i>Symbol</i> contains just a module name (for example, <b>mymodule!</b>) the engine returns the first module with this module name.</p>

<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

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