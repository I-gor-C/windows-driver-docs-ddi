---
UID: NF.fltkernel.FltReleaseFileNameInformation
title: FltReleaseFileNameInformation function
author: windows-driver-content
description: FltReleaseFileNameInformation releases a file name information structure.
old-location: ifsk\fltreleasefilenameinformation.htm
old-project: ifsk
ms.assetid: 352dbab6-76c3-4e67-a226-4c3d83fbb3b6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltReleaseFileNameInformation
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
req.alt-api: FltReleaseFileNameInformation
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

# FltReleaseFileNameInformation function



## -description
<b>FltReleaseFileNameInformation</b> releases a file name information structure. 


## -syntax

````
VOID FltReleaseFileNameInformation(
  _In_ PFLT_FILE_NAME_INFORMATION FileNameInformation
);
````


## -parameters

### -param FileNameInformation [in]

Pointer to the FLT_FILE_NAME_INFORMATION structure to be released. This parameter is required and cannot be <b>NULL</b>. 

## -returns
None 

## -remarks
<b>FltReleaseFileNameInformation</b> decrements the reference count on a file name information (<a href="ifsk.flt_file_name_information">FLT_FILE_NAME_INFORMATION</a>) structure returned by a previous call to <a href="ifsk.fltgetdestinationfilenameinformation">FltGetDestinationFileNameInformation</a>, <a href="ifsk.fltgetfilenameinformation">FltGetFileNameInformation</a>, <a href="ifsk.fltgetfilenameinformationunsafe">FltGetFileNameInformationUnsafe</a>, or <a href="ifsk.fltgettunneledname">FltGetTunneledName</a>. When this reference count reaches zero, the structure is freed. 

To increment the reference count on a file name information structure, call <a href="ifsk.fltreferencefilenameinformation">FltReferenceFileNameInformation</a>. 

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
<a href="ifsk.flt_file_name_information">FLT_FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.fltgetdestinationfilenameinformation">FltGetDestinationFileNameInformation</a>
</dt>
<dt>
<a href="ifsk.fltgetfilenameinformation">FltGetFileNameInformation</a>
</dt>
<dt>
<a href="ifsk.fltgetfilenameinformationunsafe">FltGetFileNameInformationUnsafe</a>
</dt>
<dt>
<a href="ifsk.fltgettunneledname">FltGetTunneledName</a>
</dt>
<dt>
<a href="ifsk.fltreferencefilenameinformation">FltReferenceFileNameInformation</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltReleaseFileNameInformation function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
