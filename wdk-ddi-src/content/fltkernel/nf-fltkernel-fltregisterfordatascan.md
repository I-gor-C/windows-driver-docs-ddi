---
UID: NF.fltkernel.FltRegisterForDataScan
title: FltRegisterForDataScan function
author: windows-driver-content
description: The FltRegisterForDataScan routine enables data scanning for the volume attached to the minifilter instance.
old-location: ifsk\fltregisterfordatascan.htm
old-project: ifsk
ms.assetid: E603975A-B927-475A-9DEA-2D01C1249819
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltRegisterForDataScan
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: The FltRegisterForDataScan routine is available starting with   Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltRegisterForDataScan
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

# FltRegisterForDataScan function



## -description
The <b>FltRegisterForDataScan</b> routine enables data scanning for the volume attached to the minifilter instance.



## -syntax

````
NTSTATUS FltRegisterForDataScan(
  _In_ PFLT_INSTANCE Instance
);
````


## -parameters

### -param Instance [in]

An opaque instance pointer for the minifilter driver instance to register for data scanning.


## -returns
<b>FltRegisterForDataScan</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as one of the following. 
<dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl>The filter manager does not support data scans for the volume attached to this instance.

 


## -remarks
If <b>STATUS_NOT_SUPPORTED</b> is returned by <b>FltRegisterForDataScan</b>, a minifilter can still create sections for data scanning using <a href="ifsk.fsrtlcreatesectionfordatascan">FsRtlCreateSectionForDataScan</a>. However, section access is not synchronized and conflict resolution is left to the minifilter driver.


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
The <b>FltRegisterForDataScan</b> routine is available starting with   Windows 8.

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
<a href="ifsk.fltclosesectionfordatascan">FltCloseSectionForDataScan</a>
</dt>
<dt>
<a href="ifsk.fltcreatesectionfordatascan">FltCreateSectionForDataScan</a>
</dt>
<dt>
<a href="ifsk.fsrtlcreatesectionfordatascan">FsRtlCreateSectionForDataScan</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltRegisterForDataScan routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

