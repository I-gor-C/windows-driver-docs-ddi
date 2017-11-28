---
UID: NS.fltkernel._FLT_FILE_NAME_INFORMATION
title: FLT_FILE_NAME_INFORMATION
author: windows-driver-content
description: The FLT_FILE_NAME_INFORMATION structure contains file name information.
old-location: ifsk\flt_file_name_information.htm
old-project: ifsk
ms.assetid: 998a028a-7dd8-429a-8195-68d4b4b1b156
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FLT_FILE_NAME_INFORMATION, FLT_FILE_NAME_INFORMATION, *PFLT_FILE_NAME_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FLT_FILE_NAME_INFORMATION
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
req.iface: 
---

# FLT_FILE_NAME_INFORMATION structure



## -description
<p>The FLT_FILE_NAME_INFORMATION structure contains file name information. </p>


## -syntax

````
typedef struct _FLT_FILE_NAME_INFORMATION {
  USHORT                     Size;
  FLT_FILE_NAME_PARSED_FLAGS NamesParsed;
  FLT_FILE_NAME_OPTIONS      Format;
  UNICODE_STRING             Name;
  UNICODE_STRING             Volume;
  UNICODE_STRING             Share;
  UNICODE_STRING             Extension;
  UNICODE_STRING             Stream;
  UNICODE_STRING             FinalComponent;
  UNICODE_STRING             ParentDir;
} FLT_FILE_NAME_INFORMATION, *PFLT_FILE_NAME_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size, in bytes, of the FLT_FILE_NAME_INFORMATION structure. </p>
</dd>

### -field <b>NamesParsed</b>

<dd>
<p>Bitmask of flags that indicate which name components have been parsed from the <b>Name</b> string by <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>. Note that, when parsing the <b>Name</b> string, <b>FltParseFileNameInformation</b> sets this flag for each component, whether the component is found to be present in the string. These values may be combined by using the OR operator. </p>
<table>
<tr>
<th>Flag</th>
<th>Component</th>
</tr>
<tr>
<td>
<p>FLTFL_FILE_NAME_PARSED_FINAL_COMPONENT</p>
</td>
<td>
<p><b>FinalComponent</b></p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_FILE_NAME_PARSED_EXTENSION</p>
</td>
<td>
<p><b>Extension</b></p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_FILE_NAME_PARSED_STREAM</p>
</td>
<td>
<p><b>Stream</b></p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_FILE_NAME_PARSED_PARENT_DIR</p>
</td>
<td>
<p><b>ParentDir</b></p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Format</b>

<dd>
<p>Format of the name information stored in the <b>Name</b> member. One of the following. (For an explanation of these formats, see the following Remarks section.) </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_NORMALIZED</p>
</td>
<td>
<p>The <b>Name</b> member contains the normalized name for the file. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_OPENED</p>
</td>
<td>
<p>The <b>Name</b> member contains the name that was used when the file was opened. This name string is not normalized. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_SHORT</p>
</td>
<td>
<p>The <b>Name</b> member contains the short (8.3) name for the file. The short name for a file does not include the volume name, directory path, or stream name. This name string is not normalized. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Name</b>

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that contains the file name string, formatted as specified by the <b>Format</b> member. </p>
</dd>

### -field <b>Volume</b>

<dd>
<p>UNICODE_STRING structure that contains the volume name parsed from the <b>Name</b> string. If <b>Format</b> is FLT_FILE_NAME_SHORT, <b>Volume.Length</b> is zero. </p>
</dd>

### -field <b>Share</b>

<dd>
<p>UNICODE_STRING structure that contains the network share name parsed from the <b>Name</b> string for a remote file. If <b>Format</b> is FLT_FILE_NAME_SHORT, <b>Share.Length</b> is zero. </p>
</dd>

### -field <b>Extension</b>

<dd>
<p>UNICODE_STRING structure that contains the extension parsed from the <b>Name</b> string. If no extension is found, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a> sets <b>Extension.Length</b> to zero. </p>
</dd>

### -field <b>Stream</b>

