---
UID: NF.dbgeng.IDebugRegisters2.OutputRegisters2
title: IDebugRegisters2::OutputRegisters2
author: windows-driver-content
description: The OutputRegisters2 method formats and outputs the target's registers.
old-location: debugger\outputregisters2.htm
old-project: debugger
ms.assetid: 444f7264-6072-4ee2-b3fd-030affa502b7
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugRegisters2, OutputRegisters2, IDebugRegisters2::OutputRegisters2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugRegisters2.OutputRegisters2
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
req.iface: IDebugRegisters2
---

# IDebugRegisters2::OutputRegisters2 method



## -description
<p>The <b>OutputRegisters2</b> method formats and outputs the target's <a href="debugger.x86_architecture#registers#registers">registers</a>.</p>


## -syntax

````
HRESULT OutputRegisters2(
  [in] ULONG OutputControl,
  [in] ULONG Source,
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>Specifies which clients should be sent the output of the formatted registers.  See <a href="debugger.debug_outctl_xxx">DEBUG_OUTCTL_XXX</a> for possible values.</p>
</dd>

### -param <i>Source</i> [in]

<dd>
<p>Specifies the register source to query.</p>
<p>The possible values are listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Register source</th>
</tr>
<tr>
<td>
<p>DEBUG_REGSRC_DEBUGGEE</p>
</td>
<td>
<p>Fetch register information from the target.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_REGSRC_EXPLICIT</p>
</td>
<td>
<p>Fetch register information from the current explicit <a href="debugger.changing_contexts#register_context#register_context">register context</a>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_REGSRC_FRAME</p>
</td>
<td>
<p>Fetch register information from the current scope's register context.</p>
<div class="alert"><b>Note</b>    Stack unwinding does not guarantee accurate updating of the register context, so the scope frame's register context might not be accurate in all cases.</div>
<div> </div>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies which register sets to print.  This can either be DEBUG_REGISTERS_DEFAULT to print commonly used registers, DEBUG_REGISTERS_ALL to print all of the register sets, or a combination of the values listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_REGISTERS_INT32</p>
</td>
<td>
<p>Print the 32-bit register set.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_REGISTERS_INT64</p>
</td>
<td>
<p>Print the 64-bit register set.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_REGISTERS_FLOAT</p>
</td>
<td>
<p>Print the floating-point register set.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This list does not contain all the errors that might occur.  For a list of possible errors, see <a href="debugger.hresult_values">HRESULT Values</a>.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The registers are formatted in a way that is specific to the target architecture's register set.</p>

<p>The method <a href="debugger.outputregisters">OutputRegisters</a> performs the same task as this method but always uses the target as the register source.</p>

<p>For an overview of the <a href="..\dbgeng\nn-dbgeng-idebugregisters.md">IDebugRegisters</a> interface and other register-related methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554369">Registers</a>.</p>

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
<dt>Dbgeng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugregisters2.md">IDebugRegisters2</a>
</dt>
<dt>
<a href="debugger.outputregisters">OutputRegisters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters2::OutputRegisters2 method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
