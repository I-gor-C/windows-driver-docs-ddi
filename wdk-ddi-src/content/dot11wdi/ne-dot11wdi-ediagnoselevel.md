---
UID: NE:dot11wdi.eDiagnoseLevel
title: eDiagnoseLevel
author: windows-driver-content
description: The eDiagnoseLevel enumeration defines the diagnosis levels for adapter hang diagnosis.
old-location: netvista\wdiediagnoselevel.htm
old-project: netvista
ms.assetid: C19C250D-3C8D-4855-A8B3-82E139CE09BB
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: DiagnoseLevelDriverStateDump, DiagnoseLevelFirmwareImageDump, DiagnoseLevelHardwareRegisters, DiagnoseLevelNone, dot11wdi/DiagnoseLevelDriverStateDump, dot11wdi/DiagnoseLevelFirmwareImageDump, dot11wdi/DiagnoseLevelHardwareRegisters, dot11wdi/DiagnoseLevelNone, dot11wdi/eDiagnoseLevel, eDiagnoseLevel, eDiagnoseLevel enumeration [Network Drivers Starting with Windows Vista], netvista.wdiediagnoselevel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	dot11wdi.h
api_name:
-	eDiagnoseLevel
product:
- Windows
targetos: Windows
req.typenames: eDiagnoseLevel
---

# eDiagnoseLevel Enumeration
The eDiagnoseLevel enumeration defines the diagnosis levels for adapter hang diagnosis.

## Syntax
```
typedef enum eDiagnoseLevel {
  DiagnoseLevelNone               ,
  DiagnoseLevelHardwareRegisters  ,
  DiagnoseLevelFirmwareImageDump  ,
  DiagnoseLevelDriverStateDump
} ;
```

## Constants

<table>
            
                <tr>
                    <td>DiagnoseLevelNone</td>
                    <td>No diagnostic information should be collected.</td>
                </tr>
            
                <tr>
                    <td>DiagnoseLevelHardwareRegisters</td>
                    <td>Dump the hardware registers. This information is included in the LiveKD dump.</td>
                </tr>
            
                <tr>
                    <td>DiagnoseLevelFirmwareImageDump</td>
                    <td>Dump the full firmware image and hardware registers. The firmware image should dump to a file.</td>
                </tr>
            
                <tr>
                    <td>DiagnoseLevelDriverStateDump</td>
                    <td>Dump the driver state, full firmware image, and hardware registers. The driver state and full firmware image should dump to files.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | dot11wdi.h |

## See Also

<a href="https://msdn.microsoft.com/233CCF43-481E-4759-A2FC-0329103F8208">MiniportWdiAdapterHangDiagnose</a>