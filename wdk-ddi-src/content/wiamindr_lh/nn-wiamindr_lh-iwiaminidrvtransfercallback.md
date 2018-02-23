---
UID: NN:wiamindr_lh.IWiaMiniDrvTransferCallback
title: IWiaMiniDrvTransferCallback
author: windows-driver-content
description: This is a Callback interface that is called by the WIA mini-driver for stream-based transfers.
old-location: image\iwiaminidrvtransfercallback.htm
old-project: Image
ms.assetid: A3D874CB-1F43-4AA0-975B-35C0C5F7A13C
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: image.iwiaminidrvtransfercallback, IWiaMiniDrvTransferCallback interface [Imaging Devices], IWiaMiniDrvTransferCallback interface [Imaging Devices], described, IWiaMiniDrvTransferCallback, wiamindr_lh/IWiaMiniDrvTransferCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wiamindr_lh.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Wiamindr_lh.h
apiname:
-	IWiaMiniDrvTransferCallback
product: Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---

# IWiaMiniDrvTransferCallback interface

This is a Callback interface that is called by the WIA mini-driver for stream-based transfers.

## Methods

<p>The <b>IWiaMiniDrvTransferCallback</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wiamindr_lh.IWiaMiniDrvTransferCallback.GetNextStream](nf-wiamindr_lh-iwiaminidrvtransfercallback-getnextstream.md) | Called by the WIA mini-driver to obtain a stream for the current data transfer (download or upload). |
| [wiamindr_lh.IWiaMiniDrvTransferCallback.SendMessage](nf-wiamindr_lh-iwiaminidrvtransfercallback-sendmessage.md) | Periodically called by the WIA mini-driver during a data transfer, to update the WIA application client about the progress and status of the transfer. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h |

## See Also

<a href="https://msdn.microsoft.com/83817277-3526-4f64-8e7c-7e02c8cd77bd">Data Transfer Between Legacy Application and Windows Vista Driver</a>



<a href="https://msdn.microsoft.com/0cdc02bf-23fe-4122-8d5f-f42c3c07da8b">Cancellation of Data Transfers in Windows Vista</a>



<a href="https://msdn.microsoft.com/0cdc02bf-23fe-4122-8d5f-f42c3c07da8b">Cancellation of Data Transfers in Windows Vista</a>



<a href="https://msdn.microsoft.com/83817277-3526-4f64-8e7c-7e02c8cd77bd">Data Transfer Between Legacy Application and Windows Vista Driver</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20IWiaMiniDrvTransferCallback interface%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>