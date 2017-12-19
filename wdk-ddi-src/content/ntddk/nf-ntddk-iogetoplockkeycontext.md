---
UID: NF.ntddk.IoGetOplockKeyContext
title: IoGetOplockKeyContext function
author: windows-driver-content
description: The IoGetOplockKeyContext routine returns a target oplock key context for a file object.
old-location: ifsk\iogetoplockkeycontext.htm
old-project: ifsk
ms.assetid: E93091A2-203B-418D-93E7-1219DED25C52
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IoGetOplockKeyContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: The IoGetOplockKeyContext routine is available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetOplockKeyContextEx
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# IoGetOplockKeyContext function



## -description
The <b>IoGetOplockKeyContext</b> routine returns a target oplock key context for a file object.



## -syntax

````
POPLOCK_KEY_ECP_CONTEXT IoGetOplockKeyContextEx(
   PFILE_OBJECT FileObject
);
````


## -parameters

### -param FileObject 

The file object to query for an oplock key context.


## -returns
An pointer to an <a href="ifsk.oplock_key_ecp_context">OPLOCK_KEY_ECP_CONTEXT</a> structure containing the target oplock key for <i>FileObject</i>. Otherwise, NULL if <i>FileObject</i>  has no target oplock key.


## -remarks
Use the <b>IoGetOplockKeyContext</b> routine only in Windows 7. Because  <a href="ifsk.iogetoplockkeycontextex">IoGetOplockKeyContextEx</a> returns a dual oplock key context, it should be used in Windows 8 and later versions of Windows.


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
The <b>IoGetOplockKeyContext</b> routine is available starting with Windows 7.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.dual_oplock_key_ecp_context">DUAL_OPLOCK_KEY_ECP_CONTEXT</a>
</dt>
<dt>
<a href="ifsk.iogetoplockkeycontextex">IoGetOplockKeyContextEx</a>
</dt>
<dt>
<a href="ifsk.oplock_key_ecp_context">OPLOCK_KEY_ECP_CONTEXT</a>
</dt>
<dt>
<a href="ifsk.oplock_key_context">OPLOCK_KEY_CONTEXT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoGetOplockKeyContext routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

