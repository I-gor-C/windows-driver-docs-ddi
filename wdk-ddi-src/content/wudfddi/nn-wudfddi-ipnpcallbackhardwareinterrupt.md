---
UID: NN:wudfddi.IPnpCallbackHardwareInterrupt
title: IPnpCallbackHardwareInterrupt
author: windows-driver-content
description: The IPnpCallbackHardwareInterrupt interface supports interrupt-related Plug and Play and power management callback methods.
old-location: wdf\ipnpcallbackhardwareinterrupt.htm
old-project: wdf
ms.assetid: C66A570A-EEAF-4D18-A834-B50576F51E29
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPnpCallbackHardwareInterrupt, IPnpCallbackHardwareInterrupt interface, IPnpCallbackHardwareInterrupt interface, described, umdf.ipnpcallbackhardwareinterrupt, wdf.ipnpcallbackhardwareinterrupt, wudfddi/IPnpCallbackHardwareInterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Wudfddi.h
api_name:
-	IPnpCallbackHardwareInterrupt
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IPnpCallbackHardwareInterrupt interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

  The <b>IPnpCallbackHardwareInterrupt</b> interface supports interrupt-related Plug and Play and power management callback methods.

## Methods

<p>The <b>IPnpCallbackHardwareInterrupt</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled](nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0entrypostinterruptsenabled.md) | A driver's OnD0EntryPostInterruptsEnabled event callback function performs device-specific operations that are required when the driver enables the device's hardware interrupts. |
| [IPnpCallbackHardwareInterrupt::OnD0ExitPreInterruptsDisabled](nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0exitpreinterruptsdisabled.md) | A driver's OnD0ExitPreInterruptsDisabled event callback function performs device-specific operations that are required before the driver disables the device's hardware interrupts. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |

## See Also

<a href="https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332">IUnknown</a>