<dd>
<p>UNICODE_STRING structure that contains the stream name parsed from the <b>Name</b> string. If no stream name is found, or if <b>Format</b> is FLT_FILE_NAME_SHORT, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a> sets <b>Stream.Length</b> to zero. </p>
</dd>

### -field <b>FinalComponent</b>

<dd>
<p>UNICODE_STRING structure that contains the final name component parsed from the <b>Name</b> string. If no final component name is found, or if <b>Format</b> is FLT_FILE_NAME_SHORT, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a> sets <b>FinalComponent.Length</b> to zero. </p>
</dd>

### -field <b>ParentDir</b>

<dd>
<p>UNICODE_STRING structure that contains the parent directory name parsed from the <b>Name</b> string by <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>. If no parent directory name is found, or if <b>Format</b> is FLT_FILE_NAME_SHORT, <b>FltParseFileNameInformation</b> sets <b>ParentDir.Length</b> to zero. </p>
</dd>
</dl>

## -remarks
<p>The <b>Name</b> member contains one of the following: </p>

<p>The normalized name for the file </p>

<p>The opened name for the file </p>

<p>The short name for the file </p>

<p>A file name is considered <i>normalized</i> if all of the following are true: </p>

<p>It contains the full directory path for the file, including the volume name, unless the user opened the file by file ID but does not have traverse privilege for the entire path. (For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>.) </p>

<p>The volume name is the volume's nonpersistent device object name (for example, "\Device\HarddiskVolume1"). </p>

<p>All short names are expanded to the equivalent long names. </p>

<p>Any trailing ":$DATA" or "::$DATA" strings are removed from the stream name. </p>

<p>All mount points are resolved. </p>

<p>The following is an example of a normalized file name for a local file: </p>

<p>The following is an example of a normalized file name for a remote file: </p>

<p>The <i>opened name</i> for a file is the name that was used when the file was opened. Like the normalized name, it contains the full directory path for the file, including the volume name. It differs from the normalized name in the following ways: </p>

<p>The directory path for the file can contain short names as well as long names. </p>

<p>Trailing ":$DATA" and "::$DATA" strings are not removed from the stream name. </p>

<p>Mount points are not resolved. </p>

<p>The following is an example of an opened file name for a local file: </p>

<p>The following is an example of an opened file name for a remote file: </p>

<p>The <i>short name</i> for a file is the short (8.3) name for the final component of the file name. Because it is generated when the file is opened, the short name is not available for an unopened file object, and it is not available in the create dispatch ("pre-create") path. It is also not available for NTFS stream file objects. Not all open files have short file names. For example, on NTFS partitions where short file name generation has been disabled, no files have short file names. </p>

<p>The following is an example of a short name for a file: </p>

<p>To obtain an FLT_FILE_NAME_INFORMATION structure for a file, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a>. These routines returns a pointer to a Filter Manager-owned FLT_FILE_NAME_INFORMATION structure that is shared by all minifilters. </p>

<p>File systems such as NTFS and FAT use a per-volume tunnel cache to briefly preserve file names and other metadata for files that are being renamed, linked to, or deleted. This file name tunneling can cause the final component in normalized file name information returned by a preoperation call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a> to be invalidated. If a minifilter retrieves normalized file name information in the preoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>) routine for a create, hard-link, or rename operation, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543177">FltGetTunneledName</a> from its postoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>) routine to retrieve the correct file name information for the file. </p>

<p>Although it contains numerous <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structures, the FLT_FILE_NAME_INFORMATION structure does not occupy much space in memory because all of the UNICODE_STRING structures in a FLT_FILE_NAME_INFORMATION structure share a single buffer. </p>

<p>To parse the contents of the <b>Name</b> string, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>. This routine sets the values of the <b>Extension</b>, <b>Stream</b>, <b>FinalComponent</b>, <b>ParentDir</b>, and <b>NamesParsed</b> members of this structure. </p>

<p>Minifilters are responsible for calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544320">FltReleaseFileNameInformation</a> to release the FLT_FILE_NAME_INFORMATION structure when it is no longer needed. </p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544636">FLT_FILE_NAME_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543177">FltGetTunneledName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543413">FltParseFileName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544301">FltReferenceFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544320">FltReleaseFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_FILE_NAME_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
