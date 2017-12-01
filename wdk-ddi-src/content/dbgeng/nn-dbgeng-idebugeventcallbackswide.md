---
UID: NN.dbgeng.IDebugEventCallbacksWide
title: IDebugEventCallbacksWide
author: windows-driver-content
description: IDebugEventCallbacksWide interface
old-location: debugger\idebugeventcallbackswide.htm
old-project: debugger
ms.assetid: 717fad3a-91b1-41c8-ac71-e9ea52533efd
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
req.alt-api: IDebugEventCallbacksWide
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

# IDebugEventCallbacksWide interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugEventCallbacksWide</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugEventCallbacksWide</b> also has these types of members:</p>

<p>The <b>IDebugEventCallbacksWide</b> interface has these methods.</p>

<p> This method is called by the engine when the target issues a breakpoint exception.</p>

<p>This method is called by the engine when it makes or detects changes to the target.</p>

<p>This method is called by the engine when its state has changed.</p>

<p>This method is called by the engine when the symbol state changes.</p>

<p>This method is called by the engine when a create-process debugging event occurs in the target.</p>

<p>This method is called by the engine when a create-thread debugging event occurs in the target.</p>

<p>This method is called by the engine when an exception debugging event occurs in the target.</p>

<p>This method is called by the engine when an exit-process debugging event occurs in the target.</p>

<p>This method is called by the engine when an exit-thread debugging event occurs in the target.</p>

<p>This method is called to determine which events the <b>IDebugEventCallbacksWide</b> object is interested in.</p>

<p>This method is called by the engine when a module-load debugging event occurs in the target.</p>

<p>This method is called by the engine when a change occurs in the debugger session.</p>

<p>This method is called by the engine when a system error occurs in the target.</p>

<p>This method is called by the engine when a module-unload debugging event occurs in the target.</p>

<p> </p>

## -members
<p>The <b>IDebugEventCallbacksWide</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_breakpoint">Breakpoint</a>
</td>
<td align="left" width="63%">
<p> This method is called by the engine when the target issues a breakpoint exception.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_changedebuggeestate">ChangeDebuggeeState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when it makes or detects changes to the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_changeenginestate">ChangeEngineState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when its state has changed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_changesymbolstate">ChangeSymbolState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when the symbol state changes.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_createprocess">CreateProcess</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a create-process debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_createthread">CreateThread</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a create-thread debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_exception">Exception</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exception debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_exitprocess">ExitProcess</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exit-process debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_exitthread">ExitThread</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exit-thread debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_getinterestmask">GetInterestMask</a>
</td>
<td align="left" width="63%">
<p>This method is called to determine which events the <b>IDebugEventCallbacksWide</b> object is interested in.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_loadmodule">LoadModule</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a module-load debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_sessionstatus">SessionStatus</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a change occurs in the debugger session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_systemerror">SystemError</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a system error occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbackswide_unloadmodule">UnloadModule</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a module-unload debugging event occurs in the target.</p>
</td>
</tr>
</table><p> This method is called by the engine when the target issues a breakpoint exception.</p>

<p>This method is called by the engine when it makes or detects changes to the target.</p>

<p>This method is called by the engine when its state has changed.</p>

<p>This method is called by the engine when the symbol state changes.</p>

<p>This method is called by the engine when a create-process debugging event occurs in the target.</p>

<p>This method is called by the engine when a create-thread debugging event occurs in the target.</p>

<p>This method is called by the engine when an exception debugging event occurs in the target.</p>

<p>This method is called by the engine when an exit-process debugging event occurs in the target.</p>

<p>This method is called by the engine when an exit-thread debugging event occurs in the target.</p>

<p>This method is called to determine which events the <b>IDebugEventCallbacksWide</b> object is interested in.</p>

<p>This method is called by the engine when a module-load debugging event occurs in the target.</p>

<p>This method is called by the engine when a change occurs in the debugger session.</p>

<p>This method is called by the engine when a system error occurs in the target.</p>

<p>This method is called by the engine when a module-unload debugging event occurs in the target.</p>

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