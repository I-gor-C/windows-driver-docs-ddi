---
UID: NF:wsk.WskReleaseProviderNPI
title: WskReleaseProviderNPI function
author: windows-driver-content
description: The WskReleaseProviderNPI function releases a Network Programming Interface (NPI) that was captured with WskCaptureProviderNPI.
old-location: netvista\wskreleaseprovidernpi.htm
old-project: netvista
ms.assetid: 6b0b995a-61db-4bdf-a896-74d91bd192e7
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: WskReleaseProviderNPI, WskReleaseProviderNPI function [Network Drivers Starting with Windows Vista], netvista.wskreleaseprovidernpi, wsk/WskReleaseProviderNPI, wskref_1ed7116e-c3a0-41dd-9d19-aa2f44eae257.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
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
req.lib: Netio.lib
req.dll: 
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Netio.lib
-	Netio.dll
api_name:
-	WskReleaseProviderNPI
product:
- Windows
targetos: Windows
req.typenames: WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
req.product: Windows 10 or later.
---


# WskReleaseProviderNPI function
The 
  <b>WskReleaseProviderNPI</b> function releases a 
  <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/network-programming-interface">Network Programming Interface
  (NPI)</a> that was captured with 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff571122">WskCaptureProviderNPI</a>.

## Syntax

```
void WskReleaseProviderNPI(
  PWSK_REGISTRATION WskRegistration
);
```

## Parameters

`WskRegistration`

A pointer to the memory location initialized by 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a> that identifies a WSK
     application's registration instance.


## Return Value

None

## Remarks

For each call to
    <b>WskCaptureProviderNPI</b> that returns a success code, there must be exactly one corresponding 
    <b>WskReleaseProviderNPI</b> call that uses
    the same 
    <i>WskRegistration</i> parameter that was passed to 
    <b>WskCaptureProviderNPI</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating   systems.  |
| **Target Platform** | Universal |
| **Header** | wsk.h (include Wsk.h) |
| **Library** | Netio.lib |
| **IRQL** | "<= DISPATCH_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571178">WSK_REGISTRATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff571122">WskCaptureProviderNPI</a>