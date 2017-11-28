---
UID: NF.dbgeng.IDebugControl.CoerceValues
title: IDebugControl::CoerceValues
author: windows-driver-content
description: The CoerceValues method converts an array of values into an array of values of different types.
old-location: debugger\coercevalues.htm
old-project: debugger
ms.assetid: d5374177-fddd-4f35-8cad-10be762ef4d8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl, CoerceValues, IDebugControl::CoerceValues
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
req.alt-api: IDebugControl.CoerceValues,IDebugControl2.CoerceValues,IDebugControl3.CoerceValues
req.alt-loc: Dbgeng.h
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

# IDebugControl::CoerceValues method



## -description
<p>The <b>CoerceValues</b> method converts an array of values into an array of values of different types.</p>


## -syntax

````
HRESULT CoerceValues(
  [in]  ULONG        Count,
  [in]  PDEBUG_VALUE In,
  [in]  PULONG       OutType,
  [out] PDEBUG_VALUE Out
);
````


## -parameters
<dl>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of values to convert.</p>
</dd>

### -param <i>In</i> [in]

<dd>
<p>Specifies the array of values to convert.  The number of elements that this array holds is <i>Count</i>.</p>
</dd>

### -param <i>OutType</i> [in]

<dd>
<p>Specifies the array of desired types for the converted values. For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541719">DEBUG_VALUE</a>.  The number of elements that this array holds is <i>Count</i>.</p>
</dd>

### -param <i>Out</i> [out]

<dd>
<p>Specifies the array to be populated by the converted values.  The types of these values are specified by <i>OutType</i>.  The number of elements that this array holds is <i>Count</i>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method converts an array of values of one type into values of another type.  Some of these conversions can result in loss of precision.</p>

<p>This method converts an array of values of one type into values of another type.  Some of these conversions can result in loss of precision.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539158">CoerceValue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541719">DEBUG_VALUE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::CoerceValues method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
