---
UID: NF.dbgeng.IDebugEventCallbacks.ChangeEngineState
title: IDebugEventCallbacks::ChangeEngineState
author: windows-driver-content
description: The ChangeEngineState callback method is called by the engine when its state has changed.
old-location: debugger\idebugeventcallbacks_changeenginestate.htm
old-project: debugger
ms.assetid: 42ad993a-b12e-49ff-8a1f-f62e2ab968d3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugEventCallbacks, ChangeEngineState, IDebugEventCallbacks::ChangeEngineState
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
req.alt-api: IDebugEventCallbacks.ChangeEngineState
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
req.iface: IDebugEventCallbacks
---

# IDebugEventCallbacks::ChangeEngineState method



## -description
<p>The <b>ChangeEngineState</b> callback method is called by the engine when its state has changed.</p>


## -syntax

````
HRESULT ChangeEngineState(
  [in] ULONG   Flags,
  [in] ULONG64 Argument
);
````


## -parameters
<dl>

### -param Flags [in]

<dd>
<p>Specifies a bit-set indicating the type of changes that occurred in the engine's state.  The following bit flags might be set:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_CES_CURRENT_THREAD</p>
</td>
<td>
<p>The current thread has changed, which implies that the current target and current process might also have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_EFFECTIVE_PROCESSOR</p>
</td>
<td>
<p>The effective processor has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_BREAKPOINTS</p>
</td>
<td>
<p>One or more <a href="debugger.multiprocessor_syntax#breakpoints#breakpoints">breakpoints</a> have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_CODE_LEVEL</p>
</td>
<td>
<p>The code interpretation level has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_EXECUTION_STATUS</p>
</td>
<td>
<p>The execution status has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_ENGINE_OPTIONS</p>
</td>
<td>
<p>The engine options have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_LOG_FILE</p>
</td>
<td>
<p>The log file has been opened or closed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_RADIX</p>
</td>
<td>
<p>The default radix has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_EVENT_FILTERS</p>
</td>
<td>
<p>The event filters have changed.  </p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_PROCESS_OPTIONS</p>
</td>
<td>
<p>The process options for the current process have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_EXTENSIONS</p>
</td>
<td>
<p>Extension DLLs have been loaded or unloaded. (For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552040">Loading Debugger Extension DLLs</a>.)</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_SYSTEMS</p>
</td>
<td>
<p>A target has been added or removed.  </p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_ASSEMBLY_OPTIONS</p>
</td>
<td>
<p>The assemble options have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_EXPRESSION_SYNTAX</p>
</td>
<td>
<p>The default expression syntax has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CES_TEXT_REPLACEMENTS</p>
</td>
<td>
<p>Text replacements have changed.  </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Argument [in]

<dd>
<p>Provides additional information about the change to the engine's state.  If more than one bit flag is set in the <i>Flags</i> parameter, the <i>Argument</i> parameter is not used.  Otherwise, the interpretation of the value of <i>Argument</i> depends on the value of <i>Flags</i>:</p>
<p></p>
<dl>

### -param DEBUG_CES_CURRENT_THREAD

<dd>
<p>The value of <i>Argument</i> is the current engine thread ID or--if there is no current thread--DEBUG_ANY_ID.  For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>
</dd>

### -param DEBUG_CES_EFFECTIVE_PROCESSOR

<dd>
<p>The value of <i>Argument</i> is the type of the effective processor.</p>
</dd>

### -param DEBUG_CES_BREAKPOINTS

<dd>
<p>The value of <i>Argument</i> is the breakpoint ID of the breakpoint that was changed or--if more than one breakpoint was changed--DEBUG_ANY_ID.  For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff538928">Breakpoints</a>.</p>
</dd>

### -param DEBUG_CES_CODE_LEVEL

<dd>
<p>The value of <i>Argument</i> is the code interpretation level.</p>
</dd>

### -param DEBUG_CES_EXECUTION_STATUS

<dd>
<p>The value of <i>Argument</i> is the execution status (as described in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541651">DEBUG_STATUS_XXX</a> topic) possibly combined with the bit flag DEBUG_STATUS_INSIDE_WAIT. DEBUG_STATUS_INSIDE_WAIT is set when a <b>WaitForEvent</b> call is pending. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541386">Debugging Session and Execution Model</a>.</p>
</dd>

### -param DEBUG_CES_ENGINE_OPTIONS

<dd>
<p>The value of <i>Argument</i> is the engine options. </p>
</dd>

### -param DEBUG_CES_LOG_FILE

<dd>
<p>The value of <i>Argument</i> is <b>TRUE</b> if the log file was opened and <b>FALSE</b> if the log file was closed.</p>
</dd>

### -param DEBUG_CES_RADIX

<dd>
<p>The value of <i>Argument</i> is the default radix.</p>
</dd>

### -param DEBUG_CES_EVENT_FILTERS

<dd>
<p>The value of <i>Argument</i> is the index of the event filter that was changed or--if more than one event filter was changed--DEBUG_ANY_ID.</p>
</dd>

### -param DEBUG_CES_PROCESS_OPTIONS

<dd>
<p>The value of <i>Argument</i> is the process options for the current process.</p>
</dd>

### -param DEBUG_CES_EXTENSIONS

<dd>
<p>The value of <i>Argument</i> is zero.</p>
</dd>

### -param DEBUG_CES_SYSTEMS

<dd>
<p>The value of <i>Argument</i> is the target ID of the target that was added or--if a target was removed--DEBUG_ANY_ID.</p>
</dd>

### -param DEBUG_CES_ASSEMBLE_OPTIONS

<dd>
<p>The value of <i>Argument</i> is the assemble options.</p>
</dd>

### -param DEBUG_CES_EXPRESSION_SYNTAX

<dd>
<p>The value of <i>Argument</i> is the default expression syntax.</p>
</dd>

### -param DEBUG_CES_TEXT_REPLACEMENTS

<dd>
<p>The value of <i>Argument</i> is DEBUG_ANY_ID.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>The return value is ignored by the engine unless it indicates a remote procedure call error; in this case the client, with which this <b>IDebugEventCallbacks</b> object is registered, is disabled.</p>

## -remarks
<p>This method is only called by the engine if the DEBUG_EVENT_CHANGE_ENGINE_STATE flag is set in the mask returned by <a href="debugger.idebugeventcallbacks_getinterestmask">IDebugEventCallbacks::GetInterestMask</a>.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>. </p>

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