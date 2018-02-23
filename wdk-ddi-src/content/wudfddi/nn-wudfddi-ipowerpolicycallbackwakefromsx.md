---
UID: NN:wudfddi.IPowerPolicyCallbackWakeFromSx
title: IPowerPolicyCallbackWakeFromSx
author: windows-driver-content
description: A driver's IPowerPolicyCallbackWakeFromSx interface provides callback functions that the framework calls to notify the driver about wake events. These events are related to a device's ability to wake both itself and the system from a low-power state.
old-location: wdf\ipowerpolicycallbackwakefromsx.htm
old-project: wdf
ms.assetid: dac93565-e67a-44a3-acf0-e1f58ce8dd9e
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: wdf.ipowerpolicycallbackwakefromsx, IPowerPolicyCallbackWakeFromSx interface, IPowerPolicyCallbackWakeFromSx interface, described, IPowerPolicyCallbackWakeFromSx, wudfddi/IPowerPolicyCallbackWakeFromSx, UMDFDeviceObjectRef_bc620403-691d-42df-9bdf-2a859e5718ea.xml, umdf.ipowerpolicycallbackwakefromsx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: wudfddi.h
req.dll: WUDFx.dll
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Wudfddi.h
apiname:
-	IPowerPolicyCallbackWakeFromSx
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IPowerPolicyCallbackWakeFromSx interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

A driver's <b>IPowerPolicyCallbackWakeFromSx</b> interface provides callback functions that the framework calls to notify the driver about wake events. These events are related to a device's ability to wake both itself and the system from a low-power state.

## Methods

<p>The <b>IPowerPolicyCallbackWakeFromSx</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IPowerPolicyCallbackWakeFromSx.OnArmWakeFromSx](nf-wudfddi-ipowerpolicycallbackwakefromsx-onarmwakefromsx.md) | A driver's OnArmWakeFromSx event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state. |
| [wudfddi.IPowerPolicyCallbackWakeFromSx.OnDisarmWakeFromSx](nf-wudfddi-ipowerpolicycallbackwakefromsx-ondisarmwakefromsx.md) | A driver's OnDisarmWakeFromSx event callback function disarms (that is, disables) a device's ability to trigger a wake signal while the device and system are in low-power states. |
| [wudfddi.IPowerPolicyCallbackWakeFromSx.OnWakeFromSxTriggered](nf-wudfddi-ipowerpolicycallbackwakefromsx-onwakefromsxtriggered.md) | A driver's OnWakeFromSxTriggered event callback function informs the driver that its device, which had previously entered a low-power device state because system power was reduced, might have triggered a wake signal. |

## Remarks

If your driver supports an <b>IPowerPolicyCallbackWakeFromSx</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> must return the interface.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.9 |
| **Header** | wudfddi.h (include Wudfddi.h) |