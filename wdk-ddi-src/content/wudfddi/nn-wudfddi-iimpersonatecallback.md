---
UID: NN:wudfddi.IImpersonateCallback
title: IImpersonateCallback
author: windows-driver-content
description: The IImpersonateCallback interface contains a method that handles impersonation.
old-location: wdf\iimpersonatecallback.htm
old-project: wdf
ms.assetid: 811cb070-9cbe-4906-9db0-ee8316cc18c9
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IImpersonateCallback, IImpersonateCallback interface, IImpersonateCallback interface, described, UMDFRequestObjectRef_a92c4df0-b16b-4fc0-b858-4b2cdd59c3b2.xml, umdf.iimpersonatecallback, wdf.iimpersonatecallback, wudfddi/IImpersonateCallback
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
req.lib: 
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
-	IImpersonateCallback
product:
- Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IImpersonateCallback interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IImpersonateCallback</b> interface contains a method that handles impersonation.

A driver registers the <b>IImpersonateCallback</b> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a> method.

## Methods

<p>The <b>IImpersonateCallback</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IImpersonateCallback::OnImpersonate](nf-wudfddi-iimpersonatecallback-onimpersonate.md) | The OnImpersonate method handles impersonation. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfddi.h |