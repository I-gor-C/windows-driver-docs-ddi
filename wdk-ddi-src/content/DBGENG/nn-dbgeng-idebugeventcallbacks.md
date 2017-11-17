---
UID: NN.dbgeng.IDebugEventCallbacks
title: IDebugEventCallbacks
author: windows-driver-content
description: IDebugEventCallbacks interface
old-location: debugger\idebugeventcallbacks.htm
ms.assetid: f5e51d0e-0967-4e35-b24b-4bd99c975569
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: debugger
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
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
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
<a href="https://msdn.microsoft.com/76b9aca2-4630-45e2-bed4-f701018c86a5">Breakpoint</a>
</td>
<td align="left" width="63%">
<p> This method is called by the engine when the target issues a breakpoint exception.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/157a420a-18ad-46cf-ae93-603e9226ee4f">ChangeDebuggeeState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when it makes or detects changes to the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/42ad993a-b12e-49ff-8a1f-f62e2ab968d3">ChangeEngineState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when its state has changed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/5383bd49-df44-48dd-8385-c782a1b1f80a">ChangeSymbolState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when the symbol state changes.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539321">CreateProcess</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a create-process debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/c3b2cbaa-33b9-4784-922d-d1209fc23dfd">CreateThread</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a create-thread debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/93f915ab-1f9e-453c-b76e-8260eecd7298">Exception</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exception debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/050b747e-5570-4e25-81e4-eccdde4f6995">ExitProcess</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exit-process debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/03ff46cb-dfc5-409a-b652-bef8f2b37b59">ExitThread</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exit-thread debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/165c83cb-c0be-4a09-9220-a5208f660308">GetInterestMask</a>
</td>
<td align="left" width="63%">
<p>This method is called to determine which events the <b>IDebugEventCallbacks</b> object is interested in.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/f4efcbf3-f78a-4e0e-9741-4f9b68814e5b">LoadModule</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a module-load debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/127c4e48-87db-4735-8d3d-e01fed6a9cf0">SessionStatus</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a change occurs in the debugger session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/651f5207-36c8-4d46-8305-950efb2365bf">SystemError</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a system error occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/2afdaee6-7714-42d4-a402-3cb85ef3b970">UnloadModule</a>
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
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff550563">IDebugEventCallbacksWide</a> interface includes Unicode versions of these methods; the Unicode methods share the same names as those used by the methods in <b>IDebugEventCallbacks</b>.

</p>

<p>The following <a href="debugger.events#events#events">events</a> are generated by the target.</p>

<p>DEBUG_EVENT_BREAKPOINT</p>

<p>
<a href="https://msdn.microsoft.com/76b9aca2-4630-45e2-bed4-f701018c86a5">Breakpoint</a>
</p>

<p>A breakpoint exception occurred in the target.</p>

<p>DEBUG_EVENT_EXCEPTION</p>

<p>
<a href="https://msdn.microsoft.com/93f915ab-1f9e-453c-b76e-8260eecd7298">Exception</a>
</p>

<p>An exception debugging event occurred in the target.</p>

<p>DEBUG_EVENT_CREATE_THREAD</p>

<p>
<a href="https://msdn.microsoft.com/c3b2cbaa-33b9-4784-922d-d1209fc23dfd">CreateThread</a>
</p>

<p>A create-thread debugging event occurred in the target.</p>

<p>DEBUG_EVENT_EXIT_THREAD</p>

<p>
<a href="https://msdn.microsoft.com/03ff46cb-dfc5-409a-b652-bef8f2b37b59">ExitThread</a>
</p>

<p>An exit-thread debugging event occurred in the target.</p>

<p>DEBUG_EVENT_CREATE_PROCESS</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539321">CreateProcess</a>
</p>

<p>A create-process debugging event occurred in the target.</p>

<p>DEBUG_EVENT_EXIT_PROCESS</p>

<p>
<a href="https://msdn.microsoft.com/050b747e-5570-4e25-81e4-eccdde4f6995">ExitProcess</a>
</p>

<p>An exit-process debugging event occurred in the target.</p>

<p>DEBUG_EVENT_LOAD_MODULE</p>

<p>
<a href="https://msdn.microsoft.com/f4efcbf3-f78a-4e0e-9741-4f9b68814e5b">LoadModule</a>
</p>

<p>A module-load debugging event occurred in the target.</p>

<p>DEBUG_EVENT_UNLOAD_MODULE</p>

<p>
<a href="https://msdn.microsoft.com/2afdaee6-7714-42d4-a402-3cb85ef3b970">UnloadModule</a>
</p>

<p>A module-unload debugging event occurred in the target.</p>

<p>DEBUG_EVENT_SYSTEM_ERROR</p>

<p>
<a href="https://msdn.microsoft.com/651f5207-36c8-4d46-8305-950efb2365bf">SystemError</a>
</p>

<p>A system error occurred in the target.</p>

<p> </p>

<p>The following events are generated by the debugger engine.</p>

<p>DEBUG_EVENT_SESSION_STATUS</p>

