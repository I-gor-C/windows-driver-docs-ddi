---
UID: NF.dbgeng.IDebugControl3.GetSupportedProcessorTypes
title: IDebugControl3::GetSupportedProcessorTypes
author: windows-driver-content
description: The GetSupportedProcessorTypes method returns the processor types supported by the debugger engine.
old-location: debugger\getsupportedprocessortypes.htm
old-project: debugger
ms.assetid: b1a69c60-67e8-46b0-8f2e-7da2c4860ea6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl3, GetSupportedProcessorTypes, IDebugControl3::GetSupportedProcessorTypes
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
req.alt-api: IDebugControl.GetSupportedProcessorTypes,IDebugControl2.GetSupportedProcessorTypes,IDebugControl3.GetSupportedProcessorTypes
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

# IDebugControl3::GetSupportedProcessorTypes method



## -description
<p>The <b>GetSupportedProcessorTypes</b> method returns the processor types supported by the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.    </p>


## -syntax

````
HRESULT GetSupportedProcessorTypes(
  [in]  ULONG  Start,
  [in]  ULONG  Count,
  [out] PULONG Types
);
````


## -parameters
<dl>

### -param <i>Start</i> [in]

<dd>
<p>Specifies the index of the first processor type to return.  The supported processor types are indexed by the numbers zero through the number of supported processor types minus one.  The number of supported processor types can be found using <a href="https://msdn.microsoft.com/library/windows/hardware/ff547966">GetNumberSupportedProcessorTypes</a>.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of processor types to return.</p>
</dd>

### -param <i>Types</i> [out]

<dd>
<p>Receives the list of processor types.  The number of elements this array holds is <i>Count</i>.  For a description of the processor types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545572">GetActualProcessorType</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547966">GetNumberSupportedProcessorTypes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548169">GetProcessorTypeNames</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetSupportedProcessorTypes method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
