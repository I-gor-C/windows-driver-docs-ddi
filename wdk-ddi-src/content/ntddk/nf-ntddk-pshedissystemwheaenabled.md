---
UID: NF:ntddk.PshedIsSystemWheaEnabled
title: PshedIsSystemWheaEnabled function
author: windows-driver-content
description: The PshedIsSystemWheaEnabled function returns a Boolean value that indicates whether the system is WHEA-enabled.
old-location: whea\pshedissystemwheaenabled.htm
old-project: whea
ms.assetid: d9935605-dc5f-4987-8a5b-b2c2b358dbbf
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: PshedIsSystemWheaEnabled, PshedIsSystemWheaEnabled function [WHEA Drivers and Applications], ntddk/PshedIsSystemWheaEnabled, whea.pshedissystemwheaenabled, whearef_492a4370-81bf-411b-bd87-2408f4551b18.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
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
req.lib: Pshed.lib
req.dll: Pshed.dll
req.irql: Any
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Pshed.dll
api_name:
-	PshedIsSystemWheaEnabled
product: Windows
targetos: Windows
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# PshedIsSystemWheaEnabled function
The <b>PshedIsSystemWheaEnabled</b> function returns a Boolean value that indicates whether the system is WHEA-enabled.

## Syntax

```
NTPSHEDAPI BOOLEAN PshedIsSystemWheaEnabled(

);
```

## Parameters

This function has no parameters.

## Return Value

A Boolean value that indicates whether the system is WHEA-enabled.

## Remarks

A PSHED plug-in can call the <b>PshedIsSystemWheaEnabled</b> function before it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a> function to verify that the system is WHEA-enabled.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** | Pshed.lib |
| **DLL** | Pshed.dll |
| **IRQL** | Any |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559466">PshedRegisterPlugin</a>