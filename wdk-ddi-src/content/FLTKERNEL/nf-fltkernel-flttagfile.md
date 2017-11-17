---
UID: NF.fltkernel.FltTagFile
title: FltTagFile
author: windows-driver-content
description: FltTagFile sets a reparse tag on a file or directory.
old-location: ifsk\flttagfile.htm
ms.assetid: fbc8b596-1299-4dfa-953b-5730905f0e30
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
req.alt-api: FltTagFile
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
ms.keywords: FltTagFile
req.iface: 
---

# FltTagFile function



## -description
<p><b>FltTagFile</b> sets a reparse tag on a file or directory. </p>


## -syntax

````
NTSTATUS FltTagFile(
  _In_     PFLT_INSTANCE InitiatingInstance,
  _In_     PFILE_OBJECT  FileObject,
  _In_     ULONG         FileTag,
  _In_opt_ GUID          *Guid,
  _In_     PVOID         DataBuffer,
  _In_     USHORT        DataBufferLength
);
````


## -parameters
<dl>

### -param <i>InitiatingInstance</i> [in]

<dd>
<p>Opaque instance pointer for the minifilter driver instance that initiated this I/O request. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to a file object for the file or directory on which to set a reparse point. The file object must be opened for FILE_WRITE_DATA access. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>FileTag</i> [in]

<dd>
<p>Reparse point tag. If an existing reparse tag is being modified, the tag specified in this parameter must match the tag of the reparse point to be modified. </p>
</dd>

### -param <i>Guid</i> [in, optional]

<dd>
<p>GUID that uniquely identifies the type of reparse point. If <i>FileTag</i> is not a Microsoft tag, this parameter is required and cannot be <b>NULL</b>. If an existing reparse tag is being modified, the GUID specified in this parameter must match the GUID of the reparse point to be modified. </p>
</dd>

### -param <i>DataBuffer</i> [in]

<dd>
<p>Pointer to a buffer that contains user-defined data for the reparse point. </p>
</dd>

### -param <i>DataBufferLength</i> [in]

<dd>
<p>Size, in bytes, of the buffer that <i>DataBuffer </i>points to. </p>
</dd>
</dl>

## -returns
<p><b>FltTagFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FltTagFile</b> encountered a pool allocation failure. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The file system does not support reparse points. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p><i>FileTag</i> is not a Microsoft tag, and <b>NULL</b> was specified for <i>Guid</i>. This is an error code. </p><dl>
<dt><b>STATUS_IO_REPARSE_TAG_MISMATCH</b></dt>
</dl><p>The reparse tag specified by the caller did not match the tag of the reparse point to be modified. This is an error code. </p><dl>
<dt><b>STATUS_REPARSE_ATTRIBUTE_CONFLICT</b></dt>
</dl><p>The reparse GUID specified by the caller did not match the GUID of the reparse point to be modified. This is an error code. </p>

<p> </p>

## -remarks
<p>Minifilter drivers should use <b>FltTagFile</b> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545568">FSCTL_SET_REPARSE_POINT</a> to set a reparse point. </p>

<p>Not all file systems support reparse points. The NTFS file system supports them; the FAT file system does not. Minifilter drivers can determine whether a file system supports reparse points by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>, specifying FileFsAttributeInformation for the <i>FsInformation</i> parameter, and examining the FILE_SUPPORTS_REPARSE_POINTS bit flag in the returned <a href="https://msdn.microsoft.com/library/windows/hardware/ff540251">FILE_FS_ATTRIBUTE_INFORMATION</a> structure. </p>

<p>To remove an existing reparse point, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>. </p>

<p>For more information about reparse points, see the Microsoft Windows SDK documentation. </p>

<p>Minifilter drivers should use <b>FltTagFile</b> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545568">FSCTL_SET_REPARSE_POINT</a> to set a reparse point. </p>

<p>Not all file systems support reparse points. The NTFS file system supports them; the FAT file system does not. Minifilter drivers can determine whether a file system supports reparse points by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>, specifying FileFsAttributeInformation for the <i>FsInformation</i> parameter, and examining the FILE_SUPPORTS_REPARSE_POINTS bit flag in the returned <a href="https://msdn.microsoft.com/library/windows/hardware/ff540251">FILE_FS_ATTRIBUTE_INFORMATION</a> structure. </p>

<p>To remove an existing reparse point, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>. </p>

<p>For more information about reparse points, see the Microsoft Windows SDK documentation. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540251">FILE_FS_ATTRIBUTE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544820">FLT_TAG_DATA_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542988">FltFsControlFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544828">FSCTL_DELETE_REPARSE_POINT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544836">FSCTL_GET_REPARSE_POINT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545568">FSCTL_SET_REPARSE_POINT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549452">IsReparseTagMicrosoft</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549462">IsReparseTagNameSurrogate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552012">REPARSE_DATA_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552014">REPARSE_GUID_DATA_BUFFER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltTagFile function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
