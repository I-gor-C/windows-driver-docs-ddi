---
UID: NF.dbgeng.IDebugEventCallbacks.ChangeDebuggeeState
title: IDebugEventCallbacks::ChangeDebuggeeState
author: windows-driver-content
description: The ChangeDebuggeeState callback method is called by the engine when it makes or detects changes to the target.
old-location: debugger\idebugeventcallbacks_changedebuggeestate.htm
ms.assetid: 157a420a-18ad-46cf-ae93-603e9226ee4f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugEventCallbacks.ChangeDebuggeeState
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
ms.keywords: IDebugEventCallbacks, ChangeDebuggeeState, IDebugEventCallbacks::ChangeDebuggeeState
req.iface: IDebugEventCallbacks
---

# IDebugEventCallbacks::ChangeDebuggeeState method



## -description
<p>The <b>ChangeDebuggeeState</b> callback method is called by the engine when it makes or detects changes to the target.</p>


## -syntax

````
HRESULT ChangeDebuggeeState(
  [in] ULONG   Flags,
  [in] ULONG64 Argument
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies the type of changes made to the target.  <i>Flags</i> may take one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_CDS_ALL</p>
</td>
<td>
<p>A general change in the target has occurred. For example, the target has been executing, or the engine has just attached to the target.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REGISTERS</p>
</td>
<td>
<p>The processor registers for the target have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_DATA</p>
</td>
<td>
<p>The target's data space has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH</p>
</td>
<td>
<p>Inform the GUI clients to refresh debugger windows.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Argument</i> [in]

<dd>
<p>Provides additional information about the change in the target. The interpretation of the value of <i>Argument</i> depends on the value of <i>Flags</i>:<p></p>
<dl>

### -param <a id="DEBUG_CDS_ALL"></a><a id="debug_cds_all"></a>DEBUG_CDS_ALL

<dd>
<p>The value of <i>Argument</i> is zero.</p>
</dd>

### -param <a id="DEBUG_CDS_REGISTERS"></a><a id="debug_cds_registers"></a>DEBUG_CDS_REGISTERS

<dd>
<p>If a single register has changed, the value of <i>Argument</i> is the index of that register.  Otherwise, the value of <i>Argument</i> is DEBUG_ANY_ID.</p>
</dd>

### -param <a id="DEBUG_CDS_DATA"></a><a id="debug_cds_data"></a>DEBUG_CDS_DATA

<dd>
<p>The value of <i>Argument</i> specifies which data space was changed.  The following table contains the possible values of <i>Argument</i>.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SPACE_VIRTUAL</p>
</td>
<td>
<p>The target's virtual memory has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SPACE_PHYSICAL</p>
</td>
<td>
<p>The target's physical memory has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SPACE_CONTROL</p>
</td>
<td>
<p>The target's control memory has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SPACE_IO</p>
</td>
<td>
<p>The target's I/O ports have received input or output.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SPACE_MSR</p>
</td>
<td>
<p>The target's Model-Specific Registers (MSRs) have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SPACE_BUS_DATA</p>
</td>
<td>
<p>The target's bus memory has changed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <a id="DEBUG_CDS_REFRESH"></a><a id="debug_cds_refresh"></a>DEBUG_CDS_REFRESH

<dd>
<p>The following table contains the possible values of <i>Argument</i>.</p>
<table>
<tr>
<th>Value</th>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_EVALUATE</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_EXECUTE</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_EXECUTECOMMANDFILE</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_ADDBREAKPOINT </p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_REMOVEBREAKPOINT</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_WRITEVIRTUAL</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_WRITEVIRTUALUNCACHED</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_WRITEPHYSICAL</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_WRITEPHYSICAL2</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_SETVALUE</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_SETVALUE2</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_SETSCOPE</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_SETSCOPEFRAMEBYINDEX</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_SETSCOPEFROMJITDEBUGINFO</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_SETSCOPEFROMSTOREDEVENT</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_INLINESTEP</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CDS_REFRESH_INLINESTEP_PSEUDO</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</p>
</dd>
</dl>

## -returns
<p>The return value is ignored by the engine unless it indicates a remote procedure call error; in this case the client, with which this <b>IDebugEventCallbacks</b> object is registered, is disabled.</p>

## -remarks
<p>The engine calls <b>ChangeDebuggeeState</b> only if the DEBUG_EVENT_CHANGE_DEBUGGEE_STATE flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550737">IDebugEventCallbacks::GetInterestMask</a>.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.  For information about managing the target's memory, including registers and data spaces, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552179">Memory Access</a>.  For information about the target's virtual and physical memory, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561217">Virtual and Physical Memory</a>.  For information about the target's control memory, I/O ports, MSR, and bus memory, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553172">Other Data Spaces</a>.</p>

<p>The engine calls <b>ChangeDebuggeeState</b> only if the DEBUG_EVENT_CHANGE_DEBUGGEE_STATE flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550737">IDebugEventCallbacks::GetInterestMask</a>.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.  For information about managing the target's memory, including registers and data spaces, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552179">Memory Access</a>.  For information about the target's virtual and physical memory, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561217">Virtual and Physical Memory</a>.  For information about the target's control memory, I/O ports, MSR, and bus memory, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553172">Other Data Spaces</a>.</p>

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