---
UID: NE:ntddrilapitypes.RILCAPSTYPE
title: RILCAPSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcapstype.htm
old-project: netvista
ms.assetid: 78f372fc-75b2-47e8-ac3f-818b384c6d97
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RILCAPSTYPE, ntddrilapitypes/RIL_CAPSTYPE_PBSTORELOCATIONS, ntddrilapitypes/RIL_CAPSTYPE_NITZNOTIFICATION, RIL_CAPSTYPE_PBMAXREAD, RIL_CAPSTYPE_NITZNOTIFICATION, ntddrilapitypes/RIL_CAPSTYPE_SIGNALQUALITYIMPLEMENTATION, ntddrilapitypes/RIL_CAPSTYPE_ARG_SMALLEST, ntddrilapitypes/RIL_CAPSTYPE_SMSSUPPORT, ntddrilapitypes/RIL_CAPSTYPE_MAX, RIL_CAPSTYPE_PBSTORELOCATIONS, RIL_CAPSTYPE_ARG_SMALLEST, ntddrilapitypes/RIL_CAPSTYPE_PERSOLOCKPWDLENGTH, ntddrilapitypes/RIL_CAPSTYPE_CALLSUPPORT, ntddrilapitypes/RIL_CAPSTYPE_ARG_LARGEST, RIL_CAPSTYPE_PERSOLOCKPWDLENGTH, netvista.rilcapstype, RIL_CAPSTYPE_RADIOCONFIGURATIONS, ntddrilapitypes/RIL_CAPSTYPE_RADIOCONFIGURATIONS, RIL_CAPSTYPE_ARG_LARGEST, RIL_CAPSTYPE_MAX, RIL_CAPSTYPE_SIGNALQUALITYIMPLEMENTATION, RILCAPSTYPE enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_CAPSTYPE_PBMAXREAD, RIL_CAPSTYPE_SMSSUPPORT, RIL_CAPSTYPE_CALLSUPPORT, ntddrilapitypes/RILCAPSTYPE
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddrilapitypes.h
apiname:
-	RILCAPSTYPE
product: Windows
targetos: Windows
req.typenames: RILCAPSTYPE
---

# RILCAPSTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCAPSTYPE { 
  RIL_CAPSTYPE_PERSOLOCKPWDLENGTH,
  RIL_CAPSTYPE_PBMAXREAD,
  RIL_CAPSTYPE_PBSTORELOCATIONS,
  RIL_CAPSTYPE_RADIOCONFIGURATIONS,
  RIL_CAPSTYPE_SIGNALQUALITYIMPLEMENTATION,
  RIL_CAPSTYPE_NITZNOTIFICATION,
  RIL_CAPSTYPE_CALLSUPPORT,
  RIL_CAPSTYPE_SMSSUPPORT,
  RIL_CAPSTYPE_ARG_SMALLEST,
  RIL_CAPSTYPE_ARG_LARGEST,
  RIL_CAPSTYPE_MAX
} RILCAPSTYPE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_CAPSTYPE_ARG_LARGEST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_ARG_SMALLEST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_CALLSUPPORT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_NITZNOTIFICATION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_PBMAXREAD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_PBSTORELOCATIONS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_PERSOLOCKPWDLENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_PERSOLOCKSUPPORT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_RADIOCONFIGURATIONS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_SIGNALQUALITYIMPLEMENTATION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CAPSTYPE_SMSSUPPORT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |