---
UID: NN:wudfddi.IFileCallbackClose
title: IFileCallbackClose
author: windows-driver-content
description: The framework can notify a driver when the driver should perform a close operation. The driver can handle the notification by registering the IFileCallbackClose interface.
old-location: wdf\ifilecallbackclose.htm
old-project: wdf
ms.assetid: 22ecfb7b-daba-4321-bca5-4460ead8e3cd
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IFileCallbackClose, IFileCallbackClose interface, IFileCallbackClose interface, described, UMDFFileObjectRef_52a9bb2c-0bf7-49db-80f0-7df5f4f131f6.xml, umdf.ifilecallbackclose, wdf.ifilecallbackclose, wudfddi/IFileCallbackClose
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
-	IFileCallbackClose
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IFileCallbackClose interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The framework can notify a driver when the driver should perform a close operation.  The driver can handle the notification by registering the <b>IFileCallbackClose</b> interface.

A driver registers the <b>IFileCallbackClose</b> interface when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to create a device object.

## Methods

<p>The <b>IFileCallbackClose</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IFileCallbackClose::OnCloseFile](nf-wudfddi-ifilecallbackclose-onclosefile.md) | The OnCloseFile method is called when the last reference count on a file object goes down to zero and before the file object is released. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfddi.h |