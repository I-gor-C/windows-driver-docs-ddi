---
UID: NF.dbgeng.IDebugRegisters2.SetPseudoValues
title: IDebugRegisters2::SetPseudoValues
author: windows-driver-content
description: The SetPseudoValues method sets the value of several pseudo-registers.
old-location: debugger\setpseudovalues.htm
old-project: debugger
ms.assetid: 89bfe36a-6674-43b7-a889-24fe15771aea
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugRegisters2, SetPseudoValues, IDebugRegisters2::SetPseudoValues
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
req.alt-api: IDebugRegisters2.SetPseudoValues
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

# IDebugRegisters2::SetPseudoValues method



## -description
<p>The <b>SetPseudoValues</b> method sets the value of several pseudo-registers.</p>


## -syntax

````
HRESULT SetPseudoValues(
  [in]           ULONG        Source,
  [in]           ULONG        Count,
  [in, optional] PULONG       Indices,
  [in]           ULONG        Start,
  [in]           PDEBUG_VALUE Values
);
````


## -parameters
<dl>

### -param <i>Source</i> [in]

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

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of pseudo-registers whose values are being set.</p>
</dd>

### -param <i>Indices</i> [in, optional]

<dd>
<p>Specifies an array of indices of pseudo-registers.  These are the pseudo-registers whose values will be set.  The size of <i>Indices</i> is <i>Count</i>.  If <i>Indices</i> is <b>NULL</b>, <i>Start</i> is used to specify the indices instead.</p>
</dd>

### -param <i>Start</i> [in]

<dd>
<p>Specifies the index of the first pseudo-register whose value will be set.  The pseudo-registers with indices between <i>Start</i> and <i>Start</i> plus <i>Count</i> minus one, will be set.  <i>Start</i> is only used if <i>Indices</i> is <b>NULL</b>.</p>
</dd>

### -param <i>Values</i> [in]

<dd>
<p>Specifies the new values of the pseudo-registers.  The number of elements this array holds is <i>Count</i>.  See <a href="..\dbgeng\ns-dbgeng--debug-value.md">DEBUG_VALUE</a> for a description of this parameter type.</p>
</dd>
</dl>

## -returns
<p>This list does not contain all the errors that might occur.  For a list of possible errors, see <a href="debugger.hresult_values">HRESULT Values</a>.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
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
<a href="debugger.getpseudovalues">GetPseudoValues</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters2::SetPseudoValues method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
