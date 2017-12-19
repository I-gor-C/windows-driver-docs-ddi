---
UID: NF.ntifs.ZwSetVolumeInformationFile
title: ZwSetVolumeInformationFile function
author: windows-driver-content
description: The ZwSetVolumeInformationFile routine modifies information about the volume associated with a given file, directory, storage device, or volume.
old-location: kernel\zwsetvolumeinformationfile.htm
old-project: kernel
ms.assetid: 6afc3e8b-0be0-4728-b00f-deea5e60d27e
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: ZwSetVolumeInformationFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Server 2003 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwSetVolumeInformationFile,NtSetInformationFile
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
---

# ZwSetVolumeInformationFile function



## -description
The <b>ZwSetVolumeInformationFile</b> routine modifies information about the volume associated with a given file, directory, storage device, or volume. 



## -syntax

````
NTSTATUS ZwSetVolumeInformationFile(
  _In_  HANDLE               FileHandle,
  _Out_ PIO_STATUS_BLOCK     IoStatusBlock,
  _In_  PVOID                FsInformation,
  _In_  ULONG                Length,
  _In_  FS_INFORMATION_CLASS FsInformationClass
);
````


## -parameters

### -param FileHandle [in]

Handle to a file object for an open file, directory, storage device, or volume whose volume information is to be modified. 


### -param IoStatusBlock [out]

Pointer to an <a href="kernel.io_status_block">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the operation. 


### -param FsInformation [in]

Pointer to a caller-allocated buffer containing the volume information to be modified. The structure of the information in this buffer depends on the value of <i>FsInformationClass</i>, as shown in the following table. 


### -param Length [in]

Size in bytes of the buffer pointed to by <i>FsInformation</i>. The caller should set this parameter according to the given <i>FsInformationClass</i>. 


### -param FsInformationClass [in]

Type of volume information to be set. One of the following: 

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<b>FileFsControlInformation</b>

</td>
<td>
Set <a href="ifsk.file_fs_control_information">FILE_FS_CONTROL_INFORMATION</a> for the volume. 

</td>
</tr>
<tr>
<td>
<b>FileFsLabelInformation</b>

</td>
<td>
Set <a href="ifsk.file_fs_label_information">FILE_FS_LABEL_INFORMATION</a> for the volume. 

</td>
</tr>
<tr>
<td>
<b>FileFsObjectIdInformation</b>

</td>
<td>
Set <a href="ifsk.file_fs_objectid_information">FILE_FS_OBJECTID_INFORMATION</a> for the volume. 

</td>
</tr>
</table>
 


## -returns
<b>ZwSetVolumeInformationFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:
<dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl>An invalid value was specified for <i>Length</i>. This is an error code.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
<a href="kernel.zwsetvolumeinformationfile">ZwSetVolumeInformationFile</a> encountered a pool allocation failure. This is an error code.
<dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl>An invalid value was specified for <i>FsInformationClass</i>. This is an error code.

 


## -remarks
To query volume information, call <a href="kernel.zwqueryvolumeinformationfile">ZwQueryVolumeInformationFile</a>. 

To change information about a file, call <b>ZwSetVolumeInformationFile</b>. 

Minifilters should use <a href="ifsk.fltsetinformationfile">FltSetInformationFile</a> instead of <b>ZwSetVolumeInformationFile</b>. 

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
Available in Windows Server 2003 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<a href="ifsk.file_fs_control_information">FILE_FS_CONTROL_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_fs_label_information">FILE_FS_LABEL_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_fs_objectid_information">FILE_FS_OBJECTID_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.fltsetinformationfile">FltSetInformationFile</a>
</dt>
<dt>
<a href="ifsk.irp_mj_set_volume_information">IRP_MJ_SET_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="kernel.zwqueryvolumeinformationfile">ZwQueryVolumeInformationFile</a>
</dt>
<dt>
<a href="kernel.zwsetinformationfile">ZwSetInformationFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwSetVolumeInformationFile routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

