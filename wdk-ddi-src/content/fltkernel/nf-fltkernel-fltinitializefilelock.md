---
UID: NF.fltkernel.FltInitializeFileLock
title: FltInitializeFileLock function
author: windows-driver-content
description: The FltInitializeFileLock routine initializes an opaque FILE_LOCK structure that the caller has allocated from paged pool.
old-location: ifsk\fltinitializefilelock.htm
old-project: ifsk
ms.assetid: 84bfec05-9d77-433e-bec2-ad188269fc61
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltInitializeFileLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows XP with SP2 or Windows Server 2003 with SP1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltInitializeFileLock
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

# FltInitializeFileLock function



## -description
The <b>FltInitializeFileLock</b> routine initializes an opaque <a href="ifsk.file_lock">FILE_LOCK</a> structure that the caller has allocated from paged pool.



## -syntax

````
VOID FltInitializeFileLock(
  _Out_ PFILE_LOCK FileLock
);
````


## -parameters

### -param FileLock [out]

Pointer to an uninitialized <a href="ifsk.file_lock">FILE_LOCK</a> structure. 


## -returns
None


## -remarks
The <a href="ifsk.file_lock">FILE_LOCK</a> structure is opaque: that is, its members are reserved for system use. 

Once initialized, the <a href="ifsk.file_lock">FILE_LOCK</a> structure can be used to lock a byte range in a file by calling <a href="ifsk.fltprocessfilelock">FltProcessFileLock</a>.

It is a programming error to call <b>FltInitializeFileLock</b> for a <a href="ifsk.file_lock">FILE_LOCK</a> structure that has already been initialized by <b>FltInitializeFileLock</b> or <a href="ifsk.fltallocatefilelock">FltAllocateFileLock</a>, unless the structure has been uninitialized by a subsequent call to <a href="ifsk.fltuninitializefilelock">FltUninitializeFileLock</a>.

When the <a href="ifsk.file_lock">FILE_LOCK</a> structure is no longer needed, it can be uninitialized by calling <a href="ifsk.fltuninitializefilelock">FltUninitializeFileLock</a>. The uninitialized <b>FILE_LOCK</b> structure can then be initialized for reuse by calling <b>FltInitializeFileLock</b>.

To allocate and initialize a new opaque <a href="ifsk.file_lock">FILE_LOCK</a> structure, call <a href="ifsk.fltallocatefilelock">FltAllocateFileLock</a>. 

To free an initialized <a href="ifsk.file_lock">FILE_LOCK</a> structure, call <a href="ifsk.fltfreefilelock">FltFreeFileLock</a>. 


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
Available starting with  Windows XP with SP2 or Windows Server 2003 with SP1.

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
<a href="ifsk.file_lock">FILE_LOCK</a>
</dt>
<dt>
<a href="ifsk.fltallocatefilelock">FltAllocateFileLock</a>
</dt>
<dt>
<a href="ifsk.fltchecklockforreadaccess">FltCheckLockForReadAccess</a>
</dt>
<dt>
<a href="ifsk.fltchecklockforwriteaccess">FltCheckLockForWriteAccess</a>
</dt>
<dt>
<a href="ifsk.fltfreefilelock">FltFreeFileLock</a>
</dt>
<dt>
<a href="ifsk.fltprocessfilelock">FltProcessFileLock</a>
</dt>
<dt>
<a href="ifsk.fltuninitializefilelock">FltUninitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltInitializeFileLock routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

