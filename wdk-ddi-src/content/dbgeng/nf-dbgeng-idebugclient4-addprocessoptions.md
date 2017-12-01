---
UID: NF.dbgeng.IDebugClient4.AddProcessOptions
title: IDebugClient4::AddProcessOptions
author: windows-driver-content
description: The AddProcessOptions method adds the process options to those options that affect the current process.
old-location: debugger\addprocessoptions.htm
old-project: debugger
ms.assetid: eb5f1d91-cfad-48e6-b578-64b64034222f
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient4, AddProcessOptions, IDebugClient4::AddProcessOptions
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
req.alt-api: IDebugClient.AddProcessOptions,IDebugClient2.AddProcessOptions,IDebugClient3.AddProcessOptions,IDebugClient4.AddProcessOptions,IDebugClient5.AddProcessOptions
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
req.iface: IDebugClient4
---

# IDebugClient4::AddProcessOptions method



## -description
<p>The <b>AddProcessOptions</b> method adds the process options to those options that affect the <a href="debugger.c#current_process#current_process"><i>current process</i></a>.</p>


## -syntax

````
HRESULT AddProcessOptions(
  [in] ULONG Options
);
````


## -parameters
<dl>

### -param <i>Options</i> [in]

<dd>
<p>Specifies the process options to add to those affecting the current process.  For details on these process options, see <a href="debugger.debug_process_xxx">DEBUG_PROCESS_XXX</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>This method is available only in <a href="debugger.l#live_user_mode_debugging#live_user_mode_debugging"><i>live user-mode debugging</i></a>.</p>

<p>Some of the process options are global options, others are specific to the current process.</p>

<p>If any process options are modified, the engine will notify the <a href="debugger.e#event_callbacks#event_callbacks"><i>event callbacks</i></a> by calling their <a href="debugger.idebugeventcallbacks_changeenginestate">IDebugEventCallbacks::ChangeEngineState</a> method with the DEBUG_CES_PROCESS_OPTIONS flag set.</p>

<p>For more information about creating and attaching to live user-mode targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552020">Live User-Mode Targets</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient.md">IDebugClient</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient2.md">IDebugClient2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="debugger.getprocessoptions">GetProcessOptions</a>
</dt>
<dt>
<a href="debugger.setprocessoptions">SetProcessOptions</a>
</dt>
<dt>
<a href="debugger.removeprocessoptions">RemoveProcessOptions</a>
</dt>
<dt>
<a href="debugger.debug_process_xxx">DEBUG_PROCESS_XXX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::AddProcessOptions method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
