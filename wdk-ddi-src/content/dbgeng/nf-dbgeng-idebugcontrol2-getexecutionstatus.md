---
UID: NF.dbgeng.IDebugControl2.GetExecutionStatus
title: IDebugControl2::GetExecutionStatus
author: windows-driver-content
description: The GetExecutionStatus method returns information about the execution status of the debugger engine.
old-location: debugger\getexecutionstatus.htm
old-project: debugger
ms.assetid: 58352577-9ed9-4fc6-9cc7-dabcf4f77ad9
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, GetExecutionStatus, IDebugControl2::GetExecutionStatus
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
req.alt-api: IDebugControl.GetExecutionStatus,IDebugControl2.GetExecutionStatus,IDebugControl3.GetExecutionStatus
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
req.iface: IDebugControl2
---

# IDebugControl2::GetExecutionStatus method



## -description
<p>The <b>GetExecutionStatus</b> method returns information about the execution status of the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.</p>


## -syntax

````
HRESULT GetExecutionStatus(
  [out] PULONG Status
);
````


## -parameters
<dl>

### -param <i>Status</i> [out]

<dd>
<p>Receives the execution status.  This will be set to one of the values in the following table. Note that the description of these values differs slightly from the description in <a href="debugger.debug_status_xxx">DEBUG_STATUS_XXX</a>.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_STATUS_NO_DEBUGGEE</p>
</td>
<td>
<p>The engine is not attached to a target.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STATUS_STEP_OVER</p>
</td>
<td>
<p>The target is currently executing a single instruction.  If that instruction is a subroutine call, the entire call will be executed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STATUS_STEP_INTO</p>
</td>
<td>
<p>The target is currently executing a single instruction.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STATUS_STEP_BRANCH</p>
</td>
<td>
<p>The target is currently running until it encounters a branch instruction.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STATUS_GO</p>
</td>
<td>
<p>The target is currently running normally.  It will continue normal execution until an event occurs.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_STATUS_BREAK</p>
</td>
<td>
<p>The target is not running.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.setexecutionstatus">SetExecutionStatus</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetExecutionStatus method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
