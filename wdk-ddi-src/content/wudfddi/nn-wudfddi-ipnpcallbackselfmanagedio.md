---
UID: NN:wudfddi.IPnpCallbackSelfManagedIo
title: IPnpCallbackSelfManagedIo
author: windows-driver-content
description: The IPnpCallbackSelfManagedIo interface is a Plug and Play (PnP) and power management (PM) interface.
old-location: wdf\ipnpcallbackselfmanagedio.htm
old-project: wdf
ms.assetid: 34971df0-4abc-41a1-8d2f-6e36df1daf20
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.ipnpcallbackselfmanagedio, IPnpCallbackSelfManagedIo interface, IPnpCallbackSelfManagedIo interface, described, IPnpCallbackSelfManagedIo, wudfddi/IPnpCallbackSelfManagedIo, UMDFDeviceObjectRef_0f139c45-68eb-4429-ac90-675d7eddea5a.xml, umdf.ipnpcallbackselfmanagedio
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
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
-	IPnpCallbackSelfManagedIo
product: Windows
targetos: Windows
req.typenames: "*PPOWER_ACTION, POWER_ACTION"
req.product: Windows 10 or later.
---

# IPnpCallbackSelfManagedIo interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IPnpCallbackSelfManagedIo</b> interface is a Plug and Play (PnP) and power management (PM) interface.

## Methods

<p>The <b>IPnpCallbackSelfManagedIo</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoCleanup](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediocleanup.md) | The OnSelfManagedIoCleanup method releases memory for a device's self-managed I/O operations, after the device is removed. |
| [wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoFlush](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagedioflush.md) | The OnSelfManagedIoFlush method flushes the device for a device's self-managed I/O operations. |
| [wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoInit](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagedioinit.md) | The OnSelfManagedIoInit method initializes a device's self-managed I/O operations. |
| [wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoRestart](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediorestart.md) | The OnSelfManagedIoRestart method restarts a device's self-managed I/O operations. |
| [wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoStop](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediostop.md) | The OnSelfManagedIoStop method is not used in the current version of the UMDF. |
| [wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoSuspend](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediosuspend.md) | The OnSelfManagedIoSuspend method suspends a device's self-managed I/O operations. |

## Remarks

A driver registers the <b>IPnpCallbackSelfManagedIo</b> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to create a device object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfddi.h (include Wudfddi.h) |