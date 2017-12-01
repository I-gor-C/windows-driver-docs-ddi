---
UID: NE.ksproxy.KS_LogicalMemoryType
title: KS_LogicalMemoryType
author: windows-driver-content
description: .
old-location: stream\ks_logicalmemorytype.htm
old-project: stream
ms.assetid: B02E5131-6407-4481-BABD-9F5BDA979D85
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagTRANSPORTVIDEOPARMS, TRANSPORTVIDEOPARMS, *PTRANSPORTVIDEOPARMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksproxy.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_LogicalMemoryType
req.alt-loc: Ksproxy.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# KS_LogicalMemoryType enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KS_MemoryTypeDontCare          = 0,
  KS_MemoryTypeKernelPaged,
  KS_MemoryTypeKernelNonPaged,
  KS_MemoryTypeDeviceHostMapped,
  KS_MemoryTypeDeviceSpecific,
  KS_MemoryTypeUser,
  KS_MemoryTypeAnyHost
} KS_LogicalMemoryType;
````


## -enum-fields
<dl>

### -field <a id="KS_MemoryTypeDontCare"></a><a id="ks_memorytypedontcare"></a><a id="KS_MEMORYTYPEDONTCARE"></a><b>KS_MemoryTypeDontCare</b>

<dd></dd>

### -field <a id="KS_MemoryTypeKernelPaged"></a><a id="ks_memorytypekernelpaged"></a><a id="KS_MEMORYTYPEKERNELPAGED"></a><b>KS_MemoryTypeKernelPaged</b>

<dd></dd>

### -field <a id="KS_MemoryTypeKernelNonPaged"></a><a id="ks_memorytypekernelnonpaged"></a><a id="KS_MEMORYTYPEKERNELNONPAGED"></a><b>KS_MemoryTypeKernelNonPaged</b>

<dd></dd>

### -field <a id="KS_MemoryTypeDeviceHostMapped"></a><a id="ks_memorytypedevicehostmapped"></a><a id="KS_MEMORYTYPEDEVICEHOSTMAPPED"></a><b>KS_MemoryTypeDeviceHostMapped</b>

<dd></dd>

### -field <a id="KS_MemoryTypeDeviceSpecific"></a><a id="ks_memorytypedevicespecific"></a><a id="KS_MEMORYTYPEDEVICESPECIFIC"></a><b>KS_MemoryTypeDeviceSpecific</b>

<dd></dd>

### -field <a id="KS_MemoryTypeUser"></a><a id="ks_memorytypeuser"></a><a id="KS_MEMORYTYPEUSER"></a><b>KS_MemoryTypeUser</b>

<dd></dd>

### -field <a id="KS_MemoryTypeAnyHost"></a><a id="ks_memorytypeanyhost"></a><a id="KS_MEMORYTYPEANYHOST"></a><b>KS_MemoryTypeAnyHost</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h</dt>
</dl>
</td>
</tr>
</table>