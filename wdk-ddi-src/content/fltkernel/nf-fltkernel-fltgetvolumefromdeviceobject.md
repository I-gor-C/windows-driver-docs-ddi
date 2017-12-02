---
UID: NF.fltkernel.FltGetVolumeFromDeviceObject
title: FltGetVolumeFromDeviceObject
author: windows-driver-content
description: The FltGetVolumeFromDeviceObject routine returns an opaque pointer for the volume represented by a volume device object (VDO).
old-location: ifsk\fltgetvolumefromdeviceobject.htm
old-project: ifsk
ms.assetid: 49dc5866-d793-41a7-9d9e-e89eea6f2f28
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltGetVolumeFromDeviceObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetVolumeFromDeviceObject
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltGetVolumeFromDeviceObject function



## -description
<p>The <b>FltGetVolumeFromDeviceObject</b> routine returns an opaque pointer for the volume represented by a volume device object (VDO). </p>


## -syntax

````
NTSTATUS FltGetVolumeFromDeviceObject(
  _In_  PFLT_FILTER    Filter,
  _In_  PDEVICE_OBJECT DeviceObject,
  _Out_ PFLT_VOLUME    *RetVolume
);
````


## -parameters
<dl>

### -param Filter [in]

<dd>
<p>Opaque filter pointer for the caller. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param DeviceObject [in]

<dd>
<p>Pointer to the volume device object. </p>
</dd>

### -param RetVolume [out]

<dd>
<p>Pointer to a caller-allocated variable that receives an opaque pointer for the volume. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltGetVolumeFromDeviceObject</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The volume is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Volume device object specified in the <i>DeviceObject</i> parameter was not a valid volume device object pointer, or no matching volume was found. This is an error code. </p>

<p> </p>

## -remarks
<p>The <i>DeviceObject</i> parameter can be a pointer to a filter or a file system volume device object (VDO). If it points to a storage device object, <b>FltGetVolumeFromDeviceObject</b> returns STATUS_INVALID_PARAMETER. </p>

<p>For more information about volume device objects, see <a href="ifsk.file_system_stacks">File System Stacks</a>. </p>

<p><b>FltGetVolumeFromDeviceObject</b> adds a rundown reference to the opaque volume pointer returned in the <i>RetVolume</i> parameter. When this pointer is no longer needed, the caller must release it by calling <a href="..\fltkernel\nf-fltkernel-fltobjectdereference.md">FltObjectDereference</a>. Thus every successful call to <b>FltGetVolumeFromDeviceObject</b> must be matched by a subsequent call to <b>FltObjectDereference</b>. </p>

<p>To get a pointer to the device object for a given volume, call <a href="..\fltkernel\nf-fltkernel-fltgetdeviceobject.md">FltGetDeviceObject</a>. </p>

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
<dt>FltMgr.lib</dt>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetdeviceobject.md">FltGetDeviceObject</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetdiskdeviceobject.md">FltGetDiskDeviceObject</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltobjectdereference.md">FltObjectDereference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetVolumeFromDeviceObject routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
