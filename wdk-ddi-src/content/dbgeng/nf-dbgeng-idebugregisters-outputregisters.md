---
UID: NF.dbgeng.IDebugRegisters.OutputRegisters
title: IDebugRegisters::OutputRegisters
author: windows-driver-content
description: The OutputRegisters method formats and sends the target's registers to the clients as output.
old-location: debugger\outputregisters.htm
old-project: debugger
ms.assetid: d1354ab7-4d7d-4cc2-8e30-763d8b881a11
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugRegisters, OutputRegisters, IDebugRegisters::OutputRegisters
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
req.alt-api: IDebugRegisters.OutputRegisters,IDebugRegisters2.OutputRegisters
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
req.iface: IDebugRegisters
---

# IDebugRegisters::OutputRegisters method



## -description
<p>The <b>OutputRegisters</b> method formats and sends the target's <a href="debugger.x86_architecture#registers#registers">registers</a> to the clients as output.</p>


## -syntax

````
HRESULT OutputRegisters(
  [in] ULONG OutputControl,
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param OutputControl [in]

<dd>
<p>Specifies which clients should be sent the output of the formatted registers.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a> for possible values.</p>
</dd>

### -param Flags [in]

<dd>
<p>Specifies which set of registers to print.  This can either be DEBUG_REGISTERS_DEFAULT to print commonly used registers, DEBUG_REGISTERS_ALL to print all the sets of registers, or a combination of the values listed in the following table.</p>
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
<p>This list does not contain all the errors that might occur.  For a list of possible errors, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff549771">HRESULT Values</a>.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The registers are formatted in a way that is specific to the target architecture's register set.</p>

<p>The method <a href="debugger.outputregisters2">OutputRegisters2</a> performs the same task as this method but also allows the register source to be specified.</p>

<p>For an overview of the <a href="..\dbgeng\nn-dbgeng-idebugregisters.md">IDebugRegisters</a> interface and other register-related methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554369">Registers</a>.  For details on sending output to the clients, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugregisters.md">IDebugRegisters</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugregisters2.md">IDebugRegisters2</a>
</dt>
<dt>
<a href="debugger.outputregisters2">OutputRegisters2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters::OutputRegisters method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
