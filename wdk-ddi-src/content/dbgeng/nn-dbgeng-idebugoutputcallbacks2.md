---
UID: NN.dbgeng.IDebugOutputCallbacks2
title: IDebugOutputCallbacks2
author: windows-driver-content
description: The IDebugOutputCallbacks2 interface allows clients to receive full debugger markup language (DML) content for presentation.
old-location: debugger\idebugoutputcallbacks2.htm
old-project: debugger
ms.assetid: D35D8960-AD9F-4493-B6CD-3E3049CC3BBD
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
req.alt-api: IDebugOutputCallbacks2
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

# IDebugOutputCallbacks2 interface



## -description
<p>The <b>IDebugOutputCallbacks2</b> interface allows clients to receive full  debugger markup language (DML) content for presentation. </p>
<p>This interface extends the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550801">IDebugOutputCallbacks</a> interface, not the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550804">IDebugOutputCallbacksWide</a> interface. Therefore, it can be passed in to the existing <a href="https://msdn.microsoft.com/library/windows/hardware/ff556751">SetOutputCallbacks</a> method. </p>
<p>The engine performs a <b>QueryInterface</b> for <b>IDebugOutputCallbacks2</b> to see which interface the incoming output callback object supports. If the object supports <b>IDebugOutputCallbacks2</b>, all output will be sent through the extended <b>IDebugOutputCallbacks2</b> methods.</p>
<p>An output object can register for both text and DML content, if it can handle them both. During output processing of the callback the engine will pick the format that reduces conversions, thus supporting both may reduce conversions in the engine. It is not necessary, though, and supporting only one format is the expected mode of operation.</p>
<p>The basic <a href="https://msdn.microsoft.com/library/windows/hardware/ff550815">IDebugOutputCallbacks::Output</a> method is not used. </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugOutputCallbacks2</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugOutputCallbacks2</b> also has these types of members:</p>

<p>The <b>IDebugOutputCallbacks2</b> interface has these methods.</p>

<p>Allows the callback object to describe which kinds of output notifications it wants to receive. </p>

<p>This method is not used.</p>

<p>Returns notifications for the <b>IDebugOutputCallbacks2</b> interface.</p>

<p> </p>

## -members
<p>The <b>IDebugOutputCallbacks2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugoutputcallbacks2_getinterestmask">GetInterestMask</a>
</td>
<td align="left" width="63%">
<p>Allows the callback object to describe which kinds of output notifications it wants to receive. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553183">Output</a>
</td>
<td align="left" width="63%">
<p>This method is not used.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugoutputcallbacks2_output2">Output2</a>
</td>
<td align="left" width="63%">
<p>Returns notifications for the <b>IDebugOutputCallbacks2</b> interface.</p>
</td>
</tr>
</table><p>Allows the callback object to describe which kinds of output notifications it wants to receive. </p>

<p>This method is not used.</p>

<p>Returns notifications for the <b>IDebugOutputCallbacks2</b> interface.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550801">IDebugOutputCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550804">IDebugOutputCallbacksWide</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556751">SetOutputCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugOutputCallbacks2 interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
