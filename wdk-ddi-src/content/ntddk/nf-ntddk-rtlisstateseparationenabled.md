---
UID: NF.ntddk.RtlIsStateSeparationEnabled
title: RtlIsStateSeparationEnabled function
author: windows-driver-content
description: Checks if the SKU for the current context supports multiple sessions.
old-location: kernel\rtlisstateseparationenabled.htm
old-project: kernel
ms.assetid: 7c28a82c-e039-4045-94cd-b47a45d15e28
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: RtlIsStateSeparationEnabled
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlIsStateSeparationEnabled
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode)
req.irql: PASSIVE_LEVEL
---

# RtlIsStateSeparationEnabled function



## -description

			
            Checks if the SKU for the current context supports multiple
    sessions.




## -syntax

````
 BOOLEAN  RtlIsStateSeparationEnabled(
   VOID 
);
````


## -parameters


## -returns
 TRUE indicates state separation enabled;

    FALSE otherwise.

 TRUE indicates state separation enabled;

    FALSE otherwise.

 TRUE indicates state separation enabled;

    FALSE otherwise.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10, version 1709

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

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
<dt>NtosKrnl.exe (kernel mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>