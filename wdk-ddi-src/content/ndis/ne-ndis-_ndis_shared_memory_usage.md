---
UID: NE:ndis._NDIS_SHARED_MEMORY_USAGE
title: "_NDIS_SHARED_MEMORY_USAGE"
author: windows-driver-content
description: The NDIS_SHARED_MEMORY_USAGE enumeration specifies how shared memory is used.
old-location: netvista\ndis_shared_memory_usage.htm
old-project: netvista
ms.assetid: c46102dd-26ea-459b-8cc2-f7e2d2e2f2ad
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_SHARED_MEMORY_USAGE, NDIS_SHARED_MEMORY_USAGE, NDIS_SHARED_MEMORY_USAGE enumeration [Network Drivers Starting with Windows Vista], NdisSharedMemoryUsageMax, NdisSharedMemoryUsageOther, NdisSharedMemoryUsageReceive, NdisSharedMemoryUsageReceiveData, NdisSharedMemoryUsageReceiveHeader, NdisSharedMemoryUsageReceiveLookahead, NdisSharedMemoryUsageReceivePostLookahead, NdisSharedMemoryUsageUndefined, NdisSharedMemoryUsageXmit, NdisSharedMemoryUsageXmitData, NdisSharedMemoryUsageXmitHeader, PNDIS_SHARED_MEMORY_USAGE, PNDIS_SHARED_MEMORY_USAGE enumeration pointer [Network Drivers Starting with Windows Vista], _NDIS_SHARED_MEMORY_USAGE, ndis/NDIS_SHARED_MEMORY_USAGE, ndis/NdisSharedMemoryUsageMax, ndis/NdisSharedMemoryUsageOther, ndis/NdisSharedMemoryUsageReceive, ndis/NdisSharedMemoryUsageReceiveData, ndis/NdisSharedMemoryUsageReceiveHeader, ndis/NdisSharedMemoryUsageReceiveLookahead, ndis/NdisSharedMemoryUsageReceivePostLookahead, ndis/NdisSharedMemoryUsageUndefined, ndis/NdisSharedMemoryUsageXmit, ndis/NdisSharedMemoryUsageXmitData, ndis/NdisSharedMemoryUsageXmitHeader, ndis/PNDIS_SHARED_MEMORY_USAGE, ndis_shared_memory_ref_fc268c92-4745-4916-8aab-e1e67e12d217.xml, netvista.ndis_shared_memory_usage"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ndis.h
api_name:
-	NDIS_SHARED_MEMORY_USAGE
product: Windows
targetos: Windows
req.typenames: NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE
---

# _NDIS_SHARED_MEMORY_USAGE Enumeration
The NDIS_SHARED_MEMORY_USAGE enumeration specifies how shared memory is used.

## Syntax
```
typedef enum _NDIS_SHARED_MEMORY_USAGE {
  NdisSharedMemoryUsageUndefined             ,
  NdisSharedMemoryUsageXmit                  ,
  NdisSharedMemoryUsageXmitHeader            ,
  NdisSharedMemoryUsageXmitData              ,
  NdisSharedMemoryUsageReceive               ,
  NdisSharedMemoryUsageReceiveLookahead      ,
  NdisSharedMemoryUsageReceivePostLookahead  ,
  NdisSharedMemoryUsageReceiveHeader         ,
  NdisSharedMemoryUsageReceiveData           ,
  NdisSharedMemoryUsageOther                 ,
  NdisSharedMemoryUsageMax
} NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE;
```

## Constants

<table>
            
                <tr>
                    <td>NdisSharedMemoryUsageUndefined</td>
                    <td>The shared memory application is not defined.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageXmit</td>
                    <td>The shared memory contains transmit data buffers.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageXmitHeader</td>
                    <td>The shared memory contains transmit header buffers.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageXmitData</td>
                    <td>The shared memory contains transmit data.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageReceive</td>
                    <td>The shared memory contains receive data buffers.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageReceiveLookahead</td>
                    <td>The shared memory contains receive lookahead buffers.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageReceivePostLookahead</td>
                    <td>The shared memory contains received post lookahead information.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageReceiveHeader</td>
                    <td>The shared memory contains receive header information.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageReceiveData</td>
                    <td>The shared memory contains receive data.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageOther</td>
                    <td>The shared memory application is not specified.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageMax</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
                </tr>
</table>

## Remarks

The NDIS_SHARED_MEMORY_USAGE enumeration is used in the 
    <a href="https://msdn.microsoft.com/286b08f6-179e-426e-ae65-b108529d049a">
    NDIS_SHARED_MEMORY_PARAMETERS</a> and 
    <a href="https://msdn.microsoft.com/5c14a6ed-3180-41d6-a09a-b3ae0a0c8b36">
    NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.20 and later. Supported in NDIS 6.20 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/5c14a6ed-3180-41d6-a09a-b3ae0a0c8b36">
   NDIS_SCATTER_GATHER_LIST_PARAMETERS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567303">NDIS_SHARED_MEMORY_PARAMETERS</a>