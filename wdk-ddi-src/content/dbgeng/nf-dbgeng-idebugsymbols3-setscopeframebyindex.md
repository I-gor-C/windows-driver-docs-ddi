---
UID: NF.dbgeng.IDebugSymbols3.SetScopeFrameByIndex
title: IDebugSymbols3::SetScopeFrameByIndex
author: windows-driver-content
description: The SetScopeFrameByIndex method sets the current scope to the scope of one of the frames on the call stack.
old-location: debugger\setscopeframebyindex.htm
old-project: debugger
ms.assetid: 7d5105e3-99c6-4800-88a4-af80a61c253e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSymbols3, SetScopeFrameByIndex, IDebugSymbols3::SetScopeFrameByIndex
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols3.SetScopeFrameByIndex
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::SetScopeFrameByIndex method



## -description
<p>The <b>SetScopeFrameByIndex</b> method sets the current scope to the scope of one of the frames on the call stack.</p>


## -syntax

````
HRESULT SetScopeFrameByIndex(
  [in] ULONG Index
);
````


## -parameters
<dl>

### -param Index [in]

<dd>
<p>Specifies the index of the stack frame from which to set the scope.  The index counts the number of frames from the top of the call stack.  The frame at the top of the stack, representing the current call, has index zero.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>When an event occurs and the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> breaks into a target, the scope is set to the current function call (the function that was executing when the event occurred).  Calling this method with <i>Index</i> set to one will change the current scope to the caller of the current function; with <i>Index</i> set to two, the scope is changed to the caller's caller, and so on.</p>

<p>For more information about scopes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554702">Scopes and Symbol Groups</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563155">.frame (Set Local Context)</a>
</dt>
<dt>
<a href="debugger.getcurrentscopeframeindex">GetCurrentScopeFrameIndex</a>
</dt>
<dt>
<a href="debugger.setscopefromstoredevent">SetScopeFromStoredEvent</a>
</dt>
<dt>
<a href="debugger.setscope">SetScope</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::SetScopeFrameByIndex method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
