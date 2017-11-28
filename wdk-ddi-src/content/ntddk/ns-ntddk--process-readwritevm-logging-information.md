---
UID: NS.ntddk._PROCESS_READWRITEVM_LOGGING_INFORMATION
title: PROCESS_READWRITEVM_LOGGING_INFORMATION
author: windows-driver-content
description: Stores options for read/write access for telemetry per process.
old-location: kernel\process_readwritevm_logging_information.htm
old-project: kernel
ms.assetid: F1C769FD-D05F-4C23-A91E-FAEE8EA029EC
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PROCESS_READWRITEVM_LOGGING_INFORMATION, PROCESS_READWRITEVM_LOGGING_INFORMATION, *PPROCESS_READWRITEVM_LOGGING_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PROCESS_READWRITEVM_LOGGING_INFORMATION
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PROCESS_READWRITEVM_LOGGING_INFORMATION structure



## -description
<p>Stores options for read/write access for  telemetry per process. </p>


## -syntax

````
typedef union _PROCESS_READWRITEVM_LOGGING_INFORMATION {
  UCHAR Flags;
  struct {
    UCHAR EnableReadVmLogging  :1;
    UCHAR EnableWriteVmLogging  :1;
    UCHAR Unused  :6;
  };
} PROCESS_READWRITEVM_LOGGING_INFORMATION, *PPROCESS_READWRITEVM_LOGGING_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>EnableReadVmLogging</b>

<dd>
<p>Enables or disables read access. Non-zero values enables telemetry, zero disables it.</p>
</dd>

### -field <b>EnableWriteVmLogging</b>

<dd>
<p>Enables or disables write access. Non-zero values enables telemetry, zero disables it.</p>
</dd>

### -field <b>Unused</b>

<dd>
<p>Do not use.</p>
</dd>
</dl>

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
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
</table>