---
UID: NE:rilapitypes.RILPROVISIONSTATUSPROVISIONSTATUS
title: RILPROVISIONSTATUSPROVISIONSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilprovisionstatusprovisionstatus_2.htm
old-project: netvista
ms.assetid: a0956046-766f-4cb0-9cf7-7cccdf929a2e
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RILPROVISIONSTATUSPROVISIONSTATUS, RILPROVISIONSTATUSPROVISIONSTATUS, rilapitypes/RIL_PROVISIONSTAT_SUCCESS, RILPROVISIONSTATUSPROVISIONSTATUS enumeration [Network Drivers Starting with Windows Vista], netvista.rilprovisionstatusprovisionstatus_2, rilapitypes/RIL_PROVISIONSTAT_FAILURE_END, rilapitypes/RIL_PROVISIONSTAT_MAX, rilapitypes/RIL_PROVISIONSTAT_FAILURE_RETRY, RIL_PROVISIONSTAT_NEEDED, RIL_PROVISIONSTAT_SUCCESS, rilapitypes/RIL_PROVISIONSTAT_NEEDED, RIL_PROVISIONSTAT_BIP_STARTED, RIL_PROVISIONSTAT_BIP_SUCCESS, RIL_PROVISIONSTAT_FAILURE_END, rilapitypes/RIL_PROVISIONSTAT_BIP_SUCCESS, RIL_PROVISIONSTAT_MAX, rilapitypes/RIL_PROVISIONSTAT_BIP_STARTED, RIL_PROVISIONSTAT_FAILURE_RETRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rilapitypes.h
apiname:
-	RILPROVISIONSTATUSPROVISIONSTATUS
product: Windows
targetos: Windows
req.typenames: RILPROVISIONSTATUSPROVISIONSTATUS
req.product: Windows 10 or later.
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
| **Header** | rilapitypes.h |