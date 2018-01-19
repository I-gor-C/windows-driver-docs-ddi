---
UID : NS:ntddk._WHEA_ERROR_PACKET_FLAGS
title : _WHEA_ERROR_PACKET_FLAGS
author : windows-driver-content
description : The WHEA_ERROR_PACKET_FLAGS union defines the error condition reported through a WHEA_ERROR_PACKET structure.
old-location : whea\whea_error_packet_flags.htm
old-project : whea
ms.assetid : e1dae7df-7d81-42cc-9a01-44345f53ba4e
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_ERROR_PACKET_FLAGS, *PWHEA_ERROR_PACKET_FLAGS, WHEA_ERROR_PACKET_FLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WHEA_ERROR_PACKET_FLAGS
req.alt-loc : ntddk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PWHEA_ERROR_PACKET_FLAGS, WHEA_ERROR_PACKET_FLAGS"
---

# _WHEA_ERROR_PACKET_FLAGS structure
The WHEA_ERROR_PACKET_FLAGS union defines the error condition reported through a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure.

## Syntax
````
typedef union _WHEA_ERROR_PACKET_FLAGS {
  struct {
    ULONG PreviousError  :1;
    ULONG Reserved1  :1;
    ULONG HypervisorError  :1;
    ULONG Simulated  :1;
    ULONG PlatformPfaControl  :1;
    ULONG PlatformDirectedOffline  :1;
    ULONG Reserved2  :26;
  };
  ULONG  AsULONG;
} WHEA_ERROR_PACKET_FLAGS, *PWHEA_ERROR_PACKET_FLAGS;
````

## Members

        
            `AsULONG`

            A ULONG representation of the contents of the WHEA_ERROR_PACKET_FLAGS union.

    ## Remarks
        The WHEA_ERROR_PACKET_FLAGS union describes the error condition reported by using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/d2ded330-edcc-4bdd-9b52-73c1961d8ef2">Predictive Failure Analysis (PFA)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_PACKET_FLAGS union%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>