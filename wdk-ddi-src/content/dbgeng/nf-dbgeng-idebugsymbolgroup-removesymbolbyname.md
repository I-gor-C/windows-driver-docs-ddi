---
UID: NF.dbgeng.IDebugSymbolGroup.RemoveSymbolByName
title: IDebugSymbolGroup::RemoveSymbolByName
author: windows-driver-content
description: The RemoveSymbolByName method removes the specified symbol from a symbol group.
old-location: debugger\removesymbolbyname.htm
old-project: debugger
ms.assetid: 2b03f010-cc3c-48a1-b86c-df470a832c94
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbolGroup, RemoveSymbolByName, IDebugSymbolGroup::RemoveSymbolByName
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
req.alt-api: IDebugSymbolGroup.RemoveSymbolByName,IDebugSymbolGroup2.RemoveSymbolByName
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

# IDebugSymbolGroup::RemoveSymbolByName method



## -description
<p>The <b>RemoveSymbolByName</b>  method removes the specified symbol from a symbol group.</p>


## -syntax

````
HRESULT RemoveSymbolByName(
  [in] PCSTR Name
);
````


## -parameters
<dl>

### -param <i>Name</i> [in]

<dd>
<p>The name of the symbol to remove from the symbol group.</p>
</dd>
</dl>

## -returns
<p><b>RemoveSymbolByName</b> might return one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>When a symbol is removed, the indexes of the symbols that remain in the symbol group might change.</p>

<p>For more information about symbol groups, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554702">Scopes and Symbol Groups</a>.</p>

<p>When a symbol is removed, the indexes of the symbols that remain in the symbol group might change.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537925">AddSymbol</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549121">GetSymbolName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554510">RemoveSymbolByIndex</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup::RemoveSymbolByName method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
