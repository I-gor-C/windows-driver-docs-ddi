---
UID: NF.fltkernel.FltSetInformationFile
title: FltSetInformationFile
author: windows-driver-content
description: FltSetInformationFile sets information for a given file.
old-location: ifsk\fltsetinformationfile.htm
old-project: ifsk
ms.assetid: 8d0a91ef-9fb0-45a6-979a-614aed1703a5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltSetInformationFile
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
req.alt-api: FltSetInformationFile
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

# FltSetInformationFile function



## -description
<p><b>FltSetInformationFile</b> sets information for a given file. </p>


## -syntax

````
NTSTATUS FltSetInformationFile(
  _In_ PFLT_INSTANCE          Instance,
  _In_ PFILE_OBJECT           FileObject,
  _In_ PVOID                  FileInformation,
  _In_ ULONG                  Length,
  _In_ FILE_INFORMATION_CLASS FileInformationClass
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
<p>File object pointer for the file. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>FileInformation</i> [in]

<dd>
<p>Pointer to a caller-allocated buffer that contains information to be set for the file. The <i>FileInformationClass</i> parameter specifies the type of information. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Size, in bytes, of the <i>FileInformation</i> buffer. </p>
</dd>

### -param <i>FileInformationClass</i> [in]

<dd>
<p>Specifies the type of information to be set for the file. The following values are defined. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FileAllocationInformation</b></p>
</td>
<td>
<p>Set <a href="..\ntifs\ns-ntifs--file-allocation-information.md">FILE_ALLOCATION_INFORMATION</a> for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileBasicInformation</b></p>
</td>
<td>
<p>Set <a href="..\wdm\ns-wdm--file-basic-information.md">FILE_BASIC_INFORMATION</a> for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileDispositionInformation</b></p>
</td>
<td>
<p>Set <a href="..\ntddk\ns-ntddk--file-disposition-information.md">FILE_DISPOSITION_INFORMATION</a> for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileEndOfFileInformation</b></p>
</td>
<td>
<p>Set <a href="..\ntddk\ns-ntddk--file-end-of-file-information.md">FILE_END_OF_FILE_INFORMATION</a> for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileLinkInformation</b></p>
</td>
<td>
<p>Set <a href="..\ntifs\ns-ntifs--file-link-information.md">FILE_LINK_INFORMATION</a> for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FilePositionInformation</b></p>
</td>
<td>
<p>Set <a href="..\wdm\ns-wdm--file-position-information.md">FILE_POSITION_INFORMATION</a> for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileRenameInformation</b></p>
</td>
<td>
<p>Set <a href="..\ntifs\ns-ntifs--file-rename-information.md">FILE_RENAME_INFORMATION</a> for the file. For more information about file renaming, see the following Remarks section. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileValidDataLengthInformation</b></p>
</td>
<td>
<p>Set <a href="..\ntddk\ns-ntddk--file-valid-data-length-information.md">FILE_VALID_DATA_LENGTH_INFORMATION</a> for the file. </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>FltSetInformationFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value. </p>

## -remarks
<p>A minifilter driver calls <b>FltSetInformationFile</b> to set information for a given file. The file must currently be open. </p>

<p>A file rename operation imposes the following restriction on the parameter values passed to <b>FltSetInformationFile</b>: As noted in the reference entry for <a href="..\ntifs\ns-ntifs--file-rename-information.md">FILE_RENAME_INFORMATION</a>, a file or directory can only be renamed within a volume. In other words, a rename operation cannot cause a file or directory to be moved to a different volume. Unlike <a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>, <b>FltSetInformationFile</b> does not validate the contents of the FILE_RENAME_INFORMATION structure. Thus the caller of <b>FltSetInformationFile</b> is responsible for ensuring that the new name for the file or directory is on the same volume as the old name. </p>

<p>Minifilter drivers must use <b>FltSetInformationFile</b> , not <a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>, to rename a file. </p>

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
<a href="..\ntifs\ns-ntifs--file-allocation-information.md">FILE_ALLOCATION_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--file-basic-information.md">FILE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-disposition-information.md">FILE_DISPOSITION_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-end-of-file-information.md">FILE_END_OF_FILE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-link-information.md">FILE_LINK_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--file-position-information.md">FILE_POSITION_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-rename-information.md">FILE_RENAME_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-valid-data-length-information.md">FILE_VALID_DATA_LENGTH_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltqueryinformationfile.md">FltQueryInformationFile</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformationfile.md">FltQueryVolumeInformationFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSetInformationFile function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
