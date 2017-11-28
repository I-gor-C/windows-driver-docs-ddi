---
UID: NF.dbgeng.IDebugControl3.SetNextEventIndex
title: IDebugControl3::SetNextEventIndex
author: windows-driver-content
description: The SetNextEventIndex method sets the next event for the current target by selecting the event from the static list of events for the target, if such a list exists.
old-location: debugger\setnexteventindex.htm
old-project: debugger
ms.assetid: fbff721a-fdd9-4343-b9a9-92f41fb21ba2
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl3, SetNextEventIndex, IDebugControl3::SetNextEventIndex
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
req.alt-api: IDebugControl3.SetNextEventIndex
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
req.iface: IDebugControl3
---

# IDebugControl3::SetNextEventIndex method



## -description
<p>The <b>SetNextEventIndex</b> method sets the next event for the current target by selecting the event from the static list of events for the target, if such a list exists.</p>


## -syntax

````
HRESULT SetNextEventIndex(
  [in]  ULONG  Relation,
  [in]  ULONG  Value,
  [out] PULONG NextIndex
);
````


## -parameters
<dl>

### -param <i>Relation</i> [in]

<dd>
<p>Specifies how to interpret <i>Value</i> when setting the index of the next event.  Possible values are: DEBUG_EINDEX_FROM_START, DEBUG_EINDEX_FROM_END, and DEBUG_EINDEX_FROM_CURRENT.</p>
</dd>

### -param <i>Value</i> [in]

<dd>
<p>Specifies the index of the next event relative to the first, last, or current event.  The interpretation of <i>Value</i> depends on the value of <i>Relation</i>, as follows.</p>
<table>
<tr>
<th>Value of <i>Relation</i></th>
<th>Next Event Index</th>
</tr>
<tr>
<td>
<p>DEBUG_EINDEX_FROM_START</p>
</td>
<td>
<p><i>Value</i>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_EINDEX_FROM_END</p>
</td>
<td>
<p>Number of events minus <i>Value</i>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_EINDEX_FROM_CURRENT</p>
</td>
<td>
<p>The current event index plus <i>Value</i>.</p>
</td>
</tr>
</table>
<p> </p>
<p>The resulting index must be greater than zero and one less than the number of events returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff547906">GetNumberEvents</a>.</p>
</dd>

### -param <i>NextIndex</i> [out]

<dd>
<p>Receives the index of the next event.  If <i>NextIndex</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>If the specified event is the same as the current event, this method does nothing.  Otherwise,  this method sets the execution status of the target to DEBUG_STATUS_GO (and notifies the event callbacks).  When <a href="https://msdn.microsoft.com/library/windows/hardware/ff561229">WaitForEvent</a> is called, the engine will generate the specified event for the event callbacks and set it as the current event.</p>

<p>This method is only useful if the target offers a list of events.</p>

<p>If the specified event is the same as the current event, this method does nothing.  Otherwise,  this method sets the execution status of the target to DEBUG_STATUS_GO (and notifies the event callbacks).  When <a href="https://msdn.microsoft.com/library/windows/hardware/ff561229">WaitForEvent</a> is called, the engine will generate the specified event for the event callbacks and set it as the current event.</p>

<p>This method is only useful if the target offers a list of events.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl3::SetNextEventIndex method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
