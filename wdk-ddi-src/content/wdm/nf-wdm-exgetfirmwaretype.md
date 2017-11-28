---
UID: NF.wdm.ExGetFirmwareType
title: ExGetFirmwareType
author: windows-driver-content
description: Returns the system firmware type.
old-location: kernel\exgetfirmwaretype.htm
old-project: kernel
ms.assetid: b8a420d5-7741-4676-9956-dcf996125c6d
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ExGetFirmwareType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExGetFirmwareType
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
req.irql: <=APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ExGetFirmwareType function



## -description
<p>Returns the system firmware type.</p>


## -syntax

````
FIRMWARE_TYPE ExGetFirmwareType(
   VOID 
);
````


## -parameters


## -returns
<p>Returns a <a href="base.firmware_type">FIRMWARE_TYPE</a>-type value that indicates the type of firmware.</p>

<p>Returns a <a href="base.firmware_type">FIRMWARE_TYPE</a>-type value that indicates the type of firmware.</p>

<p>Returns a <a href="base.firmware_type">FIRMWARE_TYPE</a>-type value that indicates the type of firmware.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
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
<dt>NtosKrnl.exe (kernel mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>