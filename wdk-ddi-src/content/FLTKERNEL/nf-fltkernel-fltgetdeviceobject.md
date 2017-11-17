---
UID: NF.fltkernel.FltGetDeviceObject
title: FltGetDeviceObject
author: windows-driver-content
description: The FltGetDeviceObject routine returns a pointer to the Filter Manager's volume device object (VDO) for a given volume.
old-location: ifsk\fltgetdeviceobject.htm
ms.assetid: 1351efd1-1f7f-4f4b-b0ce-d9f08fba6613
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetDeviceObject
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fltmgr.lib
req.dll: Fltmgr.sys
req.irql: <= DISPATCH_LEVEL
ms.keywords: FltGetDeviceObject
req.iface: 
---

# FltGetDeviceObject function



## -description
<p>The <b>FltGetDeviceObject</b> routine returns a pointer to the Filter Manager's volume device object (VDO) for a given volume. </p>


## -syntax

````
NTSTATUS FltGetDeviceObject(
  _In_  PFLT_VOLUME    Volume,
  _Out_ PDEVICE_OBJECT *DeviceObject
);
````


## -parameters
<dl>

### -param <i>Volume</i> [in]

<dd>
<p>Opaque pointer for the volume. </p>
</dd>

### -param <i>DeviceObject</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the volume device object pointer. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltGetDeviceObject</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_FLT_NO_DEVICE_OBJECT</b></dt>
</dl><p>The requested device object does not exist for the given volume. This is an error code. </p>

<p> </p>

## -remarks
<p><b>FltGetDeviceObject</b> returns a pointer to the Filter Manager's volume device object (VDO) for the given volume. </p>

<p>For more information about volume device objects, see <a href="ifsk.file_system_stacks">File System Stacks</a>. </p>

<p>The Filter Manager's VDO is not the same as the underlying storage driver's disk device object or the base file system's VDO. To get a pointer to the disk device object, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543013">FltGetDiskDeviceObject</a> on the volume specified in the <i>Volume</i> parameter. To get a pointer to the base file system's VDO, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548365">IoGetDeviceAttachmentBaseRef</a> on the <i>RetDeviceObject</i> returned by <b>FltGetDeviceObject</b>. </p>

<p>To get an opaque pointer for the corresponding volume for a given device object, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543197">FltGetVolumeFromDeviceObject</a>. </p>

<p><b>FltGetDeviceObject</b> increments the reference count on the returned device object pointer. When this pointer is no longer needed, the caller must decrement this reference count by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>. Thus every successful call to <b>FltGetDeviceObject</b> must be matched by a subsequent call to <b>ObDereferenceObject</b>. </p>

<p><b>FltGetDeviceObject</b> returns a pointer to the Filter Manager's volume device object (VDO) for the given volume. </p>

<p>For more information about volume device objects, see <a href="ifsk.file_system_stacks">File System Stacks</a>. </p>

<p>The Filter Manager's VDO is not the same as the underlying storage driver's disk device object or the base file system's VDO. To get a pointer to the disk device object, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543013">FltGetDiskDeviceObject</a> on the volume specified in the <i>Volume</i> parameter. To get a pointer to the base file system's VDO, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548365">IoGetDeviceAttachmentBaseRef</a> on the <i>RetDeviceObject</i> returned by <b>FltGetDeviceObject</b>. </p>

<p>To get an opaque pointer for the corresponding volume for a given device object, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543197">FltGetVolumeFromDeviceObject</a>. </p>

<p><b>FltGetDeviceObject</b> increments the reference count on the returned device object pointer. When this pointer is no longer needed, the caller must decrement this reference count by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>. Thus every successful call to <b>FltGetDeviceObject</b> must be matched by a subsequent call to <b>ObDereferenceObject</b>. </p>

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
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543013">FltGetDiskDeviceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543197">FltGetVolumeFromDeviceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548365">IoGetDeviceAttachmentBaseRef</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetDeviceObject routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
