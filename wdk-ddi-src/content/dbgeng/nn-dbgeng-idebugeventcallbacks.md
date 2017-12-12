---
UID: NN.dbgeng.IDebugEventCallbacks
title: IDebugEventCallbacks
author: windows-driver-content
description: IDebugEventCallbacks interface
old-location: debugger\idebugeventcallbacks.htm
old-project: debugger
ms.assetid: f5e51d0e-0967-4e35-b24b-4bd99c975569
ms.author: windowsdriverdev
ms.date: 12/8/2017
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
---

# IDebugEventCallbacks interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugEventCallbacks</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugEventCallbacks</b> also has these types of members:

The <b>IDebugEventCallbacks</b> interface has these methods.

 This method is called by the engine when the target issues a breakpoint exception.

This method is called by the engine when it makes or detects changes to the target.

This method is called by the engine when its state has changed.

This method is called by the engine when the symbol state changes.

This method is called by the engine when a create-process debugging event occurs in the target.

This method is called by the engine when a create-thread debugging event occurs in the target.

This method is called by the engine when an exception debugging event occurs in the target.

This method is called by the engine when an exit-process debugging event occurs in the target.

This method is called by the engine when an exit-thread debugging event occurs in the target.

This method is called to determine which events the <b>IDebugEventCallbacks</b> object is interested in.

This method is called by the engine when a module-load debugging event occurs in the target.

This method is called by the engine when a change occurs in the debugger session.

This method is called by the engine when a system error occurs in the target.

This method is called by the engine when a module-unload debugging event occurs in the target.

 


## -members
The <b>IDebugEventCallbacks</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_breakpoint">Breakpoint</a>
</td>
<td align="left" width="63%">
 This method is called by the engine when the target issues a breakpoint exception.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_changedebuggeestate">ChangeDebuggeeState</a>
</td>
<td align="left" width="63%">
This method is called by the engine when it makes or detects changes to the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_changeenginestate">ChangeEngineState</a>
</td>
<td align="left" width="63%">
This method is called by the engine when its state has changed.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_changesymbolstate">ChangeSymbolState</a>
</td>
<td align="left" width="63%">
This method is called by the engine when the symbol state changes.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_createprocess">CreateProcess</a>
</td>
<td align="left" width="63%">
This method is called by the engine when a create-process debugging event occurs in the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_createthread">CreateThread</a>
</td>
<td align="left" width="63%">
This method is called by the engine when a create-thread debugging event occurs in the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_exception">Exception</a>
</td>
<td align="left" width="63%">
This method is called by the engine when an exception debugging event occurs in the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_exitprocess">ExitProcess</a>
</td>
<td align="left" width="63%">
This method is called by the engine when an exit-process debugging event occurs in the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_exitthread">ExitThread</a>
</td>
<td align="left" width="63%">
This method is called by the engine when an exit-thread debugging event occurs in the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_getinterestmask">GetInterestMask</a>
</td>
<td align="left" width="63%">
This method is called to determine which events the <b>IDebugEventCallbacks</b> object is interested in.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_loadmodule">LoadModule</a>
</td>
<td align="left" width="63%">
This method is called by the engine when a module-load debugging event occurs in the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_sessionstatus">SessionStatus</a>
</td>
<td align="left" width="63%">
This method is called by the engine when a change occurs in the debugger session.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_systemerror">SystemError</a>
</td>
<td align="left" width="63%">
This method is called by the engine when a system error occurs in the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugeventcallbacks_unloadmodule">UnloadModule</a>
</td>
<td align="left" width="63%">
This method is called by the engine when a module-unload debugging event occurs in the target.

</td>
</tr>
</table> This method is called by the engine when the target issues a breakpoint exception.

This method is called by the engine when it makes or detects changes to the target.

This method is called by the engine when its state has changed.

This method is called by the engine when the symbol state changes.

This method is called by the engine when a create-process debugging event occurs in the target.

This method is called by the engine when a create-thread debugging event occurs in the target.

This method is called by the engine when an exception debugging event occurs in the target.

This method is called by the engine when an exit-process debugging event occurs in the target.

This method is called by the engine when an exit-thread debugging event occurs in the target.

This method is called to determine which events the <b>IDebugEventCallbacks</b> object is interested in.

This method is called by the engine when a module-load debugging event occurs in the target.

This method is called by the engine when a change occurs in the debugger session.

This method is called by the engine when a system error occurs in the target.

This method is called by the engine when a module-unload debugging event occurs in the target.

 


## -remarks
The <a href="..\dbgeng\nn-dbgeng-idebugeventcallbackswide.md">IDebugEventCallbacksWide</a> interface includes Unicode versions of these methods; the Unicode methods share the same names as those used by the methods in <b>IDebugEventCallbacks</b>.



The following <a href="debugger.events#events#events">events</a> are generated by the target.

DEBUG_EVENT_BREAKPOINT


<a href="debugger.idebugeventcallbacks_breakpoint">Breakpoint</a>


A breakpoint exception occurred in the target.

DEBUG_EVENT_EXCEPTION


<a href="debugger.idebugeventcallbacks_exception">Exception</a>


An exception debugging event occurred in the target.

DEBUG_EVENT_CREATE_THREAD


<a href="debugger.idebugeventcallbacks_createthread">CreateThread</a>


A create-thread debugging event occurred in the target.

DEBUG_EVENT_EXIT_THREAD


<a href="debugger.idebugeventcallbacks_exitthread">ExitThread</a>


An exit-thread debugging event occurred in the target.

DEBUG_EVENT_CREATE_PROCESS


<a href="debugger.idebugeventcallbacks_createprocess">CreateProcess</a>


A create-process debugging event occurred in the target.

DEBUG_EVENT_EXIT_PROCESS


<a href="debugger.idebugeventcallbacks_exitprocess">ExitProcess</a>


An exit-process debugging event occurred in the target.

DEBUG_EVENT_LOAD_MODULE


<a href="debugger.idebugeventcallbacks_loadmodule">LoadModule</a>


A module-load debugging event occurred in the target.

DEBUG_EVENT_UNLOAD_MODULE


<a href="debugger.idebugeventcallbacks_unloadmodule">UnloadModule</a>


A module-unload debugging event occurred in the target.

DEBUG_EVENT_SYSTEM_ERROR


<a href="debugger.idebugeventcallbacks_systemerror">SystemError</a>


A system error occurred in the target.

The following events are generated by the debugger engine.

DEBUG_EVENT_SESSION_STATUS


<a href="debugger.idebugeventcallbacks_sessionstatus">SessionStatus</a>


A change has occurred in the session status.

DEBUG_EVENT_CHANGE_DEBUGGEE_STATE


<a href="debugger.idebugeventcallbacks_changedebuggeestate">ChangeDebuggeeState</a>


The engine has made or detected a change in the target status.

DEBUG_EVENT_CHANGE_ENGINE_STATE


<a href="debugger.idebugeventcallbacks_changeenginestate">ChangeEngineState</a>


The engine state has changed.

DEBUG_EVENT_CHANGE_SYMBOL_STATE


<a href="debugger.idebugeventcallbacks_changesymbolstate">ChangeSymbolState</a>


The symbol state has changed.


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