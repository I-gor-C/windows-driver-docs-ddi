---
UID: NF.ntifs.FsRtlIsEcpFromUserMode
title: FsRtlIsEcpFromUserMode function
author: windows-driver-content
description: The FsRtlIsEcpFromUserMode routine determines whether an extra create parameter (ECP) context structure originated from user mode.
old-location: ifsk\fsrtlisecpfromusermode.htm
old-project: ifsk
ms.assetid: cdc5d6a3-637e-4f0e-bc94-25bfe5763695
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlIsEcpFromUserMode
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: FsRtlIsEcpFromUserMode is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIsEcpFromUserMode
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
req.irql: <= APC_LEVEL
---

# FsRtlIsEcpFromUserMode function



## -description
The <b>FsRtlIsEcpFromUserMode</b> routine determines whether an extra create parameter (ECP) context structure originated from user mode. 



## -syntax

````
BOOLEAN FsRtlIsEcpFromUserMode(
  _In_ PVOID EcpContext
);
````


## -parameters

### -param EcpContext [in]

Pointer to the ECP context structure to test. 


## -returns
<b>FsRtlIsEcpFromUserMode</b> returns <b>TRUE</b> if the ECP context structure originated in user mode and <b>FALSE</b> if the ECP context structure originated in kernel mode. 


## -remarks


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
FsRtlIsEcpFromUserMode is available starting with Windows Vista. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
&lt;= APC_LEVEL

</td>
</tr>
</table>