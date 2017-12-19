---
UID: NF.fltkernel.FltFreeSecurityDescriptor
title: FltFreeSecurityDescriptor function
author: windows-driver-content
description: FltFreeSecurityDescriptor frees a security descriptor allocated by the FltBuildDefaultSecurityDescriptor routine.
old-location: ifsk\fltfreesecuritydescriptor.htm
old-project: ifsk
ms.assetid: ebf7ad37-6c3b-4216-87e6-ea5d6a0cba20
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FltFreeSecurityDescriptor
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
req.alt-api: FltFreeSecurityDescriptor
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

# FltFreeSecurityDescriptor function



## -description
<b>FltFreeSecurityDescriptor</b> frees a security descriptor allocated by the <a href="ifsk.fltbuilddefaultsecuritydescriptor">FltBuildDefaultSecurityDescriptor</a> routine. 



## -syntax

````
VOID FltFreeSecurityDescriptor(
  _In_ PSECURITY_DESCRIPTOR SecurityDescriptor
);
````


## -parameters

### -param SecurityDescriptor [in]

Opaque pointer to the security descriptor (<a href="ifsk.security_descriptor">SECURITY_DESCRIPTOR</a>) to be freed. 


## -returns
None 


## -remarks
<b>FltFreeSecurityDescriptor</b> should only be used to free a security descriptor that was allocated by a previous call to <a href="ifsk.fltbuilddefaultsecuritydescriptor">FltBuildDefaultSecurityDescriptor</a>. 


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
<a href="ifsk.fltbuilddefaultsecuritydescriptor">FltBuildDefaultSecurityDescriptor</a>
</dt>
<dt>
<a href="ifsk.security_descriptor">SECURITY_DESCRIPTOR</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltFreeSecurityDescriptor routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

