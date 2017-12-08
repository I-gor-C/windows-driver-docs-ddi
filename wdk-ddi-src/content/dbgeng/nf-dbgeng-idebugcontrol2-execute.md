---
UID: NF.dbgeng.IDebugControl2.Execute
title: IDebugControl2::Execute
author: windows-driver-content
description: The Execute method executes the specified debugger commands.
old-location: debugger\execute.htm
old-project: debugger
ms.assetid: 595aa371-ff7e-48e2-b29a-a7aabc70ebd7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl2, Execute, IDebugControl2::Execute
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
req.alt-api: IDebugControl.Execute,IDebugControl2.Execute,IDebugControl3.Execute
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

# IDebugControl2::Execute method



## -description
<p>The <b>Execute</b>  method executes the specified debugger commands.</p>


## -syntax

````
HRESULT Execute(
  [in] ULONG OutputControl,
  [in] PCSTR Command,
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param OutputControl [in]

<dd>
<p>Specifies the output control to use while executing the command.  For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a>.  For more information about output, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>
</dd>

### -param Command [in]

<dd>
<p>Specifies the command string to execute.  The command is interpreted like those typed into a debugger command window.  This command string can contain multiple commands for the engine to execute.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff540507">Debugger Commands</a> for the command reference.</p>
</dd>

### -param Flags [in]

<dd>
<p>Specifies a bit field of execution options for the command.  The default options are to log the command but to not send it to the output.  The following table lists the bits that can be set.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_EXECUTE_ECHO</p>
</td>
<td>
<p>The command string is sent to the output.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_EXECUTE_NOT_LOGGED</p>
</td>
<td>
<p>The command string is not logged.  This is overridden by DEBUG_EXECUTE_ECHO.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_EXECUTE_NO_REPEAT</p>
</td>
<td>
<p>If <i>Command</i> is an empty string, do not repeat the last command, and do not save the current command string for repeat execution later.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>This method executes the given command string.  If the string has multiple commands, this method will not return until all of the commands have been executed. If the sequence of commands involves waiting for the target to execute, this method can take an arbitrary amount of time to complete.</p>

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
<a href="debugger.executecommandfile">ExecuteCommandFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::Execute method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
