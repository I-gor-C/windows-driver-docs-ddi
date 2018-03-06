---
UID: NN:wudfddi.IQueueCallbackCreate
title: IQueueCallbackCreate
author: windows-driver-content
description: An I/O queue notifies a driver when an open file request is available for the driver.
old-location: wdf\iqueuecallbackcreate.htm
old-project: wdf
ms.assetid: 50b8acc6-5f08-47d5-b45d-31ff33a06be1
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IQueueCallbackCreate, IQueueCallbackCreate interface, IQueueCallbackCreate interface, described, UMDFQueueObjectRef_dfb85326-329e-4d5b-9889-1894c53e4cb7.xml, umdf.iqueuecallbackcreate, wdf.iqueuecallbackcreate, wudfddi/IQueueCallbackCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	wudfddi.h
api_name:
-	IQueueCallbackCreate
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IQueueCallbackCreate interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

An I/O queue notifies a driver when an open file request is available for the driver. The I/O queue notifies the driver in response to an application calling the Microsoft Win32 <b>CreateFile</b> function. The driver can handle the notification by registering the <b>IQueueCallbackCreate</b> interface.

## Methods

<p>The <b>IQueueCallbackCreate</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IQueueCallbackCreate::OnCreateFile](nf-wudfddi-iqueuecallbackcreate-oncreatefile.md) | The OnCreateFile method is called to handle an open file request when an application opens a device through the Microsoft Win32 CreateFile function. |

## Remarks
A driver registers the <b>IQueueCallbackCreate</b> interface when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. For more information about creating or configuring an I/O queue, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/configuring-dispatch-mode-for-an-i-o-queue">Configuring Dispatch Mode for an I/O Queue</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfddi.h |