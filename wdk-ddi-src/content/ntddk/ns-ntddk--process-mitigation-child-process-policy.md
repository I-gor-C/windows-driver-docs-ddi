---
UID: NS.ntddk._PROCESS_MITIGATION_CHILD_PROCESS_POLICY
title: PROCESS_MITIGATION_CHILD_PROCESS_POLICY
author: windows-driver-content
description: Stores policy information about creating child processes.
old-location: kernel\process_mitigation_child_process_policy.htm
old-project: kernel
ms.assetid: 8f388c0e-41ee-40e4-b633-687eeff74a0a
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PROCESS_MITIGATION_CHILD_PROCESS_POLICY, PROCESS_MITIGATION_CHILD_PROCESS_POLICY, *PPROCESS_MITIGATION_CHILD_PROCESS_POLICY
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
req.alt-api: PROCESS_MITIGATION_CHILD_PROCESS_POLICY
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

# PROCESS_MITIGATION_CHILD_PROCESS_POLICY structure



## -description
<p>Stores policy information about creating child processes.</p>


## -syntax

````
typedef struct _PROCESS_MITIGATION_CHILD_PROCESS_POLICY {
  union {
    struct {
      ULONG NoChildProcessCreation  :1;
      ULONG AuditNoChildProcessCreation  :1;
      ULONG AllowSecureProcessCreation  :1;
      ULONG ReservedFlags  :29;
    } DUMMYSTRUCTNAME;
  } DUMMYUNIONNAME;
} PROCESS_MITIGATION_CHILD_PROCESS_POLICY, PROCESS_MITIGATION_CHILD_PROCESS_POLICY;
````


## -struct-fields
<dl>

### -field <b>DUMMYUNIONNAME</b>

<dd>
<dl>

### -field <b>DUMMYSTRUCTNAME</b>

<dd>
<dl>

### -field <b>NoChildProcessCreation</b>

<dd>
<p>If set, the process cannot create child processes.</p>
</dd>

### -field <b>AuditNoChildProcessCreation</b>

<dd>
<p>If set, causes audit events to be generated when child processes are created by the process. If both <b>NoChildProcessCreation</b> and <b>AuditNoChildProcessCreation</b> are set, <b>NoChildProcessCreation</b> takes precedence over audit setting.</p>
</dd>

### -field <b>AllowSecureProcessCreation</b>

<dd>
<p>Denies creation of child processes unless the child process is a secure process and if creation was previously blocked. It allows a process to spawn a child process on behalf of another process that cannot itself create child processes. See PROCESS_CREATION_CHILD_PROCESS_OVERRIDE in <a href="base.updateprocthreadattribute">UpdateProcThreadAttribute</a>.</p>
</dd>

### -field <b>ReservedFlags</b>

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