---
UID: NF.wdm.ZwRollforwardTransactionManager
title: ZwRollforwardTransactionManager function
author: windows-driver-content
description: The ZwRollforwardTransactionManager routine initiates recovery operations for all of the in-progress transactions that are assigned to a specified transaction manager.
old-location: kernel\zwrollforwardtransactionmanager.htm
old-project: kernel
ms.assetid: c2d775b1-364a-4c50-bd5e-dab9d9e07b83
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: ZwRollforwardTransactionManager
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwRollforwardTransactionManager,NtRollforwardTransactionManager
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
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

# ZwRollforwardTransactionManager function



## -description
The <b>ZwRollforwardTransactionManager</b> routine initiates recovery operations for all of the in-progress transactions that are assigned to a specified transaction manager.


## -syntax

````
NTSTATUS ZwRollforwardTransactionManager(
  _In_     HANDLE         TransactionManagerHandle,
  _In_opt_ PLARGE_INTEGER TmVirtualClock
);
````


## -parameters

### -param TransactionManagerHandle [in]

A handle to a <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a> that was obtained by a previous call to <a href="kernel.zwcreatetransactionmanager">ZwCreateTransactionManager</a> or <a href="kernel.zwopentransactionmanager">ZwOpenTransactionManager</a>. The handle must have TRANSACTIONMANAGER_RECOVER access to the object.

### -param TmVirtualClock [in, optional]

A pointer to a <a href="https://msdn.microsoft.com/de01b0f1-86b1-4e7d-af22-84dbbe3a3f83">virtual clock value</a>. This parameter is optional and can be <b>NULL</b>. For more information about this parameter, see the following Remarks section.

## -returns
<b>ZwRollforwardTransactionManager</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values:
<dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl>The specified handle is not a handle to a transaction manager object.
<dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl>An object handle is invalid.
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>The caller does not have appropriate access to the transaction manager object.
<dl>
<dt><b>STATUS_TM_VOLATILE</b></dt>
</dl>The specified transaction manager object does not have a log file, so recovery is not available.
<dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl>The specified transaction manager object is in an unexpected state.

 

The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

## -remarks
The <b>ZwRollforwardTransactionManager</b> routine recovers all logged activity that KTM finds in the transaction manager's log file, up to and including the virtual clock value that the <i>TmVirtualClock</i> parameter supplies. 

Your component can traverse the log file incrementally by calling <b>ZwRollforwardTransactionManager</b> repetitively and setting the <i>VirtualClock</i> parameter to a higher value before each call.

If the <i>TmVirtualClock</i> parameter is <b>NULL</b>, calling <b>ZwRollforwardTransactionManager</b> is equivalent to calling <a href="kernel.zwrecovertransactionmanager">ZwRecoverTransactionManager</a>. 

For more information about recovery operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546922">Handling Recovery Operations</a>.

<b>NtRollforwardTransactionManager</b> and <b>ZwRollforwardTransactionManager</b> are two versions of the same Windows Native System Services routine. The <b>NtRollforwardTransactionManager</b> routine in the Windows kernel is not directly accessible to kernel-mode drivers. However, kernel-mode drivers can access this routine indirectly by calling the <b>ZwRollforwardTransactionManager</b> routine.

For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.

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
Available in Windows Vista and later versions of Windows.
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
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.tmrecovertransactionmanager">TmRecoverTransactionManager</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="kernel.zwcreatetransactionmanager">ZwCreateTransactionManager</a>
</dt>
<dt>
<a href="kernel.zwopentransactionmanager">ZwOpenTransactionManager</a>
</dt>
<dt>
<a href="kernel.zwrecovertransactionmanager">ZwRecoverTransactionManager</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwRollforwardTransactionManager routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
