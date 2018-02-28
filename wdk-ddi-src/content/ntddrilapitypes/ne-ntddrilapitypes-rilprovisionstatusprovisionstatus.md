---
UID: NE:ntddrilapitypes.RILPROVISIONSTATUSPROVISIONSTATUS
title: RILPROVISIONSTATUSPROVISIONSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilprovisionstatusprovisionstatus.htm
old-project: netvista
ms.assetid: ed7fc20a-b5d5-4dc6-ab95-5ee9258dbdae
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RILPROVISIONSTATUSPROVISIONSTATUS, RILPROVISIONSTATUSPROVISIONSTATUS enumeration [Network Drivers Starting with Windows Vista], RIL_PROVISIONSTAT_BIP_STARTED, RIL_PROVISIONSTAT_BIP_SUCCESS, RIL_PROVISIONSTAT_FAILURE_END, RIL_PROVISIONSTAT_FAILURE_RETRY, RIL_PROVISIONSTAT_MAX, RIL_PROVISIONSTAT_NEEDED, RIL_PROVISIONSTAT_SUCCESS, netvista.rilprovisionstatusprovisionstatus, ntddrilapitypes/RILPROVISIONSTATUSPROVISIONSTATUS, ntddrilapitypes/RIL_PROVISIONSTAT_BIP_STARTED, ntddrilapitypes/RIL_PROVISIONSTAT_BIP_SUCCESS, ntddrilapitypes/RIL_PROVISIONSTAT_FAILURE_END, ntddrilapitypes/RIL_PROVISIONSTAT_FAILURE_RETRY, ntddrilapitypes/RIL_PROVISIONSTAT_MAX, ntddrilapitypes/RIL_PROVISIONSTAT_NEEDED, ntddrilapitypes/RIL_PROVISIONSTAT_SUCCESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
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
-	ntddrilapitypes.h
api_name:
-	RILPROVISIONSTATUSPROVISIONSTATUS
product: Windows
targetos: Windows
req.typenames: RILPROVISIONSTATUSPROVISIONSTATUS
---

# RILPROVISIONSTATUSPROVISIONSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPROVISIONSTATUSPROVISIONSTATUS { 
  RIL_PROVISIONSTAT_SUCCESS,
  RIL_PROVISIONSTAT_FAILURE_END,
  RIL_PROVISIONSTAT_FAILURE_RETRY,
  RIL_PROVISIONSTAT_NEEDED,
  RIL_PROVISIONSTAT_BIP_STARTED,
  RIL_PROVISIONSTAT_BIP_SUCCESS,
  RIL_PROVISIONSTAT_MAX
} RILPROVISIONSTATUSPROVISIONSTATUS;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PROVISIONSTAT_BIP_STARTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PROVISIONSTAT_BIP_SUCCESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PROVISIONSTAT_FAILURE_END</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PROVISIONSTAT_FAILURE_RETRY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PROVISIONSTAT_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PROVISIONSTAT_NEEDED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PROVISIONSTAT_STARTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PROVISIONSTAT_SUCCESS</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |