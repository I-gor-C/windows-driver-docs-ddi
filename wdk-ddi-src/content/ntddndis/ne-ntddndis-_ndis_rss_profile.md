---
UID: NE:ntddndis._NDIS_RSS_PROFILE
title: "_NDIS_RSS_PROFILE"
author: windows-driver-content
description: This enumeration is not supported.
old-location: netvista\ndis_rss_profile.htm
old-project: netvista
ms.assetid: 41A58C2C-8A25-41AC-9CBE-59AB38603A73
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PNDIS_RSS_PROFILE, NDIS_RSS_PROFILE, NDIS_RSS_PROFILE enumeration [Network Drivers Starting with Windows Vista], NdisRssProfileClosest, NdisRssProfileClosestStatic, NdisRssProfileConservative, NdisRssProfileMaximum, NdisRssProfileNuma, NdisRssProfileNumaStatic, _NDIS_RSS_PROFILE, netvista.ndis_rss_profile, ntddndis/NDIS_RSS_PROFILE, ntddndis/NdisRssProfileClosest, ntddndis/NdisRssProfileClosestStatic, ntddndis/NdisRssProfileConservative, ntddndis/NdisRssProfileMaximum, ntddndis/NdisRssProfileNuma, ntddndis/NdisRssProfileNumaStatic"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ntddndis.h, Ntddndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
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
-	ntddndis.h
api_name:
-	NDIS_RSS_PROFILE
product: Windows
targetos: Windows
req.typenames: NDIS_RSS_PROFILE, *PNDIS_RSS_PROFILE
---

# _NDIS_RSS_PROFILE Enumeration
This enumeration is not supported.

## Syntax
````
typedef enum _NDIS_RSS_PROFILE { 
  NdisRssProfileClosest        = 1,
  NdisRssProfileClosestStatic,
  NdisRssProfileNuma,
  NdisRssProfileNumaStatic,
  NdisRssProfileConservative,
  NdisRssProfileMaximum
} NDIS_RSS_PROFILE;
````

## Constants

<table>
            
                <tr>
                    <td>NdisRssProfileClosest</td>
                    <td>Default behavior is consistent with that of Windows Server 2008 R2.</td>
                </tr>
            
                <tr>
                    <td>NdisRssProfileClosestStatic</td>
                    <td>No dynamic load balancing. Distribute but don't load-balance at runtime.</td>
                </tr>
            
                <tr>
                    <td>NdisRssProfileNuma</td>
                    <td>Assign RSS CPUs on a round-robin basis across every NUMA node to enable applications that are running on NUMA servers to scale well.</td>
                </tr>
            
                <tr>
                    <td>NdisRssProfileNumaStatic</td>
                    <td>RSS processor selection is the same as for NUMA scalability without dynamic load-balancing.</td>
                </tr>
            
                <tr>
                    <td>NdisRssProfileConservative</td>
                    <td>RSS uses as few processors as possible to sustain the load. This option helps reduce the number of interrupts.</td>
                </tr>
            
                <tr>
                    <td>NdisRssProfileMaximum</td>
                    <td>This enumeration  value is reserved. Do not use.</td>
                </tr>
</table>

## Remarks

The <b>NDIS_RSS_PROFILE</b> enumeration type specifies the current  RSS load balancing profile.

NDIS network drivers use the <b>NDIS_RSS_PROFILE</b> enumeration type to set the value of the <b>RssProfile</b> member of the <a href="..\ntddndis\ns-ntddndis-_ndis_rss_processor_info.md">NDIS_RSS_PROCESSOR_INFO</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.30 and later. Supported in NDIS 6.30 and later. |
| **Header** | ntddndis.h (include Ntddndis.h, Ntddndis.h) |

## See Also

<a href="..\ntddndis\ns-ntddndis-_ndis_rss_processor_info.md">NDIS_RSS_PROCESSOR_INFO</a>



<a href="https://msdn.microsoft.com/0ea0d6f7-0dc5-40dd-a706-4712e19dbfdb">Standardized INF Keywords for RSS</a>



<a href="..\ndis\nf-ndis-ndisgetrssprocessorinformation.md">
   NdisGetRssProcessorInformation</a>