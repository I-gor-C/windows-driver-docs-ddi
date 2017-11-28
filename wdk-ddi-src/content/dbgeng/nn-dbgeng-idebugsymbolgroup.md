---
UID: NN.dbgeng.IDebugSymbolGroup
title: IDebugSymbolGroup
author: windows-driver-content
description: IDebugSymbolGroup interface
old-location: debugger\idebugsymbolgroup.htm
old-project: debugger
ms.assetid: dd629e4a-938e-4db6-b0f3-6dd12a431486
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbolGroup
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
req.iface: IDebugSystemObjects4
---

# IDebugSymbolGroup interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSymbolGroup</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugSymbolGroup</b> also has these types of members:</p>

<p>The <b>IDebugSymbolGroup</b> interface has these methods.</p>

<p>Adds a symbol to a symbol group.</p>

<p>Adds or removes the children of a symbol from a symbol group.</p>

<p> Returns the number of symbols that are contained in a symbol group.
</p>

<p>Returns the name of a symbol in a symbol group.
</p>

<p>Returns the symbol parameters that describe the specified symbols in a symbol group.
</p>

<p>Changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. 
</p>

<p>Prints the specified symbols to the debugger console.</p>

<p>Removes the specified symbol from a symbol group.
</p>

<p> Removes the specified symbol from a symbol group.
</p>

<p>Sets the value of the specified symbol.
</p>

<p> </p>

## -members
<p>The <b>IDebugSymbolGroup</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537925">AddSymbol</a>
</td>
<td align="left" width="63%">
<p>Adds a symbol to a symbol group.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543271">ExpandSymbol</a>
</td>
<td align="left" width="63%">
<p>Adds or removes the children of a symbol from a symbol group.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547975">GetNumberSymbols</a>
</td>
<td align="left" width="63%">
<p> Returns the number of symbols that are contained in a symbol group.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549121">GetSymbolName</a>
</td>
<td align="left" width="63%">
<p>Returns the name of a symbol in a symbol group.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549146">GetSymbolParameters</a>
</td>
<td align="left" width="63%">
<p>Returns the symbol parameters that describe the specified symbols in a symbol group.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553191">OutputAsType</a>
</td>
<td align="left" width="63%">
<p>Changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. 
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553264">OutputSymbols</a>
</td>
<td align="left" width="63%">
<p>Prints the specified symbols to the debugger console.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554510">RemoveSymbolByIndex</a>
</td>
<td align="left" width="63%">
<p>Removes the specified symbol from a symbol group.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554518">RemoveSymbolByName</a>
</td>
<td align="left" width="63%">
<p> Removes the specified symbol from a symbol group.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561457">WriteSymbol</a>
</td>
<td align="left" width="63%">
<p>Sets the value of the specified symbol.
</p>
</td>
</tr>
</table><p>Adds a symbol to a symbol group.</p>

<p>Adds or removes the children of a symbol from a symbol group.</p>

<p> Returns the number of symbols that are contained in a symbol group.
</p>

<p>Returns the name of a symbol in a symbol group.
</p>

<p>Returns the symbol parameters that describe the specified symbols in a symbol group.
</p>

<p>Changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. 
</p>

<p>Prints the specified symbols to the debugger console.</p>

<p>Removes the specified symbol from a symbol group.
</p>

<p> Removes the specified symbol from a symbol group.
</p>

<p>Sets the value of the specified symbol.
</p>

<p> </p>

## -remarks


## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550846">IDebugSymbolGroup2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
