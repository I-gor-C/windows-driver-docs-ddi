---
UID: NS.ntddk._PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
title: PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
author: windows-driver-content
description: Stores information about process mitigation policy.
old-location: kernel\process_mitigation_payload_restriction_policy.htm
old-project: kernel
ms.assetid: f55a47b2-c95c-4b6c-aeff-aed99dd9e43b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, *PPROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
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
req.alt-api: PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
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

# PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY structure



## -description
<p>Stores information about process mitigation policy.</p>


## -syntax

````
typedef struct _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY {
  union {
    ULONG Flags;
    struct {
      ULONG EnableExportAddressFilter  :1;
      ULONG AuditExportAddressFilter  :1;
      ULONG EnableExportAddressFilterPlus  :1;
      ULONG AuditExportAddressFilterPlus  :1;
      ULONG EnableImportAddressFilter  :1;
      ULONG AuditImportAddressFilter  :1;
      ULONG EnableRopStackPivot  :1;
      ULONG AuditRopStackPivot  :1;
      ULONG EnableRopCallerCheck  :1;
      ULONG AuditRopCallerCheck  :1;
      ULONG EnableRopSimExec  :1;
      ULONG AuditRopSimExec  :1;
      ULONG ReservedFlags  :20;
    } DUMMYSTRUCTNAME;
  } DUMMYUNIONNAME;
} PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY, PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY;
````


## -struct-fields
<dl>

### -field DUMMYUNIONNAME

<dd>
<dl>

### -field Flags

<dd>
<p>Bitwise of flags in this structure.</p>
</dd>

### -field DUMMYSTRUCTNAME

<dd>
<dl>

### -field EnableExportAddressFilter

<dd>
<p>If set this enables the Export Address Filter mitigation in enforcement mode for the process.</p>
</dd>

### -field AuditExportAddressFilter

<dd>
<p>If set this enables the Export Address Filter mitigation in audit mode for the process.</p>
</dd>

### -field EnableExportAddressFilterPlus

<dd>
<p>If set this enables the Export Address Filter Plus mitigation in enforcement mode for the process.</p>
</dd>

### -field AuditExportAddressFilterPlus

<dd>
<p>If set this enables the Export Address Filter mitigation in audit mode for the process.</p>
</dd>

### -field EnableImportAddressFilter

<dd>
<p>If set this enables the Import Address Filter mitigation in enforcement mode for the process.</p>
</dd>

### -field AuditImportAddressFilter

<dd>
<p>If set this enables the Import Address Filter mitigation in enforcement mode for the process.</p>
</dd>

### -field EnableRopStackPivot

<dd>
<p>If set this enables the stack pivot anti-ROP (Return-oriented-programming) mitigation in enforcement mode for the process.</p>
</dd>

### -field AuditRopStackPivot

<dd>
<p>If set this enables the stack pivot anti-ROP (Return-oriented-programming) mitigation in audit mode for the process.</p>
</dd>

### -field EnableRopCallerCheck

<dd>
<p>If set this enables the caller check anti-ROP (Return-oriented-programming) mitigation in enforcement mode for the process. Applies to 32-bit processes only.</p>
</dd>

### -field AuditRopCallerCheck

<dd>
<p>If set this enables the caller check anti-ROP (Return-oriented-programming) mitigation in audit mode for the process. Applies to 32-bit processes only.</p>
</dd>

### -field EnableRopSimExec

<dd>
<p>If set this enables the simulated execution anti-ROP (Return-oriented-programming) mitigation in enforcement mode for the process. Applies to 32-bit processes only.</p>
</dd>

### -field AuditRopSimExec

<dd>
<p>If set this enables the simulated execution anti-ROP (Return-oriented-programming) mitigation in audit mode for the process. Applies to 32-bit processes only.</p>
</dd>

### -field ReservedFlags

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>
</dl>
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