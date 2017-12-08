---
UID: NC.fltkernel.PFLT_INSTANCE_SETUP_CALLBACK
title: PFLT_INSTANCE_SETUP_CALLBACK
author: windows-driver-content
description: A minifilter driver can register a routine of type PFLT_INSTANCE_SETUP_CALLBACK as the minifilter driver's InstanceSetupCallback routine.
old-location: ifsk\pflt_instance_setup_callback.htm
old-project: ifsk
ms.assetid: bbdd393d-3f0f-4bbd-8a74-ed75d20b0433
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: InstanceSetupCallback
req.alt-loc: fltkernel.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: IXpsPartIterator
---

# PFLT_INSTANCE_SETUP_CALLBACK callback



## -description
<p>A minifilter driver can register a routine of type PFLT_INSTANCE_SETUP_CALLBACK as the minifilter driver's <i>InstanceSetupCallback</i> routine. </p>


## -prototype

````
PFLT_INSTANCE_SETUP_CALLBACK InstanceSetupCallback;

NTSTATUS InstanceSetupCallback(
  _In_ PCFLT_RELATED_OBJECTS    FltObjects,
  _In_ FLT_INSTANCE_SETUP_FLAGS Flags,
  _In_ DEVICE_TYPE              VolumeDeviceType,
  _In_ FLT_FILESYSTEM_TYPE      VolumeFilesystemType
)
{ ... }
````


## -parameters
<dl>

### -param FltObjects [in]

<dd>
<p>Pointer to an <a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a> structure that contains opaque pointers for the objects related to the current operation. </p>
</dd>

### -param Flags [in]

<dd>
<p>Bitmask of flags that indicate why the instance is being attached. One or more of the following: </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_SETUP_AUTOMATIC_ATTACHMENT</p>
</td>
<td>
<p>The instance is being attached automatically. Either the minifilter driver was just loaded and is being attached to all existing volumes, or it is being attached to a newly mounted volume. </p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_SETUP_MANUAL_ATTACHMENT</p>
</td>
<td>
<p>The instance is being attached manually because a user-mode application has called <a href="ifsk.filterattach">FilterAttach</a> or <a href="ifsk.filterattachataltitude">FilterAttachAtAltitude</a> or because a kernel-mode component has called <a href="..\fltkernel\nf-fltkernel-fltattachvolume.md">FltAttachVolume</a> or <a href="..\fltkernel\nf-fltkernel-fltattachvolumeataltitude.md">FltAttachVolumeAtAltitude</a>. </p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_SETUP_NEWLY_MOUNTED_VOLUME</p>
</td>
<td>
<p>The instance is being attached automatically to a newly mounted volume. </p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_SETUP_DETACHED_VOLUME</p>
</td>
<td>
<p>The instance is being attached to a detached volume. It is possible, on some filesystems (such as FAT and CDFS), to reattach a volume after it has detached. A volume is detached if it has no associated storage stack. A volume in this state is usually a dismounted volume that still has open files.  </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param VolumeDeviceType [in]

<dd>
<p>Device type of the file system volume. Must be one of the following: </p>
<dl>
<dd>
<p>FILE_DEVICE_CD_ROM_FILE_SYSTEM</p>
</dd>
<dd>
<p>FILE_DEVICE_DISK_FILE_SYSTEM</p>
</dd>
<dd>
<p>FILE_DEVICE_NETWORK_FILE_SYSTEM</p>
</dd>
</dl>
</dd>

### -param VolumeFilesystemType [in]

<dd>
<p>File system type of the volume.   The possible values are listed in <a href="..\fltuserstructures\ne-fltuserstructures--flt-filesystem-type.md">FLT_FILESYSTEM_TYPE</a>.</p>
</dd>
</dl>

## -returns
<p>This callback routine returns STATUS_SUCCESS or an NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_FLT_DO_NOT_ATTACH</b></dt>
</dl><p>Returning this value prevents the minifilter driver instance from being attached to the given volume. This is an error code. </p>

<p> </p>

## -remarks
<p>When a minifilter driver registers itself by calling <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a> from its <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine, it can register a routine of type PFLT_INSTANCE_SETUP_CALLBACK as the minifilter driver's <i>InstanceSetupCallback</i> routine. </p>

<p>To register the<i> InstanceSetupCallback</i> routine, the minifilter driver stores the address of a routine of type PFLT_INSTANCE_SETUP_CALLBACK in the <b>InstanceSetupCallback</b> member of the <a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a> structure that the minifilter driver passes as the <i>Registration</i> parameter of <b>FltRegisterFilter</b>. </p>

<p>The filter manager calls this routine on the first operation after a new volume is mounted. </p>

<p>The filter manager calls this routine to allow the minifilter driver to respond to an automatic or manual attachment request. If this routine returns an error or warning NTSTATUS code, the minifilter driver instance is not attached to the given volume. Otherwise, the minifilter driver instance is attached to the given volume. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.filterattach">FilterAttach</a>
</dt>
<dt>
<a href="ifsk.filterattachataltitude">FilterAttachAtAltitude</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltattachvolume.md">FltAttachVolume</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltattachvolumeataltitude.md">FltAttachVolumeAtAltitude</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-query-teardown-callback.md">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_INSTANCE_SETUP_CALLBACK routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
