---
UID: NF.fltkernel.FltGetFileContext
title: FltGetFileContext function
author: windows-driver-content
description: The FltGetFileContext routine retrieves a context that was set for a file by a given minifilter driver instance.
old-location: ifsk\fltgetfilecontext.htm
old-project: ifsk
ms.assetid: 3104cccf-03ae-4ff9-8cfe-86bd3719a47f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltGetFileContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetFileContext
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
---

# FltGetFileContext function



## -description
The <b>FltGetFileContext</b> routine retrieves a context that was set for a file by a given minifilter driver instance. 



## -syntax

````
NTSTATUS FltGetFileContext(
  _In_  PFLT_INSTANCE Instance,
  _In_  PFILE_OBJECT  FileObject,
  _Out_ PFLT_CONTEXT  *Context
);
````


## -parameters

### -param Instance [in]

Opaque instance pointer for the caller. This parameter is required and cannot be <b>NULL</b>. 


### -param FileObject [in]

File object pointer for the file. This parameter is required and cannot be <b>NULL</b>. 


### -param Context [out]

Pointer to a caller-allocated variable that receives the address of the context. This parameter is required and cannot be <b>NULL</b>. 


## -returns
<b>FltGetFileContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: 
<dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl>No matching context was found. This is an error code. 
<dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl>File contexts are not supported for this file. This is an error code. 

 


## -remarks
A minifilter driver calls <b>FltGetFileContext</b> to retrieve the file context that it has set for a given file. 

To decrement the reference count on a context, call <a href="ifsk.fltreleasecontext">FltReleaseContext</a>. 

<b>FltGetFileContext</b> increments the reference count on the context that the <i>Context </i>parameter points to. Thus, every successful call to <b>FltGetFileContext</b> must be matched by a subsequent call to <a href="ifsk.fltreleasecontext">FltReleaseContext</a>. 

To set a file context, call <a href="ifsk.fltsetfilecontext">FltSetFileContext</a>. 

To allocate a new context, call <a href="ifsk.fltallocatecontext">FltAllocateContext</a>. 

To delete a file context, call <a href="ifsk.fltdeletefilecontext">FltDeleteFileContext</a> or <a href="ifsk.fltdeletecontext">FltDeleteContext</a>. 

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
Version

</th>
<td width="70%">
This routine is available on Windows Vista and later. 

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
<a href="ifsk.fltdeletefilecontext">FltDeleteFileContext</a>
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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetFileContext routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

