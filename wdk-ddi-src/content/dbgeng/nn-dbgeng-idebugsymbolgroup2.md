---
UID: NN.dbgeng.IDebugSymbolGroup2
title: IDebugSymbolGroup2
author: windows-driver-content
description: IDebugSymbolGroup2 interface
old-location: debugger\idebugsymbolgroup2.htm
old-project: debugger
ms.assetid: d702fe69-966c-4b9a-aa0e-b8376288cb79
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: DebugCreateEx
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
req.alt-api: IDebugSymbolGroup2
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
---

# IDebugSymbolGroup2 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSymbolGroup2</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup.md">IDebugSymbolGroup</a>. <b>IDebugSymbolGroup2</b> also has these types of members:

The <b>IDebugSymbolGroup2</b> interface has these methods.

Adds a symbol to a symbol group.


Returns information about a symbol in a symbol group.

Returns the name of a symbol in a symbol group.


Retrieves the location in the process's virtual address space of a symbol in a symbol group, if the symbol has an absolute address.

Returns the register that contains the value or a pointer to the value of a symbol in a symbol group.


Returns the size of a symbol's value.

Returns the name of the specified symbol's type.
(ANSI version)

Returns the name of the specified symbol's type.
(Unicode version)

Returns a string that represents the value of a symbol.
(ANSI version)

Returns a string that represents the value of a symbol.
(Unicode version)

Changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type.

Removes the specified symbol from a symbol group.


Sets the value of the specified symbol.

 

## -members
The <b>IDebugSymbolGroup2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsymbolwide">AddSymbolWide</a>
</td>
<td align="left" width="63%">
Adds a symbol to a symbol group.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentryinformation">GetSymbolEntryInformation</a>
</td>
<td align="left" width="63%">
Returns information about a symbol in a symbol group.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolnamewide">GetSymbolNameWide</a>
</td>
<td align="left" width="63%">
Returns the name of a symbol in a symbol group.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymboloffset">GetSymbolOffset</a>
</td>
<td align="left" width="63%">
Retrieves the location in the process's virtual address space of a symbol in a symbol group, if the symbol has an absolute address.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolregister">GetSymbolRegister</a>
</td>
<td align="left" width="63%">
Returns the register that contains the value or a pointer to the value of a symbol in a symbol group.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolsize">GetSymbolSize</a>
</td>
<td align="left" width="63%">
Returns the size of a symbol's value.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymboltypename">GetSymbolTypeName</a>
</td>
<td align="left" width="63%">
Returns the name of the specified symbol's type.
(ANSI version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymboltypenamewide">GetSymbolTypeNameWide</a>
</td>
<td align="left" width="63%">
Returns the name of the specified symbol's type.
(Unicode version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolvaluetext">GetSymbolValueText</a>
</td>
<td align="left" width="63%">
Returns a string that represents the value of a symbol.
(ANSI version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolvaluetextwide">GetSymbolValueTextWide</a>
</td>
<td align="left" width="63%">
Returns a string that represents the value of a symbol.
(Unicode version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputastypewide">OutputAsTypeWide</a>
</td>
<td align="left" width="63%">
Changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removesymbolbynamewide">RemoveSymbolByNameWide</a>
</td>
<td align="left" width="63%">
Removes the specified symbol from a symbol group.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writesymbolwide">WriteSymbolWide</a>
</td>
<td align="left" width="63%">
Sets the value of the specified symbol.
</td>
</tr>
</table>Adds a symbol to a symbol group.


Returns information about a symbol in a symbol group.

Returns the name of a symbol in a symbol group.


Retrieves the location in the process's virtual address space of a symbol in a symbol group, if the symbol has an absolute address.

Returns the register that contains the value or a pointer to the value of a symbol in a symbol group.


Returns the size of a symbol's value.

Returns the name of the specified symbol's type.
(ANSI version)

Returns the name of the specified symbol's type.
(Unicode version)

Returns a string that represents the value of a symbol.
(ANSI version)

Returns a string that represents the value of a symbol.
(Unicode version)

Changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type.

Removes the specified symbol from a symbol group.


Sets the value of the specified symbol.

 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
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
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup2 interface%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
