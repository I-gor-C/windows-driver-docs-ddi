---
UID: NF.fltkernel.FltDeleteFileContext
title: FltDeleteFileContext function
author: windows-driver-content
description: The FltDeleteFileContext routine retrieves and deletes a file context that a given minifilter driver has set for a given file.
old-location: ifsk\fltdeletefilecontext.htm
old-project: ifsk
ms.assetid: faffa053-0382-415c-8f61-ee9121839598
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltDeleteFileContext
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
req.alt-api: FltDeleteFileContext
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
---

# FltDeleteFileContext function



## -description
The <b>FltDeleteFileContext</b> routine retrieves and deletes a file context that a given minifilter driver has set for a given file. 


## -syntax

````
NTSTATUS FltDeleteFileContext(
  _In_  PFLT_INSTANCE Instance,
  _In_  PFILE_OBJECT  FileObject,
  _Out_ PFLT_CONTEXT  *OldContext
);
````


## -parameters

### -param Instance [in]

Opaque instance pointer for the caller. This parameter is required and cannot be <b>NULL</b>. 

### -param FileObject [in]

File object pointer for the file. This parameter is required and cannot be <b>NULL</b>. 

### -param OldContext [out]

Pointer to a caller-allocated variable that receives the address of the deleted context. If no matching context is found, this variable receives NULL_CONTEXT. This parameter is optional and can be <b>NULL</b>. (For more information about this parameter, see the following Remarks section.) 

## -returns
<b>FltDeleteFileContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as one of the following: 
<dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl>No matching context was found. This is an error code. 
<dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl>File contexts are not supported for this file. This is an error code. 

 

## -remarks
The <b>FltDeleteFileContext</b> routine is available on Windows Vista and later. 

Because contexts are reference-counted, it is not usually necessary for a minifilter driver to call a routine such as <b>FltDeleteFileContext</b> or <a href="ifsk.fltdeletecontext">FltDeleteContext</a> to explicitly delete a context. 

A minifilter driver calls <b>FltDeleteFileContext</b> to retrieve and delete a file context that it previously set for a file by calling <a href="ifsk.fltsetfilecontext">FltSetFileContext</a>. 

If the <i>OldContext</i> parameter is <b>NULL</b> on input and a matching file context is found, <b>FltDeleteFileContext</b> releases the reference that was added by the minifilter driver's previous call to <a href="ifsk.fltsetfilecontext">FltSetFileContext</a>. The deleted context is usually freed immediately unless there is an outstanding reference on it (for example, because the context is still being used by another thread). 

If the <i>OldContext</i> parameter is not <b>NULL</b> and a matching file context is found and returned, the caller is responsible for releasing the reference that was added by <a href="ifsk.fltsetfilecontext">FltSetFileContext</a>. To release this reference, the minifilter driver must call <a href="ifsk.fltreleasecontext">FltReleaseContext</a> on the deleted file context as soon as possible after performing any necessary cleanup. 

To allocate a new context, call <a href="ifsk.fltallocatecontext">FltAllocateContext</a>. 

To decrement the reference count on a context, call <a href="ifsk.fltreleasecontext">FltReleaseContext</a>. 

To delete a context for which you already have a context pointer, call <a href="ifsk.fltdeletecontext">FltDeleteContext</a>. 

To retrieve a file context, call <a href="ifsk.fltgetfilecontext">FltGetFileContext</a>. 

To set a file context, call <a href="ifsk.fltsetfilecontext">FltSetFileContext</a>. 

To determine whether file contexts are supported for a given file, call <a href="ifsk.fltsupportsfilecontexts">FltSupportsFileContexts</a> or <a href="ifsk.fltsupportsfilecontextsex">FltSupportsFileContextsEx</a>. 

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
IRQL
</th>
<td width="70%">
&lt;= APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.flt_context_registration">FLT_CONTEXT_REGISTRATION</a>
</dt>
<dt>
<a href="ifsk.fltallocatecontext">FltAllocateContext</a>
</dt>
<dt>
<a href="ifsk.fltdeletecontext">FltDeleteContext</a>
</dt>
<dt>
<a href="ifsk.fltgetfilecontext">FltGetFileContext</a>
</dt>
<dt>
<a href="ifsk.fltreleasecontext">FltReleaseContext</a>
</dt>
<dt>
<a href="ifsk.fltsetfilecontext">FltSetFileContext</a>
</dt>
<dt>
<a href="ifsk.fltsupportsfilecontexts">FltSupportsFileContexts</a>
</dt>
<dt>
<a href="ifsk.fltsupportsfilecontextsex">FltSupportsFileContextsEx</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltDeleteFileContext routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
