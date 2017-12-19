---
UID: NF.fltkernel.FltCheckLockForReadAccess
title: FltCheckLockForReadAccess function
author: windows-driver-content
description: The FltCheckLockForReadAccess routine determines whether the caller has read access to a locked byte range of a file.
old-location: ifsk\fltchecklockforreadaccess.htm
old-project: ifsk
ms.assetid: 18920aaa-ae43-48ec-a06d-69ccaf75ebd8
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FltCheckLockForReadAccess
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
req.alt-api: FltCheckLockForReadAccess
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

# FltCheckLockForReadAccess function



## -description
The <b>FltCheckLockForReadAccess</b> routine determines whether the caller has read access to a locked byte range of a file.



## -syntax

````
BOOLEAN FltCheckLockForReadAccess(
  _In_ PFILE_LOCK         FileLock,
  _In_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters

### -param FileLock [in]

Pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <a href="ifsk.fltallocatefilelock">FltAllocateFileLock</a> or <a href="ifsk.fltinitializefilelock">FltInitializeFileLock</a>.


### -param CallbackData [in]

Pointer to the callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure for the <a href="ifsk.irp_mj_read">IRP_MJ_READ</a> operation. 


## -returns
<b>FltCheckLockForReadAccess</b> returns <b>TRUE</b> if the process has read access, <b>FALSE</b> otherwise.


## -remarks
This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later. 

<b>FltCheckLockForReadAccess</b> checks whether the caller has read access to the entire byte range indicated in the callback data structure. 

<b>FltCheckLockForReadAccess</b> does not complete the <a href="ifsk.irp_mj_read">IRP_MJ_READ</a> operation. 

To allocate and initialize a new file lock structure, call <a href="ifsk.fltallocatefilelock">FltAllocateFileLock</a>. 

To free an initialized FILE_LOCK structure, call <a href="ifsk.fltfreefilelock">FltFreeFileLock</a>. 


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
<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="ifsk.fltallocatefilelock">FltAllocateFileLock</a>
</dt>
<dt>
<a href="ifsk.fltchecklockforwriteaccess">FltCheckLockForWriteAccess</a>
</dt>
<dt>
<a href="ifsk.fltfreefilelock">FltFreeFileLock</a>
</dt>
<dt>
<a href="ifsk.fltinitializefilelock">FltInitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fltprocessfilelock">FltProcessFileLock</a>
</dt>
<dt>
<a href="ifsk.fltuninitializefilelock">FltUninitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlchecklockforreadaccess">FsRtlCheckLockForReadAccess</a>
</dt>
<dt>
<a href="ifsk.irp_mj_read">IRP_MJ_READ</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCheckLockForReadAccess routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

