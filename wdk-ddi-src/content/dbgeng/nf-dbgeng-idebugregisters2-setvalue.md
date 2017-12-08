---
UID: NF.dbgeng.IDebugRegisters2.SetValue
title: IDebugRegisters2::SetValue
author: windows-driver-content
description: The SetValue method sets the value of one of the target's registers.
old-location: debugger\setvalue.htm
old-project: debugger
ms.assetid: 78c7bdea-cba5-40df-b9d7-09c7d98b0403
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugRegisters2, SetValue, IDebugRegisters2::SetValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugRegisters.SetValue,IDebugRegisters2.SetValue
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
req.iface: IDebugRegisters2
---

# IDebugRegisters2::SetValue method



## -description
<p>The <b>SetValue</b> method sets the value of one of the target's <a href="debugger.x86_architecture#registers#registers">registers</a>.</p>


## -syntax

````
HRESULT SetValue(
  [in] ULONG        Register,
  [in] PDEBUG_VALUE Value
);
````


## -parameters
<dl>

### -param Register [in]

<dd>
<p>Specifies the index of the register whose value is to be set.</p>
</dd>

### -param Value [in]

<dd>
<p>Specifies the value to which to set the register.  See <a href="..\dbgeng\ns-dbgeng--debug-value.md">DEBUG_VALUE</a> for a description of this parameter type.</p>
</dd>
</dl>

## -returns
<p>This list does not contain all the errors that might occur.  For a list of possible errors, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff549771">HRESULT Values</a>.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_UNEXPECTED</b></dt>
</dl><p>The target is not accessible, or the register could not be accessed.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The value of <i>Register</i> is greater than the number of registers on the target machine.</p>

<p> </p>

## -remarks
<p>The engine does its best to coerce the value of <i>Value</i> into the type of the register; this coercion is the same as that performed by <a href="debugger.coercevalue">CoerceValue</a>.  If the value is larger than what the register can hold, the least significant bits are dropped.  Floating-point and integer conversions will also be performed if necessary.  </p>

<p>When a subregister is altered, the register containing it is also altered.</p>

<p>To set the values of multiple registers, use the <a href="debugger.setvalues">SetValues</a> method instead.</p>

<p>For an overview of the <a href="..\dbgeng\nn-dbgeng-idebugregisters.md">IDebugRegisters</a> interface and other register-related methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554369">Registers</a>.</p>

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
<dt>Dbgeng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugregisters.md">IDebugRegisters</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugregisters2.md">IDebugRegisters2</a>
</dt>
<dt>
<a href="debugger.setvalues">SetValues</a>
</dt>
<dt>
<a href="debugger.setvalues2">SetValues2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters::SetValue method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
