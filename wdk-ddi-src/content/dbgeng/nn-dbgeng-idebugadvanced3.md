---
UID: NN.dbgeng.IDebugAdvanced3
title: IDebugAdvanced3
author: windows-driver-content
description: IDebugAdvanced3 interface
old-location: debugger\idebugadvanced3.htm
old-project: debugger
ms.assetid: f0226d35-f7a9-4220-be91-afb6d0debd36
ms.author: windowsdriverdev
ms.date: 11/27/2017
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
req.alt-api: IDebugAdvanced3
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

# IDebugAdvanced3 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugAdvanced3</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugadvanced2.md">IDebugAdvanced2</a>. <b>IDebugAdvanced3</b> also has these types of members:</p>

<p>The <b>IDebugAdvanced3</b> interface has these methods.</p>

<p>Returns the filename of a source file on the source path or return the value of a variable associated with a file token.</p>

<p>Returns specified information about a source file.</p>

<p>Returns specified information about a symbol.</p>

<p> </p>

## -members
<p>The <b>IDebugAdvanced3</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.findsourcefileandtokenwide">FindSourceFileAndTokenWide</a>
</td>
<td align="left" width="63%">
<p>Returns the filename of a source file on the source path or return the value of a variable associated with a file token.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcefileinformationwide">GetSourceFileInformationWide</a>
</td>
<td align="left" width="63%">
<p>Returns specified information about a source file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolinformationwide">GetSymbolInformationWide</a>
</td>
<td align="left" width="63%">
<p>Returns specified information about a symbol.</p>
</td>
</tr>
</table><p>Returns the filename of a source file on the source path or return the value of a variable associated with a file token.</p>

<p>Returns specified information about a source file.</p>

<p>Returns specified information about a symbol.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugadvanced2.md">IDebugAdvanced2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugAdvanced3 interface%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
