---
UID: NF.ntifs.SeFreePrivileges
title: SeFreePrivileges
author: windows-driver-content
description: The SeFreePrivileges routine frees a privilege set returned by SeAccessCheck.
old-location: kernel\sefreeprivileges.htm
ms.assetid: 5b8ba64e-3147-45b4-9861-da2186c2ba10
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeFreePrivileges
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: SeFreePrivileges
req.iface: 
---

# SeFreePrivileges function



## -description
<p>The <b>SeFreePrivileges</b> routine frees a privilege set returned by <b>SeAccessCheck</b>.</p>


## -syntax

````
VOID SeFreePrivileges(
  _In_ PPRIVILEGE_SET Privileges
);
````


## -parameters
<dl>

### -param <i>Privileges</i> [in]

<dd>
<p>Pointer to the privilege set to be freed.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK. </p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551860">PRIVILEGE_SET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563674">SeAccessCheck</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554762">SeAppendPrivileges</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556686">SePrivilegeCheck</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20SeFreePrivileges routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
