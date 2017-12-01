---
UID: NF.dbgeng.IDebugControl.CoerceValue
title: IDebugControl::CoerceValue
author: windows-driver-content
description: The CoerceValue method converts a value of one type into a value of another type.
old-location: debugger\coercevalue.htm
old-project: debugger
ms.assetid: db037fc8-d503-4a72-b6bc-d5189f6786d4
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl, CoerceValue, IDebugControl::CoerceValue
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
req.alt-api: IDebugControl.CoerceValue,IDebugControl2.CoerceValue,IDebugControl3.CoerceValue
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

# IDebugControl::CoerceValue method



## -description
<p>The <b>CoerceValue</b> method converts a value of one type into a value of another type.</p>


## -syntax

````
HRESULT CoerceValue(
  [in]  PDEBUG_VALUE In,
  [in]  ULONG        OutType,
  [out] PDEBUG_VALUE Out
);
````


## -parameters
<dl>

### -param <i>In</i> [in]

<dd>
<p>Specifies the value to be converted</p>
</dd>

### -param <i>OutType</i> [in]

<dd>
<p>Specifies the desired type for the converted value. See <a href="..\dbgeng\ns-dbgeng--debug-value.md">DEBUG_VALUE</a> for possible values.</p>
</dd>

### -param <i>Out</i> [out]

<dd>
<p>Receives the converted value.  The type of this value will be the type specified by <i>OutType</i>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method converts a value of one type into a value of another type.  If the specified <i>OutType</i> is not capable of containing the information supplied by the <i>In</i> variable, data will be lost.</p>

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
<a href="..\dbgeng\ns-dbgeng--debug-value.md">DEBUG_VALUE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::CoerceValue method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
