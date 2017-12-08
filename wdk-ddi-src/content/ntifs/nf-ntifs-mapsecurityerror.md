---
UID: NF.ntifs.MapSecurityError
title: MapSecurityError function
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
---

# MapSecurityError function



## -description
The <b>MapSecurityError</b> function maps a security interface SECURITY_STATUS status code to a corresponding NSTATUS status code.


## -syntax

````
NTSTATUS SEC_ENTRY MapSecurityError(
  _In_ SECURITY_STATUS Error
);
````


## -parameters

### -param Error [in]

The security interface SECURITY_STATUS status code to be mapped.

## -returns
The NTSTATUS status code corresponding to the input Error status code.

## -remarks
This function maps a security interface status code of type SECURITY_STATUS to a corresponding NSTATUS status code.

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
Available in Microsoft Windows 2000 and later.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any.
</td>
</tr>
</table>