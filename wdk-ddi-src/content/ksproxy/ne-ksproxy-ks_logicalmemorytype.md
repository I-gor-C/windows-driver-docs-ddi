---
UID : NE:ksproxy.KS_LogicalMemoryType
title : KS_LogicalMemoryType
author : windows-driver-content
description : "."
old-location : stream\ks_logicalmemorytype.htm
old-project : stream
ms.assetid : B02E5131-6407-4481-BABD-9F5BDA979D85
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KS_LogicalMemoryType enumeration [Streaming Media Devices], KS_LogicalMemoryType, KS_MemoryTypeKernelPaged, KS_MemoryTypeDeviceSpecific, KS_MemoryTypeKernelNonPaged, ksproxy/KS_LogicalMemoryType, ksproxy/KS_MemoryTypeDontCare, KS_MemoryTypeDontCare, KS_MemoryTypeUser, ksproxy/KS_MemoryTypeDeviceSpecific, ksproxy/KS_MemoryTypeAnyHost, ksproxy/KS_MemoryTypeUser, ksproxy/KS_MemoryTypeKernelNonPaged, stream.ks_logicalmemorytype, *PKS_LogicalMemoryType, ksproxy/KS_MemoryTypeKernelPaged, KS_MemoryTypeDeviceHostMapped, ksproxy/KS_MemoryTypeDeviceHostMapped, KS_MemoryTypeAnyHost
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ksproxy.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : KS_LogicalMemoryType
---

# KS_LogicalMemoryType Enumeration


## Syntax
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

## Constants

<table>

<tr>
<td>KS_MemoryTypeAnyHost</td>
<td></td>
</tr>

<tr>
<td>KS_MemoryTypeDeviceHostMapped</td>
<td></td>
</tr>

<tr>
<td>KS_MemoryTypeDeviceSpecific</td>
<td></td>
</tr>

<tr>
<td>KS_MemoryTypeDontCare</td>
<td></td>
</tr>

<tr>
<td>KS_MemoryTypeKernelNonPaged</td>
<td></td>
</tr>

<tr>
<td>KS_MemoryTypeKernelPaged</td>
<td></td>
</tr>

<tr>
<td>KS_MemoryTypeUser</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h |