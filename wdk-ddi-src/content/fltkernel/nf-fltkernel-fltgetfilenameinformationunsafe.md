---
UID: NF.fltkernel.FltGetFileNameInformationUnsafe
title: FltGetFileNameInformationUnsafe
author: windows-driver-content
description: The FltGetFileNameInformationUnsafe routine returns name information for an open file or directory.
old-location: ifsk\fltgetfilenameinformationunsafe.htm
old-project: ifsk
ms.assetid: 3c5ec515-d332-4fef-8b78-b2f04a672fd7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltGetFileNameInformationUnsafe
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
req.alt-api: FltGetFileNameInformationUnsafe
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

# FltGetFileNameInformationUnsafe function



## -description
<p>The <b>FltGetFileNameInformationUnsafe</b> routine returns name information for an open file or directory. </p>


## -syntax

````
NTSTATUS FltGetFileNameInformationUnsafe(
  _In_     PFILE_OBJECT               FileObject,
  _In_opt_ PFLT_INSTANCE              Instance,
  _In_     FLT_FILE_NAME_OPTIONS      NameOptions,
  _Out_    PFLT_FILE_NAME_INFORMATION *FileNameInformation
);
````


## -parameters
<dl>

### -param FileObject [in]

<dd>
<p>Pointer to a file object for the file or directory. The file object must be currently open. This parameter is required and cannot be set to <b>NULL</b>. </p>
</dd>

### -param Instance [in, optional]

<dd>
<p>Instance pointer for the caller. This parameter can be set to <b>NULL</b>. </p>
</dd>

### -param NameOptions [in]

<dd>
<p>
<a href="ifsk.flt_file_name_options">FLT_FILE_NAME_OPTIONS</a> value containing flags that specify the format of the name information to be returned, as well as the query method to be used by the Filter Manager. This parameter is required and cannot be set to <b>NULL</b>. </p>
<p>The following table describes the name format flag values. Only one of the flags can be specified. For more information about these formats, see <a href="..\fltkernel\ns-fltkernel--flt-file-name-information.md">FLT_FILE_NAME_INFORMATION</a>. </p>
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
<p>The <i>FileNameInformation</i> parameter receives the address of a structure containing the normalized name for the file. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_OPENED</p>
</td>
<td>
<p>The <i>FileNameInformation</i> parameter receives the address of a structure containing the name that was used when the file was opened. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_SHORT</p>
</td>
<td>
<p>The <i>FileNameInformation</i> parameter receives the address of a structure containing the short (8.3) name for the file. The short name consists of up to 8 characters, followed immediately by a period and up to 3 more characters. The short name for a file does not include the volume name, directory path, or stream name. </p>
</td>
</tr>
</table>
<p> </p>
<p>The following table describes the query method flag values. Only one of the flags can be specified. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_QUERY_DEFAULT</p>
</td>
<td>
<p><b>FltGetFileNameInformationUnsafe</b> queries the Filter Manager's name cache for the file name information. If the name is not found in the cache, <b>FltGetFileNameInformationUnsafe</b> queries the file system and caches the result. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_QUERY_CACHE_ONLY</p>
</td>
<td>
<p><b>FltGetFileNameInformationUnsafe</b> queries the Filter Manager's name cache for the file name information. <b>FltGetFileNameInformationUnsafe</b> does not query the file system. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY</p>
</td>
<td>
<p><b>FltGetFileNameInformationUnsafe</b> queries the file system for the file name information. <b>FltGetFileNameInformationUnsafe</b> does not query the Filter Manager's name cache, and does not cache the result of the file system query. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param FileNameInformation [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the address of a system-allocated FLT_FILE_NAME_INFORMATION structure. <b>FltGetFileNameInformationUnsafe</b> allocates this structure from paged pool. When this information is no longer needed, the caller must release the structure by calling <a href="..\fltkernel\nf-fltkernel-fltreleasefilenameinformation.md">FltReleaseFileNameInformation</a>. This parameter is required and cannot be set to <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltGetFileNameInformationUnsafe</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_INVALID_NAME_REQUEST</b></dt>
</dl><p>The file object that the <i>FileObject</i> parameter points to is not currently open. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid value was passed for the <i>FileNameInformation</i> parameter. This is an error code. </p>

<p> </p>

## -remarks
<p>The <b>FltGetFileNameInformationUnsafe</b> routine is provided so that you can query the name of a file object outside of the context of an I/O operation on that file object. In these cases, you must call <a href="..\fltkernel\nf-fltkernel-fltgetfilenameinformation.md">FltGetFileNameInformation</a>. </p>

<p>Unlike the <a href="..\fltkernel\nf-fltkernel-fltgetfilenameinformation.md">FltGetFileNameInformation</a> routine, <b>FltGetFileNameInformationUnsafe</b> does not protect the caller against the following types of circumstances, where querying the file system for name information can cause deadlocks: </p>

<p>When the <b>TopLevelIrp</b> field of the current thread is not <b>NULL</b>. For more information, see <a href="..\ntifs\nf-ntifs-iogettoplevelirp.md">IoGetTopLevelIrp</a>. </p>

<p>In the paging I/O path. </p>

<p>After an <a href="ifsk.irp_mj_cleanup">IRP_MJ_CLEANUP</a> operation is completed. </p>

<p>In a postoperation callback routine for IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION.</p>

<p>If a minifilter does not yet have a filter instance, such as in its <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine, it can use <code>NULL</code> for the <i>Instance</i> parameter. This allows <i>DriverEntry</i> routines to access file name information. Except for this case, a <code>NULL</code> value for the instance parameter is reserved for system use.</p>

<p>In create, hard-link, and rename operations, file name tunneling can invalidate the final component in normalized file name information that a minifilter driver retrieves in a preoperation callback routine. If a minifilter driver retrieves normalized file name information in a preoperation callback (<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>) routine by calling a routine such as <b>FltGetFileNameInformationUnsafe</b>, it must call <a href="..\fltkernel\nf-fltkernel-fltgettunneledname.md">FltGetTunneledName</a> from its postoperation callback (<a href="..\fltkernel\nc-fltkernel-pflt-post-operation-callback.md">PFLT_POST_OPERATION_CALLBACK</a>) routine to retrieve the correct file name information for the file. </p>

<p>For more information about normalized file name information, see <a href="..\fltkernel\ns-fltkernel--flt-file-name-information.md">FLT_FILE_NAME_INFORMATION</a>. </p>

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
<a href="..\fltkernel\ns-fltkernel--flt-file-name-information.md">FLT_FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.flt_file_name_options">FLT_FILE_NAME_OPTIONS</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetdestinationfilenameinformation.md">FltGetDestinationFileNameInformation</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetfilenameinformation.md">FltGetFileNameInformation</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgettunneledname.md">FltGetTunneledName</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreferencefilenameinformation.md">FltReferenceFileNameInformation</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasefilenameinformation.md">FltReleaseFileNameInformation</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-iogettoplevelirp.md">IoGetTopLevelIrp</a>
</dt>
<dt>
<a href="ifsk.irp_mj_cleanup">IRP_MJ_CLEANUP</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-post-operation-callback.md">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetFileNameInformationUnsafe routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
