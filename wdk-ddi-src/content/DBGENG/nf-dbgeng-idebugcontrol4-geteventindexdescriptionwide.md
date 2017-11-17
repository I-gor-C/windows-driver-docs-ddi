---
UID: NF.dbgeng.IDebugControl4.GetEventIndexDescriptionWide
title: IDebugControl4::GetEventIndexDescriptionWide
author: windows-driver-content
description: The GetEventIndexDescriptionWide method describes the specified event in a static list of events for the current target.
old-location: debugger\geteventindexdescriptionwide.htm
ms.assetid: 0153ee1d-93b3-497c-9fbf-e285c3730f72
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
req.alt-api: IDebugControl4.GetEventIndexDescriptionWide
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
ms.keywords: IDebugControl4, GetEventIndexDescriptionWide, IDebugControl4::GetEventIndexDescriptionWide
req.iface: IDebugControl4
---

# IDebugControl4::GetEventIndexDescriptionWide method



## -description
<p>The <b>GetEventIndexDescriptionWide</b> method describes the specified event in a static list of events for the current target.</p>


## -syntax

````
HRESULT GetEventIndexDescriptionWide(
  [in]            ULONG  Index,
  [in]            ULONG  Which,
  [in, optional]  PWSTR  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG DescSize
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the event whose description will be returned.</p>
</dd>

### -param <i>Which</i> [in]

<dd>
<p>Specifies which piece of the event description to return.  Currently only DEBUG_EINDEX_NAME is supported; this returns the name of the event.</p>
</dd>

### -param <i>Buffer</i> [in, optional]

<dd>
<p>Receives the description of the event.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the <i>Buffer </i>buffer.</p>
</dd>

### -param <i>DescSize</i> [out, optional]

<dd>
<p>Receives the size, in characters, of the description.  If <i>DescSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The amount of descriptive information available for a particular target varies depending on the type of the target.</p>

<p>The amount of descriptive information available for a particular target varies depending on the type of the target.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547906">GetNumberEvents</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545755">GetCurrentEventIndex</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::GetEventIndexDescriptionWide method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
