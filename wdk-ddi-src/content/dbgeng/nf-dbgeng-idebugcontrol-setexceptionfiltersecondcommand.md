---
UID: NF.dbgeng.IDebugControl.SetExceptionFilterSecondCommand
title: IDebugControl::SetExceptionFilterSecondCommand
author: windows-driver-content
description: The SetExceptionFilterSecondCommand method sets the command that will be executed by the debugger engine on the second chance of a specified exception.
old-location: debugger\setexceptionfiltersecondcommand.htm
old-project: debugger
ms.assetid: c95fa025-9455-4a8e-99ef-84030255575c
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl, SetExceptionFilterSecondCommand, IDebugControl::SetExceptionFilterSecondCommand
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
req.alt-api: IDebugControl.SetExceptionFilterSecondCommand,IDebugControl2.SetExceptionFilterSecondCommand,IDebugControl3.SetExceptionFilterSecondCommand
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
req.iface: IDebugControl
---

# IDebugControl::SetExceptionFilterSecondCommand method



## -description
<p>The <b>SetExceptionFilterSecondCommand</b>  method sets the command that will be executed by the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> on the second chance of a specified <a href="wdkgloss.e#wdkgloss.exception#wdkgloss.exception"><i>exception</i></a>.</p>


## -syntax

````
HRESULT SetExceptionFilterSecondCommand(
  [in] ULONG Index,
  [in] PCSTR Command
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the exception filter whose second-chance command will be set.  <i>Index</i> must not refer to the specific event filters as these are not exception filters and only exception events get a second chance.  If <i>Index</i> refers to the default exception filter, the second-chance command is set for all exceptions that do not have an exception filter.</p>
</dd>

### -param <i>Command</i> [in]

<dd>
<p>Receives the second-chance command for the exception filter.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about <a href="debugger.events#event_filters#event_filters">event filters</a>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543071">Event Filters</a>.</p>

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
<a href="https://msdn.microsoft.com/fdb5059f-e7d9-4e14-aa3d-030e72c30732">sx, sxd, sxe, sxi, sxn (Set Exceptions)</a>
</dt>
<dt>
<a href="debugger.getexceptionfiltersecondcommand">GetExceptionFilterSecondCommand</a>
</dt>
<dt>
<a href="debugger.seteventfiltercommand">SetEventFilterCommand</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::SetExceptionFilterSecondCommand method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
