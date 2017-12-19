---
UID: NF.wdm.TmRecoverTransactionManager
title: TmRecoverTransactionManager function
author: windows-driver-content
description: The TmRecoverTransactionManager routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream.
old-location: kernel\tmrecovertransactionmanager.htm
old-project: kernel
ms.assetid: 67b18170-a17f-44fd-a5ab-12bccf2082fe
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: TmRecoverTransactionManager
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later operating system versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TmRecoverTransactionManager
req.alt-loc: NtosKrnl.exe,Ext-MS-Win-ntos-tm-l1-1-0.dll,tm.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# TmRecoverTransactionManager function



## -description
The <b>TmRecoverTransactionManager</b> routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream.



## -syntax

````
NTSTATUS TmRecoverTransactionManager(
  _In_ PKTM           Tm,
  _In_ PLARGE_INTEGER TargetVirtualClock
);
````


## -parameters

### -param Tm [in]

A pointer to a <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a>. To obtain this pointer, your TPS component must call <a href="kernel.obreferenceobjectbyhandle">ObReferenceObjectByHandle</a> and supply the object handle that a previous call to <a href="kernel.zwcreatetransactionmanager">ZwCreateTransactionManager</a> or <a href="kernel.zwopentransactionmanager">ZwOpenTransactionManager</a> provided.


### -param TargetVirtualClock [in]

A pointer to a <a href="https://msdn.microsoft.com/de01b0f1-86b1-4e7d-af22-84dbbe3a3f83">virtual clock value</a>. This parameter is optional and can be <b>NULL</b>. For more information about this parameter, see the following Remarks section. For Windows Vista, this parameter must be <b>NULL</b>.


## -returns
<b>TmRecoverTransactionManager</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: 
<dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl>For Windows Vista, the caller specified a non-<b>NULL</b> value for the <i>TargetVirtualClock</i> parameter. 
<dl>
<dt><b>STATUS_TM_VOLATILE</b></dt>
</dl>The specified transaction manager object does not have a log file, so recovery is not available.
<dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl>The specified transaction manager object is in an unexpected state.

 

The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.


## -remarks
The <b>TmRecoverTransactionManager</b> routine is a pointer-based version of the <a href="kernel.zwrecovertransactionmanager">ZwRecoverTransactionManager</a> routine.

Calling <b>TmRecoverTransactionManager</b> with a <i>TargetVirtualClock</i> parameter value of <b>NULL</b> is functionally equivalent to calling <b>ZwRecoverTransactionManager</b>. Calling <b>TmRecoverTransactionManager</b> with a non-<b>NULL</b> <i>TargetVirtualClock</i> parameter value is functionally equivalent to calling <a href="kernel.zwrollforwardtransactionmanager">ZwRollforwardTransactionManager</a>. 

For more information about recovery operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546922">Handling Recovery Operations</a>.

For information about when to use KTM's <b>Tm<i>Xxx</i></b> routines instead of <b>Zw<i>Xxx</i></b> routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565567">Using TmXxx Routines</a>.


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
Available in Windows Vista and later operating system versions.

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
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.zwrecovertransactionmanager">ZwRecoverTransactionManager</a>
</dt>
<dt>
<a href="kernel.zwrollforwardtransactionmanager">ZwRollforwardTransactionManager</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TmRecoverTransactionManager routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

