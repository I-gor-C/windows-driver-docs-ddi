---
UID: NN:wudfddi.IWDFFileHandleTargetFactory
title: IWDFFileHandleTargetFactory
author: windows-driver-content
description: The IWDFFileHandleTargetFactory interface is a factory interface that is used to create a file-handle-based target device object.
old-location: wdf\iwdffilehandletargetfactory.htm
old-project: wdf
ms.assetid: b4754176-53a2-4ee4-a441-5d9a4a4a17e2
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: IWDFFileHandleTargetFactory, IWDFFileHandleTargetFactory interface, IWDFFileHandleTargetFactory interface, described, UMDFDeviceObjectRef_01a7fcc5-c259-4bad-b44c-9a20eeae1751.xml, umdf.iwdffilehandletargetfactory, wdf.iwdffilehandletargetfactory, wudfddi/IWDFFileHandleTargetFactory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: Wudfddi.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WUDFx.dll
api_name:
-	IWDFFileHandleTargetFactory
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFFileHandleTargetFactory interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFFileHandleTargetFactory</b> interface is a factory interface that is used to create a file-handle-based target device object.

## Methods

<p>The <b>IWDFFileHandleTargetFactory</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFFileHandleTargetFactory::CreateFileHandleTarget](nf-wudfddi-iwdffilehandletargetfactory-createfilehandletarget.md) | The CreateFileHandleTarget method creates a file-handle-based I/O target object. |

## Remarks

Drivers obtain the <b>IWDFFileHandleTargetFactory</b> interface by calling <b>IWDFDevice::QueryInterface</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h (include Wudfddi.h) |