---
UID: NF.wdm.ObReferenceObjectByHandleWithTag
title: ObReferenceObjectByHandleWithTag
author: windows-driver-content
description: The ObReferenceObjectByHandleWithTag routine increments the reference count of the object that is identified by the specified handle, and writes a four-byte tag value to the object to support object reference tracing.
old-location: kernel\obreferenceobjectbyhandlewithtag.htm
old-project: kernel
ms.assetid: f36beac8-e4fb-49ce-b49d-a1a8f32f19a5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ObReferenceObjectByHandleWithTag
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ObReferenceObjectByHandleWithTag
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: HwStorPortProhibitedDDIs
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

# ObReferenceObjectByHandleWithTag function



## -description
<p>The <b>ObReferenceObjectByHandleWithTag</b> routine increments the reference count of the object that is identified by the specified handle, and writes a four-byte tag value to the object to support <a href="http://go.microsoft.com/fwlink/p/?linkid=153590">object reference tracing</a>. </p>


## -syntax

````
NTSTATUS ObReferenceObjectByHandleWithTag(
  _In_      HANDLE                     Handle,
  _In_      ACCESS_MASK                DesiredAccess,
  _In_opt_  POBJECT_TYPE               ObjectType,
  _In_      KPROCESSOR_MODE            AccessMode,
  _In_      ULONG                      Tag,
  _Out_     PVOID                      *Object,
  _Out_opt_ POBJECT_HANDLE_INFORMATION HandleInformation
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies an open handle for an object. </p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>Specifies the types of access to the object that the caller requests. This parameter is a bitmask of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>. The interpretation of this field depends on the object type. Do not use any generic access rights. </p>
</dd>

### -param <i>ObjectType</i> [in, optional]

<dd>
<p>A pointer to an opaque structure that specifies the object type. This parameter points to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff558675">OBJECT_TYPE</a> structure. Set <i>ObjectType</i> to <b>NULL</b> or to one of the following pointer values, which are declared in the Wdm.h header file: <b>*ExEventObjectType</b>, <b>*ExSemaphoreObjectType</b>, <b>*IoFileObjectType</b>, <b>*PsProcessType</b>, <b>*PsThreadType</b>, <b>*SeTokenObjectType</b>, <b>*TmEnlistmentObjectType</b>, <b>*TmResourceManagerObjectType</b>, <b>*TmTransactionManagerObjectType</b>, or <b>*TmTransactionObjectType</b>. If <i>ObjectType</i> is not <b>NULL</b>, the routine verifies that the supplied object type matches the object type of the object that the <i>Handle</i> parameter specifies. </p>
</dd>

### -param <i>AccessMode</i> [in]

<dd>
<p>Specifies the access mode to use for the access check. It must be either <b>UserMode</b> or <b>KernelMode</b>. Drivers should always specify <b>UserMode</b> for handles they receive from user address space.</p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>Specifies a four-byte, custom tag value. For more information, see the following Remarks section.</p>
</dd>

### -param <i>Object</i> [out]

<dd>
<p>A pointer to a variable into which the routine writes a pointer to the object. The following table lists the <i>Object</i> pointer types that are designated by the possible <i>ObjectType</i> parameter values.</p>
<table>
<tr>
<th><i>ObjectType</i> parameter</th>
<th><i>Object </i>pointer type</th>
</tr>
<tr>
<td>
<p><b>*ExEventObjectType</b></p>
</td>
<td>
<p>PKEVENT</p>
</td>
</tr>
<tr>
<td>
<p><b>*ExSemaphoreObjectType</b></p>
</td>
<td>
<p>PKSEMAPHORE</p>
</td>
</tr>
<tr>
<td>
<p><b>*IoFileObjectType</b></p>
</td>
<td>
<p>PFILE_OBJECT</p>
</td>
</tr>
<tr>
<td>
<p><b>*PsProcessType</b></p>
</td>
<td>
<p>PEPROCESS or PKPROCESS</p>
</td>
</tr>
<tr>
<td>
<p><b>*PsThreadType</b></p>
</td>
<td>
<p>PETHREAD or PKTHREAD</p>
</td>
</tr>
<tr>
<td>
<p><b>*SeTokenObjectType</b></p>
</td>
<td>
<p>PACCESS_TOKEN</p>
</td>
</tr>
<tr>
<td>
<p><b>*TmEnlistmentObjectType</b></p>
</td>
<td>
<p>PKENLISTMENT</p>
</td>
</tr>
<tr>
<td>
<p><b>*TmResourceManagerObjectType</b></p>
</td>
<td>
<p>PKRESOURCEMANAGER</p>
</td>
</tr>
<tr>
<td>
<p><b>*TmTransactionManagerObjectType</b></p>
</td>
<td>
<p>PKTM</p>
</td>
</tr>
<tr>
<td>
<p><b>*TmTransactionObjectType</b></p>
</td>
<td>
<p>PKTRANSACTION</p>
</td>
</tr>
</table>
<p> </p>
<p>The structures that the pointer types reference are opaque, and drivers cannot access the structure members. Because the structures are opaque, PEPROCESS is equivalent to PKPROCESS, and PETHREAD is equivalent to PKTHREAD. </p>
</dd>

### -param <i>HandleInformation</i> [out, optional]

<dd>
<p>Drivers set this parameter to <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>ObReferenceObjectByHandleWithTag</b> returns STATUS_SUCCESS if the call is successful. Possible error return values include the following:</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The <i>ObjectType</i> parameter specifies the wrong object type for the object that is identified by the <i>Handle</i> parameter. </p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller does not have the required access rights to the object. </p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>The specified handle is not valid. </p>

<p> </p>

## -remarks
<p>This routine does access validation of the specified object handle. If access can be granted, the routine increments the object reference count and provides an object pointer to the caller. This increment prevents the object from being deleted while the caller uses the object. When the object is no longer needed, the caller should decrement the reference count by calling the <a href="..\wdm\nf-wdm-obdereferenceobjectwithtag.md">ObDereferenceObjectWithTag</a> or <a href="..\wdm\nf-wdm-obdereferenceobjectdeferdeletewithtag.md">ObDereferenceObjectDeferDeleteWithTag</a> routine.</p>

<p>For more information about object references, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554294">Life Cycle of an Object</a>.</p>

<p><b>ObReferenceObjectByHandleWithTag</b> does not close or invalidate the object handle that is specified by the <i>Handle</i> parameter. When the handle is no longer needed, the caller can close the handle by calling the <a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a> routine.</p>

<p>If the <i>AccessMode</i> parameter value is <b>KernelMode</b>, the requested access is always allowed. If <i>AccessMode</i> is <b>UserMode</b>, the requested access is compared to the access rights that the caller has to the object. Only highest-level drivers can safely specify the <b>UserMode</b> value for the <i>AccessMode</i> parameter.</p>

<p>Starting with Windows 7, if <i>AccessMode</i> is <b>KernelMode</b> and handle is received from user address space, <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> issues bugcheck C4, subcode F6.</p>

<p>The <a href="..\wdm\nf-wdm-obreferenceobjectbyhandle.md">ObReferenceObjectByHandle</a> routine is similar to <b>ObReferenceObjectByHandleWithTag</b>, except that it does not enable the caller to write a custom tag to an object. In Windows 7 and later versions of Windows, <b>ObReferenceObjectByHandle</b> always writes a default tag value ('tlfD') to the object. A call to <b>ObReferenceObjectByHandle</b> has the same effect as a call to <b>ObReferenceObjectByHandleWithTag</b> that specifies <i>Tag</i> = 'tlfD'.</p>

<p>To view an object reference trace in the <a href="http://go.microsoft.com/fwlink/p/?linkid=153599">Windows debugging tools</a>, use the <a href="http://go.microsoft.com/fwlink/p/?linkid=153600">!obtrace</a> kernel-mode debugger extension. In Windows 7, the <a href="http://go.microsoft.com/fwlink/p/?linkid=153600">!obtrace</a> extension is enhanced to display object reference tags, if object reference tracing is enabled. By default, object reference tracing is turned off. Use the <a href="http://go.microsoft.com/fwlink/p/?linkid=153601">Global Flags Editor</a> (Gflags) to enable object reference tracing. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558668">Object Reference Tracing with Tags</a>. </p>

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
<p>Available in Windows 7 and later versions of the Windows operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
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
<a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obdereferenceobjectdeferdeletewithtag.md">ObDereferenceObjectDeferDeleteWithTag</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obdereferenceobjectwithtag.md">ObDereferenceObjectWithTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558675">OBJECT_TYPE</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obreferenceobjectbyhandle.md">ObReferenceObjectByHandle</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ObReferenceObjectByHandleWithTag routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
