---
UID: NF.ntddk.IoGetOplockKeyContext
title: IoGetOplockKeyContext
author: windows-driver-content
description: The IoGetOplockKeyContext routine returns a target oplock key context for a file object.
old-location: ifsk\iogetoplockkeycontext.htm
old-project: ifsk
ms.assetid: E93091A2-203B-418D-93E7-1219DED25C52
ms.author: windowsdriverdev
ms.date: 11/14/2017
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
req.iface: 
---

# IoGetOplockKeyContext function



## -description
<p>The <b>IoGetOplockKeyContext</b> routine returns a target oplock key context for a file object.</p>


## -syntax

````
POPLOCK_KEY_ECP_CONTEXT IoGetOplockKeyContextEx(
   PFILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param <i>FileObject</i> 

<dd>
<p>The file object to query for an oplock key context.</p>
</dd>
</dl>

## -returns
<p>An pointer to an <a href="..\ntddk\ns-ntddk--oplock-key-ecp-context.md">OPLOCK_KEY_ECP_CONTEXT</a> structure containing the target oplock key for <i>FileObject</i>. Otherwise, NULL if <i>FileObject</i>  has no target oplock key.</p>

## -remarks
<p>Use the <b>IoGetOplockKeyContext</b> routine only in Windows 7. Because  <a href="..\ntddk\nf-ntddk-iogetoplockkeycontextex.md">IoGetOplockKeyContextEx</a> returns a dual oplock key context, it should be used in Windows 8 and later versions of Windows.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>The <b>IoGetOplockKeyContext</b> routine is available starting with Windows 7.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.dual_oplock_key_ecp_context">DUAL_OPLOCK_KEY_ECP_CONTEXT</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iogetoplockkeycontextex.md">IoGetOplockKeyContextEx</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--oplock-key-ecp-context.md">OPLOCK_KEY_ECP_CONTEXT</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--oplock-key-context.md">OPLOCK_KEY_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoGetOplockKeyContext routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
