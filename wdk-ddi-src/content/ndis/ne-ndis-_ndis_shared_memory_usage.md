---
UID: NE:ndis._NDIS_SHARED_MEMORY_USAGE
title: "_NDIS_SHARED_MEMORY_USAGE"
author: windows-driver-content
description: The NDIS_SHARED_MEMORY_USAGE enumeration specifies how shared memory is used.
old-location: netvista\ndis_shared_memory_usage.htm
old-project: netvista
ms.assetid: c46102dd-26ea-459b-8cc2-f7e2d2e2f2ad
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: ndis/NdisSharedMemoryUsageReceiveHeader, NdisSharedMemoryUsageReceiveHeader, ndis/PNDIS_SHARED_MEMORY_USAGE, ndis/NdisSharedMemoryUsageOther, NdisSharedMemoryUsageUndefined, ndis/NdisSharedMemoryUsageUndefined, ndis/NdisSharedMemoryUsageXmitHeader, NdisSharedMemoryUsageOther, ndis/NDIS_SHARED_MEMORY_USAGE, ndis_shared_memory_ref_fc268c92-4745-4916-8aab-e1e67e12d217.xml, ndis/NdisSharedMemoryUsageReceiveData, NdisSharedMemoryUsageXmitData, PNDIS_SHARED_MEMORY_USAGE, NdisSharedMemoryUsageReceivePostLookahead, PNDIS_SHARED_MEMORY_USAGE enumeration pointer [Network Drivers Starting with Windows Vista], ndis/NdisSharedMemoryUsageReceive, NdisSharedMemoryUsageReceiveData, ndis/NdisSharedMemoryUsageXmitData, *PNDIS_SHARED_MEMORY_USAGE, NdisSharedMemoryUsageMax, ndis/NdisSharedMemoryUsageReceivePostLookahead, netvista.ndis_shared_memory_usage, NdisSharedMemoryUsageXmitHeader, NDIS_SHARED_MEMORY_USAGE, NDIS_SHARED_MEMORY_USAGE enumeration [Network Drivers Starting with Windows Vista], NdisSharedMemoryUsageXmit, ndis/NdisSharedMemoryUsageXmit, NdisSharedMemoryUsageReceive, ndis/NdisSharedMemoryUsageMax, NdisSharedMemoryUsageReceiveLookahead, _NDIS_SHARED_MEMORY_USAGE, ndis/NdisSharedMemoryUsageReceiveLookahead
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ndis.h
apiname:
-	NDIS_SHARED_MEMORY_USAGE
product: Windows
targetos: Windows
req.typenames: "*PNDIS_SHARED_MEMORY_USAGE, NDIS_SHARED_MEMORY_USAGE"
---

# _NDIS_SHARED_MEMORY_USAGE Enumeration
The NDIS_SHARED_MEMORY_USAGE enumeration specifies how shared memory is used.

## Syntax
````
typedef enum _NDIS_SHARED_MEMORY_USAGE { 
  NdisSharedMemoryUsageUndefined,
  NdisSharedMemoryUsageXmit,
  NdisSharedMemoryUsageXmitHeader,
  NdisSharedMemoryUsageXmitData,
  NdisSharedMemoryUsageReceive,
  NdisSharedMemoryUsageReceiveLookahead,
  NdisSharedMemoryUsageReceivePostLookahead,
  NdisSharedMemoryUsageReceiveHeader,
  NdisSharedMemoryUsageReceiveData,
  NdisSharedMemoryUsageOther,
  NdisSharedMemoryUsageMax
} NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE;
````

## Constants

<table>
            
                <tr>
                    <td>NdisSharedMemoryUsageMax</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageOther</td>
                    <td>The shared memory application is not specified.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageReceive</td>
                    <td>The shared memory contains receive data buffers.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageReceiveData</td>
                    <td>The shared memory contains receive data.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageReceiveHeader</td>
                    <td>The shared memory contains receive header information.</td>
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
                    <td>NdisSharedMemoryUsageUndefined</td>
                    <td>The shared memory application is not defined.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageXmit</td>
                    <td>The shared memory contains transmit data buffers.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageXmitData</td>
                    <td>The shared memory contains transmit data.</td>
                </tr>
            
                <tr>
                    <td>NdisSharedMemoryUsageXmitHeader</td>
                    <td>The shared memory contains transmit header buffers.</td>
                </tr>
</table>

    ## Remarks

        The NDIS_SHARED_MEMORY_USAGE enumeration is used in the 
    <a href="..\ndis\ns-ndis-_ndis_shared_memory_parameters.md">
    NDIS_SHARED_MEMORY_PARAMETERS</a> and 
    <a href="..\ndis\ns-ndis-_ndis_scatter_gather_list_parameters.md">
    NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.20 and later. Supported in NDIS 6.20 and later. |
| **Header** | ndis.h (include Ndis.h) |

    ## See Also

        <a href="..\ndis\ns-ndis-_ndis_shared_memory_parameters.md">NDIS_SHARED_MEMORY_PARAMETERS</a>



<a href="..\ndis\ns-ndis-_ndis_scatter_gather_list_parameters.md">
   NDIS_SCATTER_GATHER_LIST_PARAMETERS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SHARED_MEMORY_USAGE enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>