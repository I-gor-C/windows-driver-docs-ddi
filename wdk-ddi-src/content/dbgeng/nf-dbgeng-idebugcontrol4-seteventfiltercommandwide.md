---
UID: NF.dbgeng.IDebugControl4.SetEventFilterCommandWide
title: IDebugControl4::SetEventFilterCommandWide
author: windows-driver-content
description: The SetEventFilterCommandWide method sets a debugger command for the engine to execute when a specified event occurs.
old-location: debugger\seteventfiltercommandwide.htm
old-project: debugger
ms.assetid: e0e14c8b-0b11-482f-93e2-31c522235110
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl4, SetEventFilterCommandWide, IDebugControl4::SetEventFilterCommandWide
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
req.alt-api: IDebugControl4.SetEventFilterCommandWide
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

# IDebugControl4::SetEventFilterCommandWide method



## -description
<p>The <b>SetEventFilterCommandWide</b>  method sets a debugger command for the engine to execute when a specified event occurs.</p>


## -syntax

````
HRESULT SetEventFilterCommandWide(
  [in] ULONG  Index,
  [in] PCWSTR Command
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the event filter.  <i>Index</i> can take any value between zero and one less than the total number of event filters returned by <b>GetNumberEventFilters</b> (inclusive).  For more information about the index of the filters, see Index and Exception Code.</p>
</dd>

### -param <i>Command</i> [in]

<dd>
<p>Specifies the debugger command for the engine to execute when the event occurs.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about event filters, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543071">Event Filters</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fdb5059f-e7d9-4e14-aa3d-030e72c30732">sx, sxd, sxe, sxi, sxn (Set Exceptions)</a>
</dt>
<dt>
<a href="debugger.geteventfiltercommand">GetEventFilterCommand</a>
</dt>
<dt>
<a href="debugger.setexceptionfiltersecondcommand">SetExceptionFilterSecondCommand</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::SetEventFilterCommandWide method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
