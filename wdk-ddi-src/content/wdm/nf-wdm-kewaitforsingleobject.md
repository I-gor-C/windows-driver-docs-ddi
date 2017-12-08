---
UID: NF.wdm.KeWaitForSingleObject
title: KeWaitForSingleObject function
author: windows-driver-content
description: The KeWaitForSingleObject routine puts the current thread into a wait state until the given dispatcher object is set to a signaled state or (optionally) until the wait times out.
old-location: kernel\kewaitforsingleobject.htm
old-project: kernel
ms.assetid: 65a1aa46-571b-46f7-b60e-ef8c6dc14d39
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KeWaitForSingleObject
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
req.alt-api: KeWaitForSingleObject
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CompleteRequestStatusCheck, IoAllocateIrpSignalEventInCompletionTimeout, IoBuildDeviceControlWait, IoBuildDeviceControlWaitTimeout, IoBuildFsdIrpSignalEventInCompletionTimeout, IoBuildSynchronousFsdRequestWait, IoBuildSynchronousFsdRequestWaitTimeout, IrpProcessingComplete, IrqlKeWaitForMutexObject, LowerDriverReturn, MarkIrpPending2, PendedCompletedRequest, PendedCompletedRequest2, PendedCompletedRequest3, PendedCompletedRequestEx, RemoveLockForwardDeviceControl, RemoveLockForwardDeviceControlInternal, RemoveLockForwardRead, RemoveLockForwardWrite, StartDeviceWait, StartDeviceWait2, StartDeviceWait3, StartDeviceWait4, HwStorPortProhibitedDDIs, SpNoWait
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: See Remarks section.
req.product: Windows 10 or later.
---

# KeWaitForSingleObject function



## -description
The <b>KeWaitForSingleObject</b> routine puts the current thread into a wait state until the given dispatcher object is set to a signaled state or (optionally) until the wait times out.


## -syntax

````
NTSTATUS KeWaitForSingleObject(
  _In_     PVOID           Object,
  _In_     KWAIT_REASON    WaitReason,
  _In_     KPROCESSOR_MODE WaitMode,
  _In_     BOOLEAN         Alertable,
  _In_opt_ PLARGE_INTEGER  Timeout
);
````


## -parameters

### -param Object [in]

Pointer to an initialized dispatcher object (event, mutex, semaphore, thread, or timer) for which the caller supplies the storage.

### -param WaitReason [in]

Specifies the reason for the wait. A driver should set this value to <b>Executive</b>, unless it is doing work on behalf of a user and is running in the context of a user thread, in which case it should set this value to <b>UserRequest</b>.

### -param WaitMode [in]

Specifies whether the caller waits in <b>KernelMode</b> or <b>UserMode</b>. Lowest-level and intermediate drivers should specify <b>KernelMode</b>. If the given <i>Object</i> is a mutex, the caller must specify <b>KernelMode</b>.

### -param Alertable [in]

Specifies a Boolean value that is <b>TRUE</b> if the wait is alertable and <b>FALSE</b> otherwise.

### -param Timeout [in, optional]

Pointer to a time-out value that specifies the absolute or relative time, in 100-nanosecond units, at which the wait is to be completed.
A positive value specifies an absolute time, relative to January 1, 1601. A negative value specifies an interval relative to the current time. Absolute expiration times track any changes in the system time; relative expiration times are not affected by system time changes. 
If *<i>Timeout</i> = 0, the routine returns without waiting. If the caller supplies a <b>NULL</b> pointer, the routine waits indefinitely until the dispatcher object is set to the signaled state. For more information, see the following Remarks section.

## -returns
<b>KeWaitForSingleObject</b> can return one of the following:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The dispatcher object specified by the <i>Object</i> parameter satisfied the wait.
<dl>
<dt><b>STATUS_ALERTED</b></dt>
</dl>The wait was interrupted to deliver an alert to the calling thread.
<dl>
<dt><b>STATUS_USER_APC</b></dt>
</dl>The wait was interrupted to deliver a user asynchronous procedure call (APC) to the calling thread.
<dl>
<dt><b>STATUS_TIMEOUT</b></dt>
</dl>A time-out occurred before the object was set to a signaled state. This value can be returned when the specified set of wait conditions cannot be immediately met and <i>Timeout</i> is set to zero.

 

Note that the NT_SUCCESS macro recognizes all of these status values as "success" values.

## -remarks
The current state of the specified <i>Object</i> is examined to determine whether the wait can be satisfied immediately. If so, the necessary side effects are performed on the object. Otherwise, the current thread is put in a waiting state and a new thread is selected for execution on the current processor.

The <i>Alertable</i> parameter determines when the thread can be alerted and its wait state consequently aborted. For additional information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565592">Waits and APCs</a>.

A special consideration applies when the <i>Object</i> parameter passed to <b>KeWaitForSingleObject</b> is a mutex. If the dispatcher object waited on is a mutex, APC delivery is the same as for all other dispatcher objects <u>during the wait</u>. However, after <b>KeWaitForSingleObject</b> returns with STATUS_SUCCESS and the thread actually holds the mutex, only special kernel-mode APCs are delivered. Delivery of all other APCs, both kernel-mode and user-mode, is disabled. This restriction on the delivery of APCs persists until the mutex is released.

