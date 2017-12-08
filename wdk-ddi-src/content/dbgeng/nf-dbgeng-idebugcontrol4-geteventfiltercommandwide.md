---
UID: NF.dbgeng.IDebugControl4.GetEventFilterCommandWide
title: IDebugControl4::GetEventFilterCommandWide
author: windows-driver-content
description: The GetEventFilterCommandWide method returns the debugger command that the engine will execute when a specified event occurs.
old-location: debugger\geteventfiltercommandwide.htm
old-project: debugger
ms.assetid: a565627a-4a70-4255-9a88-c39a3db11d25
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl4, GetEventFilterCommandWide, IDebugControl4::GetEventFilterCommandWide
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
req.alt-api: IDebugControl4.GetEventFilterCommandWide
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

# IDebugControl4::GetEventFilterCommandWide method



## -description
<p>The <b>GetEventFilterCommandWide</b>  method returns the debugger command that the engine will execute when a specified event occurs.</p>


## -syntax

````
HRESULT GetEventFilterCommandWide(
  [in]            ULONG  Index,
  [out, optional] PWSTR  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG CommandSize
);
````


## -parameters
<dl>

### -param Index [in]

<dd>
<p>Specifies the index of the event filter.  <i>Index</i> can take any value between zero and one less than the total number of event filters returned by <a href="debugger.getnumbereventfilters">GetNumberEventFilters</a> (inclusive).  For more information about the index of the filters, see Index and Exception Code.</p>
</dd>

### -param Buffer [out, optional]

<dd>
<p>Receives the debugger command that the engine will execute when the event occurs.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size, in characters, of the buffer that <i>Buffer</i> specifies.</p>
</dd>

### -param CommandSize [out, optional]

<dd>
<p>Receives the size in characters of the command.  If <i>CommandSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
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
<a href="debugger.seteventfiltercommand">SetEventFilterCommand</a>
</dt>
<dt>
<a href="debugger.getexceptionfiltersecondcommand">GetExceptionFilterSecondCommand</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::GetEventFilterCommandWide method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
