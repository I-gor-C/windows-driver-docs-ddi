---
UID: NN:wudfddi.IWDFIoTargetStateManagement
title: IWDFIoTargetStateManagement
author: windows-driver-content
description: The IWDFIoTargetStateManagement interface exposes methods that manage and monitor the state of an I/O target object.
old-location: wdf\iwdfiotargetstatemanagement.htm
old-project: wdf
ms.assetid: 6870b6fa-1a90-4a7a-935a-4ce8eda940a1
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.iwdfiotargetstatemanagement, IWDFIoTargetStateManagement interface, IWDFIoTargetStateManagement interface, described, IWDFIoTargetStateManagement, wudfddi/IWDFIoTargetStateManagement, UMDFIoTargetObjectRef_667496e9-fa1f-4c90-911d-d456ffc3b59e.xml, umdf.iwdfiotargetstatemanagement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
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
-	WUDFx.dll
apiname:
-	IWDFIoTargetStateManagement
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFIoTargetStateManagement interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFIoTargetStateManagement</b> interface exposes methods that manage and monitor the state of an I/O target object.

## Methods

<p>The <b>IWDFIoTargetStateManagement</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFIoTargetStateManagement.GetState](nf-wudfddi-iwdfiotargetstatemanagement-getstate.md) | The GetState method returns the current state of a local I/O target. |
| [wudfddi.IWDFIoTargetStateManagement.Remove](nf-wudfddi-iwdfiotargetstatemanagement-remove.md) | The Remove method removes a local I/O target. |
| [wudfddi.IWDFIoTargetStateManagement.Start](nf-wudfddi-iwdfiotargetstatemanagement-start.md) | The Start method starts sending queued requests to a local I/O target. |
| [wudfddi.IWDFIoTargetStateManagement.Stop](nf-wudfddi-iwdfiotargetstatemanagement-stop.md) | The Stop method stops sending queued requests to a local I/O target. |

## Remarks

Drivers obtain the <b>IWDFIoTargetStateManagement</b> interface by calling <b>IWDFIoTarget::QueryInterface</b>, <b>IWDFUsbTargetPipe::QueryInterface</b>, or <b>IWDFUsbTargetPipe2::QueryInterface</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |