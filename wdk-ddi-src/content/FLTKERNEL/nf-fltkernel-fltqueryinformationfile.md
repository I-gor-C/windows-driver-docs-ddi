---
UID: NF.fltkernel.FltQueryInformationFile
title: FltQueryInformationFile
author: windows-driver-content
description: FltQueryInformationFile retrieves information for a given file.
old-location: ifsk\fltqueryinformationfile.htm
ms.assetid: f80750fb-4561-4617-bc54-1360b2e93a68
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
req.alt-api: FltQueryInformationFile
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
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: FltQueryInformationFile
req.iface: 
---

# FltQueryInformationFile function



## -description
<p><b>FltQueryInformationFile</b> retrieves information for a given file. </p>


## -syntax

````
NTSTATUS FltQueryInformationFile(
  _In_      PFLT_INSTANCE          Instance,
  _In_      PFILE_OBJECT           FileObject,
  _Out_     PVOID                  FileInformation,
  _In_      ULONG                  Length,
  _In_      FILE_INFORMATION_CLASS FileInformationClass,
  _Out_opt_ PULONG                 LengthReturned
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

### -param <i>FileInformation</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives information about the file. The <i>FileInformationClass</i> parameter specifies the type of information. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Size, in bytes, of the <i>FileInformation</i> buffer. </p>
</dd>

### -param <i>FileInformationClass</i> [in]

<dd>
<p>Type of file information to be returned. One of the following. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FileAllInformation</b></p>
</td>
<td>
<p>Return a FILE_ALL_INFORMATION structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileAttributeTagInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545750">FILE_ATTRIBUTE_TAG_INFORMATION</a> structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileBasicInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545762">FILE_BASIC_INFORMATION</a> structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileCompressionInformation</b></p>
</td>
<td>
<p>Return a FILE_COMPRESSION_INFORMATION structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileEaInformation</b></p>
</td>
<td>
<p>Return a FILE_EA_INFORMATION structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileInternalInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540318">FILE_INTERNAL_INFORMATION</a> structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileMoveClusterInformation</b></p>
</td>
<td>
<p>Return a FILE_MOVE_CLUSTER_INFORMATION structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileNameInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileNetworkOpenInformation</b></p>
</td>
<td>
<p>Return a single <a href="https://msdn.microsoft.com/library/windows/hardware/ff545822">FILE_NETWORK_OPEN_INFORMATION</a> structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FilePositionInformation</b></p>
</td>
<td>
<p>Return a single <a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a> structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileStandardInformation</b></p>
</td>
<td>
<p>Return a single <a href="https://msdn.microsoft.com/library/windows/hardware/ff545855">FILE_STANDARD_INFORMATION</a> structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileStreamInformation</b></p>
</td>
<td>
<p>Return a single <a href="https://msdn.microsoft.com/library/windows/hardware/ff540364">FILE_STREAM_INFORMATION</a> structure for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileHardLinkInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff728841">FILE_LINKS_INFORMATION</a> structure for the file. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>LengthReturned</i> [out, optional]

<dd>
<p>Pointer to a caller-allocated variable that receives the size, in bytes, of the information returned in the <i>FileInformation</i> buffer. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltQueryInformationFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_VOLUME_DISMOUNTED</b></dt>
</dl><p>The file resides on a volume that is not currently mounted. This is an error code. </p>

<p> </p>

## -remarks
<p>A minifilter driver calls <b>FltQueryInformationFile</b> to retrieve information for a given file. The file must currently be open. </p>

<p><b>FltQueryInformationFile</b> returns zero in any member of a FILE_<i>XXX</i>_INFORMATION structure that is not supported by a particular file system. </p>

<p>Callers of <b>FltQueryInformationFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with APCs enabled</a>.</p>

<p>A minifilter driver calls <b>FltQueryInformationFile</b> to retrieve information for a given file. The file must currently be open. </p>

<p><b>FltQueryInformationFile</b> returns zero in any member of a FILE_<i>XXX</i>_INFORMATION structure that is not supported by a particular file system. </p>

<p>Callers of <b>FltQueryInformationFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with APCs enabled</a>.</p>

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
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545740">FILE_ALIGNMENT_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545750">FILE_ATTRIBUTE_TAG_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545762">FILE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540318">FILE_INTERNAL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545822">FILE_NETWORK_OPEN_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545855">FILE_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540364">FILE_STREAM_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff728841">FILE_LINKS_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543446">FltQueryVolumeInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltQueryInformationFile function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
