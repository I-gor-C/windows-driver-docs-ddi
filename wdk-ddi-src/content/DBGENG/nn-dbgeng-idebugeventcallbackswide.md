---
UID: NN.dbgeng.IDebugEventCallbacksWide
title: IDebugEventCallbacksWide
author: windows-driver-content
description: IDebugEventCallbacksWide interface
old-location: debugger\idebugeventcallbackswide.htm
ms.assetid: 717fad3a-91b1-41c8-ac71-e9ea52533efd
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
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
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
<a href="https://msdn.microsoft.com/ee9b9b6c-c76e-4979-9f23-c411fe1b002a">Breakpoint</a>
</td>
<td align="left" width="63%">
<p> This method is called by the engine when the target issues a breakpoint exception.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/ffb5925a-6bbd-41f5-b8b8-e8c7189d57ac">ChangeDebuggeeState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when it makes or detects changes to the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/14205476-3f58-4105-99a7-a3baa2eba033">ChangeEngineState</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when its state has changed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/ea331612-5c48-4320-a658-101c3d93e7be">ChangeSymbolState</a>
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
<a href="https://msdn.microsoft.com/d845777c-1bc9-4ab3-9bfc-211f2231971e">CreateThread</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a create-thread debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/02f5bec1-f2d2-4b72-bd9e-b30315c334da">Exception</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exception debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/bc104b84-4f0a-420d-8c2c-14b33cc6ca04">ExitProcess</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exit-process debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/77933fa9-ff30-45cf-894d-83a425802e25">ExitThread</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when an exit-thread debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/b1e62ae3-4a3d-42db-b7fe-87d1a7e0b438">GetInterestMask</a>
</td>
<td align="left" width="63%">
<p>This method is called to determine which events the <b>IDebugEventCallbacksWide</b> object is interested in.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/03a76d41-3af1-48a9-832a-1c255a8b0cc4">LoadModule</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a module-load debugging event occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/cc3ed4ef-5e2d-4865-8d6f-b140d6b5d7af">SessionStatus</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a change occurs in the debugger session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/938eacb5-7939-43ed-a854-046708fc9c79">SystemError</a>
</td>
<td align="left" width="63%">
<p>This method is called by the engine when a system error occurs in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/05f3fa93-389e-4ecc-b7c0-71f43691232f">UnloadModule</a>
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