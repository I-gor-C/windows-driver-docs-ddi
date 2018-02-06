---
UID: NN:wudfddi.IPnpCallbackRemoteInterfaceNotification
title: IPnpCallbackRemoteInterfaceNotification
author: windows-driver-content
description: A driver's IPnpCallbackRemoteInterfaceNotification interface provides a callback function that the framework calls to notify the driver when a device interface becomes available.
old-location: wdf\ipnpcallbackremoteinterfacenotification.htm
old-project: wdf
ms.assetid: 99d670dd-2358-4f1a-b111-72484bf3132c
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.ipnpcallbackremoteinterfacenotification, IPnpCallbackRemoteInterfaceNotification interface, IPnpCallbackRemoteInterfaceNotification interface, described, IPnpCallbackRemoteInterfaceNotification, wudfddi/IPnpCallbackRemoteInterfaceNotification, UMDFDeviceObjectRef_4701eb20-04aa-412f-8511-f44a2590ee5b.xml, umdf.ipnpcallbackremoteinterfacenotification
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
-	IPnpCallbackRemoteInterfaceNotification
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IPnpCallbackRemoteInterfaceNotification interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

A driver's <b>IPnpCallbackRemoteInterfaceNotification</b> interface provides a callback function that the framework calls to notify the driver when a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/using-device-interfaces-in-umdf-drivers">device interface</a> becomes available.

## Methods

<p>The <b>IPnpCallbackRemoteInterfaceNotification</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IPnpCallbackRemoteInterfaceNotification.OnRemoteInterfaceArrival](nf-wudfddi-ipnpcallbackremoteinterfacenotification-onremoteinterfacearrival.md) | A driver's OnRemoteInterfaceArrival event callback function informs the driver when a device interface is available. |

## Remarks

If your driver supports an <b>IPnpCallbackRemoteInterfaceNotification</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> must return the interface.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.9 |
| **Header** | wudfddi.h (include Wudfddi.h) |