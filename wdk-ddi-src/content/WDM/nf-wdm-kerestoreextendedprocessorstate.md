---
UID: NF.wdm.KeRestoreExtendedProcessorState
title: KeRestoreExtendedProcessorState
author: windows-driver-content
description: The KeRestoreExtendedProcessorState routine restores extended processor state information that was previously saved.
old-location: kernel\kerestoreextendedprocessorstate.htm
ms.assetid: ea5e654a-9cb5-4d4d-9660-339410a6a20f
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeRestoreExtendedProcessorState
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (see Remarks section)
ms.keywords: KeRestoreExtendedProcessorState
req.iface: 
req.product: Windows 10 or later.
---

# KeRestoreExtendedProcessorState function



## -description
<p>The <b>KeRestoreExtendedProcessorState</b> routine restores extended processor state information that was previously saved.</p>


## -syntax

````
VOID KeRestoreExtendedProcessorState(
  _In_ PXSTATE_SAVE XStateSave
);
````


## -parameters
<dl>

### -param <i>XStateSave</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566414">XSTATE_SAVE</a> structure that contains the extended processor state information to restore. The contents of this structure must have been previously saved by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553238">KeSaveExtendedProcessorState</a> routine.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Kernel-mode driver code must ensure that calls to <b>KeSaveExtendedProcessorState</b> and <b>KeRestoreExtendedProcessorState</b> are properly nested. This is required so that, at each nesting level, the state that was restored by the <b>KeRestoreExtendedProcessorState</b> call is the same state that was saved by the corresponding <b>KeSaveExtendedProcessorState</b> call. To ensure proper nesting, kernel-mode driver code must follow these rules:</p>

<p>A <b>KeRestoreExtendedProcessorState</b> call that restores a saved state must be running at the same IRQL as the <b>KeSaveExtendedProcessorState</b> call that saved the state. </p>

<p>If a pair of <b>KeSaveExtendedProcessorState</b> and <b>KeRestoreExtendedProcessorState</b> calls is nested within a pair of surrounding <b>KeSaveExtendedProcessorState</b> and <b>KeRestoreExtendedProcessorState</b> calls, the IRQL for the nested calls must not be lower than the IRQL for the surrounding calls. </p>

<p>Typically, the caller-allocated <b>XSTATE_SAVE</b> structure that contains the state that was saved by <b>KeSaveExtendedProcessorState</b> resides on the stack. The stack naturally preserves the nesting of saved state information. If driver code stores the state in a location other than the stack, the driver writer must take special care to preserve the nesting of the <b>KeSaveExtendedProcessorState</b> and <b>KeRestoreExtendedProcessorState</b> calls.</p>

<p>The <b>KeRestoreExtendedProcessorState</b> call that restores a saved state must be running in the same thread as the <b>KeSaveExtendedProcessorState</b> call that saved the state. </p>

<p>A similar set of rules apply to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553243">KeSaveFloatingPointState</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553185">KeRestoreFloatingPointState</a> routines.</p>

<p>Kernel-mode driver code must ensure that calls to <b>KeSaveExtendedProcessorState</b> and <b>KeRestoreExtendedProcessorState</b> are properly nested. This is required so that, at each nesting level, the state that was restored by the <b>KeRestoreExtendedProcessorState</b> call is the same state that was saved by the corresponding <b>KeSaveExtendedProcessorState</b> call. To ensure proper nesting, kernel-mode driver code must follow these rules:</p>

<p>A <b>KeRestoreExtendedProcessorState</b> call that restores a saved state must be running at the same IRQL as the <b>KeSaveExtendedProcessorState</b> call that saved the state. </p>

<p>If a pair of <b>KeSaveExtendedProcessorState</b> and <b>KeRestoreExtendedProcessorState</b> calls is nested within a pair of surrounding <b>KeSaveExtendedProcessorState</b> and <b>KeRestoreExtendedProcessorState</b> calls, the IRQL for the nested calls must not be lower than the IRQL for the surrounding calls. </p>

<p>Typically, the caller-allocated <b>XSTATE_SAVE</b> structure that contains the state that was saved by <b>KeSaveExtendedProcessorState</b> resides on the stack. The stack naturally preserves the nesting of saved state information. If driver code stores the state in a location other than the stack, the driver writer must take special care to preserve the nesting of the <b>KeSaveExtendedProcessorState</b> and <b>KeRestoreExtendedProcessorState</b> calls.</p>

<p>The <b>KeRestoreExtendedProcessorState</b> call that restores a saved state must be running in the same thread as the <b>KeSaveExtendedProcessorState</b> call that saved the state. </p>

<p>A similar set of rules apply to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553243">KeSaveFloatingPointState</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553185">KeRestoreFloatingPointState</a> routines.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553185">KeRestoreFloatingPointState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553238">KeSaveExtendedProcessorState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553243">KeSaveFloatingPointState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566414">XSTATE_SAVE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRestoreExtendedProcessorState routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
