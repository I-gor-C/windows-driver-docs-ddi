---
UID: NF.wdm.PsCreateSystemThread
title: PsCreateSystemThread
author: windows-driver-content
description: The PsCreateSystemThread routine creates a system thread that executes in kernel mode and returns a handle for the thread.
old-location: kernel\pscreatesystemthread.htm
old-project: kernel
ms.assetid: 4f6bfae4-8515-4fc4-aab3-9e16dbeda6da
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsCreateSystemThread
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
req.alt-api: PsCreateSystemThread
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlPsPassive, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PsCreateSystemThread function



## -description
<p>The <b>PsCreateSystemThread</b> routine creates a system thread that executes in kernel mode and returns a handle for the thread.</p>


## -syntax

````
NTSTATUS PsCreateSystemThread(
  _Out_     PHANDLE            ThreadHandle,
  _In_      ULONG              DesiredAccess,
  _In_opt_  POBJECT_ATTRIBUTES ObjectAttributes,
  _In_opt_  HANDLE             ProcessHandle,
  _Out_opt_ PCLIENT_ID         ClientId,
  _In_      PKSTART_ROUTINE    StartRoutine,
  _In_opt_  PVOID              StartContext
);
````


## -parameters
<dl>

### -param ThreadHandle [out]

<dd>
<p>Points to a variable that will receive the handle. The driver must close the handle with <a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a> once the handle is no longer in use. This handle is a kernel handle for Windows Vista and later versions of Windows. In earlier versions of Windows, the handle might not be a kernel handle.</p>
</dd>

### -param DesiredAccess [in]

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that represents the requested types of access to the created thread.</p>
</dd>

### -param ObjectAttributes [in, optional]

<dd>
<p>Points to a structure that specifies the object's attributes. OBJ_PERMANENT, OBJ_EXCLUSIVE, and OBJ_OPENIF are not valid attributes for a thread object. On Windows XP and later versions of Windows, if the caller is not running in the system process context, it must set the OBJ_KERNEL_HANDLE attribute for <i>ObjectAttributes</i>. Drivers for Microsoft Windows 2000 and Windows 98/Me must only call <b>PsCreateSystemThread</b> from the system process context. For Windows Vista and later versions of Windows, the handle will be a kernel handle.</p>
</dd>

### -param ProcessHandle [in, optional]

<dd>
<p>Specifies an open handle for the process in whose address space the thread is to be run. The caller's thread must have PROCESS_CREATE_THREAD access to this process. If this parameter is not supplied, the thread will be created in the initial system process. This value should be <b>NULL</b> for a driver-created thread. Use the <b>NtCurrentProcess</b> macro, defined in Ntddk.h, to specify the current process.</p>
</dd>

### -param ClientId [out, optional]

<dd>
<p>Points to a structure that receives the client identifier of the new thread. This value should be <b>NULL</b> for a driver-created thread.</p>
</dd>

### -param StartRoutine [in]

<dd>
<p>The entry point for the newly created system thread. This parameter is a function pointer to a <a href="kernel.threadstart">ThreadStart</a> routine that receives a single argument, which is the <i>StartContext</i> parameter value supplied by the caller.</p>
</dd>

### -param StartContext [in, optional]

<dd>
<p>Supplies a single argument that is passed to the thread when it begins execution.</p>
</dd>
</dl>

## -returns
<p><b>PsCreateSystemThread</b> returns STATUS_SUCCESS if the thread was created.</p>

## -remarks
<p>Drivers that create device-dedicated threads call this routine, either when they initialize or when I/O requests begin to come in to such a driver's Dispatch routines. For example, a driver might create such a thread when it receives an asynchronous device control request.</p>

<p><b>PsCreateSystemThread</b> creates a kernel-mode thread that begins a separate thread of execution within the system. Such a system thread has no TEB or user-mode context and runs only in kernel mode.</p>

<p>If the input <i>ProcessHandle</i> is <b>NULL</b>, the created thread is associated with the system process. Such a thread continues running until either the system is shut down or the thread terminates itself by calling <b>PsTerminateSystemThread</b>.</p>

<p>Starting with Windows XP, driver routines that run in a process context other than that of the system process must set the OBJ_KERNEL_HANDLE attribute for the <i>ObjectAttributes</i> parameter of <b>PsCreateSystemThread</b>. This restricts the use of the handle returned by <b>PsCreateSystemThread</b> to processes running in kernel mode. Otherwise, the thread handle can be accessed by the process in whose context the driver is running. Drivers can set the OBJ_KERNEL_HANDLE attribute as follows.</p>

<p>Drivers for Windows 2000 and Windows 98/Me must call <b>PsCreateSystemThread</b> only from the system process context.</p>

<p>For more information about the <i>StartContext</i> parameter, see <a href="kernel.threadstart">ThreadStart</a>.</p>

<p> The newly created system thread runs at PASSIVE_LEVEL inside a critical region with <a href="https://msdn.microsoft.com/74ed953c-1b2a-40b9-9df3-16869b198b38">normal kernel APCs</a> disabled.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlpspassive">IrqlPsPassive</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-kesetbaseprioritythread.md">KeSetBasePriorityThread</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kesetprioritythread.md">KeSetPriorityThread</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-psterminatesystemthread.md">PsTerminateSystemThread</a>
</dt>
<dt>
<a href="kernel.threadstart">ThreadStart</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-zwsetinformationthread.md">ZwSetInformationThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsCreateSystemThread routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
