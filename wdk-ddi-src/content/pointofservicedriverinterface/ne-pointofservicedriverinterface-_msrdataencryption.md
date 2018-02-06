---
UID: NE:pointofservicedriverinterface._MsrDataEncryption
title: "_MsrDataEncryption"
author: windows-driver-content
description: This enumeration defines the kind of encryption algorithm supported by the magnetic stripe reader (MSR).
old-location: pos\msrdataencryption.htm
old-project: pos
ms.assetid: 3e587242-2d7e-4b1f-8fcd-e0acada91524
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: MsrDataEncryption enumeration, MsrDataEncryption_AES, MsrDataEncryption, MsrDataEncryption_ExtendedBase, pos.msrdataencryption, pointofservicedriverinterface/MsrDataEncryption_None, _MsrDataEncryption, MsrDataEncryption_3DEA_DUKPT, pointofservicedriverinterface/MsrDataEncryption, pointofservicedriverinterface/MsrDataEncryption_ExtendedBase, pointofservicedriverinterface/MsrDataEncryption_AES, MsrDataEncryption_None, pointofservicedriverinterface/MsrDataEncryption_3DEA_DUKPT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pointofservicedriverinterface.h
req.include-header: Pointofservicedriverinterface.h
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
req.irql: Called at PASSIVE_LEVEL.
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	pointofservicedriverinterface.h
apiname:
-	MsrDataEncryption
product: Windows
targetos: Windows
req.typenames: MsrDataEncryption
---

# _MsrDataEncryption Enumeration
This enumeration defines the kind of encryption algorithm supported by the magnetic stripe reader (MSR).

## Syntax
````
typedef enum _MsrDataEncryption { 
  MsrDataEncryption_None,
  MsrDataEncryption_3DEA_DUKPT,
  MsrDataEncryption_AES,
  MsrDataEncryption_ExtendedBase
} MsrDataEncryption;
````

## Constants

<table>
            
                <tr>
                    <td>MsrDataEncryption_3DEA_DUKPT</td>
                    <td>The Triple Data Encryption Standard (DES) Derived Unique Key Per Transaction (DUKPT) encryption algorithm.</td>
                </tr>
            
                <tr>
                    <td>MsrDataEncryption_AES</td>
                    <td>The Advanced Encryption Standard (AES).</td>
                </tr>
            
                <tr>
                    <td>MsrDataEncryption_ExtendedBase</td>
                    <td>A vendor-specific encryption algorithm. Service-specific values begin at 0x01000000 and are reserved for additional encryption algorithms.</td>
                </tr>
            
                <tr>
                    <td>MsrDataEncryption_None</td>
                    <td>Indicates no encryption algorithm.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |