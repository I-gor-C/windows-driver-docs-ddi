---
UID: NE:ksproxy.KS_LogicalMemoryType
title: KS_LogicalMemoryType
author: windows-driver-content
description: "."
old-location: stream\ks_logicalmemorytype.htm
old-project: stream
ms.assetid: B02E5131-6407-4481-BABD-9F5BDA979D85
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKS_LogicalMemoryType, KS_LogicalMemoryType, KS_LogicalMemoryType enumeration [Streaming Media Devices], KS_MemoryTypeAnyHost, KS_MemoryTypeDeviceHostMapped, KS_MemoryTypeDeviceSpecific, KS_MemoryTypeDontCare, KS_MemoryTypeKernelNonPaged, KS_MemoryTypeKernelPaged, KS_MemoryTypeUser, ksproxy/KS_LogicalMemoryType, ksproxy/KS_MemoryTypeAnyHost, ksproxy/KS_MemoryTypeDeviceHostMapped, ksproxy/KS_MemoryTypeDeviceSpecific, ksproxy/KS_MemoryTypeDontCare, ksproxy/KS_MemoryTypeKernelNonPaged, ksproxy/KS_MemoryTypeKernelPaged, ksproxy/KS_MemoryTypeUser, stream.ks_logicalmemorytype"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ksproxy.h
api_name:
-	KS_LogicalMemoryType
product: Windows
targetos: Windows
req.typenames: KS_LogicalMemoryType
---

# KS_LogicalMemoryType Enumeration


## Syntax
```
typedef enum KS_LogicalMemoryType {
  KS_MemoryTypeDontCare          ,
  KS_MemoryTypeKernelPaged       ,
  KS_MemoryTypeKernelNonPaged    ,
  KS_MemoryTypeDeviceHostMapped  ,
  KS_MemoryTypeDeviceSpecific    ,
  KS_MemoryTypeUser              ,
  KS_MemoryTypeAnyHost
} ;
```

## Constants

<table>
            
                <tr>
                    <td>KS_MemoryTypeDontCare</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KS_MemoryTypeKernelPaged</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KS_MemoryTypeKernelNonPaged</td>
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
                    <td>KS_MemoryTypeUser</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KS_MemoryTypeAnyHost</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksproxy.h |