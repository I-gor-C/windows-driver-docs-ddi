---
UID: NS:ntddk._WHEA_ERROR_INJECTION_CAPABILITIES
title: "_WHEA_ERROR_INJECTION_CAPABILITIES"
author: windows-driver-content
description: The WHEA_ERROR_INJECTION_CAPABILITIES union describes the types of hardware errors that can be injected into a hardware platform.
old-location: whea\whea_error_injection_capabilities.htm
old-project: whea
ms.assetid: 77f982e4-6f35-4d4a-9c00-9ae34eacfbd3
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_ERROR_INJECTION_CAPABILITIES, PWHEA_ERROR_INJECTION_CAPABILITIES, PWHEA_ERROR_INJECTION_CAPABILITIES union pointer [WHEA Drivers and Applications], WHEA_ERROR_INJECTION_CAPABILITIES, WHEA_ERROR_INJECTION_CAPABILITIES union [WHEA Drivers and Applications], _WHEA_ERROR_INJECTION_CAPABILITIES, ntddk/PWHEA_ERROR_INJECTION_CAPABILITIES, ntddk/WHEA_ERROR_INJECTION_CAPABILITIES, whea.whea_error_injection_capabilities, whearef_f040c2a7-cded-4903-a19c-c1163870c010.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
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
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddk.h
api_name:
-	WHEA_ERROR_INJECTION_CAPABILITIES
product: Windows
targetos: Windows
req.typenames: WHEA_ERROR_INJECTION_CAPABILITIES, *PWHEA_ERROR_INJECTION_CAPABILITIES
---

# _WHEA_ERROR_INJECTION_CAPABILITIES structure
The WHEA_ERROR_INJECTION_CAPABILITIES union describes the types of hardware errors that can be injected into a hardware platform.

## Syntax
```
typedef struct _WHEA_ERROR_INJECTION_CAPABILITIES {
  struct {
    ULONG  : 1  IA64Corrected;
    ULONG  : 1  IA64Fatal;
    ULONG  : 1  IA64Recoverable;
    ULONG  : 1  IA64RecoverableCache;
    ULONG  : 1  IA64RecoverableRegFile;
    ULONG  : 1  MemoryCorrectable;
    ULONG  : 1  MemoryUncorrectableFatal;
    ULONG  : 1  MemoryUncorrectableNonFatal;
    ULONG  : 1  PCIExpressCorrectable;
    ULONG  : 1  PCIExpressUncorrectableFatal;
    ULONG  : 1  PCIExpressUncorrectableNonFatal;
    ULONG  : 1  PlatformCorrectable;
    ULONG  : 1  PlatformUncorrectableFatal;
    ULONG  : 1  PlatformUncorrectableNonFatal;
    ULONG  : 1  ProcessorCorrectable;
    ULONG  : 1  ProcessorUncorrectableFatal;
    ULONG  : 1  ProcessorUncorrectableNonFatal;
    ULONG  : 15 Reserved;
  } DUMMYSTRUCTNAME;
  ULONG  AsULONG;
} *PWHEA_ERROR_INJECTION_CAPABILITIES, WHEA_ERROR_INJECTION_CAPABILITIES;
```

## Members


`DUMMYSTRUCTNAME`



`AsULONG`

A ULONG representation of the contents of the WHEA_ERROR_INJECTION_CAPABILITIES union.

## Remarks
A user-mode WHEA management application calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559516">WHEAErrorInjectionMethods::GetErrorInjectionCapabilitiesRtn</a> method to retrieve a WHEA_ERROR_INJECTION_CAPABILITIES union that describes the types of hardware errors that can be injected into the hardware platform. If a PSHED plug-in is registered to participate in error injection, the PSHED plug-in's <a href="https://msdn.microsoft.com/8cb19677-11b8-4594-b4dd-ebd00fae07d4">GetInjectionCapabilities</a> callback function is called to provide this information back to the calling application. The application uses this information when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559518">WHEAErrorInjectionMethods::InjectErrorRtn</a> method to inject a hardware error into the hardware platform.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/8cb19677-11b8-4594-b4dd-ebd00fae07d4">GetInjectionCapabilities</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559516">WHEAErrorInjectionMethods::GetErrorInjectionCapabilitiesRtn</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559518">WHEAErrorInjectionMethods::InjectErrorRtn</a>