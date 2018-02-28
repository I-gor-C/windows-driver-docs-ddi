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
````
typedef union _WHEA_ERROR_INJECTION_CAPABILITIES {
  struct {
    ULONG ProcessorCorrectable  :1;
    ULONG ProcessorUncorrectableNonFatal  :1;
    ULONG ProcessorUncorrectableFatal  :1;
    ULONG MemoryCorrectable  :1;
    ULONG MemoryUncorrectableNonFatal  :1;
    ULONG MemoryUncorrectableFatal  :1;
    ULONG PCIExpressCorrectable  :1;
    ULONG PCIExpressUncorrectableNonFatal  :1;
    ULONG PCIExpressUncorrectableFatal  :1;
    ULONG PlatformCorrectable  :1;
    ULONG PlatformUncorrectableNonFatal  :1;
    ULONG PlatformUncorrectableFatal  :1;
    ULONG IA64Corrected  :1;
    ULONG IA64Recoverable  :1;
    ULONG IA64Fatal  :1;
    ULONG IA64RecoverableCache  :1;
    ULONG IA64RecoverableRegFile  :1;
    ULONG Reserved  :15;
  };
  ULONG  AsULONG;
} WHEA_ERROR_INJECTION_CAPABILITIES, *PWHEA_ERROR_INJECTION_CAPABILITIES;
````

## Members


`AsULONG`

A ULONG representation of the contents of the WHEA_ERROR_INJECTION_CAPABILITIES union.

`DUMMYSTRUCTNAME`



## Remarks
A user-mode WHEA management application calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559516">WHEAErrorInjectionMethods::GetErrorInjectionCapabilitiesRtn</a> method to retrieve a WHEA_ERROR_INJECTION_CAPABILITIES union that describes the types of hardware errors that can be injected into the hardware platform. If a PSHED plug-in is registered to participate in error injection, the PSHED plug-in's <a href="..\ntddk\nc-ntddk-pshed_pi_get_injection_capabilities.md">GetInjectionCapabilities</a> callback function is called to provide this information back to the calling application. The application uses this information when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559518">WHEAErrorInjectionMethods::InjectErrorRtn</a> method to inject a hardware error into the hardware platform.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="..\ntddk\nc-ntddk-pshed_pi_get_injection_capabilities.md">GetInjectionCapabilities</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559516">WHEAErrorInjectionMethods::GetErrorInjectionCapabilitiesRtn</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559518">WHEAErrorInjectionMethods::InjectErrorRtn</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_INJECTION_CAPABILITIES union%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>