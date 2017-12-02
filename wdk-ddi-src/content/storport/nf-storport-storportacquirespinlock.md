---
UID: NF.storport.StorPortAcquireSpinLock
title: StorPortAcquireSpinLock
author: windows-driver-content
description: The StorPortAcquireSpinLock routine acquires the specified spin lock.
old-location: storage\storportacquirespinlock.htm
old-project: storage
ms.assetid: 52a877c7-b274-4bec-b948-edb0585a09e1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortAcquireSpinLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortAcquireSpinLock
req.alt-loc: storport.h
req.ddi-compliance: StorPortSpinLock, StorPortSpinLock3, StorPortSpinLock4
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StorPortAcquireSpinLock function



## -description
<p>The <b>StorPortAcquireSpinLock</b> routine acquires the specified spin lock. </p>


## -syntax

````
VOID StorPortAcquireSpinLock(
  _In_    PVOID             DeviceExtension,
  _In_    STOR_SPINLOCK     SpinLock,
  _In_    PVOID             LockContext,
  _Inout_ PSTOR_LOCK_HANDLE LockHandle
);
````


## -parameters
<dl>

### -param DeviceExtension [in]

<dd>
<p>A pointer to the miniport driver per-adapter device extension. </p>
</dd>

### -param SpinLock [in]

<dd>
<p>Contains an enumerator value of type <a href="..\storport\ne-storport--stor-spinlock.md">STOR_SPINLOCK</a> that specifies the spin lock to acquire. </p>
</dd>

### -param LockContext [in]

<dd>
<p>A pointer to the DPC object for which the lock is held if <i>SpinLock</i> indicates a type of <b>DpcLock</b>. This member should be <b>NULL</b> if <i>SpinLock </i>indicates a type of either <b>InterruptLock</b> or <b>StartIoLock</b>. </p>
</dd>

### -param LockHandle [in, out]

<dd>
<p>A pointer to a buffer that, on return, will contain a lock handle. To release the lock, the caller must pass this handle to the <a href="..\storport\nf-storport-storportreleasespinlock.md">StorPortReleaseSpinLock</a> routine. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Miniport drivers must ensure that they do not attempt to acquire a lock that is already held or acquire locks in an incorrect order. Either of these mistakes will result in system deadlock.</p>

<p>Certain locks are held automatically by the port driver before it calls the miniport driver callback routines. For each miniport driver callback routine, the following table indicates which locks the port driver acquires automatically before calling the callback routine.</p>

<p>
<a href="storage.hwstorfindadapter">HwStorFindAdapter</a>
</p>

<p>None</p>

<p>
<a href="storage.hwstorinitialize">HwStorInitialize</a>
</p>

<p>Interrupt (physical miniports), None (virtual miniports)</p>

<p>
<a href="storage.hwstorinterrupt">HwStorInterrupt</a>
</p>

<p>Interrupt</p>

<p>
<a href="storage.hwmsinterruptroutine">HwMSIInterruptRoutine</a>
</p>

<p>
<a href="storage.hwstorstartio">
        HwStorStartIo</a>
</p>

<p>StartIo (physical miniports only when requested concurrent channels &lt;= 1)</p>

<p>
<a href="storage.hwstorbuildio">HwStorBuildIo</a>
</p>

<p>
<a href="storage.hwstortimer">HwStorTimer</a>
</p>

<p> Startio, Interrupt (when <b>SynchronizationModel</b> member of <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> is set to <b>StorSynchronizeHalfDuplex</b>)</p>

<p>
<a href="storage.hwstorresetbus">HwStorResetBus</a>
</p>

<p>
<a href="storage.hwstoradaptercontrol">HwStorAdapterControl</a>
</p>

<p>
<a href="storage.hwstorunitcontrol">HwStorUnitControl</a>
</p>

<p>
<a href="storage.hwstortracingenabled">HwStorTracingEnabled</a>
</p>

<p>
<a href="storage.hwstorpassiveinitializeroutine">HwStorPassiveInitializeRoutine</a>
</p>

<p>
<a href="storage.hwstordpcroutine">HwStorDpcRoutine</a>
</p>

<p>
<a href="storage.hwstordpcroutine">HwStorStateChange</a>
</p>

<p>The locks held by the port driver influence which locks the callback routines are allowed to acquire, because spin locks must be acquired in the following order:</p>

<p>DPC or StartIo</p>

<p>For instance, if the port driver acquires the <i>Interrupt</i> spin lock before calling a callback routine, that callback routine can no longer acquire the <i>DPC</i> or <i>StartIo</i> spin lock because the <i>DPC</i> and <i>StartIo</i> spin locks are of a lower order than the <i>Interrupt</i> spin lock. On the other hand, if the port driver acquires the <i>StartIo</i> spin lock before calling a callback routine, that callback routine, when executed, could still acquire an  <i>Interrupt</i> or a <i>DPC</i> spin lock.</p>

<p>The following table indicates which spin locks each miniport driver routine can acquire. In those cases where the miniport driver routine must obtain both the <i>StartIo</i> spin lock and the <i>Interrupt</i> spin lock, the routine must always acquire the <i>StartIo</i> spin lock first.</p>

<p>DPC, Interrupt</p>

<p>DPC, StartIo, Interrupt</p>

<p> Interrupt (when <b>SynchronizationModel</b> member of <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> is not set to <b>StorSynchronizeHalfDuplex</b>)</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_storportspinlock">StorPortSpinLock</a>, <a href="devtest.storport_storportspinlock3">StorPortSpinLock3</a>, <a href="devtest.storport_storportspinlock4">StorPortSpinLock4</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\storport\ne-storport--stor-spinlock.md">STOR_SPINLOCK</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportreleasespinlock.md">StorPortReleaseSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortAcquireSpinLock routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
