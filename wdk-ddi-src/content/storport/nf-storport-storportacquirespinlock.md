---
UID: NF.storport.StorPortAcquireSpinLock
title: StorPortAcquireSpinLock function
author: windows-driver-content
description: The StorPortAcquireSpinLock routine acquires the specified spin lock.
old-location: storage\storportacquirespinlock.htm
old-project: storage
ms.assetid: 52a877c7-b274-4bec-b948-edb0585a09e1
ms.author: windowsdriverdev
ms.date: 12/8/2017
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
req.product: Windows 10 or later.
---

# StorPortAcquireSpinLock function



## -description
The <b>StorPortAcquireSpinLock</b> routine acquires the specified spin lock. 



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

### -param DeviceExtension [in]

A pointer to the miniport driver per-adapter device extension. 


### -param SpinLock [in]

Contains an enumerator value of type <a href="storage.stor_spinlock">STOR_SPINLOCK</a> that specifies the spin lock to acquire. 


### -param LockContext [in]

A pointer to the DPC object for which the lock is held if <i>SpinLock</i> indicates a type of <b>DpcLock</b>. This member should be <b>NULL</b> if <i>SpinLock </i>indicates a type of either <b>InterruptLock</b> or <b>StartIoLock</b>. 


### -param LockHandle [in, out]

A pointer to a buffer that, on return, will contain a lock handle. To release the lock, the caller must pass this handle to the <a href="storage.storportreleasespinlock">StorPortReleaseSpinLock</a> routine. 


## -returns
None


## -remarks
Miniport drivers must ensure that they do not attempt to acquire a lock that is already held or acquire locks in an incorrect order. Either of these mistakes will result in system deadlock.

Certain locks are held automatically by the port driver before it calls the miniport driver callback routines. For each miniport driver callback routine, the following table indicates which locks the port driver acquires automatically before calling the callback routine.


<a href="storage.hwstorfindadapter">HwStorFindAdapter</a>


None


<a href="storage.hwstorinitialize">HwStorInitialize</a>


Interrupt (physical miniports), None (virtual miniports)


<a href="storage.hwstorinterrupt">HwStorInterrupt</a>


Interrupt


<a href="storage.hwmsinterruptroutine">HwMSIInterruptRoutine</a>



<a href="storage.hwstorstartio">
        HwStorStartIo</a>


StartIo (physical miniports only when requested concurrent channels &lt;= 1)


<a href="storage.hwstorbuildio">HwStorBuildIo</a>



<a href="storage.hwstortimer">HwStorTimer</a>


 Startio, Interrupt (when <b>SynchronizationModel</b> member of <a href="storage.port_configuration_information__storport_">PORT_CONFIGURATION_INFORMATION</a> is set to <b>StorSynchronizeHalfDuplex</b>)


<a href="storage.hwstorresetbus">HwStorResetBus</a>



<a href="storage.hwstoradaptercontrol">HwStorAdapterControl</a>



<a href="storage.hwstorunitcontrol">HwStorUnitControl</a>



<a href="storage.hwstortracingenabled">HwStorTracingEnabled</a>



<a href="storage.hwstorpassiveinitializeroutine">HwStorPassiveInitializeRoutine</a>



<a href="storage.hwstordpcroutine">HwStorDpcRoutine</a>



<a href="storage.hwstordpcroutine">HwStorStateChange</a>


The locks held by the port driver influence which locks the callback routines are allowed to acquire, because spin locks must be acquired in the following order:

DPC or StartIo

For instance, if the port driver acquires the <i>Interrupt</i> spin lock before calling a callback routine, that callback routine can no longer acquire the <i>DPC</i> or <i>StartIo</i> spin lock because the <i>DPC</i> and <i>StartIo</i> spin locks are of a lower order than the <i>Interrupt</i> spin lock. On the other hand, if the port driver acquires the <i>StartIo</i> spin lock before calling a callback routine, that callback routine, when executed, could still acquire an  <i>Interrupt</i> or a <i>DPC</i> spin lock.

The following table indicates which spin locks each miniport driver routine can acquire. In those cases where the miniport driver routine must obtain both the <i>StartIo</i> spin lock and the <i>Interrupt</i> spin lock, the routine must always acquire the <i>StartIo</i> spin lock first.

DPC, Interrupt

DPC, StartIo, Interrupt

 Interrupt (when <b>SynchronizationModel</b> member of <a href="storage.port_configuration_information__storport_">PORT_CONFIGURATION_INFORMATION</a> is not set to <b>StorSynchronizeHalfDuplex</b>)


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
Header

</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.storport_storportspinlock">StorPortSpinLock</a>, <a href="devtest.storport_storportspinlock3">StorPortSpinLock3</a>, <a href="devtest.storport_storportspinlock4">StorPortSpinLock4</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.stor_spinlock">STOR_SPINLOCK</a>
</dt>
<dt>
<a href="storage.storportreleasespinlock">StorPortReleaseSpinLock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortAcquireSpinLock routine%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

