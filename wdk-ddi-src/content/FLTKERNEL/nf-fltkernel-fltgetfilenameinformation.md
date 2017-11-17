---
UID: NF.fltkernel.FltGetFileNameInformation
title: FltGetFileNameInformation
author: windows-driver-content
description: The FltGetFileNameInformation routine returns name information for a file or directory.
old-location: ifsk\fltgetfilenameinformation.htm
ms.assetid: 707e7e83-31d8-46cf-a2ef-e53a20edaeff
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
req.alt-api: FltGetFileNameInformation
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
ms.keywords: FltGetFileNameInformation
req.iface: 
---

# FltGetFileNameInformation function



## -description
<p>The <b>FltGetFileNameInformation</b> routine returns name information for a file or directory. </p>


## -syntax

````
NTSTATUS FltGetFileNameInformation(
  _In_  PFLT_CALLBACK_DATA         CallbackData,
  _In_  FLT_FILE_NAME_OPTIONS      NameOptions,
  _Out_ PFLT_FILE_NAME_INFORMATION *FileNameInformation
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in]

<dd>
<p>A pointer to the callback data structure for the I/O operation (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>). This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>NameOptions</i> [in]

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544636">FLT_FILE_NAME_OPTIONS</a> value containing flags that specify the format of the name information to be returned, as well as the query method that the Filter Manager is to use. (Additional flags can be used by name provider minifilter drivers to specify name query options. For more information, see <b>FLT_FILE_NAME_OPTIONS</b>.) This parameter is required and cannot be <b>NULL</b>. </p>
<p>Following are the name format flag values. Only one of the following flags can be specified. (For an explanation of these formats, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>.) </p>
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
<p>Not valid in the pre-create path. </p>
</td>
</tr>
</table>
<p> </p>
<p>Following are the query method flag values. Only one of the following flags can be specified. </p>
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
<p>If it is not currently safe to query the file system for the file name, <b>FltGetFileNameInformation</b> does nothing. Otherwise, <b>FltGetFileNameInformation</b> queries the Filter Manager's name cache for the file name information. If the name is not found in the cache, <b>FltGetFileNameInformation</b> queries the file system and caches the result. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_QUERY_CACHE_ONLY</p>
</td>
<td>
<p>FltGetFileNameInformation queries the Filter Manager's name cache for the file name information. <b>FltGetFileNameInformation</b> does not query the file system. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY</p>
</td>
<td>
<p><b>FltGetFileNameInformation</b> queries the file system for the file name information. <b>FltGetFileNameInformation</b> does not query the Filter Manager's name cache, and does not cache the result of the file system query. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_QUERY_ALWAYS_ALLOW_CACHE_LOOKUP</p>
</td>
<td>
<p><b>FltGetFileNameInformation</b> queries the Filter Manager's name cache for the file name information. If the name is not found in the cache, and it is currently safe to do so, <b>FltGetFileNameInformation</b> queries the file system for the file name information and caches the result. </p>
</td>
</tr>
</table>
<p> </p>
<p>Name provider minifilters use the following flags to specify the properties of file name operations. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_REQUEST_FROM_CURRENT_PROVIDER</p>
</td>
<td>
<p>A name provider minifilter can use this flag to specify that a name query request should be redirected to itself (the name provider minifilter) rather than being satisfied by the name providers lower in the stack. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_DO_NOT_CACHE</p>
</td>
<td>
<p>This flag denotes that the name retrieved from this query should not be cached. Name provider minifilters use this flag as they perform intermediate queries to generate a name. </p>
</td>
</tr>
<tr>
<td>
<p>FLT_FILE_NAME_ALLOW_QUERY_ON_REPARSE</p>
</td>
<td>
<p>A name provider minifilter can use this flag to specify that it is safe to query the name in the post-create path even if STATUS_REPARSE was returned. It is the caller's responsibility to ensure that the <b>FileObject-&gt;FileName</b> field was not changed. Do not use this flag with mount points or symbolic link reparse points. </p>
<p>This flag is available on Microsoft Windows Server 2003 SP1 and later. This flag is also available on Windows 2000 SP4 with Update Rollup 1 and later.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>FileNameInformation</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives the address of a system-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a> structure containing the file name information. <b>FltGetFileNameInformation</b> allocates this structure from paged pool. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p>If the name information is successfully returned, <b>FltGetFileNameInformation</b> returns STATUS_SUCCESS. Otherwise, it returns an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_INVALID_NAME_REQUEST</b></dt>
</dl><p>One of the following: </p>

