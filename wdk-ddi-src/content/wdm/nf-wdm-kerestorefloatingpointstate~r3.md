---
UID: NF.wdm.KeRestoreFloatingPointState~r3
title: KeRestoreFloatingPointState
author: windows-driver-content
description: The KeRestoreFloatingPointState routine restores the nonvolatile floating-point context saved by the preceding call to KeSaveFloatingPointState.
old-location: kernel\kerestorefloatingpointstate.htm
old-project: kernel
ms.assetid: 9a9b3c9f-5371-4d70-b1f3-5038e4cabc83
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeRestoreFloatingPointState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeRestoreFloatingPointState
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
req.iface: 
req.product: Windows 10 or later.
---

# KeRestoreFloatingPointState function



## -description
<p>The <b>KeRestoreFloatingPointState</b> routine restores the nonvolatile floating-point context saved by the preceding call to <a href="..\wdm\nf-wdm-kesavefloatingpointstate.md">KeSaveFloatingPointState</a>. </p>


## -syntax

````
NTSTATUS KeRestoreFloatingPointState(
  _In_ PKFLOATING_SAVE FloatSave
);
````


## -parameters
<dl>

### -param <i>FloatSave</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554233">KFLOATING_SAVE</a> structure that was passed in the preceding call to <a href="..\wdm\nf-wdm-kesavefloatingpointstate.md">KeSaveFloatingPointState</a>.</p>
</dd>
</dl>

## -returns
<p><b>KeRestoreFloatingPointState</b> returns STATUS_SUCCESS.</p>

## -remarks
<p><b>KeRestoreFloatingPointState</b> is the reciprocal of <b>KeSaveFloatingPointState</b>. </p>

<p>Any routine that calls <b>KeSaveFloatingPointState</b><i> must</i> call <b>KeRestoreFloatingPointState</b> before that routine returns control, and it must be running at the same IRQL as that from which the preceding call to <b>KeSaveFloatingPointState</b> occurred. Failure to meet either of these conditions causes a system bug check.</p>

<p>Kernel-mode driver code must ensure that calls to <b>KeSaveFloatingPointState</b> and <b>KeRestoreFloatingPointState</b> are properly nested. This is required so that, at each nesting level, the state that was restored by the <b>KeRestoreFloatingPointState</b> call is the same state that was saved by the corresponding <b>KeSaveFloatingPointState</b> call. To ensure proper nesting, kernel-mode driver code must follow these rules:</p>

<p>A <b>KeRestoreFloatingPointState</b> call that restores a saved state must be running at the same IRQL as the <b>KeSaveFloatingPointState</b> call that saved the state.</p>

<p>If a pair of <b>KeSaveFloatingPointState</b> and <b>KeRestoreFloatingPointState</b> calls is nested within a pair of surrounding <b>KeSaveFloatingPointState</b> and <b>KeRestoreFloatingPointState</b> calls, the IRQL for the nested calls must not be lower than the IRQL for the surrounding calls. </p>

<p>Typically, the caller-allocated <b>KFLOATING_SAVE</b> structure that contains the state that was saved by <b>KeSaveFloatingPointState</b> resides on the stack. The stack naturally preserves the nesting of saved state information. If driver code stores the state in a location other than the stack, the driver writer must take special care to preserve the nesting of the <b>KeSaveFloatingPointState</b> and <b>KeRestoreFloatingPointState</b> calls. </p>

<p>The <b>KeRestoreFloatingPointState</b> call that restores a saved state must be running in the same thread as the <b>KeSaveFloatingPointState</b> call that saved the state. </p>

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
<p>Available starting with Windows 2000.</p>
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
<a href="..\wdm\nf-wdm-kesavefloatingpointstate.md">KeSaveFloatingPointState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554233">KFLOATING_SAVE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRestoreFloatingPointState routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
