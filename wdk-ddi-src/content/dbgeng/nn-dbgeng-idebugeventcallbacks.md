---
UID: NN.dbgeng.IDebugEventCallbacks
title: IDebugEventCallbacks
author: windows-driver-content
description: IDebugEventCallbacks interface
old-location: debugger\idebugeventcallbacks.htm
old-project: debugger
ms.assetid: f5e51d0e-0967-4e35-b24b-4bd99c975569
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
req.alt-api: IDebugEventCallbacks
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

# IDebugEventCallbacks interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugEventCallbacks</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugEventCallbacks</b> also has these types of members:</p>

<p>The <b>IDebugEventCallbacks</b> interface has these methods.</p>

<p> This method is called by the engine when the target issues a breakpoint exception.</p>

<p>This method is called by the engine when it makes or detects changes to the target.</p>

<p>This method is called by the engine when its state has changed.</p>

<p>This method is called by the engine when the symbol state changes.</p>

<p>This method is called by the engine when a create-process debugging event occurs in the target.</p>

<p>This method is called by the engine when a create-thread debugging event occurs in the target.</p>

<p>This method is called by the engine when an exception debugging event occurs in the target.</p>

<p>This method is called by the engine when an exit-process debugging event occurs in the target.</p>

<p>This method is called by the engine when an exit-thread debugging event occurs in the target.</p>

<p>This method is called to determine which events the <b>IDebugEventCallbacks</b> object is interested in.</p>

<p>This method is called by the engine when a module-load debugging event occurs in the target.</p>

<p>This method is called by the engine when a change occurs in the debugger session.</p>

<p>This method is called by the engine when a system error occurs in the target.</p>

<p>This method is called by the engine when a module-unload debugging event occurs in the target.</p>

<p> </p>

## -members
<p>The <b>IDebugEventCallbacks</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_breakpoint">Breakpoint</a>
</td>
<td align="left" width="63%">
<p> This method is called by the engine when the target issues a breakpoint exception.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_changedebuggeestate">ChangeDebuggeeState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when it makes or detects changes to the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_changeenginestate">ChangeEngineState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when its state has changed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_changesymbolstate">ChangeSymbolState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when the symbol state changes.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_createprocess">CreateProcess</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a create-process debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_createthread">CreateThread</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a create-thread debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_exception">Exception</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exception debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_exitprocess">ExitProcess</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exit-process debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_exitthread">ExitThread</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exit-thread debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_getinterestmask">GetInterestMask</a>
</td>
<td align="left" width="63%">
<p>This method is called to determine which events the <b>IDebugEventCallbacks</b> object is interested in.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_loadmodule">LoadModule</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a module-load debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_sessionstatus">SessionStatus</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a change occurs in the debugger session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_systemerror">SystemError</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a system error occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_unloadmodule">UnloadModule</a>
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

<p>This method is called to determine which events the <b>IDebugEventCallbacks</b> object is interested in.</p>

<p>This method is called by the engine when a module-load debugging event occurs in the target.</p>

<p>This method is called by the engine when a change occurs in the debugger session.</p>

<p>This method is called by the engine when a system error occurs in the target.</p>

<p>This method is called by the engine when a module-unload debugging event occurs in the target.</p>

<p> </p>

## -remarks
<p>The <a href="..\dbgeng\nn-dbgeng-idebugeventcallbackswide.md">IDebugEventCallbacksWide</a> interface includes Unicode versions of these methods; the Unicode methods share the same names as those used by the methods in <b>IDebugEventCallbacks</b>.

</p>

<p>The following <a href="debugger.events#events#events">events</a> are generated by the target.</p>

<p>DEBUG_EVENT_BREAKPOINT</p>

<p>
<a href="debugger.idebugeventcallbacks_breakpoint">Breakpoint</a>
</p>

<p>A breakpoint exception occurred in the target.</p>

<p>DEBUG_EVENT_EXCEPTION</p>

<p>
<a href="debugger.idebugeventcallbacks_exception">Exception</a>
</p>

<p>An exception debugging event occurred in the target.</p>

<p>DEBUG_EVENT_CREATE_THREAD</p>

<p>
<a href="debugger.idebugeventcallbacks_createthread">CreateThread</a>
</p>

<p>A create-thread debugging event occurred in the target.</p>

<p>DEBUG_EVENT_EXIT_THREAD</p>

<p>
<a href="debugger.idebugeventcallbacks_exitthread">ExitThread</a>
</p>

<p>An exit-thread debugging event occurred in the target.</p>

<p>DEBUG_EVENT_CREATE_PROCESS</p>

<p>
<a href="debugger.idebugeventcallbacks_createprocess">CreateProcess</a>
</p>

<p>A create-process debugging event occurred in the target.</p>

<p>DEBUG_EVENT_EXIT_PROCESS</p>

<p>
<a href="debugger.idebugeventcallbacks_exitprocess">ExitProcess</a>
</p>

<p>An exit-process debugging event occurred in the target.</p>

<p>DEBUG_EVENT_LOAD_MODULE</p>

<p>
<a href="debugger.idebugeventcallbacks_loadmodule">LoadModule</a>
</p>

<p>A module-load debugging event occurred in the target.</p>

<p>DEBUG_EVENT_UNLOAD_MODULE</p>

<p>
<a href="debugger.idebugeventcallbacks_unloadmodule">UnloadModule</a>
</p>

<p>A module-unload debugging event occurred in the target.</p>

<p>DEBUG_EVENT_SYSTEM_ERROR</p>

<p>
<a href="debugger.idebugeventcallbacks_systemerror">SystemError</a>
</p>

<p>A system error occurred in the target.</p>

<p>The following events are generated by the debugger engine.</p>

<p>DEBUG_EVENT_SESSION_STATUS</p>

<p>
<a href="debugger.idebugeventcallbacks_sessionstatus">SessionStatus</a>
</p>

<p>A change has occurred in the session status.</p>

<p>DEBUG_EVENT_CHANGE_DEBUGGEE_STATE</p>

<p>
<a href="debugger.idebugeventcallbacks_changedebuggeestate">ChangeDebuggeeState</a>
</p>

<p>The engine has made or detected a change in the target status.</p>

<p>DEBUG_EVENT_CHANGE_ENGINE_STATE</p>

<p>
<a href="debugger.idebugeventcallbacks_changeenginestate">ChangeEngineState</a>
</p>

<p>The engine state has changed.</p>

<p>DEBUG_EVENT_CHANGE_SYMBOL_STATE</p>

<p>
<a href="debugger.idebugeventcallbacks_changesymbolstate">ChangeSymbolState</a>
</p>

<p>The symbol state has changed.</p>

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