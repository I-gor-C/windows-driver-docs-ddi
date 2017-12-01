---
UID: NF.fltkernel.FltQueryVolumeInformationFile
title: FltQueryVolumeInformationFile
author: windows-driver-content
description: FltQueryVolumeInformationFile retrieves volume information for a given file, directory, storage device, or volume.
old-location: ifsk\fltqueryvolumeinformationfile.htm
old-project: ifsk
ms.assetid: 3f93ce0a-f1f0-4b5b-aaf3-ce6698eb5055
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltQueryVolumeInformationFile
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
req.alt-api: FltQueryVolumeInformationFile
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltQueryVolumeInformationFile function



## -description
<p><b>FltQueryVolumeInformationFile</b> retrieves volume information for a given file, directory, storage device, or volume. </p>


## -syntax

````
NTSTATUS FltQueryVolumeInformationFile(
  _In_      PFLT_INSTANCE        Instance,
  _In_      PFILE_OBJECT         FileObject,
  _Out_     PVOID                FsInformation,
  _In_      ULONG                Length,
  _In_      FS_INFORMATION_CLASS FsInformationClass,
  _Out_opt_ PULONG               LengthReturned
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the caller. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>File object pointer for an open file, directory, storage device, or volume. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>FsInformation</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives information about the file. The <i>FsInformationClass</i> parameter specifies the type of information. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Size, in bytes, of the <i>FsInformation</i> buffer. </p>
</dd>

### -param <i>FsInformationClass</i> [in]

<dd>
<p>Type of volume information to be returned. One of the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="FileFsAttributeInformation"></a><a id="filefsattributeinformation"></a><a id="FILEFSATTRIBUTEINFORMATION"></a><dl>

### -param <b>FileFsAttributeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\ntifs\ns-ntifs--file-fs-attribute-information.md">FILE_FS_ATTRIBUTE_INFORMATION</a> structure that contains attribute information about the file system responsible for the volume. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsControlInformation"></a><a id="filefscontrolinformation"></a><a id="FILEFSCONTROLINFORMATION"></a><dl>

### -param <b>FileFsControlInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\ntifs\ns-ntifs--file-fs-control-information.md">FILE_FS_CONTROL_INFORMATION</a> structure that contains file system control information about the volume. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsDeviceInformation"></a><a id="filefsdeviceinformation"></a><a id="FILEFSDEVICEINFORMATION"></a><dl>

### -param <b>FileFsDeviceInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\wdm\ns-wdm--file-fs-device-information.md">FILE_FS_DEVICE_INFORMATION</a> structure that contains device information for the volume. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsDriverPathInformation"></a><a id="filefsdriverpathinformation"></a><a id="FILEFSDRIVERPATHINFORMATION"></a><dl>

### -param <b>FileFsDriverPathInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\ntifs\ns-ntifs--file-fs-driver-path-information.md">FILE_FS_DRIVER_PATH_INFORMATION</a> structure that contains information about whether a specified driver is in the I/O path for the volume. The caller must store the name of the driver into the <b>FILE_FS_DRIVER_PATH_INFORMATION</b> structure before calling <b>FltQueryVolumeInformationFile</b>. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsFullSizeInformation"></a><a id="filefsfullsizeinformation"></a><a id="FILEFSFULLSIZEINFORMATION"></a><dl>

### -param <b>FileFsFullSizeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\ntddk\ns-ntddk--file-fs-full-size-information.md">FILE_FS_FULL_SIZE_INFORMATION</a> structure that contains information about the total amount of space available on the volume. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsObjectIdInformation"></a><a id="filefsobjectidinformation"></a><a id="FILEFSOBJECTIDINFORMATION"></a><dl>

### -param <b>FileFsObjectIdInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\ntddk\ns-ntddk--file-fs-objectid-information.md">FILE_FS_OBJECTID_INFORMATION</a> structure that contains file-system-specific object ID information for the volume. Note that this is not the same as the (GUID-based) unique volume name that is assigned by the operating system. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsSizeInformation"></a><a id="filefssizeinformation"></a><a id="FILEFSSIZEINFORMATION"></a><dl>

### -param <b>FileFsSizeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\ntddk\ns-ntddk--file-fs-size-information.md">FILE_FS_SIZE_INFORMATION</a> structure containing information about the amount of space on the volume that is available to the user that is associated with the calling thread. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsVolumeInformation"></a><a id="filefsvolumeinformation"></a><a id="FILEFSVOLUMEINFORMATION"></a><dl>

### -param <b>FileFsVolumeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\ntddk\ns-ntddk--file-fs-volume-information.md">FILE_FS_VOLUME_INFORMATION</a> that contains information about the volume such as the volume label, serial number, and creation time. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsSectorSizeInformation"></a><a id="filefssectorsizeinformation"></a><a id="FILEFSSECTORSIZEINFORMATION"></a><dl>

### -param <b>FileFsSectorSizeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="..\ntifs\ns-ntifs--file-fs-driver-path-information.md">FILE_FS_SECTOR_SIZE_INFORMATION</a> structure that contains information about the physical and logical sector sizes of a volume.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>LengthReturned</i> [out, optional]

<dd>
<p>Pointer to a caller-allocated variable that receives the size, in bytes, of the information returned in the <i>FsInformation</i> buffer. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltQueryVolumeInformationFile</b> returns <b>STATUS_SUCCESS</b> or an appropriate <b>NTSTATUS</b> value such as the following: </p><dl>
<dt><b>STATUS_VOLUME_DISMOUNTED</b></dt>
</dl><p>The volume is not currently mounted. This is an error code. </p>

<p> </p>

## -remarks
<p><b>FltQueryVolumeInformationFile</b> retrieves volume information for a given file, directory, storage device, or volume. </p>

<p>If the <i>FileObject</i> represents a direct device open, only <i>FileFsDeviceInformation</i> can be specified as the value of <i>FsInformationClass</i>. </p>

<p><b>FltQueryVolumeInformationFile</b> returns zero in any member of a FILE_FS_<i>XXX</i>_INFORMATION structure that is not supported by a particular file system. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--file-fs-attribute-information.md">FILE_FS_ATTRIBUTE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-fs-control-information.md">FILE_FS_CONTROL_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--file-fs-device-information.md">FILE_FS_DEVICE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-fs-driver-path-information.md">FILE_FS_DRIVER_PATH_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-fs-full-size-information.md">FILE_FS_FULL_SIZE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-fs-objectid-information.md">FILE_FS_OBJECTID_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-fs-size-information.md">FILE_FS_SIZE_INFORMATION</a>
</dt>
<dt><b>FILE_FS_SECTOR_SIZE_INFORMATION</b></dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-fs-volume-information.md">FILE_FS_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetinformationfile.md">FltSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltQueryVolumeInformationFile function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
