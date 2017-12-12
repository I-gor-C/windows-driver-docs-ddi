---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlNotifyVolumeEventEx~r2
title: FsRtlNotifyVolumeEventEx function
author: windows-driver-content
description: The FsRtlNotifyVolumeEventEx routine notifies any registered applications that a volume event is occurring. Volume events include the volume being locked, unlocked, mounted, or made read-only.
old-location: ifsk\fsrtlnotifyvolumeeventex.htm
old-project: ifsk
ms.assetid: 0792e139-0217-4882-b2df-e69452118fc9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlNotifyVolumeEventEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later version of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlNotifyVolumeEventEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=DISPATCH_LEVEL
---

# FsRtlNotifyVolumeEventEx function



## -description
The <b>FsRtlNotifyVolumeEventEx</b> routine notifies any registered applications that a volume event is occurring. Volume events include the volume  being locked, unlocked, mounted, or made read-only. 



## -syntax

````
NTSTATUS FsRtlNotifyVolumeEventEx(
  _In_ PFILE_OBJECT                       FileObject,
  _In_ ULONG                              EventCode,
  _In_ PTARGET_DEVICE_CUSTOM_NOTIFICATION Event
);
````


## -parameters

### -param FileObject [in]

A pointer to a <a href="kernel.file_object">FILE_OBJECT</a> that specifies a volume.


### -param EventCode [in]

An event code for the event that is occurring. For a table of event codes, see <a href="ifsk.fsrtlnotifyvolumeevent">FsRtlNotifyVolumeEvent</a>.


### -param Event [in]

A pointer to the initialized custom notification structure (<a href="kernel.target_device_custom_notification">TARGET_DEVICE_CUSTOM_NOTIFICATION</a>) to use. 


## -returns
Returns STATUS_SUCCESS on success or another relevant NTSTATUS value, such as STATUS_INVALID_PARAMETER, if the <i>EventCode</i> is not valid.


## -remarks
<p class="note">Version to 1. 
<p class="note"><i>FileObject</i> to <b>NULL</b>.


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
Available in Windows Vista and later version of the Windows operating system.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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
&lt;=DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtlnotifyvolumeevent">FsRtlNotifyVolumeEvent</a>
</dt>
<dt>
<a href="kernel.ioregisterplugplaynotification">IoRegisterPlugPlayNotification</a>
</dt>
<dt>
<a href="kernel.iounregisterplugplaynotification">IoUnregisterPlugPlayNotification</a>
</dt>
<dt>
<a href="kernel.target_device_custom_notification">TARGET_DEVICE_CUSTOM_NOTIFICATION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlNotifyVolumeEventEx routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

