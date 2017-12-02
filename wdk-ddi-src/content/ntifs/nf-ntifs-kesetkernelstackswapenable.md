---
UID: NF.ntifs.KeSetKernelStackSwapEnable
title: KeSetKernelStackSwapEnable
author: windows-driver-content
description: The KeSetKernelStackSwapEnable routine enables and disables swapping of the caller's stack to disk.
old-location: kernel\kesetkernelstackswapenable.htm
old-project: kernel
ms.assetid: ec914f67-b2c2-4370-8685-770bca045034
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeSetKernelStackSwapEnable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeSetKernelStackSwapEnable
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
req.irql: <= APC_LEVEL
req.iface: 
---

# KeSetKernelStackSwapEnable function



## -description
<p>The <b>KeSetKernelStackSwapEnable</b> routine enables and disables swapping of the caller's stack to disk. </p>


## -syntax

````
BOOLEAN KeSetKernelStackSwapEnable(
  _In_ BOOLEAN Enable
);
````


## -parameters
<dl>

### -param Enable [in]

<dd>
<p>Specifies whether to enable swapping of the stack that belongs to the calling thread. If <b>TRUE</b>, swapping is enabled and the contents of the stack can be paged in and out of memory. If <b>FALSE</b>, swapping is disabled and the stack is memory-resident. </p>
</dd>
</dl>

## -returns
<p><b>KeSetKernelStackSwapEnable</b> returns a BOOLEAN value that indicates whether stack swapping was enabled at the time that the call was initiated. This value is <b>TRUE</b> if stack swapping was previously enabled and is <b>FALSE</b> if it was disabled. </p>

## -remarks
<p>A kernel-mode driver can call this routine to control whether its stack is pageable or locked in memory.</p>

<p>Stack swapping can occur only if the thread is in a wait state that was caused by a request from a user-mode application. Stack swapping never occurs for wait states that are initiated by kernel-mode components, regardless of whether stack swapping is enabled.</p>

<p>It is not typically necessary to disable stack swapping. Do this only in  rare cases. For an example that discusses alternatives to disabling stack swapping, see the following Examples section.</p>

<p>In a call to a kernel-mode wait routine, such as <a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a>, the caller specifies a <i>WaitMode</i> parameter to indicate whether the caller waits in kernel mode or user mode. If <i>WaitMode</i> = <b>UserMode</b>, and if the wait duration is sufficiently long, the memory manager might page out sections of the stack that belongs to the waiting thread. However, if the stack contains data items that must remain memory-resident for the duration of the wait, the thread can prevent the stack from being paged out by calling <b>KeSetKernelStackSwapEnable</b> and specifying <i>Enable</i> = <b>FALSE</b>.</p>

<p>A thread must not exit (terminate) while stack swapping is disabled or a system bug check will occur.</p>

<p>In the following code example, a driver thread allocates an event on its stack and calls <b>KeSetKernelStackSwap</b> to temporarily lock the stack in memory until the event is signaled. After the wait completes, the thread calls <b>KeSetKernelStackSwap</b> again, if necessary, to restore the original stack-swapping state of the thread.</p>

<p>An event object must be memory-resident while it can be set to a signaled or nonsignaled state, or while a thread waits on the event. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543006">Defining and Using an Event Object</a>.</p>

<p>Frequently, the use of the <b>KeSetKernelStackSwap</b> routine is unnecessary and can be avoided by allocating only pageable data items on the stack. In the previous example, the driver thread must lock the stack because the event object is allocated on the stack. A better alternative might be to simply allocate the event from nonpaged pool.</p>

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
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-keinitializeevent.md">KeInitializeEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeSetKernelStackSwapEnable routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
