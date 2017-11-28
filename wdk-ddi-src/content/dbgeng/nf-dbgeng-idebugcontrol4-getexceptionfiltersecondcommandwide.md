---
UID: NF.dbgeng.IDebugControl4.GetExceptionFilterSecondCommandWide
title: IDebugControl4::GetExceptionFilterSecondCommandWide
author: windows-driver-content
description: The GetExceptionFilterSecondCommandWide method returns the command that will be executed by the debugger engine upon the second chance of a specified exception.
old-location: debugger\getexceptionfiltersecondcommandwide.htm
old-project: debugger
ms.assetid: 17a61847-78b7-45b8-b02b-3ba4cdba6bff
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl4, GetExceptionFilterSecondCommandWide, IDebugControl4::GetExceptionFilterSecondCommandWide
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
req.alt-api: IDebugControl4.GetExceptionFilterSecondCommandWide
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
req.iface: IDebugControl4
---

# IDebugControl4::GetExceptionFilterSecondCommandWide method



## -description
<p>The <b>GetExceptionFilterSecondCommandWide</b>  method returns the command that will be executed by the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> upon the second chance of a specified <a href="wdkgloss.e#wdkgloss.exception#wdkgloss.exception"><i>exception</i></a>.</p>


## -syntax

````
HRESULT GetExceptionFilterSecondCommandWide(
  [in]            ULONG  Index,
  [out, optional] PWSTR  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG CommandSize
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the exception filter whose second-chance command will be returned.  <i>Index</i> can also refer to the default exception filter to return the second-chance command for those exceptions that do not have a specific or arbitrary exception filter.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the second-chance command for the exception filter.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the buffer that <i>Buffer</i> specifies.</p>
</dd>

### -param <i>CommandSize</i> [out, optional]

<dd>
<p>Receives the size, in characters, of the second-chance command for the exception filter.  If <i>CommandSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Only exception filters support a second-chance command.  If <i>Index</i> refers to a <a href="debug_filter_xxx.htm#specific_event_filter">specific event filter</a>, the command returned to <i>Buffer</i> will be empty.  The returned command will also be empty if no second-chance command has been set for the specified exception.</p>

<p>For more information about <a href="debugger.events#event_filters#event_filters">event filters</a>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543071">Event Filters</a>.</p>

<p>Only exception filters support a second-chance command.  If <i>Index</i> refers to a <a href="debug_filter_xxx.htm#specific_event_filter">specific event filter</a>, the command returned to <i>Buffer</i> will be empty.  The returned command will also be empty if no second-chance command has been set for the specified exception.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550526">IDebugControl4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fdb5059f-e7d9-4e14-aa3d-030e72c30732">sx, sxd, sxe, sxi, sxn (Set Exceptions)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556687">SetExceptionFilterSecondCommand</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546611">GetEventFilterCommand</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::GetExceptionFilterSecondCommandWide method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
