---
UID : NF:fltkernel.FltQueryVolumeInformationFile
title : FltQueryVolumeInformationFile function
author : windows-driver-content
description : FltQueryVolumeInformationFile retrieves volume information for a given file, directory, storage device, or volume.
old-location : ifsk\fltqueryvolumeinformationfile.htm
old-project : ifsk
ms.assetid : 3f93ce0a-f1f0-4b5b-aaf3-ce6698eb5055
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : FltQueryVolumeInformationFile
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : fltkernel.h
req.include-header : Fltkernel.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FltQueryVolumeInformationFile
req.alt-loc : fltmgr.sys
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : FltMgr.lib
req.dll : Fltmgr.sys
req.irql : PASSIVE_LEVEL
req.typenames : EXpsFontRestriction
---


# FltQueryVolumeInformationFile function
<b>FltQueryVolumeInformationFile</b> retrieves volume information for a given file, directory, storage device, or volume.

## Syntax

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

## Parameters

`Instance`

Opaque instance pointer for the caller. This parameter is required and cannot be <b>NULL</b>.

`FileObject`

File object pointer for an open file, directory, storage device, or volume. This parameter is required and cannot be <b>NULL</b>.

`FsInformation`

Pointer to a caller-allocated buffer that receives information about the file. The <i>FsInformationClass</i> parameter specifies the type of information. This parameter is required and cannot be <b>NULL</b>.

`Length`

Size, in bytes, of the <i>FsInformation</i> buffer.

`FsInformationClass`

Type of volume information to be returned. One of the following:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

`LengthReturned`

Pointer to a caller-allocated variable that receives the size, in bytes, of the information returned in the <i>FsInformation</i> buffer. This parameter is optional and can be <b>NULL</b>.


## Return Value

<b>FltQueryVolumeInformationFile</b> returns <b>STATUS_SUCCESS</b> or an appropriate <b>NTSTATUS</b> value such as the following: 
<dl>
<dt><b>STATUS_VOLUME_DISMOUNTED</b></dt>
</dl>The volume is not currently mounted. This is an error code.

## Remarks

<b>FltQueryVolumeInformationFile</b> retrieves volume information for a given file, directory, storage device, or volume. 

If the <i>FileObject</i> represents a direct device open, only <i>FileFsDeviceInformation</i> can be specified as the value of <i>FsInformationClass</i>. 

<b>FltQueryVolumeInformationFile</b> returns zero in any member of a FILE_FS_<i>XXX</i>_INFORMATION structure that is not supported by a particular file system.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fltkernel.h (include Fltkernel.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ntifs\ns-ntifs-_file_fs_attribute_information.md">FILE_FS_ATTRIBUTE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs-_file_fs_control_information.md">FILE_FS_CONTROL_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm-_file_fs_device_information.md">FILE_FS_DEVICE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs-_file_fs_driver_path_information.md">FILE_FS_DRIVER_PATH_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_file_fs_full_size_information.md">FILE_FS_FULL_SIZE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_file_fs_objectid_information.md">FILE_FS_OBJECTID_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_file_fs_size_information.md">FILE_FS_SIZE_INFORMATION</a>
</dt>
<dt><b>FILE_FS_SECTOR_SIZE_INFORMATION</b></dt>
<dt>
<a href="..\ntddk\ns-ntddk-_file_fs_volume_information.md">FILE_FS_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetinformationfile.md">FltSetInformationFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltQueryVolumeInformationFile function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>