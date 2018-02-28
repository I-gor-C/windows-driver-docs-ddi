---
UID: NN:wiamindr_lh.IWiaMiniDrvCallBack
title: IWiaMiniDrvCallBack
author: windows-driver-content
description: The IWiaMiniDrvCallBack interface provides the MiniDrvCallback method, which enables minidrivers to transfer image header data and image data from the imaging device to the WIA service.
old-location: image\iwiaminidrvcallback_interface.htm
old-project: image
ms.assetid: cf2460c5-325f-43c3-a1fe-5b6982234194
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: CallBack_2e94f80e-dde0-4289-8911-a769a909b4d8.xml, IWiaMiniDrvCallBack, IWiaMiniDrvCallBack interface [Imaging Devices], IWiaMiniDrvCallBack interface [Imaging Devices], described, image.iwiaminidrvcallback_interface, wiamindr_lh/IWiaMiniDrvCallBack
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wiamindr_lh.h
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
req.lib: wiamindr_lh.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	wiamindr_lh.h
api_name:
-	IWiaMiniDrvCallBack
product: Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---

# IWiaMiniDrvCallBack interface

The <b>IWiaMiniDrvCallBack</b> interface provides the <a href="https://msdn.microsoft.com/7d1c0d8a-65db-47fd-ad6a-a83c7ed3acd9">MiniDrvCallback</a> method, which enables minidrivers to transfer image header data and image data from the imaging device to the WIA service.

This method can also convey status information, such as the percentage of data transferred.

## Methods

<p>The <b>IWiaMiniDrvCallBack</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWiaMiniDrvCallBack::MiniDrvCallback](nf-wiamindr_lh-iwiaminidrvcallback-minidrvcallback.md) | The MiniDrvCallback method provides a callback method for WIA minidrivers to use during a callback data transfer. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wiamindr_lh.h |