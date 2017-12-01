---
UID: NF.wdm.ObReferenceObjectByPointerWithTag
title: ObReferenceObjectByPointerWithTag
author: windows-driver-content
description: The ObReferenceObjectByPointerWithTag routine increments the reference count of the specified object, and writes a four-byte tag value to the object to support object reference tracing.
old-location: kernel\obreferenceobjectbypointerwithtag.htm
old-project: kernel
ms.assetid: eaa730a8-8ee3-43a7-a18e-094fbac4ba60
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ObReferenceObjectByPointerWithTag
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
req.alt-api: ObReferenceObjectByPointerWithTag
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ObReferenceObjectByPointerWithTag function



## -description
<p>The <b>ObReferenceObjectByPointerWithTag</b> routine increments the reference count of the specified object, and writes a four-byte tag value to the object to support <a href="http://go.microsoft.com/fwlink/p/?linkid=153590">object reference tracing</a>.</p>


## -syntax

````
NTSTATUS ObReferenceObjectByPointerWithTag(
  _In_     PVOID           Object,
  _In_     ACCESS_MASK     DesiredAccess,
  _In_opt_ POBJECT_TYPE    ObjectType,
  _In_     KPROCESSOR_MODE AccessMode,
  _In_     ULONG           Tag
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>A pointer to the object. The caller obtains this pointer either when it creates the object, or from a previous call to the <a href="..\wdm\nf-wdm-obreferenceobjectbyhandlewithtag.md">ObReferenceObjectByHandleWithTag</a> routine after it opens the object.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>Specifies the types of access to the object that the caller requests. This parameter is a bitmask of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>. The interpretation of this field depends on the object type. Do not use any generic access rights.</p>
</dd>

### -param <i>ObjectType</i> [in, optional]

<dd>
<p>A pointer to an opaque structure that specifies the object type. This parameter points to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff558675">OBJECT_TYPE</a> structure. Set <i>ObjectType</i> to <b>NULL</b> or to one of the following pointer values, which are declared in the Wdm.h header file: <b>*ExEventObjectType</b>, <b>*ExSemaphoreObjectType</b>, <b>*IoFileObjectType</b>, <b>*PsProcessType</b>, <b>*PsThreadType</b>, <b>*SeTokenObjectType</b>, <b>*TmEnlistmentObjectType</b>, <b>*TmResourceManagerObjectType</b>, <b>*TmTransactionManagerObjectType</b>, or <b>*TmTransactionObjectType</b>. This parameter can be <b>NULL</b> if <i>AccessMode</i> is <b>KernelMode</b>. If <i>ObjectType</i> is not <b>NULL</b>, the routine verifies that the supplied object type matches the object type of the object that the <i>Handle</i> parameter specifies.</p>
</dd>

### -param <i>AccessMode</i> [in]

<dd>
<p>Indicates the access mode to use for the access check. Set this parameter to one of the following <b>MODE</b> enumeration values:</p>
<ul>
<li>
<p><b>UserMode</b></p>
</li>
<li>
<p><b>KernelMode</b></p>
</li>
</ul>
<p>Lower-level drivers should specify <b>KernelMode</b>.</p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>Specifies a four-byte, custom tag value. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><b>ObReferenceObjectByPointerWithTag</b> returns STATUS_SUCCESS if the call is successful. Possible error return values include the following:</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The <i>ObjectType</i> parameter specifies the wrong object type for the object that the <i>Object</i> parameter points to, or <i>ObjectType</i> is <b>NULL</b> but <i>AccessMode</i> is <b>UserMode</b>.</p>

<p> </p>

## -remarks
<p>This routine does access validation of the specified object. If access can be granted, the routine increments the object reference count. This increment prevents the object from being deleted while the caller uses the object. When the object is no longer needed, the caller should decrement the reference count by calling the <a href="..\wdm\nf-wdm-obdereferenceobjectwithtag.md">ObDereferenceObjectWithTag</a> or <a href="..\wdm\nf-wdm-obdereferenceobjectdeferdeletewithtag.md">ObDereferenceObjectDeferDeleteWithTag</a> routine.</p>

<p>For more information about object references, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554294">Life Cycle of an Object</a>.</p>

<p>The <a href="..\wdm\nf-wdm-obreferenceobjectbypointer.md">ObReferenceObjectByPointer</a> routine is similar to <b>ObReferenceObjectByPointerWithTag</b>, except that it does not enable the caller to write a custom tag to an object. In Windows 7 and later versions of Windows, <b>ObReferenceObjectByPointer</b> always writes a default tag value ('tlfD') to the object. A call to <b>ObReferenceObjectByPointer</b> has the same effect as a call to <b>ObReferenceObjectByPointerWithTag</b> that specifies <i>Tag</i> = 'tlfD'.</p>

<p>To view an object reference trace in the <a href="http://go.microsoft.com/fwlink/p/?linkid=153599">Windows debugging tools</a>, use the <a href="http://go.microsoft.com/fwlink/p/?linkid=153600">!obtrace</a> kernel-mode debugger extension. In Windows 7, the <a href="http://go.microsoft.com/fwlink/p/?linkid=153600">!obtrace</a> extension is enhanced to display object reference tags, if object reference tracing is enabled. By default, object reference tracing is turned off. Use the <a href="http://go.microsoft.com/fwlink/p/?linkid=153601">Global Flags Editor</a> (Gflags) to enable object reference tracing. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558668">Object Reference Tracing with Tags</a>.</p>

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
<p>Available in Windows 7 and later versions of the Windows operating system.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
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
<a href="..\wdm\nf-wdm-obreferenceobjectbypointer.md">ObReferenceObjectByPointer</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ObReferenceObjectByPointerWithTag routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
