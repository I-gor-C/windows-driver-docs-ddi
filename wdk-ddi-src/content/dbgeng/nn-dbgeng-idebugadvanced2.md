---
UID: NN.dbgeng.IDebugAdvanced2
title: IDebugAdvanced2
author: windows-driver-content
description: IDebugAdvanced2 interface
old-location: debugger\idebugadvanced2.htm
old-project: debugger
ms.assetid: 9b5f73db-1fb8-4e07-8053-67cb5020505e
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
req.alt-api: IDebugAdvanced2
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

# IDebugAdvanced2 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugAdvanced2</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugadvanced.md">IDebugAdvanced</a>. <b>IDebugAdvanced2</b> also has these types of members:

The <b>IDebugAdvanced2</b> interface has these methods.

Returns the filename of a source file on the source path or return the value of a variable associated with a file token.

Returns specified information about a source file.

Returns specified information about a symbol.

Returns information about operating system objects on the target.

Performs a variety of different operations.

 

## -members
The <b>IDebugAdvanced2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.findsourcefileandtoken">FindSourceFileAndToken</a>
</td>
<td align="left" width="63%">
Returns the filename of a source file on the source path or return the value of a variable associated with a file token.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcefileinformation">GetSourceFileInformation</a>
</td>
<td align="left" width="63%">
Returns specified information about a source file.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolinformation">GetSymbolInformation</a>
</td>
<td align="left" width="63%">
Returns specified information about a symbol.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsystemobjectinformation">GetSystemObjectInformation</a>
</td>
<td align="left" width="63%">
Returns information about operating system objects on the target.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.request">Request</a>
</td>
<td align="left" width="63%">
Performs a variety of different operations.
</td>
</tr>
</table>Returns the filename of a source file on the source path or return the value of a variable associated with a file token.

Returns specified information about a source file.

Returns specified information about a symbol.

Returns information about operating system objects on the target.

Performs a variety of different operations.

 

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
<a href="..\dbgeng\nn-dbgeng-idebugadvanced.md">IDebugAdvanced</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugadvanced3.md">IDebugAdvanced3</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugAdvanced2 interface%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