<p>
<a href="https://msdn.microsoft.com/127c4e48-87db-4735-8d3d-e01fed6a9cf0">SessionStatus</a>
</p>

<p>A change has occurred in the session status.</p>

<p>DEBUG_EVENT_CHANGE_DEBUGGEE_STATE</p>

<p>
<a href="https://msdn.microsoft.com/157a420a-18ad-46cf-ae93-603e9226ee4f">ChangeDebuggeeState</a>
</p>

<p>The engine has made or detected a change in the target status.</p>

<p>DEBUG_EVENT_CHANGE_ENGINE_STATE</p>

<p>
<a href="https://msdn.microsoft.com/42ad993a-b12e-49ff-8a1f-f62e2ab968d3">ChangeEngineState</a>
</p>

<p>The engine state has changed.</p>

<p>DEBUG_EVENT_CHANGE_SYMBOL_STATE</p>

<p>
<a href="https://msdn.microsoft.com/5383bd49-df44-48dd-8385-c782a1b1f80a">ChangeSymbolState</a>
</p>

<p>The symbol state has changed.</p>

<p> </p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff550563">IDebugEventCallbacksWide</a> interface includes Unicode versions of these methods; the Unicode methods share the same names as those used by the methods in <b>IDebugEventCallbacks</b>.

</p>

<p>The following <a href="debugger.events#events#events">events</a> are generated by the target.</p>

<p>DEBUG_EVENT_BREAKPOINT</p>

<p>
<a href="https://msdn.microsoft.com/76b9aca2-4630-45e2-bed4-f701018c86a5">Breakpoint</a>
</p>

<p>A breakpoint exception occurred in the target.</p>

<p>DEBUG_EVENT_EXCEPTION</p>

<p>
<a href="https://msdn.microsoft.com/93f915ab-1f9e-453c-b76e-8260eecd7298">Exception</a>
</p>

<p>An exception debugging event occurred in the target.</p>

<p>DEBUG_EVENT_CREATE_THREAD</p>

<p>
<a href="https://msdn.microsoft.com/c3b2cbaa-33b9-4784-922d-d1209fc23dfd">CreateThread</a>
</p>

<p>A create-thread debugging event occurred in the target.</p>

<p>DEBUG_EVENT_EXIT_THREAD</p>

<p>
<a href="https://msdn.microsoft.com/03ff46cb-dfc5-409a-b652-bef8f2b37b59">ExitThread</a>
</p>

<p>An exit-thread debugging event occurred in the target.</p>

<p>DEBUG_EVENT_CREATE_PROCESS</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539321">CreateProcess</a>
</p>

<p>A create-process debugging event occurred in the target.</p>

<p>DEBUG_EVENT_EXIT_PROCESS</p>

<p>
<a href="https://msdn.microsoft.com/050b747e-5570-4e25-81e4-eccdde4f6995">ExitProcess</a>
</p>

<p>An exit-process debugging event occurred in the target.</p>

<p>DEBUG_EVENT_LOAD_MODULE</p>

<p>
<a href="https://msdn.microsoft.com/f4efcbf3-f78a-4e0e-9741-4f9b68814e5b">LoadModule</a>
</p>

<p>A module-load debugging event occurred in the target.</p>

<p>DEBUG_EVENT_UNLOAD_MODULE</p>

<p>
<a href="https://msdn.microsoft.com/2afdaee6-7714-42d4-a402-3cb85ef3b970">UnloadModule</a>
</p>

<p>A module-unload debugging event occurred in the target.</p>

<p>DEBUG_EVENT_SYSTEM_ERROR</p>

<p>
<a href="https://msdn.microsoft.com/651f5207-36c8-4d46-8305-950efb2365bf">SystemError</a>
</p>

<p>A system error occurred in the target.</p>

<p> </p>

<p>The following events are generated by the debugger engine.</p>

<p>DEBUG_EVENT_SESSION_STATUS</p>

<p>
<a href="https://msdn.microsoft.com/127c4e48-87db-4735-8d3d-e01fed6a9cf0">SessionStatus</a>
</p>

<p>A change has occurred in the session status.</p>

<p>DEBUG_EVENT_CHANGE_DEBUGGEE_STATE</p>

<p>
<a href="https://msdn.microsoft.com/157a420a-18ad-46cf-ae93-603e9226ee4f">ChangeDebuggeeState</a>
</p>

<p>The engine has made or detected a change in the target status.</p>

<p>DEBUG_EVENT_CHANGE_ENGINE_STATE</p>

<p>
<a href="https://msdn.microsoft.com/42ad993a-b12e-49ff-8a1f-f62e2ab968d3">ChangeEngineState</a>
</p>

<p>The engine state has changed.</p>

<p>DEBUG_EVENT_CHANGE_SYMBOL_STATE</p>

<p>
<a href="https://msdn.microsoft.com/5383bd49-df44-48dd-8385-c782a1b1f80a">ChangeSymbolState</a>
</p>

<p>The symbol state has changed.</p>

<p> </p>

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