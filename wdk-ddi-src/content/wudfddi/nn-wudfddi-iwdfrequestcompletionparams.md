---
UID: NN:wudfddi.IWDFRequestCompletionParams
title: IWDFRequestCompletionParams
author: windows-driver-content
description: The IWDFRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or an asynchronous I/O operation completes.
old-location: wdf\iwdfrequestcompletionparams.htm
old-project: wdf
ms.assetid: f297c6e0-927a-4fb3-bab4-00fdd610a684
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.iwdfrequestcompletionparams, IWDFRequestCompletionParams interface, IWDFRequestCompletionParams interface, described, IWDFRequestCompletionParams, wudfddi/IWDFRequestCompletionParams, UMDFRequestObjectRef_746528f7-b23f-4907-8661-e228fa99df1c.xml, umdf.iwdfrequestcompletionparams
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
-	IWDFRequestCompletionParams
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFRequestCompletionParams interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFRequestCompletionParams</b> interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or an asynchronous I/O operation completes.

## Methods

<p>The <b>IWDFRequestCompletionParams</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFRequestCompletionParams.GetCompletedRequestType](nf-wudfddi-iwdfrequestcompletionparams-getcompletedrequesttype.md) | The GetCompletedRequestType method retrieves the type of operation that the request to be completed contains. |
| [wudfddi.IWDFRequestCompletionParams.GetCompletionStatus](nf-wudfddi-iwdfrequestcompletionparams-getcompletionstatus.md) | The GetCompletionStatus method retrieves the completion status of an I/O request. |
| [wudfddi.IWDFRequestCompletionParams.GetInformation](nf-wudfddi-iwdfrequestcompletionparams-getinformation.md) | The GetInformation method retrieves information that is associated with the completion of an I/O request. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |