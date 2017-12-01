---
UID: NF.wudfddi.IDriverEntry.OnInitialize
title: IDriverEntry::OnInitialize
author: windows-driver-content
description: The OnInitialize method performs any operations that are necessary to initialize a driver.
old-location: wdf\idriverentry_oninitialize.htm
old-project: wdf
ms.assetid: c676588e-348b-4840-9873-6b1bb2454987
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IDriverEntry, OnInitialize, IDriverEntry::OnInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDriverEntry.OnInitialize
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IDriverEntry
req.product: Windows 10 or later.
---

# IDriverEntry::OnInitialize method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnInitialize</b> method performs any operations that are necessary to initialize a driver.</p>


## -syntax

````
HRESULT OnInitialize(
  [in] IWDFDriver *pWdfDriver
);
````


## -parameters
<dl>

### -param <i>pWdfDriver</i> [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfdriver.md">IWDFDriver</a> interface for the framework driver object that represents the driver that is loaded in the host process.</p>
</dd>
</dl>

## -returns
<p><b>OnInitialize</b> returns S_OK if the driver completed its global initialization. Otherwise, this method returns one of the error codes that are defined in Winerror.h. If the driver returns an error code, the framework will not load the driver.</p>

## -remarks
<p>The framework creates a new driver object for each driver that is loaded in the driver host process. When a driver enters the system, the framework calls <b>OnInitialize</b> to notify the driver and passes the <a href="..\wudfddi\nn-wudfddi-iwdfdriver.md">IWDFDriver</a> interface in the call. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-idriverentry.md">IDriverEntry</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfdriver.md">IWDFDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IDriverEntry::OnInitialize method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
