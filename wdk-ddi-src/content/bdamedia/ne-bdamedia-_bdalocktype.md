---
UID: NE:bdamedia._BdaLockType
title: "_BdaLockType"
author: windows-driver-content
description: The BDA_LockType enumerated type contains values that specify lock types for a signal.
old-location: stream\bda_locktype.htm
old-project: stream
ms.assetid: 6119727a-05af-4a70-a321-5f0f2e439b93
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: BDA_LockType, BDA_LockType enumeration [Streaming Media Devices], Bda_LockType_Complete, Bda_LockType_DecoderDemod, Bda_LockType_None, Bda_LockType_PLL, _BdaLockType, bdamedia/BDA_LockType, bdamedia/Bda_LockType_Complete, bdamedia/Bda_LockType_DecoderDemod, bdamedia/Bda_LockType_None, bdamedia/Bda_LockType_PLL, bdaref_46e4b273-15bc-47bc-a14b-2a6be1cc3c0f.xml, stream.bda_locktype
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bdamedia.h
req.include-header: Bdamedia.h
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
-	bdamedia.h
api_name:
-	BDA_LockType
product: Windows
targetos: Windows
req.typenames: BDA_LockType
---

# _BdaLockType Enumeration
The BDA_LockType enumerated type contains values that specify lock types for a signal.

## Syntax
```
typedef enum _BdaLockType {
  Bda_LockType_None          ,
  Bda_LockType_PLL           ,
  Bda_LockType_DecoderDemod  ,
  Bda_LockType_Complete
} BDA_LockType;
```

## Constants

<table>
            
                <tr>
                    <td>Bda_LockType_None</td>
                    <td>The driver does not support any lock types.</td>
                </tr>
            
                <tr>
                    <td>Bda_LockType_PLL</td>
                    <td>The driver supports a phase-lock-loop (PLL) lock.</td>
                </tr>
            
                <tr>
                    <td>Bda_LockType_DecoderDemod</td>
                    <td>The driver supports a decoder-demodulator lock.</td>
                </tr>
            
                <tr>
                    <td>Bda_LockType_Complete</td>
                    <td>To be supplied.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | bdamedia.h (include Bdamedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564369">KSPROPERTY_BDA_SIGNAL_LOCK_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564370">KSPROPERTY_BDA_SIGNAL_LOCK_TYPE</a>