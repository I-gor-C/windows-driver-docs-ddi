---
UID: NF.fltkernel.FltUntagFile
title: FltUntagFile function
author: windows-driver-content
description: FltUntagFile removes a reparse point from a file or directory.
old-location: ifsk\fltuntagfile.htm
old-project: ifsk
ms.assetid: 728a9879-681b-4244-b931-7945a05e3d40
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltUntagFile
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
req.alt-api: FltUntagFile
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
---

# FltUntagFile function



## -description
<b>FltUntagFile</b> removes a reparse point from a file or directory. 


## -syntax

````
NTSTATUS FltUntagFile(
  _In_     PFLT_INSTANCE InitiatingInstance,
  _In_     PFILE_OBJECT  FileObject,
  _In_     ULONG         FileTag,
  _In_opt_ GUID          *Guid
);
````


## -parameters

### -param InitiatingInstance [in]

Opaque instance pointer for the minifilter driver instance that initiated this I/O request. This parameter is required and cannot be <b>NULL</b>. 

### -param FileObject [in]

Pointer to a file object for the file or directory from which the reparse point is to be removed. The file object must be opened for FILE_WRITE_DATA access. This parameter is required and cannot be <b>NULL</b>. 

### -param FileTag [in]

Reparse point tag. The tag specified in this parameter must match the tag of the reparse point to be removed. 

### -param Guid [in, optional]

Globally unique identifier (GUID) that uniquely identifies the type of reparse point. If <i>FileTag</i> is not a Microsoft tag, this parameter is required and cannot be <b>NULL</b>. The GUID specified in this parameter must match the GUID of the reparse point to be removed. 

## -returns
<b>FltUntagFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: 
<dl>
<dt><b>STATUS_IO_REPARSE_TAG_MISMATCH</b></dt>
</dl>The reparse tag specified by the caller did not match the tag of the reparse point to be deleted. This is an error code. 
<dl>
<dt><b>STATUS_REPARSE_ATTRIBUTE_CONFLICT</b></dt>
</dl>The reparse GUID specified by the caller did not match the GUID of the reparse point to be deleted. This is an error code. 

 

## -remarks
Minifilter drivers should use <b>FltUntagFile</b> instead of <a href="ifsk.fsctl_delete_reparse_point">FSCTL_DELETE_REPARSE_POINT</a> to delete a reparse point. 

A minifilter driver can set a reparse tag on a file or directory by calling <a href="ifsk.flttagfile">FltTagFile</a>. 

For more information about reparse points, see the Microsoft Windows SDK documentation. 

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
Header
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.flt_tag_data_buffer">FLT_TAG_DATA_BUFFER</a>
</dt>
<dt>
<a href="ifsk.flttagfile">FltTagFile</a>
</dt>
<dt>
<a href="ifsk.fsctl_delete_reparse_point">FSCTL_DELETE_REPARSE_POINT</a>
</dt>
<dt>
<a href="ifsk.fsctl_get_reparse_point">FSCTL_GET_REPARSE_POINT</a>
</dt>
<dt>
<a href="ifsk.fsctl_set_reparse_point">FSCTL_SET_REPARSE_POINT</a>
</dt>
<dt>
<a href="ifsk.isreparsetagmicrosoft">IsReparseTagMicrosoft</a>
</dt>
<dt>
<a href="ifsk.isreparsetagnamesurrogate">IsReparseTagNameSurrogate</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltUntagFile function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
