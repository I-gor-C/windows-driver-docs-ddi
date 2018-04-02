---
UID: NN:wudfddi.IWDFIoRequest3
title: IWDFIoRequest3
author: windows-driver-content
description: To obtain the IWDFIoRequest3 interface, drivers call IWDFIoRequest::QueryInterface.
old-location: wdf\iwdfiorequest3.htm
old-project: wdf
ms.assetid: 12F4CDB7-EEA5-49D1-AD41-6F5F0C9ED6C3
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFIoRequest3, IWDFIoRequest3 interface, IWDFIoRequest3 interface, described, umdf.iwdfiorequest3, wdf.iwdfiorequest3, wudfddi/IWDFIoRequest3
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
-	WUDFx.dll
api_name:
-	IWDFIoRequest3
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFIoRequest3 interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

To obtain the <b>IWDFIoRequest3</b> interface, drivers call <b>IWDFIoRequest::QueryInterface</b>.

## Methods

<p>The <b>IWDFIoRequest3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFIoRequest3::GetUserModeDriverInitiatedIo](nf-wudfddi-iwdfiorequest3-getusermodedriverinitiatedio.md) | The GetUserModeDriverInitiatedIo method determines whether an I/O request is marked as initiated by a UMDF driver. |
| [IWDFIoRequest3::RetrieveActivityId](nf-wudfddi-iwdfiorequest3-retrieveactivityid.md) | The RetrieveActivityId method retrieves the current activity identifier associated with an I/O request. |
| [IWDFIoRequest3::SetActivityId](nf-wudfddi-iwdfiorequest3-setactivityid.md) | The SetActivityId method associates an activity identifier with an I/O request. |
| [IWDFIoRequest3::SetUserModeDriverInitiatedIo](nf-wudfddi-iwdfiorequest3-setusermodedriverinitiatedio.md) | The SetUserModeDriverInitiatedIo method indicates to kernel-mode drivers that sit below the UMDF driver in the same device stack that a particular request should be treated as though it came from a UMDF driver. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff558988">IWDFIoRequest2</a>