<p><b>FltGetFileNameInformation</b> cannot get file name information if the <b>TopLevelIrp</b> field of the current thread is not <b>NULL</b>, because the resulting file system recursion could cause deadlocks or stack overflows. (For more information about this issue, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548405">IoGetTopLevelIrp</a>.) </p>

<p><b>FltGetFileNameInformation</b> cannot get file name information in the paging I/O path. </p>

<p><b>FltGetFileNameInformation</b> cannot get file name information in the post-close path. </p>

<p><b>FltGetFileNameInformation</b> cannot get the short name of a file in the pre-create path. </p>

<p>STATUS_FLT_INVALID_NAME_REQUEST is an error code.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FltGetFileNameInformation</b> encountered a pool allocation failure. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the following: </p>

<p>The <b>FileNameInformation</b> parameter cannot be <b>NULL</b>.</p>

<p>The <i>CallbackData</i> parameter cannot be <b>NULL</b>.</p>

<p>STATUS_INVALID_PARAMETER is an error code.</p><dl>
<dt><b>STATUS_FLT_NAME_CACHE_MISS</b></dt>
</dl><p>The file name information is not found in the name cache and <i>NameOptions</i> includes FLT_FILE_NAME_QUERY_CACHE_ONLY.</p>

<p>-or-</p>

<p>The file name information is not found in the name cache when <i>NameOptions</i> includes FLT_FILE_NAME_QUERY_ALWAYS_ALLOW_CACHE_LOOKUP and the file name information cannot be queried from the file system.</p>

<p>An additional call to <b>FltGetFileNameInformation</b>  with FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY set in <i>NameOptions</i> may return the file name information.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>If the user opened the file by file ID but does not have traverse privileges for the entire path, <b>FltGetFileNameInformation</b> fails with this return value. </p>

<p>STATUS_ACCESS_DENIED is an error code. </p>

<p>-or-</p>

<p>The file is a system file with all access denied.</p>

<p> </p>

## -remarks
<p><b>FltGetFileNameInformation</b> returns the requested name information for the file or directory that is represented by the file object that is the target of the I/O operation. </p>

<p>For a pre-create operation, if the <b>CallbackData</b> -&gt;<b>Iopb</b> -&gt;<b>OperationFlags</b> member contains the SL_OPEN_TARGET_DIRECTORY bitwise flag, <b>FltGetFileNameInformation</b> returns the name of the containing (parent) directory for the given file. This name is the actual path that the create operation opens.</p>

<p>To parse the contents of the FLT_FILE_NAME_INFORMATION structure returned by <b>FltGetFileNameInformation</b>, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>. (For more information about file name formats, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>.) </p>

<p>After a successful call to <b>FltGetFileNameInformation</b>, the caller is responsible for releasing the pointer returned in the <i>FileNameInformation</i> parameter when the pointer is no longer needed. The caller does this by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544320">FltReleaseFileNameInformation</a>. </p>

<p>The caller must not modify the contents of the structure returned in the <i>FileNameInformation</i> parameter because this structure is cached by the Filter Manager so that all minifilter drivers can use it. </p>

<p>If <b>FltGetFileNameInformation</b> is called in the preoperation callback routine for a create operation to retrieve the opened name, <b>FltGetFileNameInformation</b> succeeds even if the path to the file being opened does not exist on the volume. If <b>FltGetFileNameInformation</b> is called in the preoperation callback routine for a create operation to retrieve the normalized name, <b>FltGetFileNameInformation</b> succeeds even if the final component of the path to the file being opened does not exist on the volume.</p>

<p>In create, hard-link, and rename operations, file name tunneling can cause the final component in normalized file name information that a minifilter driver retrieves in a preoperation callback routine to be invalidated. If a minifilter driver retrieves normalized file name information in a preoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>) routine by calling a routine such as <b>FltGetFileNameInformation</b>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543177">FltGetTunneledName</a> from its postoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>) routine to retrieve the correct file name information for the file. </p>

<p>For Windows 8.1 and earlier, <b>FltGetFileNameInformation</b> can include a <a href="fs.file_streams">stream type</a> <i>only</i> when called from a filter’s pre-create callback.  To distinguish between a file’s default stream and metadata streams, this call should be made in the pre-create operation. The resulting stream type will remain valid across the lifetime of the file.</p>

<p> Prior to Windows 8, Filter Manager obtained the normalized name for a file or directory by collecting the name information for each component of  the file path. This required multiple queries to the file system to compile the complete path. Starting with Windows 8, local file systems support the  <b>FileNormalizedNameInformation</b> file information class and only a single query is necessary to obtain the normalized name. Remote file systems may not support the <b>FileNormalizedNameInformation</b> file information class. When this is the case, a query for each component of the file path is still required to assemble the normalized name. Under certain network conditions, a full name query can require a significant amount of time to complete.</p>