If the <i>WaitMode</i> parameter is <b>UserMode</b>, the kernel stack can be swapped out during the wait. Consequently, a caller must <u>never</u> attempt to pass parameters on the stack when calling <b>KeWaitForSingleObject</b> using the <b>UserMode</b> argument. If you allocate the event on the stack, you must set the <i>WaitMode</i> parameter to <b>KernelMode</b>.

It is especially important to check the return value of <b>KeWaitForSingleObject</b> when the <i>WaitMode</i> parameter is <b>UserMode</b> or <i>Alertable</i> is <b>TRUE</b>, because <b>KeWaitForSingleObject</b> might return early with a status of STATUS_USER_APC or STATUS_ALERTED.

All long-term waits that can be aborted by a user should be <b>UserMode</b> waits and <i>Alertable</i> should be set to <b>FALSE</b>.

Where possible, <i>Alertable</i> should be set to <b>FALSE</b> and <i>WaitMode</i> should be set to <b>KernelMode</b>, in order to reduce driver complexity. The principal exception to this is when the wait is a long-term wait.

If a <b>NULL</b> pointer is supplied for <i>Timeout</i>, the calling thread remains in a wait state until the <i>Object</i> is signaled.

A time-out value of zero allows the testing of a set of wait conditions and for the conditional performance of any side effects if the wait can be immediately satisfied, as in the acquisition of a mutex.

Time-out intervals are measured relative to the system clock, and the accuracy with which the operating system can detect the end of a time-out interval is limited by the granularity of the system clock. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj602805">Timer Accuracy</a>.

A mutex can be recursively acquired only MINLONG times. If this limit is exceeded, the routine raises a STATUS_MUTANT_LIMIT_EXCEEDED exception.

Callers of <b>KeWaitForSingleObject</b> must be running at IRQL &lt;= DISPATCH_LEVEL. However, if <i>Timeout</i> = <b>NULL</b> or *<i>Timeout</i> != 0, the caller must be running at IRQL &lt;= APC_LEVEL and in a nonarbitrary thread context. (If <i>Timeout</i> != <b>NULL</b> and *<i>Timeout</i> = 0, the caller must be running at IRQL &lt;= DISPATCH_LEVEL.)

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows 2000.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
See Remarks section.
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.wdm_completerequeststatuscheck">CompleteRequestStatusCheck</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletiontimeout">IoAllocateIrpSignalEventInCompletionTimeout</a>, <a href="devtest.wdm_iobuilddevicecontrolwait">IoBuildDeviceControlWait</a>, <a href="devtest.wdm_iobuilddevicecontrolwaittimeout">IoBuildDeviceControlWaitTimeout</a>, <a href="devtest.wdm_iobuildfsdirpsignaleventincompletiontimeout">IoBuildFsdIrpSignalEventInCompletionTimeout</a>, <a href="devtest.wdm_iobuildsynchronousfsdrequestwait">IoBuildSynchronousFsdRequestWait</a>, <a href="devtest.wdm_iobuildsynchronousfsdrequestwaittimeout">IoBuildSynchronousFsdRequestWaitTimeout</a>, <a href="devtest.wdm_irpprocessingcomplete">IrpProcessingComplete</a>, <a href="devtest.wdm_irqlkewaitformutexobject">IrqlKeWaitForMutexObject</a>, <a href="devtest.wdm_lowerdriverreturn">LowerDriverReturn</a>, <a href="devtest.wdm_markirppending2">MarkIrpPending2</a>, <a href="devtest.wdm_pendedcompletedrequest">PendedCompletedRequest</a>, <a href="devtest.wdm_pendedcompletedrequest2">PendedCompletedRequest2</a>, <a href="devtest.wdm_pendedcompletedrequest3">PendedCompletedRequest3</a>, <a href="devtest.wdm_pendedcompletedrequestex">PendedCompletedRequestEx</a>, <a href="devtest.wdm_removelockforwarddevicecontrol">RemoveLockForwardDeviceControl</a>, <a href="devtest.wdm_removelockforwarddevicecontrolinternal">RemoveLockForwardDeviceControlInternal</a>, <a href="devtest.wdm_removelockforwardread">RemoveLockForwardRead</a>, <a href="devtest.wdm_removelockforwardwrite">RemoveLockForwardWrite</a>, <a href="devtest.wdm_startdevicewait">StartDeviceWait</a>, <a href="devtest.wdm_startdevicewait2">StartDeviceWait2</a>, <a href="devtest.wdm_startdevicewait3">StartDeviceWait3</a>, <a href="devtest.wdm_startdevicewait4">StartDeviceWait4</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_spnowait">SpNoWait</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exinitializefastmutex">ExInitializeFastMutex</a>
</dt>
<dt>
<a href="kernel.kebugcheckex">KeBugCheckEx</a>
</dt>
<dt>
<a href="kernel.keinitializeevent">KeInitializeEvent</a>
</dt>
<dt>
<a href="kernel.keinitializemutex">KeInitializeMutex</a>
</dt>
<dt>
<a href="kernel.keinitializesemaphore">KeInitializeSemaphore</a>
</dt>
<dt>
<a href="kernel.keinitializetimer">KeInitializeTimer</a>
</dt>
<dt>
<a href="kernel.kewaitformultipleobjects">KeWaitForMultipleObjects</a>
</dt>
<dt>
<a href="kernel.kewaitformutexobject">KeWaitForMutexObject</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeWaitForSingleObject routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
