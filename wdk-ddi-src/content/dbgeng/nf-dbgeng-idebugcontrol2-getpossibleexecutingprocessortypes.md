---
UID: NF.dbgeng.IDebugControl2.GetPossibleExecutingProcessorTypes
title: IDebugControl2::GetPossibleExecutingProcessorTypes
author: windows-driver-content
description: The GetPossibleExecutingProcessorTypes method returns the processor types that are supported by the computer running the current target.
old-location: debugger\getpossibleexecutingprocessortypes.htm
old-project: debugger
ms.assetid: fb11b655-2528-447f-9f5e-3c9e4e040156
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, GetPossibleExecutingProcessorTypes, IDebugControl2::GetPossibleExecutingProcessorTypes
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
req.alt-api: IDebugControl.GetPossibleExecutingProcessorTypes,IDebugControl2.GetPossibleExecutingProcessorTypes,IDebugControl3.GetPossibleExecutingProcessorTypes
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

# IDebugControl2::GetPossibleExecutingProcessorTypes method



## -description
<p>The <b>GetPossibleExecutingProcessorTypes</b> method returns the processor types that are supported by the computer running the current target.</p>


## -syntax

````
HRESULT GetPossibleExecutingProcessorTypes(
  [in]  ULONG  Start,
  [in]  ULONG  Count,
  [out] PULONG Types
);
````


## -parameters
<dl>

### -param <i>Start</i> [in]

<dd>
<p>Specifies the index of the first processor type to return.  The processor types are indexed by numbers zero through to the number of processor types supported by the current target minus one.  The number of processor types supported by the current target can be found using <a href="debugger.getnumberpossibleexecutingprocessortypes">GetNumberPossibleExecutingProcessorTypes</a>.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies how many processor types to return.</p>
</dd>

### -param <i>Types</i> [out]

<dd>
<p>Receives the list of processor types.  The number of elements this array holds is <i>Count</i>.  For a description of the processor types see <a href="debugger.getactualprocessortype">GetActualProcessorType</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.</p>

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
<a href="debugger.getnumberpossibleexecutingprocessortypes">GetNumberPossibleExecutingProcessorTypes</a>
</dt>
<dt>
<a href="debugger.getactualprocessortype">GetActualProcessorType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetPossibleExecutingProcessorTypes method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