<p>For more information about normalized file name information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>. </p>

<p>The following paired operations can cause the file name <i>name</i> to be tunneled: </p>

<p>delete(<i>name</i>)/create(<i>name</i>)</p>

<p>delete(<i>name</i>)/rename(<i>source</i>, <i>name</i>)</p>

<p>rename(<i>name</i>, <i>newname</i>)/create(<i>name</i>)</p>

<p>rename(<i>name</i>, <i>newname</i>)/rename(<i>source</i>, <i>name</i>)</p>

<p>For more information about file name tunneling, see <a href="http://go.microsoft.com/fwlink/p/?linkid=3100&amp;amp;id=172190">Microsoft Knowledge Base Article 172190</a>.</p>

<p><b>FltGetFileNameInformation</b> returns the requested name information for the file or directory that is represented by the file object that is the target of the I/O operation. </p>

<p>For a pre-create operation, if the <b>CallbackData</b> -&gt;<b>Iopb</b> -&gt;<b>OperationFlags</b> member contains the SL_OPEN_TARGET_DIRECTORY bitwise flag, <b>FltGetFileNameInformation</b> returns the name of the containing (parent) directory for the given file. This name is the actual path that the create operation opens.</p>

<p>To parse the contents of the FLT_FILE_NAME_INFORMATION structure returned by <b>FltGetFileNameInformation</b>, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>. (For more information about file name formats, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>.) </p>

<p>After a successful call to <b>FltGetFileNameInformation</b>, the caller is responsible for releasing the pointer returned in the <i>FileNameInformation</i> parameter when the pointer is no longer needed. The caller does this by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544320">FltReleaseFileNameInformation</a>. </p>

<p>The caller must not modify the contents of the structure returned in the <i>FileNameInformation</i> parameter because this structure is cached by the Filter Manager so that all minifilter drivers can use it. </p>

<p>If <b>FltGetFileNameInformation</b> is called in the preoperation callback routine for a create operation to retrieve the opened name, <b>FltGetFileNameInformation</b> succeeds even if the path to the file being opened does not exist on the volume. If <b>FltGetFileNameInformation</b> is called in the preoperation callback routine for a create operation to retrieve the normalized name, <b>FltGetFileNameInformation</b> succeeds even if the final component of the path to the file being opened does not exist on the volume.</p>

<p>In create, hard-link, and rename operations, file name tunneling can cause the final component in normalized file name information that a minifilter driver retrieves in a preoperation callback routine to be invalidated. If a minifilter driver retrieves normalized file name information in a preoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>) routine by calling a routine such as <b>FltGetFileNameInformation</b>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543177">FltGetTunneledName</a> from its postoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>) routine to retrieve the correct file name information for the file. </p>

<p>For Windows 8.1 and earlier, <b>FltGetFileNameInformation</b> can include a <a href="fs.file_streams">stream type</a> <i>only</i> when called from a filter’s pre-create callback.  To distinguish between a file’s default stream and metadata streams, this call should be made in the pre-create operation. The resulting stream type will remain valid across the lifetime of the file.</p>

<p> Prior to Windows 8, Filter Manager obtained the normalized name for a file or directory by collecting the name information for each component of  the file path. This required multiple queries to the file system to compile the complete path. Starting with Windows 8, local file systems support the  <b>FileNormalizedNameInformation</b> file information class and only a single query is necessary to obtain the normalized name. Remote file systems may not support the <b>FileNormalizedNameInformation</b> file information class. When this is the case, a query for each component of the file path is still required to assemble the normalized name. Under certain network conditions, a full name query can require a significant amount of time to complete.</p>

<p>For more information about normalized file name information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>. </p>

<p>The following paired operations can cause the file name <i>name</i> to be tunneled: </p>

<p>delete(<i>name</i>)/create(<i>name</i>)</p>

<p>delete(<i>name</i>)/rename(<i>source</i>, <i>name</i>)</p>

<p>rename(<i>name</i>, <i>newname</i>)/create(<i>name</i>)</p>

<p>rename(<i>name</i>, <i>newname</i>)/rename(<i>source</i>, <i>name</i>)</p>

<p>For more information about file name tunneling, see <a href="http://go.microsoft.com/fwlink/p/?linkid=3100&amp;amp;id=172190">Microsoft Knowledge Base Article 172190</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544636">FLT_FILE_NAME_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543177">FltGetTunneledName</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548405">IoGetTopLevelIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetFileNameInformation routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
