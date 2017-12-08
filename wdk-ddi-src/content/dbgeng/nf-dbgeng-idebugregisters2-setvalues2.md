---
UID: NF.dbgeng.IDebugRegisters2.SetValues2
title: IDebugRegisters2::SetValues2
author: windows-driver-content
description: The SetValues2 method sets the value of several of the target's registers.
old-location: debugger\setvalues2.htm
old-project: debugger
ms.assetid: 9505a0ce-4f4e-43af-97a2-653b5776c423
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugRegisters2, SetValues2, IDebugRegisters2::SetValues2
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
req.alt-api: IDebugRegisters2.SetValues2
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

# IDebugRegisters2::SetValues2 method



## -description
<p>The <b>SetValues2</b> method sets the value of several of the target's <a href="debugger.x86_architecture#registers#registers">registers</a>.</p>


## -syntax

````
HRESULT SetValues2(
  [in]           ULONG        Source,
  [in]           ULONG        Count,
  [in, optional] PULONG       Indices,
  [in]           ULONG        Start,
  [in]           PDEBUG_VALUE Values
);
````


## -parameters
<dl>

### -param Source [in]

<dd>
<p>Specifies the register source to query.</p>
<p>The possible values are listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Register source</th>
</tr>
<tr>
<td>
<p>DEBUG_REGSRC_DEBUGGEE</p>
</td>
<td>
<p>Fetch register information from the target.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_REGSRC_EXPLICIT</p>
</td>
<td>
<p>Fetch register information from the current explicit <a href="debugger.changing_contexts#register_context#register_context">register context</a>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_REGSRC_FRAME</p>
</td>
<td>
<p>Fetch register information from the current scope's register context.</p>
<div class="alert"><b>Note</b>    Stack unwinding does not guarantee accurate updating of the register context, so the scope frame's register context might not be accurate in all cases.</div>
<div> </div>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Count [in]

<dd>
<p>Specifies the number of registers for which to set the values.</p>
</dd>

### -param Indices [in, optional]

<dd>
<p>Specifies an array that contains the indices of the registers for which to set the values.  The number of elements in this array is <i>Count</i>.  If <i>Indices</i> is <b>NULL</b>, <i>Start</i> is used instead.</p>
</dd>

### -param Start [in]

<dd>
<p>If <i>Indices</i> is <b>NULL</b>, the registers will be set consecutively starting at this index.  Otherwise, it is ignored.</p>
</dd>

### -param Values [in]

<dd>
<p>An array that contains the values to which to set the registers.  The number of elements that this array holds is <i>Count</i>.  See <a href="..\dbgeng\ns-dbgeng--debug-value.md">DEBUG_VALUE</a> for a description of this parameter type.</p>
</dd>
</dl>

## -returns
<p>This list does not contain all the errors that might occur.  For a list of possible errors, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff549771">HRESULT Values</a>.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The engine does its best to cast the values in <i>Values</i> into the type of the registers; this conversion is the same as that performed by <a href="debugger.coercevalue">CoerceValue</a>.  If the value is larger than what the register can hold, the least significant bits are dropped.  Floating-point and integer conversions will also be performed if necessary.  </p>

<p>If the return value is not S_OK, some of the registers still might have been set.  </p>

<p>When a subregister is altered, the register that contains it is also altered.</p>

<p>The method <a href="debugger.setvalues">SetValues</a> performs the same task as this method but always uses the target as the register source.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugregisters2.md">IDebugRegisters2</a>
</dt>
<dt>
<a href="debugger.setvalue">SetValue</a>
</dt>
<dt>
<a href="debugger.setvalues">SetValues</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters2::SetValues2 method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
