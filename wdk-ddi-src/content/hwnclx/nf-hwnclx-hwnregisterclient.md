---
UID: NF:hwnclx.HwNRegisterClient
title: HwNRegisterClient function
author: windows-driver-content
description: Registers the hardware notification client driver and its callback functions with the class extension.
old-location: gpiobtn\hwnregisterclient.htm
old-project: gpiobtn
ms.assetid: 69de1551-e41f-4d18-89db-28d190676922
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: HwNRegisterClient, HwNRegisterClient function, gpiobtn.hwnregisterclient, hwnclx/HwNRegisterClient
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hwnclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
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
req.lib: Mshwnclxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Mshwnclxstub.lib
-	Mshwnclxstub.dll
api_name:
-	HwNRegisterClient
product:
- Windows
targetos: Windows
req.typenames: HWN_CLX_EXPORT_INDEX, *PHWN_CLX_EXPORT_INDEX
---


# HwNRegisterClient function
Registers the hardware notification client driver and its callback functions with the class extension. This function should be invoked when the client driver is loaded and the <a href="..\wudfwdm\nc-wudfwdm-driver_initialize.md">DriverEntry</a> routine is called for initialization. F

## Syntax

````
FORCEINLINE NTSTATUS  HwNRegisterClient(
  _In_    WDFDRIVER                        Driver,
  _Inout_ PHWN_CLIENT_REGISTRATION_PACKET  RegistrationPacket,
  _In_    PUNICODE_STRING                  RegistryPath
);
````

## Parameters

`Driver`

Handle to the client drivers framework driver object.

`RegistrationPacket`

Pointer to the <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_CLIENT_REGISTRATION_PACKET</a> structure that contains function pointers to the callback functions defined in the client driver implementation and required by the class extension.

`RegistryPath`

Pointer to a <a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> structure that contains the path to the client driver’s registry key.


## Return Value

Returns STATUS_SUCCESS if function succeeds. Returns STATUS_INVALID_PARAMETER if corresponding client driver can't be found. Otherwise, it returns one of the error status values defined in Ntstatus.h.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | hwnclx.h |
| **Library** | Mshwnclxstub.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn789335">Hardware notifications support</a>



<a href="https://msdn.microsoft.com/405ff6db-9bc0-42f3-a740-49dd3967a8b3">Hardware notifications reference</a>