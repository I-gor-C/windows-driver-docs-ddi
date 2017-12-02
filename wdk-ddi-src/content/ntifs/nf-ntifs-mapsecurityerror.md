---
UID: NF.ntifs.MapSecurityError
title: MapSecurityError
author: windows-driver-content
description: The MapSecurityError function maps a security interface SECURITY_STATUS status code to a corresponding NSTATUS status code.
old-location: ifsk\mapsecurityerror.htm
old-project: ifsk
ms.assetid: 899b7d6e-a17b-4030-9512-591b003ca6b2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: MapSecurityError
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MapSecurityError
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
req.irql: Any.
req.iface: 
---

# MapSecurityError function



## -description
<p>The <b>MapSecurityError</b> function maps a security interface SECURITY_STATUS status code to a corresponding NSTATUS status code.</p>


## -syntax

````
NTSTATUS SEC_ENTRY MapSecurityError(
  _In_ SECURITY_STATUS Error
);
````


## -parameters
<dl>

### -param Error [in]

<dd>
<p>The security interface SECURITY_STATUS status code to be mapped.</p>
</dd>
</dl>

## -returns
<p>The NTSTATUS status code corresponding to the input Error status code.</p>

## -remarks
<p>This function maps a security interface status code of type SECURITY_STATUS to a corresponding NSTATUS status code.</p>

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
<p>Available in Microsoft Windows 2000 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
<p>Any.</p>
</td>
</tr>
</table>