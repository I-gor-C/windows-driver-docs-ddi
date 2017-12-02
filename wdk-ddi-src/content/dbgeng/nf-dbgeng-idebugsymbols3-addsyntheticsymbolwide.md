---
UID: NF.dbgeng.IDebugSymbols3.AddSyntheticSymbolWide
title: IDebugSymbols3::AddSyntheticSymbolWide
author: windows-driver-content
description: The AddSyntheticSymbolWide method adds a synthetic symbol to a module in the current process.
old-location: debugger\addsyntheticsymbolwide.htm
old-project: debugger
ms.assetid: 06d4d1f1-8d28-46cc-8c80-8a67cf4ae4c3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSymbols3, AddSyntheticSymbolWide, IDebugSymbols3::AddSyntheticSymbolWide
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
req.alt-api: IDebugSymbols3.AddSyntheticSymbolWide
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::AddSyntheticSymbolWide method



## -description
<p>The <b>AddSyntheticSymbolWide</b>  method adds a synthetic symbol to a module in the <a href="debugger.c#current_process#current_process"><i>current process</i></a>.</p>


## -syntax

````
HRESULT AddSyntheticSymbolWide(
  [in]            ULONG64              Offset,
  [in]            ULONG                Size,
  [in]            PCSTR                Name,
  [in]            ULONG                Flags,
  [out, optional] PDEBUG_MODULE_AND_ID Id
);
````


## -parameters
<dl>

### -param Offset [in]

<dd>
<p>Specifies the location in the process's virtual address space of the synthetic symbol.</p>
</dd>

### -param Size [in]

<dd>
<p>Specifies the size in bytes of the synthetic symbol.</p>
</dd>

### -param Name [in]

<dd>
<p>Specifies the name of the synthetic symbol.</p>
</dd>

### -param Flags [in]

<dd>
<p>Set to DEBUG_ADDSYNTHSYM_DEFAULT.</p>
</dd>

### -param Id [out, optional]

<dd>
<p>Receives the <a href="..\dbgeng\ns-dbgeng--debug-module-and-id.md">DEBUG_MODULE_AND_ID</a> structure that identifies the synthetic symbol.  If <i>Id</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

## -remarks
<p>The location of the synthetic symbol must not be the same as the location of another symbol.</p>

<p>If the module containing a synthetic symbol is reloaded - for example, by calling <a href="debugger.reload">Reload</a> with the <i>Module</i> parameter set to the name of the module - the synthetic symbol will be discarded.</p>

<p>For more information about synthetic symbols, see <a href="debugger.using_symbols#synthetic_symbols#synthetic_symbols">Synthetic Symbols</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.removesyntheticsymbol">RemoveSyntheticSymbol</a>
</dt>
<dt>
<a href="debugger.addsyntheticmodule">AddSyntheticModule</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::AddSyntheticSymbolWide method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
