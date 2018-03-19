---
UID: NE:ntddrilapitypes.RILCALLINFOSTATUS
title: RILCALLINFOSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfostatus.htm
old-project: netvista
ms.assetid: 0f5806e8-a7be-4703-8847-abea2d0cb2e8
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILCALLINFOSTATUS, RILCALLINFOSTATUS enumeration [Network Drivers Starting with Windows Vista], RIL_CPISTAT_CONNECTED, RIL_CPISTAT_DISCONNECTED, RIL_CPISTAT_HANDOVER, RIL_CPISTAT_MAX, RIL_CPISTAT_MEDIA, RIL_CPISTAT_NEW_INCOMING, RIL_CPISTAT_NEW_OUTGOING, RIL_CPISTAT_ONHOLD, netvista.rilcallinfostatus, ntddrilapitypes/RILCALLINFOSTATUS, ntddrilapitypes/RIL_CPISTAT_CONNECTED, ntddrilapitypes/RIL_CPISTAT_DISCONNECTED, ntddrilapitypes/RIL_CPISTAT_HANDOVER, ntddrilapitypes/RIL_CPISTAT_MAX, ntddrilapitypes/RIL_CPISTAT_MEDIA, ntddrilapitypes/RIL_CPISTAT_NEW_INCOMING, ntddrilapitypes/RIL_CPISTAT_NEW_OUTGOING, ntddrilapitypes/RIL_CPISTAT_ONHOLD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: Rilapitypes.h
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
-	ntddrilapitypes.h
api_name:
-	RILCALLINFOSTATUS
product: Windows
targetos: Windows
req.typenames: RILCALLINFOSTATUS
---

# RILCALLINFOSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLINFOSTATUS { 
  RIL_CPISTAT_NEW_OUTGOING,
  RIL_CPISTAT_NEW_INCOMING,
  RIL_CPISTAT_CONNECTED,
  RIL_CPISTAT_DISCONNECTED,
  RIL_CPISTAT_ONHOLD,
  RIL_CPISTAT_MEDIA,
  RIL_CPISTAT_HANDOVER,
  RIL_CPISTAT_MAX
} RILCALLINFOSTATUS;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_CPISTAT_UNKNOWN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CPISTAT_NEW_OUTGOING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CPISTAT_NEW_INCOMING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CPISTAT_CONNECTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CPISTAT_DISCONNECTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CPISTAT_ONHOLD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CPISTAT_MEDIA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CPISTAT_HANDOVER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CPISTAT_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |