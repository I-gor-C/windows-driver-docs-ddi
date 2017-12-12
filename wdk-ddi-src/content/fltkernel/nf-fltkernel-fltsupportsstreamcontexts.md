---
UID: NF.fltkernel.FltSupportsStreamContexts
title: FltSupportsStreamContexts function
author: windows-driver-content
description: FltSupportsStreamContexts determines whether stream contexts are supported on a given file object.
old-location: ifsk\fltsupportsstreamcontexts.htm
old-project: ifsk
ms.assetid: ea1fd4d5-85c6-40ce-9feb-a2c22e9fe905
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltSupportsStreamContexts
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
req.alt-api: FltSupportsStreamContexts
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

# FltSupportsStreamContexts function



## -description
<b>FltSupportsStreamContexts</b> determines whether stream contexts are supported on a given file object. 



## -syntax

````
BOOLEAN FltSupportsStreamContexts(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters

### -param FileObject [in]

Pointer to the file object to test. 


## -returns
<b>FltSupportsStreamContexts</b> returns <b>TRUE</b> if the file system supports stream contexts for the file object; <b>FALSE</b> otherwise. 


## -remarks
Paging files do not currently support file, stream, or stream handle contexts. 

To allocate a new context, call <a href="ifsk.fltallocatecontext">FltAllocateContext</a>. 

To delete a stream context, call <a href="ifsk.fltdeletestreamcontext">FltDeleteStreamContext</a> or <a href="ifsk.fltdeletecontext">FltDeleteContext</a>. 

To get the stream context for a file object, call <a href="ifsk.fltgetstreamcontext">FltGetStreamContext</a>. 

To set a stream context on a file object, call <a href="ifsk.fltsetstreamcontext">FltSetStreamContext</a>. 

To release a reference on a context, call <a href="ifsk.fltreleasecontext">FltReleaseContext</a>. 


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
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fltallocatecontext">FltAllocateContext</a>
</dt>
<dt>
<a href="ifsk.fltdeletecontext">FltDeleteContext</a>
</dt>
<dt>
<a href="ifsk.fltdeletestreamcontext">FltDeleteStreamContext</a>
</dt>
<dt>
<a href="ifsk.fltgetstreamcontext">FltGetStreamContext</a>
</dt>
<dt>
<a href="ifsk.fltreleasecontext">FltReleaseContext</a>
</dt>
<dt>
<a href="ifsk.fltsetstreamcontext">FltSetStreamContext</a>
</dt>
<dt>
<a href="ifsk.fltsupportsstreamhandlecontexts">FltSupportsStreamHandleContexts</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSupportsStreamContexts function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

