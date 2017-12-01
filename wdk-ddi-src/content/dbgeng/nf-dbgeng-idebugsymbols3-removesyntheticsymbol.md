---
UID: NF.dbgeng.IDebugSymbols3.RemoveSyntheticSymbol
title: IDebugSymbols3::RemoveSyntheticSymbol
author: windows-driver-content
description: The RemoveSyntheticSymbol method removes a synthetic symbol from a module in the current process.
old-location: debugger\removesyntheticsymbol.htm
old-project: debugger
ms.assetid: 07825be3-84a1-4aab-a9f0-22a45f636a04
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols3, RemoveSyntheticSymbol, IDebugSymbols3::RemoveSyntheticSymbol
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
req.alt-api: IDebugSymbols3.RemoveSyntheticSymbol
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::RemoveSyntheticSymbol method



## -description
<p>The <b>RemoveSyntheticSymbol</b> method removes a synthetic symbol from a module in the current process.</p>


## -syntax

````
HRESULT RemoveSyntheticSymbol(
  [in] PDEBUG_MODULE_AND_ID Id
);
````


## -parameters
<dl>

### -param <i>Id</i> [in]

<dd>
<p>Specifies the synthetic symbol to remove.  This must be the same value returned in the <i>Id</i> parameter of <a href="debugger.addsyntheticsymbol">AddSyntheticSymbol</a>.  See <a href="..\dbgeng\ns-dbgeng--debug-module-and-id.md">DEBUG_MODULE_AND_ID</a> for details about the type of this parameter.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>No synthetic symbol was found at the specified location.  This is returned if a synthetic symbol at this location was previously removed or discarded.</p>

<p> </p>

<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>If the module containing a synthetic symbol is reloaded - for example, by calling <a href="debugger.reload">Reload</a> with the <i>Module</i> parameter set to the name of the module - the synthetic symbol will be discarded.</p>

<p>For more information about synthetic symbols, see Synthetic Symbols.</p>

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
<a href="debugger.addsyntheticsymbol">AddSyntheticSymbol</a>
</dt>
<dt>
<a href="debugger.removesyntheticmodule">RemoveSyntheticModule</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::RemoveSyntheticSymbol method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
